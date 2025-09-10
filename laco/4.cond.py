import streamlit as st
st.title("acesso condicional")

idade = st.number_input("Digite sua idade", min_value=0, max_value=120, step=1)
if st.button("verificar idade") :
   if idade >= 18 :
       st.write("você é maior de idade")
   else :
         st.write("você é menor de idade")

else :
    st.write("clique no botão para verificar sua idade")