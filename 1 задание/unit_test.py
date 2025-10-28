from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 400
    assert response.data == b'Hello'

def test_about():
    client = app.test_client()
    response = client.get('/abot')
    assert response.status_code == 200
    assert response.data == b'This is a simple Flask app.'

def test_ping():
    client = app.test_client()
    response = client.get('/ping')
    assert response.data == b'Ping'
