# Change request: H3 subheads in Title Case

- **ID:** 2026-11-17-aot-h3-title-case
- **System:** aot
- **Requested by:** Tim
- **Status:** draft
- **Touches:** `systems/aot/DESIGN.md` (Typography prose only; no token values)

## Why

`DESIGN.md` says subheads (`h3`) are Sentence case. The 2025 brand style
guide says H3 is Title Case, so agents following `DESIGN.md` write H3s that
are off-brand.

**What the style guide says** (`AOT.Technologies.Style.Guide.2025`, read
2026-11-17):

| Page | H3 |
| --- | --- |
| p.28, Typography Hierarchy Matrix | "H3 - Subsections: Poppins, Title Case, Medium, 28px" |
| p.29, Website Font Usage (homepage) | "H3 - Subsection: Poppins Title Case Medium" |
| p.30, Website Font Usage (blog or service page) | Not shown |

Every example of H3 in the guide is Title Case. The guide doesn't say which
small words stay lower case, and its own type samples aren't consistent
("Areas of Expertise", "Meets The Needs of Your Business").

**Upstream disagrees with itself.** In the AOT Design System artifact in
Claude (read 2026-11-17):

- `project/tokens/typography.css` labels H3 "Subsection · Poppins Medium 28
  · Title Case". This matches the guide.
- `project/README.md`, Content fundamentals → Casing, says "Subheads, body,
  captions — **Sentence case**." `DESIGN.md` copies this.
- `project/guidelines/type-ui.html` shows the H3 sample as "Subsection
  heading", in sentence case.

**Where this came from.** The November 2026 website audit (finding F-07 in
the [website audit tracker](https://claude.ai/artifact/VFDRASQMGpD2AgJ9cAnfSZ))
found heading case mixed across aot-technologies.com, for example "Build
Intelligent Operations" next to "Turn form submissions into intelligent
workflows". The audit logged the conflict between `DESIGN.md` and the guide
as an open question, and this request settles it for H3.

`DESIGN.md` is also used for product UI (for example, the caseflow console
kit), so the rule reaches beyond the website (see Decision 2).

## Decisions

1. **H3 follows the style guide: Title Case.** Made by Tim on 2026-11-17.
2. **Open: scope.** Whether Title Case applies to every `h3`, including
   product UI subheads, or only to marketing and website pages. The guide's
   type table covers "Digital & Web Interface" generally. Part B is written
   for every `h3`. If the answer is website only, B1 needs a narrower
   replace.

H1 case (Title Case in the guide's type table, uppercase on its website
pages) is a separate open question in the audit tracker and isn't part of
this request.

## Part A: upstream change (a person does this first)

In the AOT Design System artifact in Claude:

- `project/README.md`, Content fundamentals → Casing. Change the subheads
  line so that subheads are Title Case, and body and captions stay Sentence
  case. Expected text:
  `- Headings (H1/H2) and subheads (H3) — **Title Case**.` and
  `- Body, captions — **Sentence case**.`
- `project/guidelines/type-ui.html`: change the H3 sample text from
  "Subsection heading" to "Subsection Heading".
- `project/tokens/typography.css`: no change. It already says Title Case.

No token values change.

**Claude Code checks before going further.** Stop and report if any check
fails:

- Upstream `README.md` no longer lists subheads as Sentence case.
- Upstream `typography.css` still labels H3 Title Case.

## Part B: source edits (`systems/aot/DESIGN.md`)

The find string matches exactly once (checked 2026-11-17).

**B1. Typography prose.** Find:
```
- **Poppins** (`h3`, `body`, `caption`, `cta`) — UI and body, the digital-first default. Subheads,
  body and captions are Sentence case; buttons (`cta`) render **UPPERCASE** via `text-transform`
  (write source labels in sentence case, e.g. `New case`).
```
Replace:
```
- **Poppins** (`h3`, `body`, `caption`, `cta`) — UI and body, the digital-first default. Subheads
  (`h3`) are Title Case; body and captions are Sentence case; buttons (`cta`) render **UPPERCASE**
  via `text-transform` (write source labels in sentence case, e.g. `New case`).
```

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system.
3. `git diff systems/aot/DESIGN.md`. Expect exactly: the Typography prose
   edit in B1. Report anything else. The plugin copy under
   `plugins/aot-design/` should show the same diff.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- H1 and H2 case. `DESIGN.md` already says Title Case for both. Whether the
  website's H1 should be uppercase (style guide pp.29–30) is still an open
  question.
- A rule for which small words stay lower case in Title Case. Neither the
  guide nor `DESIGN.md` defines one.
- Full stops at the end of headings. The guide has no rule.
- Fixing the website's headings (F-07). That follows once the case rules are
  settled.
- formsflow.ai: a separate system that uses sentence case throughout. Not
  affected.
