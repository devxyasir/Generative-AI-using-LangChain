from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model_name="gpt-4", temperature=0.7)

template = PromptTemplate(
    template="You are a helpful Tour Assistant, Greet the user {name} in 6 languages: English, Punjabi(Pakistan), Saraiki, Urdu, German, and Italian.",
    input_variables=["name"],
)

chain = template | model
result = chain.invoke({"name": "Alice"})
print(result.content)
