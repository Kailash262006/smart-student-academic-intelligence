from utils.db import get_db_connection

def add_subject(user_id, subject_name):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO subjects (user_id, subject_name) VALUES (?, ?)",
        (user_id, subject_name)
    )
    conn.commit()
    conn.close()


def get_subjects(user_id):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT subject_id, subject_name FROM subjects WHERE user_id = ?",
        (user_id,)
    ).fetchall()
    conn.close()

    return rows
