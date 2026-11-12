# Changelog

Changes to the published `DESIGN.md` files. Newest first, each entry tagged
with its system.

## 2026-11-12 [formsflow] Primary button states

- `button-primary` no longer has a solid `primary` fill at rest. The product
  spec follows the formsflow V8 Primary-Button: gray-50 fill, 1px indigo-500
  border, gray-800 `body-sml` text. On hover the border turns to `primary`.
- New selected (indigo-100 fill, `primary` border) and disabled (indigo-300
  border, gray-200 text) states. "Pressed" is no longer specified.
- New marketing-pages variant from the web Nav CTA: indigo-100 fill, 1px
  `primary` border, gray-800 `body` text. On hover it fills `primary` with
  `on-primary` text.
- `primary-hover` is unchanged, though no button state uses it now.
- Request: `changes/2026-11-12-formsflow-button-primary-states.md`.

## 2026-11-10 [aot] Primary button hover and shadow tokens

- New `colors.primary-hover` (`#33B9E2`, sky-blue darkened 6%), used by
  `button-primary-hover`. It matches `--color-brand-hover` in Claude Design.
- New `shadows` group: `xs`, `sm`, `md` and `lg` with the exact upstream
  values, plus `focus` for the 3px sky-blue ring. The Elevation prose now
  names these tokens instead of giving ranges.
- Motion prose: buttons darken ~6% on hover, not brighten; primary buttons use
  `{colors.primary-hover}`.
- Request: `changes/2026-10-21-aot-button-hover-and-shadows.md`.

## 2026-10-22 [repo] Claude plugins and GitHub releases

- The repo is now a Claude plugin marketplace, `aot-design-systems`, with one
  plugin per system: `formsflow-design` and `aot-design`. Each holds a skill
  and a generated copy of the system's `DESIGN.md`.
- `make build` refreshes the plugin copies (`scripts/build_plugins.py`), and a
  new `plugin-current` check in `make verify` fails if one is stale.
- `.github/workflows/release.yml` publishes a GitHub release per system when
  its `DESIGN.md` changes on `main` (`scripts/release.py`).
- README: new "Using these files" section.

## 2026-10-21 [formsflow] Email section aligned with zeroheight

- Scope no longer lists trial emails: marketing, onboarding lifecycle and
  account notifications.
- The Outlook for Windows conditional style is now given as an exact snippet.
- Added one `h1` per email, what each email size is for, and the fallback
  stack on every text element.
- Request: `changes/2026-10-21-formsflow-email-zeroheight-alignment.md`.

## 2026-10-21 [formsflow] Heading weights

- `h1`, `h2` and `h3` now default to semibold (600) instead of medium (500),
  matching zeroheight. `max1` stays medium; `max2` to `max6` are unchanged.
- Email: the weights note now explains why email avoids medium and light,
  instead of treating semibold headings as an exception.
- Request: `changes/2026-10-21-formsflow-heading-weights.md`.

## 2026-10-21 [formsflow] Line heights and email guidance

- Every size now has its own px line-height (from `16px` for `caption` to
  `88px` for `max6`) instead of `1`.
- `tokens/typography.json`: line heights only, read from the Figma text styles
  on the `formsflow-V8` branch through the Figma connector (not a plugin
  export). All other values matched Figma and are unchanged.
- Prose: a 12-size scale, per-size line heights, and a new Email section (font
  stack, semibold headings, sizes, container). Workflow notification emails
  are out of scope.
- Request: `changes/2026-10-21-formsflow-line-height-and-email.md`.

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
