# AOT design systems: DESIGN.md source

This repo is the shared source for two design systems, **formsflow.ai** and
**AOT Technologies**. Each has its own `DESIGN.md`: the reference AI agents
load before building UI or writing copy for that brand. Both follow the
[DESIGN.md format](https://github.com/google-labs-code/design.md).

| System | Use it for | File |
| --- | --- | --- |
| formsflow.ai | formsflow.ai product UI, marketing site and email | [`systems/formsflow/DESIGN.md`](systems/formsflow/DESIGN.md) |
| AOT Technologies | AOT Technologies brand, collateral and AOT-branded product UI | [`systems/aot/DESIGN.md`](systems/aot/DESIGN.md) |

**To use one:** give your agent the `DESIGN.md` for the brand you're working
on, for example by adding it to a Claude Project or pointing a coding agent at
the file. Give it one system, not both: formsflow.ai is an independent brand,
and mixing the two produces neither. Don't copy values into other files; link
to the file so updates reach you.

## How each system is maintained

The two systems come from different sources, so they're maintained
differently.

**formsflow.ai is generated.** Don't edit its `DESIGN.md` directly.

```
tokens/typography.json  ─┐   Figma exports (source of truth for values)
tokens/variables.json   ─┤
src/semantic.json       ─┼─▶ scripts/build_design_md.py ─▶ DESIGN.md
src/DESIGN.prose.md     ─┘   decisions + hand-written guidance
```

- Figma owns token values. A change starts in Figma, and a fresh export
  replaces the file in `tokens/`.
- zeroheight is the human-facing formsflow design system. The prose distils it
  for agents.

**AOT Technologies is hand-authored.** Its `DESIGN.md` is edited directly. The
AOT Technologies Design System in Claude Design is upstream: a token change is
made there first, then mirrored here.

## Proposing a change

1. Copy `changes/TEMPLATE.md` (or run `/new-change` in Claude Code). Name the
   system it affects and describe the change, its source and any decisions.
   One system per request.
2. Once the request is approved, run `/apply-change changes/<file>.md` in
   Claude Code. It applies the edits, rebuilds, verifies, and then waits for
   your approval before opening a PR.
3. Open a PR; don't push to `main`. CI runs `make verify` for both systems on
   every PR, and `.github/CODEOWNERS` requests a review from @timng-aot.
   Neither blocks a merge, because branch protection isn't available for this
   private repo on the org's GitHub plan. Merge only after the check passes
   and @timng-aot approves.

`CLAUDE.md` has the rules Claude Code follows in this repo.

## Commands

```
make build [SYSTEM=formsflow]   # regenerate formsflow's DESIGN.md
make verify [SYSTEM=<name>]     # check every system, or one
```

Every system must lint at 0 errors and 0 warnings. formsflow also checks that
its `DESIGN.md` matches a fresh build and that its prose colour ramp matches
the tokens. Requires Python 3.9+ (standard library only) and Node 18+.

## Status

See `CHANGELOG.md`.
