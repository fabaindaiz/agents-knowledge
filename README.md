# agents-knowledge

**A portable `.agents/` bundle for AI coding assistants: a working method and a knowledge base
of engineering judgement, versioned so it can be copied between repositories and kept in sync.**

Agents are well read. Ask one about retries, defaults, test doubles or deploy ordering and it
gives you the textbook answer, and usually the textbook is right. The expensive cases are the
ones where it is wrong, and nothing in the agent's training tells it which case it is in. This
repository collects that missing part: **which heuristic to use, when to use it, and where it
stops working**, together with a method for keeping that knowledge alive across several
repositories.

The bundle is called `agent-guides`. This repository is its root: the copy with no upstream,
where releases are cut and then offered to other repositories.

## What is in the bundle

Everything lives in [`.agents/`](.agents/). That folder is the unit: copy it and you have taken
everything.

| Path | What it holds |
|---|---|
| [`.agents/README.md`](.agents/README.md) | The bundle's header (lineage, version, digest) and its conventions. Start here |
| [`.agents/method/`](.agents/method/) | Paste-ready prompts that tell an agent how to evaluate, bootstrap, update, merge, harvest and sync. `prompt-context.md` is the reference they share |
| [`.agents/knowledge/`](.agents/knowledge/) | Short notes, one heuristic each, with the case where it does not apply, what it costs, and how well it is backed by evidence. They sit in `notes/active/`, `notes/review/` or `notes/retired/`: the folder is the note's state. [`INDEX.md`](.agents/knowledge/INDEX.md) is the way in |
| [`.agents/layout.md`](.agents/layout.md) | Where agent-facing files belong (`AGENTS.md`, `.agents/`, `docs/`, `CLAUDE.md`), and which parts of that are an actual standard |
| [`.agents/references.md`](.agents/references.md) | The sources behind the method's rules on writing documents, each linked, checked, and tied to the rule it supports |
| [`.agents/roadmap.md`](.agents/roadmap.md) | Planned work on the bundle itself |
| [`.agents/tracking/`](.agents/tracking/) | Candidate notes, queued experiments, retired notes, and the repositories that carry the bundle |
| [`.agents/tools/bundle.py`](.agents/tools/bundle.py) | A single-file, standard-library tool: digests and checks, record ids, moving a note between states, a size report, and reconciling several copies |
| [`.agents/incoming/`](.agents/incoming/) | Where another repository's copy lands before it is triaged. Empty between updates |

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

The notes cover failure behaviour, verification, data correctness, evolving contracts,
measurement, distributed correctness, adversarial controls, identity and naming, and time and
control. Every note has a `confidence` field, so an agent can tell what was paid for from what
was only believed:

| `confidence` | Means |
|---|---|
| `measured` | A number was produced in a repository, and it is written in the note |
| `reasoned` | It follows from a mechanism, but has not been tested in a repository |
| `inherited` | It was learned elsewhere and has not been verified |

A note stays only while the evidence supports it. When evidence disputes it, it moves to
`notes/review/` and stays usable, marked, until it gets a verdict: its boundary moves, its claim
is revised, or it moves to `notes/retired/` and is logged in
[`tracking/retired.md`](.agents/tracking/retired.md). The full lifecycle is in
[`knowledge/README.md`](.agents/knowledge/README.md).

## Using it in your repository

1. **Copy the folder.** Put this repository's `.agents/` into your repository's
   `.agents/incoming/`.
2. **Run the right prompt.** Which one depends on your repository's headers, not on dates:

   | Your repository | Run |
   |---|---|
   | Has no `.agents/` bundle yet | [`method/prompt-bootstrap.md`](.agents/method/prompt-bootstrap.md) |
   | Carries an older version on the same line | [`method/prompt-update.md`](.agents/method/prompt-update.md) |
   | Carries a version that diverged from this one | [`method/prompt-merge.md`](.agents/method/prompt-merge.md) |
   | Is one of several repositories you want to bring into line together | [`method/prompt-sync.md`](.agents/method/prompt-sync.md) |

   Each prompt file begins with a *Paste this to start* block. Open your agent at the root of
   the target repository and paste that block in.
