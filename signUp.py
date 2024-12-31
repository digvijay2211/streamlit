import streamlit as st

st.header("Welcome to D's Website")
st.subheader("Sign Up")

st.text_input("Enter Your Name")
st.text_input("Enter New Username")
st.text_input("Enter Mobile Number")
st.text_input("Enter New Password", type='password')
st.button("Sign Up")