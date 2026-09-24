import datetime as dt


def now():
    return dt.datetime.now(dt.timezone.utc)
