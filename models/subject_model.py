
from extensions import db
from models.schema import Subject


def add_subject(user_id, subject_name):
    subject = Subject(user_id=user_id, subject_name=subject_name)
    db.session.add(subject)
    db.session.commit()
    return subject


def get_subjects(user_id):
    rows = Subject.query.with_entities(Subject.subject_id, Subject.subject_name).filter_by(user_id=user_id).all()
    return [{'subject_id': r.subject_id, 'subject_name': r.subject_name} for r in rows]
