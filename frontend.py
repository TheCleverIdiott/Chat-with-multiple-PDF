import streamlit as st
from backend import comp_process


def frontend():
    # Streamlit UI
    st.set_page_config(page_title="Chat with multiple pdf files", layout="wide")
    st.title("Hehe hehe")
    question = st.text_input("Ask Question Below: ")

    with st.sidebar:
        api_key = st.text_input("Enter apikey", placeholder="Enter OpenAI Key", type="password")

        st.subheader("Upload PDFs here")
        pdfs = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

        if st.button('Process'):
            if pdfs and api_key:
                with st.spinner('Processing...'):
                    ans = comp_process(apikey=api_key, pdfs=pdfs, question=question)
                    st.write(ans)
            else:
                st.error("Please upload PDFs and enter an API key.")

if __name__ == "__main__":
    frontend()
