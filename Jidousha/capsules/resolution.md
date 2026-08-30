---
type: capsule
id: resolution
name: Resolution
status: sketch
tier: mvp
wave:
confidence: speculative
last-reviewed: 2026-08-29
requires: ["[[map-grid]]", "[[clock-rtwp]]", "[[trait-vocabulary]]"]
reads: ["[[wealth]]"]
writes: ["[[wealth]]"]
emits: [task-complete, task-failed]
consumes: []
attention: "outcomes are feed events at the task's place"
tags: [conf/speculative]
---
# Resolution
**Fantasy**: work takes time at a place, and who you sent matters.

**Loop**: outcomes read **aptitude-kind traits** (decided 2026-08-29:
aptitudes join the trait vocabulary as a kind; no separate skill
sheet). Duration + aptitudes -> outcome quality.

**Degrades to**: headcount + duration always-succeeds - the current
giri-rt stub, already landed.

**Open**: outcome granularity (binary? tiered?); failure consequences;
how party composition ([[parties]]) folds in.
