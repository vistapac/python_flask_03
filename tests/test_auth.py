import json
import pytest
from app import create_app
from extensions import db
from models.user import User

@pytest.fixture(scope='function')
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/py01'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register(client):
    response = client.post('/api/register', json={
        'email': 'user@1example.com',
        'password': 'password123'
    })

    assert response.status_code == 201
    data = json.loads(response.data)  # 解析 JSON 数据
    assert "User registered successfully" in data['message']

def test_login(client):
    client.post('/api/register', json={
        'email': 'user@2example.com',
        'password': 'password123'
    })
    response = client.post('/api/login', json={
        'email': 'user@2example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in json.loads(response.data)['data']


def test_get_user(client):
    client.post('/api/register', json={
        'email': 'user@3example.com',
        'password': 'password123'
    })
    login_response = client.post('/api/login', json={
        'email': 'user@3example.com',
        'password': 'password123'
    })
    token = json.loads(login_response.data)['data']['token']
    response = client.get('/api/user', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
    assert b"user@3example.com" in response.data
