---
type: capsule
id: events-director
name: Events / Director
status: drafted
tier: mvp
wave:
confidence: speculative
last-reviewed: 2026-08-29
requires: ["[[clock-rtwp]]"]
reads: []
writes: []
emits: [injected-event]
consumes: []
attention: "injected events use the standard feed/auto-pause machinery"
tags: [conf/speculative]
---
# Events / Director
**Fantasy**: the world moves without you. The anti-aimlessness lever
(chosen over opponents and over waiting for mechanic density).

**Loop**: event templates = trigger (state predicates + time window +
seeded roll) + injection. **A scenario is a file, not a mode**: pinned
triggers give fixed Frostpunk-style beats; no pins + director on =
freeplay; the tutorial is the most heavily pinned scenario and hands
off into freeplay. Pressure parameters live in the drawer. The
director's natural output type is the **petition**.

**MVP scope (decided)**: a minimal injector with 3-4 canned templates,
petition-flavored so they need no post-MVP modules (e.g. the loan
shark; a rival offer; a windfall rumor) — so the MVP fun gate measures
the character loop under mild pressure, not a vacuum. The full
director (pressure curves, storyteller pacing) is post-MVP.

**Post-MVP**: heroic-threat escalation keyed to settlement development
(the phasing arc's difficulty driver), with [[threats]].

**Degrades to**: a quiet world, pure autonomy.

**Open**: template data format (shared with petitions) · reads-broadly
must narrow to declared state at spec time.
