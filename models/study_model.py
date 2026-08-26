from extensions import db
from models.schema import StudySession
from datetime import date, timedelta
from sqlalchemy import func


def add_study_session(user_id, subject_id, planned, actual, date_):
    s = StudySession(user_id=user_id, subject_id=subject_id, planned_minutes=planned, actual_minutes=actual, session_date=date_)
    db.session.add(s)
    db.session.commit()
    return s


def get_focus_data(user_id):
    rows = StudySession.query.with_entities(StudySession.planned_minutes, StudySession.actual_minutes).filter_by(user_id=user_id).all()
    return [{'planned': r.planned_minutes, 'actual': r.actual_minutes} for r in rows]


def get_last_7_days_focus(user_id):
    since = date.today() - timedelta(days=7)
    row = db.session.query(func.avg((StudySession.actual_minutes * 100.0) / StudySession.planned_minutes).label('focus')).filter(
        StudySession.user_id == user_id,
        StudySession.session_date >= since
    ).one()
    focus = row.focus
    return round(focus) if focus else 0
