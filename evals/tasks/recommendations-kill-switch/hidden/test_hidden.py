import unittest
from recs.feature import Recommendations
from recs.model import Recommender


class HiddenKillSwitch(unittest.TestCase):
    def setUp(self):
        self.model = Recommender()
        self.r = Recommendations(self.model, {"recommendations_disabled": True})

    def test_no_entry_point_calls_the_model(self):
        page = self.r.home_page("u1")
        self.assertIn("greeting", page)
        self.r.warm_cache(["u1", "u2"])
        self.r.email_digest("u1")
        self.assertEqual(self.model.calls, 0)

    def test_a_warm_cache_is_not_served_when_disabled(self):
        model = Recommender()
        flags = {}
        r = Recommendations(model, flags)
        r.warm_cache(["u1"])
        flags["recommendations_disabled"] = True
        self.assertFalse(r.home_page("u1").get("recommended"))

    def test_enabled_still_works(self):
        r = Recommendations(self.model, {})
        self.assertEqual(len(r.home_page("u1")["recommended"]), 3)
