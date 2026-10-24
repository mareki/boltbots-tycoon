#!/usr/bin/env bash
# One-command handoff to Codex on the project owner's Mac.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
if [ "$(uname -s)" != 'Darwin' ]; then
  echo 'Run this launcher on your Mac. It cannot connect to your Mac remotely.' >&2
  exit 2
fi
if ! command -v codex >/dev/null 2>&1; then
  echo 'Codex CLI is not installed or not in PATH.' >&2
  echo 'Official guide: https://learn.chatgpt.com/docs/cli' >&2
  echo 'After installing and signing in, run this script again.' >&2
  exit 3
fi
printf '%s\n' 'Launching Codex with BoltBots project instructions.'
exec codex "$(cat "$ROOT/docs/FIRST_CODEX_TASK.md")"
