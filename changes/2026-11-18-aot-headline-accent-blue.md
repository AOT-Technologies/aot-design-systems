# Change request: a blue for accent words in headlines

- **ID:** 2026-11-18-aot-headline-accent-blue
- **System:** aot
- **Requested by:** Tim
- **Status:** draft
- **Touches:** `systems/aot/DESIGN.md` (Colors prose and Do's and Don'ts;
  possibly a new colour token and component, depending on Decision 3)

## Why

AOT headlines often set one or two words in sky-blue as a brand accent. On
light backgrounds, sky-blue `#36C5F0` (`colors.primary`) fails contrast as
text, even at headline sizes. The brand wants to keep a blue accent, so it
needs a blue that passes.

**Where this came from.** The November 2026 website audit (finding F-29 in
the [website audit tracker](https://claude.ai/artifact/VFDRASQMGpD2AgJ9cAnfSZ))
measured coloured text on aot-technologies.com at 1440px on 16 November 2026.
Sky-blue accent words fail on every light background the site uses:

| Background | Sky-blue contrast | Where |
| --- | --- | --- |
| White `#FFFFFF` | 2.02:1 | 34 headline words (48–64px) on 11 pages, including Home |
| `#F9F9F9` | 1.92:1 | 9 headline words (36–64px) on delphi, Cloud Readiness for AI and Healthcare |
| Light grey `#ECEDEF` (`surface-muted`) | 1.72:1 | "platform" (64px) on m8flow |

WCAG 2.2 SC 1.4.3 needs 3:1 for large text (24px or more, or 18.66px or more
in bold) and 4.5:1 for smaller text. These words are all large, so 3:1 is
the minimum. Sky-blue passes on gunmetal (6.05:1), so dark backgrounds aren't
affected.

**What the brand sources say:**

- The 2025 style guide (p.22): "Reserve the use of accent colours only for
  larger headline typography." Accent words in headlines are intended.
- The style guide (p.20) and `DESIGN.md` Colors: the complementary palette,
  including blue-ncs `#2F8AB7`, is "reserved for brand illustrations only".
  `DESIGN.md` deliberately doesn't expose it as a colour token.
- Upstream `project/tokens/colors.css` (read 2026-11-17) already uses
  blue-ncs in UI: `--text-link` and `--status-info`. `DESIGN.md` also uses it
  for the info status colour.
- Neither `DESIGN.md` nor upstream says which colour to use for accent words
  on light backgrounds.

**Format constraints.** These were checked on throwaway copies of `DESIGN.md`
with the pinned linter (`@google/design.md` 0.4.0). `make verify` treats any
warning as a failure.

- A colour token that no component references gets an `orphaned-tokens`
  warning.
- A component's `contrast-ratio` check applies the 4.5:1 minimum whatever the
  typography size. A heading component with `typography.h1` still fails at
  3.86:1 (`#2F8AB7`) and 3.55:1 (`#0E93BB`).

So a blue that only reaches 3:1 can be recorded in the prose, but not as a
front-matter token. A front-matter token needs at least 4.5:1 on each light
background it's used on.

## Decisions

1. **Keep a blue accent for headline words on light backgrounds**, rather
   than switching them to gunmetal. Made by Tim on 2026-11-18.
2. **Open: which blue.** The person making the upstream change sets the
   exact value. For reference, these are calculated thresholds, not
   proposals:

   | Option | Value | White | `#F9F9F9` | `#ECEDEF` |
   | --- | --- | --- | --- | --- |
   | (a) Complementary blue, existing | `#2F8AB7` | 3.86:1 | 3.67:1 | 3.30:1 |
   | (b) Darker sky-blue, same hue (194°) and saturation, passing 3:1 everywhere | about `#0E93BB` or darker | 3.55:1 | 3.38:1 | 3.03:1 |
   | (c) Darker sky-blue, same hue, passing 4.5:1 everywhere | about `#0B7494` or darker | 5.33:1 | 5.06:1 | 4.55:1 |

   Option (a) changes the hue and saturation noticeably. Options (b) and (c)
   keep the sky-blue character but are new colours.
3. **Open: how `DESIGN.md` records it.**
   - (i) A prose rule only: name the colour in the Colors section for accent
     words in large headings. This works for (a), (b) or (c).
   - (ii) A front-matter colour token, used by a new heading-accent
     component. This needs option (c) or another blue that reaches 4.5:1 on
     every light background. The token and component names are part of the
     decision.
4. **Open, only for option (a): the illustration-only rule.** Using the
   complementary blue for headline text needs an exception to the rule that
   the complementary palette is for illustrations only.

## Part A: upstream change (a person does this first)

Depends on Decisions 2 to 4. In the AOT Design System artifact in Claude:

- `project/tokens/colors.css`: for options (b) and (c), add the new colour
  with its exact value, plus a semantic alias for headline accent text. For
  option (a), add the alias pointing to `--aot-blue-ncs`.
- `project/README.md`, Visual foundations → Colour: add the rule for accent
  words in headlines. For option (a), note the exception to the
  illustration-only rule.
- `project/guidelines/colors-primary.html` or `colors-complementary.html`:
  show the new colour or the exception.

Record the exact values here:

| Item | Value |
| --- | --- |
| Headline accent colour | `<per Decision 2>` |
| Upstream variable name | `<per Decision 3>` |
| Contrast on white, `#F9F9F9` and `#ECEDEF` | `<measured after Decision 2>` |

**Claude Code checks before going further.** Stop and report if any check
fails:

- No `<…>` placeholder remains in Part A or Part B.
- The chosen colour reaches at least 3:1 on white, `#F9F9F9` and `#ECEDEF`
  (4.5:1 if Decision 3 is (ii)).
- The value in Part B matches upstream `colors.css` exactly.

## Part B: source edits (`systems/aot/DESIGN.md`)

To be finished once the decisions are made. Each find string below matches
exactly once (checked 2026-11-18).

**B1. Colour token** (only if Decision 3 is (ii)). Find:
```
  primary-hover: "#33B9E2"    # sky-blue darkened 6% — primary button hover
```
Replace: `<the same line, then the new token on the next line, per Decisions 2 and 3>`

**B2. Heading-accent component** (only if Decision 3 is (ii)). Find:
```
components:
  button-primary:
```
Replace: `<"components:", the new component (backgroundColor "{colors.surface}", textColor the new token, typography "{typography.h1}"), then "  button-primary:">`

**B3. Colors prose.** Find:
```
only — never for UI chrome**, so it is intentionally not exposed as UI tokens above.
```
Replace: `<the same line, then a new paragraph: sky-blue fails as text on light backgrounds; for accent words in large headings (24px or more, or 18.66px or more in bold) on white, #F9F9F9 or surface-muted, use the chosen colour; never for body text. For option (a), also the exception to the illustration-only rule.>`

**B4. Do's and Don'ts.** Find:
```
- **Don't** use the complementary palette for UI chrome — it is for brand illustrations only.
```
Replace: `<the same line (with the exception, for option (a)), then: "- **Don't** set sky-blue text on light backgrounds; use <the chosen colour> for accent words in large headings.">`

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system. In particular, no
   `orphaned-tokens` or `contrast-ratio` warnings.
3. `git diff systems/aot/DESIGN.md`. Expect exactly: the B1 to B4 edits that
   the decisions call for. Report anything else. The plugin copy under
   `plugins/aot-design/` should show the same diff.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- Amber accent words on light backgrounds (also F-29). No existing yellow
  passes, and that's a separate decision.
- The other F-29 colour pairs. They're fixed on the website with existing
  colours (developer brief, Ticket 5).
- Sky-blue on dark backgrounds, which passes.
- Changing the linter or `make verify` to apply 3:1 to large text.
- formsflow.ai: a separate system with its own colours. Not affected.
