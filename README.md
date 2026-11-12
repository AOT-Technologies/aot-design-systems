# AOT design systems: DESIGN.md source

This repo is the shared source for two design systems, **formsflow.ai** and
**AOT Technologies**. Each has its own `DESIGN.md`: the reference AI agents
load before building UI or writing copy for that brand. Both follow the
[DESIGN.md format](https://github.com/google-labs-code/design.md).

| System | Use it for | File |
| --- | --- | --- |
| formsflow.ai | formsflow.ai product UI, marketing site and email | [`systems/formsflow/DESIGN.md`](systems/formsflow/DESIGN.md) |
| AOT Technologies | AOT Technologies brand, collateral and AOT-branded product UI | [`systems/aot/DESIGN.md`](systems/aot/DESIGN.md) |

## Using these files

Give your agent one system, not both: formsflow.ai is an independent brand,
and mixing the two produces neither. Get the file through one of the routes
below so updates reach you, and don't copy values out of it into other files.

Each system ships as a Claude plugin (`formsflow-design` or `aot-design`)
from this repo's marketplace, `aot-design-systems`. The plugin holds a skill
that loads the brand's `DESIGN.md` before UI or copy work.

### Claude, Cowork and Claude Code (AOT Team plan)

Install the plugin for your brand from **Customize > Plugins** on claude.ai.
It also reaches Claude Code when you sign in with your claude.ai account
(Claude Code v2.1.273 or later). You don't need access to this repo.

Owner setup, once: **Organization settings > Plugins & skills > Add > Sync
from GitHub**, choose `AOT-Technologies/aot-design-systems` and leave **Sync
automatically** on. Set each plugin's availability so people get the brand
they work on, rather than installing both for everyone. Each merge to `main`
syncs.

### Claude Code without a claude.ai sign-in

Add the marketplace from GitHub. You need read access to this repo and a
stored git credential (`gh auth login`, then `gh auth setup-git`, or an SSH
key loaded in `ssh-agent`).

```
claude plugin marketplace add AOT-Technologies/aot-design-systems
claude plugin install formsflow-design@aot-design-systems    # or aot-design
```

Plugins track `main`. To get updates automatically, turn on auto-update in
`/plugin` under **Marketplaces**; otherwise run
`claude plugin marketplace update aot-design-systems`.

### Other teams and other agents: GitHub releases

Each merge to `main` that changes a system's `DESIGN.md` publishes a release
tagged `<system>/YYYY-MM-DD`, with the file attached and that system's
`CHANGELOG.md` entries as notes. You need read access to this repo; in CI, use
a token that can read it.

```
# latest formsflow release (use aot/ for AOT Technologies)
tag=$(gh release list --repo AOT-Technologies/aot-design-systems --json tagName \
  --jq '[.[] | select(.tagName | startswith("formsflow/"))][0].tagName')
gh release download "$tag" --repo AOT-Technologies/aot-design-systems --pattern DESIGN.md
```

Always name a tag or filter by the system prefix, as above. Don't use
GitHub's "Latest" release: it's the newest release from either system. Pin a
tag to stay on a version. Put the file at your repo's root, where
agents look for `DESIGN.md`, and replace it whole when you update.

## How each system is maintained

The two systems come from different sources, so they're maintained
differently.

**formsflow.ai is generated.** Don't edit its `DESIGN.md` directly.

```
tokens/typography.json  ─┐   Figma exports (source of truth for values)
tokens/variables.json   ─┤
src/semantic.json       ─┼─▶ scripts/build_design_md.py ─▶ DESIGN.md
src/DESIGN.prose.md     ─┘   decisions + hand-written guidance
```

- Figma owns token values. A change starts in Figma, and a fresh export
  replaces the file in `tokens/`.
- `typography.json` uses the JSON layout from zeroheight's Figma plugin:
  `ff.text-style.<family>.<style>`, with each property as `{"value": ...}`.
  The build reads only that layout. A Tokens Studio export needs a loader
  update in `scripts/build_design_md.py` first.
- zeroheight is the human-facing formsflow design system. The prose distils it
  for agents.

**AOT Technologies is hand-authored.** Its `DESIGN.md` is edited directly. The
AOT Technologies Design System, a Design System artifact in Claude
(https://claude.ai/artifact/YCmVtamuUv1XR4spQE447N), is upstream: a token
change is made there first, then mirrored here.

**Plugins and releases are built from the systems.** Each plugin's `SKILL.md`
and `plugin.json` are hand-authored. The `DESIGN.md` beside `SKILL.md` is a
copy that `make build` writes; don't edit it. Releases are created by
`.github/workflows/release.yml`; don't tag or release by hand.

## Proposing a change

1. Copy `changes/TEMPLATE.md` (or run `/new-change` in Claude Code). Name the
   system it affects and describe the change, its source and any decisions.
   One system per request.
2. Once the request is approved, run `/apply-change changes/<file>.md` in
   Claude Code. It applies the edits, rebuilds, verifies, and then waits for
   your approval before opening a PR.
3. Open a PR; don't push to `main`. CI runs `make verify` for both systems on
   every PR, and `.github/CODEOWNERS` requests a review from @timng-aot.
   Neither blocks a merge, because branch protection isn't available for this
   private repo on the org's GitHub plan. Merge only after the check passes
   and @timng-aot approves.

`CLAUDE.md` has the rules Claude Code follows in this repo.

## Commands

```
make build [SYSTEM=<name>]      # regenerate formsflow's DESIGN.md, refresh plugin copies
make verify [SYSTEM=<name>]     # check every system, or one
python3 scripts/release.py --dry-run   # show what the next merge would release
```

Every system must lint at 0 errors and 0 warnings, and its plugin copy must
match its `DESIGN.md`. formsflow also checks that its `DESIGN.md` matches a
fresh build and that its prose colour ramp matches the tokens. Requires
Python 3.9+ (standard library only) and Node 18+.

## Status

See `CHANGELOG.md`.
