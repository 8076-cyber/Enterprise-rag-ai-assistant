from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

loader = DirectoryLoader(
    "data",
    glob= "*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

print(f"total documents loaded :{len(documents)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store= FAISS.from_documents(chunks , embedding_model)

vector_store.save_local("vector_store/faiss_index")

print("faiss vector store successfully !")
