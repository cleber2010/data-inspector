import streamlit as st
import pandas as pd
from etl.validation import DatasetModel
from etl.transform import basic_statistics

st.set_page_config(page_title="Data Inspector", layout="wide")
st.title("📊 Data Inspector – ETL & Dashboard Interativo")


uploaded_file = st.file_uploader("Faça upload do seu arquivo CSV", type=["csv"])

if uploaded_file:
    try:

        df = pd.read_csv(uploaded_file)

        DatasetModel(data=df)
        DatasetModel.validate_not_empty(df)

        st.success("✅ CSV carregado e validado com sucesso!")
        st.subheader("Preview do DataFrame")
        st.dataframe(df.head(10))

        stats = basic_statistics(df)
        st.subheader("📈 Estatísticas Básicas")
        for col, col_stats in stats.items():
            st.markdown(f"**Coluna: {col}**")
            st.json(col_stats)


    except Exception as e:
        st.error(f"❌ Ocorreu um erro: {e}")

else:
    st.info("⏳ Aguarde ou faça upload de um CSV para começar.")
