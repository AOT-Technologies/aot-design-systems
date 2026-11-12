# Change request: AOT upstream reference after the move to Claude

- **ID:** 2026-11-10-aot-upstream-reference
- **System:** aot
- **Requested by:** Tim
- **Status:** applied (2026-11-12)
- **Touches:** `systems/aot/DESIGN.md` (source comment only), `systems/aot/system.json` (`source` field)

## Why

On 2026-11-10 the AOT Technologies Design System moved out of standalone
Claude Design (project `875c59c0-39ca-4f76-b742-061041f7f2ac`) into Claude,
where it's now a Design System artifact:
`https://claude.ai/artifact/YCmVtamuUv1XR4spQE447N`. Standalone Claude Design
closes on 2026-12-14, and the old project is read-only. Both files still name
the old project as the source, so agents and people would look in the wrong
place.

The move was checked on 2026-11-10 by reading the artifact: its
`tokens/colors.css`, `tokens/spacing.css` and `tokens/typography.css` match the
pre-move snapshot, apart from the approved `--color-brand-hover` (see
`changes/2026-10-21-aot-button-hover-and-shadows.md`). The artifact's
`design-system.json` records the old project ID as its source.

## Decisions

Both made by Tim on 2026-11-12.

1. **Record the canonical link,**
   `https://claude.ai/artifact/YCmVtamuUv1XR4spQE447N`, not the Claude Code
   link to the same artifact
   (`https://claude.ai/code/artifact/fcafe721-65ea-4193-8a3b-a51df20ac045`).
2. **Keep the old project ID for history,** as "moved from Claude Design
   project … on 2026-11-10", because the CHANGELOG and earlier requests cite
   it.

## Part A: upstream change

Not needed: no values change. The move itself is the upstream event, and it's
confirmed above.

## Part B: source edits

Each find string must match exactly once.

**B1. `systems/aot/DESIGN.md` source comment.** Find:
```
<!-- Source: AOT Technologies Design System (Claude Design project 875c59c0-39ca-4f76-b742-061041f7f2ac). -->
```
Replace:
```
<!-- Source: AOT Technologies Design System, a Design System artifact in Claude (https://claude.ai/artifact/YCmVtamuUv1XR4spQE447N); moved from Claude Design project 875c59c0-39ca-4f76-b742-061041f7f2ac on 2026-11-10. -->
```

**B2. `systems/aot/system.json` source field.** Find:
```
  "source": "AOT Technologies Design System, Claude Design project 875c59c0-39ca-4f76-b742-061041f7f2ac",
```
Replace:
```
  "source": "AOT Technologies Design System, Design System artifact in Claude https://claude.ai/artifact/YCmVtamuUv1XR4spQE447N (moved from Claude Design project 875c59c0-39ca-4f76-b742-061041f7f2ac on 2026-11-10)",
```

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system.
3. `git diff systems/aot/`. Expect exactly:
   - the source comment on the last line of `DESIGN.md` (B1);
   - the `source` field in `system.json` (B2).

   Report anything else. The plugin copy under `plugins/aot-design/` should
   show the same one-line diff as `DESIGN.md`.

Merging publishes a new AOT release, because `DESIGN.md` changes, even though
only a comment does.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- Repo-wide references to Claude Design (`CLAUDE.md`, README, the
  `/apply-change` and `/new-change` commands, `changes/TEMPLATE.md`): a
  separate `[repo]` PR.
- Past change requests and CHANGELOG entries: they record what was true at
  the time, so they keep the old project ID.
- The formsflow.ai Claude Design projects: not part of this repo's sources.
