#!/usr/bin/env python3
"""The question rules, on the question tool itself. Standard library only.

Principle 15 says what a question to the human owes: independent decisions grouped by theme, up to four
in one message; every option shown by a concrete case and priced in the repository's own units; and one
more answer, *review more*, on every decision question (`d-5ed7e8-0fec6e`, `d-5ed7e8-dd69e9`). The rule
was written, and the session that wrote it asked its next question without *review more* — which is why
it is enforced where the question is actually asked rather than stated again in prose.

    question_guard.py ask    PreToolUse on the question tool: refuse a question the rules forbid

**What it refuses** (exit 2, the reason fed back to the agent):
  - more than four questions in one message;
  - a decision question with no *review more* answer among its options.

**What it only warns about** (printed, the call proceeds): an option whose description carries no
concrete case and no price. Those are read by cue words, which is a guess; refusing on a guess would
block honest questions, so the ladder stops at a warning for them (`prompt-context.md` §*The
enforcement ladder*).

**It fails open on anything unexpected**: unknown input, no JSON, a shape it does not recognise. A hook
that cannot read the call must not be the reason the human is never asked.
"""

from __future__ import annotations

import json
import re
import sys

MAX_QUESTIONS = 4
# `review more` in the languages this owner's sessions actually use; a free-text option counts too.
REVIEW_MORE = re.compile(r"\b(review|revisar|ver)\s+m[aá]s\b|\breview more\b", re.I)
# A question that is not a decision is exempt by `d-5ed7e8-0fec6e`: a fact question, and the opening
# questions a run asks once before reading or writing.
EXEMPT = re.compile(r"\b(pre-?flight|pre-?vuelo|fact|hecho|confirm(a|e)?r?\b)", re.I)
CASE_CUE = re.compile(r"\b(ejemplo|example|e\.g\.|p\.\s?ej|por ejemplo|given|antes y despu[eé]s)\b", re.I)
PRICE_CUE = re.compile(r"\b(precio|price|cost[eo]?s?|min\b|minutos?|hours?|horas?|tokens?|ktok|"
                       r"\d+\s*(k|kb|ms|%)|\$|€)\b", re.I)


def questions_of(event: dict) -> list[dict]:
    payload = event.get("tool_input") or event.get("toolInput") or {}
    found = payload.get("questions")
    return [q for q in found if isinstance(q, dict)] if isinstance(found, list) else []


def problems(questions: list[dict]) -> tuple[list[str], list[str]]:
    refusals, warnings = [], []
    if len(questions) > MAX_QUESTIONS:
        refusals.append(f"{len(questions)} questions in one message; the cap is {MAX_QUESTIONS} "
                        "(principle 15). A larger batch is split, never squeezed.")
    for index, question in enumerate(questions, 1):
        text = str(question.get("question", ""))
        header = str(question.get("header", ""))
        options = [o for o in question.get("options", []) if isinstance(o, dict)]
        labels = " | ".join(str(o.get("label", "")) for o in options)
        where = f"question {index} ({header or text[:40]!r})"
        if not EXEMPT.search(text) and not EXEMPT.search(header) and not REVIEW_MORE.search(labels):
            refusals.append(f"{where}: no *review more* answer among its options. Every decision "
                            "question carries it; a fact question and a run's opening questions do not "
                            "(d-5ed7e8-0fec6e).")
        for option in options:
            description = str(option.get("description", ""))
            label = str(option.get("label", ""))
            if REVIEW_MORE.search(label):
                continue
            missing = [name for name, cue in (("a concrete case", CASE_CUE), ("a price", PRICE_CUE))
                       if not cue.search(description)]
            if missing:
                warnings.append(f"{where}, option {label[:30]!r}: {' and '.join(missing)} not found in its "
                                "description. Principle 15 asks for both, at the same fidelity for every option.")
    return refusals, warnings


def main() -> int:
    try:
        raw = sys.stdin.read()
    except (OSError, ValueError):
        return 0
    try:
        event = json.loads(raw) if raw.strip() else {}
    except ValueError:
        return 0
    if not isinstance(event, dict):
        return 0
    questions = questions_of(event)
    if not questions:
        return 0
    refusals, warnings = problems(questions)
    for warning in warnings:
        print(f"  ! {warning}")
    if refusals:
        for refusal in refusals:
            print(f"  x {refusal}", file=sys.stderr)
        print("Fix the question and ask again; nothing was shown to the human.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    # `sys.exit` raises SystemExit, which is a BaseException: catching that here swallowed the refusal
    # and let every malformed question through, so the guard is caught around `main()` alone and its own
    # exit code is raised afterwards, outside the net.
    try:
        code = main()
    except Exception:  # noqa: BLE001 -- failing open is the whole contract
        code = 0
    sys.exit(code)
