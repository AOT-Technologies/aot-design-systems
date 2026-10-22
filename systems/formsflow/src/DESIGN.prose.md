## Overview

This file is the single reference an agent should load before generating or
modifying any formsflow UI or copy — marketing pages and product surfaces alike.
Token values in the front matter are authoritative and generated from source; the
guidance below tells an agent how to apply them.

The front matter carries only the **semantic defaults** — the tokens meant to be
referenced directly (`primary` / `primary-hover` / `on-primary`, and one default
type token per size). The underlying **primitive colour ramps** and the explicit
**type-weight variants** are documented in prose (under Colors and Typography
below); they are the source palette semantics are drawn from, not everyday tokens.

formsflow.ai is a forms-and-workflow platform: users build digital forms that
connect to automated workflows, turning manual processes into streamlined
operations (form building + workflow automation + task management in one product).
It is an independent brand — it shares visual elements with parent company AOT
Technologies but keeps its own identity and voice. Present formsflow as its own
brand; do not fold in AOT's identity or voice.

**Archetype: the Magician.** Lead with *outcomes* (what the product does for the
user), never *activity* (what the user does in the product). Implied promise:
"Tell us what you need and we'll make it happen." The value is the transformation —
a form connects to a workflow that automates a process — not any single feature.

**Positioning.** There is no like-for-like competitor. Compete on the transformation
the integrated product delivers, not on individual features; do not position against
form builders or BPA platforms head-to-head.

**Voice** — make transformation feel effortless, understandable, and trustworthy:
- *Make complexity disappear* — describe what the product enables, not how it works;
  stay abstract where needed; no jargon or proprietary terms.
- *Be quietly powerful* — calm confidence, no hype or exaggeration; earn trust
  through restraint and predictability.
- *Lead with outcomes* — translate every capability into a felt result, specific to
  the reader (form creator, reviewer, or administrator).

## Brand naming

- **Canonical name: `formsflow.ai`** — lowercase, with the `.ai` suffix. Use it in
  all formal contexts. The **first reference** on any page or document must use the
  full name. Keep it lowercase even at the start of a sentence; never capitalise to
  "Formsflow".
- **Alternative name: `formsflow`** — allowed in running text (blog posts, articles,
  documentation, conversation) *after* the full name has been established. On pages
  where the full logo is present, `formsflow` may be used throughout the copy. Prefer
  it wherever the `.ai` suffix makes phrasing awkward or interrupts readability.
- **Don't** use the alternative name alone in legal, contractual, or formal brand
  contexts (press releases, partnership announcements) — use `formsflow.ai` there.
- **Auto-link gotcha:** many editors detect the `.ai` suffix and auto-format
  `formsflow.ai` as a hyperlink. Always review copy and clear any unintended link
  styling.

## Logo

The full logo has two elements:

- **Logomark** — the circular-arrows-and-checkmark icon. May be used independently as
  an app icon or favicon.
- **Wordmark** — `formsflow.ai` set in the brand typeface (Figtree). Always appears
  alongside the logomark in the full logo. Don't recreate the wordmark in another
  typeface.

**Do** maintain clear spacing around the logo. **Don't** separate, rearrange, or
recolour the logo components.

**Logo assets are fixed binaries — never synthesized.** The logomark and wordmark
are supplied files, not tokens in this system. Do not generate, redraw, trace,
vectorize, recolour, or "approximate" either mark, and do not recreate the wordmark
by setting `formsflow.ai` in Figtree (or any typeface) — the wordmark is a specific
lockup, not live text. **If the logo asset is unavailable, do not invent one:** leave
a labelled placeholder (e.g. `[formsflow.ai logo]`) and flag the missing asset, per
the token-gap rule in Do's and Don'ts.

## Colors

The palette is a **primitive ramp** across ten families. `gray` has 13 steps
(`gray-50` → `gray-950`, plus `gray-white`): surfaces, borders, dividers, text. The
nine chromatic families (`yellow`, `red`, `blue`, `indigo`, `green`, `orange`,
`cyan`, `purple`, `pink`) each have 7 steps — `50`/`100` (tints/surfaces),
`300`/`500` (mid), `700`/`900` (saturated, most brand-forward), `shade` (darkest,
for pressed/hover-dark states).

**Primitive ramp values.** These are the source primitives — reference the semantic
roles below (or the `gray` ramp for neutrals) in UI, not raw hexes:

