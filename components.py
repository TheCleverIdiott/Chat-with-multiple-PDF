import streamlit as st

def sidebar(api_key):
    st.sidebar.header("Configuration")
    st.sidebar.text_input("Enter your OpenAI API key", value=api_key, type="password")

def pdf_uploader():
    st.sidebar.subheader("Upload PDFs")
    return st.sidebar.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
