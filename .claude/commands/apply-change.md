---
description: Apply a change request from changes/ to one system's DESIGN.md
argument-hint: <path, e.g. changes/2026-10-21-formsflow-line-height-and-email.md>
---

Apply the change request at `$ARGUMENTS`.

1. Read `CLAUDE.md` and the change request in full. Note its **System** and
   that system's mode in `systems/<system>/system.json`. Restate the scope in
   two or three sentences. If the request has no single System, stop and ask.
2. Check every precondition, especially Part A (a fresh Figma export for
   formsflow, or a confirmed change to the AOT Design System artifact in Claude
   for aot). If a precondition isn't met, stop and say exactly what a person
   needs to do. Don't work around it, and never hand-edit generated files.
3. Create a branch named `change/<request ID>`.
4. Apply Part B exactly as written, touching only files under
   `systems/<system>/`. If a find string doesn't match exactly once, stop and
   report it. Don't approximate.
5. Run `make build SYSTEM=<system>` (for aot, this only refreshes the plugin
   copy). Then run `make verify`. If anything fails, report it and stop.
6. Compare `git diff` with the expected diff in Part C. Map every changed hunk
   to a part of the request, and list anything that doesn't map. The plugin
   copy under `plugins/<system>-design/` should match the `DESIGN.md` diff.
   Confirm the other system's files are untouched.
7. Update `CHANGELOG.md` and the request's **Status**, then show a short
   summary covering what changed, the verify result and anything unexpected.
   **Stop and wait for approval.**
8. Once approved, commit and open a pull request. Never push to `main`.
