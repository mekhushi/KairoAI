from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader

class KairoRetriever:
    def __init__(self, persist_dir="db"):
        self.persist_dir = persist_dir
        self.embeddings = OpenAIEmbeddings()
        self.db = None

    def load_docs(self, file_path):
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path)

        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = splitter.split_documents(docs)

        self.db = Chroma.from_documents(texts, self.embeddings, persist_directory=self.persist_dir)
        self.db.persist()
