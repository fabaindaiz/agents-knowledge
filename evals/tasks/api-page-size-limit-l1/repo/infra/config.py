import json
import os

_DEFAULTS = {"environment": "development", "region": "local"}


def load(path=None):
    """Settings from a JSON file named by APP_CONFIG, over the defaults."""
    data = dict(_DEFAULTS)
    path = path or os.environ.get("APP_CONFIG")
    if path and os.path.exists(path):
        with open(path) as f:
            data.update(json.load(f))
    return data
