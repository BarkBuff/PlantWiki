-- File: schemas/schema.sql

DROP TABLE IF EXISTS defects;
CREATE TABLE defects (
    defect_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    machine_id TEXT,
    defect_type TEXT,
    shift TEXT
);

DROP TABLE IF EXISTS shifts;
CREATE TABLE shifts (
    shift_id INTEGER PRIMARY KEY AUTOINCREMENT,
    operator_name TEXT,
    start_time TEXT,
    end_time TEXT
);