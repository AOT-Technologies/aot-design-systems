# Change request: <short title>

- **ID:** YYYY-MM-DD-<system>-short-slug (also the file name)
- **System:** formsflow | aot (one system per request)
- **Requested by:** <name>
- **Status:** draft | pending | applied (YYYY-MM-DD)
- **Touches:** <files under systems/<system>/>

## Why

<What's wrong or missing, and where the correct answer comes from (zeroheight
page, Figma file, Claude Design project, decision).>

## Decisions

<Numbered decisions, with who made them and when. Claude Code doesn't make
these.>

## Part A: upstream change (a person does this first; delete if not needed)

- formsflow: the Figma change, with exact expected values, then a fresh export
  into `tokens/`. Include a check Claude Code runs on the new export.
- aot: the change in the Claude Design project, with exact expected values.

## Part B: source edits

<Exact find-and-replace pairs.
formsflow: src/DESIGN.prose.md or src/semantic.json.
aot: systems/aot/DESIGN.md (front matter or prose).
Each find string must match exactly once.>

## Part C: build and verify

1. `make build SYSTEM=<system>` (aot: refreshes only the plugin copy).
2. `make verify`: every check passes for every system.
3. `git diff systems/<system>/DESIGN.md`. Expect exactly: <list>. Report
   anything else.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged with the system.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

<Related work this request deliberately doesn't cover.>
