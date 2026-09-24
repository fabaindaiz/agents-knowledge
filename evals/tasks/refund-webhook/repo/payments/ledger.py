class Ledger:
    """Customer balances. `credit` moves money: it is not reversible from here."""

    def __init__(self):
        self.balances = {}
        self.entries = []

    def credit(self, customer_id, amount_cents, memo):
        self.balances[customer_id] = self.balances.get(customer_id, 0) + amount_cents
        self.entries.append((customer_id, amount_cents, memo))
