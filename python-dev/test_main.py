"""
Starter tests for the interview sandbox. Run with:

    pytest test_main.py -v

Add tests for your new GET /users/{user_id}/transactions endpoint below.
At minimum, cover:
  - happy path with default pagination
  - 404 when user doesn't exist
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_get_user_found():
    resp = client.get("/users/1")
    assert resp.status_code == 200
    assert resp.json()["name"] == "Ada Lovelace"


def test_get_user_not_found():
    resp = client.get("/users/999")
    assert resp.status_code == 404


# ---------- ADD YOUR TESTS BELOW ----------