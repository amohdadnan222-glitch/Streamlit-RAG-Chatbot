# AI Knowledge Chatbot

## Project Overview

AI Knowledge Chatbot is an interactive web-based chatbot built using Streamlit and Retrieval-Augmented Generation (RAG).

It allows users to ask questions related to Artificial Intelligence and receive answers based on information stored in a knowledge base.

## Features

* Interactive Streamlit Web UI
* Retrieval-Augmented Generation (RAG) integration
* Streaming AI responses
* Chat message history
* Session state management
* Chat interface using `st.chat_message` and `st.chat_input`

## Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini
* ChromaDB
* Vector Embeddings

## Project Structure

* `app.py` - Streamlit chatbot interface
* `rag_pipeline.py` - RAG pipeline and response generation
* `retriever.py` - Retrieves relevant documents
* `vector_store.py` - Creates the Chroma vector database
* `sample.txt` - Knowledge base content
* `chroma_db/` - Persistent vector database
* `requirements.txt` - Python dependencies
* `.env` - Gemini API key configuration

## Setup Instructions

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to Project Folder

```bash
cd "Task 4 (Streamlit Chatbot)"
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own Gemini API key.

### 7. Run the Application

```bash
streamlit run app.py
```

The chatbot will open in your browser.

## Note

The conversation history is maintained using Streamlit session state during the active session.
