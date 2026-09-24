import time


class WebhookHandler:
    """Receives events from the payment provider."""

    def __init__(self, ledger, state=None):
        self.ledger = ledger
        self.state = state if state is not None else {}

    def handle(self, event):
        kind = event["type"]
        if kind == "ping":
            self.state["last_ping"] = time.time()
            return "pong"
        if kind == "charge.succeeded":
            self.ledger.record_payment(event["customer_id"], event["amount_cents"], event["id"])
            return "ok"
        raise ValueError(f"unhandled event type {kind}")
