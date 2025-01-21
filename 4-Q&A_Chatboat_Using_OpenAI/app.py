import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ['LANGSMITH_API_KEY'] = os.getenv("LANGSMITH_API_KEY")
os.environ['LANGSMITH_TRACING'] = "true"
os.environ['LANGSMITH_PROJECT'] = "Build Chatbot Using OpenAI"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the queries of the user."),
        ("user", "Question:{question}")
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    # Set the API key directly in the client initialization
    llm_instance = ChatOpenAI(
        model=llm,
        openai_api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
    output_parser = StrOutputParser()
    chain = prompt | llm_instance | output_parser
    answer = chain.invoke({'question': question})
    return answer


# Streamlit App
st.title("Q&A Chatbot Using OpenAI")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password")

llm = st.sidebar.selectbox("Select an OpenAI Model", ["gpt-4", "gpt-3.5-turbo", "gpt-4-turbo"])

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Type your question")
user_input = st.text_input("You:")

if user_input:
    if not api_key:
        st.error("Please enter a valid OpenAI API Key!")
    else:
        try:
            response = generate_response(user_input, api_key, llm, temperature, max_tokens)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.write("Please provide the query.")
