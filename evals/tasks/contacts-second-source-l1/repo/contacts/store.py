class Store:
    def __init__(self):
        self.rows = {}

    def upsert(self, record):
        self.rows[record["id"]] = dict(record)
