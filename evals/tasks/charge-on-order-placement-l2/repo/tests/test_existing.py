import unittest
from billing.gateway import PaymentGateway
from billing.orders import Order, OrderService
from billing.transport import Transport


class PlaceTest(unittest.TestCase):
    def test_places_a_new_order(self):
        svc = OrderService(PaymentGateway(), Transport())
        self.assertEqual(svc.place(Order("o1", "c1", 1500)).status, "placed")

    def test_rejects_an_empty_order(self):
        with self.assertRaises(ValueError):
            OrderService(PaymentGateway(), Transport()).place(Order("o2", "c1", 0))
