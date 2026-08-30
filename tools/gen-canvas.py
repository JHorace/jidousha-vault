#!/usr/bin/env python3
"""Generate Jidousha/dependency.canvas from capsule/currency/foundation
frontmatter. Derived, never drawn; positions of existing nodes are
preserved unless --fresh.

Usage (from vault repo root):
  python3 tools/gen-canvas.py                 # all edge types
  python3 tools/gen-canvas.py --fresh         # relayout from scratch
  python3 tools/gen-canvas.py --edges=requires --out=structure.canvas
  python3 tools/gen-canvas.py --hide=knowledge,threats
  python3 tools/gen-canvas.py --dump-json     # print registry JSON only
"""
import json, os, re, sys

ARGS = {a.split("=")[0]: (a.split("=", 1)[1] if "=" in a else True)
        for a in sys.argv[1:]}
VAULT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "Jidousha"))
OUT = os.path.join(VAULT, str(ARGS.get("--out", "dependency.canvas")))
SCAN = ["foundation", "currencies", "capsules"]
WIKI = re.compile(r"\[\[([^\]|#]+)")
EDGE_KINDS = [k for k in str(ARGS.get("--edges", "requires,reads,writes")).split(",") if k]
HIDE = set(str(ARGS.get("--hide", "")).split(",")) - {""}

CONF_COLOR = {"speculative": "1", "mocked": "2", "played": "3", "proven": "4"}
EDGE_COLOR = {"requires": "1", "reads": "5", "writes": "2"}

def parse(path):
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    fm, key, h1, in_fm = {}, None, None, False
    body_start = 0
    if lines and lines[0].strip() == "---":
        in_fm = True
        for i, ln in enumerate(lines[1:], 1):
            if ln.strip() == "---":
                body_start = i + 1
                break
            m = re.match(r"^([A-Za-z][\w-]*):(.*)$", ln)
            if m:
                key = m.group(1); fm[key] = m.group(2).strip()
            elif key and ln.strip().startswith("- "):
                fm[key] = fm.get(key, "") + " " + ln.strip()[2:]
    for ln in lines[body_start:]:
        if ln.startswith("# "):
            h1 = ln[2:].strip(); break
    return fm, h1

notes = {}
for sub in SCAN:
    d = os.path.join(VAULT, sub)
    if not os.path.isdir(d): continue
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"): continue
        fm, h1 = parse(os.path.join(d, fn))
        stem = fn[:-3]
        notes[stem] = {
            "id": stem, "band": sub, "file": f"{sub}/{fn}", "h1": h1,
            "tier": fm.get("tier", ""), "conf": fm.get("confidence", "speculative"),
            "status": fm.get("status", ""), "reviewed": fm.get("last-reviewed", ""),
            "requires": WIKI.findall(fm.get("requires", "")),
            "reads": WIKI.findall(fm.get("reads", "")),
            "writes": WIKI.findall(fm.get("writes", "")),
            "attention": fm.get("attention", "").strip('"'),
        }

if ARGS.get("--dump-json"):
    json.dump(list(notes.values()), sys.stdout, indent=1)
    sys.exit(0)

for nid in HIDE:
    if nid in notes: del notes[nid]

def mod_depth(nid, seen=frozenset()):
    n = notes[nid]
    if n["band"] != "capsules": return 0
    if nid in seen: return 1
    deps = [d for d in n["requires"] if d in notes and notes[d]["band"] == "capsules"]
    return 1 if not deps else 1 + max(mod_depth(d, seen | {nid}) for d in deps)

for n in notes.values():
    n["depth"] = mod_depth(n["id"])

W = {"foundation": 340, "currencies": 340, "capsules": 420}
H = {"foundation": 200, "currencies": 220, "capsules": 320}
GAP = 180
def band_y(n):
    if n["band"] == "foundation": return 2200
    if n["band"] == "currencies": return 1450
    return 700 - (n["depth"] - 1) * 800

old_pos = {}
if os.path.exists(OUT) and not ARGS.get("--fresh"):
    try:
        for nd in json.load(open(OUT, encoding="utf-8")).get("nodes", []):
            if nd.get("type") == "file":
                old_pos[nd["id"]] = (nd["x"], nd["y"], nd["width"], nd["height"])
    except Exception as e:
        print(f"warn: old canvas unreadable ({e})", file=sys.stderr)

rows = {}
for n in notes.values():
    rows.setdefault((n["band"], band_y(n)), []).append(n)

nodes = []
for (band, y), row in rows.items():
    row.sort(key=lambda n: (n["tier"] != "mvp", n["id"]))
    w, h = W[band], H[band]
    total = len(row) * (w + GAP) - GAP
    x0 = -total // 2
    for i, n in enumerate(row):
        x, ny, nw, nh = old_pos.get(n["id"], (x0 + i * (w + GAP), y, w, h))
        n["x"], n["y"], n["w"], n["h"] = x, ny, nw, nh
        node = {"id": n["id"], "type": "file", "file": n["file"],
                "x": x, "y": ny, "width": nw, "height": nh,
                "color": CONF_COLOR.get(n["conf"], "1")}
        nodes.append(node)

def group(gid, label, members):
    if not members: return None
    x0 = min(m["x"] for m in members) - 80
    y0 = min(m["y"] for m in members) - 100
    x1 = max(m["x"] + m["w"] for m in members) + 80
    y1 = max(m["y"] + m["h"] for m in members) + 80
    return {"id": gid, "type": "group", "label": label,
            "x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0}

for gid, label, band in [("g-foundation", "FOUNDATION (spine)", "foundation"),
                         ("g-shared", "SHARED STATE (currencies / facts)", "currencies"),
                         ("g-modules", "SYSTEM MODULES (capsules)", "capsules")]:
    g = group(gid, label, [n for n in notes.values() if n["band"] == band])
    if g: nodes.append(g)

nodes.append({"id": "legend", "type": "text", "x": -2600, "y": 2200,
              "width": 480, "height": 340, "text":
              "# Key\n**Node color** = confidence\n"
              "red speculative / orange mocked\nyellow played / green proven\n\n"
              "**Edge color** = type\nred requires / cyan reads / orange writes\n\n"
              "Generated by tools/gen-canvas.py.\nDrag freely (positions survive "
              "regen).\nEdit frontmatter + regenerate; never\nadd nodes/edges here. "
              "Views:\n--edges=requires --out=structure.canvas"})

edges = []
for n in notes.values():
    for kind in EDGE_KINDS:
        for tgt in n.get(kind, []):
            if tgt not in notes:
                if tgt not in HIDE:
                    print(f"warn: {n['id']} {kind} unknown [[{tgt}]]", file=sys.stderr)
                continue
            t = notes[tgt]
            if n["y"] < t["y"]: fs, ts = "bottom", "top"
            elif n["y"] > t["y"]: fs, ts = "top", "bottom"
            else: fs, ts = ("right", "left") if n["x"] < t["x"] else ("left", "right")
            edges.append({"id": f"{n['id']}--{kind}--{tgt}",
                          "fromNode": n["id"], "fromSide": fs,
                          "toNode": tgt, "toSide": ts, "color": EDGE_COLOR[kind]})

json.dump({"nodes": nodes, "edges": edges}, open(OUT, "w", encoding="utf-8"), indent="\t")
print(f"wrote {OUT}: {len([x for x in nodes if x['type']=='file'])} notes, {len(edges)} edges")
