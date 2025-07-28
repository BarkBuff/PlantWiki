from app.llm_agent.llm import ask_mistral

ROUTING_PROMPT = """
You are a query router for an industrial chatbot.

Decide if a user’s question is about:
1. Structured data (SQL)
2. Unstructured procedure/instructions (DOC)

Reply with only one word: `SQL` or `DOC`.

Examples:
Q: How many defects happened yesterday?  
A: SQL

Q: How do I reset the dryer?  
A: DOC

Q: Who worked Shift 2 last week?  
A: SQL

Q: What is the SOP for Line 3 startup?  
A: DOC
"""

def classify_query(user_query: str) -> str:
    prompt = f"{ROUTING_PROMPT}\n\nQ: {user_query}\nA:"
    response = ask_mistral(prompt).strip().upper()
    return "DOC" if "DOC" in response else "SQL"
