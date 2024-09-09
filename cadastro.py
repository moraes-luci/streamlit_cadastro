import streamlit as st
import pandas as pd
from os import path
from datetime import datetime


st.set_page_config(page_icon="📕")

file_path = "acidentes.csv"
header = ["data", "hora", "municipio", "causa", "tipo"]

# Função para efetuar o cadastro


def cadastrar(data, hora, municipio, causa, tipo):
    if municipio and causa and tipo:
        data_formatada = data.strftime("%d/%m/%Y")
        hora_formatada = hora.strftime("%H:%M:%S")

        # Verificar se o arquivo existe
        if not path.exists(file_path):
            # Criar um DataFrame com o cabeçalho
            df = pd.DataFrame(columns=header)
            # Salvar o DataFrame em um arquivo CSV
            df.to_csv(file_path, index=False)

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{data_formatada}, {hora_formatada}, {
                       municipio}, {causa}, {tipo}\n")
            st.session_state["cadastro"] = True
    else:
        st.session_state["cadastro"] = False


# Campos do sistema
st.title("Cadastro de acidentes")
data = st.date_input("Data do acidente", format=('DD/MM/YYYY'))
hora = st.time_input("Hora")
municipio = st.text_input("Município")
causa = st.text_input("Causa")
tipo = st.text_input("Tipo")


# Botão para cadastro
btn_cadastrar = st.button("Cadastrar", on_click=cadastrar, args=(
    data, hora, municipio, causa, tipo))

if btn_cadastrar:
    if st.session_state["cadastro"] == True:
        st.success("Cadastrado com sucesso.")
    else:
        st.error("Erro ao cadastrar, revise os dados.")
