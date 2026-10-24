#!/usr/bin/env bash
# Harness1.5 upgrade: invoke under authority for this target and its disclosed changes.
# This fixed-target tool replaces Core only; it never migrates Product-owned files.
set -euo pipefail

HARNESS_VERSION="1.5.3"
HARNESS_TAG="20260930-1.5.3-remove-added-rules"
CANONICAL_REPOSITORY="https://github.com/langvis/agentic_harness.git"
SCRIPT_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)

fail() { printf 'Product Harness upgrade failed: %s\n' "$*" >&2; exit 1; }

if (($#)); then
  fail "this release-specific upgrade command accepts no arguments"
fi
command -v git >/dev/null 2>&1 || fail "git is required"
command -v python3 >/dev/null 2>&1 || fail "Python 3 is required"

TARGET=$(git rev-parse --show-toplevel 2>/dev/null || true)
[[ -n "$TARGET" && "$TARGET" == "$PWD" ]] || fail "run the command from the Product Git repository root"
[[ -d "$TARGET/.agentic-harness" ]] || fail "no installed .agentic-harness directory found"

WORK_DIR=$(mktemp -d "${TMPDIR:-/tmp}/agentic-harness-upgrade.XXXXXX")
cleanup() { [[ ! -d "$WORK_DIR" ]] || find "$WORK_DIR" -depth -delete 2>/dev/null || true; }
trap cleanup EXIT INT TERM

SOURCE_ROOT=""
if [[ -f "$SCRIPT_ROOT/harness/tools/assemble_release.py" ]] \
  && [[ "$(git -C "$SCRIPT_ROOT" tag --points-at HEAD 2>/dev/null || true)" == "$HARNESS_TAG" ]]; then
  SOURCE_ROOT="$SCRIPT_ROOT"
else
  SOURCE_ROOT="$WORK_DIR/source"
  git clone --quiet --depth 1 --branch "$HARNESS_TAG" "$CANONICAL_REPOSITORY" "$SOURCE_ROOT" \
    || fail "cannot obtain exact Harness tag $HARNESS_TAG"
fi

RELEASE_DIR="$WORK_DIR/release"
python3 "$SOURCE_ROOT/harness/tools/assemble_release.py" \
  --root "$SOURCE_ROOT" --output "$RELEASE_DIR" \
  --tagged-source-bootstrap --expected-source-url "$CANONICAL_REPOSITORY" \
  >/dev/null || fail "cannot authenticate and assemble Harness $HARNESS_VERSION"

MANIFEST_SHA=$(python3 - "$WORK_DIR/release.release-evidence.json" "$HARNESS_VERSION" <<'PY'
import json, pathlib, sys
value = json.loads(pathlib.Path(sys.argv[1]).read_text())
if value.get("version") != sys.argv[2]:
    raise SystemExit("assembled release version mismatch")
print(value["manifest_sha256"])
PY
) || fail "cannot derive authenticated target manifest"

RESULT=$(python3 "$SOURCE_ROOT/harness/tools/replace_harness.py" \
  --release "$RELEASE_DIR" --target "$TARGET" \
  --expected-manifest-sha256 "$MANIFEST_SHA") || fail "Core replacement failed; prior Core was restored"

python3 - "$RESULT" <<'PY'
import json, sys
value = json.loads(sys.argv[1])
print(f"Agentic Harness {value['to_version']}: {value['action']}.")
if value.get("history"):
    print("Recalibration history:")
    for path in value["history"]:
        print(f"- {path}")
    print(f"Next: assess only concrete Product impact and record {value['recalibration']}.")
else:
    print("No Product file was changed; no recalibration is needed.")
PY
