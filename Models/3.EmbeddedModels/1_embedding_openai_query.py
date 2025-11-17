from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

text = "The quick brown fox jumps over the lazy dog"

restult = embeddings.embed_query(text)

print(restult)