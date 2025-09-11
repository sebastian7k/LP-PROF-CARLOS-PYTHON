#Escreva um algoritimo que solicite um usuario um numero 
##e mostre a tabuada desse numero##

import streamlit as st
import time

st.title("Algoritimo gerador de tabuada") 
st.header("Tabuada de multiplicação")
num = st.number_input("Digite um numero para ver a tabuada", min_value=1, max_value=100, step=1) 

if st.button("Gerar Tabuada"):
    st.subheader(f"Tabuada do {num}")
    for i in range(1, 11):
        resultado = num * i
        st.info(f"{num} x {i} = {resultado}")
    st.success("FIM")