import requests
import json
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time
import logging
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGS = ROOT/"logs"
DATA = ROOT/"data"
LOGS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS/'bcb_coleta.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

def retry_request(url, params, tentativas=3, espera=2, contexto = None):
    
    for tentativa in range (1, tentativas + 1):
        
        try:
            logger.info(f"{contexto} | Iniciando Requisição")
            response = requests.get(url, params=params, timeout=30)
            
            response.raise_for_status()
            
            data = response.json()
            
            if not data:
                raise RuntimeError(
                    f"A resposta da API esta vazia para o periodo "
                    f"{params['dataInicial']} ate {params['dataFinal']}"
                )
            else:
                logger.info(f"{contexto} | Requisição concluida | {len(data)} registros retornados")
                return data
            
        except requests.exceptions.RequestException as erro_temporario:
            
            erros = [429,500,502,503,504]
            
            status_code = (erro_temporario.response.status_code
                           if erro_temporario.response is not None
                           else None)
            
            retry = status_code is None or status_code in erros
           
            if not retry or tentativa == tentativas:
                
                logger.error(f"{contexto} | Falha definitiva após "
                             f"{tentativa} tentativas | status={status_code}")
                
                raise RuntimeError(
                    f"Falha após {tentativa} tentativas ao acessar {url}: "
                    f"(status code: {status_code}) {erro_temporario}"
                ) from erro_temporario
            
            espera_atual = espera * (2 ** (tentativa-1))
            
            logger.warning(
                f"{contexto} | Tentativa {tentativa}/{tentativas} "
                f"falhou | status={status_code} | "
                f"aguardando={espera_atual}s"
            )
            
            time.sleep(espera_atual)
             
def buscar_serie_diaria(serie, dt_inicio, dt_final):
    
    max_intervalo = 10
    
    resultado = []
    
    while dt_inicio <= dt_final :
    
        fim = date(dt_inicio.year + (max_intervalo -1 ), dt_inicio.month, dt_inicio.day)
        
        if fim > dt_final: fim = dt_final
        
        url = (
            f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados'
        )
        
        params = {
            "formato": "json",
            "dataInicial": dt_inicio.strftime("%d/%m/%Y"),
            "dataFinal": fim.strftime("%d/%m/%Y")
        }
        
        try:
            logger.info(f"Série {serie} | Coletando Periodo {dt_inicio} até {fim}")
            dados = retry_request(url, params=params,contexto=f"Série {serie} | {dt_inicio} até {fim}")
            
            resultado.extend(dados)
            logger.info(f"Série {serie} | Periodo {dt_inicio} até {fim} concluido | {len(dados)} registros")
            
        except RuntimeError as erro:
            raise RuntimeError(
                f"Erro ao buscar série {serie} "
                f"no periodo {dt_inicio} até {fim}: {erro}"
            ) from erro
        
        dt_inicio = fim + timedelta(days=1)
        
    logger.info(f"Série {serie} | Coleta concluida | Total: {len(resultado)} registros")
    return resultado


def buscar_serie_mensal(serie, dt_inicio, dt_final):
    
    max_intervalo = 10
    
    resultado = []
    
    while dt_inicio <= dt_final :
    
        fim = date(dt_inicio.year + (max_intervalo -1 ), dt_inicio.month, dt_inicio.day)
        
        if fim > dt_final: fim = dt_final
        
        url = (
            f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados'
        )
        
        params = {
            "formato": "json",
            "dataInicial": dt_inicio.strftime("%d/%m/%Y"),
            "dataFinal": fim.strftime("%d/%m/%Y")
        }
        
        try:
            logger.info(f"Série {serie} | Coletando Periodo {dt_inicio} até {fim}")
            dados = retry_request(url, params=params,contexto=f"Série {serie} | {dt_inicio} até {fim}")
                    
            resultado.extend(dados)
            logger.info(f"Série {serie} | Periodo {dt_inicio} até {fim} concluido | {len(dados)} registros")
                    
        except RuntimeError as erro:
            raise RuntimeError(
                    f"Erro ao buscar série {serie} "
                    f"no periodo {dt_inicio} até {fim}: {erro}"
                    ) from erro
                
        dt_inicio = fim + relativedelta(months=1)
    
    logger.info(f"Série {serie} | Coleta concluida | Total: {len(resultado)} registros")
    return resultado
  
def salvar_json (nome_arquivo, dados):
    caminho = DATA/f'{nome_arquivo}.json'
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)