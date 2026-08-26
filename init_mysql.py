from config import SQLALCHEMY_DATABASE_URI, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB
from extensions import db
from app import app
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

# Define minimal models matching existing schema to create empty tables
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    department = db.Column(db.String(255))
    semester = db.Column(db.Integer)

class Subject(db.Model):
    __tablename__ = 'subjects'
    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    subject_name = db.Column(db.String(255))

class Mark(db.Model):
    __tablename__ = 'marks'
    mark_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    subject_id = db.Column(db.Integer)
    exam_type = db.Column(db.String(255))
    marks = db.Column(db.Integer)
    max_marks = db.Column(db.Integer)
    exam_date = db.Column(db.Date)

class StudySession(db.Model):
    __tablename__ = 'study_sessions'
    session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    subject_id = db.Column(db.Integer)
    planned_minutes = db.Column(db.Integer)
    actual_minutes = db.Column(db.Integer)
    session_date = db.Column(db.Date)

class MoodLog(db.Model):
    __tablename__ = 'mood_logs'
    mood_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    mood_level = db.Column(db.Integer)
    stress_level = db.Column(db.Integer)
    log_date = db.Column(db.Date)

class ExamSchedule(db.Model):
    __tablename__ = 'exam_schedule'
    exam_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    subject_id = db.Column(db.Integer)
    exam_date = db.Column(db.Date)


def create_mysql_tables():
    print("Creating MySQL database if it doesn't exist...")
    # Try to create database first (connect to server without a DB)
    try:
        no_db_uri = f"mysql+pymysql://{MYSQL_USER}:{quote_plus(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/"
        engine = create_engine(no_db_uri)
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{MYSQL_DB}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"))
        print(f"Ensured database `{MYSQL_DB}` exists")
    except Exception as e:
        print("Warning: could not auto-create database. Ensure it exists or create it manually.")
        print("Error:", e)

    print("Creating tables in MySQL based on SQLAlchemy models...")
    with app.app_context():
        db.create_all()
    print("Done.")

if __name__ == '__main__':
    create_mysql_tables()
