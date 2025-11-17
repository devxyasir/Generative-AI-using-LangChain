from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.7)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate the following English text to French: 'Hello, how are you?'")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)