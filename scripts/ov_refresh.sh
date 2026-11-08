#!/usr/bin/env bash
# FALLBACK ONLY: ingest a local snapshot of the committed Git tree into OpenViking.
# The intended integration is a Git-URL resource with a scheduled Watch (see
# integration/openviking.md §1). Use this script only when no Git remote is reachable.
#
# Why a staging copy: OpenViking's directory scanner honors .gitignore, so an
# ignored marker file would never be ingested; and ingesting the working tree
# risks including untracked drafts. `git archive` exports exactly HEAD.
#
# Usage: scripts/ov_refresh.sh [--to viking://resources/repos/web-app-ux] [--no-wait]
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
TO="viking://resources/repos/web-app-ux"
WAIT="--wait"
while [ $# -gt 0 ]; do
  case "$1" in
    --to) TO="$2"; shift 2;;
    --no-wait) WAIT=""; shift;;
    *) echo "unknown arg $1" >&2; exit 2;;
  esac
done
if [ -n "$(git -C "$REPO" status --porcelain)" ]; then
  echo "working tree is not clean; commit first" >&2; exit 1
fi
SHA="$(git -C "$REPO" rev-parse HEAD)"
STAGE="$(mktemp -d /tmp/web-app-ux-ingest.XXXXXX)/web-app-ux"
mkdir -p "$STAGE"
git -C "$REPO" archive HEAD | tar -x -C "$STAGE"
# Not useful in the semantic index: catalog table (chunks dominate results), tooling, assets, PR template.
rm -rf "$STAGE/INDEX.md" "$STAGE/index.json" "$STAGE/scripts" "$STAGE/assets" "$STAGE/.github" "$STAGE/.gitignore"
mkdir -p "$STAGE/integration"
cat > "$STAGE/integration/INGESTED_COMMIT.md" <<MD
# Ingested commit

- repository: web-app-ux
- commit: $SHA
- ingested_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)
- note: compare with \`git rev-parse HEAD\`; if different, the OpenViking copy is stale.
MD
echo "staging: $STAGE  commit: $SHA  target: $TO"
ov add-resource "$STAGE" --to "$TO" \
  --include '*.md' \
  --tags "repo=web-app-ux,kind=ux-knowledge" \
  --processing-mode semantic_and_vectors \
  --args parse_mode:no_split \
  $WAIT -o json | grep -v '^cmd' || true
echo "If the request timed out, processing continues server-side: ov task list"
