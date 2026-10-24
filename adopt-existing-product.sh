#!/usr/bin/env bash
set -euo pipefail

HARNESS_VERSION="1.5.3"
HARNESS_TAG="20260930-1.5.3-remove-added-rules"
CANONICAL_REPOSITORY="https://github.com/langvis/agentic_harness.git"

TARGET=""
SOURCE_ROOT=""
ASSUME_YES=false

usage() {
  cat <<'EOF'
Safely stage Agentic Harness 1.5.3 in an existing Product Git repository.

Usage:
  adopt-existing-product.sh --target PATH [--yes]

Options:
  --target PATH  Existing Product repository root (required)
  --source PATH  Explicit trusted local 1.5.3 Harness tag checkout (offline/testing)
  --yes          Apply the displayed Core-only plan without an interactive prompt
  --help         Show this help

This command creates only .agentic-harness/** and leaves it inactive_staged. It never rewrites
Product-owned root, routing, lifecycle, plan, code, or historical Contract files.
EOF
}

fail() { printf 'Harness adoption failed: %s\n' "$*" >&2; exit 1; }

while (($#)); do
  case "$1" in
    --target) [[ $# -ge 2 ]] || fail "--target requires a value"; TARGET=$2; shift 2 ;;
    --source) [[ $# -ge 2 ]] || fail "--source requires a value"; SOURCE_ROOT=$2; shift 2 ;;
    --yes) ASSUME_YES=true; shift ;;
    --help|-h) usage; exit 0 ;;
    *) fail "unknown argument: $1" ;;
  esac
done

[[ -n "$TARGET" ]] || fail "--target is required"
command -v git >/dev/null 2>&1 || fail "git is required"
command -v python3 >/dev/null 2>&1 || fail "Python 3 is required"
python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)' \
  || fail "Python 3.10 or newer is required"

TARGET=$(python3 - "$TARGET" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1]).absolute()
if path.is_symlink() or not path.is_dir():
    raise SystemExit("target must be an existing regular directory")
for component in (path, *path.parents):
    if component.is_symlink():
        raise SystemExit(f"target path contains a symlink: {component}")
resolved = path.resolve(strict=True)
if resolved == pathlib.Path(resolved.anchor) or resolved == pathlib.Path.home().resolve():
    raise SystemExit("target may not be the filesystem root or home directory")
print(resolved)
PY
) || fail "unsafe target"

GIT_ROOT=$(git -C "$TARGET" rev-parse --show-toplevel 2>/dev/null || true)
[[ -n "$GIT_ROOT" ]] || fail "target must already be a Git repository"
GIT_ROOT=$(python3 -c 'import pathlib,sys; print(pathlib.Path(sys.argv[1]).resolve())' "$GIT_ROOT")
[[ "$GIT_ROOT" == "$TARGET" ]] || fail "--target must be the Product repository root"

WORK_DIR=$(mktemp -d "${TMPDIR:-/tmp}/agentic-harness-adoption.XXXXXX")
LOCK_DIR="$(dirname "$TARGET")/.$(basename "$TARGET").agentic-harness-adoption-lock"
LOCK_HELD=false
cleanup() {
  if [[ "$LOCK_HELD" == true ]]; then rmdir "$LOCK_DIR" 2>/dev/null || true; fi
  if [[ -d "$WORK_DIR" ]]; then find "$WORK_DIR" -depth -delete 2>/dev/null || true; fi
}
trap cleanup EXIT INT TERM

if [[ -n "$SOURCE_ROOT" ]]; then
  SOURCE_ROOT=$(python3 -c 'import pathlib,sys; print(pathlib.Path(sys.argv[1]).resolve(strict=True))' "$SOURCE_ROOT")
  [[ -d "$SOURCE_ROOT/harness/tools" ]] || fail "--source is not an Agentic Harness checkout"
  EXPECTED_SOURCE_URL=$(git -C "$SOURCE_ROOT" remote get-url origin 2>/dev/null || true)
  [[ -n "$EXPECTED_SOURCE_URL" ]] || fail "trusted local source has no origin"
else
  SOURCE_ROOT="$WORK_DIR/source"
  git clone --quiet --depth 1 --branch "$HARNESS_TAG" "$CANONICAL_REPOSITORY" "$SOURCE_ROOT" \
    || fail "cannot clone ${HARNESS_TAG}; authenticate Git access to ${CANONICAL_REPOSITORY}"
  EXPECTED_SOURCE_URL="$CANONICAL_REPOSITORY"
fi

python3 - "$SOURCE_ROOT" "$TARGET" <<'PY'
import pathlib, sys
source, target = (pathlib.Path(value).resolve(strict=True) for value in sys.argv[1:])
if source == target or source in target.parents or target in source.parents:
    raise SystemExit("Harness source and Product target may not overlap")
PY

RELEASE_DIR="$WORK_DIR/release"
python3 "$SOURCE_ROOT/harness/tools/assemble_release.py" \
  --root "$SOURCE_ROOT" --output "$RELEASE_DIR" \
  --tagged-source-bootstrap --expected-source-url "$EXPECTED_SOURCE_URL"

RELEASE_EVIDENCE="$WORK_DIR/release.release-evidence.json"
MANIFEST_SHA=$(python3 - "$RELEASE_EVIDENCE" "$HARNESS_VERSION" <<'PY'
import json, pathlib, sys
value = json.loads(pathlib.Path(sys.argv[1]).read_text())
if value.get("version") != sys.argv[2] or value.get("distribution_mode") != "tagged_source_bootstrap":
    raise SystemExit("assembled source is not the requested exact-tag distribution")
print(value["manifest_sha256"])
PY
) || fail "release evidence is invalid"

PLAN_JSON="$WORK_DIR/adoption-plan.json"
python3 "$SOURCE_ROOT/harness/tools/install_or_upgrade.py" adopt \
  --release "$RELEASE_DIR" --target "$TARGET" \
  --release-manifest-sha256 "$MANIFEST_SHA" >"$PLAN_JSON"
cat "$PLAN_JSON"

PLAN_SHA=$(python3 -c 'import hashlib,pathlib,sys; print(hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest())' "$PLAN_JSON")
if [[ "$ASSUME_YES" != true ]]; then
  printf 'Stage this exact Core-only plan in %s? Type ADOPT to continue: ' "$TARGET"
  read -r CONFIRMATION
  [[ "$CONFIRMATION" == "ADOPT" ]] || fail "adoption cancelled; no Product files changed"
fi

mkdir "$LOCK_DIR" 2>/dev/null || fail "another adoption owns the Product repository lock: $LOCK_DIR"
LOCK_HELD=true
TRANSACTION_ID="adopt-$(printf '%s' "$HARNESS_VERSION" | tr '.' '-')-${PLAN_SHA:0:12}"

python3 "$SOURCE_ROOT/harness/tools/install_or_upgrade.py" adopt \
  --release "$RELEASE_DIR" --target "$TARGET" \
  --release-manifest-sha256 "$MANIFEST_SHA" \
  --run-authority-reference "adoption-confirmation:${PLAN_SHA}" \
  --transaction-id "$TRANSACTION_ID" --apply

printf '\nAgentic Harness %s Core is safely staged in %s.\n' "$HARNESS_VERSION" "$TARGET"
printf 'No Product-owned file was changed. Core remains inactive until Human-authorized root/routing integration and Context coverage are recorded.\n'
