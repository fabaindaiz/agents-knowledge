#!/usr/bin/env python3
"""One-time migration to 0.0.22: the index tables become fields of the notes they describe.

Until 0.0.21 a note's phases, its check, its *about to do* rows and what it rests on were written only
in the index tables, by hand. From 0.0.22 they are fields of the full note in `sources/notes/`, and the
tables are generated from them. This script moves them, by parsing the old tables, so no field is
retyped; and it proves nothing was lost:

    python3 meta/migrations/v0_0_22_notes.py --from .agents --write     write sources/ from an old tree
    python3 meta/migrations/v0_0_22_notes.py --verify-against v0.0.21   the proof, repeatable at any time

The proof renders the current sources in the old tables' own row order, without the new column, and
compares them byte for byte with the tables of the tagged release. Deleted in 0.0.23; the tag keeps it.
"""

from __future__ import annotations

import argparse
import io
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "meta/tools"))
import release as R  # noqa: E402

B = R.B

PHASE_LABELS = {
    "Plan and design": "plan",
    "Design a dataset, a population or a model": "dataset",
    "Implement": "implement",
    "Write tests": "tests",
    "Review": "review",
    "Verify and report": "verify",
    "Debug or investigate": "debug",
}
CARDS_HEADER = "| Note | Claim | Verify by |"
ABOUT_HEADER = "| …do this | Read | Because the default answer is wrong when |"
FOUNDED_HEADER = "| Note | Claim rests on | Our evidence |"
PHASE_HEADER = "| Phase | The question to ask | Notes |"
LINK = re.compile(r"^\[([\w-]+)\]\((?:\.\./)?notes/(\w+)/([\w-]+)\.md\)$")
STRENGTH = re.compile(r"^(.*) — \*\*([^*]+)\*\*$")
TOPIC_HEADING = re.compile(r"^### `([\w-]+)`$")


def _slug(cell: str) -> str:
    m = LINK.match(cell)
    if not m or m.group(1) != m.group(3):
        raise ValueError(f"not a note link: {cell!r}")
    return m.group(1)


def _table_span(lines: list[str], start: int) -> int:
    end = start + 2
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    return end


def parse_area(text: str, area: str, fields: dict, order: R.Order) -> str:
    """Reads one old area index into `fields` and `order`; returns its template."""
    _, body = B.split_frontmatter(text)
    lines = body.split("\n")
    out, i, topic = [], 0, None
    while i < len(lines):
        line = lines[i]
        heading = TOPIC_HEADING.match(line)
        if heading:
            topic = heading.group(1)
        if line == CARDS_HEADER:
            end = _table_span(lines, i)
            order.cards[topic] = []
            for row in lines[i + 2 : end]:
                note, claim, check = R.split_row(row)
                slug = _slug(note)
                fields.setdefault(slug, {}).update({"topic": topic, "claim": claim, "check": check})
                order.cards[topic].append(slug)
            out.append(f"<!-- generated: cards {topic} -->")
            i = end
            continue
        if line == ABOUT_HEADER:
            end = _table_span(lines, i)
            order.about[area] = []
            for row in lines[i + 2 : end]:
                do, note, wrong_when = R.split_row(row)
                slug = _slug(note)
                about = fields.setdefault(slug, {}).setdefault("about", [])
                order.about[area].append((slug, len(about)))
                about.append({"do": do, "wrong_when": wrong_when})
            out.append("<!-- generated: about -->")
            i = end
            continue
        if line == FOUNDED_HEADER:
            end = _table_span(lines, i)
            order.founded[area] = []
            for row in lines[i + 2 : end]:
                slug, rests, evidence = R.split_row(row)
                m = STRENGTH.match(rests)
                if m and "**" not in m.group(1):
                    fields.setdefault(slug, {}).update({"rests_on": m.group(1), "strength": m.group(2)})
                else:
                    fields.setdefault(slug, {}).update({"rests_on": rests})
                fields[slug]["our_evidence"] = evidence
                order.founded[area].append(slug)
            out.append("<!-- generated: founded -->")
            i = end
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def parse_index(text: str, fields: dict, order: R.Order) -> str:
    """Reads the old INDEX phase table into `fields` and `order`; returns the INDEX template."""
    _, body = B.split_frontmatter(text)
    lines = body.split("\n")
    at = lines.index(PHASE_HEADER)
    end = _table_span(lines, at)
    for n in range(at + 2, end):
        label, question, notes = R.split_row(lines[n])
        key = PHASE_LABELS[label.strip("*")]
        slugs = [_slug(link.strip()) for link in notes.split(" · ")]
        order.phases[key] = slugs
        for slug in slugs:
            fields.setdefault(slug, {}).setdefault("phases", []).append(key)
        lines[n] = R._row([label, question, "{{notes:" + key + "}}"])
    return "\n".join(lines)


OLD_NOTE_KEY = re.compile(r"^(\w+):[ \t]*(.*?)[ \t]*$")
KEPT_OLD_KEYS = ("slug", "topic", "claim", "confidence", "retired_because", "superseded_by")
FIELD_ORDER = ("slug", "topic", "claim", "confidence", "phases", "check", "about", "rests_on", "strength",
               "our_evidence", "boundary", "retired_because", "superseded_by")


