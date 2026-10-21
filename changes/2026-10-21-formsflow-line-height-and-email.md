# Change request: line heights and email guidance

- **ID:** 2026-10-21-formsflow-line-height-and-email
- **System:** formsflow
- **Requested by:** Tim
- **Status:** applied (2026-10-21)
- **Touches:** `systems/formsflow/tokens/typography.json` (via Figma), `systems/formsflow/src/DESIGN.prose.md`

## Why

`DESIGN.md` sets `lineHeight: 1` on every size. zeroheight (Foundations ›
Typography) defines real line heights, and 1.0 reads far too tightly in running
text. `DESIGN.md` also has no email guidance: no fallback font stack and no
container width.

## Decisions (Tim, 2026-10-21)

1. Correct `DESIGN.md` to zeroheight's line heights, fixed at the source in
   Figma. For `max5` and `max6`, which zeroheight doesn't define, follow the
   +8px pattern of the other display sizes: 72px and 88px.
2. Email headings use semibold (600) instead of the product default, medium
   (500). This is an accepted trade-off, and a dedicated note explains it.
3. Notification emails sent by customers' formsflow workflows are out of
   scope, with a specific note saying so.
4. Source Serif 4 isn't used in email.

The four parts below are one change. Don't merge Part B without Part A: the
new prose describes per-size line heights.

## Part A: tokens (a person does this first)

1. In Figma, set the line height in **px** on every text style. All four weight
   variants of a size share its value:

   | Size | Font size | Line height |
   | --- | --- | --- |
   | `caption` | 12px | 16px |
   | `body-sml` | 14px | 20px |
   | `body` | 16px | 24px |
   | `h3` | 20px | 28px |
   | `h2` | 24px | 32px |
   | `h1` | 32px | 40px |
   | `max1` | 36px | 44px |
   | `max2` | 40px | 48px |
   | `max3` | 44px | 52px |
   | `max4` | 48px | 56px |
   | `max5` | 64px | 72px |
   | `max6` | 80px | 88px |

2. Export the text styles as before and replace
   `systems/formsflow/tokens/typography.json`.

**Claude Code checks before going further.** Stop and report if any check fails:

- Every style's `line-height` matches the table, in px:
  ```
  python3 -c "import json;E={'caption':16,'body-sml':20,'body':24,'h3':28,'h2':32,'h1':40,'max1':44,'max2':48,'max3':52,'max4':56,'max5':72,'max6':88};S=json.load(open('systems/formsflow/tokens/typography.json'))['ff']['text-style']['sans'];bad=[n for n,s in S.items() if s['line-height']['value']!=f\"{E[n.rsplit('-',1)[0]]}px\"];print('OK' if not bad else bad)"
  ```
- Compared with the previous export, nothing changed except line heights
  (`git diff systems/formsflow/tokens/typography.json`). If the export's structure differs from
  the bootstrapped file, see the bootstrap note in `CLAUDE.md`.

## Part B: prose edits (`systems/formsflow/src/DESIGN.prose.md`)

Each find string must match exactly once.

**B1. Size count.**
Find: `Single family: **Figtree**, a 10-size scale.`
Replace: `Single family: **Figtree**, a 12-size scale.`

**B2. Weight variants.** The find string spans a line break.
Find:
```
They share their size's `fontSize` and
`lineHeight: 1`; only
```
Replace:
```
They share their size's `fontSize` and
`lineHeight`; only
```

**B3. Line-height rule.**
Find:
```
**Line-height is intentionally `1.0` across the entire scale** — apply it as given; do not loosen it.
```
Replace:
```
**Each size carries its own line-height** in the front matter. Apply it as given;
don't loosen, tighten or round it.
```

**B4. New Email section.** Insert immediately before `## Do's and Don'ts`,
followed by one blank line:

````markdown
## Email

Applies to HTML emails that formsflow.ai sends: marketing, trial and onboarding
lifecycle, and account notifications.

**Out of scope: workflow notification emails.** Emails that customers' formsflow
workflows send (approval requests, submission confirmations and similar) are not
covered. They can carry a customer's own branding, which needs separate font and
colour rules. Don't apply this section to them; flag the gap instead.

**Font stack.** Use exactly:
`font-family: 'Figtree', 'Helvetica Neue', Helvetica, Arial, sans-serif;`
This is the only sanctioned fallback stack: it adds fallbacks, not brand
families. Load Figtree with a Google Fonts `<link>` in the `<head>`. Add an
`<!--[if mso]>` style block that sets `font-family: Arial, sans-serif` on text
elements, so Outlook for Windows doesn't fall back to Times New Roman. Never use
`'Figtree-Regular'` or `'Figtree-Medium'` in email; they are design-tool names
and won't resolve. Email is Figtree-only.

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

**Sizes.** Use only `caption`, `body-sml`, `body`, `h3`, `h2` and `h1`; no `max`
sizes. Apply each token's px line-height as given, with
`mso-line-height-rule: exactly` so Outlook respects it.

**Container.** 600px maximum width, centred, fluid at 100% below that. Side
padding uses spacing step `6` (24px), dropping to `4` (16px) at 600px and below.
Use `6` (24px) between blocks and `8` (32px) between sections.
````

## Part C: build and verify

1. `make build SYSTEM=formsflow`, then `make verify`. Every check must pass,
   with 0 errors and 0 warnings.
2. Check the diff with `git diff systems/formsflow/DESIGN.md`. Expect exactly:
   - 12 front-matter `lineHeight` values changing from `1` to px (24 diff
     lines);
   - the prose edits B1 to B4.

   Report anything else as unexpected.

## Part D: record

1. Add an entry to `CHANGELOG.md`.
2. Set **Status** above to `applied` with the date.
3. Summarise and wait for approval, then open a PR (per `CLAUDE.md`).

## Out of scope (tracked separately)

- The zeroheight Foundations › Email page.
- Rules for workflow notification emails.
- Reconciling Source Serif 4: zeroheight lists it, `DESIGN.md` says Figtree
  only.
- zeroheight's Typography page has no `max5`/`max6` rows and still says 10
  sizes.
