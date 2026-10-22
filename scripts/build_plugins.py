#!/usr/bin/env python3
"""
build_plugins.py: copy each system's DESIGN.md into its Claude Code plugin.

    systems/<name>/DESIGN.md  ->  plugins/<name>-design/skills/<name>-design-system/DESIGN.md

.claude-plugin/marketplace.json lists the plugins. Each plugin's SKILL.md and
plugin.json are hand-authored. The DESIGN.md beside SKILL.md is GENERATED:
never hand-edit it. A copy (not a symlink) survives Windows checkouts and
claude.ai organisation sync.

Usage:
    python scripts/build_plugins.py                   # every system
    python scripts/build_plugins.py --system aot      # one

Standard library only.
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SYSTEMS = ROOT / "systems"
PLUGINS = ROOT / "plugins"


def copy_path(name):
    return PLUGINS / f"{name}-design" / "skills" / f"{name}-design-system" / "DESIGN.md"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--system", help="system folder name under systems/ (default: all)")
    args = p.parse_args()
    names = [args.system] if args.system else [c.parent.name for c in sorted(SYSTEMS.glob("*/system.json"))]
    for name in names:
        out = copy_path(name)
        if not out.parent.is_dir():
            sys.exit(f"no plugin skill for '{name}': expected {out.parent.relative_to(ROOT)}/")
        out.write_text((SYSTEMS / name / "DESIGN.md").read_text())
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
