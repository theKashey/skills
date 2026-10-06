#!/usr/bin/env python3
"""Render a blueprint to one offline HTML page and check it renders on GitHub.

Usage: render.py .blueprints/<slug>.md

Writes <slug>.html beside the blueprint, using only the Python standard
library: the Markdown as HTML, a subset of flowchart, stateDiagram-v2, and
sequenceDiagram drawn as inline SVG, a legend built from the blueprint's own
classDef lines, and each block's or question's table row shown on hover. A
view outside that subset, or one whose drawing would lose any of its text,
stays as Mermaid source on the page. The layout is simpler than GitHub's; the
Markdown stays the source.

Each hazard that would break a view pasted into GitHub prints as
path:line: message. Exit 0 when the page is written with no hazard, 1 when a
hazard is found (the page is still written), 2 when the blueprint cannot be
read or the page cannot be written.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

E = html.escape
FENCE = re.compile(r"^\s*(`{3,}|~{3,})\s*([^\s`]*)")
CLASSDEF = re.compile(r"^\s*classDef\s+([\w-]+)\s+(.+?);?\s*$")
ROW_ID = re.compile(r"^\|\s*([BQ]\d+)\s*\|(.+)\|\s*$")
COMMIT = re.compile(r"\b[0-9a-f]{7,40}\b")

# --- GitHub hazards -------------------------------------------------------

DIAGRAM_START = re.compile(r"^\s*(flowchart|graph|sequenceDiagram|stateDiagram)")
HAZARDS = [
    (re.compile(r"^\s*(click|callback)\s+[A-Za-z_]\w*\b|^\s*links?\s+[\w-]+\s*:"),
     "GitHub disables click, link, and tooltip directives"),
    (re.compile(r"<(?!br\s*/?>)[A-Za-z/][^>]*>", re.I),
     "HTML other than <br> in a diagram; GitHub strips it"),
    (re.compile(r"(--?>>|--?x|--?\))[+-]"),
     "`+` or `-` right after an arrow means activate; put the marker after the colon"),
    (re.compile(r"\b[\w-]+[\[{](?![\"(\[{])[^\]}\"]*[()\"]"),
     'a label holding brackets or quotes must be quoted, as ["..."]'),
    (re.compile(r"^\s*%%\{\s*init.*\btheme\b|^\s*theme\s*:"),
     "a theme directive stops GitHub following light and dark mode"),
]


def check(path: Path, lines: list[str]) -> list[str]:
    found, fence, lang, first = [], None, "", False
    for n, line in enumerate(lines, 1):
        m = FENCE.match(line)
        if fence is None:
            if m:
                fence, lang, first = m.group(1), m.group(2), True
            continue
        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2):
            fence = None
            continue
        if lang != "mermaid":
            if first and DIAGRAM_START.match(line):
                found.append(f"{path}:{n}: diagram fence lacks the `mermaid` info string")
            first = False
            continue
        first = False
        skip_labels = line.lstrip().startswith(("classDef", "class ", "style "))
        for rx, msg in HAZARDS:
            if rx.search(line) and not (skip_labels and "quoted" in msg):
                found.append(f"{path}:{n}: {msg}")
    if fence is not None:
        found.append(f"{path}:{len(lines)}: fence never closed")
    return found

# --- Mermaid subset to SVG ------------------------------------------------

NODE = r"([\w-]+|\[\*\])(?:\s*(\[\[|\[\(|\(\[|\(\(|\[|\(|\{\{|\{|>)(.*?)(\]\]|\)\]|\]\)|\)\)|\]|\)|\}\}|\}))?(?::::([\w-]+))?"
ARROW = r"\s*(-->|---|-\.->|-\.-|==>|--x|--o|--\s[^-][^>]*?-->)(?:\|([^|]*)\|)?\s*"
EDGE_LINE = re.compile(rf"^{NODE}(?:{ARROW}{NODE})+(?:\s*:\s*(.*))?$")
NODE_RE, ARROW_RE = re.compile(NODE), re.compile(ARROW)
W, H, GAP_X, GAP_Y, CH = 168, 44, 28, 54, 6.6


def label(raw: str | None, ident: str) -> str:
    text = (raw or ident).strip().strip('"')
    return re.sub(r"<br\s*/?>", "\n", text)


def wrap(text: str, width: int = W - 16) -> list[str]:
    out = []
    for para in text.split("\n"):
        line = ""
        for word in para.split():
            if line and (len(line) + 1 + len(word)) * CH > width:
                out.append(line)
                line = word
            else:
                line = f"{line} {word}".strip()
        out.append(line)
    return out


def style(spec: str) -> dict[str, str]:
    return {k.strip(): v.strip() for k, _, v in (p.partition(":") for p in spec.split(","))}


def parse_graph(body: list[str], state: bool):
    nodes, edges, groups, classes, stack, notes = {}, [], {}, {}, [], []
    lines = iter(body)

    def add(ident, raw, cls, end=""):
        ident = ident + end if ident == "[*]" else ident
        node = nodes.setdefault(ident, {"label": ident, "cls": None, "group": None})
        if raw is not None:
            node["label"] = label(raw, ident)
        if cls:
            node["cls"] = cls
        if stack and node["group"] is None:
            node["group"] = stack[-1]
        return ident

    for line in lines:
        s = line.strip()
        if not s or s.startswith(("%%", "direction")):
            continue
        if state and (m := re.match(r"^note\s+(?:left|right)\s+of\s+([\w-]+)\s*(?::\s*(.*))?$", s)):
            text = m.group(2)
            if text is None:  # a block note runs to `end note`
                block = []
                for inner in lines:
                    if inner.strip() == "end note":
                        break
                    block.append(inner.strip())
                else:
                    return None
                text = "\n".join(block)
            notes.append((add(m.group(1), None, None), text.strip()))
        elif m := CLASSDEF.match(s):
            classes[m.group(1)] = style(m.group(2))
        elif m := re.match(r"^subgraph\s+([\w-]+)?\s*(?:\[\"?(.*?)\"?\])?\s*(.*)$", s):
            gid = m.group(1) or f"g{len(groups)}"
            groups[gid] = label(m.group(2) or m.group(3) or gid, gid)
            if stack:  # boxes are not nested, so a box names its outer groups
                groups[gid] = f"{groups[stack[-1]]} › {groups[gid]}"
            stack.append(gid)
        elif s == "end" or s == "}":
            stack and stack.pop()
        elif m := re.match(r"^class\s+([\w,-]+)\s+([\w-]+)", s):
            for ident in m.group(1).split(","):
                add(ident, None, m.group(2))
        elif m := re.match(r'^state\s+"(.*?)"\s+as\s+([\w-]+)$', s):
            add(m.group(2), m.group(1), None)
        elif state and (m := re.match(r"^([\w-]+)\s*:\s*(.+)$", s)):
            ident = add(m.group(1), None, None)
            nodes[ident]["label"] += "\n" + m.group(2).strip()
        elif EDGE_LINE.match(s):
            core, _, tail = s.partition(":") if state else (s, "", "")
            pos, prev = 0, None
            while True:
                nm = NODE_RE.match(core, pos)
                if not nm:
                    return None
                end = " start" if prev is None else " end"
                ident = add(nm.group(1), nm.group(3), nm.group(5), end)
                if prev is not None:
                    edges.append((prev[0], ident, prev[1] or tail.strip(), prev[2]))
                pos = nm.end()
                am = ARROW_RE.match(core, pos)
                if not am or pos >= len(core):
                    if core[pos:].strip():  # unparsed rest: draw nothing
                        return None
                    break
                text = am.group(2) or (am.group(1)[2:-3].strip() if am.group(1).startswith("-- ") else "")
                prev, pos = (ident, text, "." in am.group(1)), am.end()
        elif nm := NODE_RE.fullmatch(s):
            add(nm.group(1), nm.group(3), nm.group(5))
        else:
            return None
    return nodes, edges, groups, classes, notes


def draw_graph(body: list[str], hover: dict[str, str]) -> str | None:
    parsed = parse_graph(body[1:], body[0].strip().startswith("state"))
    if not parsed or not parsed[0]:
        return None
    nodes, edges, groups, classes, notes = parsed
    rank, seen, back = {n: 0 for n in nodes}, set(), set()

    def visit(n, path):  # edges into the current path are back edges
        seen.add(n)
        for i, (a, b, *_) in enumerate(edges):
            if a == n:
                if b in path:
                    back.add(i)
                elif b not in seen:
                    visit(b, path | {b})

    for n in nodes:
        n in seen or visit(n, {n})
    for _ in nodes:
        for i, (a, b, *_) in enumerate(edges):
            if i not in back and rank[b] <= rank[a]:
                rank[b] = rank[a] + 1
    columns = list(dict.fromkeys([nodes[n]["group"] for n in nodes]))
    slots: dict[tuple, list] = {}
    for n in nodes:
        slots.setdefault((nodes[n]["group"], rank[n]), []).append(n)
    width = {g: max(len(v) for (gg, _), v in slots.items() if gg == g) for g in columns}
    pos, x0 = {}, 48  # the left margin is the channel for back edges
    lines_of = {n: wrap(nodes[n]["label"]) for n in nodes}
    tall = max(len(v) for v in lines_of.values())
    nh = max(H, 16 + 16 * tall)
    for g in columns:
        for (gg, r), members in slots.items():
            if gg == g:
                for i, n in enumerate(members):
                    pos[n] = (x0 + 12 + i * (W + GAP_X), 40 + r * (nh + GAP_Y))
        x0 += width[g] * (W + GAP_X) + 24
    out = []
    for g in columns:
        if g is None:
            continue
        xs = [pos[n][0] for n in nodes if nodes[n]["group"] == g]
        ys = [pos[n][1] for n in nodes if nodes[n]["group"] == g]
        x, y = min(xs) - 12, min(ys) - 28
        out.append(f'<rect x="{x}" y="{y}" width="{max(xs) - x + W + 12}" height="{max(ys) - y + nh + 12}" rx="6" fill="#f6f8fa" stroke="#d0d7de"/>'
                   f'<text x="{x + 8}" y="{y + 17}" class="g">{E(groups.get(g, g))}</text>')
    key = []
    name = lambda n: nodes[n]["label"].replace("[*] ", "").split("\n")[0]
    for k, (a, b, text, dotted) in enumerate(edges):
        (ax, ay), (bx, by) = pos[a], pos[b]
        if a == b:
            sx, sy = ax + W, ay + nh * 0.3
            d = f"M{sx},{sy} c34,0 34,{nh * 0.4} 0,{nh * 0.4}"
            lx, ly = sx + 30, sy + nh * 0.2
        elif by <= ay:
            ch, sy, ty = 12 + k % 4 * 8, ay + nh / 2, by + nh / 2
            d = f"M{ax},{sy} H{ch} V{ty} H{bx}"
            lx, ly = ch, (sy + ty) / 2
        elif ax == bx and rank[b] - rank[a] > 1:  # skip past the nodes between
            sx, sy, ty = ax + W, ay + nh / 2, by + nh / 2
            d = f"M{sx},{sy} C{sx + 26},{sy} {sx + 26},{ty} {sx},{ty}"
            lx, ly = sx + 20, (sy + ty) / 2
        else:
            sx, sy, tx, ty = ax + W / 2, ay + nh, bx + W / 2, by
            d = f"M{sx},{sy} C{sx},{(sy + ty) / 2} {tx},{(sy + ty) / 2} {tx},{ty}"
            lx, ly = tx + (sx - tx) * 0.2, ty - 14  # just above the target
        dash = ' stroke-dasharray="4 3"' if dotted else ""
        out.append(f'<path d="{d}" class="e"{dash} marker-end="url(#a)"/>')
        if len(text) <= 14:  # short labels such as + and − sit on the edge
            text and out.append(f'<text x="{lx + 5}" y="{ly + 4}" class="l">{E(text)}</text>')
        else:  # long ones become a numbered badge and a key line
            key.append(f"<li>{E(name(a))} → {E(name(b))}: {inline(text)}</li>")
            out.append(f'<circle cx="{lx}" cy="{ly}" r="8" class="k"/>'
                       f'<text x="{lx}" y="{ly + 4}" text-anchor="middle" class="kn">{len(key)}</text>')
    for n, node in nodes.items():
        x, y = pos[n]
        st = {k: E(v) for k, v in classes.get(node["cls"] or "", {}).items()}
        circle = n.startswith("[*]")
        if circle:
            ring = '<circle r="11" fill="none" stroke="#1f2328"/>' if n.endswith("end") else ""
            out.append(f'<g transform="translate({x + W / 2},{y + nh / 2})">{ring}<circle r="7" fill="#1f2328"/></g>')
            continue
        attrs = (f'fill="{st.get("fill", "#fff")}" stroke="{st.get("stroke", "#57606a")}" '
                 f'stroke-width="{st.get("stroke-width", "1.5").rstrip("px")}"'
                 + (f' stroke-dasharray="{st["stroke-dasharray"].replace(" ", ",")}"' if "stroke-dasharray" in st else ""))
        tip = hover.get(re.split(r"\W", node["label"] + " ")[0], "")
        out.append(f'<g>{f"<title>{E(tip)}</title>" if tip else ""}<rect x="{x}" y="{y}" width="{W}" height="{nh}" rx="5" {attrs}/>')
        ty0 = y + nh / 2 - (len(lines_of[n]) - 1) * 8 + 4
        for i, t in enumerate(lines_of[n]):
            out.append(f'<text x="{x + W / 2}" y="{ty0 + i * 16}" text-anchor="middle" fill="{st.get("color", "#1f2328")}">{E(t)}</text>')
        out.append("</g>")
    for n, text in notes:  # a note keeps its constraint as a keyed badge
        x, y = pos[n]
        key.append(f'<li class="nt">Note on {E(name(n))}: {inline(text).replace(chr(10), "<br>")}</li>')
        out.append(f'<circle cx="{x + W - 4}" cy="{y + 4}" r="8" class="nb"/>'
                   f'<text x="{x + W - 4}" y="{y + 8}" text-anchor="middle" class="kn">{len(key)}</text>')
    vh = 40 + (max(rank.values()) + 1) * (nh + GAP_Y)
    return svg(x0 + 60, vh, out) + (f'<ol class="key">{"".join(key)}</ol>' if key else "")


def draw_sequence(body: list[str]) -> str | None:
    parts, rows, number = {}, [], None
    for line in body:
        s = line.strip()
        if not s or s.startswith("%%"):
            continue
        if s == "autonumber":
            number = 0
            continue
        if m := re.match(r"^(participant|actor)\s+([\w-]+)(?:\s+as\s+(.*))?$", s):
            parts.setdefault(m.group(2), m.group(3) or m.group(2))
        elif m := re.match(r"^(\w+(?:-\w+)*)\s*(--?>>|--?>|--?x|--?\))\s*(\w+(?:-\w+)*)\s*:\s*(.*)$", s):
            for p in (m.group(1), m.group(3)):
                parts.setdefault(p, p)
            text = m.group(4)
            if number is not None:
                number += 1
                text = f"{number}. {text}"
            rows.append(("msg", m.group(1), m.group(3), text, m.group(2).startswith("--")))
        elif m := re.match(r"^[Nn]ote\s+(?:over|left of|right of)\s+([\w-]+)(?:\s*,\s*([\w-]+))?\s*:\s*(.*)$", s):
            for p in filter(None, (m.group(1), m.group(2))):
                parts.setdefault(p, p)
            rows.append(("note", m.group(1), m.group(2) or m.group(1), m.group(3), False))
        elif m := re.match(r"^(alt|else|opt|loop|par|and|critical|break|rect)\b\s*(.*)$", s):
            rows.append(("frame", m.group(1), "", m.group(2), False))
        elif s == "end":
            rows.append(("end", "", "", "", False))
        else:
            return None
    if not parts:
        return None
    col = {p: 16 + i * (W + 40) for i, p in enumerate(parts)}
    out, y, opened = [], 70, []
    for kind, a, b, text, dashed in rows:
        if kind == "msg":
            x1, x2 = col[a] + W / 2, col[b] + W / 2
            dash = ' stroke-dasharray="4 3"' if dashed else ""
            if a == b:
                out.append(f'<path d="M{x1},{y} h40 v18 h-40" class="e"{dash} marker-end="url(#a)"/>')
            else:
                out.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="e"{dash} marker-end="url(#a)"/>')
            out.append(f'<text x="{(x1 + x2) / 2 + (30 if a == b else 0)}" y="{y - 6}" text-anchor="middle" class="l">{E(text)}</text>')
            y += 40
        elif kind == "note":
            x1, x2 = min(col[a], col[b]), max(col[a], col[b]) + W
            out.append(f'<rect x="{x1}" y="{y - 18}" width="{x2 - x1}" height="26" fill="#fff8c5" stroke="#d4a72c"/>'
                       f'<text x="{(x1 + x2) / 2}" y="{y}" text-anchor="middle">{E(text)}</text>')
            y += 40
        elif kind == "frame":
            out.append(f'<text x="20" y="{y - 4}" class="g">{E(a)} {E(text)}</text>')
            if a in ("else", "and"):
                out.append(f'<line x1="8" y1="{y - 20}" x2="{16 + len(parts) * (W + 40) - 32}" y2="{y - 20}" class="f"/>')
            else:
                opened.append(y - 20)
            y += 28
        elif kind == "end" and opened:
            top = opened.pop()
            out.append(f'<rect x="8" y="{top}" width="{len(parts) * (W + 40) - 24}" height="{y - top - 16}" class="f" fill="none"/>')
            y += 8
    head = []
    for p, name in parts.items():
        x = col[p]
        head.append(f'<line x1="{x + W / 2}" y1="48" x2="{x + W / 2}" y2="{y}" stroke="#d0d7de"/>'
                    f'<rect x="{x}" y="8" width="{W}" height="40" rx="5" fill="#fff" stroke="#57606a"/>'
                    f'<text x="{x + W / 2}" y="33" text-anchor="middle">{E(name)}</text>')
    return svg(16 + len(parts) * (W + 40), y + 8, head + out)


def svg(w: float, h: float, body: list[str]) -> str:
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img">'
            '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#57606a"/></marker></defs>' + "".join(body) + "</svg>")


SYNTAX = set("flowchart graph TB TD BT LR RL stateDiagram v2 sequenceDiagram subgraph end state as "
              "note left right of over participant actor".split())
QUIET = re.compile(r"^\s*(%%|direction\b|classDef\b|class\s|end\s*$|\}\s*$|autonumber\s*$|$)")
WORD = re.compile(r"[^\W_]+|[+−~⚠]")


def words(text: str) -> set[str]:
    return set(WORD.findall(text))


def lost(code: list[str], drawn: str) -> list[str]:
    """Words of the source that the drawing does not show.

    Every line except comments and styling or layout directives must leave its
    words in the drawing, so a line the parser accepted but did not draw
    sends the view back to its source instead of vanishing.
    """
    ids = set()  # names a drawn label or alias stands in for
    for line in code[1:]:
        ids |= set(re.findall(r"(\w+(?:-\w+)*)(?:\[|\(|\{|>(?!>)|@\{)", line))
        ids |= set(re.findall(r"\b(?:participant|actor)\s+([\w-]+)\s+as\b", line))
        ids |= set(re.findall(r'^\s*state\s+".*"\s+as\s+([\w-]+)\s*$', line))
        ids |= set(re.findall(r":::([\w-]+)", line))
    ids = {w for i in ids for w in WORD.findall(i)}
    shown = words(html.unescape(re.sub(r"<title>.*?</title>|<[^>]+>", " ", drawn)))
    need = set()
    for line in code[1:]:
        if not QUIET.match(line):
            text = re.sub(r"<br\s*/?>|:::[\w-]+", " ", line)
            need |= words(re.sub(r"[-=.]*-[-=.]*(?:>>|>|x\b|o\b|\))?|==>", " ", text))
    return sorted(need - shown - ids - SYNTAX)


def diagram(code: list[str], hover: dict[str, str]) -> str:
    head = code[0].strip() if code else ""
    drawn = None
    try:
        if head.startswith(("flowchart", "graph", "stateDiagram")):
            drawn = draw_graph(code, hover)
        elif head.startswith("sequenceDiagram"):
            drawn = draw_sequence(code[1:])
    except (KeyError, ValueError, IndexError, AttributeError, RecursionError):
        drawn = None
    why = "outside the subset this page draws"
    if drawn and (missing := lost(code, drawn)):
        why, drawn = f"drawing it would drop {', '.join(missing[:6])}", None
    if drawn:
        return f'<figure class="d">{drawn}</figure>'
    return f'<pre class="raw"><code>{E(chr(10).join(code))}</code></pre><p class="note">Left as Mermaid source: {E(why)}.</p>'

# --- Markdown subset to HTML ----------------------------------------------


def inline(text: str) -> str:
    spans: list[str] = []

    def keep(m):
        spans.append(f"<code>{E(m.group(1))}</code>")
        return f"\0{len(spans) - 1}\0"

    text = E(re.sub(r"`([^`]+)`", keep, text))
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)\*(?!\w)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    return re.sub(r"\0(\d+)\0", lambda m: spans[int(m.group(1))], text)


def cells(row: str) -> list[str]:
    return [c.strip() for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]


def markdown(lines: list[str], hover: dict[str, str]) -> str:
    out, i, para = [], 0, []

    def flush():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        if m := FENCE.match(line):
            flush()
            fence, lang, code = m.group(1), m.group(2), []
            i += 1
            while i < len(lines) and not ((c := FENCE.match(lines[i])) and c.group(1)[0] == fence[0]
                                          and len(c.group(1)) >= len(fence) and not c.group(2)):
                code.append(lines[i])
                i += 1
            out.append(diagram(code, hover) if lang == "mermaid" else f"<pre><code>{E(chr(10).join(code))}</code></pre>")
        elif m := re.match(r"^(#{1,6})\s+(.*)$", line):
            flush()
            out.append(f"<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>")
        elif line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            flush()
            rows = [f"<tr>{''.join(f'<th>{inline(c)}</th>' for c in cells(line))}</tr>"]
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(f"<tr>{''.join(f'<td>{inline(c)}</td>' for c in cells(lines[i]))}</tr>")
                i += 1
            out.append(f"<table>{''.join(rows)}</table>")
            continue
        elif m := re.match(r"^\s*([-*]|\d+\.)\s+(.*)$", line):
            flush()
            tag, items = ("ol" if m.group(1)[0].isdigit() else "ul"), []
            while i < len(lines) and (m := re.match(r"^\s*([-*]|\d+\.)\s+(.*)$", lines[i])):
                item = [m.group(2)]
                i += 1
                while i < len(lines) and re.match(r"^\s{2,}\S", lines[i]) and not re.match(r"^\s*([-*]|\d+\.)\s", lines[i]):
                    item.append(lines[i].strip())
                    i += 1
                items.append(f"<li>{inline(' '.join(item))}</li>")
            out.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue
        elif line.startswith(">"):
            flush()
            out.append(f"<blockquote>{inline(line.lstrip('> '))}</blockquote>")
        elif not line.strip():
            flush()
        else:
            para.append(line.strip())
        i += 1
    flush()
    return "\n".join(out)

# --- Page -----------------------------------------------------------------

CSS = """body{margin:0;font:14px/1.5 -apple-system,system-ui,"Segoe UI",sans-serif;color:#1f2328;background:#fff}
.bar{position:sticky;top:0;z-index:1;background:#f6f8fa;border-bottom:1px solid #d0d7de;padding:8px 16px}
.bar small{color:#59636e;margin-left:12px}.chip{display:inline-block;border:1px solid;border-radius:4px;padding:0 6px;margin:4px 4px 0 0;font-size:12px}
main{max-width:1200px;margin:0 auto;padding:8px 16px 48px}table{border-collapse:collapse;display:block;overflow-x:auto}
td,th{border:1px solid #d0d7de;padding:4px 8px;vertical-align:top}code{background:#eff1f3;padding:1px 4px;border-radius:4px;font-size:90%}
pre{overflow-x:auto;background:#f6f8fa;padding:8px}.d{margin:12px 0;overflow-x:auto}.note{color:#9a6700;font-size:12px}
svg{font:12px system-ui,sans-serif;max-width:none}svg .e{fill:none;stroke:#57606a;stroke-width:1.4}svg .l{fill:#57606a;font-size:11px;paint-order:stroke;stroke:#fff;stroke-width:4px}
svg .g{fill:#59636e;font-weight:600}svg .k{fill:#fff;stroke:#57606a}svg .nb{fill:#fff8c5;stroke:#d4a72c}svg .kn{font-size:10px;font-weight:600}
.key .nt{background:#fff8c5}
.key{margin:4px 0 0;font-size:13px;color:#59636e}svg .f{stroke:#8c959f;stroke-dasharray:5 4;fill:none}
@media print{.bar{position:static}.d,table{break-inside:avoid}}"""


def page(md: str) -> str:
    lines = md.splitlines()
    hover = {}
    for line in lines:
        if (m := ROW_ID.match(line.strip())) and m.group(1) not in hover:
            hover[m.group(1)] = " · ".join(re.sub(r"[`*]", "", c) for c in cells(m.group(2)) if c and c != "—")[:600]
    legend = {}
    for line in lines:
        if (m := CLASSDEF.match(line)) and m.group(1) not in legend:
            st = style(m.group(2))
            legend[m.group(1)] = (f'background:{st.get("fill", "#fff")};border-color:{st.get("stroke", "#888")};'
                                  f'color:{st.get("color", "#1f2328")}' + (";border-style:dashed" if "stroke-dasharray" in st else ""))
    chips = "".join(f'<span class="chip" style="{E(s)}">{E(n)}</span>' for n, s in legend.items())
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "Blueprint")
    read_at = next((l.strip() for l in lines[:15] if COMMIT.search(l) and not l.startswith("#")), "")
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title.replace("`", ""))}</title><style>{CSS}</style></head><body>'
            f'<div class="bar"><b>{inline(title)}</b><small>{inline(read_at)}</small><div>{chips}</div></div>'
            f"<main>{markdown(lines, hover)}</main></body></html>\n")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("blueprint", type=Path)
    args = parser.parse_args(argv)
    try:
        md = args.blueprint.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        print(f"render.py: {error}", file=sys.stderr)
        return 2
    out = args.blueprint.with_suffix(".html")  # inside the excluded folder
    try:
        out.write_text(page(md), encoding="utf-8")
    except OSError as error:
        print(f"render.py: {error}", file=sys.stderr)
        return 2
    hazards = check(args.blueprint, md.splitlines())
    print("\n".join(hazards + [f"wrote {out}"]))
    return 1 if hazards else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
