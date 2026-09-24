import unittest
from infra.text import slug


class SlugTest(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(slug("Hello, World"), "hello-world")
