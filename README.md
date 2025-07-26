# PlantWiki v1 – Industrial NLP Chatbot for Manufacturing Insights

- “How many Class A defects this week?”  
- “How do I reset the dryer?”  
- “Average downtime for Machine B?”  

Ask like a human. Get real answers from structured **SQL data** or unstructured **SOPs/manuals**.

---

## What Is PlantWiki?

A dual-brain NLP chatbot for industrial plants:

| Structured (SQL)                 | Unstructured (Docs)               |
| -------------------------------- | --------------------------------- |
| Defect counts, downtime, shifts  | SOPs, instructions, policies      |
| Queries SQLite or production DB  | Searches indexed documents        |
| LLM → SQL → Result               | LLM → RAG → Semantic Answer       |

---

## Powered By

- **Mistral 7B** via [Ollama](https://ollama.com/)
- **LangChain** for RAG pipeline
- **SQLite3** for structured data
- **Local vector store (FAISS)** for document Q&A
- **Python 3.11+** and `venv` (no Docker needed)

---

## Features

- Chatbot understands SQL-style + SOP-style queries
- Semantic document search (PDF/CSV/TXT) via vector DB
- Tiny keyword router for SQL vs RAG question classification
- File upload support
- Built-in error handling for hallucinations or empty answers
- Designed for UI and API integration

---

## Folder Structure

```bash
PlantWiki/
├── main.py                      # Unified Q&A entrypoint
├── app/
│   ├── llm_agent/llm.py         # LLM handler (Mistral)
│   ├── sql_interface/           # Structured DB query engine
│   │   ├── query_run.py
│   │   └── sql_templates.py
│   └── doc_index/               # RAG-based SOP system
│       ├── rag_engine.py
│       ├── vector_store.py
│       └── document_loader.py
├── data/
│   ├── plant.db                 # SQLite database
│   └── sop_docs/                # Plant SOPs/manuals
├── schemas/
│   └── schema.sql               # Table definitions
├── scripts/
│   ├── init_db.py               # Setup database
│   └── populate_db.py           # Insert mock defect data
├── requirements.txt             # All dependencies
└── .env                         # Config
````

---

## Setup Instructions

```bash
# Setup Python environment
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Init database
python scripts/init_db.py
python scripts/populate_db.py

# Run Mistral
ollama run mistral

# Launch the chatbot
python main.py
```

---

## Example Prompts

| You Ask...                                    | Route Used | Output Type     |
| --------------------------------------------- | ---------- | --------------- |
| “How many defects in Shift 1 today?”          | SQL Engine | Numeric summary |
| “Who worked on Machine B yesterday?”          | SQL Engine | Name list       |
| “How to reset the dryer after overheating?”   | Doc Engine | SOP explanation |
| “Show me shutdown protocol”                   | Doc Engine | Text from SOP   |
| “Average Class B defects per day this month?” | SQL Engine | Aggregation     |

---

## Roadmap

| Feature                           | Status       |
|-----------------------------------|--------------|
| SQL Q\&A                          | Done         |
| RAG-powered SOP Q\&A              | In Progress  |
| Auto router for query types       | In Progress  |
| UI (Bolt / Loveable integration)  | Coming Soon  |
| API server (FastAPI)              | Coming Soon  |
| Fine-tuned LLM (plant-specific)   | PlantWiki v2 |

---

## Built By **BarkBuff** & **Synapse**

- Systems thinking meets machine intelligence.
- You bring the machines. We bring them to life.

---