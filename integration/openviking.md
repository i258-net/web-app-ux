---
id: INT-OPENVIKING
title: OpenViking integration — ingestion, refresh, retrieval, staleness
type: reference
topics: [openviking, retrieval, ingestion, integration, git-watch]
status: active
updated: 2026-11-08
---

# OpenViking integration

**Authority:** the Git repository is the single source of truth. OpenViking holds a processed copy as a **resource** (never memories) for semantic retrieval and progressive disclosure. If the two disagree, Git wins.

Labels: **[verified]** = exercised against this environment on the `updated:` date; **[docs]** = stated in OpenViking documentation; **[observed]** = seen during a test ingestion. Research notes with source URLs are in `../research/findings/openviking.md`.

## Environment

| Item | Value |
|---|---|
| CLI | `ov` 0.5.1 (`~/.local/bin/ov`) [verified] |
| Server | v0.5.2.1, healthy, API-key auth; account `i258`, user `daniel` [verified] |
| Existing convention | Git repositories are ingested from their **Git URL** with a recurring **Watch** task, to `viking://resources/repos/<org>/<repo>` (e.g. `https://github.com/i258-net/docs.git` → `viking://resources/repos/i258-net/docs`, interval 60 min, `semantic_and_vectors`) [verified: `ov task watch ls`] |
| Target for this repository | `viking://resources/repos/<org>/web-app-ux` once the GitHub remote exists |

## 1. Ingestion (the intended way: Git source + Watch)

Prerequisite: the repository is pushed to a Git remote the OpenViking server can reach.

Either in the web UI (**Scheduled Sync** → add) or with the CLI:

```sh
ov add-resource https://github.com/<org>/web-app-ux.git \
  --to viking://resources/repos/<org>/web-app-ux \
  --ignore-dirs '.git,.github,assets,scripts' \
  --tags 'repo=web-app-ux,kind=ux-knowledge' \
  --processing-mode semantic_and_vectors \
  --watch-interval 60
```

- Git sources are re-readable, so the Watch re-pulls on the interval and reprocesses changes; this is the documented refresh mechanism and matches the existing `i258-net/docs` watch [docs, verified config].
- Omit `--reason`: a non-empty reason can trigger memory extraction, and this content must stay resources-only [docs]. (The existing docs watch does carry a reason; that was a deliberate choice for that resource.)
- Native Git ingestion works without the Connector service; `--add-type git` (Connector) is a different, server-enabled path and is not needed [docs].
- `--ignore-dirs` keeps tooling and the PR template out. `INDEX.md` is a catalog table whose chunks rank highly for almost any query [observed]; if that proves noisy under the Git watch, exclude it via the repository's `.ovignore`-style mechanism if the server supports one, or accept it as the cost of a browsable catalog. This is an open item.

## 2. How OpenViking represents the files

[observed during a test ingestion of a local snapshot; expected to be the same for Git sources since the same Markdown parser runs]

- The scanner honors `.gitignore`.
- Each Markdown file becomes a **directory named after its H1 title** (sanitized, truncated, hash-suffixed), with the content **split into section chunks** (a pattern became three files). Original filenames are not preserved, so `glob` by filename or ID does not work.
- YAML front matter is preserved verbatim in the first chunk, so `ov grep "id: PAT-MO-004"` resolves an ID to its URI in one call [verified].
- Directory-level abstracts (L0) and overviews (L1) are generated asynchronously by a model; the chunk files are L2.
- `--args parse_mode:no_split` is documented to disable section splitting and keep one file per document [docs]; it was **not** exercised. It is worth enabling on the Git watch if whole-pattern reads matter more than fine-grained hits.

## 3. Retrieval

| Need | CLI | MCP tool |
|---|---|---|
| Candidates by problem | `ov find "<problem>" -u <resource> --context-type resource -n 8 -o json` | `find(query, target_uri=…, context_type="resource", limit=8)` |
| Confirm a directory | `ov abstract <dir>` / `ov overview <dir>` | `read(uri="<dir>/.abstract.md")` |
| Resolve an ID | `ov grep "id: PAT-SH-003" -u <resource>` | `grep` |
| Read | `ov read <uri>` (all chunks in the pattern's directory) | `read(uris=[…])` |

`find -o json` returns `{ok, result:{resources:[{uri, level, score, abstract, tags, context_type}], …}}`; the CLI prints a `cmd:` line before the JSON [verified].

Recipe: `find` scoped to the resource → read L0/L1 for directory hits → `grep` to resolve `related:` IDs → read the 3–6 documents that matter.

## 4. Refresh after Git changes

With a Git Watch: **nothing to do** beyond merging to the watched branch. The next scheduled run pulls and reprocesses. To refresh immediately: `ov task watch trigger <watch-task-id>` [verified: command exists]. Check `ov task watch ls` for `last_status`, `last_error`, `next_execution_time`.

`ov reindex` rebuilds semantic artifacts for stored content and does not fetch Git changes [verified: help].

## 5. Staleness detection

- **Primary:** `ov task watch ls -o json` → compare `last_execution_time` with the time of the last merge; `last_status` must be `completed` with `last_error` null.
- **Per document:** every authoritative file carries `updated:` in its front matter, visible in L2 reads.
- OpenViking's `stat.id` is an MD5 of account+URI, not a content hash; `modTime` alone does not prove equality with Git HEAD [verified].

## 6. Avoiding stale or duplicate content

- One resource URI per repository. Do not also ingest a local folder copy.
- Deprecated patterns stay in Git with `status: deprecated` so retrieval returns the pointer, not a dangling result.
- No UX guidance is stored as OpenViking memories; the skill never writes memories.

## 7. Retrieval validation

`scripts/retrieval_test.py --resource <uri>` runs the 16 queries in `../examples/retrieval-tests.md` and resolves hits to IDs via `grep`. Run after the watch's first completed run and after significant content changes. Log results in that file.

## Verification log

| Date | What was done | Result |
|---|---|---|
| 2026-11-08 | CLI inventory, health, `find -o json` shape, `stat`/`attrs` fields, existing Git watch config | Verified as described |
| 2026-11-08 | **Test ingestion of a local folder snapshot** to `viking://resources/repos/web-app-ux` (not the intended Git-watch path; done before confirming the owner's convention) | 121 files uploaded, 0 failures; parser split and renamed files as described in §2; semantic processing of `patterns/` still running at last check; retrieval tests 1/16 while abstracts were "not ready". **This snapshot should be removed and replaced by the Git watch once the remote exists.** |
| — | Git-watch ingestion of this repository | Not yet performed (remote not connected) |
| — | `parse_mode:no_split` | Not exercised |
| — | Retrieval tests against the Git-watched resource | Not yet performed |

## Fallback: local snapshot (testing only)

`scripts/ov_refresh.sh` ingests `git archive HEAD` from a staging folder to a given `--to` URI. It exists for environments without a reachable Git remote. A local snapshot cannot be watched and must be re-run manually after every change; do not use it alongside a Git watch on the same URI.
