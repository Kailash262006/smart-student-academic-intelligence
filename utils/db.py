from extensions import db


def get_db_session():
    """Return the SQLAlchemy session (use `db.session` for transactions).

    Use `get_db_session().execute(...)` for raw SQL or ORM for model queries.
    """
    return db.session


def get_engine():
    """Return the SQLAlchemy engine bound to the Flask app."""
    return db.engine
