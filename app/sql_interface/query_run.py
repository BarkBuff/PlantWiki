import sqlite3
from app.llm_agent.llm import ask_mistral
from app.sql_interface.sql_templates import SYSTEM_PROMPT

DB_PATH = "data/plant.db"

def generate_sql(user_query: str) -> str:
    from app.llm_agent.llm import ask_mistral
    from app.sql_interface.sql_templates import SYSTEM_PROMPT

    prompt = f"{SYSTEM_PROMPT}\n\nQ: {user_query}\nA:"
    sql = ask_mistral(prompt).strip()

    if not sql.lower().startswith("select"):
        raise ValueError("⚠️ Generated SQL does not start with SELECT.")

    return sql


def run_sql(sql: str) -> str:
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"❌ SQL error: {e}"

def format_response(sql: str, result, user_query: str) -> dict:
    if isinstance(result, str) and "error" in result.lower():
        return {"text": f"⚠️ SQL Error: {result}", "source": "SQL"}
    
    return {
        "text": f"📊 Result for: '{user_query}'\n\n```sql\n{sql}\n```\n→ {result}",
        "source": "Plant Database"
    }
