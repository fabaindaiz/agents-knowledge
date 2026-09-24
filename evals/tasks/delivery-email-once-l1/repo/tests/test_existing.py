import unittest
from infra.kv import KV
from notify.mailer import Mailer
from notify.worker import Worker


class HandleTest(unittest.TestCase):
    def test_sends(self):
        m = Mailer()
        Worker(KV(), m).handle({"event_id": "e1", "order_id": "o1", "email": "a@x.test"})
        self.assertEqual(len(m.sent), 1)
