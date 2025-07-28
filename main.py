from app.router.query_classifier import classify_query
from app.sql_interface.query_run import generate_sql, run_sql, format_response
import traceback
try:
    from app.doc_agent.rag_engine import get_doc_answer
except ImportError:
    def get_doc_answer(query): return "📄 [DOC answer system not yet implemented]"


def main():
    while True:
        user_input = input("\n❓ Ask your plant data question: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("👋 Goodbye!")
            break

        try:
            route = classify_query(user_input)

            if route == "SQL":
                sql = generate_sql(user_input)
                answer = run_sql(sql)
            else:
                answer = get_doc_answer(user_input)

        except Exception as e:
            answer = f"❌ Error: {str(e)}"
            traceback.print_exc()

        print("\n📤 Answer:\n", answer)


if __name__ == "__main__":
    print("🏭 PlantWiki v1 - Industrial NLP Chatbot")
    print("Type 'exit' or 'quit' to stop\n")
    main()