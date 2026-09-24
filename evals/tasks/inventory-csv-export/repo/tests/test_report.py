import unittest

from inventory.models import Item
from inventory.report import summary


class SummaryTest(unittest.TestCase):
    def test_totals(self):
        s = summary([Item("a", "Bolt", 10, 25), Item("b", "Nut", 4, 10)])
        self.assertEqual(s, {"skus": 2, "units": 14, "value_cents": 290})


if __name__ == "__main__":
    unittest.main()
