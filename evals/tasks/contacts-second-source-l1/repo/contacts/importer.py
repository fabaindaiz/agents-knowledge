def import_crm(store, crm_rows):
    """Import contacts from the CRM export."""
    for row in crm_rows:
        store.upsert({"id": row["crm_id"], "name": row["name"], "email": row["email"], "source": "crm"})
