import unittest

from prefs.service import SettingsService
from prefs.store import DocumentStore


def make():
    store = DocumentStore()
    store.put("u1", {"language": "en", "timezone": "UTC",
                     "notifications": {"email": True, "sms": False, "push": True, "digest": "weekly"}})
    return store, SettingsService(store)


class LanguageTest(unittest.TestCase):
    def test_sets_language(self):
        store, svc = make()
        svc.set_language("u1", "es")
        self.assertEqual(svc.get("u1")["language"], "es")

    def test_rejects_bad_language(self):
        _, svc = make()
        with self.assertRaises(ValueError):
            svc.set_language("u1", "spanish")


if __name__ == "__main__":
    unittest.main()
