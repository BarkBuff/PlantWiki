import sqlite3
from datetime import datetime, timedelta
import random

machines = ['Machine_A', 'Machine_B', 'Machine_C']
defect_types = ['Class A', 'Class B', 'Class C']
shifts = ['Shift 1', 'Shift 2', 'Shift 3']
operators = ['John', 'Alice', 'Bob', 'Ravi']

conn = sqlite3.connect("data/plant.db")
cur = conn.cursor()

# Insert defects
for i in range(50):
    date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    machine = random.choice(machines)
    defect = random.choice(defect_types)
    shift = random.choice(shifts)
    cur.execute("INSERT INTO defects (date, machine_id, defect_type, shift) VALUES (?, ?, ?, ?)",
                (date, machine, defect, shift))

# Insert shifts
for op in operators:
    start_time = (datetime.now() - timedelta(hours=random.randint(1, 24))).strftime("%Y-%m-%d %H:%M:%S")
    end_time = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO shifts (operator_name, start_time, end_time) VALUES (?, ?, ?)",
                (op, start_time, end_time))

conn.commit()
conn.close()

print("✅ Dummy data inserted into plant.db.")
