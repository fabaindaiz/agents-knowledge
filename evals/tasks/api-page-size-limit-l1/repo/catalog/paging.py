def next_offset(offset, page_size, total):
    return offset + page_size if offset + page_size < total else None
