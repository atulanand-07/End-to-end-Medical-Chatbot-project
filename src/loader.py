from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_pdf(data_path):
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    return loader.load()