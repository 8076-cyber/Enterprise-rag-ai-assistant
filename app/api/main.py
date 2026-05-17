from fastapi import FastAPI
from pydantic import BaseModel
from app.utils.vector_db import load_vector_store
from langchain_ollama import OllamaLLM

app = FastAPI()

vectore_store = load_vector_store()

llm = OllamaLLM(model="tinyllama")

class QueryRequest(BaseModel):
    query:str

@app.post("/ask")
def ask_question(request: QueryRequest):
    
    results= vectore_store.similarity_search(request.query, k=2)

    context = "\n" .join([result.page_content for result in results])

    prompt = f"""you are an AI assistant
    Answer only from the provided context.
    context:
    {context}
question:{request.query}
answer:
"""
    response= llm.invoke(prompt)
    return{
        "query": request.query,
        "answer": response
    }


    





