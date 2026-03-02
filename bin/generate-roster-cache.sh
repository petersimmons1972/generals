#!/bin/bash
# generate-roster-cache.sh
# Wrapper: runs the Python cache generator for generals roster.
# Usage: ./generate-roster-cache.sh
#        Called by ~/.claude/refresh-generals-cache.sh at session start.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/generate-roster-cache.py"

if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    echo "ERROR: Python script not found: $PYTHON_SCRIPT" >&2
    exit 1
fi

# Try python3 first, then python
PYTHON=""
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "ERROR: No python interpreter found" >&2
    exit 1
fi

echo "Generating generals roster cache..."
"$PYTHON" "$PYTHON_SCRIPT"
