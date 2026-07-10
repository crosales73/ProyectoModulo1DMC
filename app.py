import streamlit as st
st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

valor_inicial = st.number_imput("ingrese el valor inicial", value = 0)
valor_final = st.number_imput("ingrese el valor final", value = 1)

lista_numerica = list(range(valor_inicial,valor_final))
