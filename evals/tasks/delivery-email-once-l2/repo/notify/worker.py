class Worker:
    def __init__(self, kv, mailer):
        self.kv = kv
        self.mailer = mailer

    def handle(self, event):
        """event: {"event_id": ..., "order_id": ..., "email": ...}"""
        self.kv.set(f"last-event:{event['order_id']}", event["event_id"])
        self.mailer.send(event["email"], f"Your order {event['order_id']} was delivered")
