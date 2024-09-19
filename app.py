
import streamlit as st
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {e}"

st.set_page_config(page_title='Q&A Demo')

st.header("Langchain Application")


input=st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

if submit:
    st.subheader("Response")
    response = get_openai_response(input)
    st.write(response)

#What are the ten biggest cities in Japan in terms of population?