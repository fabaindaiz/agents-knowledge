# The home's own skills

Procedures **only this repository runs**. They are not part of the bundle: no carrier cuts a release,
so a `cut` skill would cost every carrier bytes it can never use. They live here, outside `sources/`,
and never reach `.agents/`.

**Install, and keep current:**

```sh
python3 meta/tools/release.py install-home-skills            # every base here, into .claude/skills/<name>/SKILL.md
python3 meta/tools/release.py install-home-skills --check    # fails when one is missing, stale or hand-edited
```

`release.py check` runs the check, so an edit to a base fails the gate until the skill is installed again.

The installed file is generated: edit `<name>/SKILL.md` here, or the `LOCAL.md` beside the installed one,
and install again. Its banner names its base and ends with the hash of what was written, so an edit made
under the banner is caught rather than silently overwritten.

**It is a different folder from `.claude/skills/` to the bundle's tools.** `bundle.py install-skills` reads
only the release's bases and never writes here; its `installed_skill_problems` skips a skill that does not
carry the bundle's banner, which is why this one carries a banner of its own. Neither tool touches the
other's files, and a name may not be in both.

| Skill | When |
|---|---|
| `cut` | a release of the bundle is to be cut and tagged here; the full order is [`../prompt-sync.md`](../prompt-sync.md) |
