#!/usr/bin/env python3
"""The home repository's half of the agent-guides tools. Python 3.11+, standard library only.

The carrier tool (`.agents/tools/bundle.py`) is what every repository that carries the bundle runs.
This one is what only the home runs: it builds the shipped knowledge from the full notes in
`sources/`, cuts a release, and carries it to the other carriers. It loads the carrier tool rather
than copying from it, so every rule both need exists once.

    python3 meta/tools/release.py build [--check]         generated knowledge and SHA256SUMS, from sources/
    python3 meta/tools/release.py release X.Y.Z           version, date, build; prints the tag to create
    python3 meta/tools/release.py check                   the home's CI: verify, build --check, privacy, links, its decisions log
    python3 meta/tools/release.py gather [REPO...] --out DIR [--packs FILE...]   phase 1: each carrier and its proposals
    python3 meta/tools/release.py intake DIR              the gathered proposals into meta/tracking/, as received
    python3 meta/tools/release.py lost BASE SNAPSHOT...   lines a carrier added that the home does not hold
    python3 meta/tools/release.py splice [REPO...] [--write --backup DIR]   phase 2: the release into each carrier
    python3 meta/tools/release.py register [REPO...]      the carriers table, by stored carrier id
    python3 meta/tools/release.py align [REPO...]         phase 3: every carrier on one version
    python3 meta/tools/release.py note-state SLUG STATE   move a full note between states, then build
    python3 meta/tools/release.py report [--check]        sizes, budgets and the knowledge funnel

The tests are in `meta/tests/` (`python3 -m unittest discover -s meta/tests -t .`).
"""

from __future__ import annotations

import sys

# Before any other import, in syntax that 3.9 still parses: an older interpreter gets one line, not a traceback.
if sys.version_info < (3, 11):
    sys.exit(f"release.py needs Python 3.11 or newer; this is {sys.version.split()[0]} at {sys.executable}. "
             "Run it with a newer one: python3.11 meta/tools/release.py ... (or uv run --python 3.11 ...)")

import argparse
import datetime
import importlib.util
import io
import re
import subprocess
import tarfile
import tokenize
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load_bundle():  # noqa: ANN202 -- a module
    if "bundle" in sys.modules:
        return sys.modules["bundle"]
    # The original, not its release copy: the build writes the copy, and must not depend on it.
    spec = importlib.util.spec_from_file_location("bundle", ROOT / "sources/bundle/tools/bundle.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["bundle"] = module
    spec.loader.exec_module(module)
    return module


B = _load_bundle()
RefusedError = B.RefusedError

PACK_LIMIT = 2**18  # bytes per proposal: far above a paragraph and its evidence, far below anything else


def carrier_ids(repos: list[Path]) -> dict[Path, str]:
    """Every repository's stored id, or a refusal when two of them store the same one.

    A bundle copied whole into a new repository brings the old one's carrier file, id included, and the
    two would then be one row of the carriers table and one prefix of records.
    """
    ids = {repo: B.repo_carrier_id(repo) for repo in repos}
    seen: dict[str, Path] = {}
    for repo, value in ids.items():
        if value in seen:
            raise RefusedError(
                f"{seen[value]} and {repo} both store {value}: a bundle copied from one repository carries its id; "
                f"delete `{B.CARRIER_FIELD}` from the copy's {B.CARRIER_FILE} and run `bundle.py carrier-id --mint` there")
        seen[value] = repo
    return ids


def read_pack(path: Path) -> dict[str, str]:
    """{file name: text} of the proposals in a pack; anything else in it is refused, never extracted."""
    out = {}
    with tarfile.open(path) as archive:
        for member in archive.getmembers():
            name = member.name.removeprefix(f"{B.PROPOSALS}/")
            if not (member.isfile() and "/" not in name and name.endswith(".md") and B.PROPOSAL_NAME.match(name[:-3])):
                raise RefusedError(f"{path}: {member.name!r} is not a proposal file; a pack holds proposals only")
            if name in out:
                raise RefusedError(f"{path}: {name} is in it twice; a pack holds each proposal once")
            if member.size > PACK_LIMIT:
                raise RefusedError(f"{path}: {member.name} is larger than a proposal can be")
            data = archive.extractfile(member).read()  # type: ignore[union-attr]
            try:
                out[name] = data.decode("utf-8")
            except UnicodeDecodeError as error:
                raise RefusedError(f"{path}: {member.name} is not UTF-8") from error
    return out


def checksums_text(tree: Path) -> str:
    """The `SHA256SUMS` content for a tree: GNU coreutils text format, `<hex>  <path>`, byte order."""
    lines = []
    for rel in B.shipped(tree):
        if "\\" in rel or len(rel.splitlines()) != 1 or rel != rel.strip("\n"):
            raise RefusedError(f"{rel!r}: a path GNU sha256sum would escape or split; rename it")
        lines.append(f"{B.sha256_file(tree / rel)}  {rel}\n")
    return "".join(lines)


def write_checksums(tree: Path) -> None:
    (tree / B.CHECKSUMS).write_text(checksums_text(tree), encoding="utf-8")


# --- the build: sources/ -> .agents/knowledge/ -------------------------------------------------------
# A note is written once, in full, in `sources/notes/<state>/<slug>.md`. Everything a carrier reads about
# it is derived from that file by code: the short note it ships, its row in every index table, and its
# card (claim, where it stops applying, the check). Nothing derived is written by hand, so nothing
# derived can disagree with its source; `build --check` fails when the output is not what the sources
# produce.

NOTE_STATES = ("active", "review", "retired")
SHIPPED_STATES = ("active", "review")
# The sections of a full note that stay home: where a note came from, what it rests on, what was
# measured. A carrier reads the mechanism, the boundary and the cost; the evidence is for the release.
EVIDENCE_SECTIONS = ("Where it came from", "Literature", "Evidence")
BOUNDARY_SECTION = "When it does NOT apply"
# The phases of work, in the order `INDEX.md` lists them. A note's `phases` field names them by key.
PHASES = ("plan", "dataset", "implement", "tests", "review", "verify", "debug")
CONFIDENCE = ("measured", "reasoned", "inherited")
REQUIRED = ("slug", "topic", "claim", "confidence", "check")
SHIPPED_FIELDS = ("slug", "topic", "claim", "confidence", "check", "boundary")
# Every file of the release says it is one, and no original does (`form_problems`): the two forms of the
# content must be unmistakable in every file, whatever other forms exist beside them.
RELEASE_MARK = "Generated by the release build"
BANNER = f"<!-- {RELEASE_MARK} from the full notes. Edit the original in the home repository, never this file. -->\n"
NOTE_BANNER = f"{RELEASE_MARK} from the full note; edit the original in the home repository, never this file"
COPY_BANNER = f"{RELEASE_MARK} from its original in the home repository's sources/bundle/; edit that, never this file."
ORIGINALS = "sources/bundle"
# The one shipped file that cannot carry a banner: the GNU checksum format has no comments.
UNMARKED = ("SHA256SUMS",)


def strip_comments(text: str) -> str:
    """Python source without its comments, found as COMMENT tokens so a `#` inside a string stays; a shebang
    stays, a line that held only a comment goes, and a line with code keeps its code."""
    lines = text.split("\n")
    found = [t.start for t in tokenize.generate_tokens(io.StringIO(text).readline) if t.type == tokenize.COMMENT]
    drop: set[int] = set()
    for row, col in found:
        if row == 1 and lines[0].startswith("#!"):
            continue
        kept = lines[row - 1][:col].rstrip()
        if kept:
            lines[row - 1] = kept
        else:
            drop.add(row - 1)
    return "\n".join(line for i, line in enumerate(lines) if i not in drop)


def with_banner(rel: str, text: str) -> str:
    """An original as it ships: the same bytes, with the release banner where the file's format allows it."""
    if rel.endswith(".py"):
        first, _, rest = text.partition("\n")
        return (first + "\n# " + COPY_BANNER + "\n" + rest) if first.startswith("#!") else "# " + COPY_BANNER + "\n" + text
    if rel.endswith(".md"):
        if text.startswith("---\n"):
            return "---\n# " + COPY_BANNER + "\n" + text[4:]
        return "<!-- " + COPY_BANNER + " -->\n" + text
    raise BuildError(f"{ORIGINALS}/{rel}: no banner form for this kind of file")


def without_banner(rel: str, text: str) -> str:
    """The inverse of `with_banner`: what the proof compares with the original."""
    for mark in ("# " + COPY_BANNER + "\n", "<!-- " + COPY_BANNER + " -->\n"):
        text = text.replace(mark, "", 1)
    return text


def _marked(text: str) -> bool:
    return RELEASE_MARK.lower() in "\n".join(text.split("\n")[:4]).lower()


def form_problems(root: Path) -> list[str]:
    """Every release file without the release banner, and every original that carries one."""
    bundle = root / ".agents"
    problems = [f".agents/{rel}: a release file without the release banner; it would read as an original"
                for rel in B.shipped(bundle) if rel not in UNMARKED
                and not _marked((bundle / rel).read_text(encoding="utf-8", errors="replace"))]
    problems += [f"{p.relative_to(root).as_posix()}: an original that carries the release banner"
                 for folder in ("sources", "meta") for p in sorted((root / folder).rglob("*"))
                 if p.is_file() and p.suffix in (".md", ".py") and "__pycache__" not in p.parts
                 and _marked(p.read_text(encoding="utf-8", errors="replace"))]
    return problems
GENERATED_MARKER = re.compile(r"^<!-- generated: (cards|about|founded|principles) ?([\w-]*) -->$", re.MULTILINE)
PHASE_TOKEN = re.compile(r"\{\{notes:([\w-]+)\}\}")
# Anything that looks like a marker or a token must be one the build knows: a misspelt one would ship
# literally, and its table would be silently missing.
ANY_MARKER = re.compile(r"(?i)<!--\s*generated\b[^>]*-->|\{\{[^}]*\}\}")
REVIEW_MARK = " ⚠ review"


@dataclass
class Note:
    slug: str
    state: str
    meta: dict
    body: str
    where: str
    boundary: str = ""

    @property
    def topic(self) -> str:
        return self.meta["topic"]


class BuildError(RuntimeError):
    """The sources do not describe a buildable knowledge base; every problem is listed."""


def _headings(body: str) -> list[tuple[int, int, str]]:
    """(line index, level, text) of every heading outside fenced blocks."""
    lines = body.split("\n")
    prose = B._prose(lines)
    out = []
    for i, line in enumerate(lines):
        m = B.HEADING.match(line) if prose[i] else None
        if m:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def short_body(body: str) -> str:
    """The body a carrier ships: everything before the first evidence section."""
    lines = body.split("\n")
    cut = next((i for i, level, text in _headings(body) if level == 2 and text in EVIDENCE_SECTIONS), len(lines))
    return "\n".join(lines[:cut]).rstrip("\n") + "\n"


def _section_lines(body: str, heading: str) -> list[str] | None:
    lines = body.split("\n")
    heads = _headings(body)
    for n, (i, level, text) in enumerate(heads):
        if level == 2 and text == heading:
            end = next((j for j, lv, _ in heads[n + 1 :] if lv <= 2), len(lines))
            return lines[i + 1 : end]
    return None


BOLD_LEAD = re.compile(r"^- \*\*(.+?)\*\*")


def lead_ins(body: str) -> list[str] | None:
    """The bold lead-ins of *When it does NOT apply*, or None when any top-level bullet has none.

    A section written as bullets that each open in bold states its cases in their own words; the card
    lists those words. A section in prose, or with one bullet that does not open in bold, has no such
    words, and its note carries a `boundary:` written for the card instead.
    """
    section = _section_lines(body, BOUNDARY_SECTION)
    if section is None:
        return None
    bullets = [line for line in section if line.startswith("- ")]
    if not bullets or any(not BOLD_LEAD.match(line) for line in bullets):
        return None
    return [BOLD_LEAD.match(line).group(1).strip().rstrip(".:;,").strip() for line in bullets]


def load_notes(sources: Path, strict_cards: bool = True) -> list[Note]:
    """Every full note under `sources/notes/<state>/`, parsed and checked; all problems at once.

    With `strict_cards` off, a note whose card has no boundary yet is loaded anyway (the migration proof
    renders the old tables, which had no card column).
    """
    notes, problems = [], []
    nouns = product_nouns(sources.parent)
    for state in NOTE_STATES:
        for path in sorted((sources / "notes" / state).glob("*.md"), key=lambda p: p.name.encode()):
            where = path.relative_to(sources.parent).as_posix()
            try:
                meta, body = B.read_frontmatter(path.read_text(encoding="utf-8"), where)
            except B.FrontmatterError as error:
                problems.append(str(error))
                continue
            note = Note(path.stem, state, meta, body, where)
            problems += [p for p in _note_problems(note, nouns) if strict_cards or "boundary" not in p]
            notes.append(note)
    slugs = [n.slug for n in notes]
    problems += [f"note {s!r} is in more than one state folder" for s in sorted({s for s in slugs if slugs.count(s) > 1})]
    # A principle names what several notes carry between them; one note alone is just the note.
    groups = principles(notes)
    problems += [f"principle {p!r} is carried by one note only ({ns[0].slug}); drop the field or name the others"
                 for p, ns in groups.items() if len(ns) < 2]
    if problems:
        raise BuildError("\n".join(problems))
    return notes


def principles(notes: list[Note]) -> dict[str, list[Note]]:
    """{principle: the shipped notes that carry it}, from the optional `principle` field."""
    out: dict[str, list[Note]] = {}
    for n in notes:
        if n.state in SHIPPED_STATES and isinstance(n.meta.get("principle"), str) and n.meta["principle"]:
            out.setdefault(n.meta["principle"], []).append(n)
    return out


def product_nouns(root: Path) -> list[str]:
    """The lower-cased product names in `meta/product-nouns.txt`; none when the file is absent."""
    path = root / "meta" / "product-nouns.txt"
    if not path.is_file():
        return []
    lines = (line.strip().lower() for line in path.read_text(encoding="utf-8").splitlines())
    return [line for line in lines if line and not line.startswith("#")]


def _product_cues(cues: list, nouns: list[str]) -> list[tuple[str, str]]:
    """[(cue, noun)] for every cue that holds a listed product name as a word (or a phrase)."""
    found = []
    for cue in cues:
        folded = str(cue).casefold()
        words = set(re.findall(r"[a-z0-9_]+", folded))
        for noun in nouns:
            if noun in words or (" " in noun and noun in folded):
                found.append((str(cue), noun))
    return found


def _note_problems(note: Note, nouns: list[str] | None = None) -> list[str]:
    meta, problems = note.meta, []
    nouns = product_nouns(ROOT) if nouns is None else nouns
    cues = meta.get("cues")
    problems += [f"{note.where}: cue {cue!r} names a product ({noun}); say the mechanism"
                 for cue, noun in _product_cues(cues if isinstance(cues, list) else [], nouns)]
    missing = [k for k in REQUIRED if not str(meta.get(k) or "").strip()]
    if note.state == "retired":
        missing = [k for k in ("slug", "claim") if not meta.get(k)]
    problems += [f"{note.where}: missing `{k}`" for k in missing]
    if meta.get("slug") and meta["slug"] != note.slug:
        problems.append(f"{note.where}: `slug: {meta['slug']}` is not the file name")
    if meta.get("principle") is not None and not (isinstance(meta["principle"], str)
                                                  and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta["principle"])):
        problems.append(f"{note.where}: `principle` is a kebab-case name")
    if meta.get("confidence") and meta["confidence"] not in CONFIDENCE:
        problems.append(f"{note.where}: `confidence` is one of {', '.join(CONFIDENCE)}")
    unknown = [p for p in meta.get("phases") or [] if p not in PHASES]
    problems += [f"{note.where}: unknown phase {p!r} (one of {', '.join(PHASES)})" for p in unknown]
    for row in meta.get("about") or []:
        if not isinstance(row, dict) or set(row) != {"do", "wrong_when"}:
            problems.append(f"{note.where}: every `about` row is {{do, wrong_when}}")
    stray = [text for _, level, text in _headings(note.body) if level != 2 and text.strip() in EVIDENCE_SECTIONS]
    problems += [f"{note.where}: *{text}* is not a level-2 heading, so the build would ship it" for text in stray]
    if note.state in SHIPPED_STATES:
        if not meta.get("phases"):
            problems.append(f"{note.where}: in no phase, so the index never routes to it")
        if not meta.get("about"):
            problems.append(f"{note.where}: in no *about to do* row")
        leads = lead_ins(note.body)
        if leads and meta.get("boundary"):
            problems.append(f"{note.where}: has both bold lead-ins under *{BOUNDARY_SECTION}* and a `boundary:`; keep one")
        elif leads:
            note.boundary = " · ".join(leads)
        elif meta.get("boundary"):
            note.boundary = meta["boundary"]
        else:
            problems.append(f"{note.where}: *{BOUNDARY_SECTION}* has no bold lead-in on every bullet, so the card "
                            "needs a `boundary:`")
    return problems


