from flask import Flask, redirect
from config import SQLALCHEMY_DATABASE_URI
from init_db import init_db
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.marks_routes import marks_bp
from routes.study_routes import study_bp
from routes.burnout_routes import burnout_bp
from routes.planner_routes import planner_bp
from routes.subject_routes import subject_bp

from extensions import db

app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize SQLAlchemy with the app
db.init_app(app)


@app.route('/')
def home():
    return redirect('/login')


# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(marks_bp)
app.register_blueprint(study_bp)
app.register_blueprint(burnout_bp)
app.register_blueprint(planner_bp)
app.register_blueprint(subject_bp)

# Initialize SQLite DB (keeps local copy) and ensure MySQL tables can be created later
init_db()

if __name__ == "__main__":
    app.run(debug=True)
