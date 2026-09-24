class LRU:
    def __init__(self, size=128):
        self.size = size
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def put(self, key, value):
        if len(self.data) >= self.size:
            self.data.pop(next(iter(self.data)))
        self.data[key] = value
