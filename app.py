from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st;
import os


os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## PROMPT TEMPLATE
prompt=ChatPromptTemplate(
    [
        ("system","You are a helpful assistant. Please response to he user queries"),
        ("user","Question:{question}")
    ]
)

## STREAMLIT UI
st.title("Langchain demo")
input_text=st.text_input("Search the topic")

## LLM

llm=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response)

    