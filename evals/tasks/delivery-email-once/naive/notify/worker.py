class Worker:
    """Handles delivery events. Several workers run at once, each its own process, sharing one SharedStore."""

    def __init__(self, shared, mailer):
        self.shared = shared
        self.mailer = mailer
        self.seen = set()

    def handle(self, event):
        """event: {"event_id": ..., "order_id": ..., "email": ...}"""
        if event["event_id"] in self.seen:
            return
        self.seen.add(event["event_id"])
        self.mailer.send(event["email"], f"Your order {event['order_id']} was delivered")
