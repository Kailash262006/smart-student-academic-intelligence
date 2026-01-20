from utils.db import get_db_connection

def add_mood_log(user_id, mood, stress, date):
    conn = get_db_connection()
    conn.execute(
        """INSERT INTO mood_logs (user_id, mood_level, stress_level, log_date)
           VALUES (?, ?, ?, ?)""",
        (user_id, mood, stress, date)
    )
    conn.commit()
    conn.close()


def get_avg_mood(user_id):
    conn = get_db_connection()

    row = conn.execute(
        """
        SELECT AVG(mood_level) AS avg_mood
        FROM mood_logs
        WHERE user_id = ?
          AND log_date >= date('now', '-7 days')
        """,
        (user_id,)
    ).fetchone()

    conn.close()
    return round(row['avg_mood']) if row['avg_mood'] else 3
