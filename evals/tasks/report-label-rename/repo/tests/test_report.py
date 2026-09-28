import unittest

from stock.report import render


class Report(unittest.TestCase):
    def test_one_line_per_row(self):
        self.assertEqual(len(render([("bolt", 3), ("nut", 5)]).splitlines()), 4)
