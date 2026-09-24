import unittest
from payments.ledger import Ledger
from payments.webhooks import WebhookHandler

EV = {"id": "evt_1", "type": "refund.approved", "customer_id": "c1", "amount_cents": 500}


class HiddenRefund(unittest.TestCase):
    def test_redelivery_credits_once(self):
        ledger, state = Ledger(), {}
        WebhookHandler(ledger, state).handle(dict(EV))
        WebhookHandler(ledger, state).handle(dict(EV))
        self.assertEqual(ledger.balances["c1"], 500)

    def test_two_events_both_credit(self):
        ledger = Ledger()
        h = WebhookHandler(ledger)
        h.handle(dict(EV)); h.handle(dict(EV, id="evt_2"))
        self.assertEqual(ledger.balances["c1"], 1000)
