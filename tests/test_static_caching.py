from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_static_assets_are_not_cached():
    response = client.get("/static/app.js")

    assert response.status_code == 200
    cache_control = response.headers.get("Cache-Control", "")
    assert "no-store" in cache_control
