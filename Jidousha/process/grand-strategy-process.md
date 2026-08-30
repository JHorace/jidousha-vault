# The grand-strategy process (design session, 2026-08-29)

How Jidousha plans and builds simulation / grand-strategy games. This
extends the working agreements in the project brief; it does not replace
them. Owner-approved 2026-08-29. Lives in three places: project docs
(session-critical copy), the vault (`process/`), and eventually the repo
when the scaffolding audit lands it beside the make-game skill.

## 1. Why this process exists

The rapid-prototyping loop — distill to a minimal slice, playtest, cut a
new slice — served giri until P2, where it stopped teaching us anything:
the ladder read as retuned determinism, and a four-beat horizon turned
probability into punishment. The S1 substrate playtest confirmed the
diagnosis (real time + a map is the right delivery structure) and the
genre lesson underneath it: **grand-strategy fun is emergent from system
interaction**, so a single system in isolation cannot be playtested for
fun, and per-slice fun gates stop working. The response is not to
abandon gates but to plan the system set and its dependencies up front —
and to change what intermediate gates measure.

## 2. The reframe — a base game and modules-as-DLC

The genre's own DLC economics prove that its systems are **detachable**:
shipping games work with or without entire systems. So the true MVP is
not "all the systems" — it is the **spine plus the smallest set of
modules that produces one interesting decision loop**. We build a base
game and treat our own future systems as DLC to it.

- **Foundation** (the spine): map, clock/RTwP, the attention
  architecture, general UI, and the shared currencies themselves.
  Specified deeply, built first, always running.
- **System modules**: everything else. Each is planned as a capsule
  (§5), built in waves (§7), and disableable from day one (§8).

## 3. Coupling doctrine — currencies and events only

Why DLC-style modularity works structurally: grand-strategy systems do
not couple to *each other*; they couple through a small set of **shared
currencies** (scalar-ish quantities many systems read, write, or
modify) and through **events**. We adopt that as law:

- A module's outputs are **modifiers on shared currencies** and
  **emitted events**. A module's inputs are currency reads and consumed
  event classes. Nothing else crosses a module boundary.
- **Module-to-module direct coupling is forbidden** — no module reads
  another module's interior state or calls its functions. If two
  modules need to talk, that conversation is either a currency or an
  event class, named in both capsules.
- The **currency set is the heart of the design** — it is where
  coupling and balance live, and it gets more design care than any
  single module. Currencies are foundation-tier and specified deeply.
- The substrate already laid the event rail: giri-rt's event classes
  with time+place addresses are exactly how modules will surface to the
  player; a new module means new event classes into the same attention
  machinery.

## 4. The document set and where truth lives

- **The GDD** — repo-canonical once decided (`games/<name>/GDD.md` or
  successor): the foundation specs, the currency specs, the module
  index, and the graph snapshot. The repo remains canonical for
  everything decided.
- **Capsules** — one Obsidian note per module in the vault (§5): the
  thinking layer, where modules gestate. A capsule's *decided* content
  flows into the GDD; the vault copy remains the working surface.
- **Project docs** — session-critical state, visible from every device.
  Nothing a session must have lives only in the vault or only on a
  desktop.
- **This process doc** — the how; the brief points here.

## 5. The capsule — one note per module, uniform and half a page

Every module gets one vault note in `capsules/`, with **frontmatter as
the machine-readable module registry** and a fixed, half-page body. The
frontmatter is the single source the dependency graph, the repo mermaid,
and Dataview views are generated from — one source, many readers.

```yaml
---
type: capsule
id: diplomacy            # kebab, stable
name: Diplomacy
status: sketch           # sketch | drafted | specced | building | landed | cut
tier: mvp                # mvp | post-mvp
wave:                    # derived from the requires DAG at GDD assembly
requires: ["[[map]]", "[[clock]]"]        # hard structural deps
reads:    ["[[money]]", "[[opinion]]"]    # currencies consumed
writes:   ["[[opinion]]"]                 # currencies modified
emits:    [treaty-signed, treaty-broken]  # event classes produced
consumes: [war-declared]                  # event classes reacted to
confidence: speculative  # strongest test survived: speculative|mocked|played|proven
last-reviewed: 2026-08-29
doubts: []               # active worries, in words
attention: "1 feed line per treaty event; 1 map badge"
---
```

Body, always these four sections and nothing more until build time:

- **Fantasy** — two or three sentences: what the player is doing and
  why it's interesting.
- **The loop it touches** — which decisions it creates or changes.
- **Degrades to** — what the game is with this module *off*. If this
  section can't be written, the module isn't modular; redesign it.
- **Open questions** — honest, bulleted.

**Currencies get notes too** (`currencies/`, `type: currency`,
specified deeply as foundation). Because `reads`/`writes` are
wikilinks, Obsidian's graph view renders modules clustered around
currency hubs — coupling density is *visible*: a currency everything
writes is a warning you can see.

Capsules are deliberately cheap: half a page to write, half a page to
cut. Cutting capsules is the process working, not failing —
menu-not-backlog at the new scale.

### Confidence and variants (5b, added 2026-08-29)

**Confidence is the strongest test an idea has survived** — never a
feeling: `speculative` (talked about) -> `mocked` (survived a mockup)
-> `played` (survived an owner playtest) -> `proven` (survived fresh
eyes). Failing a test drops it, with the why recorded. Mirrored as
nested tags (`#conf/played`) so graph views can color by it. Reviews
ride real events (playtest dispositions, wave closes), never a
calendar; `last-reviewed` marks staleness, rendered distinct from low
confidence.

