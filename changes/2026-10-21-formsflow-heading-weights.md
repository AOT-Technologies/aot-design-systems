# Change request: heading weights

- **ID:** 2026-10-21-formsflow-heading-weights
- **System:** formsflow
- **Requested by:** Tim
- **Status:** pending
- **Touches:** `systems/formsflow/src/semantic.json`, `systems/formsflow/src/DESIGN.prose.md`
- **Follows:** `2026-10-21-formsflow-line-height-and-email` (applied and merged).
  The find strings below match the text that request merged.

## Why

`DESIGN.md` sets the default weight of `h1`, `h2` and `h3` to medium (500).
zeroheight's Typography page assigns semibold (600) to headings and keeps
medium for emphasis within body text, active navigation and component states,
and selected items. The medium mapping came from the July session, and
zeroheight is the source of truth for this.

The Email section merged in the previous request was written on the medium
assumption. It presents semibold email headings as an exception to the
product's heading weight. Once headings are semibold everywhere, that framing
is wrong.

## Decisions (Tim, 2026-10-21)

1. zeroheight is right: `h1`, `h2` and `h3` default to semibold (600).
2. `max1` stays at medium (500), as the first step of the display weight
   curve. `max2` to `max6` are unchanged.
3. The email note is reframed. It now explains why email avoids medium and
   light, rather than justifying semibold as an exception.

## Part A: upstream change

None. Default weights are a design decision recorded in `src/semantic.json`,
not a Figma token value. Every size already exports all four weight variants,
so `tokens/` doesn't change.

## Part B: source edits

Each find string must match exactly once.

**B1. Default heading weights** (`systems/formsflow/src/semantic.json`).
Find:
```
    "h3": "medium",
    "h2": "medium",
    "h1": "medium",
```
Replace:
```
    "h3": "semibold",
    "h2": "semibold",
    "h1": "semibold",
```

**B2. Default weights prose** (`systems/formsflow/src/DESIGN.prose.md`).
Find:
```
`body` = regular (400); `h3` / `h2` / `h1` / `max1` = medium (500); `max2`–`max5` =
```
Replace:
```
`body` = regular (400); `h3` / `h2` / `h1` = semibold (600); `max1` = medium (500); `max2`–`max5` =
```

**B3. Email weights and note** (`systems/formsflow/src/DESIGN.prose.md`, in
`## Email`).
Find:
```
**Weights.** Headings use the semibold variants (`h1-semibold`, `h2-semibold`,
`h3-semibold`); all other text uses regular (400). Don't use light (300) or
medium (500) in email.

**Why email headings are semibold.** Product headings default to medium (500),
but email can't rely on Figtree loading: Gmail and Outlook for Windows show a
fallback font, and those fallbacks only have regular and bold. Medium falls back
to regular, so headings would match body text and the hierarchy flattens.
Semibold falls back to bold, so headings stay distinct in every client. Where
Figtree does load, email headings look slightly heavier than in the product.
That trade-off is deliberate: a reliable hierarchy in every inbox matters more
than an exact weight match with the product.
```
Replace:
```
**Weights.** Headings use their default semibold tokens (`h1`, `h2`, `h3`);
all other text uses regular (400). Don't use light (300) or medium (500) in
email.

**Why email avoids medium and light.** Email can't rely on Figtree loading:
Gmail and Outlook for Windows show a fallback font, and those fallbacks only
have regular and bold. Medium and light fall back to regular, so a medium
heading would match body text and the hierarchy flattens. Semibold, the
standard heading weight, falls back to bold, so headings stay distinct in every
client.
```

## Part C: build and verify

1. `make build SYSTEM=formsflow`, then `make verify`. Every check must pass,
   with 0 errors and 0 warnings.
2. Check the diff with `git diff systems/formsflow/DESIGN.md`. Expect exactly:
   - `h1`, `h2` and `h3`: `fontWeight` 500 → 600, and `fontFamily`
     `"'Figtree', 'Figtree-Medium'"` → `"'Figtree'"`;
   - `max1` and every other token unchanged, including all `lineHeight` values;
   - the prose edits B2 and B3.

   Report anything else as unexpected.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[formsflow]`.
2. Set **Status** above to `applied` with the date.
3. Summarise and wait for approval, then open a PR (per `CLAUDE.md`).

## Out of scope

- zeroheight Foundations › Email: already corrected directly. Its weights note
  now matches B3.
- zeroheight Foundations › Typography: already says semibold for headings, so
  no change is needed.
- `max2` to `max6` weights.
