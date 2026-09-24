import unittest
from notify.shared import SharedStore
from notify.worker import Worker


class Mailer:
    def __init__(self):
        self.sent = []

    def send(self, to, body):
        self.sent.append((to, body))


E = {"event_id": "e1", "order_id": "o1", "email": "a@x.test"}


class HiddenOnce(unittest.TestCase):
    def test_same_worker_twice(self):
        m = Mailer()
        w = Worker(SharedStore(), m)
        w.handle(dict(E)); w.handle(dict(E))
        self.assertEqual(len(m.sent), 1)

    def test_two_workers_sharing_the_store(self):
        m, shared = Mailer(), SharedStore()
        Worker(shared, m).handle(dict(E))
        Worker(shared, m).handle(dict(E))
        self.assertEqual(len(m.sent), 1)

    def test_distinct_events_both_sent(self):
        m = Mailer()
        w = Worker(SharedStore(), m)
        w.handle(dict(E)); w.handle(dict(E, event_id="e2"))
        self.assertEqual(len(m.sent), 2)