def _cell(text: str) -> str:
    return " ".join(str(text).split("\n")).replace("|", "\\|")


def _row(cells: list[str]) -> str:
    return "| " + " | ".join(_cell(c) for c in cells) + " |"


def _link(note: Note, prefix: str) -> str:
    return f"[{note.slug}]({prefix}notes/{note.state}/{note.slug}.md)" + (REVIEW_MARK if note.state == "review" else "")


@dataclass
class Order:
    """A row order other than the canonical one: used once, to reproduce the hand-ordered tables."""

    cards: dict[str, list[str]] = field(default_factory=dict)
    about: dict[str, list[tuple[str, int]]] = field(default_factory=dict)
    founded: dict[str, list[str]] = field(default_factory=dict)
    phases: dict[str, list[str]] = field(default_factory=dict)


def _ordered(items: list, key, override: list | None):  # noqa: ANN001, ANN202
    if override is None:
        return sorted(items, key=key)
    position = {k: i for i, k in enumerate(override)}
    unknown = [it for it in items if key(it) not in position]
    if unknown:
        raise BuildError(f"the given order lacks {sorted(map(str, map(key, unknown)))}")
    return sorted(items, key=lambda it: position[key(it)])


def render_card(note: Note, siblings: list[Note] | None = None) -> str:
    """`knowledge/cards/<slug>.md`: what a session applies, in one small file, one lookup from the index.

    Pilot-6 measured the cost of reaching a summary through an area index of tens of thousands of
    characters; a card is a few hundred, and the full note stays one link away.
    """
    return BANNER + "\n".join([
        f"# {note.slug}" + (REVIEW_MARK if note.state == "review" else ""),
        "",
        f"**Claim.** {note.meta['claim']}",
        "",
        *([f"**Applies if.** {note.meta['applies_if']}", ""] if note.meta.get("applies_if") else []),
        f"**Not when.** {note.boundary}",
        "",
        f"**Check.** {note.meta['check']}",
        "",
        *([f"**Shares its principle** (`{note.meta['principle']}`) with "
           + ", ".join(f"[{s.slug}]({s.slug}.md)" for s in siblings)
           + ": removing or ignoring this note does not remove the principle.", ""] if siblings else []),
        f"*{note.meta['confidence']}.* Open the full note only when you cannot tell whether its boundary holds here: "
        f"[{note.slug}](../notes/{note.state}/{note.slug}.md).",
    ]) + "\n"


def _card_link(note: Note) -> str:
    return f"[{note.slug}](cards/{note.slug}.md)" + (REVIEW_MARK if note.state == "review" else "")


def _card_name(note: Note) -> str:
    """A note in a phase cell: its slug, which names its card (`cards/<slug>.md`). The card's one link from
    the index is its *about to do* row, which every shipped note has; repeating it in every phase the note
    is in cost the reviewer, who loads the index whole, about a tenth of its budget."""
    return f"`{note.slug}`" + (REVIEW_MARK if note.state == "review" else "")


def render_index(template: str, notes: list[Note], topics: list[str], order: Order | None = None,
                 link=None, name=None) -> str:  # noqa: ANN001 -- (Note) -> str
    """`INDEX.md` from its template: every `{{notes:PHASE}}` replaced by that phase's notes, each written
    by `name`, and an `<!-- generated: about -->` marker by the *about to do* rows of every area, each
    linking a card by `link`."""
    order = order or Order()
    rank = {t: i for i, t in enumerate(topics)}
    shipped = [n for n in notes if n.state in SHIPPED_STATES]
    link = link or (lambda n: _link(n, ""))
    name = name or link
    items = sorted(((n, i, r) for n in shipped for i, r in enumerate(n.meta.get("about") or [])),
                   key=lambda it: (rank.get(it[0].topic, len(rank)), it[0].slug, it[1]))
    about = "\n".join([_row(["…do this", "Card", "Because the default answer is wrong when"]), "|---|---|---|",
                       *[_row([r["do"], link(n), r["wrong_when"]]) for n, _, r in items]])
    template = re.sub(r"^<!-- generated: about -->$", lambda _: about, template, flags=re.MULTILINE)

    def cell(m: re.Match) -> str:
        phase = m.group(1)
        if phase not in PHASES:
            raise BuildError(f"INDEX template: unknown phase {phase!r}")
        members = [n for n in shipped if phase in n.meta.get("phases", [])]
        members = _ordered(members, lambda n: n.slug, order.phases.get(phase)) if order.phases.get(phase) \
            else sorted(members, key=lambda n: (rank.get(n.topic, len(rank)), n.slug))
        return " · ".join(name(n) for n in members)

    return PHASE_TOKEN.sub(cell, template)


def short_note(note: Note) -> str:
    """The note a carrier ships: the card fields, and the body up to the evidence."""
    meta = {k: (note.boundary if k == "boundary" else note.meta.get(k)) for k in SHIPPED_FIELDS}
    if note.meta.get("cues"):  # what a change or its diff would contain, read by `bundle.py lookup` (0.0.30)
        meta["cues"] = note.meta["cues"]
    return B.dump_frontmatter(meta, NOTE_BANNER) + short_body(note.body)


def area_topics(template: str) -> list[str]:
    return [m.group(2) for m in GENERATED_MARKER.finditer(template) if m.group(1) == "cards"]


OPEN_CELL = 180  # characters: enough for a slug and a claim to be recognised, not the evidence behind them


def _clip(text: str, limit: int = OPEN_CELL) -> str:
    """A cell cut at a word boundary: OPEN.md is for recognising a row, the home holds the rest."""
    text = re.sub(r"\s*\(see \*[^*]+\*[^)]*\)", "", text).strip()
    return text if len(text) <= limit else text[: text.rfind(" ", 0, limit)].rstrip(",;:—- ") + " …"


RECEIVED_LEDGER = "meta/tracking/received.md"
RECORDS_BANNER = f"<!-- {RELEASE_MARK} from the home repository's {RECEIVED_LEDGER}; edit that, never this file. -->\n"


def received_rows(meta_dir: Path) -> list[list[str]]:
    return [r for r in read_table(meta_dir / "tracking/received.md", B.RECEIVED_HEADER) if len(r) >= 3]


def render_received(meta_dir: Path) -> str:
    """`proposals/RECEIVED.md`: every proposal the home took in, by id, with where it went.

    A carrier removes the ones it finds here (`bundle.py proposals --prune`); ids only, so the list says
    nothing of which carrier offered what.
    """
    rows = sorted(received_rows(meta_dir), key=lambda r: r[0])
    versions = sorted({r[1].strip() for r in rows if B.SEMVER.match(r[1].strip())}, key=B.semver_key)
    recent = set(versions[-2:])  # the last two releases keep their verdicts; older ids still prune
    rows = [r[:2] + [r[2] if r[1].strip() in recent else "—"] for r in rows]
    lines = [
        "# Received — the proposals the home repository took in",
        "",
        "Generated at each release from the home's records. Each row is a proposal some carrier wrote in its own "
        "`proposals/`, and what the home did with it. A carrier that finds one of its own here removes it "
        "with `python3 .agents/tools/bundle.py proposals --prune`; one not listed yet is still waiting, and "
        "stays. Verdicts older than the last two releases are kept in the home's ledger only. Nothing here is "
        "guidance.",
        "",
        B.RECEIVED_HEADER,
        "|---|---|---|",
        *[_row(r[:3]) for r in rows],
    ]
    return "\n".join(lines) + "\n"


