# Decision review of the rulings taken while running the 0.0.31 tool plan (2026-10-09)

**State: closed on 2026-10-09.** The owner walked the four, one per turn, and confirmed the
summary; every row is in `meta/decisions.md`: R3 `d-5ed7e8-3ec5f0`, R5 `d-5ed7e8-d5e034`, R13 `d-5ed7e8-505656`, R10
`d-5ed7e8-f83ee5`, and the agent's twelve as `agent s-5ed7e8-4632df`, from `d-5ed7e8-51d905` to `d-5ed7e8-abd06e`.
Every recommendation was taken. R5's reason is the owner's: going over the limit without raising it, and reducing
the content to fit in later stages. Applied at once: R3's fallback in `AGENTS.md`, R13's scope in `prompt-sync.md`.

**Context.** The plan `meta/reviews/2026-10-08-plan-0.0.31-tools.md` ran subagent-driven on 2026-10-09 and landed on
`main` (`8161e4b..13a5d57`). The controller took fourteen rulings on the owner's behalf (its ledger was a working
artifact and is gone; the rulings are copied here whole) and two decisions it did not log as rulings. A review walked
after a plan has run tends to change its rulings, so each option below is *keep* or *change*, priced as the change.

## The owner's decisions (walk one per turn, in this order)

1. **R3 — how a plan lands when the host's permission classifier refuses the per-task push.** D7
   (`d-5ed7e8-905aa8`) planned one branch per task, each fast-forwarded to `main` after its gate and review. The host
   refused the first fast-forward and push; the controller then based each task's branch on the previous one (a linear
   chain) and `main` was fast-forwarded once, with the owner's word, at the end (17 commits). Options: keep the chain
   and one fast-forward at the end as the practice; add a permission rule so the per-task push runs as D7 says; one
   branch for the whole plan. Cost if it stays: a task a later review wants out means rebasing the chain.
2. **R5 — how the owner's rule on the export cap was codified.** The owner: "raise now and reduce at the release; that
   should always be the method". Codified as `d-5ed7e8-a3e7e8`: the cap's value stays 913,167 bytes; `release.py
   check` warns while the export is over it and `release.py release` refuses the cut. The literal alternative: raise
   the constant now by what a plan adds, and lower it at the cut. Today the export is about 920 KB.
3. **R13 — which worktrees the *Worktrees* rule governs.** `meta/method/prompt-sync.md` *Worktrees*: "they sit side by
   side in one folder, each named after its repository and branch (a path inside a repository is never a worktree's
   home)". Its first sentence mixes two scopes ("the worktrees a meta-session opens in carriers for their updates, and
   a change to the tools or the method is made in one too"), and this plan's own worktrees lived under
   `.claude/worktrees/` inside the home, the host's default. Options: the rule covers carriers' update worktrees only
   (fix the first sentence); it covers every worktree, the home's plans included (move them outside the repository);
   it covers carriers' worktrees and says the host's in-repository default is accepted for the home.
4. **R10 — where the branch rule the owner sets for an update is written.** Today: in the changelog entry Phase 2
   step 6 writes in each carrier, in that carrier's format. Alternatives: in the bundle's `CHANGELOG.md` for the
   release; in both.

## Decided by the agent (shown to the owner with examples; the owner may move any of them up)

- **R1** — Task 3's trial intake ran against a scratch copy of the home, never `meta/tracking/` (an intake there is a
  release step). Moot: it could not run, because the three held proposals are on no carrier on this machine.
- **R2** — the plan's line numbers were hints; implementers located code by name.
- **R4** — `align` names a carrier whose `carrier.toml` holds no id (`<name>: no carrier id in carrier.toml`) and
  checks the rest, as D5 says for a missing bundle.
- **R6/R7** — `export --replace` keeps the legacy `tracking/` outbox: what a replace keeps is `is_carrier_owned` plus
  `proposals/` and `incoming/`. First ruled the other way (refuse), superseded when review showed the update converts
  the outbox only after the replace.
- **R8** — `declined_skills(tree)` rather than the plan's `(repo)`: `carrier.toml` lives in the bundle's tree.
- **R9** — "the main checkout's environment" is what it has installed and configured, never a fresh install; an
  editable install bound to the main checkout's code makes the result unproven (`prompt-bootstrap.md` §*4. Verify*).
- **R11** — the update's question 5 names the session log, which `carrier.toml`'s `log` points at (a reviewer had
  suggested the decisions log).
- **R12** — the whole-branch review ran before Task 10, so the records carried its outcome.
- **R14** — the residual Important after the final fix wave went to the owner, who approved one more round.
- **A (candidate to move up: it changes a note's text)** — the product-noun check (D8) failed the build on a second
  note, so its cues were rewritten too: `order-writes-by-failure-residue` `"sqs"` → `"message visibility timeout"`,
  `"kafka offset"` → `"consumer offset commit"`; and, as planned, `nested-partial-update-replaces` `"$set"` →
  `"field-set operator"`, `"firestore update"` → `"nested field partial update"`.
- **B** — `meta/product-nouns.txt` seeds 22 public products across stores, clouds, queues and frameworks; short ones
  (`spring`, `react`, `oracle`) may catch a future prose cue, and the build then fails visibly.
- **C** — `export --replace` leaves caches and a real `.DS_Store` where they are (ignored as `verify` ignores them),
  rather than deleting what no release lists.

## To record when the walk ends

Each row in `meta/decisions.md`: the owner's as `accepted <date> · h1` with the reason given, the agent's as
`· agent s-…` with `unconfirmed:` where no reason was given; a change the owner picks becomes a roadmap item for the
code or text it touches.
