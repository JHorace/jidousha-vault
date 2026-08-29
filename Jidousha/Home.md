---
role: vault-home
---

# Jidousha vault — home

This vault is the project's **thinking layer**: brainstorm residue,
capsules in progress, playtest notes, working drafts. The layers above
it: the **GitHub repo is canonical** for anything decided; the Claude
**project docs** carry orientation and session-critical state (they are
visible from every device — this vault is desktop-only for Claude
sessions). Hard rule: **nothing session-critical lives only here** — at
the end of any session that works in this vault, whatever the next
session needs is mirrored to the project docs.

## Conventions (accumulate here as they settle)

- One note per **system-module capsule**, in `capsules/` (arrives with
  the brainstorm session). Capsule frontmatter is the machine-readable
  module registry — the dependency graph artifact, the repo mermaid,
  and Dataview views are all generated from it. One source.
- Wikilinks in capsule frontmatter/fields (`requires`, `reads`,
  `writes`, `events`) so Obsidian's graph view doubles as the live
  dependency graph.
- Claude writes only inside agreed subtrees; the owner writes anywhere.
- Owner: James Sumihiro. Claude sessions read this note first.
