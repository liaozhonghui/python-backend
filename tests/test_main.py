# tests/test_main.py
from fastapi.testclient import TestClient
from test_project.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}
