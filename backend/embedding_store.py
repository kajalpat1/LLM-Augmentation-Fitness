from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

def create_vector_store():
    loader = TextLoader("data/workouts", glob="**/*.txt")
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs_split = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(docs_split, embeddings)
    vectordb.save_local("faiss_index")