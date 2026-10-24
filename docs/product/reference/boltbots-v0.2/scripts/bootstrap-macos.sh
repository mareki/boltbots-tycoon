#!/usr/bin/env bash
# Approval-gated helper. Default: report intended work only. No uninspected pipe-to-shell.
set -euo pipefail

APPLY=0
if [ "${1:-}" = '--apply' ]; then
  APPLY=1
elif [ "$#" -gt 0 ]; then
  echo 'Usage: bash scripts/bootstrap-macos.sh [--apply]' >&2
  exit 2
fi

if [ "$(uname -s 2>/dev/null)" != 'Darwin' ]; then
  echo 'This bootstrap runs only on macOS.' >&2
  exit 2
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

say() { printf '\n== %s ==\n' "$1"; }
ask() {
  local answer
  printf '%s [y/N]: ' "$1"
  IFS= read -r answer
  case "$answer" in y|Y|yes|YES) return 0 ;; *) return 1 ;; esac
}

offer_installer() {
  local name="$1" url="$2" interpreter="$3" temp
  if [ "$APPLY" -eq 0 ]; then
    echo "PENDING: download, inspect and (after approval) run $name from $url"
    return 0
  fi
  say "Review installer: $name"
  temp="$(mktemp "${TMPDIR:-/tmp}/rft-installer.XXXXXX")"
  if ! curl -fsSL "$url" -o "$temp"; then
    rm -f "$temp"
    echo "Could not download $name installer" >&2
    return 1
  fi
  printf 'Downloaded %s bytes to %s\n' "$(wc -c < "$temp")" "$temp"
  shasum -a 256 "$temp" || true
  printf '\nFirst 60 lines for review:\n'
  sed -n '1,60p' "$temp"
  echo 'Read the whole local script before approval if desired.'
  if ask "Execute reviewed $name installer with $interpreter?"; then
    "$interpreter" "$temp"
  else
    echo "SKIPPED $name; local installer was not executed."
  fi
  rm -f "$temp"
}

say 'Step 1 - macOS environment'
bash scripts/doctor-macos.sh || true

say 'Step 2 - Apple developer tools / Git'
if xcode-select -p >/dev/null 2>&1; then
  echo 'Apple developer tools already selected.'
else
  if [ "$APPLY" -eq 0 ]; then
    echo 'PENDING: xcode-select --install (interactive macOS system dialog)'
  elif ask 'Open macOS Xcode Command Line Tools installer dialog?'; then
    xcode-select --install || echo 'macOS dialog may already be open.'
  fi
fi

say 'Step 3 - Codex CLI'
if command -v codex >/dev/null 2>&1; then
  echo "Existing Codex: $(command -v codex)"
else
  offer_installer 'OpenAI Codex' 'https://chatgpt.com/codex/install.sh' 'sh'
fi

say 'Step 4 - Rokit toolchain manager'
if command -v rokit >/dev/null 2>&1; then
  echo "Existing Rokit: $(command -v rokit)"
else
  offer_installer 'Rokit' 'https://raw.githubusercontent.com/rojo-rbx/rokit/main/scripts/install.sh' 'bash'
fi

# New tools may only be visible in a fresh shell after installer modifies PATH.
say 'Step 5 - Pinned Rojo project tool'
if command -v rokit >/dev/null 2>&1; then
  if [ "$APPLY" -eq 0 ]; then
    echo 'PENDING: rokit install'
  elif ask 'Install pinned project tools from rokit.toml?'; then
    rokit install
  fi
else
  echo 'Rokit not in PATH. Start a fresh shell after installer, then rerun.'
fi

say 'Step 6 - Roblox Studio'
STUDIO='/Applications/RobloxStudio.app/Contents/MacOS/RobloxStudio'
if [ -x "$STUDIO" ]; then
  echo 'Studio found at standard app path.'
  if command -v rojo >/dev/null 2>&1; then
    if [ "$APPLY" -eq 0 ]; then
      echo 'OPTIONAL: rojo plugin install (Studio plugin)'
    elif ask 'Install/update Rojo plugin into local Roblox Studio?'; then
      rojo plugin install
    fi
  fi
else
  echo 'Requires official RobloxStudio.dmg download + account sign-in.'
  if [ "$APPLY" -eq 0 ]; then
    echo 'PENDING: open https://create.roblox.com/docs/studio/setup'
  elif ask 'Open official Roblox Studio setup page in browser?'; then
    open 'https://create.roblox.com/docs/studio/setup'
  fi
fi

say 'Next checks'
echo 'When the tools appear in PATH and Studio is installed:'
echo '  bash scripts/build.sh'
echo '  bash scripts/studio-smoke.sh'
echo 'No Roblox public publishing, API key creation or paid actions are included.'
