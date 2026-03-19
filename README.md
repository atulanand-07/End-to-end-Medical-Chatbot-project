# 🩺 AI Medical Chatbot (RAG GenAI Project)

An end-to-end **Medical Chatbot** built using **Streamlit, LangChain, Pinecone, and LLM APIs**.
This project uses **Retrieval-Augmented Generation (RAG)** to provide context-aware medical responses based on a medical knowledge base.

---

# 🚀 Features

* 💬 Interactive chatbot UI (Streamlit)
* 📚 Context-aware answers using medical knowledge base
* 🔍 Semantic search with vector embeddings (Pinecone)
* 🧠 LLM-powered responses (Qwen / OpenRouter / Groq)
* ⚡ Fast retrieval with optimized pipeline
* 🔐 Secure API key management using Streamlit Secrets

---

# 🧠 Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python, LangChain
* **Vector Database**: Pinecone
* **Embeddings**: Sentence Transformers
* **LLM**: API-based (OpenRouter / Groq / OpenAI)
* **Deployment**: Streamlit Community Cloud

---

# 📁 Project Structure

```
medical-chatbot/
│
├── app.py                # Streamlit frontend
├── config.py             # Config & environment variables
├── ingest.py             # Data ingestion (run locally once)
├── requirements.txt
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

* Process documents
* Generate embeddings
* Store them in Pinecone

---

## 6. Run the App

```
streamlit run app.py
```

---

# ☁️ Deployment (Streamlit Cloud)

## Steps:

1. Push your code to GitHub
2. Go to Streamlit Community Cloud
3. Click **"New App"**
4. Select your repository
5. Set:

   * Branch → `main`
   * Main file → `app.py`

---

## 🔐 Add Secrets (IMPORTANT)

In **Advanced Settings → Secrets**, add:

```
PINECONE_API_KEY = "your_key"
PINECONE_HOST = "your_host"
INDEX_NAME = "medical-chatbot"
OPENROUTER_API_KEY = "your_key"
```

---

## ▶️ Deploy

Click **Deploy** and wait a few minutes.

---

## 🌍 Live App

You will get a public URL like:

```
https://your-app.streamlit.app
```

---

# ⚠️ Important Notes

* ❌ Do NOT include `.env` file in GitHub
* ❌ Do NOT run `ingest.py` during deployment
* ✅ Use API-based LLM (not local Ollama)
* ⚠️ First load may take a few seconds

---

# 🧪 Example Workflow

```
User Query → Retriever (Pinecone)
           → Relevant Context
           → LLM API
           → Response → Streamlit UI
```

---

# 📌 Disclaimer

⚠️ This chatbot is for **educational purposes only**
It is **not a substitute for professional medical advice**

---

# 👨‍💻 Author

**Atul Anand**
B.Tech | NIT Jamshedpur

---

# 🌟 Future Improvements

* Chat memory with context awareness
* Source citations
* Voice interaction
* Authentication system
* UI enhancements

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
