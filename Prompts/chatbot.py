from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv()

# Initialize model
model = ChatOpenAI(model_name="gpt-4", temperature=0)

# Chat history stored as a Python list of dicts
chat_history = []

print("Start chatting! Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        break

    # Add user message
    chat_history.append({"role": "user", "content": user_input})

    # The model expects message list, NOT DataFrame or DataFrame dict
    response = model.invoke(chat_history)

    # Add assistant reply to history
    ai_reply = response.content
    chat_history.append({"role": "assistant", "content": ai_reply})

    print(f"AI: {ai_reply}")

# -----------------------------
# Save history after exiting
# -----------------------------

# Save as CSV
pd.DataFrame(chat_history).to_csv("chat_history.csv", index=False)

# Save as JSON
with open("chat_history.json", "w") as f:
    json.dump(chat_history, f, indent=4)

print("\nChat history saved as chat_history.csv and chat_history.json")