```
gray     50 #FCFCFC · 100 #F6F6F6 · 150 #F0F0F0 · 200 #E5E5E5 · 300 #D1D2D3 · 400 #B7B7B8 · 500 #979899 · 600 #7C7D7F · 700 #636365 · 800 #4A4A4A · 900 #2E2E30 · 950 #1C1C1E · white #FFFFFF
yellow   50 #FEFCF7 · 100 #FDF7EA · 300 #FAECCB · 500 #F6D896 · 700 #F1C562 · 900 #ECB22E · shade #B88B24
red      50 #FCF4F4 · 100 #F9EAEA · 300 #F1C9C9 · 500 #E29494 · 700 #D45E5E · 900 #C62828 · shade #9A1F1F
blue     50 #F7FAFC · 100 #EAF3F8 · 300 #CBE2ED · 500 #97C4DB · 700 #63A7C9 · 900 #2F8AB7 · shade #256C8F
indigo   50 #F4F5FF · 100 #E8EBFF · 300 #C6CCFE · 500 #8D9AFD · 700 #5467FC · 900 #1B34FB · shade #1529C4
green    50 #F7FCFA · 100 #EAF8F2 · 300 #CBEDDE · 500 #96DABE · 700 #62C89E · 900 #2EB67D · shade #248E62
orange   50 #FFFBF5 · 100 #FFF6E6 · 300 #FFE8BF · 500 #FFD080 · 700 #FFB840 · 900 #FFA100 · shade #C77E00
cyan     50 #F5FBFD · 100 #E7F6FB · 300 #C2E8F4 · 500 #85D2EA · 700 #48BCDF · 900 #0BA5D4 · shade #0981A5
purple   50 #FBF7FF · 100 #F6EAFE · 300 #E8CCFC · 500 #D198FA · 700 #BA64F8 · 900 #A331F5 · shade #7F26BF
pink     50 #FEF6F8 · 100 #FCE8EE · 300 #F7C7D6 · 500 #F08EAC · 700 #E85683 · 900 #E01E5A · shade #AF1746
```

**Semantic roles are set.** Use these — never a raw hex — for interactive and
brand surfaces (only these live in the front matter):

- **`primary`** = `indigo-900` (`#1B34FB`) — brand/action colour.
- **`primary-hover`** = `indigo-shade` (`#1529C4`) — hover/pressed on primary.
- **`on-primary`** = `gray-white` (`#FFFFFF`) — text/icons on a primary fill.

Take neutrals from the `gray` ramp (`gray-50`/`gray-white` lightest surfaces,
`gray-800` primary text).

## Typography

Single family: **Figtree**, a 12-size scale. Sizes (px): `caption` 12 · `body-sml`
14 · `body` 16 · `h3` 20 · `h2` 24 · `h1` 32 · `max1` 36 · `max2` 40 · `max3` 44 ·
`max4` 48 · `max5` 64 · `max6` 80.

- `body*` / `caption` / `body-sml` — running text, labels, metadata.
- `h1`–`h3` — in-product headings and section titles.
- `max1`–`max6` — display sizes; reserve for marketing hero/landing headlines.

**Default weights (the front-matter tokens).** Each size carries one default weight,
and only that default token lives in the front matter: `caption` / `body-sml` /
`body` = regular (400); `h3` / `h2` / `h1` = semibold (600); `max1` = medium (500); `max2`–`max5` =
regular (400); `max6` = light (300). Weight lightens as display sizes grow, since
size itself carries the emphasis. Use these semantic tokens (`body`, `h1`, …) — they
encode the defaults above.

**Explicit weight variants (prose only).** Every size also has four weight variants
— `-light` (300), `-regular` (400), `-medium` (500), `-semibold` (600), e.g.
`body-semibold`, `h1-light`, `max6-regular`. They share their size's `fontSize` and
`lineHeight`; only `fontWeight` (and `fontFamily`) changes. The `fontFamily` is
`'Figtree'` for `-light` and `-semibold`, `'Figtree', 'Figtree-Medium'` for
`-medium`, and `'Figtree', 'Figtree-Regular'` for `-regular`. These are kept out of
the front matter — reach for them only for deliberate overrides of a size's default.

**Each size carries its own line-height** in the front matter. Apply it as given;
don't loosen, tighten or round it.

**Casing & emphasis** (not brand-specified — interim default for consistency):
sentence case for all headings and UI text; avoid ALL CAPS except short labels or
eyebrows; use bold sparingly for emphasis and italic rarely. Replace this line if a
rule is added to zeroheight.

## Layout & Spacing

Spacing is a **4px base scale**. Step *names* are indices with gaps
(`0,1,2,3,4,5,6,8,10,12,16`) and are not the pixel values — the value is the px:
`1`=4 · `2`=8 · `3`=12 · `4`=16 · `5`=20 · `6`=24 · `8`=32 · `10`=40 · `12`=48 ·
`16`=64. Use only these steps for padding, gaps, and margins; snap to the nearest
defined step rather than inventing in-between values.

Lay out on an **8px grid**: align elements and size components to 8px increments,
using the 4px base scale for finer adjustments within that grid.

<!-- ADD WHEN AVAILABLE: grid/breakpoint tokens, container max-widths, section rhythm. -->

## Elevation & Depth

Shadows are gray-950-tinted (`#1C1C1E`), layered ambient + direct, low alpha:

- `shadow-sm` — `0 1px 2px rgba(28,28,30,.06), 0 1px 3px rgba(28,28,30,.10)` — cards, resting surfaces.
- `shadow-md` — `0 2px 4px rgba(28,28,30,.06), 0 4px 8px rgba(28,28,30,.08)` — dropdowns, popovers.
- `shadow-lg` — `0 4px 8px rgba(28,28,30,.08), 0 12px 24px rgba(28,28,30,.25)` — modals, overlays (higher alpha for the stronger modal separation).
- `shadow-focus` — `0 0 0 3px rgba(27,52,251,.35)` — focus ring, tinted to `primary` (indigo-900).

