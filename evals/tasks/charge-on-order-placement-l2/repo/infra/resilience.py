import json
import os

_ERRORS = {"timeout": TimeoutError, "connection": ConnectionError}
_CONFIG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "outbound.json")


class Policy:
    def __init__(self, attempts=1, retry_on=()):
        self.attempts = attempts
        self.retry_on = tuple(_ERRORS[name] for name in retry_on)

    def execute(self, fn, *args, **kwargs):
        for attempt in range(self.attempts):
            try:
                return fn(*args, **kwargs)
            except self.retry_on:
                if attempt == self.attempts - 1:
                    raise


def load_policy(name):
    with open(_CONFIG) as f:
        return Policy(**json.load(f).get(name, {}))
