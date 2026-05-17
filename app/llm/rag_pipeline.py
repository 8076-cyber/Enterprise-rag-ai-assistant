from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from app.utils.vector_db import load_vector_store

loader = DirectoryLoader(
    "data",
    glob= "*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

vector_store = load_vector_store()

query = input("Ask your question :")

results = vector_store.similarity_search(query, k=2)

context = "\n".join([result.page_content for result in results])

prompt = f""" you are an AI assistance.
Answer the questiononly from the provided context.
If the Answer in not found in the context , 
say:"i could not find the answer in the document.

conext:
{context}

question:{query}

Answer:"""

llm = OllamaLLM(model="tinyllama")

response = llm.invoke(prompt)

print(response)

print(f"Total documents loaded : {len(documents)}")

