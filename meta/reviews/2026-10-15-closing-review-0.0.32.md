# The review that closes 0.0.32

**Scope, by the owner's decision (`d-5ed7e8-aef668`): the notes this intake touched and their
neighbours, one verdict per class for the rest, and the two cheapest experiments of the notes
touched.** `sources/README.md` §4 asks for verdicts, not a count, and forbids pruning what this
release itself admitted.

## Overlapping pairs, where this release touched both sides

| Pair | Verdict | The mechanism that separates them |
|---|---|---|
| `a-workaround-that-writes-the-subject-destroys-the-measurement` (new) · `a-request-accepted-is-not-an-effect` | **keep both**, with the shared incident counted once | the first is about the investigator's own writes erasing the evidence; the second about a system reporting an effect it did not have. A probe that writes is not a request that lies |
| the new note · `count-both-sides-and-use-a-control-window` | **keep both** | the control window is about **what to compare** a finding against; the new note about **what not to touch** before comparing. The 2026-10-15 occurrence of the control note (report the margin) and the new note's probe hygiene are **the same two incidents**, so each note now says which half it counts and the evidence is not counted twice |
| the new note · `a-check-must-be-seen-to-fail` | **keep both** | a planted violation is a write made **on purpose, to a subject nobody is diagnosing**; the trap here is a write made to get a reading. The planted-fault boundary this release adds to the latter (place the plant where the property is observable) is the mirror image and is cited in neither |
| `refusal-must-not-read-like-an-answer` · `a-default-scope-is-the-widest-one` | **keep both**, as before: this release's occurrence of the first (a pipeline's exit status lost to a filter) and of the second (an empty selection read as "everything") both end in a green check over nothing, but one is a status discarded and the other a scope widened |
| `ratchet-in-a-pinned-environment` · `reproduce-the-checkout-not-only-the-environment` | **keep both**; the 2026-10-15 occurrences sharpen the line: the ratchet note now says the baseline must be findings rather than a total, the checkout note that a pin is resolved from where the command ran. One is about the number, the other about the tree |
| `test-double-fidelity`'s two new occurrences | **merged into one note**, not split: the command-line double that accepts a negative number, and the two doubles sharing a name, are both "the double accepts more than the real thing, and nobody checked which double this is" |

## One verdict per class, for the notes this intake did not touch

- **Notes in review:** none. The only one left review this release (`a-rewrite-cleans-only-what-refs-reach`),
  and the verdict is named precisely here: the §3 verdict it took is **the claim's check revised**, not a new bullet under *When it does NOT apply*, which is what "the boundary moves" means in the method. Nothing was sent to review.
- **Notes whose *Evidence* names an experiment never run:** **queued**, unchanged, except the two run
  below. 64 were queued at the start of this release, 28 had ever run, and **none had run since the
  previous release** — that zero is what the owner's decision set out to break.
- **Notes whose `confidence` their *Evidence* does not earn:** none found among the nineteen touched (seventeen folded, one returned from review, one new);
  the new note is written as `reasoned`, which its two unquantified incidents earn, and no note gained
  `measured` this release.
- **Notes an occurrence contradicted:** two, and both were acted on rather than absorbed. `a-request-accepted-is-not-an-effect`'s own check would have passed the occurrence folded into it — the state was read back, agreed, and the effect was wrong — so its check now asks for the effect itself. And — the shallow-clone
  incident satisfied `a-rewrite-cleans-only-what-refs-reach`'s own check while losing a fifth of a
  branch's commits, so the check gained the commit-count comparison and the note returned to active.
- **Pairs not touched by this release:** not reviewed, and that is a gap this release does not close.
  The full pairwise pass over the 52 notes has never been done; it stays in the roadmap.

## The two experiments

Both are recorded in full in `meta/tracking/experiments.md` (2026-10-15):

1. **`a-default-scope-is-the-widest-one`** — five of five commands that take a set of target
   repositories default to the widest scope for reading (the machine's manifest, 11 repositories
   here); the writing path refuses a scope it was not given, by a dedicated error. **Confirms**, and
   names where the next occurrence will come from: the read side still widens in silence.
2. **`a-check-must-be-seen-to-fail`** — the new undefined-citation warning was read before it was
   trusted, and it was green while blind: 95 findings, none of them real, because a roadmap item
   written as a bullet was not recognised as a definition. Teaching the check that shape moved
   definitions from 155 to 225 and the warning to zero. **Confirms**, and adds a second occurrence to
   the boundary a 2026-10-01 run named — compare what a check examined against the subjects known to
   exist. The same check had its heading shape fixed in 0.0.27; this was the other half.

## What this review did not do

The pairwise pass over every note; a verdict on the 110 queued candidates beyond the ones this intake
moved; and any downgrade of a `confidence` — none was found wanting, which is a weaker statement than
having checked all 52.
