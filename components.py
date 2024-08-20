import streamlit as st

def sidebar(api_key):
    """Displays the sidebar for configuration settings."""
    st.sidebar.header("Configuration")
    st.sidebar.text_input("Enter your OpenAI API key", value=api_key, type="password")
    
    st.sidebar.subheader("Processing Options")
    processing_speed = st.sidebar.selectbox("Choose processing speed", ["Fast", "Balanced", "Accurate"])
    response_format = st.sidebar.radio("Select response format", ["Summary", "Detailed Analysis", "Key Points"])

    st.sidebar.subheader("Customization")
    theme = st.sidebar.selectbox("Select theme", ["Light", "Dark"])
    show_advanced = st.sidebar.checkbox("Show advanced options")
    
    return processing_speed, response_format, theme, show_advanced

def pdf_uploader():
    """Displays the file uploader in the sidebar."""
    st.sidebar.subheader("Upload PDFs")
    return st.sidebar.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

def advanced_options():
    """Displays advanced options if selected."""
    st.sidebar.subheader("Advanced Options")
    language = st.sidebar.selectbox("Select language", ["English", "Spanish", "French", "German"])
    st.sidebar.slider("Set confidence threshold", min_value=0.0, max_value=1.0, value=0.5)
    return language
