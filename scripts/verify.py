#!/usr/bin/env python3
"""
verify.py: run the checks each system declares in systems/<name>/system.json.

    build-current  DESIGN.md matches a fresh build from source (generated systems)
    prose-ramp     the primitive colour ramp in the prose matches tokens/variables.json
    lint           the DESIGN.md linter reports 0 errors and 0 warnings

Usage:
    python scripts/verify.py                    # every system
    python scripts/verify.py --system aot       # one system
    python scripts/verify.py --linter @google/design.md@0.4.0
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_design_md as builder  # noqa: E402

ROOT = builder.ROOT
SYSTEMS = builder.SYSTEMS


def check_build_current(name, _):
    built = builder.build(name)
    current = (SYSTEMS / name / "DESIGN.md").read_text()
    if built != current:
        return f"DESIGN.md is out of date: run `make build SYSTEM={name}` and commit the result."
    return None


def check_prose_ramp(name, _):
    d = SYSTEMS / name
    prose = (d / "src" / "DESIGN.prose.md").read_text()
    tokens = json.loads((d / "tokens" / "variables.json").read_text())["ff"]["color"]
    m = re.search(r"\*\*Primitive ramp values\.\*\*.*?```\n(.*?)```", prose, re.S)
    if not m:
        return "couldn't find the 'Primitive ramp values' block in the prose."
    written = {}
    for line in m.group(1).strip().splitlines():
        fam, rest = line.split(None, 1)
        for step, hx in re.findall(r"(\w+) (#[0-9A-Fa-f]{6})", rest):
            written[f"{fam}-{step}"] = hx.upper()
    exported = {f"{f}-{s}": t["$value"]["hex"].upper() for f, steps in tokens.items() for s, t in steps.items()}
    diffs = [f"{k}: prose {written.get(k, 'missing')} vs tokens {exported.get(k, 'missing')}"
             for k in sorted(set(written) | set(exported)) if written.get(k) != exported.get(k)]
    if diffs:
        return "colour ramp out of sync with tokens/variables.json:\n      " + "\n      ".join(diffs)
    return None


def check_lint(name, linter):
    path = SYSTEMS / name / "DESIGN.md"
    r = subprocess.run(["npx", "-y", "-p", linter, "designmd", "lint", str(path)],
                       capture_output=True, text=True)
    try:
        report = json.loads(r.stdout)
    except json.JSONDecodeError:
        return f"couldn't read linter output:\n{r.stdout}\n{r.stderr}"
    s = report["summary"]
    if s["errors"] or s["warnings"]:
        found = [f"[{f['severity']}] {f.get('rule', '')}: {f['message']}"
                 for f in report.get("findings", []) if f.get("severity") != "info"]
        return f"{s['errors']} errors, {s['warnings']} warnings\n      " + "\n      ".join(found)
    return None


CHECKS = {"build-current": check_build_current, "prose-ramp": check_prose_ramp, "lint": check_lint}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--system", help="system folder name under systems/ (default: all)")
    p.add_argument("--linter", default="@google/design.md", help="npm package spec for the linter")
    args = p.parse_args()
    names = [args.system] if args.system else [c.parent.name for c in sorted(SYSTEMS.glob("*/system.json"))]

    failed = False
    for name in names:
        cfg = builder.system_config(name)
        print(f"{cfg['title']} ({name}, {cfg['mode']})")
        for check in cfg.get("checks", []):
            if check not in CHECKS:
                print(f"  ✗ {check}: unknown check")
                failed = True
                continue
            try:
                problem = CHECKS[check](name, args.linter)
            except Exception as e:  # report and keep going so every system is checked
                problem = f"{type(e).__name__}: {e}"
            print(f"  {'✗' if problem else '✓'} {check}" + (f": {problem}" if problem else ""))
            failed = failed or bool(problem)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
