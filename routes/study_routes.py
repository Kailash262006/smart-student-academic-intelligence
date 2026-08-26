from flask import Blueprint, render_template, request, session, redirect
from models.study_model import add_study_session
from datetime import date
from models.subject_model import get_subjects

study_bp = Blueprint('study', __name__)

@study_bp.route('/study', methods=['GET', 'POST'])
def study():
    if 'user_id' not in session:
        return redirect('/login')

    subjects = get_subjects(session['user_id'])

    if request.method == 'POST':
        add_study_session(
            session['user_id'],
            request.form['subject_id'],
            request.form['planned'],
            request.form['actual'],
            date.today()
        )

    return render_template('study.html', subjects=subjects)
