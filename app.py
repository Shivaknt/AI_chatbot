import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("Hamsi Marketing Q&A Chatbot")



question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])