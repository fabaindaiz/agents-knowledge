import unittest
from jobs.nightly import warm_cache
from mail.digest import email_digest
from recs.context import AppContext
from recs.home import home_page
from recs.model import Recommender
from web.widgets import render


class HiddenKillSwitch(unittest.TestCase):
    def test_no_entry_point_calls_the_model(self):
        model = Recommender()
        ctx = AppContext(model, {"recommendations_disabled": True})
        self.assertIn("greeting", home_page(ctx, "u1"))
        warm_cache(ctx, ["u1", "u2"])
        email_digest(ctx, "u1")
        render(ctx, "recommended", "u1")
        self.assertEqual(model.calls, 0)

    def test_a_warm_cache_is_not_served_when_disabled(self):
        ctx = AppContext(Recommender(), {})
        warm_cache(ctx, ["u1"])
        ctx.flags["recommendations_disabled"] = True
        self.assertFalse(home_page(ctx, "u1").get("recommended"))

    def test_enabled_still_works(self):
        ctx = AppContext(Recommender(), {})
        self.assertEqual(len(home_page(ctx, "u1")["recommended"]), 3)
