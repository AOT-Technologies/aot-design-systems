---
version: alpha
name: AOT Technologies
description: Brand and product design system for AOT Technologies.
colors:
  primary: "#36C5F0"          # sky-blue — signature, the triangle
  primary-hover: "#33B9E2"    # sky-blue darkened 6% — primary button hover
  on-primary: "#2C373C"       # gunmetal text on sky/amber
  secondary: "#2C373C"        # gunmetal — dark surfaces & solid controls
  on-secondary: "#FFFFFF"
  amber: "#ECB22E"            # yellow-red — the plus
  raspberry: "#E01E5A"        # the circle
  accent: "#2EB67D"           # sea-green — success accent
  surface: "#FFFFFF"
  surface-sunken: "#F5F6F7"   # app canvases & table headers
  surface-muted: "#ECEDEF"    # cultured
  text-primary: "#2C373C"
  text-secondary: "#696969"
  info-surface: "#E3F0F6"   # tint of blue-ncs #2F8AB7 (see Colors)
  success-surface: "#E4F5EE"
  warning-surface: "#FCF3DE"
  error-surface: "#FCE2EA"
typography:
  h1:
    fontFamily: Aron
    fontSize: 3rem            # 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.01em
  h2:
    fontFamily: Aron
    fontSize: 2.25rem         # 36px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.005em
  h3:
    fontFamily: Poppins
    fontSize: 1.75rem         # 28px
    fontWeight: 500
    lineHeight: 1.2
  body:
    fontFamily: Poppins
    fontSize: 1.125rem        # 18px
    fontWeight: 400
    lineHeight: 1.55
  caption:
    fontFamily: Poppins
    fontSize: 0.875rem        # 14px
    fontWeight: 300
    lineHeight: 1.45
  cta:
    fontFamily: Poppins
    fontSize: 1rem            # 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.06em
rounded:
  xs: 4px
  sm: 8px
  md: 10px
  lg: 16px
  xl: 24px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
shadows:
  xs: "0 1px 2px rgba(44, 55, 60, 0.06)"
  sm: "0 1px 3px rgba(44, 55, 60, 0.08), 0 1px 2px rgba(44, 55, 60, 0.06)"
  md: "0 4px 12px rgba(44, 55, 60, 0.08), 0 2px 4px rgba(44, 55, 60, 0.05)"
  lg: "0 12px 32px rgba(44, 55, 60, 0.12), 0 4px 8px rgba(44, 55, 60, 0.06)"
  focus: "0 0 0 3px rgba(54, 197, 240, 0.35)"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.cta}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.cta}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
  button-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.cta}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.cta}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
  button-danger:
    backgroundColor: "{colors.raspberry}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.cta}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  panel:
    backgroundColor: "{colors.surface-sunken}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  badge-neutral:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.text-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
  badge-brand:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
  badge-success:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
  badge-warning:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
  alert-info:
    backgroundColor: "{colors.info-surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  alert-success:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  alert-warning:
    backgroundColor: "{colors.warning-surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  alert-error:
    backgroundColor: "{colors.error-surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  tabs:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.cta}"
---

## Overview

AOT's identity is **geometric, optimistic and digital-first**. The icon is built from three simple
shapes in three primary colours — a **sky-blue triangle**, a **raspberry circle** and a
**yellow-red plus** — and those shapes double as standalone graphic elements. The tone is clear and
confident without being loud: clean Poppins UI, characterful Aron for display, generous rounding,
cool low-spread shadows, and lots of white space.

**Voice.** Plain, direct, second-person ("Sign in to your workspace"). Confident and helpful, never
jargon-heavy or salesy. Address the user as **you**; the product/company is **we**. No exclamation
marks in product UI, and **no emoji** — iconography is line-icon SVG only.

**Product naming — always lowercase.** AOT's products are stylized in lower case in *all* copy,
headings, labels and UI, even at the start of a sentence: **caseflow**, **formsflow**,
**formsflow.ai**, **node-wire**, **m8flow**, **delphi**. Only the company name **AOT Technologies**
keeps its capitals.

## Colors

Three primaries are used freely across layout and collateral: sky-blue (`primary`), yellow-red
(`amber`) and raspberry. Sea-green (`accent`) is the success/positive accent. A gunmetal neutral
scale (`secondary` / `text-primary` `#2C373C` → `surface-muted` `#ECEDEF`) carries text and dark
surfaces.

Semantic status colours reuse the brand hues — success = sea-green, warning = yellow-red, error =
raspberry, info = blue-ncs — each paired with a soft surface tint (`*-surface`) for alert backgrounds.

**Rule from the brand book:** only **gunmetal-black (`on-primary`) or white** text may sit on the
core colours. The complementary palette (blue-ncs `#2F8AB7`, mid-blue `#78D7DD`, red `#921D21`,
pink `#F6BBC1`, orange `#FFA100`, yellow-crayola `#FFD57E`) is reserved **for brand illustrations
only — never for UI chrome**, so it is intentionally not exposed as UI tokens above.

