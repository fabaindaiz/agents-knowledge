class SharedStore:
    """Key-value state shared by every worker process (production: the shared cache service)."""

    def __init__(self):
        self._data = {}

    def add_if_absent(self, key):
        """Atomically record `key`. True if it was new, False if some worker already added it."""
        if key in self._data:
            return False
        self._data[key] = True
        return True

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
