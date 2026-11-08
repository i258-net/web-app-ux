#!/usr/bin/env python3
"""Validate the web-app-ux knowledge repository.

Checks:
  - every authoritative .md file (outside research/, assets/, scripts/) has YAML front matter with id, title, type, status, updated
  - ids are unique
  - cross-references in front matter (principles, patterns, dimensions, gates, related) resolve to known ids
  - relative markdown links resolve to existing files
  - pattern files have the required body sections
  - INDEX.md lists every id (run with --write-index to regenerate)

Usage: python3 scripts/validate.py [--write-index] [--check-urls]
No third-party dependencies.
"""
from __future__ import annotations
import os, re, sys, json, urllib.request, urllib.error, concurrent.futures

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "assets", "scripts", "research", ".github", "node_modules"}
REQUIRED_FM = ["id", "title", "type", "status", "updated"]
PATTERN_SECTIONS = ["Problem", "Recommendation", "Evidence", "Alternatives and tradeoffs",
                    "Exceptions and failure modes", "Evaluation questions", "Related"]
GATE_RE = re.compile(r"^\| (QG-\d{3}[a-z]?) \|", re.M)
DIM_RE = re.compile(r"^## (D-\d{2}) ", re.M)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
URL_RE = re.compile(r"https?://[^\s)\]>\"'`]+")

def parse_front_matter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    block = text[4:end]
    fm = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            items = [i.strip().strip("'\"") for i in v[1:-1].split(",") if i.strip()]
            fm[k.strip()] = items
        else:
            fm[k.strip()] = v.strip("'\"")
    return fm, text[end + 4:]

def md_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)

def main():
    write_index = "--write-index" in sys.argv
    check_urls = "--check-urls" in sys.argv
    errors, warnings = [], []
    ids = {}        # id -> relpath
    docs = []       # (relpath, fm, body)
    all_urls = set()

    for path in md_files():
        rel = os.path.relpath(path, ROOT)
        text = open(path, encoding="utf-8").read()
        fm, body = parse_front_matter(text)
        all_urls.update(u.rstrip('.,;:`') for u in URL_RE.findall(text))
        if rel in ("README.md", "INDEX.md", "CONTRIBUTING.md") or rel.startswith("evaluation/checklists/"):
            docs.append((rel, fm or {}, body))
            # README and INDEX are exempt from front matter
        else:
            if fm is None:
                errors.append(f"{rel}: missing front matter")
                continue
            for k in REQUIRED_FM:
                if k not in fm:
                    errors.append(f"{rel}: front matter missing '{k}'")
            docs.append((rel, fm, body))
        if fm and "id" in fm:
            if fm["id"] in ids:
                errors.append(f"{rel}: duplicate id {fm['id']} (also {ids[fm['id']]})")
            ids[fm["id"]] = rel
        # register embedded ids: gates and dimensions
        for m in GATE_RE.finditer(text):
            ids.setdefault(m.group(1), rel)
        for m in DIM_RE.finditer(text):
            ids.setdefault(m.group(1), rel)

    # cross references and links
    for rel, fm, body in docs:
        for key in ("principles", "patterns", "dimensions", "gates", "related", "superseded_by"):
            vals = fm.get(key, [])
            if isinstance(vals, str):
                vals = [vals]
            for v in vals:
                if v.endswith("*"):
                    continue
                if v not in ids:
                    errors.append(f"{rel}: front matter {key} references unknown id {v}")
        for m in LINK_RE.finditer(body):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#", "viking://")):
                continue
            target = target.split("#")[0]
            if not target:
                continue
            abs_t = os.path.normpath(os.path.join(ROOT, os.path.dirname(rel), target))
            if not os.path.exists(abs_t):
                errors.append(f"{rel}: broken link {m.group(1)}")
        if fm.get("type") == "pattern":
            for sec in PATTERN_SECTIONS:
                if not re.search(rf"^## {re.escape(sec)}\b", body, re.M):
                    errors.append(f"{rel}: pattern missing section '## {sec}'")
            if not re.search(r"\bE[1-5]\b", body):
                warnings.append(f"{rel}: pattern has no evidence class tags (E1–E5)")
            for k in ("scope", "platforms", "inputs", "principles", "dimensions"):
                if k not in fm:
                    errors.append(f"{rel}: pattern front matter missing '{k}'")
        if fm.get("type") == "principle" and not re.search(r"^## Universal outcome", body, re.M):
            errors.append(f"{rel}: principle missing '## Universal outcome'")

    # index
    rows = []
    for rel, fm, body in docs:
        if "id" in fm:
            rows.append({"id": fm["id"], "title": fm.get("title", ""), "type": fm.get("type", ""),
                         "status": fm.get("status", ""), "path": rel,
                         "scope": fm.get("scope", ""), "platforms": fm.get("platforms", []),
                         "inputs": fm.get("inputs", []), "topics": fm.get("topics", [])})
    rows.sort(key=lambda r: (r["type"], r["id"]))
    if write_index:
        lines = ["# Index", "", "Generated by `scripts/validate.py --write-index`. Every stable identifier, its title, type, status, and path.", "",
                 "| ID | Title | Type | Scope | Platforms | Inputs | Status | Path |", "|---|---|---|---|---|---|---|---|"]
        for r in rows:
            lines.append(f"| {r['id']} | {r['title']} | {r['type']} | {r['scope']} | {', '.join(r['platforms'])} | {', '.join(r['inputs'])} | {r['status']} | [{r['path']}]({r['path']}) |")
        # gates and dims
        lines += ["", "## Embedded identifiers", "", "Dimensions `D-01…D-10` are defined in `rubric/dimensions.md`; quality gates `QG-xxx` in `rubric/quality-gates.md`.", ""]
        open(os.path.join(ROOT, "INDEX.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
        json.dump(rows, open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8"), indent=1)
        print(f"wrote INDEX.md and index.json with {len(rows)} entries")
    else:
        idx_path = os.path.join(ROOT, "INDEX.md")
        if os.path.exists(idx_path):
            idx = open(idx_path, encoding="utf-8").read()
            for r in rows:
                if f"| {r['id']} |" not in idx:
                    errors.append(f"INDEX.md missing {r['id']} (run --write-index)")
        else:
            warnings.append("INDEX.md not present (run --write-index)")

    if check_urls:
        def head(u):
            req = urllib.request.Request(u, method="GET", headers={"User-Agent": "Mozilla/5.0 web-app-ux-validator"})
            try:
                with urllib.request.urlopen(req, timeout=20) as r:
                    return u, r.status
            except urllib.error.HTTPError as e:
                return u, e.code
            except Exception as e:
                return u, str(e)[:60]
        with concurrent.futures.ThreadPoolExecutor(8) as ex:
            for u, st in ex.map(head, sorted(all_urls)):
                if st not in (200, 301, 302, 303, 307, 308):
                    warnings.append(f"URL {u} -> {st}")
        print(f"checked {len(all_urls)} URLs")

    counts = {}
    for r in rows:
        counts[r["type"]] = counts.get(r["type"], 0) + 1
    print("documents by type:", json.dumps(counts))
    for w in warnings:
        print("WARN", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