def answered(meta_dir: Path) -> list[str]:
    """The slugs the home's history says left the queue, from the first cell of its tables."""
    path = meta_dir / "tracking/history.md"
    if not path.is_file():
        return []
    slugs = {m.group(1) for line in path.read_text(encoding="utf-8").split("\n")
             if (m := re.match(r"^\| `([\w-]+)` \|", line))}
    return sorted(slugs)


def render_open(meta_dir: Path) -> str:
    """`knowledge/OPEN.md`: what a harvest checks before it offers something, from the home's records.

    Cells are clipped: a harvest reads it to recognise what is already known, and the full rows, with
    their evidence, stay in the home.
    """
    experiments = read_table(meta_dir / "tracking/experiments.md", "| Note | Experiment | Cost | Would change |")
    candidates = read_table(meta_dir / "tracking/candidates.md", "| Candidate | Kind | Lacks |", prefix=True)
    lines = [
        "# Open — what the home is still waiting for",
        "",
        "Generated at each release from the home repository's records, each cell shortened. A harvest reads it "
        "before offering anything: an experiment queued here is one this repository may be able to run, and a "
        "candidate listed here is extended with a new occurrence (`extends <slug>`), not offered again.",
        "",
        "## Experiments waiting to be run",
        "",
        "| Note | Experiment | Cost |",
        "|---|---|---|",
        *[_row([r[0], _clip(r[1]), _clip(r[2], 60)]) for r in experiments],
        "",
        "## Candidates waiting for what they lack",
        "",
        "By slug and kind; the claim and what each lacks stay in the home's queue.",
        "",
        "| Candidate | Kind |",
        "|---|---|",
        *[_row([f"`{slug_of(r[0])}`", r[1]]) for r in candidates],
        "",
        "## Answered: admitted, folded, refused or discarded, not to offer again",
        "",
        ", ".join(f"`{s}`" for s in answered(meta_dir)) or "None yet.",
    ]
    return "\n".join(lines) + "\n"



def oldest_carrier_version(meta_dir: Path) -> str | None:
    """The oldest version any registered carrier was aligned to, from `meta/tracking/carriers.md`."""
    path = meta_dir / "tracking/carriers.md"
    if not path.is_file():
        return None
    versions = [r[1].strip() for r in read_table(path, "| Carrier | Version | Aligned on |") if len(r) > 1]
    versions = [v for v in versions if B.SEMVER.match(v)]
    return min(versions, key=B.semver_key) if versions else None


def trim_changelog(text: str, oldest: str | None) -> str:
    """The changelog a release ships: the sections from the oldest registered carrier's version on, since no
    carrier needs what changed before the version it holds; the full history stays in the home's original."""
    if not oldest:
        return text
    sections = list(re.finditer(r"^## \[(\d+\.\d+\.\d+)\]", text, re.MULTILINE))
    cut = next((m.start() for m in sections if B.semver_key(m.group(1)) < B.semver_key(oldest)), None)
    if cut is None:
        return text
    return (text[:cut].rstrip("\n") + "\n\n"
            f"Versions before {oldest}, which no registered carrier holds, are in the home repository's "
            "`sources/bundle/CHANGELOG.md`, at any release tag.\n")

# The table readers live in the carrier tool, which needs them to convert the outbox of 0.0.23.
split_row = B.split_row
read_table = B.read_table


def build_outputs(root: Path, order: Order | None = None, cards: bool = True, banner: bool = True) -> dict[str, str]:
    """Everything the build writes into `.agents/`, as {bundle-relative path: content}, SHA256SUMS aside."""
    sources = root / "sources"
    notes = load_notes(sources)
    templates = sources / "templates"
    areas = sorted((templates / "areas").glob("*.md"), key=lambda p: p.name.encode())
    topics_by_area = {p.stem: area_topics(p.read_text(encoding="utf-8")) for p in areas}
    topics = [t for ts in topics_by_area.values() for t in ts]
    problems = [f"{t}: a topic in more than one area template" for t in sorted({t for t in topics if topics.count(t) > 1})]
    problems += [f"{n.where}: topic {n.topic!r} has no `<!-- generated: cards {n.topic} -->` in any area template"
                 for n in notes if n.state in SHIPPED_STATES and n.topic not in topics]
    if problems:
        raise BuildError("\n".join(problems))
    for path in [*areas, templates / "INDEX.md"]:
        text = path.read_text(encoding="utf-8")
        # Known by position, not by text: an indented copy of a real marker is not one. Phase tokens only
        # have a meaning in INDEX, markers only in the area templates.
        if path.name == "INDEX.md" and path.parent == templates:
            known = {m.start() for m in PHASE_TOKEN.finditer(text) if m.group(1) in PHASES}
            known |= {m.start() for m in re.finditer(r"^<!-- generated: about -->$", text, re.MULTILINE)}
        else:
            known = {m.start() for m in GENERATED_MARKER.finditer(text)}
        problems += [f"{path.relative_to(root).as_posix()}: {m.group(0)!r} is not a marker the build knows"
                     for m in ANY_MARKER.finditer(text) if m.start() not in known]
    shipped_topics = {n.topic for n in notes if n.state in SHIPPED_STATES}
    problems += [f"topic {t!r} has a cards marker and no note" for t in topics if t not in shipped_topics]
    if problems:
        raise BuildError("\n".join(problems))
    head = BANNER if banner else ""
    out = {f"knowledge/notes/{n.state}/{n.slug}.md": short_note(n) for n in notes if n.state in SHIPPED_STATES}
    # The area templates still place each topic in an area; their pages are not shipped since 0.0.30, as no
    # session or step read them (`meta/decisions.md`, d-5ed7e8-da9b80): the index routes to the cards.
    out["knowledge/INDEX.md"] = head + render_index((templates / "INDEX.md").read_text(encoding="utf-8"), notes, topics, order,
                                                     link=_card_link if banner else None,
                                                     name=_card_name if banner else None)
    groups = principles(notes)
    out.update({f"knowledge/cards/{n.slug}.md": render_card(n, [s for s in groups.get(n.meta.get("principle"), []) if s is not n])
                for n in notes if n.state in SHIPPED_STATES})
    reviewer = templates / "knowledge-reviewer.md"
    if reviewer.is_file():
        # The reviewer subagent of the phased session: one template, the topics filled in from the areas.
        where = reviewer.relative_to(root).as_posix()
        text = reviewer.read_text(encoding="utf-8").replace("{{topics}}", "topics: " + ", ".join(topics))
        if "{{" in text:
            raise BuildError(f"{where}: a token the build does not fill")
        if not text.startswith("---\n"):
            raise BuildError(f"{where}: a subagent definition opens with its frontmatter")
        try:
            meta = B.read_frontmatter(text, where)[0]
        except B.FrontmatterError as e:
            raise BuildError(str(e)) from None
        if missing := [k for k in ("name", "description", "tools") if not str(meta.get(k) or "").strip()]:
            raise BuildError(f"{where}: the frontmatter lacks {', '.join(missing)}")
        banner = f"{RELEASE_MARK} from the home repository's sources/templates/knowledge-reviewer.md; edit that, never this file"
        out["agents/knowledge-reviewer.md"] = "---\n# " + banner + "\n" + text[4:]
    out["knowledge/OPEN.md"] = head + render_open(root / "meta")
    out[B.RECEIVED] = (RECORDS_BANNER if banner else "") + render_received(root / "meta")
    originals = root / ORIGINALS
    for skill in sorted(originals.glob("method/skills/*/SKILL.md")):
        try:
            named = B.read_frontmatter(skill.read_text(encoding="utf-8"), str(skill))[0].get("model")
        except B.FrontmatterError as e:
            raise BuildError(str(e)) from None
        if named:
            raise BuildError(f"{skill.relative_to(root).as_posix()}: names a model; switching it for a turn misses the "
                             "whole prompt cache, so a method skill never does (`prompt-context.md`, cost)")
    for path in sorted(originals.rglob("*"), key=lambda p: p.as_posix().encode()):
        if path.is_file() and "__pycache__" not in path.parts and not path.name.startswith("."):
            rel = path.relative_to(originals).as_posix()
            if rel in out:
                raise BuildError(f"{ORIGINALS}/{rel}: an original for a file the build also generates")
            text = path.read_text(encoding="utf-8")
            if rel == B.CHANGELOG:
                text = trim_changelog(text, oldest_carrier_version(root / "meta"))
            elif rel == "tools/bundle.py":
                text = strip_comments(text)
            out[rel] = with_banner(rel, text)
    return out


GENERATED = ("knowledge/notes/", "knowledge/areas/", "knowledge/INDEX.md", "knowledge/OPEN.md")
LEDGER = "meta/tracking/INDEX.md"


def history_rows(meta_dir: Path) -> list[tuple[str, str]]:
    """(slug, where it went) for every table row of the history whose first cell is a backticked slug."""
    path = meta_dir / "tracking/history.md"
    if not path.is_file():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").split("\n"):
        if re.match(r"^\| `[\w-]+` \|", line):
            cells = split_row(line)
            out.append((cells[0].strip("`"), cells[1] if len(cells) > 1 else ""))
    return out


def render_ledger(root: Path) -> str:
    """`meta/tracking/INDEX.md`: one line per idea the home has already met, so no meta-session recreates it.

    Generated from the full notes and the records: notes under review and retired, candidates in the
    queue or offered again, and every candidate the history says left the queue.
    """
    notes = load_notes(root / "sources", strict_cards=False)
    queue = read_table(root / "meta/tracking/candidates.md", CANDIDATES_HEADER, prefix=True)
    text = (root / "meta/tracking/candidates.md").read_text(encoding="utf-8")
    again = []
    if AGAIN_HEADING in text:
        tail = text[text.index(AGAIN_HEADING):]
        again = [split_row(l) for l in tail.split("\n") if l.startswith("| ") and not l.startswith(CANDIDATES_HEADER)]
    def line(slug: str, *rest: str) -> str:
        return f"- `{slug}` — " + " · ".join(_clip(r, 140) for r in rest if r)
    review = [line(n.slug, n.meta.get("claim", "")) for n in notes if n.state == "review"]
    retired = [line(n.slug, n.meta.get("retired_because", ""), f"superseded by `{n.meta['superseded_by']}`"
                    if n.meta.get("superseded_by") else "") for n in notes if n.state == "retired"]
    queued = [line(slug_of(r[0]), f"{r[1]}, since {r[5] if len(r) > 5 else '?'}", f"lacks {r[2]}") for r in queue]
    offered = [line(slug_of(r[0]), "another occurrence to merge") for r in again]
    answered = [line(slug, where) for slug, where in history_rows(root / "meta")]
    parts = [
        "<!-- Generated by `release.py build` from sources/notes/ and meta/tracking/. Edit those, never this file. -->",
        "",
        "# Ledger — every idea the home has already met",
        "",
        "Read it before admitting a note or writing a candidate: an idea listed here is extended, merged or left",
        "answered, never created again under a new name. The full rows are in `candidates.md` and `history.md`,",
        "the notes in `sources/notes/`.",
    ]
    for title, rows in (("Notes under review", review), ("Retired notes", retired), ("Candidates in the queue", queued),
                        ("Offered again, to merge", offered), ("Answered: admitted, folded, refused or dropped", answered)):
        parts += ["", f"## {title} ({len(rows)})", "", *(rows or ["None."])]
    return "\n".join(parts) + "\n"


def _generated_on_disk(bundle: Path) -> set[str]:
    """Every shipped file but the checksums: all of them come from the build now."""
    return {rel for rel in B.shipped(bundle) if rel not in UNMARKED}


