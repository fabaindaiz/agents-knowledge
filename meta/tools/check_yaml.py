#!/usr/bin/env python3
"""CI only: every frontmatter the bundle writes is YAML, and reads the same through PyYAML as through the tool.

The tools read a documented subset of YAML with the standard library. A subset reader that accepted
something PyYAML reads differently would let a carrier's own YAML tooling see another note than the
release built; so every frontmatter in `.agents/` and `sources/` is parsed by both and compared.

    pip install pyyaml && python3 meta/tools/check_yaml.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "meta/tools"))
import release as R  # noqa: E402

B = R.B


def main() -> int:
    problems, count = [], 0
    for folder in (ROOT / ".agents", ROOT / "sources"):
        for path in sorted(folder.rglob("*.md")):
            block, _ = B.split_frontmatter(path.read_text(encoding="utf-8"))
            if block is None:
                continue
            count += 1
            where = path.relative_to(ROOT).as_posix()
            try:
                ours = B.parse_frontmatter(block, where)
                theirs = yaml.safe_load(block) or {}
            except (B.FrontmatterError, yaml.YAMLError) as error:
                problems.append(f"{where}: {error}")
                continue
            if ours != theirs:
                keys = sorted(k for k in set(ours) | set(theirs) if ours.get(k) != theirs.get(k))
                problems.append(f"{where}: the tool and PyYAML read {', '.join(keys)} differently")
    for problem in problems:
        print("  x " + problem)
    print(f"{count} frontmatter blocks: " + ("the tool and PyYAML agree" if not problems else f"{len(problems)} disagree"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