## Typography

Three families, each with a clear job. Fallback for Aron & Poppins is **"Helvetica Neue", Arial** —
never a monospace fallback.

- **Aron** (`h1`, `h2`) — display headings, branded print, emphasis. Title Case.
- **Poppins** (`h3`, `body`, `caption`, `cta`) — UI and body, the digital-first default. Subheads,
  body and captions are Sentence case; buttons (`cta`) render **UPPERCASE** via `text-transform`
  (write source labels in sentence case, e.g. `New case`).
- **JetBrains Mono** — numeric and code accents only, used **sparingly** (IDs like `AOT-2048`, SLAs
  like `99.98%`, deltas like `+12%`), with tabular figures.

## Layout

Spacing follows an **8-point grid** (`spacing.xs` 4px → `spacing.3xl` 64px). Layouts breathe: default
card padding is `lg` (24px) and screen padding is `xl` (32px). App canvases and table headers sit on
`surface-sunken`; everything else is clean white `surface`. No gradients, photographic hero washes or
textures — the flat vector brand illustrations supply colour and personality. Layout containers:
640 / 960 / 1200 / 1440px.

## Elevation & Depth

Shadows are **cool, gunmetal-tinted and low-spread**. Resting cards use `{shadows.xs}`/`{shadows.sm}`; overlays and hovers lift to
`{shadows.md}`/`{shadows.lg}`. Focus is a **3px sky-blue ring**
(`{shadows.focus}`). Use these values exactly. No warm or heavy drop shadows, no glassmorphism. A
`rgba(44,55,60,.35–.4)` gunmetal scrim sits behind modals and slide-overs; interactive cards lift 2px.

**Motion** is quick and understated: 120ms / 200ms / 320ms durations with `ease-standard`
(`cubic-bezier(.4,0,.2,1)`) and `ease-out` (`cubic-bezier(.16,1,.3,1)`). Buttons scale to `0.97` on
press. On hover, primary buttons use `{colors.primary-hover}`; other variants
darken ~6%; icon-buttons scale to `0.92`; modals fade + scale from `0.96`. No
bounces, no infinite loops.

## Shapes

Rounding is soft, echoing the geometry of the icon: `xs` 4px, `sm` 8px, `md` 10px (chips/swatches),
`lg` 16px (cards/fields), `xl` 24px, and full `pill` (999px) on buttons and badges. Avatars and
status dots are circular (50%). Borders are 1px hairlines (`#D7DBDE`) for cards and dividers, 2px for
button outlines and control rings; the optional accent card adds a 3px sky-blue top border.

**Iconography:** thin **line icons**, ~2px stroke, rounded caps/joins, on a 24×24 grid (Lucide-style),
inlined as SVG with `stroke="currentColor"` so they inherit text colour. Never emoji.

## Components

- **Button** — `variant`: `primary` (sky-blue) · `secondary` (gunmetal) · `outline` · `ghost` ·
  `danger` (raspberry); `size`: `sm | md | lg`; `block`, `startIcon`, `endIcon`. Labels UPPERCASE.
- **IconButton** — icon-only action control.
- **Forms** — **Input** (`label`, `hint`, `error` → raspberry border, `size`, `startIcon`,
  `endIcon`), plus **Textarea**, **Select**, **Checkbox**, **Radio**, **Switch**.
- **Card** — `padding` (default 24), `interactive` (lift on hover), `accent` (sky-blue top border),
  `header`, `footer`.
- **Badge** — `variant`: `neutral | info | success | warning | error | brand`; `solid`, `dot`.
- **Tag**, **Avatar** (circular).
- **Alert** — `variant`: `info | success | warning | error`; `title`, `onClose`.
- **Tabs** — `items[{ id, label, icon? }]`, controlled `value` / `defaultValue`, `onChange`;
  underline bar with a sky-blue active indicator.
- **Logo** — official AOT lockups (horizontal / stacked / icon, light & white).

## Do's and Don'ts

- **Do** build with tokens (`var(--aot-sky-blue)`, `{colors.primary}`, `{rounded.pill}`) rather than
  hard-coded values, and compose the provided components.
- **Do** put only gunmetal-black or white text on the core colours.
- **Do** use the real logo and illustration assets instead of redrawing them.
- **Don't** use the complementary palette for UI chrome — it is for brand illustrations only.
- **Don't** use emoji, exclamation marks in product UI, gradients, photographic washes, or
  glassmorphism.
- **Don't** capitalise product names — caseflow, formsflow and m8flow are always lowercase.

<!-- Source: AOT Technologies Design System, a Design System artifact in Claude (https://claude.ai/artifact/YCmVtamuUv1XR4spQE447N); moved from Claude Design project 875c59c0-39ca-4f76-b742-061041f7f2ac on 2026-11-10. -->
