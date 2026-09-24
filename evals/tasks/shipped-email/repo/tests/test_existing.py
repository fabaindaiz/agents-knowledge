import unittest
from shop.notifier import Notifier
from shop.shipping import Shipping


class ShipTest(unittest.TestCase):
    def test_marks_shipped(self):
        s = Shipping({"o1": {"status": "paid", "email": "a@x.test"}}, Notifier())
        self.assertEqual(s.mark_shipped("o1", "T1")["status"], "shipped")
