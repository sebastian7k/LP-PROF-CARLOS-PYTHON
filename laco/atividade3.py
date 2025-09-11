#escrevendo um algoritimo que mostra os 
#numeros  pares entre 100 e 120

import streamlit as st
import time
st.title("Algoritimo gerando números pares")
st.header("Contagem de números pares")


if st.button("Iniciar"):
    for i in range(100, 121):
        if i % 2 == 0:
            st.info(i)
            time.sleep(1)

    st.header("FIM")
