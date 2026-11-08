---
id: SRC-011
title: OpenViking documentation (for the integration guide)
type: source
publisher: OpenViking project (volcengine)
evidence_classes: [E3]
status: active
updated: 2026-11-08
---

# SRC-011 OpenViking documentation

## Publisher and scope

OpenViking is an open-source context database maintained under the `volcengine` GitHub organization. It stores resources, memories, and skills under `viking://` URIs and serves layered summaries for retrieval. This register entry supports [`integration/openviking.md`](../integration/openviking.md) only. **It is not a UX evidence source**, and nothing here backs a principle, pattern, rubric level, or quality gate.

Research (`research/findings/openviking.md`) used the published documentation in its `/llms.txt` Markdown form and the project README. The documentation covers:

- resource ingestion and refresh
- watches
- the filesystem and content APIs
- retrieval
- context layers (L0 and L1)
- skills
- MCP integration
- ovpack export and import
- server configuration and the FAQ

The research also ran read-only CLI commands on this machine: `ov --version` returned 0.5.1 and `ov health` reported server v0.5.2.1. That CLI evidence is recorded in the findings file, not here.

## How to classify their material

The UX evidence scale does not really apply to this material. The findings file uses its own labels:

| Label | Meaning | Register treatment |
|---|---|---|
| **Docs** | Published documentation, not tested against this server | Treat as **E3-like** vendor documentation of intended behavior |
| **CLI verified** | A help or read-only command was run here | Stronger for this installation only |
| **Unknown** | Neither source establishes the behavior | Resolve with a disposable test fixture before production use |

The front matter lists `E3` only so the register stays consistent with the other source files.

## Licensing and access

The OpenViking source code and README are on GitHub under the project's open-source license (see the repository). The documentation site is public. No authentication was used. Configuration and API keys were not printed or recorded. Paraphrase the docs. Quoting short CLI help strings is fine.

## Known limitations and biases

- **Rolling docs.** The published documentation is not pinned to v0.5.2.1. Behavior may differ from the installed server.
- **Contradictions.** Local `ov add-resource --help` describes `--to` as an "Exact target URI (must not exist yet)", while the current docs describe refreshing an existing target. Resolve this with a disposable fixture (see the findings file's open questions).
- **No mutation testing.** No ingestion, deletion, tag change, export or import, or MCP call was performed. Ingestion timing, upload limits, tag propagation, and parser path mapping are untested.
- **Connector.** Git ingestion through Connector must be enabled on the server and is disabled by default. This deployment's Connector was not inspected.

## Cited pages

All rows were fetched successfully on 2026-11-08 (findings fetch log). No page showed a publication date. The "Used in" column replaces finding IDs because the OpenViking findings are organized by numbered section rather than `F-xx-nn` IDs.

| Title | URL | Published/updated | Accessed | Evidence class | Finding IDs |
|---|---|---|---|---|---|
| OpenViking docs index (llms.txt) | <https://docs.openviking.ai/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; fetch log |
| Getting started: CLI setup | <https://docs.openviking.ai/en/getting-started/05-cli-setup/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; fetch log |
| Getting started: Resources (tutorial) | <https://docs.openviking.ai/en/getting-started/08-resources/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §1 Ingestion |
| API: Resource Management | <https://docs.openviking.ai/en/api/02-resources/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §1 Ingestion, §2 Re-ingestion |
| API: Retrieval | <https://docs.openviking.ai/en/api/06-retrieval/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §3 Retrieval |
| API: Watches | <https://docs.openviking.ai/en/api/15-watches/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §2 Re-ingestion |
| Guide: MCP integration | <https://docs.openviking.ai/en/guides/06-mcp-integration/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §6 MCP parameters |
| API: Skills | <https://docs.openviking.ai/en/api/04-skills/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §4 Summaries and tags, §7 Skills |
| Concepts: Context layers | <https://docs.openviking.ai/en/concepts/03-context-layers/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §3 Retrieval, §4 Summaries and tags |
| API: Filesystem | <https://docs.openviking.ai/en/api/03-filesystem/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §2 Re-ingestion, §5 Staleness |
| API: Content | <https://docs.openviking.ai/en/api/12-content/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §4 Summaries and tags, §5 Staleness |
| Guide: ovpack | <https://docs.openviking.ai/en/guides/09-ovpack/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §2 Re-ingestion |
| FAQ | <https://docs.openviking.ai/en/faq/faq/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; fetch log |
| Guide: Configuration | <https://docs.openviking.ai/en/guides/01-configuration/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; fetch log |
| Configuration: Server | <https://docs.openviking.ai/en/configuration/01-server/llms.txt> | not shown | 2026-11-08 | Docs (E3-like) | none; §1 Ingestion, §8 Limits |
| OpenViking README (raw; the file actually fetched) | <https://raw.githubusercontent.com/volcengine/OpenViking/main/README.md> | not shown | 2026-11-08 | Docs (E3-like) | none; fetch log |
| OpenViking README (human-readable GitHub URL of the same file) | <https://github.com/volcengine/OpenViking/blob/main/README.md> | not shown | 2026-11-08 (via raw URL) | Docs (E3-like) | none; §1 Ingestion |

The repository URL `https://github.com/volcengine/OpenViking` appears in §1 only as the argument of an example `ov add-resource` command quoted from the README. It was not fetched as a page, so it is not a citation.
