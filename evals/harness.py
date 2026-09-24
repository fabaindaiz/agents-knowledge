#!/usr/bin/env python3
"""Runner for the bundle-efficacy experiment. Standard library only. The protocol is PROTOCOL.md.

Every trial is one headless Claude Code session on a fresh copy of one task's repository, prepared
for one condition, graded afterwards by hidden tests the agent never saw.

    python3 evals/harness.py check [--tasks ID...]
        validate the tasks: the hidden tests fail on the starting state and on the naive overlay,
        pass on the reference overlay, and the visible tests pass on all three
    python3 evals/harness.py plan RUN --model M [--tasks ID...] [--conditions C...] [--reps K] [--seed S]
        freeze a randomised, interleaved schedule and every setting into RUN/plan.json
    python3 evals/harness.py probe RUN
        manipulation check: one tool-less session per condition reports which instructions it loaded
    python3 evals/harness.py run RUN [--limit N] [--dry-run]
        execute the pending trials of the plan in order, appending to RUN/results.jsonl (resumable)
    python3 evals/harness.py status RUN

Isolation, per trial: the workspace lives outside any repository and any CLAUDE.md; the Claude
configuration directory is a clean one given by --config-dir (never ~/.claude); the environment is
rebuilt from an allowlist; Bash runs in Claude Code's sandbox with no network and no read of the home
directory; the Read and Edit tools are allowed only inside the workspace.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TASKS = HERE / "tasks"
BUNDLE = ROOT / ".agents"
HIDDEN_DIR = "_hidden_eval_tests"

# The conditions, and which task families run them. See PROTOCOL.md, "Conditions".
CONDITIONS = ["none", "minimal", "bundle", "ablated", "oracle", "oracle_placebo"]
FAMILY_CONDITIONS = {
    "judgment": CONDITIONS,
    "boundary": CONDITIONS,
    "neutral": ["none", "minimal", "bundle"],
}

ROUTING = """
## Engineering knowledge

`.agents/knowledge/INDEX.md` indexes short notes on where the textbook answer to a design question
is wrong. Before a design decision, and before claiming the work is done, look up what you are about
to do in the index and read only the notes it points to.
"""

ORACLE_HEADER = """
## Engineering note

The note below applies to this repository.

"""

TOOLS = ["Bash", "Read", "Edit", "Write", "Glob", "Grep"]


# ---------------------------------------------------------------- tasks

def load_task(task_id: str) -> dict:
    d = TASKS / task_id
    meta = json.loads((d / "task.json").read_text())
    meta["dir"] = str(d)
    meta["prompt"] = (d / "prompt.md").read_text().strip()
    meta["agents_minimal"] = (d / "AGENTS.minimal.md").read_text()
    assert meta["id"] == task_id, f"{task_id}: id mismatch"
    assert meta["family"] in FAMILY_CONDITIONS, f"{task_id}: unknown family"
    if meta["family"] != "neutral" and meta.get("placebo_note", "auto") == "auto":
        meta["placebo_note"] = pick_placebo(meta["notes"])
    for slug in meta.get("notes", []) + [meta.get("placebo_note")] * bool(meta.get("placebo_note")):
        assert note_path(slug).exists(), f"{task_id}: note {slug} not in the bundle"
    return meta


def topic_areas() -> dict:
    """topic -> area, read from the routing table in INDEX.md."""
    areas = {}
    for line in (BUNDLE / "knowledge" / "INDEX.md").read_text().splitlines():
        m = re.search(r"\(areas/(\w+)\.md\)", line)
        if m:
            for topic in re.findall(r"`([\w-]+)`", line):
                areas[topic] = m.group(1)
    return areas


def pick_placebo(targets: list) -> str:
    """The pre-registered rule: the active note from another area whose text length is closest to the
    targets' combined length. Mechanical, so the experimenter does not choose it."""
    areas = topic_areas()
    def topic(slug):
        return re.search(r"^topic:\s*(\S+)", note_path(slug).read_text(), re.M).group(1)
    target_areas = {areas[topic(t)] for t in targets}
    length = sum(len(note_text(t)) for t in targets)
    cands = []
    for p in sorted((BUNDLE / "knowledge" / "notes" / "active").glob("*.md")):
        if p.stem in targets or areas.get(topic(p.stem)) in target_areas:
            continue
        cands.append((abs(len(note_text(p.stem)) - length), p.stem))
    return min(cands)[1]


