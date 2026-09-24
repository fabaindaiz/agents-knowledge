import unittest
from records.audit import AuditLog
from records.service import Records


class ReadTest(unittest.TestCase):
    def test_reads(self):
        self.assertEqual(Records({"p1": {"name": "A"}}, AuditLog()).read("dr", "p1"), {"name": "A"})
