#!/usr/bin/env python3
"""
build_design_md.py: assemble DESIGN.md for a generated system from source.

For each system with "mode": "generated" in systems/<name>/system.json:

    tokens/typography.json   Figma Styles export      (values: size, weight, line-height, family)
    tokens/variables.json    Figma Variables export   (values: colour ramps, spacing)
    src/semantic.json        human design decisions   (colour roles, default weights, radii)
    src/DESIGN.prose.md      hand-authored body       (rationale, rules, do's and don'ts)

typography.json uses the JSON layout from zeroheight's Figma plugin
(ff.text-style.<family>.<style>.<property>.value). load_typography() reads only
that layout; a Tokens Studio export needs a loader update first.

The front matter is GENERATED. Never hand-edit it in DESIGN.md: edit a source
file and rebuild. Rebuilt from the July 2026 converter (ff_tokens_to_designmd.py);
output format is unchanged.

Manual systems (such as aot) have no build step: their DESIGN.md is the source.

Usage:
    python scripts/build_design_md.py                     # build every generated system
    python scripts/build_design_md.py --system formsflow  # build one
    python scripts/build_design_md.py --check             # exit 1 if any output is out of date

Standard library only.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SYSTEMS = ROOT / "systems"
WEIGHT_SUFFIXES = ("light", "regular", "medium", "semibold")


class BuildError(Exception):
    pass


def q(s):
    """Double-quote a string for YAML."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def px_value(v):
    """Numeric spacing value -> '16px'."""
    if isinstance(v, (int, float)):
        return f"{int(v) if float(v).is_integer() else v}px"
    return str(v)


def norm_line_height(v):
    """'100%' -> 1, '150%' -> 1.5; px values ('24px') and numbers pass through.
    The DESIGN.md format accepts unitless numbers and px/em/rem, not %."""
    s = str(v).strip()
    if s.endswith("%"):
        n = float(s[:-1]) / 100.0
        return str(int(n)) if n.is_integer() else str(round(n, 3))
    return s


# ---- sources ---------------------------------------------------------------

def load_typography(path):
    doc = json.loads(Path(path).read_text())
    families = doc.get("ff", {}).get("text-style", {})
    if not families:
        raise BuildError(f"{path}: expected ff.text-style.<family>.<style>")
    styles = {}
    for family in families.values():
        for name, props in family.items():
            styles[name] = {k: v.get("value") for k, v in props.items()}
    return styles


def load_variables(path):
    doc = json.loads(Path(path).read_text()).get("ff", {})
    colours = {}
    for fam, steps in doc.get("color", {}).items():
        for step, tok in steps.items():
            colours[f"{fam}-{step}"] = tok["$value"]["hex"].upper()
    spacing = {k: v["$value"] for k, v in doc.get("space", {}).items()}
    if not colours or not spacing:
        raise BuildError(f"{path}: expected ff.color and ff.space")
    return colours, spacing


# ---- front matter ----------------------------------------------------------

def build_front_matter(name, styles, colours, spacing, semantic):
    out = ["---", f"version: {q(semantic.get('version', 'alpha'))}", f"name: {q(name)}"]
    if semantic.get("description"):
        out.append(f"description: {q(semantic['description'])}")

    out.append("colors:")
    for role, ref in semantic["colors"].items():
        if ref not in colours:
            raise BuildError(f"semantic.json colour role '{role}' -> '{ref}' not in variables export")
        out.append(f"  {role}: {q(colours[ref])}   # = {ref}")

    out.append("typography:")
    rows = []
    for size, weight in semantic["typography_defaults"].items():
        if weight not in WEIGHT_SUFFIXES:
            raise BuildError(f"semantic.json: '{size}' has unknown weight '{weight}'")
        style = styles.get(f"{size}-{weight}")
        if style is None:
            raise BuildError(f"typography export has no style '{size}-{weight}'")
        rows.append((float(str(style["font-size"]).rstrip("px")), size, style))
    for _, size, s in sorted(rows, key=lambda r: r[0]):  # ascending by size
        out += [
            f"  {size}:",
            f"    fontFamily: {q(s['font-family'])}",
            f"    fontSize: {s['font-size']}",
            f"    fontWeight: {int(s['font-weight'])}",
            f"    lineHeight: {norm_line_height(s['line-height'])}",
        ]  # letter-spacing is deliberately excluded

    out.append("spacing:")
    for k in sorted(spacing, key=lambda x: float(x)):
        out.append(f"  {q(k)}: {px_value(spacing[k])}")

    out.append("rounded:")
    for k, v in semantic["rounded"].items():
        line = f"  {k}: {v['value']}"
        if v.get("comment"):
            line += f"  # {v['comment']}"
        out.append(line)

    out.append("---")
    return "\n".join(out) + "\n"


def system_config(name):
    path = SYSTEMS / name / "system.json"
    if not path.exists():
        raise BuildError(f"unknown system '{name}' (no {path.relative_to(ROOT)})")
    return json.loads(path.read_text())


def generated_systems():
    return [p.parent.name for p in sorted(SYSTEMS.glob("*/system.json"))
            if json.loads(p.read_text()).get("mode") == "generated"]


def build(name):
    cfg = system_config(name)
    if cfg.get("mode") != "generated":
        raise BuildError(f"'{name}' is a {cfg.get('mode')} system: edit its DESIGN.md directly")
    d = SYSTEMS / name
    styles = load_typography(d / "tokens" / "typography.json")
    colours, spacing = load_variables(d / "tokens" / "variables.json")
    semantic = json.loads((d / "src" / "semantic.json").read_text())
    prose = (d / "src" / "DESIGN.prose.md").read_text()
    return build_front_matter(cfg["name"], styles, colours, spacing, semantic) + "\n" + prose


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--system", help="system folder name under systems/ (default: all generated systems)")
    p.add_argument("--check", action="store_true", help="fail if DESIGN.md is out of date")
    args = p.parse_args()
    names = [args.system] if args.system else generated_systems()
    failed = False
    for name in names:
        if system_config(name).get("mode") != "generated":
            print(f"{name} is a manual system: nothing to generate.")
            continue
        try:
            result = build(name)
        except (BuildError, KeyError, ValueError) as e:
            sys.exit(f"build failed ({name}): {e}")
        out = SYSTEMS / name / "DESIGN.md"
        rel = out.relative_to(ROOT)
        if args.check:
            if not out.exists() or out.read_text() != result:
                print(f"{rel} is out of date: run `make build SYSTEM={name}` and commit the result.")
                failed = True
            else:
                print(f"{rel} is up to date.")
        else:
            out.write_text(result)
            print(f"wrote {rel}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
