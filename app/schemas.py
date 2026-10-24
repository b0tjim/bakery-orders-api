"""Pydantic schemas: what clients send and what the API returns."""

from datetime import datetime
from decimal import Decimal
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class OrderStatus(StrEnum):
    pending = "pending"
    baking = "baking"
    ready = "ready"
    picked_up = "picked_up"
    cancelled = "cancelled"


class OrderItemCreate(BaseModel):
    product: str = Field(min_length=1, max_length=100)
    quantity: int = Field(gt=0, le=100)
    unit_price: Decimal = Field(gt=0, max_digits=8, decimal_places=2)


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=100)
    items: list[OrderItemCreate] = Field(min_length=1)


class OrderItemRead(OrderItemCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int


class OrderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_name: str
    status: OrderStatus
    created_at: datetime
    items: list[OrderItemRead]


class OrderStatusUpdate(BaseModel):
    status: OrderStatus
