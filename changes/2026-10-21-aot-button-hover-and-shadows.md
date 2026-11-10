# Change request: primary button hover colour and shadow values

- **ID:** 2026-10-21-aot-button-hover-and-shadows
- **System:** aot
- **Requested by:** Tim
- **Status:** draft
- **Touches:** `systems/aot/DESIGN.md` (front matter and prose)

## Why

Two gaps make agents guess values:

1. **Primary button hover.** `button-primary-hover` uses `{colors.primary}`,
   the same background as `button-primary`, so the hover state is identical to
   rest. The only guidance is in the Motion prose ("brighten ~6% on hover"),
   which no colour token backs.
2. **Shadows.** Elevation & Depth gives the `xs` to `lg` levels only as ranges
   (`0 1px 2–3px rgba(44,55,60,.06–.08)` and `0 4–12px
   rgba(44,55,60,.08–.12)`). There are no shadow tokens, so each agent picks
   its own value inside the range.

The correct values live upstream in the AOT Technologies Design System (Claude
Design project `875c59c0-39ca-4f76-b742-061041f7f2ac`).

## Decisions

1. **Open:** does hover darken or brighten, and what are the hover colour's
   exact hex and token name? Part B assumes `colors.primary-hover`. See
   Finding 1: the upstream Button darkens, but the prose here and upstream
   says "brighten".
2. **Open:** do the other button variants (`secondary`, `outline`, `ghost`,
   `danger`) get hover tokens in this request, or keep a shared rule? Part B
   assumes they keep the rule, and lists them under Out of scope. Finding 1
   applies: the upstream Button uses the same hover filter on every variant.
3. **Open:** where the shadow values live. Part B assumes a new `shadows` group
   in the front matter (`xs`, `sm`, `md`, `lg`), with the prose naming the
   tokens instead of restating values. The pinned linter (`@google/design.md`
   0.4.0) accepts a `shadows` group with 0 errors and 0 warnings. That was
   checked on a throwaway copy, and it isn't confirmed as part of the format.
   The alternative is exact values in the prose only.
4. **Open:** confirm that the upstream shadow values in Finding 2 replace the
   ranges in the prose. Some layers fall outside those ranges.
5. **Open:** the focus ring (already exact, and a token upstream; see
   Finding 2) and the modal scrim (still a range, `rgba(44,55,60,.35–.4)`):
   tokenise them here, or leave them? Part B leaves both as they are.

### Findings from Claude Design (read-only, 2026-11-10)

Read from project `875c59c0-39ca-4f76-b742-061041f7f2ac` before the move to
Claude. A person still confirms each value upstream (Part A).

1. **Hover darkens in code; the prose says brighten.**
   `components/actions/Button.jsx` sets `filter: brightness(0.94)` on hover
   for every variant, a 6% darkening. Our `DESIGN.md` Motion prose and the
   project's `readme.md` Motion section both say "brighten ~6% on hover". The
   project's readme also says solid buttons get "a small brightness drop" on
   hover, which matches the code. No hover colour token exists upstream. For
   reference only: `#36C5F0` multiplied by 0.94 per channel is about
   `#33B9E2`. That isn't an approved value; Decision 1 sets the real one.
2. **Shadows are exact tokens upstream** (`tokens/spacing.css`):

   | Token | Upstream value |
   | --- | --- |
   | `--shadow-xs` | `0 1px 2px rgba(44, 55, 60, 0.06)` |
   | `--shadow-sm` | `0 1px 3px rgba(44, 55, 60, 0.08), 0 1px 2px rgba(44, 55, 60, 0.06)` |
   | `--shadow-md` | `0 4px 12px rgba(44, 55, 60, 0.08), 0 2px 4px rgba(44, 55, 60, 0.05)` |
   | `--shadow-lg` | `0 12px 32px rgba(44, 55, 60, 0.12), 0 4px 8px rgba(44, 55, 60, 0.06)` |
   | `--shadow-focus` | `0 0 0 3px rgba(54, 197, 240, 0.35)` |

   `md`'s second layer (`0.05`) and `lg`'s first layer (`32px` blur) fall
   outside the prose ranges. Every layer uses the gunmetal tint.

## Part A: upstream change (a person does this first)

In the Claude Design project, confirm or define these values, then write them
into this request in place of the `<…>` placeholders in Part B:

| Token | Expected value |
| --- | --- |
| `colors.primary-hover` | `<hex>`: sky-blue `#36C5F0` darkened or brightened ~6%, per Decision 1 |
| `shadows.xs` | `<box-shadow>`: upstream `--shadow-xs` (Finding 2), once confirmed |
| `shadows.sm` | `<box-shadow>`: upstream `--shadow-sm` (Finding 2), once confirmed |
| `shadows.md` | `<box-shadow>`: upstream `--shadow-md` (Finding 2), once confirmed |
| `shadows.lg` | `<box-shadow>`: upstream `--shadow-lg` (Finding 2), once confirmed |

**Claude Code checks before going further.** Stop and report if any check
fails:

- No `<…>` placeholder remains in Part B.
- `primary-hover` is a 6-digit hex and differs from `#36C5F0`.
- Each shadow uses the gunmetal tint `rgba(44,55,60,…)`.

## Part B: source edits (`systems/aot/DESIGN.md`)

Each find string must match exactly once.

**B1. Hover colour token.** Find:
```
  primary: "#36C5F0"          # sky-blue — signature, the triangle
```
Replace:
```
  primary: "#36C5F0"          # sky-blue — signature, the triangle
  primary-hover: "<hex>"      # sky-blue hover (Claude Design)
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
  xs: "<box-shadow>"
  sm: "<box-shadow>"
  md: "<box-shadow>"
  lg: "<box-shadow>"
components:
```

**B4. Elevation prose.** Find:
```
Resting cards use `xs`/`sm`
(`0 1px 2–3px rgba(44,55,60,.06–.08)`); overlays and hovers lift to `md`/`lg`
(`0 4–12px rgba(44,55,60,.08–.12)`).
```
Replace:
```
Resting cards use `{shadows.xs}`/`{shadows.sm}`; overlays and hovers lift to
`{shadows.md}`/`{shadows.lg}`. Use these values exactly.
```

**B5. Hover prose.** Find:
```
press and brighten ~6% on hover;
```
Replace:
```
press. On hover, primary buttons use `{colors.primary-hover}`; other variants
brighten ~6%;
```

The B5 replacement says "brighten". If Decision 1 settles on darken, update it
to match before this request is approved.

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system.
3. `git diff systems/aot/DESIGN.md`. Expect exactly:
   - one added `primary-hover` colour (B1);
   - `button-primary-hover` background changed to `{colors.primary-hover}`
     (B2);
   - a new `shadows` group with four values (B3);
   - the Elevation & Depth and Motion prose edits (B4, B5).

   Report anything else.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- Hover tokens for `secondary`, `outline`, `ghost` and `danger` buttons
  (unless Decision 2 brings them in).
- Pressed, focus and disabled states as tokens.
- The modal scrim range and the focus ring (unless Decision 5 brings them in).
- formsflow.ai: a separate system, with its own shadows. Not affected.
