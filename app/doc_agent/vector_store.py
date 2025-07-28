import faiss
import numpy as np
import pickle
import os

def save_to_vector_store(embedded_chunks, index_path="../../data/vector_store/index.faiss", metadata_path="../../data/vector_store/meta.pkl"):
    os.makedirs("../../data/vector_store", exist_ok=True)

    vectors = np.array([chunk["embedding"] for chunk in embedded_chunks]).astype("float32")
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    faiss.write_index(index, index_path)

    metadata = [{"text": c["text"], "source": c["source"]} for c in embedded_chunks]
    with open(metadata_path, "wb") as f:
        pickle.dump(metadata, f)