def build(root: Path = ROOT, check: bool = False) -> list[str]:
    """Writes, or with `check` compares, everything generated and then `SHA256SUMS`.

    Returns:
        With `check`: one problem per generated file that is stale, missing or not produced by the sources,
        and a stale `SHA256SUMS`. Without: what was written or removed.
    """
    bundle = root / ".agents"
    outputs = build_outputs(root)
    stale = sorted(_generated_on_disk(bundle) - set(outputs), key=str.encode)
    ledger = render_ledger(root)
    ledger_path = root / LEDGER
    if check:
        problems = [f"{rel}: generated, and not what the sources produce (run `release.py build`)"
                    for rel, text in sorted(outputs.items()) if not (bundle / rel).is_file()
                    or (bundle / rel).read_bytes() != text.encode("utf-8")]
        problems += [f"{rel}: generated by nothing in sources/; `release.py build` removes it" for rel in stale]
        problems += form_problems(root) if not problems else []
        if not ledger_path.is_file() or ledger_path.read_bytes() != ledger.encode("utf-8"):
            problems.append(f"{LEDGER}: generated, and not what the records produce (run `release.py build`)")
        if not problems and (not (bundle / B.CHECKSUMS).is_file()
                             or (bundle / B.CHECKSUMS).read_bytes() != checksums_text(bundle).encode("utf-8")):
            problems.append(f"{B.CHECKSUMS}: not the checksums of the bundle as it is (run `release.py build`)")
        return problems
    changes = []
    for rel, text in outputs.items():
        path = bundle / rel
        if not path.is_file() or path.read_bytes() != text.encode("utf-8"):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(text.encode("utf-8"))
            changes.append(f"wrote {rel}")
    for rel in stale:
        (bundle / rel).unlink()
        changes.append(f"removed {rel}")
    if not ledger_path.is_file() or ledger_path.read_text(encoding="utf-8") != ledger:
        ledger_path.write_text(ledger, encoding="utf-8")
        changes.append(f"wrote {LEDGER}")
    write_checksums(bundle)
    return changes


# --- versions, tags and the release ------------------------------------------------------------------


def git(*args: str, repo: Path = ROOT, binary: bool = False) -> str | bytes:
    return B.git(repo, *args, binary=binary)


def tags(repo: Path = ROOT) -> list[str]:
    """The release tags, `vX.Y.Z`, oldest first by Semantic Versioning precedence."""
    names = [n for n in str(git("tag", "-l", "v*", repo=repo)).split() if B.SEMVER.match(n[1:])]
    return sorted(names, key=B.semver_key)


def tag_dates(repo: Path = ROOT) -> dict[str, str]:
    """{tag: date of the commit it tags}: a retro-tag counts from its commit, not from the day it was made."""
    out = str(git("for-each-ref", "refs/tags/v*", "--format=%(refname:short) %(*committerdate:short)%(committerdate:short)", repo=repo))
    dates = {}
    for line in out.splitlines():
        name, _, date = line.partition(" ")
        dates[name] = date[:10]
    return dates


def legacy_version(tree: Path) -> str | None:
    """The version a pre-0.0.22 bundle declares, as SemVer: its integer `version: N` becomes 0.0.N."""
    value = B.field(B.header(tree / "README.md"), "version") if (tree / "README.md").is_file() else None
    return f"0.0.{int(value)}" if value and value.isdigit() else None


def installed_version(tree: Path) -> str | None:
    return B.bundle_version(tree) or legacy_version(tree)


def set_version(root: Path, version: str, released: str, parent: str | None = None) -> None:
    """Version, date, the building home's id (its own carrier file) and the tag this release follows."""
    readme = root / ORIGINALS / "README.md"
    data, body = B.read_frontmatter(readme.read_text(encoding="utf-8"), str(readme))
    data.update({"version": version, "released": released})
    home = (B.read_carrier(root / ".agents") or {}).get(B.CARRIER_FIELD)
    if home:
        data["home"] = home
    if parent:
        data["parent"] = parent
    readme.write_text(B.dump_frontmatter(data) + body, encoding="utf-8")


def release(version: str, root: Path = ROOT) -> str:
    """Cuts a release: version and date into the README, the build, and the tag command to run.

    Refused unless the version is newer than every release tag and the changelog has its dated section:
    a release nobody described is a release nobody can triage.
    """
    B.semver_key(version)
    existing = tags(root)
    if existing and B.semver_key(version) <= B.semver_key(existing[-1][1:]):
        raise RefusedError(f"{version} is not newer than the last release, {existing[-1]}")
    text = (root / ORIGINALS / B.CHANGELOG).read_text(encoding="utf-8")
    section = next((m for m in B.CHANGELOG_SECTION.finditer(text) if m.group(1) == version), None)
    if section is None or not section.group(2):
        raise RefusedError(f"{B.CHANGELOG} has no `## [{version}] - YYYY-MM-DD` section; describe the release first")
    over = export_over_cap(root, EXPORT_CAP)
    if over:
        raise RefusedError(over)
    set_version(root, version, section.group(2), existing[-1] if existing else None)
    build(root)
    B.record_lineage(root / ".agents", section.group(2))
    return f'git tag -a v{version} -m "agent-guides {version}"'


# --- the home's own checks -----------------------------------------------------------------------------
# The sessions only the home runs: their `Reads:` lists name paths from the repository root.
HOME_SESSIONS = {"sync": ("meta/method/prompt-sync.md", 0), "merge": ("meta/method/prompt-merge.md", 0)}


