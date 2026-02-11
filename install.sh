#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE="$SCRIPT_DIR/get_leetcode_cookie.py"
DEST_NAME="leetcookie"

# Default install directory
INSTALL_DIR="${1:-$HOME/.local/bin}"

if [[ ! -f "$SOURCE" ]]; then
    echo "Error: get_leetcode_cookie.py not found in $SCRIPT_DIR" >&2
    exit 1
fi

# Create install directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Copy and rename
cp "$SOURCE" "$INSTALL_DIR/$DEST_NAME"
chmod +x "$INSTALL_DIR/$DEST_NAME"

echo "Installed $DEST_NAME to $INSTALL_DIR/$DEST_NAME"

# Check if install dir is in PATH
if ! echo "$PATH" | tr ':' '\n' | grep -qx "$INSTALL_DIR"; then
    echo ""
    echo "Warning: $INSTALL_DIR is not in your PATH."
    echo "Add it with:"
    echo "  export PATH=\"$INSTALL_DIR:\$PATH\""
fi
