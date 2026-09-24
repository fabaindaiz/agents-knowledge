import unittest
from recs.feature import Recommendations


class HomeTest(unittest.TestCase):
    def test_home_page_lists_items(self):
        r = Recommendations()
        self.assertEqual(len(r.home_page("u1")["recommended"]), 3)
