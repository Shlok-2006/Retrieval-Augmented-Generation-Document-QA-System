# 📄 Retrieval-Augmented Generation (RAG) Document QA System

## Overview

Large Language Models (LLMs) often hallucinate when answering questions outside their training data.  
This project implements a **Retrieval-Augmented Generation (RAG)** system that grounds LLM responses in external documents, improving factual accuracy, explainability, and scalability.

The system retrieves relevant document chunks using semantic search and injects them into the LLM prompt at inference time.

---

## 🚀 Key Features

- 📂 Document ingestion pipeline
- ✂️ Chunking for efficient retrieval
- 🧠 Embedding-based semantic search
- 🔍 FAISS vector database
- ⚙️ Model-agnostic answer synthesis
- 🌐 FastAPI backend
- 💻 Lightweight frontend UI
- 📌 Source transparency for answers

---

## 🛠️ Tech Stack

### Backend
- **Language:** Python 3.10+
- **API Framework:** FastAPI
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Database:** FAISS
- **Document Processing:** Extracts text from .docx, .pdf, .txtfiles

### Frontend
- HTML, CSS, JavaScript (minimal chat UI)

---

## ▶️ How to Run the RAG Document QA System

This guide explains how to **ingest documents**, **run the backend**, and **launch the frontend**.

# 1️⃣ Install Dependencies
    pip install -r backend/requirements.txt

# 2️⃣ Add Documents for Ingestion
    data/raw_documents/
 
    python -m scripts.ingest_documents

## 3️⃣ Start the Backend Server
      uvicorn backend.app:app --reload
   
### If successful, you will see:
Application startup complete.
     
# 4️⃣ Run the Frontend
    frontend/index.html

---

💡 How the System Works

- User submits a question via the frontend
- Backend encodes the query
- FAISS retrieves top-K relevant document chunks
- Answer is synthesized from retrieved context
- Sources are returned for transparency

---

## Key Design Decisions
- **RAG over fine-tuning** to enable fast updates and reduce hallucination
- **Chunk-based retrieval** to fit LLM context limits
- **Semantic embeddings** for robust similarity matching
- **FAISS** for scalable and efficient nearest-neighbor search

---

### ⚠️ Note: The backend (FastAPI, FAISS, embeddings, and LLM inference) is intended to run locally due to ML dependencies and is not deployed publicly.
## The frontend is hosted via GitHub Pages for UI demonstration.


