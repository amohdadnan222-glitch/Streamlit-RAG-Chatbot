import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

def search_documents(question: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI API KEY do not found."
        )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key = api_key
    )

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    results = vector_store.similarity_search(
        question,
        k=2
    )

    return results