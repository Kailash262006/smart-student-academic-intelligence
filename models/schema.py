from extensions import db


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
