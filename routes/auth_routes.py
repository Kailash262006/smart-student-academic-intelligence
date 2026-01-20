from flask import Blueprint, render_template, request, redirect, session
from models.user_model import get_user_by_email, create_user
from utils.auth import hash_password, verify_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = get_user_by_email(email)

        if not user:
            return render_template('login.html', error="User not found")

        if not verify_password(password, user['password']):
            return render_template('login.html', error="Incorrect password")

        session['user_id'] = user['user_id']
        session['name'] = user['name']
        return redirect('/dashboard')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']

        # 🔍 Check if email already exists
        existing_user = get_user_by_email(email)
        if existing_user:
            return render_template(
                'register.html',
                error="Email already registered. Please login."
            )

        create_user(
            request.form['name'],
            email,
            hash_password(request.form['password']),
            request.form['department'],
            request.form['semester']
        )

        return redirect('/login')

    return render_template('register.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
