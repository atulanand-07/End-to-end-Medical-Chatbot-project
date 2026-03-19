from langchain_core.retrievers import BaseRetriever


def get_retriever(vectorstore):
    """
    Basic retriever (used before reranking)
    Fetches more documents so reranker can filter best ones
    """

    retriever = vectorstore.as_retriever(
        search_type="similarity",   # cosine similarity
        search_kwargs={
            "k": 10   # fetch more → reranker will pick top 3
        }
    )

    return retriever