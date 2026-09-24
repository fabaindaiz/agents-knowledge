class Worker:
    """Handles delivery events. Several workers run at once, each its own process, sharing one SharedStore."""

    def __init__(self, shared, mailer):
        self.shared = shared
        self.mailer = mailer

    def handle(self, event):
        """event: {"event_id": ..., "order_id": ..., "email": ...}"""
        if not self.shared.add_if_absent(f"delivered-email:{event['event_id']}"):
            return
        self.mailer.send(event["email"], f"Your order {event['order_id']} was delivered")
