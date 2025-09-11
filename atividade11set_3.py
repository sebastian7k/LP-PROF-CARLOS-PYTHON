#Escreva um algoritimo que solicite ao usuario 5 valores inteiros
#e no final os mostre  quantos numeros sao pares e quantos numeros sao impares

import streamlit as st
st.title("Contagem de Números Pares e Ímpares")
st.header("Digite 5 números inteiros")

pares = 0
impares = 0
numero1 = st.number_input("Digite um número", step=1)
numero2 = st.number_input("Digite um número", step=1)
numero3 = st.number_input("Digite um número", step=1)
numero4 = st.number_input("Digite um número", step=1)
numero5 = st.number_input("Digite um número", step=1)
if st.button("Contar Pares e Ímpares"):
    for i in range(1, 6):
        numero = st.number_input(f"Digite o {i}º número", step=1)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    st.success(f"Números pares: {pares}")
    st.success(f"Números ímpares: {impares}")
