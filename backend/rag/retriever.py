import numpy as np
from backend.vectorstore.faiss_index import load_faiss_index
from sentence_transformers import SentenceTransformer
from backend.config import TOP_K

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query):
    index, metadata = load_faiss_index()
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, TOP_K)

    results = []
    for idx in indices[0]:
        results.append(metadata[idx])

    return results
