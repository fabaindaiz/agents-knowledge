class Shipping:
    def __init__(self, orders, notifier):
        self.orders = orders          # order_id -> {"status": ..., "email": ...}
        self.notifier = notifier

    def mark_shipped(self, order_id, tracking_no):
        order = self.orders[order_id]
        if order["status"] != "paid":
            raise ValueError(f"order {order_id} is {order['status']}, not paid")
        order["status"] = "shipped"
        order["tracking_no"] = tracking_no
        return order