def all_task_ids() -> list[str]:
    return sorted(p.parent.name for p in TASKS.glob("*/task.json"))


def tree_hash(path: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(path.rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts:
            h.update(str(p.relative_to(path)).encode() + b"\0" + p.read_bytes() + b"\0")
    return h.hexdigest()[:16]


def note_path(slug: str) -> Path:
    for state in ("active", "review"):
        p = BUNDLE / "knowledge" / "notes" / state / f"{slug}.md"
        if p.exists():
            return p
    return BUNDLE / "knowledge" / "notes" / "active" / f"{slug}.md"


def note_text(slug: str) -> str:
    text = note_path(slug).read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    claim = ""
    if m:
        cm = re.search(r"^claim:\s*(.+)$", m.group(1), re.M)
        claim = cm.group(1).strip() if cm else ""
        text = text[m.end():]
    return (f"**Claim:** {claim}\n" if claim else "") + text.strip() + "\n"


# ---------------------------------------------------------------- conditions

def copy_bundle(dst: Path) -> None:
    def ignore(d, names):
        skip = {"__pycache__"}
        if Path(d).name == "incoming":
            skip |= {n for n in names if n != "README.md"}
        return skip & set(names) | {n for n in names if n.startswith("evaluation-")}
    shutil.copytree(BUNDLE, dst / ".agents", ignore=ignore)


def ablate(agents: Path, slugs: list[str]) -> dict:
    """Remove the target notes, and every line of the bundle that names one of them."""
    removed_lines = 0
    for slug in slugs:
        for state in ("active", "review", "retired"):
            p = agents / "knowledge" / "notes" / state / f"{slug}.md"
            if p.exists():
                p.unlink()
    pat = re.compile("|".join(re.escape(s) for s in slugs))
    for p in agents.rglob("*"):
        if not p.is_file() or p.suffix not in (".md", ".py"):
            continue
        lines = p.read_text().splitlines(keepends=True)
        kept = []
        for line in lines:
            if pat.search(line):
                # In a " · "-separated list of note links, drop only the link; otherwise the line.
                if " · " in line and line.lstrip().startswith("|"):
                    cells = line.split("|")
                    new_cells = []
                    for c in cells:
                        if pat.search(c) and " · " in c:
                            parts = [x for x in c.split(" · ") if not pat.search(x)]
                            c = " · ".join(parts)
                            if not c.startswith(" "):
                                c = " " + c
                        new_cells.append(c)
                    line = "|".join(new_cells)
                    if not pat.search(line):
                        kept.append(line)
                        removed_lines += 1
                        continue
                removed_lines += 1
                continue
            kept.append(line)
        if len(kept) != len(lines) or kept != lines:
            p.write_text("".join(kept))
    return {"lines_touched": removed_lines}


def prepare(task: dict, condition: str, ws: Path) -> dict:
    """Build the workspace for one trial. Returns what was installed, for the record."""
    shutil.copytree(Path(task["dir"]) / "repo", ws, ignore=shutil.ignore_patterns("__pycache__"))
    info: dict = {"condition": condition}
    agents_md = None
    if condition == "minimal":
        agents_md = task["agents_minimal"]
    elif condition in ("bundle", "ablated"):
        agents_md = task["agents_minimal"].rstrip() + "\n" + ROUTING
        copy_bundle(ws)
        if condition == "ablated":
            info["ablation"] = ablate(ws / ".agents", task["notes"])
    elif condition == "oracle":
        agents_md = task["agents_minimal"].rstrip() + "\n" + ORACLE_HEADER
        agents_md += "\n".join(note_text(s) for s in task["notes"])
    elif condition == "oracle_placebo":
        agents_md = task["agents_minimal"].rstrip() + "\n" + ORACLE_HEADER + note_text(task["placebo_note"])
    if agents_md is not None:
        (ws / "AGENTS.md").write_text(agents_md)
        # Claude Code reads AGENTS.md through CLAUDE.md, the documented bridge (see .agents/layout.md).
        (ws / "CLAUDE.md").write_text("@AGENTS.md\n")
        info["agents_md_chars"] = len(agents_md)
    if (ws / ".agents").exists():
        info["bundle_chars"] = sum(p.stat().st_size for p in (ws / ".agents").rglob("*") if p.is_file())
    git(ws, "init", "-q")
    git(ws, "add", "-A")
    git(ws, "commit", "-q", "-m", "start")
    return info


def git(ws: Path, *args: str) -> str:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(ws),
           "GIT_CONFIG_NOSYSTEM": "1", "GIT_AUTHOR_NAME": "eval", "GIT_AUTHOR_EMAIL": "eval@localhost",
           "GIT_COMMITTER_NAME": "eval", "GIT_COMMITTER_EMAIL": "eval@localhost"}
    r = subprocess.run(["git", "-c", "init.defaultBranch=main", *args], cwd=ws, env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


# ---------------------------------------------------------------- grading

def run_tests(ws: Path, cmd: list[str], timeout: int = 300) -> dict:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(ws), "PYTHONDONTWRITEBYTECODE": "1",
           "LANG": "C.UTF-8"}
    try:
        r = subprocess.run(cmd, cwd=ws, env=env, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"passed": False, "timeout": True, "ran": None, "failures": None, "errors": None, "tail": ""}
    out = r.stdout + r.stderr
    ran = re.search(r"Ran (\d+) tests?", out)
    fails = re.search(r"failures=(\d+)", out)
    errs = re.search(r"errors=(\d+)", out)
    return {"passed": r.returncode == 0 and bool(ran) and int(ran.group(1)) > 0, "timeout": False,
            "ran": int(ran.group(1)) if ran else 0,
            "failures": int(fails.group(1)) if fails else 0, "errors": int(errs.group(1)) if errs else 0,
            "tail": out[-1500:]}


def grade(task: dict, ws: Path) -> dict:
    visible = run_tests(ws, task["visible_test_cmd"])
    hdst = ws / HIDDEN_DIR
    if hdst.exists():
        shutil.rmtree(hdst)
    shutil.copytree(Path(task["dir"]) / "hidden", hdst)
    hidden = run_tests(ws, task["hidden_test_cmd"])
    shutil.rmtree(hdst)
    return {"hidden": hidden, "visible": visible}


def overlay(src: Path, ws: Path) -> None:
    for p in src.rglob("*"):
        if p.is_file() and "__pycache__" not in p.parts:
            dst = ws / p.relative_to(src)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)


