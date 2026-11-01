import streamlit as st

from rag_pipeline import generate_answer


st.set_page_config(
    page_title="AI Knowledge Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 AI Knowledge Chatbot")

st.caption(
    "Ask questions about Artificial Intelligence, "
    "Machine Learning, Deep Learning and more."
)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    if message["role"] == "user":

        left, right = st.columns([2, 1])

        with right:
            with st.chat_message("user"):
                st.markdown(message["content"])

    else:

        left, right = st.columns([1, 1])

        with left:
            with st.chat_message("assistant"):
                st.markdown(message["content"])


if prompt := st.chat_input("Ask something about AI..."):

    left, right = st.columns([1, 1])

    with right:
        with st.chat_message("user"):
            st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    left, right = st.columns([1, 1])

    with left:
        with st.chat_message("assistant"):

            with st.spinner("Generating answer..."):

                response = generate_answer(prompt)
                answer = st.write_stream(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )