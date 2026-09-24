class Payments:
    def __init__(self, orders, notifier):
        self.orders = orders
        self.notifier = notifier

    def mark_paid(self, order_id, amount_cents):
        order = self.orders[order_id]
        order["status"] = "paid"
        order["paid_cents"] = amount_cents
        return order
