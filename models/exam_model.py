from utils.db import get_db_connection

def add_exam(user_id, subject_id, exam_date):
    conn = get_db_connection()
    conn.execute(
        """INSERT INTO exam_schedule (user_id, subject_id, exam_date)
           VALUES (?, ?, ?)""",
        (user_id, subject_id, exam_date)
    )
    conn.commit()
    conn.close()


def get_upcoming_exams(user_id):
    conn = get_db_connection()

    rows = conn.execute(
        """
        SELECT s.subject_name, e.exam_date
        FROM exam_schedule e
        JOIN subjects s ON e.subject_id = s.subject_id
        WHERE e.user_id = ?
          AND e.exam_date >= date('now')
        ORDER BY e.exam_date
        """,
        (user_id,)
    ).fetchall()

    conn.close()

    return [
        {'subject': row['subject_name'], 'exam_date': row['exam_date']}
        for row in rows
    ]
