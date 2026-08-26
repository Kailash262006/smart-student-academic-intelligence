from app import app
from models.user_model import create_user
from utils.auth import hash_password

with app.app_context():
    # create a test user with hashed password
    try:
        u = create_user('LoginTest', 'logintest@example.com', hash_password('secret123'), 'CS', 1)
    except Exception:
        # user may already exist
        pass

with app.test_client() as client:
    resp = client.post('/login', data={'email':'logintest@example.com','password':'secret123'}, follow_redirects=True)
    print('POST /login ->', resp.status_code)
    print(resp.data.decode('utf-8')[:400])
