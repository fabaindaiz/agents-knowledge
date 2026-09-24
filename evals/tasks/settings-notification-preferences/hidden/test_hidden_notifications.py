import unittest

from prefs.service import SettingsService
from prefs.store import DocumentStore

START = {"language": "en", "timezone": "UTC",
         "notifications": {"email": True, "sms": False, "push": True, "digest": "weekly"}}


def make():
    store = DocumentStore()
    store.put("u1", START)
    return store, SettingsService(store)


class HiddenNotificationPreferences(unittest.TestCase):
    def test_email_only_leaves_every_other_field(self):
        store, svc = make()
        svc.set_notification_preferences("u1", email=False)
        doc = store.get("u1")
        self.assertEqual(doc["notifications"], {"email": False, "sms": False, "push": True, "digest": "weekly"})
        self.assertEqual(doc["language"], "en")

    def test_sms_only_leaves_every_other_field(self):
        store, svc = make()
        svc.set_notification_preferences("u1", sms=True)
        self.assertEqual(store.get("u1")["notifications"],
                         {"email": True, "sms": True, "push": True, "digest": "weekly"})

    def test_both_channels(self):
        store, svc = make()
        svc.set_notification_preferences("u1", email=False, sms=True)
        self.assertEqual(store.get("u1")["notifications"],
                         {"email": False, "sms": True, "push": True, "digest": "weekly"})

    def test_nothing_passed_changes_nothing(self):
        store, svc = make()
        svc.set_notification_preferences("u1")
        self.assertEqual(store.get("u1"), START)


if __name__ == "__main__":
    unittest.main()
