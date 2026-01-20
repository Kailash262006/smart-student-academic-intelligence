from utils.db import get_db_connection

def add_study_session(user_id, subject_id, planned, actual, date):
    conn = get_db_connection()
    conn.execute(
        """INSERT INTO study_sessions
           (user_id, subject_id, planned_minutes, actual_minutes, session_date)
           VALUES (?, ?, ?, ?, ?)""",
        (user_id, subject_id, planned, actual, date)
    )
    conn.commit()
    conn.close()


def get_focus_data(user_id):
    conn = get_db_connection()

    rows = conn.execute(
        """SELECT planned_minutes, actual_minutes
           FROM study_sessions
           WHERE user_id = ?""",
        (user_id,)
    ).fetchall()

    conn.close()

    return [
        {'planned': row['planned_minutes'], 'actual': row['actual_minutes']}
        for row in rows
    ]


def get_last_7_days_focus(user_id):
    conn = get_db_connection()

    row = conn.execute(
        """
        SELECT AVG((actual_minutes * 100.0) / planned_minutes) AS focus
        FROM study_sessions
        WHERE user_id = ?
          AND session_date >= date('now', '-7 days')
        """,
        (user_id,)
    ).fetchone()

    conn.close()
    return round(row['focus']) if row['focus'] else 0
