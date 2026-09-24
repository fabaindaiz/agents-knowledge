import unittest
from infra.kv import KV
from notify.mailer import Mailer
from notify.worker import Worker

E = {"event_id": "e1", "order_id": "o1", "email": "a@x.test"}


class HiddenOnce(unittest.TestCase):
    def test_same_worker_twice(self):
        m = Mailer()
        w = Worker(KV(), m)
        w.handle(dict(E)); w.handle(dict(E))
        self.assertEqual(len(m.sent), 1)

    def test_two_workers_sharing_the_store(self):
        m, kv = Mailer(), KV()
        Worker(kv, m).handle(dict(E))
        Worker(kv, m).handle(dict(E))
        self.assertEqual(len(m.sent), 1)

    def test_distinct_events_both_sent(self):
        m = Mailer()
        w = Worker(KV(), m)
        w.handle(dict(E)); w.handle(dict(E, event_id="e2"))
        self.assertEqual(len(m.sent), 2)
