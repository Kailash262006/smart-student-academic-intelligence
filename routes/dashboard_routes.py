from flask import Blueprint, render_template, session, redirect
from models.marks_model import get_subject_performance
from models.study_model import get_focus_data
from models.exam_model import get_upcoming_exams
from analytics.weakness import classify_subjects
from analytics.focus import calculate_focus_efficiency
from analytics.burnout import calculate_burnout_risk
from analytics.insights import generate_insights
from analytics.priority import calculate_priority

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # 1️⃣ AUTH CHECK
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']

    # 2️⃣ FETCH RAW DATA (MODELS)
    subject_data = get_subject_performance(user_id)
    focus_sessions = get_focus_data(user_id)
    upcoming_exams = get_upcoming_exams(user_id)

    # 3️⃣ ANALYTICS LAYER
    subject_analysis = classify_subjects(subject_data)
    focus_percent = calculate_focus_efficiency(focus_sessions)
    burnout_status = calculate_burnout_risk(user_id)

    # 4️⃣ INSIGHTS ENGINE
    insights = generate_insights(
        subject_analysis,
        focus_percent,
        burnout_status
    )

    # 5️⃣ DATA FOR CHARTS
    subject_labels = [s['subject'] for s in subject_data]
    subject_scores = [s['percentage'] for s in subject_data]

    weak_count = len([s for s in subject_analysis if s['level'] == 'Weak'])
    
    # FETCH EXAMS
    upcoming_exams = get_upcoming_exams(user_id)

    # CALCULATE PRIORITY
    priority_list = calculate_priority(subject_data, upcoming_exams)

    return render_template(
    'dashboard.html',
    user=session,
    weak_count=weak_count,
    focus=focus_percent,
    burnout=burnout_status,
    upcoming_exams=len(upcoming_exams),
    subject_labels=subject_labels,
    subject_scores=subject_scores,
    insights=insights,
    priorities=priority_list   # 🔥 NEW
)
