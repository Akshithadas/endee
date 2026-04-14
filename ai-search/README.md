# 🤖 AI Chatbot using Endee (RAG-based)

## 📌 Overview

This project is a **Retrieval Augmented Generation (RAG)** based chatbot that answers user queries using a custom knowledge base.

Unlike traditional chatbots, this system does not rely solely on pre-trained knowledge. Instead, it retrieves relevant information from a vector database and generates accurate, context-aware responses.

The project uses **Endee** as the vector database for efficient semantic search and retrieval.

---

## 🚀 Features

* 🔍 Semantic Search using vector embeddings
* 🧠 Context-aware response generation using LLM
* 📂 Custom knowledge base (data.txt)
* ⚡ Fast retrieval with Endee vector database
* 💬 Command-line chatbot interface

---

## 🧠 How It Works (RAG Pipeline)

1. Data is loaded from `data.txt`
2. Text is split into chunks
3. Chunks are converted into embeddings
4. Stored in Endee vector database
5. User query is converted into embedding
6. Relevant chunks are retrieved (semantic search)
7. Context + query sent to LLM
8. LLM generates final answer

---

## 🏗️ Project Structure

```
ai-chatbot/
│
├── ingest.py          # Stores data into Endee
├── query.py           # Performs semantic search
├── rag_chatbot.py     # Main chatbot logic
├── config.py          # API configuration
├── data.txt           # Knowledge base
├── requirements.txt   # Dependencies
└── .env               # API key (not pushed to GitHub)
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd ai-search
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### Step 1: Ingest Data

```bash
python ingest.py
```

### Step 2: Run Chatbot

```bash
python rag_chatbot.py
```

---

## 💬 Example

```
You: What is AI?
Bot: Artificial Intelligence is the simulation of human intelligence by machines.
```

---

## 🛠️ Tech Stack

* Python
* Endee (Vector Database)
* OpenAI API (LLM)
* dotenv

---

## 📈 Future Improvements

* 📄 PDF document support
* 🌐 Web UI using Streamlit
* 🧠 Conversation memory
* 📊 Better chunking & ranking

---

## ⚠️ Important Notes

* Ensure `ingest.py` is run before querying
* Do not upload `.env` file to GitHub
* Works best with meaningful data

---

## 📚 What I Learned

* Vector databases and embeddings
* Semantic search vs keyword search
* RAG architecture
* Prompt engineering basics

---

## 🙌 Acknowledgment

This project uses **Endee** as the vector database.

---

