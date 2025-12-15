# 📊 Automação de Relatórios por Guia e Proprietário

Este projeto é uma aplicação em **Python + Streamlit** que permite filtrar clientes por **Guias** e gerar relatórios em **PDF** organizados por **Proprietário**.  
O objetivo é automatizar tarefas repetitivas de análise e exportação de dados, garantindo eficiência e padronização dos relatórios.

---

## 🚀 Funcionalidades

- Upload e leitura de planilhas Excel com dados de clientes e guias.  
- Seleção interativa dos **Guias da Semana** via interface Streamlit.  
- Visualização dos clientes vinculados aos guias selecionados em tabela dinâmica.  
- Geração automática de **PDFs individuais por Proprietário**, contendo:  
  - Coligador  
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

## 📂 Estrutura do projeto
├── data/ # Planilhas de entrada (exemplo fictício) │ 
└── data - guias ficticios.xlsx 
├── PDFs_por_proprietario/ # Saída dos relatórios gerados 
├── app.py # Código principal da aplicação 
├── requirements.txt # Dependências do projeto 
└── README.md # Documentação
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

👉 Esse README já está pronto para subir junto com seu código. Ele mostra claramente o **propósito**, **funcionalidades**, **instalação** e **uso**.  


