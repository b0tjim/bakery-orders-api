"""Order endpoints: create, list, fetch and update the status of orders."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Order, OrderItem
from app.schemas import OrderCreate, OrderRead, OrderStatus, OrderStatusUpdate

DbSession = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate, db: DbSession) -> Order:
    order = Order(
        customer_name=payload.customer_name,
        items=[OrderItem(**item.model_dump()) for item in payload.items],
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("", response_model=list[OrderRead])
def list_orders(db: DbSession, status: OrderStatus | None = None) -> list[Order]:
    query = select(Order).order_by(Order.id)
    if status is not None:
        query = query.where(Order.status == status)
    return list(db.scalars(query))


@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: DbSession) -> Order:
    order = db.get(Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.patch("/{order_id}/status", response_model=OrderRead)
def update_order_status(
    order_id: int, payload: OrderStatusUpdate, db: DbSession
) -> Order:
    order = db.get(Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = payload.status
    db.commit()
    db.refresh(order)
    return order
