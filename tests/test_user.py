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

def test_change_role(client):    
    client.post('/api/register', json={
        'email': 'user@4example.com',
        'password': 'password123'
    })
    response = client.post('/api/login', json={
        'email': 'user@4example.com',
        'password': 'password123'
    })
    user_id = json.loads(response.data)['data']['id']
    client.post('/api/register', json={
        'email': 'admin@5example.com',
        'password': 'password123',
        'role': 'admin'
    })
    response = client.post('/api/login', json={
        'email': 'admin@5example.com',
        'password': 'password123'
    })

    token = json.loads(response.data)['data']['token']

    response = client.put(f'/api/users/{user_id}/role', headers={
        'Authorization': f'Bearer {token}'
    }, json={
        'role': 'admin'
    })
    assert response.status_code == 200
    assert b"successfully" in response.data
