---
id: INT-OPENVIKING
title: OpenViking integration — ingestion, refresh, retrieval, staleness
type: reference
topics: [openviking, retrieval, ingestion, integration]
status: active
updated: 2026-11-08
---

# OpenViking integration

**Authority:** the Git repository is the single source of truth. OpenViking is a retrieval and discovery layer that holds a processed copy of the Markdown as **resources** (not memories). It never redefines guidance. If the two disagree, Git wins and the resource is refreshed.

Verified facts below are labeled **[verified]** (run against this environment on the date in `updated:`) or **[docs]** (stated in OpenViking documentation, not exercised here). Research notes with URLs are in `../research/findings/openviking.md`.

## Environment at time of writing

| Item | Value |
|---|---|
| CLI | `ov` 0.5.1 at `~/.local/bin/ov` [verified] |
| Server | v0.5.2.1, healthy, API-key auth, user `daniel` (admin) [verified] |
| Existing convention | Repositories ingested under `viking://resources/repos/<repo-name>` (e.g. `i258-net`) [verified] |
| Target URI for this repository | `viking://resources/repos/web-app-ux` |
| MCP | Claude Code plugin `openviking-memory` exposes `find`, `search`, `read`, `tree`, `glob`, `grep`, `add_resource` and others [verified: tool names]; documented MCP parameters use `target_uri` for scope (not the CLI's `-u`) [docs] |

## 1. Repository ingestion

Ingest the **Markdown only**, from a clean checkout (committed state), excluding `.git`, `assets`, and `scripts`. The `research/` directory is ingested too so that evidence trails are retrievable, but its documents are labeled non-authoritative in their own text.

```sh
# from the repository root, on a clean working tree
ov add-resource "$(pwd)" \
  --to viking://resources/repos/web-app-ux \
  --include '*.md' \
  --ignore-dirs '.git,assets,scripts,node_modules' \
  --tags 'repo=web-app-ux,kind=ux-knowledge' \
  --processing-mode semantic_and_vectors --wait
```

Notes:
- `--to` must be a new URI on first ingestion [verified: CLI help]. Documentation states that re-running `add-resource` with the **same exact `--to`** refreshes in place (unchanged content reused, removed files may be removed) [docs]. See §4 for what was verified here.
- Do **not** pass `--reason`: a non-empty reason can trigger memory extraction, and this content must stay resources-only [docs].
- `--watch-interval` applies to re-readable remote sources (URLs, native Git URLs). A local folder upload is a static snapshot and cannot be watched [docs]. Git-URL ingestion with watching requires the Connector service (`--add-type git`), which is disabled by default server-side and was not inspected here [docs].
- OpenViking generates **directory-level** abstracts (L0, ~256 chars) and overviews (L1, ~4000 chars) bottom-up with a model; per-file summaries feed them. The generated text is an interpretation; the L2 file is the evidence [docs].
- Arbitrary YAML front matter is **not** documented as queryable metadata. Our `tags:`/`platforms:` front matter is retrievable only as text inside the file, not as OpenViking tags [docs]. Explicit retrieval tags are the `--tags` k=v pairs.

## 2. Resource organization and naming

The ingested tree mirrors the repository: `viking://resources/repos/web-app-ux/{principles,patterns/{shared,mobile,desktop,responsive,pwa},rubric,evaluation,sources,examples,governance,integration,research}`. The directory structure therefore *is* the progressive-disclosure structure: the `patterns/mobile` L0 abstract answers "is this where mobile guidance lives?", its L1 overview lists the files, and L2 is the pattern.

Do not create a second copy under another URI (e.g. a user-private path). One resource, one URI.

## 3. Indexing and retrieval

| Need | Command (CLI) | MCP tool |
|---|---|---|
| Find candidate documents by problem | `ov find "<problem>" -u viking://resources/repos/web-app-ux --context-type resource -n 8 -o json` | `find(query, target_uri=…, context_type="resource", limit=8)` |
| Confirm a directory is relevant | `ov abstract <dir-uri>` / `ov overview <dir-uri>` | `read(uri="<dir-uri>/.abstract.md")`, `read(uri="<dir-uri>/.overview.md")` |
| Read a pattern | `ov read <file-uri>` | `read(uri=…)` or `read(uris=[…])` for several |
| Exact term / ID lookup | `ov grep "PAT-MO-004" -u viking://resources/repos/web-app-ux` | `grep` |
| Path lookup | `ov glob "**/PAT-SH-*.md" -u viking://resources/repos/web-app-ux` | `glob` |

Retrieval recipe used by the review skill:

1. `find` with a problem phrased in user terms, scoped to the resource, limited to ~8 results, resource type only.
2. For the top hits that are directories, read the L0/L1 sidecar to confirm; for file hits, read the file.
3. Follow `related:` IDs by `grep`/`glob` rather than issuing new semantic searches.
4. Stop at 3–6 documents per screen under review.

`find -o json` returns `{ok, result:{memories:[], resources:[{uri, level, score, abstract, tags, context_type}], skills:[], total}}` [verified]. The CLI prints a human `cmd:` line before JSON on stdout; automation must skip non-JSON lines [verified].

## 4. Refreshing after Git changes

Procedure (run after merging to `main`):

```sh
git -C <repo> pull --ff-only
git -C <repo> rev-parse HEAD > integration/INGESTED_COMMIT        # record what is about to be ingested (not committed to Git; see note)
ov add-resource "<repo>" --to viking://resources/repos/web-app-ux \
  --include '*.md' --ignore-dirs '.git,assets,scripts,node_modules' \
  --tags 'repo=web-app-ux,kind=ux-knowledge' --processing-mode semantic_and_vectors --wait
ov task status <TASK_ID>         # if --wait returned early
ov tree viking://resources/repos/web-app-ux -L 2
```

- **Preferred:** in-place refresh with identical `--to` [docs]. Status in this environment: see "Verification log" below.
- **Fallback (deliberate, destructive):** `ov rm viking://resources/repos/web-app-ux --recursive --wait` then re-add. This creates a retrieval gap and regenerates all summaries and vectors; use only if in-place refresh is rejected.
- `ov reindex` rebuilds semantic artifacts for content already stored; it does not pick up Git changes [verified: CLI help].
- There is no generic `sync` command [verified: CLI help]. The `--manifest` option (OpenViking Assets manifest) can create or sync selected assets and is a candidate for a future scripted refresh, but it was not exercised.

**No custom synchronization service is introduced.** The refresh is one command run after merges; a Git hook or CI job that runs it is optional and out of scope.

## 5. Staleness detection

OpenViking exposes `modTime` and an `id` that is an MD5 of account+URI (not a content hash); neither proves equality with Git HEAD [verified].

Mechanism used here: the file `integration/INGESTED_COMMIT` is written by the refresh procedure **immediately before ingestion** and ingested with the tree (it is listed in `.gitignore`, because a committed file cannot contain its own commit SHA). A consumer compares:

```sh
ov read viking://resources/repos/web-app-ux/integration/INGESTED_COMMIT
git -C <repo> rev-parse HEAD
```

If they differ, the OpenViking copy is stale: prefer the Git copy and run the refresh. Every authoritative file also carries `updated:` in its front matter, which is visible in L2 reads and is a per-document secondary signal.

## 6. Avoiding stale or duplicate content

- One target URI; never ingest the same repository under two URIs.
- Ingest from a clean checkout only (`git status --porcelain` empty), so no untracked drafts enter.
- `--include '*.md'` keeps SVGs, scripts, and JSON (`index.json`) out of the semantic index. `INDEX.md` is included deliberately as a catalog.
- Deprecated patterns stay in Git (status `deprecated`) so retrieval shows the pointer to the successor rather than a dangling result.
- Do not store UX guidance as OpenViking **memories**; the memory plugin's automatic capture is unrelated to this resource, and nothing in the skill writes memories.

## 7. Retrieval validation

Representative queries and expected top documents are listed in `../examples/retrieval-tests.md`. Run them after every refresh; a query whose expected document falls out of the top results indicates either a regression in content or a stale index.

## Verification log

| Date | What was done | Result |
|---|---|---|
| 2026-11-08 | CLI inventory, health, existing convention, `find -o json` shape, `stat`/`attrs` fields | Verified as described above |
| 2026-11-08 | Initial ingestion and retrieval tests | *pending — see below; this row is replaced when executed* |
