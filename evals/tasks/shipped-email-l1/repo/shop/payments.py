from infra import log

from .notifier import NotifierError

_log = log.get(__name__)


class Payments:
    def __init__(self, orders, notifier):
        self.orders = orders
        self.notifier = notifier

    def mark_paid(self, order_id, amount_cents):
        order = self.orders[order_id]
        order["status"] = "paid"
        order["paid_cents"] = amount_cents
        try:
            self.notifier.send(order["email"], f"Receipt for {order_id}")
        except NotifierError:
            _log.warning("receipt for %s not sent", order_id)
        return order