def home_files(root: Path = ROOT) -> list[Path]:
    return [p for folder in ("meta", "sources") for p in sorted((root / folder).rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts and not any(part.startswith(".") for part in p.relative_to(root).parts)]


def home_link_problems(root: Path = ROOT) -> list[str]:
    """Dead links in `meta/` and `sources/`, and links into the generated notes, which move with a note's state."""
    problems = []
    for path in home_files(root):
        if path.suffix != ".md":
            continue
        rel = path.relative_to(root).as_posix()
        for target, resolved in B._links(root, rel):
            if not (root / resolved).exists():
                problems.append(f"{rel}: links to {target}, which does not exist")
            elif resolved.startswith(".agents/knowledge/notes/"):
                problems.append(f"{rel}: links to the generated {target}; link the full note in sources/notes/")
    return problems


def home_session_problems(root: Path = ROOT) -> list[str]:
    problems = []
    for name, (rel, index) in HOME_SESSIONS.items():
        path = root / rel
        found = B.reads_lists(path.read_text(encoding="utf-8")) if path.is_file() else []
        if index >= len(found):
            problems.append(f"session {name!r}: {rel} has no `Reads:` list number {index}")
            continue
        problems += [f"session {name!r}: {p}" for p in B._session_parts(root, found[index])[1]]
    return problems


def check(root: Path = ROOT) -> tuple[list[str], list[str]]:
    """The home's CI: the bundle verifies, the build is current, the records link and leak nothing.

    Returns:
        (problems, notes): every failure, and the privacy warnings and allowances to print.
    """
    bundle = root / ".agents"
    privacy = B.privacy_check(bundle)
    problems = B.verify_problems(bundle, privacy) + build(root, check=True)
    home = B.privacy_check(paths=home_files(root))
    problems += [f"privacy: {f.where} {f.rule}: {f.match}" for f in home.failures]
    problems += B.invisible_characters(root, [p.relative_to(root).as_posix() for p in home_files(root)])
    problems += home_link_problems(root) + home_session_problems(root) + B.budget_problems(bundle)
    problems += [f"meta/tracking/candidates.md: {s}: *Since* is not a release version" for s in funnel(root)["since_invalid"]]
    problems += queue_problems(root) + manifest_problems(root)
    log = root / "meta/decisions.md"  # the home's own decisions log, in the format artifact 6 asks of carriers
    errors, warnings, _ = B.decision_check([log]) if log.is_file() else ([], [], {})
    problems += [f"decisions: {e}" for e in errors]
    over = export_over_cap(root, EXPORT_CAP)
    return problems, (privacy.notes() + home.notes() + [f"  ! decisions: {w}" for w in warnings]
                      + ([f"  ! WARN {over}"] if over else [])
                      + [f"  ! {w}" for w in B.user_deny_warnings(root)])


QUEUE_ROW = re.compile(r"^(?:(?:extends|overlaps)\s+)?`?[a-z0-9][\w.-]*`?(?:\s*\+\s*`?[a-z0-9][\w.-]*`?)*\s+—\s")


def queue_problems(root: Path = ROOT) -> list[str]:
    """Every queued candidate whose row does not open with its slug: a harvest can only extend what it can name."""
    rows = read_table(root / "meta/tracking/candidates.md", CANDIDATES_HEADER, prefix=True)
    return [f"meta/tracking/candidates.md: {r[0][:50]!r}: does not open with its slug (`slug — claim`)"
            for r in rows if not QUEUE_ROW.match(r[0].strip())]


# `MANIFEST.md`'s checked limits. The export's cap was 0.0.29's shipped bytes, raised once to 1 MB and no further
# (d-5ed7e8-efd0e2): the room is not a budget. It binds at the cut: between releases the export may grow past it and
# `check` warns; `release` refuses.
EXPORT_CAP = 1_000_000
DESCRIPTIONS_CAP = 2_776  # chars of the skill and agent descriptions a carrier loads on every turn, in total
# Each description is capped by its kind, since a long process must recognise varied phrasing and an agent run only
# on request need not (the descriptions' caps by kind, in meta/decisions.md).
DESCRIPTION_KIND_CAPS = {"long process": 750, "light skill": 250, "agent on request": 250, "delegated agent": 200}
DESCRIPTION_KINDS = {"close": "long process", "decision-review": "long process", "user-walk": "long process",
                     "next": "light skill", "knowledge-reviewer": "agent on request", "researcher": "delegated agent"}
HANDOFF_CAP = 500  # words in the roadmap's *Where we are*


def export_over_cap(root: Path = ROOT, export_cap: int = EXPORT_CAP) -> str | None:
    """The message when the shipped export is over its cap, else None: a warning from `check`, a refusal from `release`."""
    tree = root / ".agents"
    size = sum((tree / rel).stat().st_size for rel in B.shipped(tree)) if tree.is_dir() else 0
    if size > export_cap:
        return f"the export ships {size} bytes, over the manifest's cap of {export_cap}; shrink it before the cut"
    return None


def manifest_problems(root: Path = ROOT, export_cap: int = EXPORT_CAP, descriptions_cap: int = DESCRIPTIONS_CAP,
                      handoff_cap: int = HANDOFF_CAP) -> list[str]:
    """The limits `MANIFEST.md` marks as checked: what every turn loads and the hand-off (the export binds at the cut)."""
    problems = []
    tree = root / ".agents"
    described = sorted(tree.glob("method/skills/*/SKILL.md")) + sorted(tree.glob("agents/*.md"))
    lengths = {}
    for f in described:
        meta = B.read_frontmatter(f.read_text(encoding="utf-8"), str(f))[0]
        lengths[str(meta.get("name") or f.parent.name)] = len(str(meta.get("description", "")))
    chars = sum(lengths.values())
    for name, length in sorted(lengths.items()):
        kind = DESCRIPTION_KINDS.get(name)
        if kind is None:
            problems.append(f"{name}: a description with no kind; add it to DESCRIPTION_KINDS in meta/tools/release.py")
        elif length > DESCRIPTION_KIND_CAPS[kind]:
            problems.append(f"{name}: its description is {length} chars, over the cap for its kind, {kind} ({DESCRIPTION_KIND_CAPS[kind]})")
    if chars > descriptions_cap:
        problems.append(f"the skill and agent descriptions are {chars} characters, over the manifest's cap of {descriptions_cap}")
    roadmap = root / "meta/roadmap.md"
    if roadmap.is_file():
        section = re.search(r"^## Where we are[ \t]*\r?\n(.*?)(?=^## |\Z)", roadmap.read_text(encoding="utf-8"), re.S | re.M)
        words = len(section.group(1).split()) if section else 0
        if not section:
            problems.append("meta/roadmap.md: no *Where we are* section, so the hand-off cap cannot be read")
        elif words > handoff_cap:
            problems.append(f"meta/roadmap.md: the hand-off is {words} words, over the manifest's cap of {handoff_cap}")
    return problems

# --- carriers: gather, intake, lost, splice, register, align ------------------------------------------
# A carrier writes only what it owns: its carrier file and its harvest outbox. So a meta-session over
# carriers on the current layout gathers their outboxes and checks, by their checksums, that nothing
# else moved. A carrier still on a layout from before 0.0.22 is compared line by line with the release
# it holds, which the home has under its tag, and `lost` names every line it added.

GATHER_MARKER = ".bundle-gather"
CANDIDATES_HEADER = "| Candidate | Kind | Lacks | Evidence | First seen |"
EXPERIMENTS_RUN_HEADER = "| Date | Note | Where | What was run | Result | Verdict |"


def _names(repos: list[Path]) -> list[str]:
    if not repos:
        raise RefusedError("no repositories in scope: name the carriers this session has open")
    names = [repo.name for repo in repos]
    twice = sorted({n for n in names if names.count(n) > 1})
    if twice:
        raise RefusedError(f"two carriers are both called {', '.join(twice)}: give each checkout its own folder name")
    return names


def extract(tag: str, into: Path, root: Path = ROOT) -> Path:
    """The `.agents` folder of a release tag, from `git archive`, without touching the working tree."""
    import io
    import tarfile

    data = git("archive", tag, ".agents", repo=root, binary=True)
    with tarfile.open(fileobj=io.BytesIO(data)) as archive:  # type: ignore[arg-type]
        archive.extractall(into, filter="data")
    return into / ".agents"


def _body(path: Path) -> str | None:
    """A file's content with any frontmatter removed: what a line comparison across layouts reads."""
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    return B.split_frontmatter(text)[1] if path.suffix == ".md" else text


def _lines(path: Path) -> set[str]:
    return {line for line in (_body(path) or "").split("\n") if line.strip()}


# Where a file of a bundle from before 0.0.22 lives now. Every path not listed stayed where it was.
PATH_MAP = {
    "roadmap.md": ["meta/roadmap.md"],
    "references.md": ["sources/references.md"],
    "layout.md": ["sources/layout.md"],
    "method/prompt-sync.md": ["meta/method/prompt-sync.md"],
    "method/prompt-merge.md": ["meta/method/prompt-merge.md"],
    "method/changelog.md": ["meta/archive/method-changelog.md"],
    "method/prompt-context.md": [".agents/method/prompt-context.md", "meta/method/home.md"],
    "knowledge/README.md": [".agents/knowledge/README.md", "sources/README.md"],
    "knowledge/INDEX.md": [".agents/knowledge/INDEX.md", "sources/templates/INDEX.md"],
}


def home_counterparts(rel: str, root: Path = ROOT) -> list[Path]:
    """The home files that hold what `rel` held in a bundle from before 0.0.22."""
    if rel in PATH_MAP:
        return [root / p for p in PATH_MAP[rel]]
    if rel.startswith("knowledge/notes/"):
        name = rel.rsplit("/", 1)[-1]
        return sorted((root / "sources/notes").glob(f"*/{name}")) + sorted((root / ".agents/knowledge/notes").glob(f"*/{name}"))
    if rel.startswith("knowledge/areas/"):
        return [root / ".agents" / rel, root / "sources/templates/areas" / rel.rsplit("/", 1)[-1]]
    if rel.startswith("tracking/"):
        return [root / "meta" / rel]
    return [root / ".agents" / rel]


def lost(base: Path, snapshots: dict[str, Path], root: Path = ROOT) -> list[tuple[str, str, str]]:
    """Every non-blank line a carrier added over the release it holds that the home does not hold.

    The home is read across its whole layout (`.agents/`, `meta/`, `sources/`), so a line that moved
    to the full notes or the release records is found where it went.
    """
    missing = []
    frame = {B._cells_of(h)[0] for h in B.OUTBOX_COLUMNS.values()}
    for name, tree in snapshots.items():
        for rel in B.all_files(tree):
            if (B.is_carrier_owned(rel) and not rel.startswith("tracking/")) or rel == B.CHECKSUMS:
                continue
            added = _lines(tree / rel) - _lines(base / rel)
            if rel in B.OUTBOX:
                # The rows of the old outbox tables travel as proposals, taken in and recorded by id: they are
                # accounted for there, however intake rewrote them and however a formatter spaced them.
                rows = {line for line, _ in B.outbox_table(tree / rel, rel)[0]}
                added = {line for line in added if line.strip() not in rows and not B.TABLE_SEPARATOR.match(line.strip())
                         and not (line.strip().startswith("|") and B._cells_of(line.strip())[:1]
                                  and B._cells_of(line.strip())[0] in frame)}
            present = set().union(*(_lines(p) for p in home_counterparts(rel, root))) if added else set()
            missing += [(name, rel, line) for line in sorted(added - present)]
    return missing


def _added_rows(tree: Path, base: Path) -> list[tuple[str, list[str]]]:
    """The outbox rows of a bundle from before 0.0.22 that its release did not already hold: the carrier's own."""
    known = {(rel, tuple(row)) for rel, row in B.outbox_rows(base)}
    return [(rel, row) for rel, row in B.outbox_rows(tree) if (rel, tuple(row)) not in known]


def _carrier_of(tree: Path) -> str:
    """A carrier's id: its carrier file's, or on the old layout its headers', or one minted since into a carrier file."""
    try:
        own = legacy_own_fields(tree) if B.is_legacy(tree) else {}
        return str(own.get("carrier") or (B.read_carrier(tree) or {}).get("carrier") or "")
    except RefusedError:
        return ""


def _unconverted(tree: Path, base: Path, rows: list[tuple[str, list[str]]], name: str, root: Path) -> list[str]:
    """Lines a carrier on the old layout added to its `tracking/` that are neither rows to convert nor held by
    the home: what converting it would remove unread."""
    return [f"{rel}: {line.strip()[:80]}" for _, rel, line in lost(base, {name: tree}, root) if rel.startswith("tracking/")]


def _offered(tree: Path, base: Path | None) -> tuple[list[dict], list[str]]:
    """What a carrier offers: its proposals, and each row of an outbox from before them as the proposal it
    becomes when the carrier converts it (the same id), so nothing is taken in twice."""
    from dataclasses import asdict

    found, problems = B.proposals_of(tree)
    offered = [{**asdict(p), "source": f"{B.PROPOSALS}/{p.id}.md"} for p in found]
    legacy = B.is_legacy(tree)
    rows = _added_rows(tree, base) if legacy and base is not None else [] if legacy else B.outbox_rows(tree)
    if legacy and base is None and B.outbox_rows(tree):
        problems.append("its tracking rows cannot be told from its release's without that release's tag; read them by hand")
    if not legacy:
        problems += [f"{rel}: not a row of its table, and a conversion would refuse to remove it: {line.strip()[:80]!r}"
                     for rel in B.OUTBOX for line in B.outbox_table(tree / rel, rel)[1]]
    carrier = _carrier_of(tree)
    if rows and not B.CARRIER_ID.match(carrier):
        problems.append(f"{len(rows)} outbox rows cannot become proposals: it has no carrier id")
        rows = []
    offered += [{**asdict(B.row_proposal(rel, row, carrier)), "source": f"{rel}, the row {row[0][:40]!r}"} for rel, row in rows]
    return offered, problems


def proposal_privacy(offered: list[dict]) -> dict[str, list[str]]:
    """Each proposal's privacy findings, read as the carrier's own file is read: a FAIL, or a WARN that no
    `privacy-allow: <reason>` on its line answered, keeps it out of the intake until the carrier generalises
    it or its owner answers. Only the rule and the line are reported, never what matched."""
    import tempfile

    found: dict[str, list[str]] = {}
    with tempfile.TemporaryDirectory() as scratch:
        folder = Path(scratch) / ".agents" / B.PROPOSALS
        folder.mkdir(parents=True)
        for item in offered:
            proposal = B.Proposal(**{k: v for k, v in item.items() if k != "source"})
            path = folder / f"{proposal.id}.md"
            path.write_text(B.render_proposal(proposal), encoding="utf-8")
            findings = B.privacy_check(paths=[path]).findings
            if findings:
                found[proposal.id] = [f"{f.level} {f.rule} at line {f.where.rsplit(':', 1)[-1]}" for f in findings]
    return found


def _forked_from(base: Path, tree: Path) -> list[str]:
    """Every shipped file that differs from the tagged release, even when the carrier rewrote its checksums."""
    ours, theirs = set(B.shipped(base)), set(B.shipped(tree))
    out = [f"{rel}: differs from the tagged release" for rel in sorted(ours & theirs)
           if (base / rel).read_bytes() != (tree / rel).read_bytes()]
    out += [f"{rel}: missing, the tagged release ships it" for rel in sorted(ours - theirs)]
    out += [f"{rel}: not in the tagged release" for rel in sorted(theirs - ours)]
    return out


def gather(repos: list[Path], out: Path, root: Path = ROOT, packs: list[Path] | None = None,
           missing: tuple[Path, ...] = ()) -> dict:
    """Phase 1, read-only: every carrier against the release it holds; its proposals; what it forked.

    `packs` are proposals a carrier sent as one file (`bundle.py proposals --pack`), from a machine where
    this session cannot open it: read as they are, never extracted. `missing` are carriers with no bundle
    on disk: the report says *not read* for each, so their proposals are never dropped in silence.
    """
    import json
    import shutil

    names = _names(repos)
    if out.exists() and (not out.is_dir() or (any(out.iterdir()) and not (out / GATHER_MARKER).exists())):
        raise RefusedError(f"{out}: exists and is not a previous gather's output; give it a new or empty folder")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / GATHER_MARKER).write_text("written by release.py gather; the whole folder is replaced by the next one\n")
    available = set(tags(root))
    report: dict = {"carriers": {}, "packs": {}}
    lines = [f"# Gather — {len(repos)} carrier{'' if len(repos) == 1 else 's'}" + (f", {len(missing)} not read" if missing else "") + (f" and {len(packs)} pack{'' if len(packs) == 1 else 's'}" if packs else ""), ""]
    for path in missing:
        branches = bundle_branches(path)
        lines += [f"## {path.name} — not read: no bundle on disk", "",
                  *[f"- a bundle on {b} ({v})" for b, v in branches], "- its proposals, if any, were not gathered", ""]
    report["missing"] = [path.name for path in missing]
    for repo, name in zip(repos, names):
        snapshot = out / "carriers" / name / ".agents"
        shutil.copytree(repo / ".agents", snapshot, ignore=shutil.ignore_patterns("__pycache__"))
        version = installed_version(snapshot)
        legacy = B.is_legacy(snapshot)
        base = None
        if version and f"v{version}" in available:
            place = out / "base" / version
            base = place / ".agents" if place.exists() else extract(f"v{version}", place, root)
        entry = {"version": version, "legacy": legacy, "base": str(base) if base else None}
        # The home's own release files are the build's, ahead of its last tag while a release is being written.
        home = repo.resolve() == root.resolve()
        entry["forked"] = [] if legacy or home else B.check_local(repo) + (_forked_from(base, snapshot) if base else [])
        entry["lost"] = [f"{rel}: {line[:120]}" for _, rel, line in lost(base, {name: snapshot}, root)] if legacy and base else []
        entry["proposals"], entry["problems"] = _offered(snapshot, base)
        entry["privacy"] = [f"{pid}: {'; '.join(found)}" for pid, found in proposal_privacy(entry["proposals"]).items()]
        report["carriers"][name] = entry
        offered = entry["proposals"]
        old = sum(not o["source"].startswith(B.PROPOSALS) for o in offered)
        lines += [f"## {name} — holds {version or 'an unknown version'}" + (" (layout before 0.0.22)" if legacy else ""), "",
                  f"- base: {'tag v' + version if base else 'none: no release tag for this version; compare by hand'}",
                  f"- offers {len(offered)} proposals" + (f", {old} of them rows of its old outbox" if old else ""),
                  *[f"- not readable as a proposal: {p}" for p in entry["problems"]],
                  *[f"- privacy, not taken in until generalised or answered: {p}" for p in entry["privacy"]],
                  *[f"- changed what only a release writes: {p}" for p in entry["forked"]],
                  *[f"- added over its release, and not in the home: {p}" for p in entry["lost"]], ""]
    from dataclasses import asdict

    for pack in packs or []:
        found, problems = [], []
        for name, text in sorted(read_pack(pack).items()):
            proposal, issues = B.parse_proposal(text, f"{pack.name}:{name}")
            if proposal is not None and proposal.id != name.removesuffix(".md"):
                issues.append(f"{pack.name}:{name}: its `proposal` field is {proposal.id}, not its file name")
            problems += issues
            if proposal is not None and not issues:
                found.append({**asdict(proposal), "source": f"{pack.name}:{name}"})
        flagged = [f"{pid}: {'; '.join(f)}" for pid, f in proposal_privacy(found).items()]
        report["packs"][pack.name] = {"proposals": found, "problems": problems, "privacy": flagged}
        lines += [f"## pack {pack.name}", "", f"- offers {len(found)} proposals",
                  *[f"- not readable as a proposal: {p}" for p in problems],
                  *[f"- privacy, not taken in until generalised or answered: {p}" for p in flagged], ""]
    (out / "gather.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (out / "gather.md").write_text("\n".join(lines), encoding="utf-8")
    return report


def slug_of(cell: str) -> str:
    """The slug a candidate row names: its first word, without markup; `extends x` names note x."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", re.sub(r"[`*]", "", cell)).strip()
    text = re.sub(r"^(?:extends|overlaps)\s+", "", text, flags=re.IGNORECASE).strip()
    return re.split(r"\s+[—-]\s+|\s", text, maxsplit=1)[0].strip(".,:;").lower()


def candidate_cell(p: B.Proposal) -> str:
    """The queue's first cell for a proposal: `slug — claim`, or `extends slug — …` for an extension."""
    return (f"{p.action} " if p.action in ("extends", "overlaps") else "") + f"{p.target} — " + " ".join(p.claim.split())


def _note_text(root: Path, rev: str | None, slug: str) -> str | None:
    for state in NOTE_STATES:
        rel = f"sources/notes/{state}/{slug}.md"
        if rev is None:
            if (root / rel).is_file():
                return (root / rel).read_text(encoding="utf-8")
        else:
            try:
                return str(git("show", f"{rev}:{rel}", repo=root))
            except Exception:  # noqa: BLE001 -- not at that tag, in that state
                continue
    return None


def base_moved(p: B.Proposal, root: Path, available: set[str]) -> bool:
    """Whether the note a proposal concerns changed after the release it was written against."""
    now = _note_text(root, None, p.target)
    if now is None or not p.base or f"v{p.base}" not in available:
        return False
    return _note_text(root, f"v{p.base}", p.target) != now


RECEIVED_INTRO = (
    "# Proposals received\n\n"
    "Every proposal a carrier offered that `release.py intake` took in, by its id, the release it was taken in at, "
    "and where it went. `release.py build` publishes this table as `.agents/proposals/RECEIVED.md`, and each carrier "
    "removes the proposals listed there with `bundle.py proposals --prune`. Ids only: which carrier offered a "
    "proposal is never written here or anywhere in the home. Rows are appended by `intake`, never edited.\n\n"
    + B.RECEIVED_HEADER + "\n|---|---|---|\n")


def intake(out: Path, version: str, root: Path = ROOT) -> dict:
    """The gathered proposals into the home's records: new candidates queued, duplicates named, runs logged.

    A candidate whose slug the queue, the history or a note already holds is not queued twice; it is
    listed so the release can add it to that row as another occurrence, which is what admission counts.
    Every proposal taken in is written to `meta/tracking/received.md` with where it went; one already
    there is skipped, so a carrier that has not pruned yet is never taken in twice.
    """
    import json

    report = json.loads((out / "gather.json").read_text(encoding="utf-8"))
    queue_path, runs_path = root / "meta/tracking/candidates.md", root / "meta/tracking/experiments.md"
    queued = {slug_of(r[0]) for r in read_table(queue_path, CANDIDATES_HEADER, prefix=True)}
    history = (root / "meta/tracking/history.md").read_text(encoding="utf-8") if (root / "meta/tracking/history.md").is_file() else ""
    notes = {p.stem for p in (root / "sources/notes").rglob("*.md")}
    heard = {r[0].strip("`") for r in received_rows(root / "meta")}
    available = set(tags(root))
    result: dict = {"queued": [], "duplicates": [], "refused": [], "runs": 0, "received": [], "skipped": 0,
                    "moved": [], "malformed": [], "privacy": []}
    new_rows, new_runs, refused, again, ledger = [], [], [], [], []
    sources = [*report["carriers"].items(), *[(f"pack {k}", v) for k, v in report.get("packs", {}).items()]]
    for name, entry in sources:
        result["malformed"] += [f"{name}: {p}" for p in entry.get("problems", [])]
        for offered in entry.get("proposals", []):
            p = B.Proposal(**{k: v for k, v in offered.items() if k != "source"})
            if p.id in heard:
                result["skipped"] += 1
                continue
            _, issues = B.parse_proposal(B.render_proposal(p), offered["source"])
            if issues:
                result["malformed"] += [f"{name}: {i}" for i in issues]
                continue
            # Read again here, whatever gather said: gather.json is a file anyone can edit, and a pack or a
            # carrier without the hooks never ran the check. A warning no owner answered stays out too.
            flagged = proposal_privacy([offered]).get(p.id)
            if flagged:
                result["privacy"].append(f"{name}: {p.id}: {'; '.join(flagged)}")
                continue
            heard.add(p.id)
            if p.kind == "experiment":
                new_runs.append(_row([p.seen, p.target, p.where, " ".join(p.claim.split()), " ".join(p.evidence.split()), p.verdict]))
                verdict = f"run logged against `{p.target}`"
            else:
                slug, kind = p.target, B.PROPOSAL_KINDS[p.kind]
                cells = [candidate_cell(p), kind, p.lacks, " ".join(p.evidence.split()), p.seen]
                if p.lacks.lower().startswith("refused"):
                    # A learning the harvest refused: recorded where the next harvest looks, never queued.
                    refused.append(f"| `{slug}` | {p.lacks} |")
                    result["refused"].append(slug)
                    verdict = "refused by its harvest; recorded in the history"
                elif slug in queued or slug in notes or f"`{slug}`" in history:
                    result["duplicates"].append(f"{name}: {slug} (already {'a note' if slug in notes else 'queued or answered'})")
                    again.append(_row([*cells, version]))
                    verdict = f"another occurrence of `{slug}`, to merge"
                else:
                    queued.add(slug)
                    new_rows.append(_row([*cells, version]))
                    result["queued"].append(slug)
                    verdict = f"queued as `{slug}`"
            if base_moved(p, root, available):
                result["moved"].append(f"{p.id}: `{p.target}` changed after {p.base}, which it was written against; read it again before merging")
            ledger.append(_row([f"`{p.id}`", version, verdict]))
            result["received"].append(p.id)
    _insert_rows(queue_path, CANDIDATES_HEADER, new_rows, at_top=False)
    if again:
        # Another occurrence of something known is evidence: kept, for the release to add to its row or note.
        text = queue_path.read_text(encoding="utf-8").rstrip("\n")
        if AGAIN_HEADING not in text:
            text += f"\n\n{AGAIN_HEADING}\n\n{AGAIN_INTRO}\n\n{CANDIDATES_HEADER} Since |\n|---|---|---|---|---|---|"
        queue_path.write_text(text + "\n" + "\n".join(again) + "\n", encoding="utf-8")
    if refused:
        history_path = root / "meta/tracking/history.md"
        text = history_path.read_text(encoding="utf-8")
        head, _, rest = text.partition("\n## ")
        section = (f"## Refused by carriers' harvests, taken in at {version}\n\n| Candidate | Where it went |\n|---|---|\n"
                   + "\n".join(refused) + "\n\n")
        history_path.write_text(head + "\n" + section + ("## " + rest if rest else ""), encoding="utf-8")
    _insert_rows(runs_path, EXPERIMENTS_RUN_HEADER, new_runs, at_top=True)
    if ledger:
        path = root / RECEIVED_LEDGER
        text = path.read_text(encoding="utf-8") if path.is_file() else RECEIVED_INTRO
        path.write_text(text.rstrip("\n") + "\n" + "\n".join(ledger) + "\n", encoding="utf-8")
    result["runs"] = len(new_runs)
    (out / "intake.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


AGAIN_HEADING = "## Offered again, to merge"
AGAIN_INTRO = ("Rows a harvest offered for a slug already queued, answered or admitted: another occurrence, a new "
               "boundary or a number. The release adds each to its row or note, then removes it from here.")


def _insert_rows(path: Path, header: str, rows: list[str], at_top: bool) -> None:
    if not rows:
        return
    lines = path.read_text(encoding="utf-8").split("\n")
    at = next(i for i, line in enumerate(lines) if line.startswith(header))
    end = at + 2
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    position = at + 2 if at_top else end
    path.write_text("\n".join(lines[:position] + rows + lines[position:]), encoding="utf-8")


def legacy_own_fields(tree: Path) -> dict:
    """A pre-0.0.22 carrier's own fields, read from its README and method headers, which must agree.

    Refused when two headers disagree: the conversion would otherwise have to pick one carrier's word.
    """
    fields: dict = {}
    sources = [tree / "README.md", *sorted((tree / "method").glob("prompt-*.md"))]
    seen: dict[str, tuple[str, object]] = {}
    for path in sources:
        front = B.header(path)
        if not front:
            continue
        start = front.find("\nadopted:")
        tail = B.parse_frontmatter(front[start + 1 : front.rindex("---\n")], str(path)) if start != -1 else {}
        upstream = B.field(front, "upstream")
        if upstream is not None:
            tail["upstream"] = upstream.strip("\"'")
        carrier = B.field(front, "carrier")
        if carrier and "carrier" not in tail:
            tail["carrier"] = carrier.strip("\"'")
        for key, value in tail.items():
            if key in seen and seen[key][1] != value:
                raise RefusedError(f"{path.name} and {seen[key][0]} disagree on `{key}`; settle it in the carrier first")
            seen[key] = (path.name, value)
            fields[key] = value
    own = {k: fields[k] for k in ("carrier", "adopted", "upstream", "adapted", "declined") if fields.get(k) is not None}
    own.setdefault("adapted", [])
    own.setdefault("declined", [])
    for key in ("adapted", "declined"):
        if isinstance(own[key], str):
            own[key] = [own[key]]
    dates = sorted(re.findall(r"\b20\d\d-\d\d-\d\d\b", "".join((tree / r).read_text(encoding="utf-8", errors="replace")
                                                             for r in B.all_files(tree) if r.startswith("tracking/"))))
    if dates:
        own["harvested_through"] = dates[-1]
    return own


def _dirty(repo: Path) -> list[str]:
    entries = str(git("status", "--porcelain", "-z", "--untracked-files=all", "--", ".agents", repo=repo)).split("\0")
    paths, skip = [], False
    for entry in entries:
        if skip:
            skip = False
            continue
        if len(entry) < 4:
            continue
        rel = entry[3:].removeprefix(".agents/")
        if not B.is_carrier_owned(rel) and "__pycache__" not in rel.split("/"):
            paths.append(rel)
        skip = entry[0] in "RC" or entry[1] in "RC"
    return paths


def splice(repo: Path, write: bool, backup: Path | None, *, root: Path = ROOT, allow_dirty: bool = False,
           scope: list[Path] | None = None) -> list[str]:
    """Phase 2 for one carrier: the release's shipped files, its own files kept, an old outbox turned into proposals.

    Refused unless the home's `.agents/` is the tagged release, byte for byte. A carrier on the layout
    before 0.0.22 has its own fields moved into `carrier.toml`, and the files that moved out removed. The
    rows of an outbox from 0.0.22 or 0.0.23 (on the old layout, the rows it added over its release) become
    one proposal each before the tables go, so a row is never lost, whether or not it was gathered.
    Nothing here removes a proposal: the carrier prunes what the release lists as received.
    """
    import shutil
    import tempfile

    source, target = root / ".agents", repo / ".agents"
    if target.resolve() == source.resolve():
        return []
    if scope is not None and repo.resolve() not in [p.resolve() for p in scope]:
        raise B.OutsideWorkspaceError(f"{repo}: not a repository of this workspace; it is not this session's to write")
    version = B.bundle_version(source)
    if f"v{version}" not in tags(root):
        raise RefusedError(f"the home's bundle is {version}, which has no tag; release and tag it before carrying it")
    tagged = str(git("show", f"v{version}:.agents/{B.CHECKSUMS}", repo=root))
    if tagged != (source / B.CHECKSUMS).read_text(encoding="utf-8") or B.checksum_problems(source):
        raise RefusedError(f"the home's .agents/ is not the tagged release v{version}; carry only a tagged release")
    if write and not allow_dirty and (dirty := _dirty(repo)):
        raise B.DirtyTreeError(f"{repo}: uncommitted bundle files {dirty}; commit them or pass allow_dirty")
    legacy = B.is_legacy(target)
    own = legacy_own_fields(target) if legacy else None
    if own is not None and not own.get("carrier") and _carrier_of(target):
        own["carrier"] = _carrier_of(target)  # minted into a carrier file since its headers were written
    held = legacy_version(target) if legacy else B.bundle_version(target)
    rows = B.outbox_rows(target)
    if legacy and any(r.startswith("tracking/") for r in B.all_files(target)):
        if not held or f"v{held}" not in tags(root):
            raise RefusedError(f"{repo}: the release it holds has no tag here, so what it added to tracking/ cannot "
                               "be told from the release's; convert it by hand first")
        with tempfile.TemporaryDirectory() as tmp:
            base = extract(f"v{held}", Path(tmp), root)
            rows = _added_rows(target, base)
            unread = _unconverted(target, base, rows, repo.name, root)
        if unread:
            raise RefusedError(f"{repo}: {len(unread)} lines it added to tracking/ are neither rows to convert nor held by "
                               f"the home, and converting would remove them; take them in first (`release.py lost`): "
                               + "; ".join(unread[:3]))
    elif not legacy:
        leftover = [f"{rel}: {line.strip()[:60]!r}" for rel in B.OUTBOX for line in B.outbox_table(target / rel, rel)[1]]
        if leftover:
            raise RefusedError(f"{repo}: {len(leftover)} lines of its old outbox are not rows of its tables, and would be "
                               "removed unread; the carrier moves them into a row first: " + "; ".join(leftover[:3]))
    carrier = _carrier_of(target)
    if rows and not B.CARRIER_ID.match(carrier):
        raise RefusedError(f"{repo}: {len(rows)} outbox rows cannot become proposals without a carrier id; mint one first")
    ships, present = set(B.shipped(source)) | {B.CHECKSUMS}, set(B.all_files(target))
    keep = {r for r in present if B.is_carrier_owned(r) and not (r.startswith("tracking/") and (legacy or r in B.OUTBOX))}
    actions = [f"write {r}" for r in sorted(ships, key=str.encode)]
    actions += [f"remove {r}" for r in sorted(present - ships - keep, key=str.encode)]
    actions += [f"convert {len(rows)} outbox rows into {B.PROPOSALS}/"] if rows else []
    actions += [f"write {B.CARRIER_FILE} (own fields moved from the old headers)"] if legacy else []
    if not write:
        return actions
    if backup is not None:
        destination = backup / repo.name / ".agents"
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(target, destination)
    if rows or any((target / rel).is_file() for rel in B.OUTBOX):
        B.convert_outbox(target, rows, carrier=carrier, base=held or "")
    for rel in present - ships - keep:
        (target / rel).unlink(missing_ok=True)
    for rel in ships:
        (target / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / rel, target / rel)
    if legacy:
        B.write_carrier(target, own)
    for folder in sorted({p.parent for p in target.rglob("*")}, key=lambda p: len(p.parts), reverse=True):
        if folder != target and folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()
    return actions


def register(repos: list[Path], date: str | None = None, root: Path = ROOT, manifest: Path | None = None) -> None:
    """One row per carrier in `meta/tracking/carriers.md`, at the version it holds, by its stored id.

    With `manifest`, the same carriers are also remembered there by name and path (`remember`): the
    registry in the repository names them only by id, and this machine's manifest is where an id meets
    the repository it belongs to.
    """
    date = date or datetime.date.today().isoformat()
    ids = carrier_ids(repos)
    if manifest is not None:
        remember([local_record(repo, date) for repo in repos], manifest)
    path = root / "meta/tracking/carriers.md"
    text = path.read_text(encoding="utf-8")
    for repo in repos:
        row = f"| {ids[repo]} | {B.bundle_version(repo / '.agents')} | {date} |"
        pattern = rf"^\| {re.escape(ids[repo])} \|.*$"
        if re.search(pattern, text, re.MULTILINE):
            text = re.sub(pattern, row, text, count=1, flags=re.MULTILINE)
        else:
            separator = "|---|---|---|\n"
            at = text.index(separator) + len(separator)
            text = text[:at] + row + "\n" + text[at:]
    path.write_text(text, encoding="utf-8")


# --- this machine's record of its carriers -------------------------------------------------------------
# The repository's registry names a carrier only by a random id, so nothing in it identifies a repository.
# Which id is which repository, and where it lives, is this machine's knowledge: it is kept in the local
# manifest, outside every repository, and never written anywhere that travels.


def main_repository(repo: Path) -> Path:
    """The repository a linked worktree belongs to, or the repository itself: a scratch worktree is deleted after
    the session, so the manifest must never remember its path (proposal `register-resolves-a-worktree-…`)."""
    shown = subprocess.run(["git", "-C", str(repo), "rev-parse", "--path-format=absolute", "--git-common-dir"],
                           capture_output=True, text=True)
    common = Path(shown.stdout.strip()) if shown.returncode == 0 and shown.stdout.strip() else None
    return common.parent.resolve() if common is not None and common.name == ".git" else repo.resolve()


def local_record(repo: Path, date: str | None = None) -> dict:
    """What this machine knows of one carrier: its id, name, path, version and when it was last seen."""
    tree = repo / ".agents"
    main = main_repository(repo)
    carrier = B.stored_carrier_id(repo)
    legacy = B.is_legacy(tree)
    if carrier is None and legacy:
        try:
            carrier = legacy_own_fields(tree).get("carrier")
        except RefusedError:
            carrier = None
    return {"carrier": carrier or "", "name": main.name, "path": str(main),
            "version": B.bundle_version(tree) or ("the layout before 0.0.22" if legacy else ""),
            "seen": date or datetime.date.today().isoformat()}


def remember(records: list[dict], manifest: Path) -> None:
    """Write `records` into this machine's manifest, keeping its `carriers` list and every other record.

    Refused when the manifest would sit inside a repository: the names it holds must never travel.
    """
    resolved = manifest.expanduser().resolve()
    for parent in resolved.parents:
        if (parent / ".git").exists():
            raise RefusedError(f"{manifest}: inside the repository {parent}; this machine's record of its carriers "
                               "names repositories and is kept outside every one")
    import tomllib

    data = tomllib.loads(resolved.read_text(encoding="utf-8")) if resolved.is_file() else {}
    listed = [str(p) for p in data.get("carriers", [])]
    # A record without an id names a repository that is no carrier yet: never written, and one an earlier
    # run wrote is dropped. Its path stays in `carriers`, which is the machine's own list.
    known = {r["path"]: r for r in data.get("carrier", []) if r.get("carrier")}
    for record in records:
        if record.get("carrier"):
            known[record["path"]] = record
        if record["path"] not in listed:
            listed.append(record["path"])
    lines = ["# This machine's carriers of the agent-guides bundle. Never committed anywhere.",
             "# `carriers` is the list of carriers; each [[carrier]] record below is rewritten by",
             "# `release.py register` and `release.py carriers`, and names the repository behind each id.",
             "carriers = [", *[f"  {B._toml_str(p)}," for p in listed], "]"]
    for path in listed:
        if path in known:
            r = known[path]
            lines += ["", "[[carrier]]", *[f"{k} = {B._toml_str(str(r.get(k, '')))}" for k in
                                             ("carrier", "name", "path", "version", "seen")]]
    resolved.parent.mkdir(parents=True, exist_ok=True)
    resolved.write_text("\n".join(lines) + "\n", encoding="utf-8")


def bundle_branches(repo: Path) -> list[tuple[str, str]]:
    """(branch, version) for every local and remote branch of `repo` whose tree holds a bundle.

    A carrier may keep its bundle on a branch that is not checked out, and then has no bundle folder on
    disk: a search of the filesystem passes it by, and reading every branch is what finds it.
    """
    if not (repo / ".git").exists():
        return []  # not a git repository (a mistyped path): no branch to read
    refs = str(git("for-each-ref", "--format=%(refname:short) %(symref)", "refs/heads", "refs/remotes", repo=repo)).split("\n")
    found = []
    for line in refs:
        name, _, symref = line.partition(" ")
        if not name or symref.strip():
            continue
        try:
            text = str(git("show", f"{name}:.agents/README.md", repo=repo))
        except Exception:  # noqa: BLE001 -- no bundle on that branch
            continue
        try:
            data, _ = B.read_frontmatter(text, f"{name}:.agents/README.md")
            version = data.get("version")
        except B.FrontmatterError:
            version = None
        found.append((name, version if isinstance(version, str) and B.SEMVER.match(version)
                       else "the layout before 0.0.22"))
    return sorted(found, key=lambda pair: pair[0].encode())


def splice_report(name: str, actions: list[str], write: bool, backup: Path | None) -> list[str]:
    """What a splice did, or would do, to one carrier: the counts, then every path it removes.

    The paths are what the carrier's own step that repoints links needs; counts alone sent it back to
    comparing file lists by hand.
    """
    removed = [a.removeprefix("remove ") for a in actions if a.startswith("remove ")]
    head = (f"{name}: {'spliced' if write else 'would splice'} {sum(a.startswith('write') for a in actions)} files, "
            f"remove {len(removed)}" + (f" (backup {backup})" if write else ""))
    return [head, *(f"  - {rel}" for rel in removed)]


def align(repos: list[Path], root: Path = ROOT, missing: tuple[Path, ...] = ()) -> list[str]:
    """Phase 3: every carrier verifies, holds the home's release byte for byte, and is registered at it."""
    problems = []
    unnamed = [repo for repo in repos if B.stored_carrier_id(repo) is None]
    problems += [f"{repo.name}: no carrier id in carrier.toml" for repo in unnamed]
    repos = [repo for repo in repos if repo not in unnamed]
    ids = carrier_ids(repos)
    version = B.bundle_version(root / ".agents")
    # The tagged release, not the working one: work built in the home after a release would otherwise unalign
    # every carrier that still equals its tag file for file (proposal `align-compares-against-the-tag`).
    shown = subprocess.run(["git", "-C", str(root), "show", f"v{version}:.agents/{B.CHECKSUMS}"], capture_output=True, text=True)
    if shown.returncode:
        return [f"the home has no tag v{version}: cut the release before aligning to it"]
    reference = shown.stdout
    table = (root / "meta/tracking/carriers.md").read_text(encoding="utf-8")
    for repo, name in zip(repos, _names(repos)):
        tree = repo / ".agents"
        problems += [f"{name}: {p}" for p in B.verify_problems(tree)]
        if (tree / B.CHECKSUMS).is_file() and (tree / B.CHECKSUMS).read_text(encoding="utf-8") != reference:
            problems.append(f"{name}: its SHA256SUMS is not the home's {version}")
        row = re.search(rf"^\| {re.escape(ids[repo])} \| ([^|]+) \|", table, re.MULTILINE)
        if not row:
            problems.append(f"{name}: {ids[repo]} is not in meta/tracking/carriers.md")
        elif row.group(1).strip() != version:
            problems.append(f"{name}: registered at {row.group(1).strip()}, the home is at {version}")
    for path in missing:
        found = "".join(f"; a bundle on {b} ({v})" for b, v in bundle_branches(path))
        problems.append(f"{path.name}: no bundle on disk{found}")
    return problems


# --- notes and the funnel -----------------------------------------------------------------------------


def note_state(slug: str, state: str, root: Path = ROOT) -> list[str]:
    """Moves a full note between state folders, rewrites every link to it in `sources/` and `meta/`, builds."""
    if state not in NOTE_STATES:
        raise RefusedError(f"unknown state {state!r}: one of {', '.join(NOTE_STATES)}")
    found = sorted((root / "sources/notes").glob(f"*/{slug}.md"))
    if len(found) != 1:
        raise RefusedError(f"note {slug!r}: {'not found' if not found else 'in more than one state'} under sources/notes/")
    old = found[0].relative_to(root).as_posix()
    new = f"sources/notes/{state}/{slug}.md"
    if old == new:
        return []
    changes = [f"moved {old} -> {new}"]
    for path in home_files(root):
        if path.suffix != ".md":
            continue
        rel = path.relative_to(root).as_posix()
        here = new if rel == old else rel

        def visit(target: str, rel: str = rel, here: str = here) -> str | None:
            resolved = B._resolve(rel, target)
            if resolved is None or (resolved != old and rel != old):
                return None
            _, anchor = B._relative(target)
            pointed = new if resolved == old else resolved
            return B.posixpath.relpath(pointed, B.posixpath.dirname(here) or ".") + anchor

        updated, count = B._each_link(path.read_text(encoding="utf-8"), visit)
        if count:
            path.write_text(updated, encoding="utf-8")
            changes.append(f"rewrote {count} link{'s' if count > 1 else ''} in {here}")
    (root / new).parent.mkdir(parents=True, exist_ok=True)
    (root / old).rename(root / new)
    if state == "retired":
        changes.append(f"left for you: `retired_because:` (and `superseded_by:`) in {new}, and a row in meta/tracking/retired.md")
    changes += build(root)
    return changes


def funnel(root: Path = ROOT) -> dict:
    """How the knowledge queue moves: candidates by releases waited, experiments queued and run.

    Informational: nothing is discarded by age. A candidate leaves the queue only by a release's decision,
    recorded in the history, and the ledger (`meta/tracking/INDEX.md`) keeps its slug in view.
    """
    released = tags(root)
    order = [t[1:] for t in released]
    current = B.bundle_version(root / ".agents")
    if current and current not in order:
        order.append(current)
    rows = read_table(root / "meta/tracking/candidates.md", CANDIDATES_HEADER, prefix=True)
    waited, invalid = [], []
    for row in rows:
        since = row[5] if len(row) > 5 else ""
        if not B.SEMVER.match(since):
            invalid.append(slug_of(row[0]))
        waited.append((slug_of(row[0]), sum(1 for v in order if B.SEMVER.match(since) and B.semver_key(v) > B.semver_key(since))))
    runs = read_table(root / "meta/tracking/experiments.md", EXPERIMENTS_RUN_HEADER)
    queued = read_table(root / "meta/tracking/experiments.md", "| Note | Experiment | Cost | Would change |")
    dates = tag_dates(root)
    last = dates.get(released[-1], "") if released else ""
    return {
        "candidates": len(rows),
        "by_releases_waited": {str(k): sum(1 for _, w in waited if w == k) for k in sorted({w for _, w in waited})},
        "since_invalid": invalid,
        "experiments_queued": len(queued),
        "experiments_run": len(runs),
        "experiments_run_since_last_release": sum(1 for r in runs if r and r[0][:10] > last),
    }


# --- command line ---------------------------------------------------------------------------------


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="release.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")
    p = sub.add_parser("build", help="the generated knowledge and SHA256SUMS, from sources/")
    p.add_argument("--check", action="store_true", help="compare instead of writing; exit 1 on any difference")
    p = sub.add_parser("release", help="version and date into the README, then build; prints the tag command")
    p.add_argument("version", metavar="X.Y.Z")
    sub.add_parser("check", help="the home's CI: verify, build --check, privacy and links of meta/ and sources/, budgets, meta/decisions.md")
    p = sub.add_parser("gather", help="phase 1: each carrier against its release tag, and its proposals (writes only --out)")
    p.add_argument("repos", nargs="*")
    p.add_argument("--out", required=True)
    p.add_argument("--packs", nargs="+", default=[], metavar="FILE", help="proposals a carrier sent as one file (`bundle.py proposals --pack`)")
    p = sub.add_parser("intake", help="a gather's proposals into meta/tracking/, each recorded as received")
    p.add_argument("out")
    p.add_argument("--version", help="the release the new candidates enter the queue at (default: the home's)")
    p = sub.add_parser("lost", help="lines a carrier added over its release that the home does not hold")
    p.add_argument("base", help="the release's .agents, as gather extracted it")
    p.add_argument("snapshots", nargs="+", help="gather's carriers/<name>/.agents folders")
    p = sub.add_parser("splice", help="phase 2: the tagged release into each carrier, its own files kept")
    p.add_argument("repos", nargs="*")
    p.add_argument("--write", action="store_true")
    p.add_argument("--backup")
    p.add_argument("--allow-dirty", action="store_true")
    p = sub.add_parser("register", help="the carriers table, by stored carrier id")
    p.add_argument("repos", nargs="*")
    sub.add_parser("carriers", help="this machine's carriers by id, name, path and version; remembered in the manifest only")
    p = sub.add_parser("align", help="phase 3: every carrier on the home's release")
    p.add_argument("repos", nargs="*")
    p = sub.add_parser("note-state", help="move a full note between states, links rewritten, then build")
    p.add_argument("slug")
    p.add_argument("state", choices=NOTE_STATES)
    p = sub.add_parser("report", help="sizes, budgets and the knowledge funnel")
    p.add_argument("--check", action="store_true", help="also fail when a budget is crossed")
    return parser


def main(argv: list[str] | None = None) -> int:  # noqa: C901, PLR0911, PLR0912 -- one branch per command
    import json
    import tempfile

    args = _parser().parse_args(argv)
    try:
        if args.command == "build":
            lines = build(ROOT, check=args.check)
            for line in lines:
                print(("  x " if args.check else "") + line)
            if args.check:
                print("build: up to date" if not lines else f"build: {len(lines)} problems")
                return 1 if lines else 0
            print(f"build: {len(lines)} files changed; SHA256SUMS written")
            return 0
        if args.command == "release":
            print(f"released {args.version}; now commit, then tag it:\n  {release(args.version)}")
            return 0
        if args.command == "check":
            problems, notes = check(ROOT)
            for line in notes + [f"  x {p}" for p in problems]:
                print(line)
            print("home check: " + ("passed" if not problems else f"{len(problems)} problems"))
            return 1 if problems else 0
        if args.command == "gather":
            scope = B.workspace(args.repos)
            for line in B._scope_report(scope, "gathered"):
                print(line)
            gather(scope.repos, Path(args.out), packs=[Path(f) for f in args.packs], missing=scope.missing)
            print(Path(args.out) / "gather.md")
            return 0
        if args.command == "intake":
            result = intake(Path(args.out), args.version or B.bundle_version(ROOT / ".agents"))
            for line in result["duplicates"]:
                print(f"  ! already known: {line}")
            for line in result["moved"]:
                print(f"  ! written against an older release: {line}")
            for line in result["malformed"]:
                print(f"  x not taken in: {line}")
            for line in result["privacy"]:
                print(f"  x not taken in, privacy (generalise it, or the carrier's owner answers with privacy-allow): {line}")
            print(f"intake: {len(result['received'])} proposals received ({len(result['queued'])} candidates queued, "
                  f"{result['runs']} experiment runs logged), {result['skipped']} already received before")
            return 0
        if args.command == "lost":
            snapshots = [Path(s) for s in args.snapshots]
            missing = lost(Path(args.base), dict(zip(_names([s.parent for s in snapshots]), snapshots)))
            for name, rel, line in missing:
                print(f"  x {name} {rel}: {line[:120]}")
            print(f"{len(missing)} lines lost")
            return 1 if missing else 0
        if args.command == "splice":
            scope = B.workspace(args.repos, writing=args.write)
            _names(scope.repos)
            backup = (Path(args.backup) if args.backup else Path(tempfile.mkdtemp(prefix="bundle-backup-"))) if args.write else None
            for line in B._scope_report(scope, "written"):
                print(line)
            for repo in scope:
                actions = splice(repo, args.write, backup, allow_dirty=args.allow_dirty, scope=scope.repos)
                if not actions:
                    print(f"{repo.name}: the home itself, left alone")
                    continue
                for line in splice_report(repo.name, actions, args.write, backup):
                    print(line)
            return 0
        if args.command == "register":
            scope = B.workspace(args.repos, writing=True)
            register(scope.repos, manifest=B.MANIFEST)
            print(f"registered {len(scope)} carriers in meta/tracking/carriers.md; names and paths in {B.MANIFEST} only")
            return 0
        if args.command == "carriers":
            # Reads each carrier, writes nothing in any repository: only this machine's manifest.
            if not B.MANIFEST.is_file():
                print(f"no manifest at {B.MANIFEST}")
                return 1
            paths = [Path(p).expanduser().resolve() for p in B.manifest_carriers(B.MANIFEST)]
            records = [local_record(p) for p in paths if (p / ".agents").is_dir()]
            remember(records, B.MANIFEST)
            for r in records:
                if r["carrier"]:
                    print(f"{r['carrier']:10} {r['version'] or '?':26} {r['name']}  {r['path']}")
            for r in records:
                # A repository started from the template and paused before its bootstrap minted an id holds a
                # release but is no carrier yet: listed, and never recorded under an empty id.
                if not r["carrier"]:
                    why = ("not a carrier yet (no carrier.toml)" if not (Path(r["path"]) / ".agents" / B.CARRIER_FILE).is_file()
                           else "no carrier id stored yet")
                    print(f"  {r['name']}: {why}; holds {r['version'] or 'no versioned release'}  {r['path']}")
            for path in paths:
                # The working tree is one branch: a bundle kept on another is found only by reading them all.
                branches = bundle_branches(path) if (path / ".git").exists() else []
                if branches:
                    print(f"  {path.name}: a bundle on " + ", ".join(f"{b} ({v})" for b, v in branches))
            print(f"remembered in {B.MANIFEST}, outside every repository")
            return 0
        if args.command == "align":
            scope = B.workspace(args.repos)
            for line in B._scope_report(scope, "aligned"):
                print(line)
            problems = align(scope.repos, missing=scope.missing)
            for problem in problems:
                print("  x " + problem)
            print(f"{len(scope) + len(scope.missing)} carriers " + ("aligned" if not problems else f"NOT aligned: {len(problems)} problems"))
            return 1 if problems else 0
        if args.command == "note-state":
            for line in note_state(args.slug, args.state) or [f"{args.slug} is already {args.state}; nothing changed"]:
                print(line)
            return 0
        if args.command == "report":
            data = B.report(ROOT / ".agents")
            print(B.report_markdown(data))
            print("## Funnel\n\n" + json.dumps(funnel(ROOT), indent=2))
            problems = B.budget_problems(ROOT / ".agents", data)
            for problem in problems:
                print("  x " + problem)
            return 1 if args.check and problems else 0
    except (BuildError, RefusedError, B.NotACarrierError, B.OutsideWorkspaceError, B.DirtyTreeError,
            B.UndeclaredScopeError, B.FrontmatterError) as error:
        print(f"  x {error}")
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
