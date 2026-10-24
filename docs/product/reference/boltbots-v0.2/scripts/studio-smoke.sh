#!/usr/bin/env bash
# Studio CLI smoke; requires GUI-capable local macOS and Roblox Studio installation.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STUDIO='/Applications/RobloxStudio.app/Contents/MacOS/RobloxStudio'
if [ "$(uname -s 2>/dev/null)" != 'Darwin' ]; then
  echo 'Studio smoke requires owner macOS; this machine is not macOS.' >&2
  exit 2
fi
if [ ! -x "$STUDIO" ]; then
  echo 'Roblox Studio executable not found at standard path.' >&2
  exit 3
fi
"$ROOT/scripts/build.sh"
mkdir -p "$ROOT/logs"
LOG="$ROOT/logs/studio-smoke.log"
# Studio RunScript is an engine test, not a guarantee of full networked gameplay/visuals.
"$STUDIO" --task RunScript --localPlaceFile "$ROOT/build/BoltBotsTycoon.rbxlx" \
  --runScriptFile "$ROOT/scripts/studio-smoke.luau" --outputFile "$LOG" --quitAfterExecution
if [ ! -f "$LOG" ]; then
  echo 'Studio returned without an output file; mark smoke as NOT VERIFIED.' >&2
  exit 4
fi
if ! grep -q 'BOLTBOTS_SMOKE_OK' "$LOG"; then
  echo "Missing expected marker in $LOG. Mark smoke FAIL/NOT VERIFIED." >&2
  exit 5
fi
echo "Studio smoke verified: $LOG"
