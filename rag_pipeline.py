from langchain_google_genai import ChatGoogleGenerativeAI

from retriever import search_documents


def generate_answer(question: str):
    documents = search_documents(question)

    context = "\n\n".join(
        document.page_content for document in documents
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0
    )

    prompt = f"""
    Answer the question using only the context below.

    If the answer is not present in the context,
    say that the information is not available
    in the knowledge base.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    for chunk in llm.stream(prompt):

        content = chunk.content

        if isinstance(content, str):
            if content:
                yield content

        elif isinstance(content, list):

            for block in content:

                if isinstance(block, dict) and block.get("type") == "text":
                    text = block.get("text", "")

                    if text:
                        yield text