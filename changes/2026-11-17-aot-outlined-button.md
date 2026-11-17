# Change request: define the outlined button

- **ID:** 2026-11-17-aot-outlined-button
- **System:** aot
- **Requested by:** Tim
- **Status:** draft
- **Touches:** `systems/aot/DESIGN.md` (front matter `components.button-outline`,
  possibly a new component; Shapes and Components prose)

## Why

The outlined button is the most common button on aot-technologies.com, but
the design system describes it three different ways, and none of them
matches the site. The 2025 brand style guide doesn't define buttons, so it
can't settle this.

**Where this came from.** In the November 2026 website audit (finding F-26
in the [website audit tracker](https://claude.ai/artifact/VFDRASQMGpD2AgJ9cAnfSZ)),
every button on the homepage and the 18 Products and Solutions pages was
measured at 1440px on 17 November 2026. There were 126 buttons, all listed
on the tracker's Buttons tab. 56 of them are outlined:

| Labels | Buttons | Where |
| --- | --- | --- |
| Gunmetal `#2C373C` on light backgrounds | 28 | The header "Talk To Us" (every page), "Tell Me More" (delphi), "All Projects" and in-page "Talk to Us" links |
| White `#FFFFFF` on dark backgrounds | 26 | The hero CTA ("Let's Get Started", 15 buttons on 14 pages; "Talk To An Expert" on delphi and node-wire), "ALL CASE STUDIES", "Read Article", "Go to Github" |
| Light grey `#ECEDEF` on a dark background | 2 | SLED360's two audience buttons |

All 56 have no fill, a **1px sky-blue (`#36C5F0`) border** and a fully
rounded pill shape. Their labels are Poppins Medium 500, 14px, in mixed case.
That label style is a website defect, tracked as F-26 and assigned to the
web developer. It isn't part of this request.

**How the design system describes the outlined button today:**

| Source | Fill | Border | Label |
| --- | --- | --- | --- |
| `DESIGN.md` front matter (`components.button-outline`) | White (`{colors.surface}`) | Not stated | Gunmetal (`{colors.text-primary}`), CTA type |
| `DESIGN.md` Shapes prose | Not stated | "2px for button outlines", colour not stated | Not stated |
| Upstream `project/components/actions/Button.jsx` (read 2026-11-17) | Transparent | 2px `--border-strong` (`#B6BDC1`) | Gunmetal, CTA type |
| Website | None | 1px `#36C5F0` | Gunmetal on light backgrounds, white on dark |

Neither `DESIGN.md` nor upstream defines an outlined button for dark
backgrounds, which is where 26 of the site's outlined buttons are.

**Contrast.** Measured against WCAG 2.2 SC 1.4.11 (non-text contrast,
3:1):

| Border | On white | On gunmetal |
| --- | --- | --- |
| Sky-blue `#36C5F0` (website) | 2.02:1 | 6.05:1 |
| `--border-strong` `#B6BDC1` (upstream) | 1.90:1 | Not measured |

Both borders fall below 3:1 on white. That may be acceptable if the label
alone identifies the button, but someone needs to make that call (Decision
5).

**Format constraints.** These were checked on a throwaway copy of
`DESIGN.md` with the pinned linter (`@google/design.md` 0.4.0), and
`make verify` treats any warning as a failure:

- `borderColor` and `borderWidth` aren't valid component sub-tokens (warning
  `broken-ref`). The valid ones are `backgroundColor`, `textColor`,
  `typography`, `rounded`, `padding`, `size`, `height` and `width`. So the
  border has to be described in prose, not in the front matter.
- A transparent `backgroundColor` triggers a `contrast-ratio` warning. The
  front matter needs a real fill colour, such as the surface the button sits
  on.

## Decisions

Not yet made. Claude Code doesn't make these.

1. **Open: border colour.** Sky-blue `#36C5F0` (as on the website),
   `--border-strong` `#B6BDC1` (as in upstream code), or another existing
   token.
2. **Open: border width.** 1px (website) or 2px (upstream code and the
   `DESIGN.md` Shapes prose).
3. **Open: fill.** No fill, showing the surface behind it (website and
   upstream code), or white (`DESIGN.md` front matter today). Given the format
   constraint above, the front matter can record the light-background
   surface, with the prose saying the button has no fill of its own.
4. **Open: a version for dark backgrounds.** Whether to add a component (for
   example `button-outline-inverse`: gunmetal surface, white label) to match
   the site's 26 outlined buttons on dark backgrounds. If yes, upstream needs
   a matching `Button` variant. The name is part of the decision.
5. **Open: non-text contrast.** Whether a border below 3:1 on white is
   acceptable for this button, given that its label identifies it.

## Part A: upstream change (a person does this first)

Depends on Decisions 1 to 5. Make the change in the AOT Design System
artifact in Claude, then record the exact values here:

- `project/components/actions/Button.jsx`: the `outline` palette entry
  (`background`, `color`, `border`), and a new variant for dark backgrounds if
  Decision 4 adds one.
- `project/components/actions/Button.prompt.md`: list any new variant.
- `project/tokens/colors.css`: only if the chosen border colour needs a new
  alias. No new colour values are expected, because all the options above are
  existing tokens.

| Token or property | Current upstream | New |
| --- | --- | --- |
| `outline` background | `transparent` | `<per Decision 3>` |
| `outline` border | `2px solid var(--border-strong)` | `<per Decisions 1 and 2>` |
| `outline` label | `var(--aot-gunmetal)` | `<unchanged, or per Decision 4>` |
| Variant for dark backgrounds | None | `<per Decision 4>` |

**Claude Code checks before going further.** Stop and report if any check
fails:

- No `<…>` placeholder remains in Part A or Part B.
- Each colour in Part B already exists as a `DESIGN.md` colour token or in
  upstream `colors.css`.
- Each value in Part B matches upstream `Button.jsx` exactly.

## Part B: source edits (`systems/aot/DESIGN.md`)

To be finished once the decisions are made. Each find string below matches
exactly once (checked 2026-11-17).

**B1. Outline component.** Find:
```
  button-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.cta}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
```
Replace: `<per Decision 3; only backgroundColor and textColor can change>`

**B2. Version for dark backgrounds** (only if Decision 4 adds one). Find:
```
  button-ghost:
```
Replace: `<the new component block, then "  button-ghost:">`

**B3. Border prose (Shapes).** Find:
```
Borders are 1px hairlines (`#D7DBDE`) for cards and dividers, 2px for
button outlines and control rings;
```
Replace: `<per Decisions 1 and 2: the outline button's border width and colour, by token name>`

**B4. Button prose (Components).** Find:
```
- **Button** — `variant`: `primary` (sky-blue) · `secondary` (gunmetal) · `outline` · `ghost` ·
  `danger` (raspberry); `size`: `sm | md | lg`; `block`, `startIcon`, `endIcon`. Labels UPPERCASE.
```
Replace: `<the same line, plus when to use outline and the dark-background version>`

## Part C: build and verify

1. `make build SYSTEM=aot` (refreshes the plugin copy of `DESIGN.md`).
2. `make verify`: every check passes for every system. In particular, no
   `broken-ref` or `contrast-ratio` warnings on the button components.
3. `git diff systems/aot/DESIGN.md`. Expect exactly: the B1 to B4 edits that
   the decisions call for. Report anything else. The plugin copy under
   `plugins/aot-design/` should show the same diff.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[aot]`.
2. Set **Status** to `applied` with the date.
3. Summarise and wait for approval, then open a PR.

## Out of scope

- The website's button label style (14px, Medium 500, mixed case). It's a
  site defect (F-26), with the web developer.
- The `ghost` button. Its front matter also uses a white fill, but the
  website doesn't use it.
- Hover, pressed and disabled states for outlined buttons. `DESIGN.md`
  already says non-primary variants darken ~6% on hover.
- `IconButton`'s outline variant.
- formsflow.ai: a separate system with its own buttons. Not affected.
