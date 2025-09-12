#Escreva um algoritimo que mostr
#os numeros impars de 1 a 20

import streamlit as st
import time 

st.error("Algoritimo gerador numeros impares")
st.header("Contagem de numeros impares")

if st.button("Iniciar"):
    for i in range(1, 21):
        if i % 2 != 0:
            st.info(i)
            time.sleep(1)
    st.success("FIM")

