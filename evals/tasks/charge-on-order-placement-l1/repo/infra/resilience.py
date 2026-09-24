import functools


def retry(on, attempts):
    def decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except on:
                    if attempt == attempts - 1:
                        raise
        return wrapper
    return decorate
