from backend.ingestion.loader import load_documents
from backend.ingestion.chunker import chunk_text
from backend.ingestion.embedder import embed_texts
from backend.vectorstore.faiss_index import build_faiss_index
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


docs = load_documents("data/raw_documents")

all_chunks = []
metadata = []

for doc in docs:
    chunks = chunk_text(doc["text"])
    for chunk in chunks:
        all_chunks.append(chunk)
        metadata.append(doc["source"])

embeddings = embed_texts(all_chunks)
embeddings = np.array(embeddings).astype("float32")

build_faiss_index(embeddings, all_chunks)

print("✅ Documents ingested and indexed successfully")
