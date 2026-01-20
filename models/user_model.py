from utils.db import get_db_connection

def get_user_by_email(email):
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE user_id = ?", (user_id,)
    ).fetchone()
    conn.close()
    return user

def create_user(name, email, password, department, semester):
    conn = get_db_connection()
    conn.execute(
        """INSERT INTO users (name, email, password, department, semester)
           VALUES (?, ?, ?, ?, ?)""",
        (name, email, password, department, semester)
    )
    conn.commit()
    conn.close()
