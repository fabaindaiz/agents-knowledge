import unittest
from recs.context import AppContext
from recs.home import home_page
from recs.model import Recommender


class HomeTest(unittest.TestCase):
    def test_home_page_lists_items(self):
        self.assertEqual(len(home_page(AppContext(Recommender()), "u1")["recommended"]), 3)
