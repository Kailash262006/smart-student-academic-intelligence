from extensions import db
from models.schema import ExamSchedule, Subject
from datetime import date


def add_exam(user_id, subject_id, exam_date):
    exam = ExamSchedule(user_id=user_id, subject_id=subject_id, exam_date=exam_date)
    db.session.add(exam)
    db.session.commit()
    return exam


def get_upcoming_exams(user_id):
    rows = db.session.query(Subject.subject_name, ExamSchedule.exam_date).join(ExamSchedule, ExamSchedule.subject_id == Subject.subject_id).filter(
        ExamSchedule.user_id == user_id,
        ExamSchedule.exam_date >= date.today()
    ).order_by(ExamSchedule.exam_date).all()

    return [{'subject': r.subject_name, 'exam_date': r.exam_date} for r in rows]
