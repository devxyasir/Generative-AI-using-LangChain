from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0)
chat_history = [
    SystemMessage(content="You are a helpful assistant. Help user to chat with AI."),
]

while True:
    user_input = input("You: ")
    # chat_history.append({"role": "user", "content": user_input})
    chat_history.append(HumanMessage(user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"AI: {response.content}")

print(chat_history)

