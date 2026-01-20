def calculate_focus_efficiency(study_sessions):
    """
    study_sessions = [
      {'planned': 120, 'actual': 90},
      {'planned': 60, 'actual': 30}
    ]
    """

    total_planned = sum(s['planned'] for s in study_sessions)
    total_actual = sum(s['actual'] for s in study_sessions)

    if total_planned == 0:
        return 0

    efficiency = (total_actual / total_planned) * 100
    return round(efficiency)
