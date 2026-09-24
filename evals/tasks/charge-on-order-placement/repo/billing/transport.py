import time


class RetryingTransport:
    """Calls a function, retrying up to `attempts` times when it raises TimeoutError."""

    def __init__(self, attempts=3, backoff_s=0.0, sleep=time.sleep):
        self.attempts = attempts
        self.backoff_s = backoff_s
        self.sleep = sleep

    def call(self, fn, *args, **kwargs):
        for attempt in range(self.attempts):
            try:
                return fn(*args, **kwargs)
            except TimeoutError:
                if attempt == self.attempts - 1:
                    raise
                self.sleep(self.backoff_s * (2 ** attempt))
