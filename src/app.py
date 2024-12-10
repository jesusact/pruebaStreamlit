import streamlit as st

st.title("Hello world from Streamlit!")

st.write("Esta es una aplicación de prueba que usa Streamlit.")

firstNumber = st.number_input("Introduce el primer número")

secondNumber = st.number_input("Introduce el segundo número")

st.write("La suma es: ", (firstNumber + secondNumber))

