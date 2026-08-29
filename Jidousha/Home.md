---
role: vault-home
---

# Jidousha vault — home

This vault is the project's **thinking layer**: brainstorm residue,
capsules in progress, playtest notes, working drafts. The layers above
it: the **GitHub repo is canonical** for anything decided; the Claude
**project docs** carry orientation and session-critical state (visible
from every device). Hard rule: **nothing session-critical lives only
here** — any session that works in this vault mirrors whatever the next
session needs into the project docs before ending.

The vault lives in the git repo `jidousha-vault` (vault root:
`Jidousha/`). Desktop Claude sessions read/write it directly; iPad
sessions read it via the GitHub knowledge sync and write via
**whole-file manifests** applied by a Claude Code session (see the
process doc §11 — never unified diffs; additive writes preferred).

## Conventions (accumulate here as they settle)

- Process docs live in `process/` — read
  [[grand-strategy-process]] for how planning, capsules, waves, and
  gates work.
- One note per **system-module capsule** in `capsules/`; shared
  currencies and relational state in `currencies/`; foundation
  elements in `foundation/`; session logs in `sessions/`. Capsule
  frontmatter is the machine-readable module registry — the
  dependency-graph artifact, the GDD mermaid, and Dataview views are
  all generated from it. One source. Schema + the fixed body (Fantasy
  / Loop / Degrades to / Open questions) per process doc §5.
- Wikilinks in `requires`/`reads`/`writes` fields so the graph view
  doubles as the live dependency graph (currencies render as hubs).
- **Design confidence** (adopted 2026-08-29, pending review-in-use):
  `confidence:` is the strongest test survived — `speculative` (only
  talked about) → `mocked` (survived a mockup) → `played` (survived
  owner playtest) → `proven` (survived fresh eyes). Failures drop it
  with a recorded why. Mirrored as nested tags (`#conf/played`) so
  graph-view groups can color by it. `last-reviewed:` marks staleness;
  reviews ride real events (playtest dispositions, wave closes), not a
  calendar. Effective confidence is *derived* — a node caps at its
  weakest hard-`requires` ancestor; never hand-maintained. `doubts:`
  holds active worries in words.
- **Variants live inside their capsule** (slot vs fill): the node is
  the *slot* (role + interface — what neighbors depend on); variants
  are competing *fills*, each with status (leading / live / parked /
  cut) and its own confidence. Parked is honored, not purged. Two
  "variants" that declare different edges are competing architectures
  — say so. Variants converge when the module's build wave arrives,
  not before.
- Claude writes only inside agreed subtrees (`capsules/`,
  `currencies/`, `foundation/`, `process/`, `sessions/`); the owner
  writes anywhere.
- Owner: James Sumihiro. Claude sessions read this note first.
- **`dependency.canvas`** is the structured dependency view: generated
  by `tools/gen-canvas.py` (repo root) from capsule frontmatter — node
  color = confidence, edge color = type (red requires / cyan reads /
  orange writes), bands grouped. Drag nodes freely (positions survive
  regeneration); never add nodes or edges by hand — edit frontmatter
  and regenerate.
- The **Jidousha Loom** (claude.ai artifact) is the interactive
  dependency view: edge-type filters, hover labels, focus/hide,
  confidence + derived effective confidence. Regenerate its data with
  `python3 tools/gen-canvas.py --dump-json` and ask a design session to
  republish. Canvas views: `--edges=requires --out=structure.canvas`
  for a requires-only canvas; `--hide=id,id` to omit nodes; `--fresh`
  to relayout. Edge labels live in the canvas Key card, not on edges.
- Canvas cards show plain filenames (no subpath embeds). To keep the
  Properties block out of canvas cards, this vault uses the per-vault
  setting **Settings → Editor → Properties in document → Hidden**
  (frontmatter stays editable in the Properties side panel).
