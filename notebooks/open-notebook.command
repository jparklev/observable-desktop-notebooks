#!/bin/bash
# Open Observable Desktop notebooks in Ghostty
# Double-click this file to launch the picker

# If launched from Finder (not in a terminal), relaunch in Ghostty
if [[ "$TERM_PROGRAM" != "ghostty" && "$TERM_PROGRAM" != "Apple_Terminal" && -z "$SSH_TTY" ]]; then
    if command -v ghostty &> /dev/null; then
        exec ghostty -e "$0"
    fi
fi

cd "$(dirname "$0")/.."

# Find all notebooks (exclude the launcher itself)
notebooks=(notebooks/*.html)

if [ ${#notebooks[@]} -eq 0 ]; then
    echo "No notebooks found"
    read -p "Press Enter to close..."
    exit 1
fi

# Use fzf for selection
selected=$(printf '%s\n' "${notebooks[@]}" | fzf \
    --height 100% \
    --reverse \
    --border \
    --prompt="Select notebook: " \
    --preview 'grep -o "<title>[^<]*</title>" {} | sed "s/<[^>]*>//g" | head -1' \
    --preview-window=up:1)

if [ -n "$selected" ]; then
    ./observable.py open "$selected"
fi
