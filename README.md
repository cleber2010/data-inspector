# 📊 Data Inspector – ETL & Dashboard Interativo

Data Inspector é uma aplicação interativa que permite fazer upload de arquivos CSV e realizar análise exploratória de dados (EDA) de forma automática.  
Ele valida os dados, calcula estatísticas descritivas.

---

## 🔹 Funcionalidades

- Upload de arquivos CSV diretamente na interface web.
- Validação básica do dataset:
  - Dataset não vazio
  - Contagem de valores nulos e duplicados
- Estatísticas descritivas automáticas:
  - Média, mediana, mínimo, máximo, desvio padrão
  - Contagem de valores únicos
- Interface simples e intuitiva via **Streamlit**

---

## 🔹 Tecnologias Utilizadas

| Tecnologia | Função |
|------------|-------|
| Python     | Linguagem principal |
| Pandas     | Leitura e manipulação de dados |
| Streamlit  | Interface web interativa |
| FPDF       | Geração de relatórios PDF |
| NumPy      | Cálculos estatísticos |
| Pydantic   | Validação de dados |

---

## 🔹 Como Rodar Localmente

1. Clonar o repositório:

```bash
git clone https://github.com/cleber2010/data-inspector.git
cd data-inspector

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
