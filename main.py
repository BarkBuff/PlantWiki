import os
from app.sql_interface.query_run import generate_sql, run_sql, format_response
from app.doc_agent.rag_engine import rebuild_doc_index, get_doc_answer

# Optional: ensure working dir is project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("🔄 Rebuilding document index from /sops and /uploads...")
rebuild_doc_index()
print("✅ Document index updated.\n")

print("🏭 PlantWiki v1 - Industrial NLP Chatbot")
print("Type 'exit' or 'quit' to stop\n")

while True:
    user_query = input("❓ Ask your plant data question: ").strip()
    if user_query.lower() in ["exit", "quit"]:
        break

    try:
        # Attempt SQL answer
        sql = generate_sql(user_query)
        result = run_sql(sql)
        response = format_response(sql, result, user_query)
    except Exception as e:
        print("🔁 SQL failed — falling back to document search...")
        response = get_doc_answer(user_query)

    print("\n📤 Answer:\n", response["text"], "\n")
