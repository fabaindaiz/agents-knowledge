class Worker:
    def __init__(self, kv, mailer):
        self.kv = kv
        self.mailer = mailer

    def handle(self, event):
        """event: {"event_id": ..., "order_id": ..., "email": ...}"""
        if not self.kv.add_if_absent(f"delivered-email:{event['event_id']}"):
            return
        self.kv.set(f"last-event:{event['order_id']}", event["event_id"])
        self.mailer.send(event["email"], f"Your order {event['order_id']} was delivered")
