from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=1.6)

result = model.invoke("Who was the founder of Pakistan?")

print(result.content)