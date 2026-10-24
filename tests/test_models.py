from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import Base
from app.models import Order, OrderItem


def test_order_persists_with_items():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        order = Order(
            customer_name="Ada",
            items=[
                OrderItem(product="Apple pie", quantity=2, unit_price=Decimal("18.50"))
            ],
        )
        session.add(order)
        session.commit()

        saved = session.get(Order, order.id)
        assert saved.status == "pending"
        assert saved.created_at is not None
        assert saved.items[0].product == "Apple pie"
        assert saved.items[0].unit_price == Decimal("18.50")
