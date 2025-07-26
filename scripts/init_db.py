import sqlite3

# Create database
conn = sqlite3.connect("data/plant.db")
with open("schemas/schema.sql", "r") as f:
    conn.executescript(f.read())
conn.commit()
conn.close()

print("✅ Database initialized from schema.sql.")
