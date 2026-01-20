import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT UNIQUE,
  password TEXT,
  department TEXT,
  semester INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS subjects (
  subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  subject_name TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS marks (
  mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  subject_id INTEGER,
  exam_type TEXT,
  marks INTEGER,
  max_marks INTEGER,
  exam_date DATE
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS study_sessions (
  session_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  subject_id INTEGER,
  planned_minutes INTEGER,
  actual_minutes INTEGER,
  session_date DATE
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS mood_logs (
  mood_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  mood_level INTEGER,
  stress_level INTEGER,
  log_date DATE
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS exam_schedule (
  exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  subject_id INTEGER,
  exam_date DATE
)
""")

conn.commit()
conn.close()

print("✅ Database initialized successfully")
