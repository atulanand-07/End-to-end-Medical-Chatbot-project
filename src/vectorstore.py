from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from config import INDEX_NAME, PINECONE_API_KEY


# Initialize Pinecone client (NEW SDK way)
pc = Pinecone(api_key=PINECONE_API_KEY)


def create_vectorstore(docs, embeddings):
    """
    Used in ingest.py (run once)
    Creates and uploads embeddings to Pinecone
    """
    index = pc.Index(INDEX_NAME)

    return PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index=index
    )


def load_vectorstore(embeddings):
    """
    Used in app.py (runtime)
    Loads existing Pinecone index
    """
    index = pc.Index(INDEX_NAME)

    return PineconeVectorStore(
        index=index,
        embedding=embeddings
    )