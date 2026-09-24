from infra.cache import LRU

from . import db
from .serializers import page_response

_cache = LRU()


def _key(offset, page_size):
    return f"items:{offset}:{page_size}"


def list_items(offset=0, page_size=20):
    """One page of items, with the offset of the next page (None at the end)."""
    if page_size < 1:
        raise ValueError("page_size must be positive")
    page_size = min(page_size, 100)
    cached = _cache.get(_key(offset, page_size))
    if cached is not None:
        return cached
    items = db.fetch(offset, page_size)
    page = page_response(items, offset, page_size, db.count())
    _cache.put(_key(offset, page_size), page)
    return page
