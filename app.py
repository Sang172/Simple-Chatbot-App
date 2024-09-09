
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
import os

def get_openai_response(question):
    llm = OpenAI(model_name="gpt-3.5-turbo",temperature=0.5)
    response=llm(question)
    return response


st.set_page_config(page_title='Q&A Demo')

st.header("Langchain Application")


input=st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

if submit:
    st.subheader("Response")
    response = get_openai_response(input)
    st.write(response)

#What are the ten biggest cities in Japan in terms of population?