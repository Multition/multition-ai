from fastapi.testclient import TestClient

from multition_ai.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "multition-ai"


def test_unknown_route_returns_not_found() -> None:
    response = client.get("/not-implemented")
    assert response.status_code == 404
