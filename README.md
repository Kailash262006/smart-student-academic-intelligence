# 🎓 Smart Student Academic Intelligence System

> A **full-stack academic analytics platform** that helps students understand their performance, study effectiveness, mental well-being, and exam priorities through **intelligent insights**.

---

## 🌟 Why this Project?

Students often struggle to answer questions like:
- ❓ *Which subjects am I weak in?*
- ❓ *Am I actually focused while studying?*
- ❓ *Am I mentally exhausted or close to burnout?*
- ❓ *Which exam should I prioritize first?*

This project solves these problems by **collecting student data and converting it into actionable insights** using smart analytics and a modern dashboard.

---

## 🚀 Key Features

### 🔐 Authentication
- Secure user registration & login
- Session-based access control

### 📘 Subject Management
- Dynamic subject creation
- Used consistently across all modules

### 📊 Academic Performance Analysis
- Subject-wise marks tracking
- Automatic weak/strong subject identification

### ⏱️ Study Focus Tracker
- Planned vs actual study time
- Focus efficiency calculation
- Distraction detection

### 🧠 Mood & Stress Logging
- Mood level (1–5)
- Stress level (1–5)
- Daily mental health tracking

### ⚠️ Burnout Risk Detection
- Combines mood, stress, and focus data
- Classifies burnout risk:
  - **Low**
  - **Medium**
  - **High**

### 🗓️ Exam Planner & Priority Engine
- Track upcoming exams
- Automatically prioritizes subjects based on:
  - Performance weakness
  - Exam urgency

### 📈 Smart Dashboard
- Centralized analytics view
- Academic + behavioral + mental insights
- Clean, colorful, and modern UI

---

## 🧠 What Makes It “Smart Student AI”?

> **AI here means Decision Intelligence**, not a chatbot or heavy machine learning.

The system:
- Analyzes patterns in student data
- Applies rule-based intelligence
- Generates priorities & alerts automatically
- Supports better academic decisions

This reflects how many **real-world intelligent systems** are built.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Python (Flask) |
| Frontend | HTML, CSS, JavaScript |
| Database | MySQL |
| Analytics | Rule-based decision logic |
| Architecture | Modular MVC-style design |

---

## 📂 Project Structure
```
student_academic_intelligence/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/ # DB connection, auth helpers, DB initialization
├── models/ # Database interaction logic
├── routes/ # Flask route handlers
├── analytics/ # Burnout & priority logic
├── templates/ # HTML templates
└── static/ # CSS & JavaScript
```
---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Kailash262006/smart-student-academic-intelligence.git
cd smart-student-academic-intelligence
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the application
```bash
python app.py
```
### 4️⃣ Open in browser
```bash
http://127.0.0.1:5000
```
---

## 🔮 Future Enhancements

Planned upgrades to improve intelligence and scalability:

- 🤖 Machine Learning-based burnout prediction

- 📊 Interactive charts using Chart.js

- 📄 PDF academic performance reports

- 🌐 Online deployment (Render / Railway)

- 📱 Mobile-responsive UI

- 📈 Personalized study recommendations

- 🔐 Role-based access (Student / Mentor)

---

## 👤 Author

KAILASH GOWTHAM U
- B.E. Computer Science and Engineering
- Interested in Full-Stack Development, Data Analytics

## ⭐ Final Note

- This project was built as a hands-on learning experience to understand:

- Full-stack application development

- Database design & lifecycle

- Analytics-driven decision systems

- Real-world debugging & problem solving
