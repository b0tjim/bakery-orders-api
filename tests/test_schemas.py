from datetime import UTC, datetime
from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.models import Order, OrderItem
from app.schemas import OrderCreate, OrderRead


def test_order_create_accepts_valid_payload():
    order = OrderCreate(
        customer_name="Ada",
        items=[{"product": "Apple pie", "quantity": 2, "unit_price": "18.50"}],
    )
    assert order.items[0].unit_price == Decimal("18.50")


@pytest.mark.parametrize(
    "payload",
    [
        {
            "customer_name": "",
            "items": [{"product": "Pie", "quantity": 1, "unit_price": "5"}],
        },
        {"customer_name": "Ada", "items": []},
        {
            "customer_name": "Ada",
            "items": [{"product": "Pie", "quantity": 0, "unit_price": "5"}],
        },
        {
            "customer_name": "Ada",
            "items": [{"product": "Pie", "quantity": 1, "unit_price": "-1"}],
        },
    ],
)
def test_order_create_rejects_invalid_payload(payload):
    with pytest.raises(ValidationError):
        OrderCreate(**payload)


def test_order_read_builds_from_orm_object():
    order = Order(
        id=1,
        customer_name="Ada",
        status="pending",
        created_at=datetime.now(UTC),
        items=[OrderItem(id=1, product="Pie", quantity=1, unit_price=Decimal("5.00"))],
    )
    read = OrderRead.model_validate(order)
    assert read.status == "pending"
    assert read.items[0].product == "Pie"
