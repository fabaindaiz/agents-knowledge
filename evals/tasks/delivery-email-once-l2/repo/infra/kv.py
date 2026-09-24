class KV:
    def __init__(self):
        self._data = {}

    @classmethod
    def connect(cls, url=None):
        return cls()

    def add_if_absent(self, key):
        if key in self._data:
            return False
        self._data[key] = True
        return True

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
