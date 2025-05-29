import os
import glob
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

def create_vector_store():
    paths = glob.glob("data/workouts/**/*.txt", recursive=True)
    if not paths:
        raise RuntimeError("No txt files found under data/workouts")

    docs = []
    for path in paths:
        loader = TextLoader(path)
        docs.extend(loader.load())

    splitter = CharacterTextSplitter(chunk_size=1200, chunk_overlap=200)
    docs_split = splitter.split_documents(docs)

    print(f" Found {len(docs)} docs, split into {len(docs_split)} chunks")

    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Missing OPENAI_API_KEY in environment")

    embeddings = OpenAIEmbeddings(openai_api_key=key)

    vectordb = FAISS.from_documents(docs_split, embeddings)
    vectordb.save_local("faiss_index")
    print("Saved FAISS index to ./faiss_index")

if __name__ == "__main__":
    create_vector_store()




