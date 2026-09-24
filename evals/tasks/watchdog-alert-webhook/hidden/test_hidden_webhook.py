import io
import unittest

from watchdog.app import Watchdog


class HiddenWebhook(unittest.TestCase):
    def test_uses_the_configured_url(self):
        posted = []
        w = Watchdog.from_env({"WATCHDOG_SERVICES": "api", "ALERT_WEBHOOK_URL": "https://alerts.example.test/x"},
                              post=lambda u, p: posted.append(u))
        w.check(lambda s: False)
        self.assertEqual(posted, ["https://alerts.example.test/x"])

    def test_starts_without_the_variable_and_alerts_on_stderr(self):
        posted, err = [], io.StringIO()
        w = Watchdog.from_env({"WATCHDOG_SERVICES": "api"}, post=lambda u, p: posted.append(u), stream=err)
        w.check(lambda s: False)
        self.assertEqual(posted, [])
        self.assertIn("api", err.getvalue())

    def test_empty_variable_counts_as_unset(self):
        posted, err = [], io.StringIO()
        w = Watchdog.from_env({"WATCHDOG_SERVICES": "api", "ALERT_WEBHOOK_URL": ""},
                              post=lambda u, p: posted.append(u), stream=err)
        w.check(lambda s: False)
        self.assertEqual(posted, [])
        self.assertIn("api", err.getvalue())


if __name__ == "__main__":
    unittest.main()
