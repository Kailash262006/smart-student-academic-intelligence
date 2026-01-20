def generate_insights(subjects, focus, burnout):
    insights = []

    weak_subjects = [s['subject'] for s in subjects if s['level'] == 'Weak']

    if weak_subjects:
        insights.append(
            f"📌 Focus more on {', '.join(weak_subjects)} — performance is below average."
        )

    if focus < 50:
        insights.append(
            "⏱ Your focus efficiency is low. Try shorter study sessions with breaks."
        )
    elif focus > 80:
        insights.append(
            "🔥 Excellent focus efficiency! Your study strategy is working."
        )

    if burnout == "HIGH":
        insights.append(
            "⚠ High burnout risk detected. Reduce workload and take rest."
        )
    elif burnout == "MEDIUM":
        insights.append(
            "⚠ Moderate burnout risk. Balance study and relaxation."
        )

    if not insights:
        insights.append("✅ You're doing great! Keep up the consistency.")

    return insights
