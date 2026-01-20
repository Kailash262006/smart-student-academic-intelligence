from flask import Flask, redirect
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.marks_routes import marks_bp
from routes.study_routes import study_bp
from routes.burnout_routes import burnout_bp
from routes.planner_routes import planner_bp
from routes.subject_routes import subject_bp

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route('/')
def home():
    return redirect('/login')

# 🔥 THIS LINE IS THE KEY 🔥
app.register_blueprint(auth_bp)

app.register_blueprint(dashboard_bp)
app.register_blueprint(marks_bp)
app.register_blueprint(study_bp)
app.register_blueprint(burnout_bp)
app.register_blueprint(planner_bp)
app.register_blueprint(subject_bp)

if __name__ == "__main__":
    app.run(debug=True)
