class WebhookHandler:
    """Receives events from the payment provider. The provider delivers each event at least once,
    each with a unique `id`; handlers may keep state in `self.state` (a persistent key-value store)."""

    def __init__(self, ledger, state=None):
        self.ledger = ledger
        self.state = state if state is not None else {}

    def handle(self, event):
        kind = event["type"]
        if kind == "ping":
            return "pong"
        raise ValueError(f"unhandled event type {kind}")
