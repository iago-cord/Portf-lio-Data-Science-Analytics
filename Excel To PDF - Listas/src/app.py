import pandas as pd 
import streamlit as st
from fpdf import FPDF
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape
import os


#Lendo o arquivo Excel
df= pd.read_excel(r'C:\Users\eder.amorim\Desktop\Iago\Clientes x Guias\Automatizacao\data - guias ficticios.xlsx')

coligador = df.copy()

#Interface Seleção dos Guias
guias = coligador['Organização - Guia'].dropna().unique()
guias_selecionados = st.multiselect('Selecione os Guias da Semana', sorted(guias))

# Aplicar Filtro dos Guias Selecionados
if guias_selecionados:
    resultado = df[df['Organização - Guia'].isin(guias_selecionados)]
    st.write('Clientes vinculados aos Guias selecionados')
    st.dataframe(resultado, width='stretch')
else:
    st.info('Selecione pelo menos um guia para ver os clientes')

#Gerar Tabela
def gerar_pdf_tabela(df, caminho_arquivo):
    # Página em modo paisagem e sem margens
    doc = SimpleDocTemplate(
        caminho_arquivo,
        pagesize=landscape(A4),
        leftMargin=0,
        rightMargin=0,
        topMargin=0,
        bottomMargin=0
    )

    # Dados da tabela
    dados = [df.columns.tolist()] + df.astype(str).values.tolist()

    # Calcular largura proporcional
    largura_total = 800  # largura útil em pontos para paisagem A4
    comprimentos = [max(len(str(item)) for item in [col] + df[col].astype(str).tolist()) for col in df.columns]
    soma = sum(comprimentos)
    larguras = [(c / soma) * largura_total for c in comprimentos]

    tabela = Table(dados, colWidths=larguras, repeatRows=1)
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
    ]))

    doc.build([tabela])
# Botão para gerar os Pdf's
if st.button("Gerar PDFs por Proprietário"):
    pasta_saida = "PDFs_por_proprietario"
    os.makedirs(pasta_saida, exist_ok=True)

    proprietarios = resultado['Organização - Proprietário'].dropna().unique()

    for prop in proprietarios:
        dados_prop = resultado[resultado['Organização - Proprietário'] == prop].copy()

    # Ajustar colunas e renomear
        colunas_desejadas = [
        'Organização - Coligador',
        'Organização - Nome',
        'Organização - Proprietário',
        'Organização - Guia',
        'Organização - Limite disponível',
        'Organização - Ticket Médio Ult 12 meses'
    ]
        dados_prop = dados_prop[colunas_desejadas]
        dados_prop = dados_prop.rename(columns={
        'Organização - Coligador': 'Coligador',
        'Organização - Nome': 'Nome',
        'Organização - Proprietário': 'Proprietário',
        'Organização - Guia': 'Guia',
        'Organização - Limite disponível': 'Limite disponível',
        'Organização - Ticket Médio Ult 12 meses': 'Ticket Médio (12m)'
    })
        # Ajustes de conteúdo
        dados_prop['Coligador'] = dados_prop['Coligador'].astype(int).astype(str)
        dados_prop['Limite disponível'] = dados_prop['Limite disponível'].apply(lambda x: f"R${x:,.2f}")
        dados_prop['Ticket Médio (12m)'] = dados_prop['Ticket Médio (12m)'].apply(lambda x: f"R${x:,.2f}")

        nome_arquivo = os.path.join(pasta_saida, f"{prop}.pdf")
        gerar_pdf_tabela(dados_prop, nome_arquivo)

    st.success(f"PDFs gerados com sucesso para {len(proprietarios)} proprietários!")
