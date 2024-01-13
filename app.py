from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st 
import os

import  google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro")

# function to load gemini pro model and get response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# initialize our streamlit app
st.set_page_config(page_title="Q&A")
st.header("Question Answer Gemini LLM Application")
input=st.text_input("Ask the question ",key="input")
submit = st.button("Submit")


# When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("Generated Response ")
    st.write(response)