"""Client for the payment provider. This in-memory version reproduces the provider's documented behaviour.

charge(customer_id, amount_cents, idempotency_key=None) debits the customer and returns a charge id.
When an idempotency_key has been seen before, the provider returns the original charge id and debits
nothing. Network timeouts surface as TimeoutError.
"""


class PaymentGateway:
    def __init__(self):
        self.charges = []
        self._by_key = {}
        self.timeouts_after_apply = 0  # simulates the provider applying a charge and the answer being lost

    def charge(self, customer_id, amount_cents, idempotency_key=None):
        if amount_cents <= 0:
            raise ValueError("amount must be positive")
        if idempotency_key is not None and idempotency_key in self._by_key:
            return self._by_key[idempotency_key]
        charge_id = f"ch_{len(self.charges) + 1}"
        self.charges.append((charge_id, customer_id, amount_cents))
        if idempotency_key is not None:
            self._by_key[idempotency_key] = charge_id
        if self.timeouts_after_apply:
            self.timeouts_after_apply -= 1
            raise TimeoutError("the provider did not answer in time")
        return charge_id

    def total_charged(self, customer_id):
        return sum(amount for _, cust, amount in self.charges if cust == customer_id)
