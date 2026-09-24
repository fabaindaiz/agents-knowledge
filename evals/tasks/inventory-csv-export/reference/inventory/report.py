import csv
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
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sku", "name", "quantity", "price"])
        for i in items:
            w.writerow([i.sku, i.name, i.quantity, f"{i.price_cents // 100}.{i.price_cents % 100:02d}"])
