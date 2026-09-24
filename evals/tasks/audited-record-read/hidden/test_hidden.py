import unittest
from records.audit import AuditLog
from records.service import Records


class HiddenAudit(unittest.TestCase):
    def test_read_is_recorded(self):
        log = AuditLog()
        Records({"p1": {"name": "A"}}, log).read("dr", "p1")
        self.assertEqual(log.records, [("dr", "read", "p1")])

    def test_no_record_no_read(self):
        r = Records({"p1": {"name": "A"}}, AuditLog(down=True))
        with self.assertRaises(Exception):
            r.read("dr", "p1")
