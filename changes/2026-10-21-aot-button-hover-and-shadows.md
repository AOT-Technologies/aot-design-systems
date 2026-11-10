# Change request: primary button hover colour and shadow values

- **ID:** 2026-10-21-aot-button-hover-and-shadows
- **System:** aot
- **Requested by:** Tim
- **Status:** applied (2026-11-10)
- **Touches:** `systems/aot/DESIGN.md` (front matter and prose)

## Why

Two gaps make agents guess values:

1. **Primary button hover.** `button-primary-hover` uses `{colors.primary}`,
   the same background as `button-primary`, so the hover state is identical to
   rest. The only guidance is in the Motion prose ("brighten ~6% on hover"),
   which no colour token backs, and which is wrong: buttons darken on hover.
2. **Shadows.** Elevation & Depth gives the `xs` to `lg` levels only as ranges
   (`0 1px 2–3px rgba(44,55,60,.06–.08)` and `0 4–12px
   rgba(44,55,60,.08–.12)`). There are no shadow tokens, so each agent picks
   its own value inside the range.

The correct values live upstream in the AOT Technologies Design System (Claude
Design project `875c59c0-39ca-4f76-b742-061041f7f2ac`).

## Decisions

All made by Tim on 2026-11-10.

1. **Hover darkens.** The primary hover colour is `#33B9E2` (sky-blue
   darkened 6%), as `colors.primary-hover`. Upstream token:
   `--color-brand-hover`.
2. **Other variants keep a shared rule:** darken ~6% on hover. No hover
   tokens for `secondary`, `outline`, `ghost` or `danger`.
3. **Shadows go in a new `shadows` front-matter group,** with the prose naming
   the tokens instead of restating values. The pinned linter
   (`@google/design.md` 0.4.0) accepts a `shadows` group with 0 errors and 0
   warnings (checked on a throwaway copy; not confirmed as part of the
   format).
4. **Use the upstream shadow values** (Finding 2). They replace the ranges in
   the prose.
5. **Tokenise the focus ring** as `shadows.focus`, with the exact upstream
   value. Leave the modal scrim as it is.

### Findings from Claude Design (read-only, 2026-11-10)

Read from project `875c59c0-39ca-4f76-b742-061041f7f2ac` before the move to
Claude.

1. **Hover darkens in code; the prose said brighten.**
   `components/actions/Button.jsx` set `filter: brightness(0.94)` on hover for
   every variant, a 6% darkening. Our `DESIGN.md` Motion prose and the
   project's `readme.md` Motion section both said "brighten ~6% on hover". The
   project's readme also says solid buttons get "a small brightness drop" on
   hover, which matches the code. `#36C5F0` multiplied by 0.94 per channel is
   about `#33B9E2` (approved in Decision 1).
2. **Shadows are exact tokens upstream** (`tokens/spacing.css`):

   | Token | Upstream value |
   | --- | --- |
   | `--shadow-xs` | `0 1px 2px rgba(44, 55, 60, 0.06)` |
   | `--shadow-sm` | `0 1px 3px rgba(44, 55, 60, 0.08), 0 1px 2px rgba(44, 55, 60, 0.06)` |
   | `--shadow-md` | `0 4px 12px rgba(44, 55, 60, 0.08), 0 2px 4px rgba(44, 55, 60, 0.05)` |
   | `--shadow-lg` | `0 12px 32px rgba(44, 55, 60, 0.12), 0 4px 8px rgba(44, 55, 60, 0.06)` |
   | `--shadow-focus` | `0 0 0 3px rgba(54, 197, 240, 0.35)` |

   `md`'s second layer (`0.05`) and `lg`'s first layer (`32px` blur) fall
   outside the old prose ranges. Every xs–lg layer uses the gunmetal tint.

## Part A: upstream change (done 2026-11-10)

Made in the Claude Design project by Tim, then checked read-only by Claude
Code on 2026-11-10:

- `tokens/colors.css`: added `--color-brand-hover: #33B9E2;` under Semantic
  aliases.
- `components/actions/Button.jsx`: on hover, the primary variant uses
  `var(--color-brand-hover)` for background and border. Other variants keep
  `filter: brightness(0.94)`.