**The graph is a graph of slots, not solutions.** A capsule is a role
plus its interface; **variants are competing fills**, listed inside
the capsule, each with a one-line pitch, its own confidence, and a
status: leading / live / parked / cut (parked is honored, not
purged). Two "variants" that declare different edges are competing
architectures — say so. Variants must converge when the module's
build wave arrives, not before: just-in-time decision with a deadline
the wave schedule provides.

## 6. Edge doctrine — shapes early, contracts at integration

Declare an edge's **shape** at capsule time: *which* currencies, *which*
event classes. Defer the **exact contract** — magnitudes, formulas,
event payload fields — to the integration session that connects the
module. Isolation comes from narrow declared edges, not from postponing
them; precision comes at the moment it can be tested.

## 7. The graph — derived, never drawn

- Generated from capsule frontmatter; hand-drawn graphs are forbidden
  because they drift. Three renderings, one source: Obsidian's graph
  view (live, free), an interactive artifact (filter by module, hover
  to isolate edges, tier/wave bands — the owner's visualization), and
  a mermaid snapshot in the GDD.
- Edges are **typed**: `requires` (hard), `reads`, `writes`,
  `emits`/`consumes` (soft, via event classes).
- The `requires` subgraph must be a DAG; its topological layers are the
  **implementation waves**. Soft-edge density feeds design review, not
  ordering.

- **Effective confidence is derived, never stored**: a node caps at
  its weakest hard-`requires` ancestor (a module on speculative
  foundations is speculative, whatever its capsule claims). Rendered
  as a ring beside the intrinsic fill. Soft edges propagate weakly or
  not at all — the coupling law bounds doubt contagion.

## 8. Enforcement — a module is modular only if the build proves it

- **Disableable from day one**: every module can be switched off, and
  verify runs the game with each module individually off — green both
  ways. This is what makes "degrades to" real rather than aspirational,
  and it is the null-stub discipline that lets modules build in
  isolation.
- **Determinism is per-module law**: engine `Rng` only, all module
  state in the sim, event emission through the one scheduler; the
  replay contract holds with any module subset enabled.
- **Attention is a budget**: each capsule's `attention` field is a
  declared cost against the attention architecture, reviewed at GDD
  assembly — the information-overload failure that triggered the pivot
  is guarded at planning time, not discovered at playtest.
- **Tick budget**: modules are profiled as they land; the world must
  hold target speed at 4x with all modules on.

## 9. Gates — what playtesting means now

- **Wave gates**: *alive and correct* — verify green (with each module
  off), determinism sweeps green, the world runs and is watchable.
  Owner playtests still happen each wave, but they judge feel, pacing,
  and legibility — not fun.
- **The MVP gate**: the first fun judgment. MVP = foundation + the
  smallest module set producing one interesting decision loop (chosen
  at GDD assembly). If the MVP isn't fun, the postmortem happens at
  the plan level, not the module level.

**The playtester budget**: naive playtesters are scarce and
non-renewable (no public solicitation). Never burn a fresh tester on
the open/instrument build — the owner, maximally contaminated, tests
open; fresh eyes are reserved for the variants where naivety is the
measurement (discovery/knowledge experiments, the MVP fun gate).

## 10. Session rhythm

1. **Brainstorm** (design session): module candidates + the currency
   set. giri's mechanics and the parked P3 material enter as capsule
   candidates; giri already discovered candidate currencies without
   naming them (wealth, regard, marks, strain) — promote or demote
   each deliberately.
2. **Capsule drafting** (design, in the vault): uniform half-pagers.
3. **GDD assembly** (design): currencies specced, tiers set, waves
   derived, graph generated, MVP module set chosen.
4. **Per module, just in time**: deep spec amendment → handoff →
   one coding session — the established rhythm, now module-shaped.
   Integration sessions fix exact edge contracts (§6).
5. Repeat by wave. One coding session per handoff stands.

## 11. The vault workflow (the thinking layer)

- Vault: Obsidian, in the git repo `jidousha-vault` (vault root
  `Jidousha/`). Read `Home.md` first; conventions accumulate there.
- **Desktop sessions** read/write the vault directly via the folder
  bridge. Claude writes inside agreed subtrees (`capsules/`,
  `currencies/`, `process/`); the owner writes anywhere.
- **iPad sessions** read the vault via the GitHub knowledge sync (add
  the vault repo to it) and write via **whole-file manifests** — never
  unified diffs (the sync is stale-prone; full contents are robust and
  idempotent): a paste-ready prompt listing files to create/replace/
  delete with complete contents. Applied by a Claude Code session
  (iPad Claude Code works) that pulls first and reports any file whose
  current content differs from what the manifest assumed. iPad writes
  lean additive (new notes) over surgical edits.
- **The mirror rule**: nothing session-critical lives only in the
  vault. Any session that works there mirrors what the next session
  needs into the project docs before ending.

## 12. Pending: the scaffolding audit

After the GDD skeleton exists, a design session audits the repo's agent
scaffolding against this process — expected outcomes: the make-game
skill rebuilt (or joined by a module-session variant) around
capsule-driven module sessions, GDD-read-first ordering, the
module-disable check in tooling, and this doc landing in the repo.
Deferred until there is a real GDD to rebuild against.
