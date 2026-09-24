class PaymentGateway:
    def __init__(self):
        self.charges = []
        self.refunds = []
        self._by_key = {}

    def charge(self, customer_id, amount_cents, idempotency_key=None):
        if amount_cents <= 0:
            raise ValueError("amount must be positive")
        if idempotency_key is not None and idempotency_key in self._by_key:
            return self._by_key[idempotency_key]
        charge_id = f"ch_{len(self.charges) + 1}"
        self.charges.append((charge_id, customer_id, amount_cents))
        if idempotency_key is not None:
            self._by_key[idempotency_key] = charge_id
        return charge_id

    def refund(self, charge_id):
        self.refunds.append(charge_id)
        return f"re_{len(self.refunds)}"

    def total_charged(self, customer_id):
        return sum(amount for _, cust, amount in self.charges if cust == customer_id)
