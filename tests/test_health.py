import os

os.environ.setdefault("DATABASE_URL", "postgresql://toggle:toggle@localhost:5432/toggledb")
os.environ.setdefault("AUTH_SERVICE_URL", "http://localhost:9999")

from app import app


def test_health_returns_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
