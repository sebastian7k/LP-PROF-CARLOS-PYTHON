import streamlit as st

# Inicialização do estado de sessão
if 'notas' not in st.session_state:
    st.session_state.notas = [0.0, 0.0, 0.0]  # Inicializa com 3 notas

st.title("Notas")
#st.header("Calculadora de notas")

# Entradas de notas
for i in range(3):  # Definindo um número fixo de entradas
    st.session_state.notas[i] = st.number_input(f"Digite sua nota {i+1}:", 
                                                min_value=0.0, 
                                                max_value=10.0, 
                                                step=0.1, 
                                                value=st.session_state.notas[i])

if st.button("Verificar Notas"):
    media = sum(st.session_state.notas) / len(st.session_state.notas)
    st.write(f"Sua média é: {media:.2f}")

    if media >= 7:
        st.success("Aprovado")
    elif 5 <= media < 7:
        st.warning("Recuperação")
    else:
        st.error("Reprovado")