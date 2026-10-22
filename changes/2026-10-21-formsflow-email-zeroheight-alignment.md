# Change request: align the Email section with zeroheight

- **ID:** 2026-10-21-formsflow-email-zeroheight-alignment
- **System:** formsflow
- **Requested by:** Tim
- **Status:** applied (2026-10-21)
- **Touches:** `systems/formsflow/src/DESIGN.prose.md`

## Why

zeroheight Foundations › Email
(https://formsflow.zeroheight.com/styleguide/s/140529/p/31b81f) has been
reviewed. A comparison with `DESIGN.md` found no conflicting values, but three
differences in wording and coverage:

1. **Scope.** `DESIGN.md` lists "marketing, trial and onboarding lifecycle";
   zeroheight lists "marketing, onboarding lifecycle".
2. **Outlook conditional style.** zeroheight gives the exact snippet, with its
   selector list and `!important`. `DESIGN.md` only describes it, so agents
   can leave out `!important` or some of the elements.
3. **Guidance only in zeroheight.** One `h1` per email, what each size is used
   for, and using the full fallback stack on every text element. Agents
   reading `DESIGN.md` don't see any of it.

## Decisions (Tim, 2026-10-21)

1. zeroheight is right about scope: drop "trial".
2. Use zeroheight's conditional style snippet exactly as written.
3. Bring zeroheight's email-only guidance into `DESIGN.md`: one `h1` per email,
   usage for each size, and the full stack on every text element.

## Part A: upstream change

None. These are prose edits only: no token values change, and `tokens/` and
`src/semantic.json` are untouched.

## Part B: source edits (`systems/formsflow/src/DESIGN.prose.md`)

Each find string must match exactly once.

**B1. Scope** (Decision 1). Find:
```
Applies to HTML emails that formsflow.ai sends: marketing, trial and onboarding
lifecycle, and account notifications.
```
Replace:
```
Applies to HTML emails that formsflow.ai sends: marketing, onboarding lifecycle,
and account notifications.
```

**B2. Stack on every text element** (Decision 3). Find:
```
**Font stack.** Use exactly:
```
Replace:
```
**Font stack.** Use exactly, on every text element:
```

**B3. Outlook conditional style** (Decision 2). Find:
```
Add an
`<!--[if mso]>` style block that sets `font-family: Arial, sans-serif` on text
elements, so Outlook for Windows doesn't fall back to Times New Roman. Never use
```
Replace:
```
Outlook for
Windows can ignore the whole stack when the first font is a web font and fall
back to Times New Roman, so add this conditional style exactly:
`<!--[if mso]><style>body, table, td, p, a, h1, h2, h3 { font-family: Arial, sans-serif !important; }</style><![endif]-->`
Never use
```

**B4. Usage for each size** (Decision 3). Find:
```
**Sizes.** Use only `caption`, `body-sml`, `body`, `h3`, `h2` and `h1`; no `max`
sizes. Apply each token's px line-height as given, with
`mso-line-height-rule: exactly` so Outlook respects it.
```
Replace:
```
**Sizes.** Use only `caption`, `body-sml`, `body`, `h3`, `h2` and `h1`; no `max`
sizes. Use `h1` for the headline, once per email; `h2` for subheadings; `h3`
for section headings; `body` for default text; `body-sml` for secondary text
and metadata; and `caption` for the footer, legal text and unsubscribe link.
Apply each token's px line-height as given, with
`mso-line-height-rule: exactly` so Outlook respects it.
```

## Part C: build and verify

1. `make build SYSTEM=formsflow`, then `make verify`. Every check must pass,
   with 0 errors and 0 warnings.
2. Check the diff with `git diff systems/formsflow/DESIGN.md`. Expect exactly
   the prose edits B1 to B4 in `## Email`. The front matter doesn't change.

   Report anything else as unexpected.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[formsflow]`.
2. Set **Status** above to `applied` with the date.
3. Summarise and wait for approval, then open a PR (per `CLAUDE.md`).

## Out of scope

- zeroheight's table of which font each email client renders. It's background
  for people, not a rule agents act on.
- zeroheight's `text-size-*` and `space-*` names. Its "Ref" column already maps
  them to `DESIGN.md`'s token names.
- The zeroheight Email page is hidden in the navigation. Publishing it is a
  zeroheight task.
- zeroheight's Typography page still says 10 sizes and has no `max5` or `max6`
  rows (already tracked).
