# Change request: button-primary states

- **ID:** 2026-11-12-formsflow-button-primary-states
- **System:** formsflow
- **Requested by:** Tim
- **Status:** applied (2026-11-12)
- **Touches:** `systems/formsflow/src/DESIGN.prose.md`

## Why

`DESIGN.md` specifies **button-primary** as a solid `primary` (indigo-900)
fill with `on-primary` text, and `primary-hover` (indigo-shade) on
hover/pressed. Neither formsflow source draws it that way. The rest state is
never a solid indigo-900 fill (Tim, 2026-11-12).

The two sources also disagree with each other:

| State | Web: Nav module CTA (formsflow-Web Figma, node `1:7824`) | Product: formsflow V8 `Primary-Button` (published) |
| --- | --- | --- |
| Rest | bg `indigo-100`, border 1px `indigo-900` | bg `gray-50`, border 1px `indigo-500`, text `gray-800`, `body-sml` regular |
| Hover | bg `indigo-900`, white text | border 1px `indigo-900`; bg and text unchanged |
| Selected | not drawn | bg `indigo-100`, border 1px `indigo-900` |
| Disabled | not drawn | border 1px `indigo-300`, text `gray-200` |
| Pressed | not drawn | not drawn |
| Padding, radius | — | `12px 20px` (`ff/space/3`, `ff/space/5`), `pill` |

The web hover state comes from Tim (2026-11-12). The file draws only the rest
state; the Nav W/ Rollover frame doesn't show a hover.

Every colour above already exists in the primitive ramp, so no new values are
needed.

## Decisions (Tim, 2026-11-12)

1. **Split by surface.** Marketing pages use the web Nav CTA rest state. The
   product (everywhere else) uses the V8 Primary-Button.
2. **Hover also splits.** On marketing pages, hover fills `primary` with
   `on-primary` text. In the product, hover darkens the border to `primary`
   and leaves the fill and text unchanged.
3. **`primary-hover` stays unchanged** in `semantic.json`, the front matter
   and the Colors prose.
4. **Label type:** marketing pages use `body` (regular 16/24); the product
   uses `body-sml` (regular 14/20). The use-cases prototypes in formsflow-Web
   move to regular 16.
5. **States:** include the product's selected and disabled states. Drop
   "pressed" from the spec.

Known gap: the web source draws no selected or disabled state for marketing
pages, so the spec doesn't define them there.

## Part A: upstream change

None. Every colour is an existing primitive, and button states are prose, not
a Figma token export. `tokens/` doesn't change.

## Part B: source edits

The find string has been checked to match exactly once in the current file.

**B1. Component spec** (`systems/formsflow/src/DESIGN.prose.md`, in `## Components`).
Find:
```
- **button-primary** — bg `primary`, text `on-primary`, radius `pill`, padding `12px 20px`.
- **button-primary (hover/pressed)** — bg `primary-hover`.
```
Replace:
```
- **button-primary** — bg `gray-50`, border `1px indigo-500`, text `gray-800` (`body-sml`), radius `pill`, padding `12px 20px`. Never a solid `primary` fill at rest.
- **button-primary (hover)** — border `1px primary`; bg and text unchanged.
- **button-primary (selected)** — bg `indigo-100`, border `1px primary`.
- **button-primary (disabled)** — border `1px indigo-300`, text `gray-200`.
- **button-primary (marketing pages)** — bg `indigo-100`, border `1px primary`, text `gray-800` (`body`), radius `pill`, padding `12px 20px`; on hover, bg `primary`, text `on-primary`.
```

## Part C: build and verify

1. `make build SYSTEM=formsflow`, then `make verify`. Every check must pass,
   with 0 errors and 0 warnings.
2. Check the diff with `git diff systems/formsflow/DESIGN.md`. Expect exactly
   the `## Components` button lines replaced as in B1. The front matter must be
   unchanged, including `primary-hover`. Report anything else as unexpected.

## Part D: record

1. Add an entry to `CHANGELOG.md`, tagged `[formsflow]`.
2. Set **Status** above to `applied` with the date.
3. Summarise and wait for approval, then open a PR (per `CLAUDE.md`).

## Out of scope

- **button-secondary**: `DESIGN.md` has no secondary button. The V8
  `Secondary-Button` (`gray-50` bg, 1px `gray-200` border, `gray-800` text,
  hover border `gray-800`) needs its own request.
- **TabItem off-palette fills** (`#EDEDED` active, `#D5D5D5` active-hover) in
  formsflow V8: this is a Figma library fix, not a `DESIGN.md` change.
- **Figma**: the use-cases prototypes are updated separately (Decision 4). The
  web Nav module and the V8 Primary-Button are unchanged.
- **`primary-hover` usage**: no button state uses it now (Decision 3 keeps it).
  Revisit if it stays unused.
- **`shadow-focus`** on buttons: unchanged.
