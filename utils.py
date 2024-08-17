import streamlit as st

def load_api_key():
    api_key = st.text_input("Enter apikey", placeholder="Enter OpenAI Key", type="password")
    return api_key

def validate_inputs(pdfs, api_key, question):
    if not api_key:
        st.error("API key is required.")
        return False
    if not pdfs:
        st.error("Please upload at least one PDF file.")
        return False
    if not question:
        st.error("Please enter a question.")
        return False
    return True
