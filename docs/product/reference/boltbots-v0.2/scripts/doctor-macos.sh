#!/usr/bin/env bash
# Read-only environment preflight. Safe to run without approval.
set -u

report() { printf '%-23s %s\n' "$1" "$2"; }
has() { command -v "$1" >/dev/null 2>&1; }

printf '%s\n' 'BoltBots Tycoon: macOS environment doctor' '------------------------------------------------'
if [ "$(uname -s 2>/dev/null)" != "Darwin" ]; then
  report 'Operating system' 'NOT macOS. Run this script on the owner Mac.'
  exit 2
fi
report 'macOS' "$(sw_vers -productVersion 2>/dev/null || echo unknown)"
report 'CPU architecture' "$(uname -m 2>/dev/null || echo unknown)"
for cmd in git curl codex rokit rojo brew; do
  if has "$cmd"; then
    path="$(command -v "$cmd")"
    report "$cmd" "$path"
  else
    report "$cmd" 'MISSING'
  fi
done
if xcode-select -p >/dev/null 2>&1; then
  report 'Xcode CLT' "$(xcode-select -p)"
else
  report 'Xcode CLT' 'MISSING or not selected'
fi
STUDIO='/Applications/RobloxStudio.app/Contents/MacOS/RobloxStudio'
if [ -x "$STUDIO" ]; then
  report 'Roblox Studio' "$STUDIO"
else
  report 'Roblox Studio' 'NOT FOUND at standard system path'
fi
if has rojo; then rojo --version 2>&1 || true; fi
if has rokit; then rokit --version 2>&1 || true; fi
if has codex; then codex --version 2>&1 || true; fi
printf '%s\n' 'Doctor is read-only. Missing tools are not installed by this script.'
