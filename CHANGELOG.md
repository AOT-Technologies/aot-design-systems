# Changelog

Changes to the published `DESIGN.md` files. Newest first, each entry tagged
with its system.

## 2026-10-21 [repo] Two-system setup

- The repo now holds two systems, each with its own `DESIGN.md`:
  `systems/formsflow/` (generated) and `systems/aot/` (manual).
- Added `systems/<name>/system.json` (mode and checks) and `scripts/verify.py`.
  `make build` and `make verify` take an optional `SYSTEM=<name>`.
- Added `.github/CODEOWNERS`: @timng-aot reviews all changes.

## 2026-10-21 [aot] Added to the repo

- Imported the existing AOT Technologies `DESIGN.md` unchanged (from the
  Claude Design project). It lints at 0 errors and 0 warnings.

## 2026-10-21 [formsflow] Pipeline rebuilt

- Rebuilt the July converter as `scripts/build_design_md.py`. It reproduces the
  July `DESIGN.md` byte for byte.
- Reconstructed `tokens/` from that `DESIGN.md` (bootstrap; see `CLAUDE.md`).
- Verify checks: build is current, prose colour ramp is in sync, and lint is
  0/0 (`@google/design.md` 0.4.0).
- No change to `DESIGN.md` content.
- Pending: `changes/2026-10-21-formsflow-line-height-and-email.md`.

## 2026-07 [formsflow] First version

- Front matter generated from the Figma exports, with semantic colour roles,
  default weight per size and the radius scale.
- Prose distilled from zeroheight: brand, voice, naming, logo, do's and don'ts.
