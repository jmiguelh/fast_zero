from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app

client = TestClient(app)


def test_root_ok():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
