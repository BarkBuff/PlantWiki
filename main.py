from app.sql_interface.query_run import generate_sql, run_sql, format_response

if __name__ == "__main__":
    question = input("❓ Ask your plant data question: ").strip()
    
    sql = generate_sql(question)
    result = run_sql(sql)
    response = format_response(sql, result, question)

    print("\n📤 Answer:\n", response["text"])
