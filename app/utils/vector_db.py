from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_vector_store():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local(
    "vector_store/faiss_index" ,
    embedding_model,
    allow_dangerous_deserialization=True
    )
    return vector_store

