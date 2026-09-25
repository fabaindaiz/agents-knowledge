# agents-knowledge

**A portable `.agents/` bundle for AI coding assistants: a working method and a knowledge base
of engineering judgement, released with a version so it can be copied between repositories and kept in sync.**

Agents are well read. Ask one about retries, defaults, test doubles or deploy ordering and it
gives you the textbook answer, and usually the textbook is right. The expensive cases are the
ones where it is wrong, and nothing in the agent's training tells it which case it is in. This
repository collects that missing part: **which heuristic to use, when to use it, and where it
stops working**, together with a method for keeping that knowledge alive across several
repositories.

The bundle is called `agent-guides`. This repository is its home: where the notes are written and
releases are built, tagged and offered to the repositories that carry it.

## The three folders

**`.agents/` holds only what a carrier runs; everything needed to write or release it stays outside.**

| Folder | What it holds | Ships |
|---|---|---|
| [`.agents/`](.agents/) | The paste-ready method prompts (bootstrap, evaluate, update, harvest) and their shared reference `prompt-context.md`; the knowledge notes in short form with their indexes; `tools/bundle.py`; `CHANGELOG.md` and `SHA256SUMS`. [`.agents/README.md`](.agents/README.md) is the way in | yes: copy it and you have taken everything a carrier needs |
| [`meta/`](meta/) | How a release is made and carried to every carrier (`method/prompt-sync.md`, `tools/release.py`, the tests), the roadmap, and the records: the candidate queue, history, retired notes and the carriers table | no |
| [`sources/`](sources/) | Where the content is written: the full notes, with where each came from, its literature and its evidence; the index templates; the literature behind the method and the layout survey | no, only what `release.py build` generates from it |

### The knowledge notes

Each note makes one claim in the imperative and states the case where the usual answer is
wrong. Some examples:

- [Fail-closed defaults](.agents/knowledge/notes/active/fail-closed-defaults.md): a fallback value
  should refuse to run, not quietly match production.
- [A check must be seen to fail](.agents/knowledge/notes/active/a-check-must-be-seen-to-fail.md): a
  test you have never watched fail proves nothing.
- [Retry over an irreversible effect](.agents/knowledge/notes/active/retry-over-irreversible-effect.md)
- [Coverage measures execution](.agents/knowledge/notes/active/coverage-measures-execution.md)
- [Test-double fidelity](.agents/knowledge/notes/active/test-double-fidelity.md)

A shipped note is short: the claim, why it works, when it does NOT apply, what it costs. Each area
index shows it as a card (claim, *Not when*, how to verify), so an agent opens the note only when the
boundary is unclear. Every note has a `confidence` field, so an agent can tell what was paid for from
what was only believed:

| `confidence` | Means |
|---|---|
| `measured` | A number was produced in a repository, and it is written in the note |
| `reasoned` | It follows from a mechanism, but has not been tested in a repository |
| `inherited` | It was learned elsewhere and has not been verified |

A note stays only while the evidence supports it. When evidence disputes it, it moves to review and
stays usable, marked, until it gets a verdict; a retired note stays in `sources/` and never ships. The
lifecycle is in [`sources/README.md`](sources/README.md).

## Using it in your repository

1. **Copy a release.** Take the files a release's `.agents/SHA256SUMS` lists into your repository's
   `.agents/`, and nothing else: no other repository's `carrier.toml`, `tracking/` rows or reports.
2. **Bootstrap.** Open your agent at the root of your repository and paste the *Paste this to start*
   block of [`method/prompt-bootstrap.md`](.agents/method/prompt-bootstrap.md). It mints your
   repository's random id (`bundle.py carrier-id --mint`) into `.agents/carrier.toml`, and wires your
   root file: `AGENTS.md` names `.agents/`, and for Claude Code `CLAUDE.md` imports `AGENTS.md`.
   Nothing in `.agents/` loads by itself.

To judge your current setup before adopting anything,
[`method/prompt-evaluate.md`](.agents/method/prompt-evaluate.md) reviews a repository's AI
instructions and writes a report without changing anything.

**A bundle is offered, never pushed.** `.agents/carrier.toml` belongs to your repository: its id,
when it adopted the bundle, where it pulls from, what it adapted and what it declined. No release
writes it.

## Updating and verifying

The bundle follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html), one version for the
whole bundle, in `.agents/README.md`; releases are tagged `vX.Y.Z` here. While the version is `0.0.z`,
any release may change what a carrier depends on. [`.agents/CHANGELOG.md`](.agents/CHANGELOG.md)
follows Keep a Changelog; `bundle.py changelog --since X.Y.Z` prints what changed since the version you
hold. To update, put the new release in `.agents/incoming/` and run
[`method/prompt-update.md`](.agents/method/prompt-update.md).

`.agents/SHA256SUMS` proves a copy is intact (not who made it), without this tool:

```bash
cd .agents && sha256sum -c SHA256SUMS      # or: shasum -a 256 -c SHA256SUMS
python3 .agents/tools/bundle.py verify     # also links, routing, privacy, unlisted files
```

The tool needs Python 3.11 or newer and nothing outside the standard library.

## Measuring whether it helps

[`evals/`](evals/) holds two studies, outside the bundle. Study 1
([`PROTOCOL.md`](evals/PROTOCOL.md)) asks whether a note's content reaches a decision where it
applies; five exploratory pilots are in [`REPORT.md`](evals/REPORT.md): the bundle costs about twice as
much per task for a frontier model, and a content effect shows only where the decisive fact is out of
sight, on few tasks and without significance. Study 2
([`PROTOCOL-general.md`](evals/PROTOCOL-general.md)) asks whether carrying the bundle changes general
performance on external benchmarks; it is a reviewed draft and has not run.

## Keeping several repositories in sync

A *meta-session* runs from here over every carrier open on the machine: it gathers what each one's
harvest learned, builds and tags one release, splices it into each carrier and checks they all end
on that version. Each machine lists its own carrier paths in `~/.config/agent-guides/carriers.toml`,
which is never committed. [AGENTS.md](AGENTS.md) describes the procedure.

## Conventions

- **Nothing private, direct or reconstructible.** No detail that identifies a private repository,
  its owner, customers or infrastructure, or any person who uses the bundle, including by combining
  harmless-looking facts. `bundle.py privacy` enforces it, alongside hooks and CI.
- **English only**, whatever language the host repository uses.
- **No project nouns.** A repository is named only by a random id it minted for itself
  (`r-xxxxxx`), never next to a description of it; domains are named by mechanism, not product.
- **Records written by parallel sessions are not numbered**: they get an id from `bundle.py id`, so
  two sessions on different branches never mint the same one. Numbers are never reused or renumbered.

The complete list, with what enforces each rule, is in [`.agents/README.md`](.agents/README.md).
Contributions are covered in [CONTRIBUTING.md](CONTRIBUTING.md).
