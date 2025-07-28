import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from app.doc_agent.document_loader import load_documents
from app.doc_agent.embedder import embed_chunks
from app.doc_agent.vector_store import save_to_vector_store
from app.llm_agent.llm import ask_mistral

model = SentenceTransformer('all-MiniLM-L6-v2')

# Absolute paths under /data/
VECTOR_PATH = "data/vector_store/index.faiss"
META_PATH = "data/vector_store/meta.pkl"

def rebuild_doc_index():
    print("📥 Loading and chunking documents from /data/sops and /data/uploads...")
    chunks = load_documents(["data/sops/", "data/uploads/"])
    if not chunks:
        print("⚠️ No documents found to index.")
        return

    print(f"🔢 Embedding {len(chunks)} chunks...")
    embedded_chunks = embed_chunks(chunks)

    print(f"💾 Saving to vector store...")
    save_to_vector_store(embedded_chunks, VECTOR_PATH, META_PATH)
    print("✅ Vector store updated.\n")


def get_doc_answer(user_query):
    if not os.path.exists(VECTOR_PATH) or not os.path.exists(META_PATH):
        return {"text": "⚠️ Vector store missing. Please rebuild the index.", "source": "Docs"}

    # Load FAISS index + metadata
    index = faiss.read_index(VECTOR_PATH)
    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)

    # Embed query + search top 3 similar chunks
    query_vector = model.encode([user_query]).astype("float32")
    D, I = index.search(query_vector, k=3)

    # Extract top chunks
    top_chunks = [metadata[i]["text"] for i in I[0] if i < len(metadata)]
    
    if not top_chunks:
        return {"text": "⚠️ No relevant document found.", "source": "Docs"}

    # Compose context + prompt for LLM
    context = "\n\n".join(top_chunks)
    prompt = f"""You are a helpful industrial assistant. Based on the documents below, answer the question clearly and concisely.

Documents:
{context}

Question: {user_query}
Answer:"""

    try:
        answer = ask_mistral(prompt).strip()
        return {"text": f"📚 {answer}", "source": "Docs + LLM"}
    except Exception as e:
        return {"text": f"⚠️ LLM failure: {e}", "source": "Docs"}
