import unittest

from notes_cli.cli import build_parser


class HiddenHelp(unittest.TestCase):
    def test_no_misspelling_left_in_the_help(self):
        help_text = build_parser().format_help()
        self.assertNotIn("recieve", help_text)
        self.assertEqual(help_text.count("receive"), 2)
