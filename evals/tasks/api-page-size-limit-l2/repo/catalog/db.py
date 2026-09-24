ROWS = [{"id": i, "name": f"item {i}"} for i in range(1, 1001)]


def fetch(offset, limit):
    return ROWS[offset:offset + limit]


def count():
    return len(ROWS)
