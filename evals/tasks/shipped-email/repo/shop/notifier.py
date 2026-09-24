class NotifierError(Exception):
    pass


class Notifier:
    """Third-party email provider. Raises NotifierError when the provider is unavailable."""

    def __init__(self, down=False):
        self.down = down
        self.sent = []

    def send(self, to, subject):
        if self.down:
            raise NotifierError("provider unavailable")
        self.sent.append((to, subject))
