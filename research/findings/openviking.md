# OpenViking research findings

Research date: **2026-11-08**. Target: a local Git repository containing approximately 80–120 small Markdown knowledge files, imported as **resources** under `viking://resources/repos/web-app-ux`.

Evidence labels: **CLI verified** means help or a read-only command was run here; **Docs** means published documentation, not tested against this server; **Unknown** means neither establishes the behavior. No server mutation, ingestion, deletion, tag change, export/import, or MCP call was performed. Configuration and API keys were not printed. Published docs are rolling documentation, not a pinned v0.5.2.1 specification.

## 1. Ingestion

**CLI verified:** `/Users/daniel/.local/bin/ov --version` returned `openviking 0.5.1`; `ov health` reported healthy server **v0.5.2.1**. `ov tree viking://resources/repos -L 2` showed `i258-net/docs`, confirming the existing repository convention.

**Docs:** [Resource Management](https://docs.openviking.ai/en/api/02-resources/llms.txt) describes scanning a directory, parsing supported files, constructing a resource tree, persisting it, and asynchronously generating summaries and vectors. Local directory scans honor root/nested `.gitignore`; include/exclude and ignored-directory filters further narrow the selection. Markdown is parsed content, not guaranteed byte-for-byte archival storage. The [resource tutorial](https://docs.openviking.ai/en/getting-started/08-resources/llms.txt) shows `project.md` becoming `project/project.md`; do not assume every imported URI matches the original relative path. Inspect the returned tree. `args.parse_mode=no_split` disables document splitting while retaining normal parsing; it does not promise byte identity.

**CLI verified:** `ov add-resource --help` provides these options:

| Option | Meaning and qualification |
| --- | --- |
| `--parent URI` | Existing destination directory; the imported resource is placed beneath it. Mutually exclusive with `--to`. |
| `--to URI` | Exact resource root. Local help says **“Exact target URI (must not exist yet)”**. Current docs instead describe refresh of an existing target; see §2. |
| `--parent-auto-create URI` / `-p` | Destination parent, created if absent; incompatible with `--to` and `--parent`. This takes a URI, not a Boolean. |
| `--include '*.md,*.markdown'` | Include filename/extension glob patterns; quote shell globs. |
| `--exclude '*.tmp,*.log'` | Exclude filename/extension glob patterns. |
| `--ignore-dirs '.git,node_modules,dist'` | Comma-separated directory names to skip. |
| `--tags 'repo=web-app-ux,kind=knowledge'` | Explicit retrieval `k=v` tags applied after import. `--tag-mode` is `replace`, `append`, or `clear`. |
| `--wait` | Wait for processing. Docs clarify that standard imports wait for this import's work, not all server work; an HTTP timeout does not mean cancellation. |
| `--watch-interval MINUTES` | Automatic monitoring cadence; zero disables creation of monitoring. Local snapshots cannot be watched (§2). |
| `--processing-mode semantic_and_vectors` | Normal mode: generate L0/L1 semantic artifacts and vectors. Required for fresh progressive-disclosure summaries. |
| `--processing-mode vectors_only` | Skip semantic understanding and generate file vectors; existing L0/L1 can remain stale. |

**Git:** Native Git URLs are documented and the [README](https://github.com/volcengine/OpenViking/blob/main/README.md) demonstrates `ov add-resource https://github.com/volcengine/OpenViking`. `--add-type git` explicitly routes through **Connector**, rather than the ordinary local-file path. Local help states: **“must be enabled server-side”**, requires `--to`, and forbids `--parent`, `--parent-auto-create`, and `--manifest`. Docs say Connector does not support `wait=true`; Git can use a native fallback when Connector does not apply, except with Connector-only credentials. [Server configuration](https://docs.openviking.ai/en/configuration/01-server/llms.txt) lists Connector as an external ingestion service, disabled by default. Server network access and appropriate private-repository credentials are needed; this server's Connector deployment, credentials, and Git access were not inspected. Use ordinary native ingestion unless Connector is intentionally configured.

**Resources-only caution (Docs):** A nonempty `reason` can trigger memory extraction referencing the resource. Omit `--reason` for this resources-only use case.

## 2. Re-ingestion and refresh

**Docs:** [Resource Management](https://docs.openviking.ai/en/api/02-resources/llms.txt) explicitly says an existing exact `to` is refreshed. Unchanged content is reused and changed portions reprocessed when the resolved root equals `to`. Files absent from the new tree **may be removed**: the destination should contain only this imported repository. `--parent` is for adding a resource, and automatic conflict naming can create suffixed siblings; it is not a reliable update identity.

**CLI verified / unresolved conflict:** v0.5.1 help says `--to` “must not exist yet”; the introductory tutorial also advises a new demo path for repeat runs. No write was attempted, so it is **unknown whether this installed client/server pair accepts documented in-place refresh**. A help statement alone does not establish an actual rejection. Do not present either “always fails” or “verified safe in-place update” as measured behavior.

**CLI verified:** Top-level `ov --help` has no generic resource `sync` or `update` command. `ov skills update` concerns skills, not resources. A newer manifest workflow exists in `add-resource --help` (`--manifest`: create or sync selected assets), but is not a generic Git working-tree synchronizer. `ov reindex --help` rebuilds semantic/vector artifacts for already stored content; it does not fetch Git changes or re-upload a local folder.

**Docs:** Watches refresh re-readable remote sources, including URLs, feeds and native Git repositories. Local directory/file uploads are static snapshots (`temp_file_id`) and cannot monitor this Mac's working tree. Re-add the snapshot after changes. The scheduler checks due work every 60 seconds; this is scheduling granularity, not a processing SLA. Re-importing with monitoring enabled creates a new watch subject to target ownership rules, rather than editing an existing subscription. A native import with explicit `to` and nonpositive interval can pause an existing single watch on that target. [Watches API](https://docs.openviking.ai/en/api/15-watches/llms.txt)

**CLI verified:** `ov task --help` exposes `status`, `list`, `cancel`, and `watch`; `ov task watch --help` exposes `ls`, `show`, `rm`, `pause`, `resume`, `update`, and `trigger`. A remote watch can be refreshed immediately with `task watch trigger`; it cannot turn a local snapshot into a filesystem watcher. `ov wait --help` says it waits for queued asynchronous processing. Prefer the returned ingestion `task_id` and `ov task status TASK_ID` to distinguish successful completion from submission or unrelated queued work.

**Deletion fallback:** `ov rm --help` supports `--recursive --wait`, with an example waiting for generated overviews to refresh. The [filesystem API](https://docs.openviking.ai/en/api/03-filesystem/llms.txt) describes removal of associated vector data. Deleting and re-adding removes availability between operations, discards the incremental-update benefit, and regenerates summaries/vectors; semantic search results and scores can change. It is not an atomic replacement. It should be a deliberate fallback, not the default refresh procedure.

**Transfer:** `ov export URI file.ovpack` and `ov import file.ovpack TARGET_PARENT` transfer persisted context, not changes from a Git checkout. Export includes semantic sidecars and can optionally include compatible dense vectors (`--include-vectors`). Import supports `--on-conflict fail|overwrite|skip` and `--vector-mode auto|recompute|require`; default auto restores compatible snapshots or recomputes vectors. Without vector snapshots, import recomputes vectors. Useful for backup/migration, not a documented source synchronization strategy. Neither command was executed. [OVPack guide](https://docs.openviking.ai/en/guides/09-ovpack/llms.txt)

## 3. Retrieval and progressive disclosure

**CLI verified:** The following distinctions come from each command's `--help`, consistent with the [retrieval API](https://docs.openviking.ai/en/api/06-retrieval/llms.txt):

| Command | Purpose |
| --- | --- |
| `find QUERY` | Fast semantic retrieval without session intent analysis. |
| `search QUERY` | Experimental context-aware/deeper retrieval; optional `--session-id`. `--mode list` returns hits; `--mode context` assembles model-ready context. |
| `grep PATTERN` | Text-pattern/regex content search; supports case insensitivity and context lines. |
| `glob PATTERN` | Filename/path glob matching. |
| `abstract DIRECTORY_URI` | L0 directory abstract. |
| `overview DIRECTORY_URI` | L1 directory overview/navigation. |
| `read FILE_URI` | L2 file content; optional zero-based `--offset` and line `--limit`. Direct sidecar reads return raw metadata too. |

**Docs:** [Context layers](https://docs.openviking.ai/en/concepts/03-context-layers/llms.txt) defines L0 as a directory's `.abstract.md` (default generated body budget 256 characters), L1 as `.overview.md` (4000 characters), and L2 as original files or parsed bodies. These are character budgets, not hard storage limits. L0/L1 are **directory-level**, not guaranteed per-file companion summaries. The skill should select a promising directory from L0, inspect L1 navigation, then read the actual returned L2 URI.

**CLI verified:** `find -u URI` scopes retrieval to that subtree; `-L 0,1,2` selects levels; `--context-type resource` excludes memories/skills by type. `search -u` and level filters apply to **list mode**, not context mode. `--tags 'a=b,c=d'` requires **all** explicit tags. `grep` and `glob` also support URI scope and AND tag filtering. Tags are retrieval metadata, not arbitrary YAML-field queries.

Harmless command executed:

```sh
ov find 'homelab documentation' -u viking://resources/repos -n 1 -o json
```

Actual output shape (one result; abstract shortened):

```json
{
  "ok": true,
  "result": {
    "memories": [],
    "resources": [{
      "context_type": "resource",
      "uri": "viking://resources/repos/.abstract.md",
      "level": 0,
      "score": 0.7552796602249146,
      "abstract": "This directory contains human-facing homelab documentation…",
      "tags": []
    }],
    "skills": [],
    "total": 1
  }
}
```

The CLI additionally printed a human `cmd: ...` diagnostic line before JSON in this run; automation should not assume every stdout line is JSON. Fields above are observed, not a promise that all optional API fields always appear. `--read-content` can request full content; progressive disclosure should normally leave it off.

## 4. YAML, generated summaries, and tags

**Docs:** Resource summaries are generated during semantic processing by the model-backed summarizer, bottom-up from file summaries to directory L1 and L0. These are generated interpretations; the selected L2 source remains the evidence. `vectors_only` deliberately skips this stage.

**Unknown:** The fetched resource documentation does **not** establish extraction of arbitrary knowledge-file YAML fields (such as `title`, `status`, `tags`, or `updated`) into queryable resource metadata. Do not assume frontmatter `tags:` becomes explicit retrieval tags. Exact preservation, YAML stripping, and effect on Markdown splitting were not tested.

**Docs distinguish two supported frontmatter cases:** Skills parse `SKILL.md` YAML metadata. Generated L0/L1 sidecars use schema-validated OKF frontmatter (`directory`, `source`, `generated_by`, `freshness`); unknown sidecar fields are dropped. This is not evidence that arbitrary resource frontmatter is indexed as attributes. `abstract`/`overview` expose sidecar bodies; `read .../.overview.md` exposes raw frontmatter. [Skills](https://docs.openviking.ai/en/api/04-skills/llms.txt), [layers](https://docs.openviking.ai/en/concepts/03-context-layers/llms.txt)

**CLI verified:** `ov set-tags --help` supports `--tags`, default replacement or `--mode append` (merge by key), and `--recursive`, described as updating descendant files and semantic nodes. Recursive tagging propagates an explicit update to current descendants; it does **not** document permanent inheritance for future children. Reapply/import tags after refresh as needed. [Content API](https://docs.openviking.ai/en/api/12-content/llms.txt) also supports `clear` at API level; the top-level local `set-tags` help advertises only replace/append, while ingestion advertises clear.

## 5. Staleness detection

**CLI verified:** These read-only probes targeted `viking://resources/repos/i258-net/docs/CONTRIBUTING.md`:

```sh
ov stat viking://resources/repos/i258-net/docs/CONTRIBUTING.md -o json
ov attrs get viking://resources/repos/i258-net/docs/CONTRIBUTING.md -o json
```

`stat.result` contained `name`, `size: 3616`, `mode: 420`, `modTime: "2026-11-01T19:18:00Z"`, `isDir: false`, `uri`, `isLocked: false`, and a 32-character `id`. `attrs.result` contained `uri`, `context_type: "resource"`, and `attrs: {"tags": []}`. Neither returned a content hash, Git revision, or source checkout version.

**Docs:** The stat `id` is `md5(account_id + ':' + uri)` for an L2 vector record: **not a content hash**. Internal content fingerprints used by reindex are not a documented generic `stat`/`attrs` Git-version contract. `modTime` alone cannot prove equality with Git HEAD. Skill integrity manifests expose hashes/revisions through a different API; that does not establish the same resource facility. [Filesystem](https://docs.openviking.ai/en/api/03-filesystem/llms.txt), [content](https://docs.openviking.ai/en/api/12-content/llms.txt)

**Recommended design (inference):** In a clean ingestion staging snapshot, add a visible `INGESTION.md` recording repository origin, exact source commit SHA, export time, filters, and optional per-file hashes. Generate it *after* resolving the source commit; committing a file containing its own final commit SHA is self-referential. After successful processing, read the ingested marker and compare its source SHA to `git rev-parse HEAD`. A SHA marker identifies the intended snapshot, not proof that every file succeeded; validate the returned task, tree, and any failure metadata. A dirty working tree requires a manifest/dirty-state record, since HEAD alone cannot identify its bytes. No marker was created here.

**Docs:** Sidecar `freshness.pending_child_changes > 0` indicates known lag behind lower-level changes. This concerns already ingested descendants, not unseen Git changes; zero does not prove Git freshness. Direct sidecar metadata is useful supplementary evidence only.

## 6. MCP parameters (docs only; no MCP calls)

The [MCP tool reference](https://docs.openviking.ai/en/guides/06-mcp-integration/llms.txt) lists:

| Tool | Documented parameters |
| --- | --- |
| `find` | `query`, optional `target_uri`, `limit`, `min_score`, optional `level`, `context_type`, `read_content`, `events_time_decay_protection`. |
| `search` | `query`, `mode` (`list` or `context`), `target_uri` (list only), optional `session_id`, `limit`, `min_score`, `level` (list), optional `context_type`, `events_time_decay_protection`; context options `quotas`, `purpose`, `max_tokens`, `detail` or `detail_by_category`, `dedup_turns`, `exclude_uris`, `peer_scope`, `other_peer_penalty` or `other_peer_penalties`, and `rewrite` (`off` or `auto`). |
| `read` | `uri` for one file **or** `uris` array for batch reads; `offset`, `limit` in text lines. |

The table does not list `tags` for MCP find/search, despite CLI/REST tag support. Installed Claude plugin schema/version compatibility, argument defaults/types beyond the published table, and whether its tools extend that table remain unverified. Do not copy CLI `-u` into MCP arguments: the documented MCP scope parameter is `target_uri`. L0/L1 can be accessed using `read` on sidecar URIs even when a plugin has no dedicated abstract/overview tools.

## 7. Skills

**CLI verified:** `ov add-skill --help` accepts a skill directory, single `SKILL.md`, raw content, Git repository, or GitHub tree URL. `--skill NAME` selects skills; `--list` lists without installing; `--wait` waits; `--parent-auto-create URI` chooses the skill root, with user-private default stated in help. `ov skills --help` lists `add`, `list`, `find`, `show`, `update`, `remove`, and local `validate`.

**Docs:** Skills are packages containing `SKILL.md` and optional auxiliary files, installed and semantically indexed. `viking://agent/skills` is account-shared; `viking://~/skills` resolves to the authenticated user's private root (`viking://user/{user_id}/skills`). Configured add-target overrides may change the default destination, so specify it explicitly. Peer-scoped skills are unsupported. Git-installed skills can be updated from recorded source; local uploads have no Git source to pull automatically. [Skills API](https://docs.openviking.ai/en/api/04-skills/llms.txt)

**Inference supported by docs:** The same review-skill source can be installed in a harness's local skills directory and imported into OpenViking. OpenViking installation does not itself install scripts into the local harness or keep both copies synchronized. Keep one authoritative source and update both destinations. The knowledge repository should still be ingested separately as resources; the skill should retrieve from its explicit resource scope.

## 8. Limits and processing expectations

**Docs:** Native Markdown extensions include `.md`, `.markdown`, `.mdown`, `.mkd`. Resource Management also lists PDF, HTML, Word/ODT/RTF, text, EPUB, spreadsheets/CSV, presentations, common code formats, images, audio/video, Git sources, and web/cloud documents; some require parser/media configuration. `--strict` fails directory scanning on unsupported files; default behavior can skip unsupported inputs. Restricting to Markdown avoids accidentally importing unrelated material.

[Server configuration](https://docs.openviking.ai/en/configuration/01-server/llms.txt) says `parsers.directory.max_files` defaults to `null` (no file-count cap); example defaults include `max_depth: 10`, `max_concurrent: 4`. File/depth caps apply to Understanding directory routing; native directory parsing does not apply those two limits. Local directory ZIP uploads are subject to `/resources/temp_upload` limits; no common per-file byte limit is imposed by DirectoryParser after extraction. Individual parser/backend limits still apply. Actual server upload ceiling and settings were not inspected, and the fetched pages do not establish a universal numeric Markdown size limit.

No documented processing-time SLA for 80–120 Markdown files was found. Parsing, file/directory summarization, embedding, queues and provider latency determine elapsed time; monitor task completion rather than assuming a fixed duration. The README's “first 50 files are free” concerns the hosted commercial service, not a self-hosted file-count cap. Skill integrity's 512-entry / 16 MiB-per-file / 64 MiB-total limits apply to its integrity-manifest API, not generic resource ingestion.

## Fetch log

All following URLs were fetched successfully on **2026-11-08**. `/llms.txt` is the site's Markdown representation of the corresponding page. README was fetched from the raw URL below; its human-readable GitHub URL is cited above. No fetched content was saved separately.

- https://docs.openviking.ai/llms.txt
- https://docs.openviking.ai/en/getting-started/05-cli-setup/llms.txt
- https://docs.openviking.ai/en/getting-started/08-resources/llms.txt
- https://docs.openviking.ai/en/api/02-resources/llms.txt
- https://docs.openviking.ai/en/api/06-retrieval/llms.txt
- https://docs.openviking.ai/en/api/15-watches/llms.txt
- https://docs.openviking.ai/en/guides/06-mcp-integration/llms.txt
- https://docs.openviking.ai/en/api/04-skills/llms.txt
- https://docs.openviking.ai/en/concepts/03-context-layers/llms.txt
- https://docs.openviking.ai/en/api/03-filesystem/llms.txt
- https://docs.openviking.ai/en/api/12-content/llms.txt
- https://docs.openviking.ai/en/guides/09-ovpack/llms.txt
- https://docs.openviking.ai/en/faq/faq/llms.txt
- https://docs.openviking.ai/en/guides/01-configuration/llms.txt
- https://docs.openviking.ai/en/configuration/01-server/llms.txt
- https://raw.githubusercontent.com/volcengine/OpenViking/main/README.md

## Recommended ingestion and refresh procedure — commands only, NOT executed

```sh
# Initial ingestion of the selected Markdown working-tree snapshot.
# Existing viking://resources/repos parent was verified; inspect task/tree afterward.
ov add-resource /Users/daniel/.t3/projects/web-app-ux \
  --to viking://resources/repos/web-app-ux \
  --include '*.md,*.markdown,*.mdown,*.mkd' \
  --ignore-dirs '.git,node_modules,dist' \
  --tags 'repo=web-app-ux,kind=knowledge' \
  --processing-mode semantic_and_vectors --wait
ov tree viking://resources/repos/web-app-ux
ov find 'review guidance' -u viking://resources/repos/web-app-ux --context-type resource -n 5 -o json
ov abstract viking://resources/repos/web-app-ux
ov overview viking://resources/repos/web-app-ux

# After Git changes: documented in-place refresh; actual v0.5.1/v0.5.2.1 behavior remains untested.
# Reuse identical source, exact target, filters and semantic processing mode.
ov add-resource /Users/daniel/.t3/projects/web-app-ux \
  --to viking://resources/repos/web-app-ux \
  --include '*.md,*.markdown,*.mdown,*.mkd' \
  --ignore-dirs '.git,node_modules,dist' \
  --tags 'repo=web-app-ux,kind=knowledge' \
  --processing-mode semantic_and_vectors --wait

# If submission returned or waiting timed out, substitute the returned task ID.
ov task status TASK_ID
ov tree viking://resources/repos/web-app-ux
ov find 'review guidance' -u viking://resources/repos/web-app-ux --tags 'repo=web-app-ux' -n 5 -o json

# Optional explicit propagation to current descendants, after confirming successful ingestion.
ov set-tags viking://resources/repos/web-app-ux --tags 'repo=web-app-ux,kind=knowledge' --mode append --recursive

# Deliberate destructive fallback ONLY if existing-target refresh is actually rejected.
# Creates a retrieval gap and rebuilds semantics/vectors; not the default procedure.
ov rm viking://resources/repos/web-app-ux --recursive --wait
ov add-resource /Users/daniel/.t3/projects/web-app-ux \
  --to viking://resources/repos/web-app-ux \
  --include '*.md,*.markdown,*.mdown,*.mkd' \
  --ignore-dirs '.git,node_modules,dist' \
  --tags 'repo=web-app-ux,kind=knowledge' \
  --processing-mode semantic_and_vectors --wait
```

## Open questions

- Does this exact CLI/server pair refresh an occupied `--to`, despite contradictory CLI help? Resolve with an authorized disposable fixture before production refresh.
- Which parser handles this local Git directory, how does it map paths/split Markdown, and how does it preserve ordinary YAML frontmatter? Does `no_split` improve the desired file-level retrieval?
- What are this deployment's upload limits, model configuration, Connector availability and measured ingestion duration?
- Does every refreshed file and semantic node receive ingestion tags consistently, including newly added children? Verify tagged retrieval after ingestion.
- What MCP tool schema/version does the Claude plugin actually expose, especially tag filtering and search/read options?
- Which Markdown subset should be published, and should ingestion exclude drafts, generated research and local-only documents beyond `.gitignore`?
- Who generates the source-SHA/manifest marker, verifies failed files and deletions, and maintains the local/OpenViking copies of the review skill?
