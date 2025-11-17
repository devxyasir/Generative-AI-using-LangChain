from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be, that is the question"
]

results = embeddings.embed_documents(documents)
for i, doc in enumerate(documents):
    print(f"Document: {doc}\nEmbedding: {results[i]}\n")

