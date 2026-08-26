from extensions import db
from models.schema import User


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def get_user_by_id(user_id):
    return User.query.filter_by(user_id=user_id).first()


def create_user(name, email, password, department, semester):
    user = User(name=name, email=email, password=password,
                department=department, semester=semester)
    db.session.add(user)
    db.session.commit()
    return user
