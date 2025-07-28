from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)
    return [
        {"embedding": emb, "text": chunk["text"], "source": chunk["source"]}
        for emb, chunk in zip(embeddings, chunks)
    ]
