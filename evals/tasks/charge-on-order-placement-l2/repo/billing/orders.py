from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    id: str
    customer_id: str
    total_cents: int
    status: str = "new"
    charge_id: Optional[str] = None


class OrderService:
    def __init__(self, gateway, transport):
        self.gateway = gateway
        self.transport = transport

    def place(self, order: Order) -> Order:
        if order.total_cents <= 0:
            raise ValueError("an order must have a positive total")
        if order.status != "new":
            raise ValueError(f"order {order.id} is already {order.status}")
        order.status = "placed"
        return order

    def cancel(self, order: Order) -> Order:
        if order.status != "placed":
            raise ValueError(f"order {order.id} is {order.status}")
        if order.charge_id:
            self.transport.call(self.gateway.refund, order.charge_id)
        order.status = "cancelled"
        return order