def cmd_check(args) -> int:
    ok = True
    for tid in args.tasks or all_task_ids():
        task = load_task(tid)
        rows = []
        for state in ("start", "naive", "reference"):
            with tempfile.TemporaryDirectory() as tmp:
                ws = Path(tmp) / "ws"
                shutil.copytree(Path(task["dir"]) / "repo", ws)
                if state != "start":
                    overlay(Path(task["dir"]) / state, ws)
                g = grade(task, ws)
                rows.append((state, g["visible"]["passed"], g["hidden"]["passed"], g))
        # The naive overlay's visible result is informational: a wrong design may break existing tests.
        want = {"start": (True, False), "naive": (None, False), "reference": (True, True)}
        for state, vis, hid, g in rows:
            wv, wh = want[state]
            good = hid == wh and (wv is None or vis == wv)
            # A grader that "fails" because the code does not import has not been seen to fail.
            if state == "naive" and re.search(r"(ImportError|SyntaxError|IndentationError|ModuleNotFoundError|"
                                              r"NameError|failed to import)", g["hidden"]["tail"]):
                good = False
            ok &= good
            mark = "ok  " if good else "FAIL"
            print(f"{mark} {tid:40s} {state:9s} visible={'pass' if vis else 'fail'} hidden={'pass' if hid else 'fail'}")
            if not good:
                print("     hidden tail:", g["hidden"]["tail"][-400:].replace("\n", "\n     "))
                print("     visible tail:", g["visible"]["tail"][-400:].replace("\n", "\n     "))
    print("all tasks valid" if ok else "SOME TASKS ARE INVALID")
    return 0 if ok else 1


# ---------------------------------------------------------------- the agent

def claude_bin(explicit: str | None) -> str:
    if explicit:
        return explicit
    found = shutil.which("claude")
    if found:
        return found
    cands = sorted(Path.home().glob(".vscode/extensions/anthropic.claude-code-*/resources/native-binary/claude"))
    if cands:
        return str(cands[-1])
    raise SystemExit("no claude binary: pass --claude PATH")


DEFAULT_CONFIG = "default"


