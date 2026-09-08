from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_list_users_returns_custom_headers() -> None:
    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) >= 3
    assert response.headers["X-App-Name"] == "device_systems"
    assert response.headers["X-API-Version"] == "1.0"


def test_filters_users_by_role_and_status() -> None:
    response = client.get("/users", params={"role": "admin", "is_active": "true"})

    assert response.status_code == 200
    assert all(user["role"] == "admin" and user["is_active"] for user in response.json())


def test_get_user_by_id_returns_404_when_missing() -> None:
    response = client.get("/users/999")

    assert response.status_code == 404


def test_create_user_validates_and_rejects_duplicate_email() -> None:
    payload = {
        "name": "Ana Torres",
        "email": "ana.torres@example.com",
        "role": "support",
        "is_active": True,
    }

    created_response = client.post("/users", json=payload)
    duplicate_response = client.post("/users", json=payload)

    assert created_response.status_code == 201
    assert created_response.json()["name"] == "Ana Torres"
    assert duplicate_response.status_code == 409


def test_create_user_rejects_short_name() -> None:
    response = client.post(
        "/users",
        json={"name": "AB", "email": "valid@example.com", "role": "user"},
    )

    assert response.status_code == 422
