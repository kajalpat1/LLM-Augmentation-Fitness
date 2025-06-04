import os
import glob

from dotenv import load_dotenv
#langchain imports
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()  

def create_vector_store():
    paths = glob.glob("data/workouts/**/*.txt", recursive=True)
    if not paths:
        raise RuntimeError("No .txt files found under data/workouts")
    docs = []
    for path in paths:
        loader = TextLoader(path)   
        docs.extend(loader.load())         
    #split text accordingly
    splitter = CharacterTextSplitter(chunk_size=1200, chunk_overlap=200)
    docs_split = splitter.split_documents(docs)

    print(f"Found {len(docs)} source files, split into {len(docs_split)} chunks.")

    #model were using
    hf_model = os.getenv("HUGGINGFACE_EMB_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

    embeddings = HuggingFaceEmbeddings(model_name=hf_model)

    vectordb = FAISS.from_documents(docs_split, embeddings)

    vectordb.save_local("faiss_index")
    print("Saved FAISS index to ./faiss_index")


if __name__ == "__main__":
    create_vector_store()




