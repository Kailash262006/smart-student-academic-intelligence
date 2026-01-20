from models.study_model import get_last_7_days_focus
from models.mood_model import get_avg_mood

def calculate_burnout_risk(user_id):
    avg_focus = get_last_7_days_focus(user_id)
    avg_mood = get_avg_mood(user_id)

    if avg_focus < 50 and avg_mood <= 2:
        return "HIGH"

    if 50 <= avg_focus <= 70 and avg_mood == 3:
        return "MEDIUM"

    return "LOW"
