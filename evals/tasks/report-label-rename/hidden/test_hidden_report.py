import unittest

from stock.report import render


class HiddenReport(unittest.TestCase):
    def test_the_label_reads_quantity_everywhere(self):
        text = render([("bolt", 3), ("nut", 5)])
        self.assertNotIn("Qty", text)
        self.assertTrue(text.splitlines()[0].rstrip().endswith("Quantity"))
        self.assertEqual(text.splitlines()[-1], "Total Quantity: 8")
