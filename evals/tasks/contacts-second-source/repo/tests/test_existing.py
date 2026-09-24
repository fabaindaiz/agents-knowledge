import unittest
from contacts.importer import Store, import_crm


class CrmTest(unittest.TestCase):
    def test_imports(self):
        s = Store()
        import_crm(s, [{"crm_id": 1, "name": "Ana", "email": "a@x.test"}])
        self.assertEqual(len(s.rows), 1)
