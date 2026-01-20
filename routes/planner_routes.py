from flask import Blueprint, render_template, request, session, redirect
from models.exam_model import add_exam
from models.subject_model import get_subjects

planner_bp = Blueprint('planner', __name__)

@planner_bp.route('/planner', methods=['GET', 'POST'])
def planner():
    if 'user_id' not in session:
        return redirect('/login')

    subjects = get_subjects(session['user_id'])

    if request.method == 'POST':
        add_exam(
            session['user_id'],
            request.form['subject_id'],
            request.form['exam_date']
        )

    return render_template('planner.html', subjects=subjects)
