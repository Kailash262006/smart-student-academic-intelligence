from utils.db import get_db_connection

def add_marks(user_id, subject_id, exam_type, marks, max_marks, exam_date):
    conn = get_db_connection()
    conn.execute(
        """INSERT INTO marks (user_id, subject_id, exam_type, marks, max_marks, exam_date)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (user_id, subject_id, exam_type, marks, max_marks, exam_date)
    )
    conn.commit()
    conn.close()


def get_subject_performance(user_id):
    conn = get_db_connection()

    rows = conn.execute(
        """
        SELECT s.subject_name,
               AVG((m.marks * 100.0) / m.max_marks) AS percentage
        FROM marks m
        JOIN subjects s ON m.subject_id = s.subject_id
        WHERE m.user_id = ?
        GROUP BY s.subject_name
        """,
        (user_id,)
    ).fetchall()

    conn.close()

    return [
        {'subject': row['subject_name'], 'percentage': round(row['percentage'])}
        for row in rows
    ]
