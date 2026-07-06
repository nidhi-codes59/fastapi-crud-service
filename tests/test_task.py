from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "UP"


def test_create_task():
    payload = {
        "title": "Complete API development",
        "description": "Build Task Management API",
        "priority": "High",
        "assignee": "Nidhi",
        "due_date": "2026-07-15"
    }

    response = client.post("/tasks", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


def test_get_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200


def test_get_task_by_id():
    response = client.get("/tasks/1")
    assert response.status_code in [200, 404]


def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code in [200, 404]
