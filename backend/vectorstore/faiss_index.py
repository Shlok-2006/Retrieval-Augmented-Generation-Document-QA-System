import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "data/processed/faiss.index"
META_PATH = "data/processed/metadata.pkl"

def build_faiss_index(embeddings, metadata):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs("data/processed", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)

def load_faiss_index():
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata
