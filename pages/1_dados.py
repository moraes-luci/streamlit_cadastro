import streamlit as st
import pandas as pd

st.set_page_config(page_icon="🧾")

st.header("Dados de acidentes")
st.divider()

try:
    dados = pd.read_csv("acidentes.csv")
    st.dataframe(dados,  hide_index=True)
except FileNotFoundError:
    st.write("Base e dados não encontrada!")
