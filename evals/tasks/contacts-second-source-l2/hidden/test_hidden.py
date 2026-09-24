import unittest
from contacts.importer import import_crm, import_shop
from contacts.store import Store

CRM = [{"crm_id": 1, "name": "Ana", "email": "a@x.test"}, {"crm_id": 2, "name": "Bo", "email": "b@x.test"}]
SHOP = [{"customer_no": 1, "full_name": "Cy", "mail": "c@x.test"}, {"customer_no": 3, "full_name": "Di", "mail": "d@x.test"}]


class HiddenSources(unittest.TestCase):
    def emails(self, s):
        return sorted(r["email"] for r in s.rows.values())

    def test_overlapping_numbers_keep_both_contacts(self):
        s = Store()
        import_crm(s, CRM)
        import_shop(s, SHOP)
        self.assertEqual(self.emails(s), ["a@x.test", "b@x.test", "c@x.test", "d@x.test"])

    def test_reimport_does_not_duplicate(self):
        s = Store()
        import_crm(s, CRM)
        import_shop(s, SHOP)
        import_shop(s, SHOP)
        import_crm(s, CRM)
        self.assertEqual(len(s.rows), 4)
