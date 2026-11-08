#!/usr/bin/env python3
"""Run the retrieval tests in examples/retrieval-tests.md against OpenViking.

For each query: `ov find <query> -u <resource> --context-type resource -n 8 -o json`,
then resolve each hit URI to the knowledge-base ID by reading the first lines of the
hit (or, for directory sidecars, the files beneath it) and looking for `id:`.
Pass = any expected ID (or a file path fragment) appears among resolved hits.
Usage: python3 scripts/retrieval_test.py [--resource viking://resources/repos/web-app-ux]
"""
import json, re, subprocess, sys, os
RES = "viking://resources/repos/web-app-ux"
if "--resource" in sys.argv:
    RES = sys.argv[sys.argv.index("--resource") + 1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS = []
for line in open(os.path.join(ROOT, "examples/retrieval-tests.md"), encoding="utf-8"):
    m = re.match(r"^\| (R\d+) \| (.+?) \| (.+?) \|$", line)
    if m:
        ids = re.findall(r"(PAT-[A-Z]{2}-\d{3}|QG-\d{3}|rubric/[a-z-]+\.md|evaluation/[a-z-]+\.md)", m.group(3))
        TESTS.append((m.group(1), m.group(2), ids))

def ov(*args):
    out = subprocess.run(["ov", *args, "-o", "json"], capture_output=True, text=True, timeout=120).stdout
    js = out[out.find("{"):]
    return json.loads(js)

def resolve(uri):
    """Return a set of IDs/paths that this hit represents."""
    found = set()
    rel = uri.split(RES + "/", 1)[-1] if uri.startswith(RES) else uri
    # path fragments for rubric/evaluation files are recognizable by folder names
    top = rel.split("/")[0]
    if top in ("rubric", "evaluation"):
        found.add(top)
    if uri.endswith(".md") and not uri.rsplit("/", 1)[-1].startswith("."):
        try:
            txt = ov("read", uri, "--limit", "4")["result"]
            content = txt.get("content", txt) if isinstance(txt, dict) else txt
            m = re.search(r"id:\s*([A-Z]+-[A-Z0-9-]+)", str(content))
            if m: found.add(m.group(1))
        except Exception:
            pass
    else:
        # directory sidecar: grep for ids under it
        d = uri.rsplit("/", 1)[0] if uri.endswith(".md") else uri
        try:
            g = ov("grep", "^id: ", "-u", d)["result"]
            for mt in g.get("matches", []):
                m = re.search(r"id:\s*([A-Z]+-[A-Z0-9-]+)", mt["content"])
                if m: found.add(m.group(1))
        except Exception:
            pass
    return found

passed = 0; rows = []
for tid, q, expected in TESTS:
    hits = ov("find", q, "-u", RES, "--context-type", "resource", "-n", "8")["result"]["resources"]
    got = set()
    for h in hits:
        got |= resolve(h["uri"])
    ok = any(e in got or e.split("/")[0] in got for e in expected)
    # rubric/evaluation path expectations
    for e in expected:
        if "/" in e and e.split("/")[0] in got: ok = True
    passed += ok
    rows.append((tid, "PASS" if ok else "FAIL", ", ".join(expected), ", ".join(sorted(i for i in got if i.startswith(("PAT","QG","P-","RUBRIC","EVAL","rubric","evaluation")))[:8])))
for r in rows: print(" | ".join(r))
print(f"\n{passed}/{len(TESTS)} passed")
