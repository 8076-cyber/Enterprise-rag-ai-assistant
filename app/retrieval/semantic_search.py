from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

pdf_path = "data/sample.pdf"

loader = PyPDFLoader(pdf_path)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


chunks = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = FAISS.from_documents(chunks , embedding_model)

query = "what skills are mentioned?"

results = vector_store.similarity_search(query , k=2)

for i , result in enumerate(results):
    print(f"\nresult {i+1}")
    print(result.page_content)

