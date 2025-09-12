#caucular media com laços de repetição for

import streamlit as st

st.title("Cálculo da Média")

soma = 0 
QUANTIDADES_NOTAS = 3


for i in range(QUANTIDADES_NOTAS):
    nota = st.number_input(f"Digite sua {i}º nota")
    soma = soma + nota
media = soma / QUANTIDADES_NOTAS
if st.button("Caucular Média"):
    st.info(f"Média: {media:.1f}")
    if media >=  7 :
        st.success(f"Aprovado : {media}")
    elif media >= 4:  
         st.warning(f"Recuperação : {media}")
    else:
        st.error(f"Reprovado : {media}")
