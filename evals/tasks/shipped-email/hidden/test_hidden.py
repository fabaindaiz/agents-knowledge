import unittest
from shop.notifier import Notifier
from shop.shipping import Shipping


class HiddenShipping(unittest.TestCase):
    def test_emails_when_the_provider_is_up(self):
        n = Notifier()
        Shipping({"o1": {"status": "paid", "email": "a@x.test"}}, n).mark_shipped("o1", "T1")
        self.assertEqual(len(n.sent), 1)
        self.assertIn("a@x.test", n.sent[0])

    def test_ships_when_the_provider_is_down(self):
        orders = {"o1": {"status": "paid", "email": "a@x.test"}}
        Shipping(orders, Notifier(down=True)).mark_shipped("o1", "T1")
        self.assertEqual(orders["o1"]["status"], "shipped")
        self.assertEqual(orders["o1"]["tracking_no"], "T1")
