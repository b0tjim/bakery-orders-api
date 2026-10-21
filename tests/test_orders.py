import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

PAYLOAD = {
    "customer_name": "Ada",
    "items": [{"product": "Apple pie", "quantity": 2, "unit_price": "18.50"}],
}


@pytest.fixture
def client():
    # StaticPool keeps one in-memory SQLite connection shared across requests.
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    TestingSession = sessionmaker(bind=engine, expire_on_commit=False)

    def override_get_db():
        with TestingSession() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_create_then_get_order(client):
    created = client.post("/orders", json=PAYLOAD)

    assert created.status_code == 201
    body = created.json()
    assert body["status"] == "pending"
    assert body["items"][0]["product"] == "Apple pie"

    fetched = client.get(f"/orders/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == body


def test_get_missing_order_returns_404(client):
    assert client.get("/orders/999").status_code == 404


def test_create_order_with_no_items_returns_422(client):
    response = client.post("/orders", json={"customer_name": "Ada", "items": []})

    assert response.status_code == 422


def test_list_orders_filters_by_status(client):
    first = client.post("/orders", json=PAYLOAD).json()
    second = client.post("/orders", json=PAYLOAD).json()
    client.patch(f"/orders/{second['id']}/status", json={"status": "ready"})

    everything = client.get("/orders").json()
    ready = client.get("/orders", params={"status": "ready"}).json()

    assert [o["id"] for o in everything] == [first["id"], second["id"]]
    assert [o["id"] for o in ready] == [second["id"]]


def test_list_orders_rejects_unknown_status(client):
    assert client.get("/orders", params={"status": "burnt"}).status_code == 422


def test_update_status(client):
    order = client.post("/orders", json=PAYLOAD).json()

    response = client.patch(f"/orders/{order['id']}/status", json={"status": "baking"})

    assert response.status_code == 200
    assert response.json()["status"] == "baking"


def test_update_status_missing_order_returns_404(client):
    response = client.patch("/orders/999/status", json={"status": "baking"})

    assert response.status_code == 404
