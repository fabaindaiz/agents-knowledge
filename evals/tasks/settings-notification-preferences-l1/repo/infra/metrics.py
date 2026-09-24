from collections import Counter

_counters = Counter()


def incr(name, value=1):
    _counters[name] += value


def snapshot():
    return dict(_counters)
