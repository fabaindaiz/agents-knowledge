import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="notes", description="Keep short notes.")
    parser.add_argument("text", nargs="?", help="the note to add")
    parser.add_argument("--inbox", help="the folder that will receive new notes")
    parser.add_argument("--notify", action="store_true", help="receive a message when a note is added")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.text:
        print(f"added: {args.text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
