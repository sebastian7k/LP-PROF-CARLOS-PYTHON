#escrever um algoritimo que solicite au usuario um numero e faça a contagem regressiva  apartir do numero
# informado ate o numero 1  agauardando 1 segundo entre cada numero exibido na tela

import streamlit as st
import time

st.title("Contagem Regressiva")
st.header("Digite um numero para inicair a contagem regressiva")

numero = st.number_input("Digite um numero", min_value=1, step=1)
if st.button("INICIAR"):
    for i in range(numero, 0, -1):
        st.info(i)
        time.sleep(1)
    st.write("Contagem regressiva finalizada!")
    st.snow()
    st.balloons()  
      # Embed do vídeo do YouTube para tocar áudio
    st.markdown("""
    <iframe width="300" height="80" 
        src="https://www.youtube.com/embed/Hv3st70Rmpk?autoplay=1&controls=1" 
        frameborder="0" 
        allow="autoplay; encrypted-media" 
        allowfullscreen>
    </iframe>
    """, unsafe_allow_html=True)
    st.success("Contagem regressiva finalizada!")