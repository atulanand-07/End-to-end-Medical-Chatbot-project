import streamlit as st

from src.embeddings import get_embeddings
from src.vectorstore import load_vectorstore
from src.retriever import get_retriever
from src.chain import get_chain


# ------------------ PAGE CONFIG ------------------

st.set_page_config(page_title="Medical Chatbot", layout="wide")

st.title("🩺 Medical Chatbot")


# ------------------ LOAD SYSTEM ------------------

@st.cache_resource
def load_system():
    emb = get_embeddings()
    vs = load_vectorstore(emb)
    retriever = get_retriever(vs)
    chain = get_chain(retriever)
    return chain

chain = load_system()


# ------------------ SESSION STATE ------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ------------------ DISPLAY CHAT HISTORY ------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):

        if isinstance(msg["content"], dict):
            st.markdown(f"### 🧠 Topic: {msg['content'].get('topic', 'N/A')}")
            st.markdown(f"### 🏷️ Category: {msg['content'].get('category', 'N/A')}")
            st.markdown(msg["content"].get("answer", ""))
        else:
            st.markdown(msg["content"])


# ------------------ USER INPUT ------------------

user_input = st.chat_input("Ask a medical question...")

if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking..."):

            try:
                response = chain.invoke({"question": user_input})

                # 🔥 Handle structured output
                if isinstance(response, dict):

                    st.markdown(f"### 🧠 Topic: {response.get('topic', 'N/A')}")
                    st.markdown(f"### 🏷️ Category: {response.get('category', 'N/A')}")
                    st.markdown(response.get("answer", ""))

                else:
                    st.markdown(response)

            except Exception as e:
                response = f"❌ Error: {str(e)}"
                st.error(response)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })