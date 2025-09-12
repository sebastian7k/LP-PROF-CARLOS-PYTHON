#escreva um algoritimo que solicite ao usuario 2 notas 
#caso seja menor que 0 ou maior que 10 mostre pergunta novamente
#caso contrario apresente a media das notas

import streamlit as st
st.title("Cálculo da Média com Validação")

nota1 = st.number_input("Digite a 1º nota", step=1, key="nota1")
nota2 = st.number_input("Digite a 2º nota", step=1, key="nota2")
media = nota1 + nota2 /2

if st.button("Calcular Média"):
    if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
        st.error("Nota inválida! Digite notas entre 0 e 10 ")
    else:
        media = (nota1 + nota2) / 2
        st.success(f"A Média é: {media}")
        if media >= 6:
            st.info("Aprovado")
        else:
            st.error("Reprovado")
st.header("Fim do Programa")