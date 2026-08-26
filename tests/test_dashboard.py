from app import app
from models.user_model import create_user
from utils.auth import hash_password

with app.app_context():
    try:
        create_user('DashTest', 'dashtest@example.com', hash_password('secret123'), 'CS', 1)
    except Exception:
        pass

with app.test_client() as client:
    # login
    resp = client.post('/login', data={'email':'dashtest@example.com','password':'secret123'}, follow_redirects=True)
    print('login', resp.status_code)
    # access dashboard
    resp = client.get('/dashboard')
    print('/dashboard', resp.status_code)
    print(resp.data.decode('utf-8')[:400])
