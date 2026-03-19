import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_HOST = os.getenv("PINECONE_HOST")

INDEX_NAME = os.getenv("INDEX_NAME", "medical-chatbot")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "qwen/qwen-2.5-7b-instruct"
TEMPERATURE = 0.2
