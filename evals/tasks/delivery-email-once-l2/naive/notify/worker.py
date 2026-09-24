class Worker:
    def __init__(self, kv, mailer):
        self.kv = kv
        self.mailer = mailer
        self.seen = set()

    def handle(self, event):
        """event: {"event_id": ..., "order_id": ..., "email": ...}"""
        if event["event_id"] in self.seen:
            return
        self.seen.add(event["event_id"])
        self.kv.set(f"last-event:{event['order_id']}", event["event_id"])
        self.mailer.send(event["email"], f"Your order {event['order_id']} was delivered")
