def charge_succeeded(ledger, state, event):
    key = f"seen:{event['id']}"
    if state.get(key):
        return "duplicate"
    ledger.record_payment(event["customer_id"], event["amount_cents"], event["id"])
    state[key] = True
    return "ok"
