from extensions import db
from models.schema import MoodLog
from datetime import date, timedelta
from sqlalchemy import func


def add_mood_log(user_id, mood, stress, date_):
    m = MoodLog(user_id=user_id, mood_level=mood, stress_level=stress, log_date=date_)
    db.session.add(m)
    db.session.commit()
    return m


def get_avg_mood(user_id):
    since = date.today() - timedelta(days=7)
    row = db.session.query(func.avg(MoodLog.mood_level).label('avg_mood')).filter(
        MoodLog.user_id == user_id,
        MoodLog.log_date >= since
    ).one()
    avg = row.avg_mood
    return round(avg) if avg else 3
