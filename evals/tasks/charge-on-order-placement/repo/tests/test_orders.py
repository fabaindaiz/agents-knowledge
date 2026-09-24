import unittest

from billing.gateway import PaymentGateway
from billing.orders import Order, OrderService
from billing.transport import RetryingTransport


class PlaceTest(unittest.TestCase):
    def setUp(self):
        self.svc = OrderService(PaymentGateway(), RetryingTransport(sleep=lambda s: None))

    def test_places_a_new_order(self):
        order = self.svc.place(Order("o1", "c1", 1500))
        self.assertEqual(order.status, "placed")

    def test_rejects_an_empty_order(self):
        with self.assertRaises(ValueError):
            self.svc.place(Order("o2", "c1", 0))


if __name__ == "__main__":
    unittest.main()
