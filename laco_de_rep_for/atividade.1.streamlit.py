import streamlit as st

#Escreva um algoritmo que leia três notas de um aluno.
#Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o 
# aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios: 
#Se a média for a partir de 7, aprovado; 
#Se a média for entre 5 e 6,9, o aluno está em recuperação; 
#Caso seja menor que 5, o aluno está reprovado.


st.title("Notas")

notas = []

for i in range (1, 4):
      nota = st.number_input(f"Digite sua nota {i}:", min_value=0.0, max_value=10.0, step=0.1)
      notas.append(nota)
if st.button("Verificar Notas"):
    media = sum(notas) / len(notas)

    st.write(f"Sua média é : {media:.2f}")

    if  media >= 7:
        st.success("Aprovado")
    elif 5 <= media< 7 :
        st.warning("Recuperação")
    else:
        st.error("Reprovado")
