def classify_subjects(subject_data):
    """
    subject_data = [
      {'subject': 'Maths', 'percentage': 72},
      {'subject': 'Physics', 'percentage': 48}
    ]
    """

    results = []

    for s in subject_data:
        pct = s['percentage']

        if pct < 50:
            level = 'Weak'
        elif pct <= 75:
            level = 'Medium'
        else:
            level = 'Strong'

        results.append({
            'subject': s['subject'],
            'percentage': pct,
            'level': level
        })

    return results
