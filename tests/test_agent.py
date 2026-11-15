
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_agent_endpoint():
    response = client.post(
        "/agent/run",
        json={"question": "What is CI/CD?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["question"] == "What is CI/CD?"
    assert "AI Agent received" in data["response"]
