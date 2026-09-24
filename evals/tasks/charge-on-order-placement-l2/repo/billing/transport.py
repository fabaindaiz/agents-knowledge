from infra.resilience import load_policy


class Transport:
    """Outbound calls to the payment provider."""

    def __init__(self):
        self.policy = load_policy("payment_provider")

    def call(self, fn, *args, **kwargs):
        return self.policy.execute(fn, *args, **kwargs)
