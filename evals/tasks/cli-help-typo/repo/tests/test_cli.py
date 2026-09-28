import unittest

from notes_cli.cli import build_parser


class Cli(unittest.TestCase):
    def test_parses_a_note_and_options(self):
        args = build_parser().parse_args(["hello", "--inbox", "in", "--notify"])
        self.assertEqual((args.text, args.inbox, args.notify), ("hello", "in", True))
