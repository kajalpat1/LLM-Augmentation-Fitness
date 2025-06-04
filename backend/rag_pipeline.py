import os

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub

from routines import generate_routine 

def get_workout_response(query: str, goal: str = None, level: str = None):
   
    if goal and level:
        return generate_routine(goal, level)

    hf_model = os.getenv("HUGGINGFACE_EMB_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    embedder = HuggingFaceEmbeddings(model_name=hf_model)

    vectordb = FAISS.load_local("faiss_index", embedder)

    llm = HuggingFaceHub(
    repo_id="google/flan-t5-small", #need free to work
    model_kwargs={"temperature":0, "max_length":256}
)  


    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=False,
    )

    return qa.run(query)
