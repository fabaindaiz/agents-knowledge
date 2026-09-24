import unittest
from billing.gateway import PaymentGateway
from billing.orders import Order, OrderService
from billing.transport import Transport


class LosesOneAnswer(PaymentGateway):
    """The provider applies the charge and the response is lost once."""

    def __init__(self):
        super().__init__()
        self.lose = 0

    def charge(self, *args, **kwargs):
        result = super().charge(*args, **kwargs)
        if self.lose:
            self.lose -= 1
            raise TimeoutError("read timed out")
        return result


class HiddenCharge(unittest.TestCase):
    def setUp(self):
        self.gw = LosesOneAnswer()
        self.svc = OrderService(self.gw, Transport())

    def test_charges_the_total_once_and_records_it(self):
        order = self.svc.place(Order("o1", "c1", 1500))
        self.assertEqual(order.status, "placed")
        self.assertIsNotNone(order.charge_id)
        self.assertEqual(self.gw.total_charged("c1"), 1500)

    def test_a_lost_answer_does_not_charge_twice(self):
        self.gw.lose = 1
        order = self.svc.place(Order("o2", "c2", 2000))
        self.assertEqual(order.status, "placed")
        self.assertEqual(self.gw.total_charged("c2"), 2000)
