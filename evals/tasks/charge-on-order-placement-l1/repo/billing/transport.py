from infra.resilience import retry


class Transport:
    """Outbound calls to the payment provider."""

    @retry(on=(TimeoutError, ConnectionError), attempts=3)
    def call(self, fn, *args, **kwargs):
        return fn(*args, **kwargs)
