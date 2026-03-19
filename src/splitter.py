from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

def split_text(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    return splitter.split_documents(docs)