from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()
model = ChatOpenAI(model_name="gpt-4", temperature=0)

st.title("Prompt Template Example")
st.header("Using PromptTemplate and load_prompt with LangChain")

prompt_input = st.text_input("Enter a topic for the prompt: e.g Artificial Intelligence, Climate Change, Space Exploration")
style_input = st.text_input("Enter a writing style: e.g Formal, Casual, Humorous")
length_input = st.number_input("Enter desired length (in words):", min_value=50, max_value=1000, value=200)

template = load_prompt("tempalate.json")


if st.button("Generate Prompt"):
    chain = template | model
    result = chain.invoke({
        "prompt_input": prompt_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(result.content)
