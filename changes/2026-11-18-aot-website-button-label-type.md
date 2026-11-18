# Change request: website button labels differ from the CTA type style

- **ID:** 2026-11-18-aot-website-button-label-type
- **System:** aot
- **Requested by:** Tim
- **Status:** draft
- **Touches:** `systems/aot/DESIGN.md` (front matter `typography.cta`;
  possibly the Typography and Components prose, depending on Decision 1)

## Why

The button labels on aot-technologies.com don't use the design system's CTA
type style. Every brand source agrees on that style. Only the live site
differs, so someone needs to decide which way to align.

**Where this came from.** The November 2026 website audit (finding F-26 in
the [website audit tracker](https://claude.ai/artifact/VFDRASQMGpD2AgJ9cAnfSZ))
measured every button on the homepage and the 18 Products and Solutions
pages at 1440px on 17 November 2026. It found 126 buttons, all listed on the
tracker's Buttons tab.

| Label style on the website | Buttons | Pages | Examples |
| --- | --- | --- | --- |
| Poppins Medium 500, 14px, as typed | 81 | 19 | Header "Talk To Us", hero "Let's Get Started", card "Learn More" and "Discover" |
| Poppins Medium 500, 14px, capitalised | 2 | 2 | In-page "Talk To Us" (Home, Open Technology Ecosystems) |
| Poppins Medium 500, 16px, as typed | 19 | 19 | Footer newsletter "Submit" |
| Poppins Regular 400, 16px, capitalised | 15 | 15 | Contact form "Get Started" ("Get in touch" on caseflow and formsflow.ai) |
| Poppins Regular 400, 16px, as typed | 2 | 1 | m8flow "Talk to an expert", "Explore the Open Source Engine" |
| Poppins Medium 500, 12.8px, as typed | 7 | 1 | Healthcare card buttons |

None of the 126 labels is set in uppercase. Three are typed partly or fully
in capitals ("ALL CASE STUDIES" once, "ALL Projects" twice).

**What the brand sources say:**

| Source | Family | Weight | Size | Case | Letter spacing |
| --- | --- | --- | --- | --- | --- |
| 2025 style guide p.28 (type table: "CTAs / Buttons") | Poppins | SemiBold | 16px | Uppercase | Not stated |
| 2025 style guide p.29 (website homepage) | Poppins | SemiBold | Not stated | Uppercase | Not stated |
| `DESIGN.md` `typography.cta` and prose | Poppins | 600 | 1rem (16px) | Uppercase | 0.06em |
| Upstream `project/tokens/typography.css` (`--cta-*`, read 2026-11-17) | Poppins | 600 | 16px | Uppercase | 0.06em |
| Upstream `project/components/actions/Button.jsx` | Poppins | 600 | 13px (`sm`), 16px (`md`), 17px (`lg`) | Uppercase | 0.06em |

Upstream's `Button` sizes go beyond `typography.cta`: a small button uses a
13px label and a large one 17px. `DESIGN.md` lists the `size` prop
(`sm | md | lg`), but not the label size for each.

The audit's fix for the site's button fills and label colours has gone to
the web developer. This label-type part is held back until the direction is
decided.

## Decisions

Not yet made. Claude Code doesn't make these.

1. **Open: which way to align.**
   - (a) The website follows the design system. `DESIGN.md` doesn't change,
     this request is withdrawn, and the fix goes back to the web developer.
   - (b) The design system adopts the website's label style for `cta`.
   - (c) The design system keeps `cta` for product UI and adds a separate
     label style for marketing pages.
2. **Open: exact values** for any changed style: family, weight, size in rem
   with a px comment, line height, letter spacing and case. The person making
   the upstream change sets these.
3. **Open: label size by button size.** Whether `DESIGN.md` should record the
   `sm`, `md` and `lg` label sizes that upstream's `Button` already uses
   (13px, 16px, 17px).

## Part A: upstream change (a person does this first)

Depends on Decisions 1 to 3. Not needed if Decision 1 is (a). In the AOT
Design System artifact in Claude:

- `project/tokens/typography.css`: the `--cta-*` variables, or new
  variables for a marketing label style if Decision 1 is (c).
- `project/components/actions/Button.jsx`: the label `fontWeight`,
  `fontSize` per size, `letterSpacing` and `textTransform`.
- `project/README.md` (Content fundamentals → Casing, and Visual foundations
  → Type) and `project/guidelines/type-cta-mono.html`.

Record the exact values here:

| Token | Current | New |
| --- | --- | --- |
| `typography.cta` | Poppins 600, 1rem (16px), line height 1, letter spacing 0.06em, uppercase | `<per Decisions 1 and 2>` |
| Label size by button size | Not in `DESIGN.md` (upstream: 13px, 16px, 17px) | `<per Decision 3>` |

**Claude Code checks before going further.** Stop and report if any check
fails:

- No `<…>` placeholder remains in Part A or Part B.
- Each value in Part B matches upstream `typography.css` and `Button.jsx`
  exactly.
- Font sizes are in rem with a px comment, following the existing front
  matter.

## Part B: source edits (`systems/aot/DESIGN.md`)

To be finished once the decisions are made. Each find string below matches
exactly once (checked 2026-11-18).

**B1. CTA type token.** Find:
```
  cta:
    fontFamily: Poppins
    fontSize: 1rem            # 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.06em
```
Replace: `<per Decisions 1 and 2>`

**B2. Typography prose: label case** (only if the case changes). Find:
```
buttons (`cta`) render **UPPERCASE** via `text-transform`
```
Replace: `<per Decision 2>`

**B3. Components prose: Button** (only if the case changes or Decision 3
adds label sizes). Find:
```
`block`, `startIcon`, `endIcon`. Labels UPPERCASE.
```
Replace: `<per Decisions 2 and 3>`

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system.
3. `git diff systems/aot/DESIGN.md`. Expect exactly: the B1 to B3 edits that
   the decisions call for. Report anything else. The plugin copy under
   `plugins/aot-design/` should show the same diff.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- Button fills and label colours on the website (also F-26). They're with
  the web developer (developer brief, Ticket 2).
- The outlined button's fill and border (change request
  `2026-11-17-aot-outlined-button`).
- Button wording, such as the eight different contact labels (finding F-08).
- Heading case (finding F-07; change request `2026-11-17-aot-h3-title-case`).
- formsflow.ai: a separate system with its own buttons. Not affected.
