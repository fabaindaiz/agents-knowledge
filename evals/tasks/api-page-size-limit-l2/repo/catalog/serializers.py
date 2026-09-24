from .paging import next_offset


def page_response(items, offset, page_size, total):
    return {"items": items, "page_size": page_size, "next_offset": next_offset(offset, page_size, total)}