Prefer the lightest level that reads; don't stack shadows or invent new ones.

## Shapes

Radius scale (see `rounded` in the front matter): `none` 0 · `sm` 3px (subtle) ·
`md` 5px (**default for all components**) · `pill` 25px (**buttons and rounded
elements**) · `full` 9999px (**genuine circular elements** — avatars, status dots,
icon buttons — where `pill` isn't enough). Don't introduce radii outside these five.

## Components

- **button-primary** — bg `primary`, text `on-primary`, radius `pill`, padding `12px 20px`.
- **button-primary (hover/pressed)** — bg `primary-hover`.
- **card** — surface `gray-white`, border `1px gray-200`, radius `md`, `shadow-sm`.
- **input** — surface `gray-white`, border `1px gray-300`, radius `md`; on focus add `shadow-focus`.

## Email

Applies to HTML emails that formsflow.ai sends: marketing, onboarding lifecycle,
and account notifications.

**Out of scope: workflow notification emails.** Emails that customers' formsflow
workflows send (approval requests, submission confirmations and similar) are not
covered. They can carry a customer's own branding, which needs separate font and
colour rules. Don't apply this section to them; flag the gap instead.

**Font stack.** Use exactly, on every text element:
`font-family: 'Figtree', 'Helvetica Neue', Helvetica, Arial, sans-serif;`
This is the only sanctioned fallback stack: it adds fallbacks, not brand
families. Load Figtree with a Google Fonts `<link>` in the `<head>`. Outlook for
Windows can ignore the whole stack when the first font is a web font and fall
back to Times New Roman, so add this conditional style exactly:
`<!--[if mso]><style>body, table, td, p, a, h1, h2, h3 { font-family: Arial, sans-serif !important; }</style><![endif]-->`
Never use
`'Figtree-Regular'` or `'Figtree-Medium'` in email; they are design-tool names
and won't resolve. Email is Figtree-only.

**Weights.** Headings use their default semibold tokens (`h1`, `h2`, `h3`);
all other text uses regular (400). Don't use light (300) or medium (500) in
email.

**Why email avoids medium and light.** Email can't rely on Figtree loading:
Gmail and Outlook for Windows show a fallback font, and those fallbacks only
have regular and bold. Medium and light fall back to regular, so a medium
heading would match body text and the hierarchy flattens. Semibold, the
standard heading weight, falls back to bold, so headings stay distinct in every
client.

**Sizes.** Use only `caption`, `body-sml`, `body`, `h3`, `h2` and `h1`; no `max`
sizes. Use `h1` for the headline, once per email; `h2` for subheadings; `h3`
for section headings; `body` for default text; `body-sml` for secondary text
and metadata; and `caption` for the footer, legal text and unsubscribe link.
Apply each token's px line-height as given, with
`mso-line-height-rule: exactly` so Outlook respects it.

**Container.** 600px maximum width, centred, fluid at 100% below that. Side
padding uses spacing step `6` (24px), dropping to `4` (16px) at 600px and below.
Use `6` (24px) between blocks and `8` (32px) between sections.

## Do's and Don'ts

### Visual

**Do**
- Reference `primary` / `primary-hover` / `on-primary` for brand and interactive surfaces.
- Take neutrals from the `gray` ramp — never eyeball a grey or mix your own.
- Snap all spacing to the scale; use `pill` radius on buttons, `md` elsewhere.
- Use `max1`–`max4` for marketing display headlines; `h1`–`h3` inside the product.

**Don't**
- Don't use a colour that isn't in the palette; every formsflow colour has a token.
- Don't invent corner radii, shadows, or font families beyond what this file states.
- Don't generate, redraw, or recolour the logo — reference the supplied asset, or flag it as missing.
- Don't re-round or convert token values (px→rem, tightening line-height) — emit them exactly.
- If a token is missing for what you need, flag the gap rather than filling it.

### Content & voice

**Do**
- Lead with the problem being solved and the outcome achieved — not the feature or UI action.
- Describe the transformation (form → workflow → automation); connect forms to workflows early in any narrative.
- Write for process owners and people close to the business problem; every label, prompt, and message must be understandable on first read — no jargon or proprietary terms.
- Use progressive disclosure: an approachable entry point with depth on mastery; make the next step visible and inviting.
- Keep copy calm and quietly confident; let capabilities speak for themselves.

**Don't**
- Don't lead with features, tooling, or a list of UI actions.
- Don't treat forms and workflows as separate capabilities.
- Don't position against form builders or BPA platforms head-to-head.
- Don't use hype, exaggeration, or anything that surprises; don't surface how the engine works underneath.
- Don't fold in AOT Technologies' identity or voice.

<!-- Source: zeroheight brand > design principles + voice/tone. Naming and logo
     rules live in their own sections above. -->
