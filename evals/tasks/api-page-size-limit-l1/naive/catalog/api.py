from . import db
from .serializers import page_response


def list_items(offset=0, page_size=20):
    """One page of items, with the offset of the next page (None at the end)."""
    if page_size < 1:
        raise ValueError("page_size must be positive")
    items = db.fetch(offset, min(page_size, 100))
    return page_response(items, offset, page_size, db.count())
