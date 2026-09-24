class Store:
    """The contacts table. `upsert` inserts or replaces the record with the same `id`."""

    def __init__(self):
        self.rows = {}

    def upsert(self, record):
        self.rows[record["id"]] = dict(record)


def import_crm(store, crm_rows):
    """Import contacts from the CRM export. CRM rows look like {"crm_id": 17, "name": ..., "email": ...}."""
    for row in crm_rows:
        store.upsert({"id": f"crm:{row['crm_id']}", "name": row["name"], "email": row["email"], "source": "crm"})


def import_shop(store, shop_rows):
    for row in shop_rows:
        store.upsert({"id": f"shop:{row['customer_no']}", "name": row["full_name"], "email": row["mail"], "source": "shop"})
