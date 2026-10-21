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

1. **Open:** the hover colour's exact hex, and its token name. Part B assumes
   `colors.primary-hover`.
2. **Open:** do the other button variants (`secondary`, `outline`, `ghost`,
   `danger`) get hover tokens in this request, or keep the "brighten ~6%" rule?
   Part B assumes they keep the rule, and lists them under Out of scope.
3. **Open:** where the shadow values live. Part B assumes a new `shadows` group
   in the front matter (`xs`, `sm`, `md`, `lg`), with the prose naming the
   tokens instead of restating values. The pinned linter (`@google/design.md`
   0.4.0) accepts a `shadows` group with 0 errors and 0 warnings. That was
   checked on a throwaway copy, and it isn't confirmed as part of the format.
   The alternative is exact values in the prose only.
4. **Open:** the exact `xs`, `sm`, `md` and `lg` shadow values.
5. **Open:** the focus ring (already exact) and the modal scrim (still a
   range, `rgba(44,55,60,.35–.4)`): tokenise them here, or leave them? Part B
   leaves both as they are.

## Part A: upstream change (a person does this first)

In the Claude Design project, confirm or define these values, then write them
into this request in place of the `<…>` placeholders in Part B:

| Token | Expected value |
| --- | --- |
| `colors.primary-hover` | `<hex>`: sky-blue `#36C5F0` brightened ~6% |
| `shadows.xs` | `<box-shadow>`: within `0 1px 2–3px rgba(44,55,60,.06–.08)` |
| `shadows.sm` | `<box-shadow>`: within `0 1px 2–3px rgba(44,55,60,.06–.08)` |
| `shadows.md` | `<box-shadow>`: within `0 4–12px rgba(44,55,60,.08–.12)` |
| `shadows.lg` | `<box-shadow>`: within `0 4–12px rgba(44,55,60,.08–.12)` |

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

## Part C: build and verify

1. aot: no build step.
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
