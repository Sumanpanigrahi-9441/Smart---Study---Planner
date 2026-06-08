import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn . cursor()

cursor . execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY ,
    subject TEXT,
    exam_date TEXT ,
    study_hours REAL
)
""")

conn .commit()
conn.close()

print("datebase created Successfully")