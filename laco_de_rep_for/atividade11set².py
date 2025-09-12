#escreva um progama de computador que solicite do usuario 4 notas 
# e no final apresenta a media aritmetica das notas

import streamlit as st
st.title("Cálculo da Média")

numero1 = st.number_input("Digite o 1º número", step=1, key="numero1")
numero2 = st.number_input("Digite o 2º número", step=1, key="numero2")
numero3 = st.number_input("Digite o 3º número", step=1, key="numero3")
numero4 = st.number_input("Digite o 4º número", step=1, key="numero4")

soma = numero1 + numero2 + numero3 + numero4
media = soma / 5

if st.button("Caucular Média"):
    st.success(f"A Média Aritmética é: {media}")
else:
    st.warning(f"Reprovado : {media}")
    
