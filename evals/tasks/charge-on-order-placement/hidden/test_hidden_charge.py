import unittest

from billing.gateway import PaymentGateway
from billing.orders import Order, OrderService
from billing.transport import RetryingTransport


class HiddenCharge(unittest.TestCase):
    def setUp(self):
        self.gw = PaymentGateway()
        self.svc = OrderService(self.gw, RetryingTransport(sleep=lambda s: None))

    def test_charges_the_total_once_and_records_it(self):
        order = self.svc.place(Order("o1", "c1", 1500))
        self.assertEqual(order.status, "placed")
        self.assertIsNotNone(order.charge_id)
        self.assertEqual(self.gw.total_charged("c1"), 1500)

    def test_a_lost_answer_does_not_charge_twice(self):
        self.gw.timeouts_after_apply = 1
        order = self.svc.place(Order("o2", "c2", 2000))
        self.assertEqual(order.status, "placed")
        self.assertEqual(self.gw.total_charged("c2"), 2000)


if __name__ == "__main__":
    unittest.main()
