import unittest

from watchdog.app import Watchdog


class FromEnvTest(unittest.TestCase):
    def test_reads_services_and_interval(self):
        w = Watchdog.from_env({"WATCHDOG_SERVICES": "api,db", "WATCHDOG_INTERVAL_S": "10"}, post=lambda u, p: None)
        self.assertEqual(w.services, ["api", "db"])
        self.assertEqual(w.interval_s, 10)

    def test_alerts_on_a_down_service(self):
        sent = []

        class Sink:
            def send(self, message):
                sent.append(message)

        w = Watchdog(["api", "db"], 30, Sink())
        w.check(lambda s: s == "db")
        self.assertEqual(sent, ["api is down"])


if __name__ == "__main__":
    unittest.main()