def _old_note(text: str) -> tuple[dict, str]:
    """The old one-line-per-key note header, read line by line: its values were never quoted."""
    block, body = B.split_frontmatter(text)
    meta = {}
    for line in (block or "").split("\n"):
        m = OLD_NOTE_KEY.match(line)
        if m and m.group(1) in KEPT_OLD_KEYS:
            meta[m.group(1)] = m.group(2).strip('"') if m.group(1) in ("retired_because", "superseded_by") else m.group(2)
    return meta, body


def migrate(old: Path) -> tuple[dict[str, str], R.Order, list[str]]:
    """{sources-relative path: content} for every note and template, the old row order, and problems."""
    fields: dict[str, dict] = {}
    order = R.Order()
    files: dict[str, str] = {}
    problems: list[str] = []
    for area in sorted((old / "knowledge/areas").glob("*.md")):
        files[f"templates/areas/{area.name}"] = parse_area(area.read_text(encoding="utf-8"), area.stem, fields, order)
    files["templates/INDEX.md"] = parse_index((old / "knowledge/INDEX.md").read_text(encoding="utf-8"), fields, order)
    seen = set()
    for state in R.NOTE_STATES:
        for path in sorted((old / "knowledge/notes" / state).glob("*.md")):
            meta, body = _old_note(path.read_text(encoding="utf-8"))
            slug = path.stem
            seen.add(slug)
            table = fields.get(slug, {})
            if state in R.SHIPPED_STATES:
                if table.get("claim") != meta.get("claim"):
                    problems.append(f"{slug}: the claim in the note and in its card differ")
                if table.get("topic") != meta.get("topic"):
                    problems.append(f"{slug}: the topic in the note and the table it sits in differ")
            merged = {**meta, **{k: v for k, v in table.items() if k not in ("claim", "topic")}}
            new = {k: merged[k] for k in FIELD_ORDER if k in merged}
            files[f"notes/{state}/{slug}.md"] = B.dump_frontmatter(new) + body
    problems += [f"{slug}: in an index table but no such note" for slug in sorted(set(fields) - seen)]
    return files, order, problems


def verify(old: Path, root: Path) -> list[str]:
    """The proof: the sources, rendered in the old order without the new column, are the old tables."""
    notes = R.load_notes(root / "sources", strict_cards=False)
    templates = root / "sources/templates"
    topics_by_area = {p.stem: R.area_topics(p.read_text(encoding="utf-8")) for p in sorted((templates / "areas").glob("*.md"))}
    topics = [t for ts in topics_by_area.values() for t in ts]
    _, order, problems = migrate(old)
    pairs = [(f"knowledge/areas/{a}.md", R.render_area((templates / f"areas/{a}.md").read_text(encoding="utf-8"), a, notes,
                                                         ts, order, cards=False)) for a, ts in topics_by_area.items()]
    pairs.append(("knowledge/INDEX.md", R.render_index((templates / "INDEX.md").read_text(encoding="utf-8"), notes, topics, order)))
    for rel, rendered in pairs:
        _, expected = B.split_frontmatter((old / rel).read_text(encoding="utf-8"))
        if rendered != expected:
            a, b = rendered.split("\n"), expected.split("\n")
            line = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            problems.append(f"{rel}: differs from the old table from line {line + 1}: "
                            f"{(a[line] if line < len(a) else '<end>')[:90]!r} vs {(b[line] if line < len(b) else '<end>')[:90]!r}")
    return problems


def _extract(tag: str, into: Path) -> Path:
    data = subprocess.run(["git", "-C", str(ROOT), "archive", tag, ".agents"], check=True, capture_output=True).stdout
    with tarfile.open(fileobj=io.BytesIO(data)) as archive:
        archive.extractall(into, filter="data")
    return into / ".agents"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--from", dest="old", help="an old-layout .agents folder to migrate")
    parser.add_argument("--write", action="store_true", help="write sources/ (refused if it holds notes already)")
    parser.add_argument("--verify-against", metavar="TAG", help="prove the current sources reproduce TAG's tables")
    args = parser.parse_args(argv)
    if args.verify_against:
        with tempfile.TemporaryDirectory() as scratch:
            problems = verify(_extract(args.verify_against, Path(scratch)), ROOT)
        for p in problems:
            print("  x " + p)
        print(f"migration proof against {args.verify_against}: " + ("identical" if not problems else f"{len(problems)} differences"))
        return 1 if problems else 0
    files, _, problems = migrate(Path(args.old))
    for p in problems:
        print("  x " + p)
    if problems:
        return 1
    if args.write:
        target = ROOT / "sources"
        if any((target / "notes").rglob("*.md")):
            print(f"  x {target}/notes holds notes already; the migration runs once")
            return 1
        for rel, text in files.items():
            (target / rel).parent.mkdir(parents=True, exist_ok=True)
            (target / rel).write_text(text, encoding="utf-8")
    print(f"{len(files)} files {'written' if args.write else 'would be written'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
