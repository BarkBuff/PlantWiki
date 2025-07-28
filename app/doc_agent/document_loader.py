import os

def chunk_text(text, source, chunk_size=300):
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return [{"text": chunk, "source": source} for chunk in chunks]

def load_documents(folders):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, "..", ".."))

    documents = []
    for folder in folders:
        full_path = os.path.join(root_dir, folder)
        if not os.path.isdir(full_path):
            continue

        for filename in os.listdir(full_path):
            if filename.endswith(".txt"):
                with open(os.path.join(full_path, filename), "r") as f:
                    content = f.read()
                    chunks = chunk_text(content, source=filename)
                    documents.extend(chunks)
    return documents
