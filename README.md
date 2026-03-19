# End-to-end-Medical-Chatbot-project


# 🩺 AI Medical Chatbot (RAG GenAI Project)

An end-to-end **Medical Chatbot** built using **Streamlit, LangChain, Pinecone, and LLM APIs**.
This project uses **Retrieval-Augmented Generation (RAG)** to provide context-aware medical responses based on a medical knowledge base.

---

# 🚀 Features

* 💬 Interactive chatbot UI (Streamlit)
* 📚 Context-aware answers using medical PDF knowledge
* 🔍 Semantic search with vector embeddings (Pinecone)
* 🧠 LLM-powered responses (Qwen / OpenRouter / API-based)
* ⚡ Fast retrieval with optimized pipeline
* 🔐 Secure API key management via environment variables

---

# Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python, LangChain
* **Vector Database**: Pinecone
* **Embeddings**: Sentence Transformers
* **LLM**: API-based (OpenRouter / OpenAI / Groq)
* **Deployment**: Render

---

# 📁 Project Structure

```
medical-chatbot/
│
├── app.py                # Streamlit frontend
├── config.py             # Environment config
├── ingest.py             # Data ingestion (run once locally)
├── requirements.txt
│
├── data/
│   └── Medical_book.pdf
│
├── src/
│   ├── chain.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── loader.py
│   ├── prompt.py
│   ├── retriever.py
│   ├── splitter.py
│   ├── vectorstore.py
│   └── confidence.py
│
└── README.md
```

---

# ⚙️ Setup Instructions (Local)

## 1. Clone the Repository

```
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

---

## 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Setup Environment Variables

Create a `.env` file:

```
PINECONE_API_KEY=your_key
PINECONE_HOST=your_host
INDEX_NAME=medical-chatbot
OPENROUTER_API_KEY=your_key
```

---

## 5. Run Data Ingestion (Only Once)

```
python ingest.py
```

👉 This will:

* Process PDF
* Generate embeddings
* Store them in Pinecone

---

## 6. Run the App

```
streamlit run app.py
```

---

# 🌐 Deployment (Render)

## Steps:

1. Push code to GitHub
2. Go to Render → New Web Service
3. Connect repository

### Build Command:

```
pip install -r requirements.txt
```

### Start Command:

```
streamlit run app.py --server.port=10000 --server.address=0.0.0.0
```

---

## 🔐 Add Environment Variables in Render

```
PINECONE_API_KEY = your_key
PINECONE_HOST = your_host
INDEX_NAME = medical-chatbot
OPENROUTER_API_KEY = your_key
```

---

# ⚠️ Important Notes

* ❌ Do NOT run `ingest.py` during deployment
* ❌ Do NOT expose API keys in code
* ✅ Use API-based LLM (not local Ollama)
* ⚠️ Free tier may have cold start delays

---

# 🧪 Example Workflow

```
User Query → Retriever (Pinecone)
           → Relevant Context
           → LLM (Qwen / API)
           → Response → Streamlit UI
```

---

# 📌 Disclaimer

This chatbot is for **educational purposes only**
It is **not a substitute for professional medical advice**
**The Project is only for the learning purpose**

---

# 👨‍💻 Author

**Atul Anand**
B.Tech | NIT Jamshedpur

---

# 🌟 Future Improvements

* Chat history (memory)
* Source citations
* Voice input/output
* Doctor-style UI
* Authentication system

---
