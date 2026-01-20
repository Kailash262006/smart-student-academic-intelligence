from datetime import datetime

def calculate_priority(subjects, exams):
    priorities = []

    for exam in exams:
        subject = exam['subject']
        exam_date = datetime.strptime(exam['exam_date'], '%Y-%m-%d')
        days_left = (exam_date - datetime.now()).days

        # ✅ SAFE subject percentage lookup
        subject_data = next(
            (s for s in subjects if s['subject'] == subject),
            None
        )

        # If marks not yet added, assume weakest
        if subject_data:
            subject_pct = subject_data['percentage']
        else:
            subject_pct = 0  # no marks yet

        weakness_score = 100 - subject_pct

        if days_left <= 7:
            urgency = 40
        elif days_left <= 14:
            urgency = 20
        else:
            urgency = 10

        priority_score = weakness_score + urgency

        priorities.append({
            'subject': subject,
            'priority_score': priority_score,
            'days_left': days_left
        })

    priorities.sort(key=lambda x: x['priority_score'], reverse=True)
    return priorities
