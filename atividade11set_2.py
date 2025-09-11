#escrever um progama que sol que solicite do 
# usuario 5 numeros inteiros e ao final
# apresente a soma de todos numeros lidos

import streamlit as st
st.title("Soma de Números Inteiros")
st.header("Digite 5 números inteiros")
soma = 0
if st.button("Calcular Soma"):
    for i in range(1, 6):
        numero = st.number_input(f"Digite o {i}º número", step=1)
        soma += numero
    st.success(f"A soma dos números digitados é: {soma}")
    st.balloons()
        