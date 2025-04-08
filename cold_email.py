
import streamlit as st
from text import Chain
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text

def create_streamlit(llm, clean_text):
    st.title("Email Generator LEMONWEE")
    url_input = st.text_input("Enter a URL:", value = "https://careers.tiktok.com/position/6865207344658204941/detail")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            jobs = llm.extract_jobs(data)
            for job in jobs:
                email = llm.write_email(job)
                st.code(email, language = "markdown")
        

        except Exception as e:
            st.error("An error occur")

if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout = "wide", page_title= "Cold Email ")
    create_streamlit(chain, clean_text)

 