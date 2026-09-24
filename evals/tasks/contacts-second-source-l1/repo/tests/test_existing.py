import unittest
from contacts.importer import import_crm
from contacts.store import Store


class CrmTest(unittest.TestCase):
    def test_imports(self):
        s = Store()
        import_crm(s, [{"crm_id": 1, "name": "Ana", "email": "a@x.test"}])
        self.assertEqual(len(s.rows), 1)
