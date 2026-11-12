---
description: Draft a change request for one system's DESIGN.md
argument-hint: <system and what should change, e.g. "aot: add a hover colour for primary buttons">
---

Draft a change request for: $ARGUMENTS

1. Work out which system it targets. If that's unclear, or the change spans
   both systems, ask before drafting. A change to both becomes two requests.
2. Read `CLAUDE.md` and that system's sources (`systems/<system>/system.json`
   and its `DESIGN.md`, plus `src/` for formsflow) so the draft is grounded in
   the current text.
3. Copy `changes/TEMPLATE.md` to `changes/<YYYY-MM-DD>-<system>-<slug>.md` and
   fill it in with **Status: draft**.
4. Put any new or changed token values in Part A as an upstream step for a
   person (Figma for formsflow, the AOT Design System artifact in Claude for
   aot), with the exact expected values.
5. Write Part B as exact find-and-replace pairs against the current files, and
   confirm each find string matches exactly once.
6. Don't fill in decisions yourself. List any open question under Decisions as
   **Open:** and ask about it in your summary.
7. Don't edit any other file. Show the draft and stop.
