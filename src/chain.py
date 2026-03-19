from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from src.llm import get_llm
from src.prompt import get_prompt
from src.reranker import Reranker
from src.confidence import check_confidence, LOW_CONFIDENCE
import json

def get_chain(retriever):

    llm = get_llm()
    prompt = get_prompt()
    reranker = Reranker()

    # Retrieve documents
    def retrieve(x):
        try:
            docs = retriever.invoke(x["question"])
        except Exception as e:
            print("Retriever error:", e)
            docs = []

        return {**x, "docs": docs}

    # Confidence check
    def confidence(x):
        if not check_confidence(x["docs"]):
            return {**x, "answer": LOW_CONFIDENCE}
        return x

    # Rerank docs
    def rerank(x):
        if "answer" in x:
            return x

        top_docs = reranker.rerank(
            x["question"],
            x["docs"],
            top_k=3
        )

        context = "\n\n".join([d.page_content for d in top_docs])

        return {**x, "context": context}



    def generate(x):
        if "answer" in x:
            return x

        context = x.get("context", "")

        if not context:
            return {
                **x,
                "answer": {
                    "topic": "",
                    "category": "",
                    "answer": "Not present in the provided medical context."
                }
            }

        raw = (prompt | llm | StrOutputParser()).invoke({
            "question": x["question"],
            "context": context
        })

        try:
            parsed = json.loads(raw)
        except:
            parsed = {
                "topic": "Unknown",
                "category": "Unknown",
                "answer": raw
            }

        return {**x, "answer": parsed}

    # Final output
    def output(x):
        return x["answer"]

    # PIPELINE
    chain = (
        RunnablePassthrough()
        | RunnableLambda(retrieve)
        | RunnableLambda(confidence)
        | RunnableLambda(rerank)
        | RunnableLambda(generate)
        | RunnableLambda(output)
    )

    return chain