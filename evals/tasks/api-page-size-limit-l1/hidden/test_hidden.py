import unittest
from catalog.api import list_items


class HiddenLimit(unittest.TestCase):
    def test_large_request_is_treated_as_100_everywhere(self):
        page = list_items(0, 1000)
        self.assertEqual(len(page["items"]), 100)
        self.assertEqual(page["page_size"], 100)
        self.assertEqual(page["next_offset"], 100)

    def test_paging_through_with_a_large_size_sees_every_item(self):
        seen, offset = [], 0
        while offset is not None:
            page = list_items(offset, 500)
            seen += [r["id"] for r in page["items"]]
            offset = page["next_offset"]
        self.assertEqual(seen, list(range(1, 1001)))

    def test_small_request_unchanged(self):
        page = list_items(20, 5)
        self.assertEqual(page["page_size"], 5)
        self.assertEqual(page["next_offset"], 25)
