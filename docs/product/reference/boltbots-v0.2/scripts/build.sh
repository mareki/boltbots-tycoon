#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
if ! command -v rojo >/dev/null 2>&1; then
  echo 'Rojo is not in PATH. Run rokit install / shell setup first.' >&2
  exit 3
fi
mkdir -p build
rojo build default.project.json -o build/BoltBotsTycoon.rbxlx
if [ ! -s build/BoltBotsTycoon.rbxlx ]; then
  echo 'Build file was not created or is empty.' >&2
  exit 4
fi
printf 'Rojo place generated: %s\n' "$ROOT/build/BoltBotsTycoon.rbxlx"