3. **Point your assistant at it.** Nothing in `.agents/` loads by itself. The root `AGENTS.md`
   has to name it, and for Claude Code the root `CLAUDE.md` needs to import `AGENTS.md`. The
   [layout guide](.agents/layout.md) explains why and shows the Cursor and Copilot equivalents.

Want to judge your current setup before adopting anything?
[`method/prompt-evaluate.md`](.agents/method/prompt-evaluate.md) reviews a repository's existing
AI instructions and writes a report without changing anything.

**A bundle is offered, never pushed.** Your repository decides what to take, and the header
fields `adopted`, `adapted` and `declined` record what it changed and what it refused, and
`upstream` says where it pulls from. Those fields belong to your repository and never come from
upstream.

## Verifying a copy

Every copy declares a `digest` of its content in the header of `.agents/README.md`. Before
trusting a copy's version, check that the digest matches:

```bash
python3 .agents/tools/bundle.py digest .agents --check
```

The tool needs **Python 3.9 or newer** and nothing outside the standard library. It includes
its own tests:

```bash
python3 .agents/tools/bundle.py selftest
```

To see how much the bundle weighs, per folder and per type of session (coding, consulting,
bootstrapping, syncing and so on), in files, bytes and estimated tokens:

```bash
python3 .agents/tools/bundle.py report
```

## Measuring whether it helps

[`evals/`](evals/) holds a pre-registered experiment on whether carrying the bundle changes what an
agent does, and whether its content is the cause: hidden-test graders, and arms that separate the
notes' content from context length and from routing. It lives outside `.agents/` and never travels.
Five exploratory pilots are reported in [`evals/REPORT.md`](evals/REPORT.md): the bundle costs about
twice as much per task for a frontier model, and a content effect shows only where the decisive fact
is out of sight, on few tasks and without significance. The confirmatory run is roadmap item
`i-5ed7e8-0d9b6a`.

Those tasks were written from the notes, so they measure whether a note's content reaches a decision,
not whether the agent works better in general. That second question has its own protocol,
[`evals/PROTOCOL-general.md`](evals/PROTOCOL-general.md) (roadmap item `i-5ed7e8-bf5663`), with tasks from
external benchmarks: real issues opened after the models' training cutoffs, competitive programming,
code reasoning, optimisation and design judged by what it costs to change later. It is a reviewed
draft; nothing of it has run.

## Keeping several repositories in sync

This repository is where the bundle is maintained. A *meta-session*
([`method/prompt-sync.md`](.agents/method/prompt-sync.md)) runs from here over every carrier open
on the machine. It collects what each one learned, builds one release, writes that release into
each carrier and checks that they all end up identical. The bundle moves between machines through
this repository's remote. Each machine lists its own carrier paths in
`~/.config/agent-guides/carriers.toml`, which is never committed. [AGENTS.md](AGENTS.md) describes
the procedure.

## Conventions

Anything inside `.agents/` must follow these rules, because it gets copied into other
repositories and other organisations:

- **Nothing private, direct or reconstructible.** No detail that identifies a private repository,
  its owner, customers or infrastructure, or any person who uses the bundle, including by combining
  harmless-looking facts. `bundle.py privacy` enforces it, alongside hooks and CI.
- **English only**, whatever language the host repository uses.
- **No project nouns.** A repository is named only by a random id it minted for itself
  (`r-xxxxxx`, never derived from its name), never next to a description of it; domains are named
  by mechanism rather than by product.
- **Every file carries provenance**: a frontmatter header, or a comment block for the tool.
- **Records written by parallel sessions are not numbered.** A decision, a roadmap item or a
  session entry gets `d-`, `i-` or `s-` plus the repository's random id and a hash of its content
  (`bundle.py id`), so two sessions on different branches never mint the same id. Numbers
  remain only for what a release writes, and are never reused or renumbered.

The complete list, with what enforces each rule, is in [`.agents/README.md`](.agents/README.md).
Contributions are covered in [CONTRIBUTING.md](CONTRIBUTING.md).
