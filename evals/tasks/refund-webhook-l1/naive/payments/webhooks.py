from .handlers import charges


class WebhookHandler:
    """Receives events from the payment provider."""

    def __init__(self, ledger, state=None):
        self.ledger = ledger
        self.state = state if state is not None else {}

    def handle(self, event):
        kind = event["type"]
        if kind == "ping":
            return "pong"
        if kind == "charge.succeeded":
            return charges.charge_succeeded(self.ledger, self.state, event)
        if kind == "refund.approved":
            self.ledger.credit(event["customer_id"], event["amount_cents"], f"refund {event['id']}")
            return "ok"
        raise ValueError(f"unhandled event type {kind}")
