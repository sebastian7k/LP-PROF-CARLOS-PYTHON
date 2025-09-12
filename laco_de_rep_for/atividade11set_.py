#Escreva um algoritimo que solicite ao usuario 5 valores inteiros
#e no final os mostre  quantos numeros sao pares e quantos numeros sao impares

import streamlit as st

st.title("Contagem de Números Pares e Ímpares")
st.header("Digite 5 números inteiros")

numero1 = st.number_input("Digite o 1º número", step=1, key="numero1")
numero2 = st.number_input("Digite o 2º número", step=1, key="numero2")
numero3 = st.number_input("Digite o 3º número", step=1, key="numero3")
numero4 = st.number_input("Digite o 4º número", step=1, key="numero4")
numero5 = st.number_input("Digite o 5º número", step=1, key="numero5")

pares = 0
impares = 0
if st.button("Contar Pares e Ímpares"):
    numeros = [numero1, numero2, numero3, numero4, numero5]
    
    pares = sum(1 for num in numeros if num % 2 == 0)
    
    impares = sum(1 for num in numeros if num % 2 != 0)
    
    st.success(f"Números pares: {pares}")
    st.success(f"Números ímpares: {impares}")
