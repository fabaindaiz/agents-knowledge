import unittest
from catalog.api import list_items


class ListTest(unittest.TestCase):
    def test_first_page(self):
        page = list_items(0, 10)
        self.assertEqual([r["id"] for r in page["items"]], list(range(1, 11)))
        self.assertEqual(page["next_offset"], 10)
