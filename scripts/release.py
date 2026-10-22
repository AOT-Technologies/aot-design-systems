#!/usr/bin/env python3
"""
release.py: publish a GitHub release for each system whose DESIGN.md changed.

For each system, compares systems/<name>/DESIGN.md at HEAD with its latest
release tag. If it differs, or the system has no release yet, creates:

    tag      <name>/YYYY-MM-DD      (HEAD's commit date, UTC; .2, .3 ... if taken)
    asset    DESIGN.md
    notes    CHANGELOG.md entries tagged [<name>] that weren't in the previous release

Releases are never marked "Latest": the repo holds two systems, so a
repo-wide latest would point at whichever released last.

Runs from .github/workflows/release.yml on every push to main. Needs full
history and tags, and `gh` authenticated (GH_TOKEN).

Usage:
    python scripts/release.py              # create releases
    python scripts/release.py --dry-run    # print what would be released

Standard library only.
"""
import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SYSTEMS = ROOT / "systems"
REPO = "AOT-Technologies/aot-design-systems"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_design_md as builder  # noqa: E402


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def latest_tag(name):
    """Newest <name>/YYYY-MM-DD[.N] tag, or None."""
    pattern = re.compile(rf"^{re.escape(name)}/(\d{{4}}-\d{{2}}-\d{{2}})(?:\.(\d+))?$")
    found = []
    for tag in git("tag", "--list", f"{name}/*").split():
        m = pattern.match(tag)
        if m:
            found.append(((m.group(1), int(m.group(2) or 1)), tag))
    return max(found)[1] if found else None


def new_tag(name):
    ts = int(git("log", "-1", "--format=%ct").strip())
    date = datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d")
    taken = set(git("tag", "--list", f"{name}/{date}*").split())
    tag, n = f"{name}/{date}", 1
    while tag in taken:
        n += 1
        tag = f"{name}/{date}.{n}"
    return tag


def changelog_sections(text, name):
    """{heading: section} for CHANGELOG sections tagged [name]."""
    sections = {}
    for part in re.split(r"(?m)^(?=## )", text):
        first = part.split("\n", 1)[0]
        if re.match(rf"## \S+ \[{re.escape(name)}\] ", first):
            sections[first] = part.strip()
    return sections


def notes(name, prev):
    current = changelog_sections((ROOT / "CHANGELOG.md").read_text(), name)
    seen = changelog_sections(git("show", f"{prev}:CHANGELOG.md"), name) if prev else {}
    new = [s for h, s in current.items() if h not in seen]
    body = "\n\n".join(new) if new else "_No CHANGELOG entry for this release._"
    return (f"{body}\n\n---\n\nDownload:\n\n"
            f"```\ngh release download {new_tag(name)} --repo {REPO} --pattern DESIGN.md\n```\n")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dry-run", action="store_true", help="print what would be released and stop")
    args = p.parse_args()
    head = git("rev-parse", "HEAD").strip()

    for cfg_path in sorted(SYSTEMS.glob("*/system.json")):
        name = cfg_path.parent.name
        rel = f"systems/{name}/DESIGN.md"
        prev = latest_tag(name)
        if prev and git("show", f"{prev}:{rel}") == (ROOT / rel).read_text():
            print(f"{name}: unchanged since {prev}")
            continue
        tag = new_tag(name)
        title = f"{builder.system_config(name)['title']} {tag.split('/', 1)[1]}"
        body = notes(name, prev)
        print(f"{name}: releasing {tag} (previous: {prev or 'none'})")
        if args.dry_run:
            print("\n".join("    " + line for line in body.splitlines()))
            continue
        subprocess.run(["gh", "release", "create", tag, rel, "--repo", REPO, "--target", head,
                        "--title", title, "--notes", body, "--latest=false"], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
