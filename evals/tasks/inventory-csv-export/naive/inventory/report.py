from typing import Iterable

from .models import Item


def summary(items: Iterable[Item]) -> dict:
    items = list(items)
    return {
        "skus": len(items),
        "units": sum(i.quantity for i in items),
        "value_cents": sum(i.quantity * i.price_cents for i in items),
    }


def export_csv(items, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("sku,name,quantity,price\n")
        for i in items:
            f.write(f"{i.sku},{i.name},{i.quantity},{i.price_cents / 100:.2f}\n")
