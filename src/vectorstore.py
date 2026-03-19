from langchain_pinecone import PineconeVectorStore
from config import INDEX_NAME


def create_vectorstore(docs, embeddings):
    """
    Used in ingest.py (run once)
    Creates and uploads embeddings to Pinecone
    """
    return PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index_name=INDEX_NAME
    )


def load_vectorstore(embeddings):
    """
    Used in app.py (runtime)
    Loads existing Pinecone index
    """
    return PineconeVectorStore.from_existing_index(
        index_name=INDEX_NAME,
        embedding=embeddings
    )