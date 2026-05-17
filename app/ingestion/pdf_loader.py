from langchain_community.document_loaders import PyPDFLoader

pdf_path = "data/sample.pdf"

loader = PyPDFLoader(pdf_path)

documents = loader.load()

print(documents[0].page_content)
