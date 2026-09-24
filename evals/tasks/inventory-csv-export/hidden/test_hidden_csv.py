import csv
import os
import tempfile
import unittest

from inventory.models import Item
from inventory.report import export_csv


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


class HiddenCsv(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.path = os.path.join(self.dir, "out.csv")

    def test_header_rows_and_prices(self):
        export_csv([Item("a1", "Bolt", 10, 1250), Item("b2", "Nut", 3, 5)], self.path)
        self.assertEqual(read(self.path), [["sku", "name", "quantity", "price"],
                                           ["a1", "Bolt", "10", "12.50"], ["b2", "Nut", "3", "0.05"]])

    def test_names_with_commas_and_quotes_round_trip(self):
        export_csv([Item("c3", 'Hinge, 3" steel', 1, 199)], self.path)
        self.assertEqual(read(self.path)[1], ["c3", 'Hinge, 3" steel', "1", "1.99"])

    def test_no_items_writes_the_header_only(self):
        export_csv([], self.path)
        self.assertEqual(read(self.path), [["sku", "name", "quantity", "price"]])


if __name__ == "__main__":
    unittest.main()
