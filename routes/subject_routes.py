from flask import Blueprint, render_template, request, session, redirect
from models.subject_model import add_subject, get_subjects

subject_bp = Blueprint('subject', __name__)

@subject_bp.route('/subjects', methods=['GET', 'POST'])
def subjects():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        add_subject(
            session['user_id'],
            request.form['subject_name']
        )

    subjects = get_subjects(session['user_id'])
    return render_template('subjects.html', subjects=subjects)
