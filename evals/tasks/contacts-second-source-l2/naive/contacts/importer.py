def import_crm(store, crm_rows):
    """Import contacts from the CRM export."""
    for row in crm_rows:
        store.upsert({"id": row["crm_id"], "name": row["name"], "email": row["email"], "source": "crm"})


def import_shop(store, shop_rows):
    for row in shop_rows:
        store.upsert({"id": row["customer_no"], "name": row["full_name"], "email": row["mail"], "source": "shop"})
