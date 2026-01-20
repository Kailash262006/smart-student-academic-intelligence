from flask import Blueprint, render_template, request, session, redirect
from models.marks_model import add_marks
from models.subject_model import get_subjects

marks_bp = Blueprint('marks', __name__)

@marks_bp.route('/marks', methods=['GET', 'POST'])
def marks():
    if 'user_id' not in session:
        return redirect('/login')

    subjects = get_subjects(session['user_id'])

    if request.method == 'POST':
        add_marks(
            session['user_id'],
            request.form['subject_id'],
            request.form['exam_type'],
            request.form['marks'],
            request.form['max_marks'],
            request.form['exam_date']
        )

    return render_template('marks.html', subjects=subjects)
