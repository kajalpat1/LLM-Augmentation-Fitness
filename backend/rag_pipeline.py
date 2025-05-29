from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from routines import generate_routine

def get_workout_response(query, goal=None, level=None):
    if goal and level:
        return generate_routine(goal, level)

    vectordb = FAISS.load_local("faiss_index", OpenAIEmbeddings())
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),   
        retriever=vectordb.as_retriever(),
        return_source_documents=False
    )
    return qa.run(query)
