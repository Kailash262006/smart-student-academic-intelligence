from flask import Blueprint, render_template, request, session, redirect
from models.mood_model import add_mood_log
from datetime import date

burnout_bp = Blueprint('burnout', __name__)

@burnout_bp.route('/burnout', methods=['GET', 'POST'])
def burnout():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        add_mood_log(
            session['user_id'],
            request.form['mood'],
            request.form['stress'],
            date.today()
        )

    return render_template('burnout.html')
