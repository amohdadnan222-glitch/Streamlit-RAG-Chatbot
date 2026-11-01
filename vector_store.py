import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

def create_vector_store():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Please check your .env file."
        )

    loader = TextLoader("sample.txt", encoding="utf-8")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 100
    )

    chunks = text_splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model = "gemini-embedding-001",
        google_api_key = api_key
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    print(f"Vector database created with {len(chunks)} text chunks")



if __name__ == "__main__":
    create_vector_store()
