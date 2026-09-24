import unittest
from payments.ledger import Ledger
from payments.webhooks import WebhookHandler


class PingTest(unittest.TestCase):
    def test_ping(self):
        self.assertEqual(WebhookHandler(Ledger()).handle({"id": "e0", "type": "ping"}), "pong")
