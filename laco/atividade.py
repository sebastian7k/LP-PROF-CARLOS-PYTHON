import streamlit as st
st.title(" Verificação de media")


not1 = st.number_input("Digite a primeira nota", min_value=0.0, max_value=10.0, step=0.1)
not2 = st.number_input("Digite a segunda nota", min_value=0.0, max_value=10.0, step=0.1)
media = (not1 + not2) / 2

if st.button("verificar media") :
    if media >= 7.0 :
        st.success(f"Sua média é {media:.2f}. Você foi aprovado!")
    else :
          st.error(f"Sua média é {media:.2f}. Você foi reprovado.")
else :
    st.write("Clique no botão para verificar sua média")    