- `readme.md`: the Motion line now says "darken \~6% on hover (brightness
  0.94; primary buttons use --color-brand-hover)".
- Shadows, focus ring and modal scrim: unchanged, as decided.

| Token | Value |
| --- | --- |
| `colors.primary-hover` | `#33B9E2` |
| `shadows.xs` | `0 1px 2px rgba(44, 55, 60, 0.06)` |
| `shadows.sm` | `0 1px 3px rgba(44, 55, 60, 0.08), 0 1px 2px rgba(44, 55, 60, 0.06)` |
| `shadows.md` | `0 4px 12px rgba(44, 55, 60, 0.08), 0 2px 4px rgba(44, 55, 60, 0.05)` |
| `shadows.lg` | `0 12px 32px rgba(44, 55, 60, 0.12), 0 4px 8px rgba(44, 55, 60, 0.06)` |
| `shadows.focus` | `0 0 0 3px rgba(54, 197, 240, 0.35)` |

**Claude Code checks before going further.** Stop and report if any check
fails:

- No `<…>` placeholder remains in Part B.
- `primary-hover` is a 6-digit hex and differs from `#36C5F0`.
- Each `xs` to `lg` shadow uses the gunmetal tint `rgba(44, 55, 60, …)`.
- Each value in Part B matches the table above exactly.

## Part B: source edits (`systems/aot/DESIGN.md`)

Each find string must match exactly once.

**B1. Hover colour token.** Find:
```
  primary: "#36C5F0"          # sky-blue — signature, the triangle
```
Replace:
```
  primary: "#36C5F0"          # sky-blue — signature, the triangle
  primary-hover: "#33B9E2"    # sky-blue darkened 6% — primary button hover
```

**B2. Primary button hover.** Find:
```
  button-primary-hover:
    backgroundColor: "{colors.primary}"
```
Replace:
```
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
```

**B3. Shadow tokens.** Find:
```
  3xl: 64px
components:
```
Replace:
```
  3xl: 64px
shadows:
  xs: "0 1px 2px rgba(44, 55, 60, 0.06)"
  sm: "0 1px 3px rgba(44, 55, 60, 0.08), 0 1px 2px rgba(44, 55, 60, 0.06)"
  md: "0 4px 12px rgba(44, 55, 60, 0.08), 0 2px 4px rgba(44, 55, 60, 0.05)"
  lg: "0 12px 32px rgba(44, 55, 60, 0.12), 0 4px 8px rgba(44, 55, 60, 0.06)"
  focus: "0 0 0 3px rgba(54, 197, 240, 0.35)"
components:
```

**B4. Elevation prose.** Find:
```
Resting cards use `xs`/`sm`
(`0 1px 2–3px rgba(44,55,60,.06–.08)`); overlays and hovers lift to `md`/`lg`
(`0 4–12px rgba(44,55,60,.08–.12)`). Focus is a **3px sky-blue ring**
(`0 0 0 3px rgba(54,197,240,.35)`).
```
Replace:
```
Resting cards use `{shadows.xs}`/`{shadows.sm}`; overlays and hovers lift to
`{shadows.md}`/`{shadows.lg}`. Focus is a **3px sky-blue ring**
(`{shadows.focus}`). Use these values exactly.
```

**B5. Hover prose.** Find:
```
press and brighten ~6% on hover;
```
Replace:
```
press. On hover, primary buttons use `{colors.primary-hover}`; other variants
darken ~6%;
```

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system.
3. `git diff systems/aot/DESIGN.md`. Expect exactly:
   - one added `primary-hover` colour (B1);
   - `button-primary-hover` background changed to `{colors.primary-hover}`
     (B2);
   - a new `shadows` group with five values (B3);
   - the Elevation & Depth and Motion prose edits (B4, B5).

   Report anything else. The plugin copy under `plugins/aot-design/` should
   show the same diff.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- Hover tokens for `secondary`, `outline`, `ghost` and `danger` buttons
  (Decision 2).
- Pressed and disabled states as tokens.
- The modal scrim range (Decision 5).
- formsflow.ai: a separate system, with its own shadows. Not affected.
