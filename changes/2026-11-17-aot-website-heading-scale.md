# Change request: website heading scale differs from the design system

- **ID:** 2026-11-17-aot-website-heading-scale
- **System:** aot
- **Requested by:** Tim
- **Status:** draft
- **Touches:** `systems/aot/DESIGN.md` (front matter `typography.h1` to `h3`;
  possibly the Typography prose, depending on Decision 1)

## Why

The November 2026 audit of aot-technologies.com (finding F-25 in the
[website audit tracker](https://claude.ai/artifact/VFDRASQMGpD2AgJ9cAnfSZ))
found that the live site's headings don't follow the design system's type
scale. The design system and its upstream agree with each other: the AOT
Design System artifact in Claude (`project/tokens/typography.css`, read
2026-11-17) has the same H1 to H3 values as `DESIGN.md`. The gap is between
the system and the site.

Measured at 1440px wide on 16 November 2026, across the homepage and 18
Products and Solutions pages (19 pages):

| Level | `DESIGN.md` and upstream | Website (most common) | Website (other values) |
| --- | --- | --- | --- |
| H1 | Aron 700, 48px | Aron 700, 67.2px (15 pages) | Aron 700, 64px (2 pages); Arial 700, 80px (homepage hero, tracked separately as F-30) |
| H2 | Aron 600, 36px | Aron 700, 64px (68 headings, all 19 pages) | Aron 400, 64px (7 pages); Aron 700 at 32px, 36px and 48px |
| H3 | Poppins 500, 28px | Aron 700 at 20.8px, 32px or 48px | About 20 size and weight combinations from 16px to 56px, almost all Aron |

Two upstream details may matter for Decision 2:

- The site's 64px H2 equals the upstream supporting ramp step
  `--text-5xl: 64px`. `DESIGN.md` doesn't carry that ramp.
- The site's 67.2px H1 matches no upstream token.

Neither the 2025 brand style guide nor the design system gives mobile or
responsive heading sizes. The style guide only says sizes adapt at
breakpoints.

The heading fix has been taken out of the web developer's brief until this
request is decided, so the developer doesn't build to a scale that may
change.

## Decisions

Not yet made. Claude Code doesn't make these.

1. **Open: which way to align.**
   - (a) The website follows the design system. `DESIGN.md` doesn't change,
     this request is withdrawn, and the fix goes back to the developer.
   - (b) The design system adopts the website's scale for `h1` to `h3`.
   - (c) The design system keeps `h1` to `h3` for product UI and documents,
     and adds a separate, larger display scale for marketing pages.
2. **Open: exact values** for each changed level (family, size in rem with a
   px comment, weight, line height, letter spacing), if Decision 1 is (b) or
   (c). The person making the upstream change sets these.
3. **Open: H3 family.** The site uses Aron Bold for H3. The design system
   uses Poppins Medium.
4. **Open: mobile sizes.** Whether the design system should define heading
   sizes for small screens and, if so, their values. Nothing upstream defines
   them today.

## Part A: upstream change (a person does this first)

Depends on Decisions 1 to 4. Not needed if Decision 1 is (a).

- aot: in the AOT Design System artifact in Claude, update
  `project/tokens/typography.css` (`--h1-*`, `--h2-*`, `--h3-*`, or new
  display-scale variables for option (c)) and the matching guideline cards
  (`project/guidelines/type-display.html`, `type-ui.html`). Record the exact
  values here:

| Token | Current | New |
| --- | --- | --- |
| `typography.h1` | Aron 700, 3rem (48px), line height 1.08, spacing -0.01em | `<per Decision 2>` |
| `typography.h2` | Aron 600, 2.25rem (36px), line height 1.12, spacing -0.005em | `<per Decision 2>` |
| `typography.h3` | Poppins 500, 1.75rem (28px), line height 1.2 | `<per Decisions 2 and 3>` |

**Claude Code checks before going further.** Stop and report if any check
fails:

- No `<…>` placeholder remains in Part A or Part B.
- Each value in Part B matches the upstream `typography.css` exactly.
- Font sizes are in rem with a px comment, following the existing front
  matter.

## Part B: source edits (`systems/aot/DESIGN.md`)

To be finished once the decisions are made. Each find string below matches
exactly once (checked 2026-11-17).

**B1. H1.** Find:
```
  h1:
    fontFamily: Aron
    fontSize: 3rem            # 48px
    fontWeight: 700
```
Replace: `<per Decision 2>`

**B2. H2.** Find:
```
  h2:
    fontFamily: Aron
    fontSize: 2.25rem         # 36px
    fontWeight: 600
```
Replace: `<per Decision 2>`

**B3. H3.** Find:
```
  h3:
    fontFamily: Poppins
    fontSize: 1.75rem         # 28px
    fontWeight: 500
```
Replace: `<per Decisions 2 and 3>`

**B4. Typography prose** (only if Decision 1 is (c) or Decision 4 adds mobile
sizes). Find:
```
- **Aron** (`h1`, `h2`) — display headings, branded print, emphasis. Title Case.
```
Replace: `<a line naming when to use the display scale, or the mobile sizes>`

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system.
3. `git diff systems/aot/DESIGN.md`. Expect exactly: the B1 to B4 edits that
   the decisions call for. Report anything else. The plugin copy under
   `plugins/aot-design/` should show the same diff.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- Heading case. The site renders most H1s and H2s in uppercase; the design
  system says Title Case. This is an open question in the audit tracker
  (F-07).
- Button styles (F-26) and the homepage hero font (F-30). They stay with the
  web developer.
- Changing the website itself. Once this is decided, the fix goes back to the
  developer as a ticket.
- formsflow.ai: a separate system with its own type scale. Not affected.
