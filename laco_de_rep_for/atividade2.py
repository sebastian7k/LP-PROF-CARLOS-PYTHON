import streamlit as st
st.title("Algoritimo de Verificaçãod de Números")

n1 = st.number_input("Digite o primeiro numero", step=1)
n2 = st.number_input("Digite o segundo numero", step=1) 

soma = n1 + n2
media = (n1 + n2) / 2
produto = n1 * n2
menor = n1 if n1 < n2 else n2
maior = n1 if n1 > n2 else n2
if st.button("verificar") :
    st.success(f"A Soma é {soma}")
    st.success(f"A Média é {media}")
    st.success(f"O Produto é {produto}")
    if n1 == n2 :
        st.warning("Os numeros são igauis")
    elif n1 != n2 :
        st.success(f"O menor valor é {menor}")
        st.success(f"O maior valor é {maior}")
else :
    st.warning("Clique no botão para verificar os numeros")