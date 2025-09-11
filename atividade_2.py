import streamlit as st

st.title("Gerador da Tabuada")

num = st.number_input("Digite um número para ver a tabuada", min_value=1, max_value=100, step=1)

tabuada = [f"{num} x {i} = {num * i}" for i in range(1, 11)]

st.write("\n".join(tabuada))