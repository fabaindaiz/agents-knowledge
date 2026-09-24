import unittest
from notify.shared import SharedStore
from notify.worker import Worker


class Mailer:
    def __init__(self):
        self.sent = []

    def send(self, to, body):
        self.sent.append((to, body))


class HandleTest(unittest.TestCase):
    def test_sends(self):
        m = Mailer()
        Worker(SharedStore(), m).handle({"event_id": "e1", "order_id": "o1", "email": "a@x.test"})
        self.assertEqual(len(m.sent), 1)
