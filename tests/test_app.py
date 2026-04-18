from app import app, db
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
        
def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_info():
    client = app.test_client()
    response = client.get("/info")
    assert response.status_code == 200
    assert "app" in response.json

def test_echo():
    client = app.test_client()
    response = client.post("/echo", json={"message": "hello"})
    assert response.status_code == 200
    assert response.json["received"]["message"] == "hello"

def test_add_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Test"})
    assert response.status_code == 201

def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200