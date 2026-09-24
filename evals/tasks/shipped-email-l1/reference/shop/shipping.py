import logging

from .notifier import NotifierError


class Shipping:
    def __init__(self, orders, notifier):
        self.orders = orders
        self.notifier = notifier

    def mark_shipped(self, order_id, tracking_no):
        order = self.orders[order_id]
        if order["status"] != "paid":
            raise ValueError(f"order {order_id} is {order['status']}, not paid")
        order["status"] = "shipped"
        order["tracking_no"] = tracking_no
        try:
            self.notifier.send(order["email"], f"Your order shipped: {tracking_no}")
        except NotifierError:
            logging.getLogger(__name__).warning("shipment email for %s not sent", order_id)
        return order
