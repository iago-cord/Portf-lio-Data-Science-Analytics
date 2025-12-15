# 📊 Automação de Relatórios por Guia e Proprietário

Este projeto é uma aplicação em **Python + Streamlit** que permite filtrar clientes por **Guias** e gerar relatórios em **PDF** organizados por **Proprietário**.  
O objetivo é automatizar tarefas repetitivas de análise e exportação de dados, garantindo eficiência e padronização dos relatórios.


## 🎯 Contexto e Motivação

Toda semana um grupo de guias comparecia à empresa com clientes antigos e novos. Como os guias mudavam semanalmente, era necessário gerar listas personalizadas para cada consultora, contendo os clientes vinculados aos guias confirmados naquela semana. Essas listas eram usadas para que as consultoras entrassem em contato com os clientes, oferecendo produtos e informando que o guia estava presente e poderia levar a mercadoria.

O processo manual levava cerca de **2 horas** para ser concluído.  
Com este projeto em **Python + Streamlit**, o tempo caiu para **2 minutos**, graças à automação que:
- Permite selecionar os guias confirmados via interface.  
- Gera automaticamente arquivos **PDF** com os clientes de cada consultora.  
- Padroniza e organiza as informações de forma prática e acessível.
---

## 🚀 Funcionalidades

- Upload e leitura de planilhas Excel com dados de clientes e guias.  
- Seleção interativa dos **Guias da Semana** via interface Streamlit.  
- Visualização dos clientes vinculados aos guias selecionados em tabela dinâmica.  
- Geração automática de **PDFs individuais por Proprietário**, contendo:  
  - Código  
  - Nome  
  - Proprietário  
  - Guia  
  - Limite disponível (formatado em R$)  
  - Ticket Médio dos últimos 12 meses (formatado em R$)  
- Layout dos PDFs em modo **paisagem**, com tabela estilizada e cabeçalho destacado.

---

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)  
- [Pandas](https://pandas.pydata.org/) – manipulação de dados  
- [Streamlit](https://streamlit.io/) – interface web interativa  
- [ReportLab](https://www.reportlab.com/) – geração de PDFs com tabelas  
- [FPDF](https://pyfpdf.readthedocs.io/) – suporte adicional para PDFs  
- [OS](https://docs.python.org/3/library/os.html) – manipulação de diretórios  

---

## ⚙️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
pip install -r requirements.txt

▶️ Como usar
Coloque sua planilha Excel na pasta data/.

Execute o aplicativo Streamlit:
streamlit run app.py
Na interface:

Selecione os Guias da Semana.

Visualize os clientes filtrados.

Clique em Gerar PDFs por Proprietário.

Os relatórios serão salvos automaticamente na pasta PDFs_por_proprietario/

📌 Exemplo de saída
Cada PDF contém uma tabela formatada com os dados do respectivo proprietário, em modo paisagem, com colunas ajustadas proporcionalmente.

📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.

✨ Autor
Eder Iago Cordeiro de Amorim

LinkedIn - 
---