def check_config_dir(cfg) -> list[str]:
    """A clean configuration directory holds credentials and nothing that shapes behaviour.
    `default` reuses the logged-in ~/.claude with user settings excluded: degraded isolation, because the
    user's CLAUDE.md then loads in every arm. Allowed for exploratory runs only (PROTOCOL.md, Deviations)."""
    if str(cfg) == DEFAULT_CONFIG:
        return []
    cfg = Path(cfg)
    problems = []
    if not cfg.is_dir():
        return [f"{cfg} does not exist"]
    if cfg.resolve() == (Path.home() / ".claude").resolve():
        problems.append("the config dir is ~/.claude: use a dedicated clean one")
    for name in ("CLAUDE.md", "CLAUDE.local.md", "rules", "skills", "agents", "commands", "plugins",
                 "output-styles", "hooks"):
        if (cfg / name).exists():
            problems.append(f"{cfg / name} exists and would shape every condition")
    s = cfg / "settings.json"
    if s.exists():
        try:
            data = json.loads(s.read_text() or "{}")
        except json.JSONDecodeError:
            data = {"unparseable": True}
        extra = set(data) - {"$schema"}
        if extra:
            problems.append(f"{s} sets {sorted(extra)}")
    return problems


def ancestors_clean(path: Path) -> list[str]:
    bad = []
    for a in [path, *path.parents]:
        for name in ("CLAUDE.md", "AGENTS.md", "CLAUDE.local.md", ".git", ".claude"):
            if (a / name).exists():
                bad.append(str(a / name))
    return bad


def trial_settings(ws: Path) -> dict:
    w = str(ws)
    return {
        "sandbox": {
            "enabled": True,
            "failIfUnavailable": True,
            "allowUnsandboxedCommands": False,
            "autoAllowBashIfSandboxed": True,
            "filesystem": {"denyRead": ["~/"]},
            "network": {"allowedDomains": [], "strictAllowlist": True},
        },
        "permissions": {
            "allow": [f"Read(/{w}/**)", f"Edit(/{w}/**)", "Glob", "Grep"],
            "deny": ["Read(~/**)", "Edit(~/**)", "WebFetch", "WebSearch"],
        },
    }


def clean_env(cfg) -> dict:
    env = {k: os.environ[k] for k in ("PATH", "HOME", "LANG", "TERM", "USER", "LOGNAME") if k in os.environ}
    if str(cfg) != DEFAULT_CONFIG:
        env["CLAUDE_CONFIG_DIR"] = str(cfg)
    env.update({
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
        "DISABLE_TELEMETRY": "1",
        "DISABLE_AUTOUPDATER": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
    })
    for key in ("ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN"):
        if os.environ.get(key):
            env[key] = os.environ[key]
    return env


def invoke(plan: dict, ws: Path, prompt: str, settings_path: Path, transcript: Path,
           max_turns: int, timeout: int, tools: list[str] | None = None) -> dict:
    cmd = [plan["claude"], "-p", prompt,
           "--output-format", "stream-json", "--verbose",
           "--model", plan["model"],
           "--max-turns", str(max_turns),
           # acceptEdits, not dontAsk: dontAsk refused sandboxed Bash commands that write files, more often in
           # some arms than others (pilots 1 and 2; REPORT.md). The sandbox is the boundary either way.
           "--permission-mode", "acceptEdits",
           "--settings", str(settings_path),
           "--strict-mcp-config",
           "--disable-slash-commands",
           "--no-session-persistence",
           "--tools", *(TOOLS if tools is None else (tools or [""]))]
    if plan.get("effort"):
        cmd += ["--effort", plan["effort"]]
    if plan["config_dir"] == DEFAULT_CONFIG:
        cmd += ["--setting-sources", "project,local"]
    t0 = time.time()
    timed_out = False
    with open(transcript, "w") as out:
        try:
            p = subprocess.run(cmd, cwd=ws, env=clean_env(plan["config_dir"]), stdout=out,
                               stderr=subprocess.PIPE, text=True, timeout=timeout)
            rc, stderr = p.returncode, p.stderr
        except subprocess.TimeoutExpired as e:
            rc, stderr, timed_out = None, (e.stderr or b"").decode() if isinstance(e.stderr, bytes) else (e.stderr or ""), True
    return {"rc": rc, "timed_out": timed_out, "wall_s": round(time.time() - t0, 1), "stderr": stderr[-2000:]}


