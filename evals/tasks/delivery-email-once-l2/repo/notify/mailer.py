class Mailer:
    def __init__(self):
        self.sent = []

    def send(self, to, body):
        self.sent.append((to, body))
