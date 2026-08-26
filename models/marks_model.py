from extensions import db
from sqlalchemy import func
from models.schema import Mark, Subject


def add_marks(user_id, subject_id, exam_type, marks, max_marks, exam_date):
    m = Mark(user_id=user_id, subject_id=subject_id, exam_type=exam_type,
             marks=marks, max_marks=max_marks, exam_date=exam_date)
    db.session.add(m)
    db.session.commit()
    return m


def get_subject_performance(user_id):
    rows = db.session.query(
        Subject.subject_name,
        func.avg((Mark.marks * 100.0) / Mark.max_marks).label('percentage')
    ).join(Mark, Mark.subject_id == Subject.subject_id).filter(Mark.user_id == user_id).group_by(Subject.subject_name).all()

    return [{'subject': r.subject_name, 'percentage': round(r.percentage)} for r in rows]
