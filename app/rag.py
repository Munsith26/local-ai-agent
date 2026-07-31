from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DOCUMENT_FOLDER = Path("documents")
VECTOR_DB_FOLDER = "vector_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def list_documents():
    if not DOCUMENT_FOLDER.exists():
        return []

    return [file.name for file in DOCUMENT_FOLDER.glob("*.pdf")]


def create_vector_db():
    pdf_files = list(DOCUMENT_FOLDER.glob("*.pdf"))

    if not pdf_files:
        return "No PDF files found."

    documents = []

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    vector_db = FAISS.from_documents(chunks, embeddings)

    vector_db.save_local(VECTOR_DB_FOLDER)

    return f"Indexed {len(chunks)} chunks from {len(pdf_files)} PDF(s)."


def search_documents(question):
    vector_db = FAISS.load_local(
        VECTOR_DB_FOLDER,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vector_db.similarity_search(question, k=3)

    context = "\n\n".join(doc.page_content for doc in docs)

    return context