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
