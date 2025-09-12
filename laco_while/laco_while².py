import streamlit as st

st.title("Laço de Repetição While")

nota = st.number_input("Digite uma nota", step=1)

if st.button("Verificar"):
    if nota < 0 or nota > 10:
        st.error("Nota inválida! Digite uma nota entre 0 e 10.")
    else:
        st.info("Nota válida!")