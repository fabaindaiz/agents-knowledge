from typing import Iterable

from .models import Item


def summary(items: Iterable[Item]) -> dict:
    items = list(items)
    return {
        "skus": len(items),
        "units": sum(i.quantity for i in items),
        "value_cents": sum(i.quantity * i.price_cents for i in items),
    }