def parse_transcript(path: Path, ws: Path) -> dict:
    """The result event (cost, tokens, turns) and every file the agent read or searched."""
    res: dict = {"result": None, "init": None, "reads": [], "outside": [], "tool_calls": 0, "bash": 0, "denials": 0}
    wsr = str(ws.resolve())
    for line in path.read_text(errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "system" and ev.get("subtype") == "init":
            res["init"] = {k: ev.get(k) for k in ("model", "claude_code_version", "tools", "mcp_servers",
                                                   "cwd", "permissionMode", "plugins", "memory_paths")}
        elif ev.get("type") == "result":
            res["result"] = {k: ev.get(k) for k in ("subtype", "is_error", "num_turns", "duration_ms",
                                                     "total_cost_usd", "usage", "modelUsage")}
        elif ev.get("type") == "user":
            for c in (ev.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    t = c.get("content")
                    t = t if isinstance(t, str) else json.dumps(t)
                    if "has been denied" in t or "denied by your permission settings" in t:
                        res["denials"] += 1
        elif ev.get("type") == "assistant":
            for c in (ev.get("message") or {}).get("content") or []:
                if c.get("type") != "tool_use":
                    continue
                res["tool_calls"] += 1
                inp = c.get("input") or {}
                if c.get("name") == "Bash":
                    res["bash"] += 1
                    cmdline = inp.get("command", "")
                    for m in re.finditer(r"\.agents/[\w./-]+", cmdline):
                        res["reads"].append(m.group(0))
                    if re.search(r"(~|/home/)", cmdline):
                        res["outside"].append(cmdline[:200])
                for key in ("file_path", "path"):
                    fp = inp.get(key)
                    if not fp:
                        continue
                    full = str((ws / fp).resolve()) if not os.path.isabs(fp) else os.path.normpath(fp)
                    if not full.startswith(wsr):
                        res["outside"].append(full)
                    else:
                        res["reads"].append(os.path.relpath(full, wsr))
                if c.get("name") == "Grep" and inp.get("pattern"):
                    res["reads"].append(f"grep:{inp.get('pattern')}")
    return res


# ---------------------------------------------------------------- plan / run

def workspace_base(arg: str | None) -> Path:
    base = Path(arg) if arg else Path(tempfile.gettempdir()) / "agent-guides-eval"
    base.mkdir(parents=True, exist_ok=True)
    bad = ancestors_clean(base)
    if bad:
        raise SystemExit(f"workspace base {base} sits under instruction files or a repository: {bad}")
    return base


def cmd_plan(args) -> int:
    run = Path(args.run)
    if (run / "plan.json").exists():
        raise SystemExit(f"{run}/plan.json exists: a plan is frozen once written")
    tasks = [load_task(t) for t in (args.tasks or all_task_ids())]
    cfg = args.config_dir if args.config_dir == DEFAULT_CONFIG else Path(args.config_dir).expanduser()
    problems = check_config_dir(cfg)
    if problems:
        raise SystemExit("config dir is not clean:\n  " + "\n  ".join(problems))
    claude = claude_bin(args.claude)
    version = subprocess.run([claude, "--version"], capture_output=True, text=True).stdout.strip()
    trials = []
    for t in tasks:
        conds = [c for c in FAMILY_CONDITIONS[t["family"]] if not args.conditions or c in args.conditions]
        for rep in range(args.reps):
            # Interleave: within each repetition, every task's conditions appear in a shuffled order.
            for c in conds:
                trials.append({"task": t["id"], "family": t["family"], "condition": c, "rep": rep})
    rng = random.Random(args.seed)
    blocks = {}
    for tr in trials:
        blocks.setdefault(tr["rep"], []).append(tr)
    ordered = []
    for rep in sorted(blocks):
        b = blocks[rep]
        rng.shuffle(b)
        ordered += b
    for i, tr in enumerate(ordered):
        tr["order"] = i
        tr["trial"] = hashlib.sha256(f"{args.seed}:{i}:{tr['task']}:{tr['condition']}:{tr['rep']}".encode()).hexdigest()[:10]
    digest = subprocess.run([sys.executable, str(BUNDLE / "tools" / "bundle.py"), "digest", str(BUNDLE)],
                            capture_output=True, text=True).stdout.strip().splitlines()[:1]
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = bool(subprocess.run(["git", "status", "--porcelain", "--", ".agents", "evals"], cwd=ROOT,
                                capture_output=True, text=True).stdout.strip())
    plan = {
        "created": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "model": args.model, "effort": args.effort, "claude": claude, "claude_version": version,
        "config_dir": str(cfg), "isolation": "degraded: user CLAUDE.md in every arm" if str(cfg) == DEFAULT_CONFIG else "clean",
        "workspace_base": args.workspace_base,
        "max_turns": args.max_turns, "timeout_s": args.timeout, "seed": args.seed, "reps": args.reps,
        "bundle_digest": digest[0] if digest else None, "repo_head": head, "repo_dirty": dirty,
        "tasks": {t["id"]: {"family": t["family"], "level": t.get("level", "L0"), "trap": t.get("trap", t["id"]),
                            "notes": t.get("notes", []),
                            "placebo_note": t.get("placebo_note"), "hash": tree_hash(Path(t["dir"])),
                            "oracle_chars": sum(len(note_text(n)) for n in t.get("notes", [])),
                            "placebo_chars": len(note_text(t["placebo_note"])) if t.get("placebo_note") else None}
                  for t in tasks},
        "harness_hash": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16],
        "trials": ordered,
    }
    run.mkdir(parents=True, exist_ok=True)
    (run / "plan.json").write_text(json.dumps(plan, indent=1))
    n_by = {}
    for tr in ordered:
        n_by[tr["condition"]] = n_by.get(tr["condition"], 0) + 1
    print(f"plan: {len(ordered)} trials over {len(tasks)} tasks, {n_by}; bundle {plan['bundle_digest']}; "
          f"{version}; repo {'DIRTY' if dirty else 'clean'} at {head[:10]}")
    return 0


def done_trials(run: Path) -> set[str]:
    p = run / "results.jsonl"
    if not p.exists():
        return set()
    return {json.loads(l)["trial"] for l in p.read_text().splitlines() if l.strip()}


def run_trial(plan: dict, tr: dict, run: Path, dry: bool) -> dict:
    task = load_task(tr["task"])
    base = workspace_base(plan.get("workspace_base"))
    tdir = base / tr["trial"]
    if tdir.exists():
        shutil.rmtree(tdir)
    tdir.mkdir()
    ws = tdir / "ws"
    info = prepare(task, tr["condition"], ws)
    settings_path = tdir / "settings.json"
    settings_path.write_text(json.dumps(trial_settings(ws), indent=1))
    rec = {**tr, "started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "prepared": info}
    if dry:
        rec["dry_run"] = True
        print(f"[dry] {tr['order']:4d} {tr['task']} {tr['condition']} rep{tr['rep']} -> {ws}")
        return rec
    art = run / "trials" / tr["trial"]
    art.mkdir(parents=True, exist_ok=True)
    transcript = art / "transcript.jsonl"
    rec["invoke"] = invoke(plan, ws, task["prompt"], settings_path, transcript,
                           task.get("max_turns", plan["max_turns"]), task.get("timeout_s", plan["timeout_s"]))
    rec["trace"] = parse_transcript(transcript, ws)
    git(ws, "add", "-A")
    # Against the starting commit, not the index: an agent may commit its own work.
    start = git(ws, "rev-list", "--max-parents=0", "HEAD").split()[0]
    diff = git(ws, "diff", "--cached", start, "--", ".", ":(exclude).agents", ":(exclude)AGENTS.md", ":(exclude)CLAUDE.md")
    (art / "diff.patch").write_text(diff)
    rec["diff_lines"] = sum(1 for l in diff.splitlines() if l[:1] in "+-" and l[:3] not in ("+++", "---"))
    rec["grade"] = grade(task, ws)
    rec["success"] = bool(rec["grade"]["hidden"]["passed"])
    shutil.rmtree(tdir, ignore_errors=True)
    return rec


def cmd_run(args) -> int:
    run = Path(args.run)
    plan = json.loads((run / "plan.json").read_text())
    for tid, t in plan["tasks"].items():
        if tree_hash(TASKS / tid) != t["hash"]:
            raise SystemExit(f"task {tid} changed since the plan was frozen")
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16] != plan["harness_hash"] and not args.dry_run:
        raise SystemExit("the harness changed since the plan was frozen; write a new plan")
    problems = check_config_dir(plan["config_dir"])
    if problems:
        raise SystemExit("config dir is not clean:\n  " + "\n  ".join(problems))
    done = done_trials(run)
    pending = [t for t in plan["trials"] if t["trial"] not in done]
    if args.limit:
        pending = pending[: args.limit]
    print(f"{len(done)} done, {len(pending)} to run now, {args.jobs} at a time", flush=True)
    lock = threading.Lock()

    def one(tr):
        try:
            rec = run_trial(plan, tr, run, args.dry_run)
        except Exception as e:  # an infrastructure failure: recorded, never silently dropped
            rec = {**tr, "harness_error": repr(e), "success": None, "trace": {"result": None, "tool_calls": 0}}
        if args.dry_run:
            return
        with lock:
            with open(run / "results.jsonl", "a") as f:
                f.write(json.dumps(rec) + "\n")
            r = ((rec.get("trace") or {}).get("result") or {})
            print(f"{tr['order']:4d} {tr['task']:36s} {tr['condition']:14s} rep{tr['rep']} "
                  f"{'PASS' if rec['success'] else 'fail' if rec['success'] is not None else 'ERROR'} "
                  f"turns={r.get('num_turns')} cost={r.get('total_cost_usd')} "
                  f"{'TIMEOUT' if (rec.get('invoke') or {}).get('timed_out') else ''}"
                  f"{' OUTSIDE-ACCESS' if (rec.get('trace') or {}).get('outside') else ''}"
                  f"{' ' + rec['harness_error'] if rec.get('harness_error') else ''}", flush=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as ex:
        list(ex.map(one, pending))
    return 0


PROBE = ("Do not use any tool. List, verbatim, every Markdown heading (lines starting with #) of the "
         "project instructions you were given for this session (CLAUDE.md, AGENTS.md or anything they "
         "import), in order. If you were given no project instructions, reply with the single word NONE.")


def cmd_probe(args) -> int:
    run = Path(args.run)
    plan = json.loads((run / "plan.json").read_text())
    tid = next(iter(t for t, v in plan["tasks"].items() if v["family"] == "judgment"), next(iter(plan["tasks"])))
    task = load_task(tid)
    out = []
    for cond in CONDITIONS:
        if cond not in FAMILY_CONDITIONS[task["family"]]:
            continue
        base = workspace_base(plan.get("workspace_base"))
        tdir = base / f"probe-{cond}"
        shutil.rmtree(tdir, ignore_errors=True)
        tdir.mkdir()
        ws = tdir / "ws"
        prepare(task, cond, ws)
        sp = tdir / "settings.json"
        sp.write_text(json.dumps(trial_settings(ws)))
        tpath = run / f"probe-{cond}.jsonl"
        inv = invoke(plan, ws, PROBE, sp, tpath, 2, 300, tools=[])
        text = ""
        for line in tpath.read_text().splitlines():
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "result":
                text = ev.get("result") or ""
        out.append({"condition": cond, "reply": text, "invoke": inv})
        print(f"--- {cond}\n{text.strip()}\n")
        shutil.rmtree(tdir, ignore_errors=True)
    (run / "probe.json").write_text(json.dumps(out, indent=1))
    return 0


def cmd_status(args) -> int:
    run = Path(args.run)
    plan = json.loads((run / "plan.json").read_text())
    done = done_trials(run)
    print(f"{len(done)}/{len(plan['trials'])} trials done")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--tasks", nargs="*")
    p = sub.add_parser("plan")
    p.add_argument("run")
    p.add_argument("--model", required=True)
    p.add_argument("--effort")
    p.add_argument("--tasks", nargs="*")
    p.add_argument("--conditions", nargs="*", choices=CONDITIONS)
    p.add_argument("--reps", type=int, default=3)
    p.add_argument("--seed", type=int, default=20260924)
    p.add_argument("--max-turns", type=int, default=60)
    p.add_argument("--timeout", type=int, default=1800)
    p.add_argument("--config-dir", default="~/.config/agent-guides/eval-claude")
    p.add_argument("--workspace-base")
    p.add_argument("--claude")
    for name in ("run", "probe", "status"):
        s = sub.add_parser(name)
        s.add_argument("run")
        if name == "run":
            s.add_argument("--limit", type=int)
            s.add_argument("--dry-run", action="store_true")
            s.add_argument("--jobs", type=int, default=1)
    a = ap.parse_args(argv)
    return {"check": cmd_check, "plan": cmd_plan, "run": cmd_run, "probe": cmd_probe, "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
