# CLAUDE.md: AOT design systems repo

This repo is the shared source for two design systems. Each system has its own
`DESIGN.md`, the reference AI agents load before generating UI or copy for that
brand. Both follow the DESIGN.md format
(https://github.com/google-labs-code/design.md). Agents across the organisation
read these files, so a wrong value here spreads everywhere. Work carefully and
stay inside the rules below.

| System | Folder | Mode | Source of truth |
| --- | --- | --- | --- |
| formsflow.ai | `systems/formsflow/` | generated | Figma exports in `tokens/`, plus `src/` |
| AOT Technologies | `systems/aot/` | manual | Claude Design project `875c59c0-39ca-4f76-b742-061041f7f2ac` |

Each folder's `system.json` records its mode and the checks it must pass.

## Keep the systems separate

- **Every change targets exactly one system.** If something affects both,
  write two change requests.
- **Never copy tokens, rules or prose from one system to the other.** Some hex
  values appear in both (shared lineage), but that isn't a reason to align
  them. formsflow.ai is an independent brand: its file says not to fold in
  AOT's identity or voice.
- **Each system's voice and naming rules live in its own `DESIGN.md`.** Follow
  the target system's rules, never the other's. For example, AOT uses Title
  Case display headings, while formsflow uses sentence case throughout.

## formsflow (generated)

| To change… | Edit | Notes |
| --- | --- | --- |
| Rationale, rules, do's and don'ts | `src/DESIGN.prose.md` | Hand-authored. |
| Colour roles, default weight per size, radius scale | `src/semantic.json` | Design decisions. Change only when a change request says so. |
| Sizes, weights, line heights, colour hexes, spacing | `tokens/*.json` | Figma exports. **Never edit by hand.** |
| How the front matter is generated | `scripts/build_design_md.py` | If a new export's shape differs, change the loader, never the export. |
| `DESIGN.md` | Nothing. | Generated. Run `make build SYSTEM=formsflow`. |

The `tokens/` files were reconstructed on 2026-10-21 from the July 2026
`DESIGN.md`. The values are exact, and the structure matches the July Figma
export. The first real export replaces them.

## AOT (manual)

`systems/aot/DESIGN.md` is the source file. Nothing generates it, and its
front matter (colours, type, radii, spacing, components) is edited directly.
Run `make build SYSTEM=aot` afterwards to refresh its plugin copy.

- The Claude Design project is upstream. A token value changes there first, by
  a person, and is then mirrored here through a change request. Don't change a
  value only in this repo.
- Keep the existing front-matter conventions: rem font sizes with a px comment,
  named spacing (`xs` to `3xl`), and component references such as
  `"{colors.primary}"`.

## Distribution (both systems)

Consumers get each `DESIGN.md` through a Claude plugin or a GitHub release.
See the README's "Using these files".

- `.claude-plugin/marketplace.json` lists one plugin per system, in
  `plugins/<system>-design/`. `plugin.json` and `SKILL.md` are hand-authored.
  The `DESIGN.md` beside `SKILL.md` is a generated copy: `make build` writes
  it, and `make verify` fails if it's stale. Leave `version` out of
  `plugin.json` so plugins track `main`.
- `.github/workflows/release.yml` runs `scripts/release.py` on every push to
  `main`. It releases each system whose `DESIGN.md` changed, tagged
  `<system>/YYYY-MM-DD`, with that system's `CHANGELOG.md` entries as notes.
  Never create tags or releases by hand.

## Hard rules (both systems)

1. **Don't invent values.** No new colours, sizes, radii, shadows, font
   families, spacing steps or components unless a change request specifies
   them. If something is missing, flag the gap.
2. **Never hand-edit a generated file**: formsflow's `DESIGN.md` or `tokens/`,
   or a plugin's copy of `DESIGN.md`.
3. **`make verify` must pass for every system.** That means 0 errors and 0
   warnings from the linter, plus each system's own checks.
4. **Approval gate.** After building and verifying, summarise the diff and
   stop. Commit, push or open a PR only after a person approves. Never push to
   `main`.
5. **Apply change requests exactly.** If a find-and-replace doesn't match
   exactly once, stop and report it. Don't improvise a nearby edit.

## Writing prose for agents

- Write short, imperative lines an agent can act on, not aspirational brand
  copy.
- Don't restate token values the front matter already carries. Duplicates
  drift. (formsflow's primitive colour ramp is the one exception, and
  `make verify` keeps it in sync.)
- Use Canadian/British spelling in prose (colour, centre). Keep the format's
  own section names (`## Colors`).

## Workflow

Change requests live in `changes/`, named `YYYY-MM-DD-<system>-<slug>.md`, with
a `System:` field. Start from `changes/TEMPLATE.md`.

- `/new-change <description>` drafts one for review.
- `/apply-change <path>` applies an approved one.

When a change is applied, add an entry to `CHANGELOG.md` tagged with the system,
and set the request's `Status` to `applied`.

## Commands

```
make build [SYSTEM=<name>]      # regenerate generated systems, refresh plugin copies
make verify [SYSTEM=<name>]     # run each system's checks (default: all)
```

Requires Python 3.9+ (standard library only) and Node 18+ (for `npx`). The
linter version is pinned in the `Makefile`.
