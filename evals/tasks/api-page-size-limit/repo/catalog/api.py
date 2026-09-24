from .db import ROWS


def list_items(offset=0, page_size=20):
    """One page of items, with the offset of the next page (None at the end)."""
    if page_size < 1:
        raise ValueError("page_size must be positive")
    items = ROWS[offset:offset + page_size]
    next_offset = offset + page_size if offset + page_size < len(ROWS) else None
    return {"items": items, "page_size": page_size, "next_offset": next_offset}
