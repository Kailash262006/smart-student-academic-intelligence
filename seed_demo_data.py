from app import app
from models.user_model import get_user_by_email, create_user
from models.subject_model import add_subject, get_subjects
from models.marks_model import add_marks
from models.study_model import add_study_session
from models.exam_model import add_exam
from utils.auth import hash_password
from datetime import date, timedelta

EMAIL = input('User email to seed (default: dashtest@example.com): ') or 'dashtest@example.com'

with app.app_context():
    user = get_user_by_email(EMAIL)
    if not user:
        print('User not found. Creating user...')
        user = create_user('Demo User', EMAIL, hash_password('demo123'), 'CS', 1)
    user_id = user.user_id

    # Add subjects
    subjects = ['Maths', 'Physics', 'Chemistry']
    subject_ids = []
    for s in subjects:
        subj = add_subject(user_id, s)
        subject_ids.append(subj.subject_id)

    # Add marks (simulate performance)
    add_marks(user_id, subject_ids[0], 'Midterm', 80, 100, date.today() - timedelta(days=30))
    add_marks(user_id, subject_ids[1], 'Midterm', 45, 100, date.today() - timedelta(days=25))
    add_marks(user_id, subject_ids[2], 'Midterm', 60, 100, date.today() - timedelta(days=20))

    # Add study sessions
    add_study_session(user_id, subject_ids[0], 120, 90, date.today() - timedelta(days=3))
    add_study_session(user_id, subject_ids[1], 60, 20, date.today() - timedelta(days=4))
    add_study_session(user_id, subject_ids[2], 90, 60, date.today() - timedelta(days=2))

    # Add upcoming exams
    add_exam(user_id, subject_ids[1], date.today() + timedelta(days=5))

    print('Seeding completed for', EMAIL)
