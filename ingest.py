from src.loader import load_pdf
from src.splitter import split_text
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore

print("Loading documents...")
docs = load_pdf("data/")

print("Splitting documents...")
chunks = split_text(docs)

print("Creating embeddings...")
embeddings = get_embeddings()

print("Uploading to Pinecone...")
create_vectorstore(chunks, embeddings)

print("✅ Index created successfully!")