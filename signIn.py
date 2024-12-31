import streamlit as st

st.header("Welcome to D's new Website")
st.subheader("Sign In")

st.text_input("Username")
st.text_input("Password", type='password')
st.button("Sign in")