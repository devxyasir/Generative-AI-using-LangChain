from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)
documents = [
    "Life teaches us through contrasts — light through darkness, courage through fear, and wisdom through mistakes",
    "A strong mind learns to find meaning in both success and failure",
    "The mark of a pen lasts longer than the strength of a sword",
    "True strength comes not from comfort but from understanding struggle",
    "Every failure hides a lesson waiting to be discovered"
]

query = "What lesson does the passage teach about finding wisdom and strength through struggle?"
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query) 
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
most_similar_idx = np.argmax(similarities)
print(f"Most similar document:\n{documents[most_similar_idx]}\nSimilarity Score: {similarities[most_similar_idx]}")
print("\nAll similarity scores:")
for i, score in enumerate(similarities):
    print(f"Document {i}: {score}")

# Output:
# Most similar document:    