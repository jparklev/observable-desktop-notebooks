#!/usr/bin/env python3
"""
Observable Desktop CLI - Integration toolkit for Claude Code

Features:
- Cell-level editing (add, edit, delete, list cells)
- File watching with fswatch
- Visual feedback via screenshots
- Two-way sync detection
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import html


@dataclass
class Cell:
    """Represents a notebook cell"""
    id: Optional[str]
    type: str  # module, text/markdown, text/html, etc.
    content: str
    pinned: bool = False
    hidden: bool = False
    index: int = 0


class Notebook:
    """Parse and manipulate Observable notebook HTML files"""

    def __init__(self, path: str):
        self.path = Path(path)
        self.title = "Untitled"
        self.theme = None
        self.cells: list[Cell] = []
        self._raw = ""

        if self.path.exists():
            self.load()

    def load(self):
        """Load notebook from file"""
        self._raw = self.path.read_text()

        # Extract theme
        theme_match = re.search(r'<notebook\s+theme="([^"]*)"', self._raw)
        self.theme = theme_match.group(1) if theme_match else None

        # Extract title
        title_match = re.search(r'<title>([^<]*)</title>', self._raw)
        self.title = title_match.group(1) if title_match else "Untitled"

        # Extract cells (script tags)
        self.cells = []
        pattern = r'<script([^>]*)>(.*?)</script>'
        for idx, match in enumerate(re.finditer(pattern, self._raw, re.DOTALL)):
            attrs_str, content = match.groups()

            # Parse attributes
            cell_id = None
            cell_type = "module"
            pinned = False
            hidden = False

            id_match = re.search(r'id="([^"]*)"', attrs_str)
            if id_match:
                cell_id = id_match.group(1)

            type_match = re.search(r'type="([^"]*)"', attrs_str)
            if type_match:
                cell_type = type_match.group(1)

            pinned = 'pinned' in attrs_str
            hidden = 'hidden' in attrs_str

            self.cells.append(Cell(
                id=cell_id,
                type=cell_type,
                content=content.strip(),
                pinned=pinned,
                hidden=hidden,
                index=idx
            ))

    def save(self):
        """Save notebook to file"""
        self.path.write_text(self.to_html())

    def to_html(self) -> str:
        """Generate HTML from notebook"""
        theme_attr = f' theme="{self.theme}"' if self.theme else ''

        lines = [
            '<!doctype html>',
            f'<notebook{theme_attr}>',
            f'  <title>{html.escape(self.title)}</title>',
        ]

        for cell in self.cells:
            attrs = []
            if cell.id:
                attrs.append(f'id="{cell.id}"')
            if cell.type != "module":
                attrs.append(f'type="{cell.type}"')
            else:
                attrs.append('type="module"')
            if cell.pinned:
                attrs.append('pinned')
            if cell.hidden:
                attrs.append('hidden')

            attr_str = ' '.join(attrs)
            lines.append(f'  <script {attr_str}>')
            lines.append(cell.content)
            lines.append('  </script>')

        lines.append('</notebook>')
        return '\n'.join(lines) + '\n'

    def add_cell(self, content: str, cell_type: str = "application/vnd.observable.javascript",
                 pinned: bool = True, cell_id: Optional[str] = None,
                 index: Optional[int] = None) -> Cell:
        """Add a new cell (defaults to Observable JavaScript for reactivity)"""
        cell = Cell(
            id=cell_id or f"cell-{len(self.cells) + 1}",
            type=cell_type,
            content=content,
            pinned=pinned,
            index=len(self.cells)
        )

        if index is not None and 0 <= index <= len(self.cells):
            self.cells.insert(index, cell)
            # Re-index
            for i, c in enumerate(self.cells):
                c.index = i
        else:
            self.cells.append(cell)

        return cell

    def edit_cell(self, identifier: str | int, content: str) -> bool:
        """Edit a cell by ID or index"""
        cell = self.get_cell(identifier)
        if cell:
            cell.content = content
            return True
        return False

    def delete_cell(self, identifier: str | int) -> bool:
        """Delete a cell by ID or index"""
        cell = self.get_cell(identifier)
        if cell:
            self.cells.remove(cell)
            # Re-index
            for i, c in enumerate(self.cells):
                c.index = i
            return True
        return False

    def get_cell(self, identifier: str | int) -> Optional[Cell]:
        """Get cell by ID or index"""
        if isinstance(identifier, int):
            if 0 <= identifier < len(self.cells):
                return self.cells[identifier]
        else:
            for cell in self.cells:
                if cell.id == identifier:
                    return cell
        return None

    def list_cells(self) -> list[dict]:
        """List all cells with metadata"""
        return [
            {
                "index": c.index,
                "id": c.id,
                "type": c.type,
                "pinned": c.pinned,
                "preview": c.content[:50].replace('\n', ' ') + ('...' if len(c.content) > 50 else '')
            }
            for c in self.cells
        ]


def get_observable_window_id() -> Optional[int]:
    """Get the window ID for Observable Desktop without changing focus"""
    # Compile and cache the Swift helper for getting window IDs
    swift_code = '''
import Cocoa
let options = CGWindowListOption(arrayLiteral: .optionOnScreenOnly)
if let windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID) as? [[String: Any]] {
    for window in windowList {
        if let owner = window[kCGWindowOwnerName as String] as? String,
           owner.contains("Observable") {
            if let windowID = window[kCGWindowNumber as String] as? Int {
                print(windowID)
                break
            }
        }
    }
}
'''
    swift_file = Path(tempfile.gettempdir()) / "get_obs_window.swift"
    binary_file = Path(tempfile.gettempdir()) / "get_obs_window"

    # Compile if needed
    if not binary_file.exists() or swift_file.stat().st_mtime > binary_file.stat().st_mtime if binary_file.exists() else True:
        swift_file.write_text(swift_code)
        subprocess.run(['swiftc', str(swift_file), '-o', str(binary_file)],
                      capture_output=True)

    result = subprocess.run([str(binary_file)], capture_output=True, text=True)
    if result.stdout.strip():
        try:
            return int(result.stdout.strip())
        except ValueError:
            pass
    return None


def take_screenshot(output_path: Optional[str] = None, background: bool = True) -> str:
    """Take screenshot of Observable Desktop window

    Args:
        output_path: Where to save the screenshot
        background: If True, capture without stealing focus (default)
    """
    if output_path is None:
        output_path = tempfile.mktemp(suffix='.png')

    if background:
        # Get window ID and capture without focus change
        window_id = get_observable_window_id()
        if window_id:
            subprocess.run(['screencapture', '-l', str(window_id), '-o', '-x', output_path],
                          capture_output=True)
            return output_path

    # Fallback: bring to front and capture
    script = '''
    tell application "System Events"
        tell process "Observable Desktop"
            set frontmost to true
            if (count of windows) > 0 then
                perform action "AXRaise" of window 1
            end if
        end tell
    end tell
    '''
    subprocess.run(['osascript', '-e', script], capture_output=True)
    time.sleep(0.3)
    subprocess.run(['screencapture', '-o', '-x', output_path], capture_output=True)

    return output_path


def reload_notebook(file_path: str, background: bool = False):
    """Close and reopen notebook in Observable Desktop

    Improvements:
    - Uses 'open -g' to avoid pulling focus on open
    - Uses Accessibility 'click button 1' (close button) to avoid pulling focus on close
    - Ensures all windows are closed to prevent 'multiple windows' bug
    """
    full_path = str(Path(file_path).resolve())

    # Remember current frontmost app if doing background reload
    prev_app = None
    if background:
        result = subprocess.run([
            'osascript', '-e',
            'tell application "System Events" to get name of first process whose frontmost is true'
        ], capture_output=True, text=True)
        prev_app = result.stdout.strip()

    # Close ALL Observable windows to ensure clean slate using Accessibility (no activation needed)
    script = '''
    tell application "System Events"
        if exists process "Observable Desktop" then
            tell process "Observable Desktop"
                -- Close all windows
                repeat while (count of windows) > 0
                    try
                        click button 1 of window 1
                    on error
                        exit repeat
                    end try
                    delay 0.1
                end repeat
            end tell
        end if
    end tell
    '''
    subprocess.run(['osascript', '-e', script], capture_output=True)
    time.sleep(0.5)

    # Reopen in background
    # -g: Do not bring to the foreground
    subprocess.run(['open', '-g', '-a', 'Observable Desktop', full_path], capture_output=True)

    # Restore focus if background mode (safety check)
    if background and prev_app and prev_app != "Observable Desktop":
        # Check if we accidentally stole focus
        check = subprocess.run([
            'osascript', '-e',
            'tell application "System Events" to get name of first process whose frontmost is true'
        ], capture_output=True, text=True)
        
        if check.stdout.strip() == "Observable Desktop":
            subprocess.run([
                'osascript', '-e',
                f'tell application "{prev_app}" to activate'
            ], capture_output=True)


def scroll_to_cell(cell_index: int, total_cells: int, restore_focus: bool = True):
    """Scroll Observable window to show a specific cell

    Uses Page Down key presses since we can't inject JS into WKWebView.
    For cells in the last third of the notebook, scrolls to bottom instead.
    """
    # For cells near the end, just go to bottom
    if cell_index >= total_cells * 0.6:
        scroll_to_bottom(restore_focus=restore_focus)
        return

    # For earlier cells, scroll from top
    # Reduce ratio slightly to ensure we don't overshoot
    pages_down = max(0, int(cell_index / 1.8))

    restore_script = '''
    if prevApp is not "Observable Desktop" then
        tell application prevApp to activate
    end if
    ''' if restore_focus else ''

    script = f'''
    -- Save current app
    tell application "System Events"
        set prevApp to name of first process whose frontmost is true
    end tell

    -- Activate Observable and scroll
    tell application "Observable Desktop" to activate
    -- Reduced delays for better ergonomics
    delay 0.1
    tell application "System Events"
        tell process "Observable Desktop"
            set frontmost to true
            delay 0.05
            -- Scroll to top
            key code 126 using {{command down}}
            delay 0.1
            -- Page down to cell
            repeat {pages_down} times
                key code 121
                delay 0.05
            end repeat
        end tell
    end tell

    -- Restore previous app
    {restore_script}
    '''
    subprocess.run(['osascript', '-e', script], capture_output=True)


def scroll_down(pages: int = 1, restore_focus: bool = True):
    """Scroll down by a number of pages"""
    restore_script = '''
    if prevApp is not "Observable Desktop" then
        tell application prevApp to activate
    end if
    ''' if restore_focus else ''

    script = f'''
    tell application "System Events"
        set prevApp to name of first process whose frontmost is true
    end tell

    tell application "Observable Desktop" to activate
    delay 0.1
    tell application "System Events"
        tell process "Observable Desktop"
            repeat {pages} times
                key code 121  -- Page Down
                delay 0.05
            end repeat
        end tell
    end tell

    {restore_script}
    '''
    subprocess.run(['osascript', '-e', script], capture_output=True)


def scroll_to_bottom(restore_focus: bool = True):
    """Scroll to the bottom of the notebook, then up slightly to show output"""
    # Save current app, activate Observable, scroll, restore
    script = f'''
    -- Save current app
    tell application "System Events"
        set prevApp to name of first process whose frontmost is true
    end tell

    -- Activate Observable and scroll
    tell application "Observable Desktop" to activate
    delay 0.1
    tell application "System Events"
        tell process "Observable Desktop"
            set frontmost to true
            delay 0.05
            -- Scroll down aggressively
            repeat 12 times
                key code 121  -- Page Down
                delay 0.02
            end repeat
            delay 0.1
            -- Then scroll back up a bit to show cell output (not just code)
            repeat 2 times
                key code 116  -- Page Up
                delay 0.05
            end repeat
        end tell
    end tell

    -- Restore previous app
    {"" if not restore_focus else '''
    if prevApp is not "Observable Desktop" then
        tell application prevApp to activate
    end if
    '''}
    '''
    subprocess.run(['osascript', '-e', script], capture_output=True)


def watch_file(file_path: str, callback=None):
    """Watch file for changes using fswatch"""
    full_path = str(Path(file_path).resolve())

    print(f"Watching: {full_path}")
    print("Press Ctrl+C to stop")

    # Open initially
    subprocess.run(['open', '-a', 'Observable Desktop', full_path], capture_output=True)

    # Use fswatch
    proc = subprocess.Popen(
        ['fswatch', '-1', '--event', 'Updated', full_path],
        stdout=subprocess.PIPE,
        text=True
    )

    try:
        while True:
            proc.wait()
            print(f"{time.strftime('%H:%M:%S')} - File changed, reloading...")
            reload_notebook(full_path)

            if callback:
                callback(full_path)

            # Restart fswatch
            proc = subprocess.Popen(
                ['fswatch', '-1', '--event', 'Updated', full_path],
                stdout=subprocess.PIPE,
                text=True
            )
    except KeyboardInterrupt:
        proc.terminate()
        print("\nStopped watching")


def edit_and_view(file_path: str, cell_id: str | int, content: str,
                  background: bool = True, scroll_to: bool = True) -> str:
    """Edit a cell and return screenshot path for visual feedback

    Args:
        file_path: Path to notebook
        cell_id: Cell index or ID to edit
        content: New cell content
        background: Don't steal focus from current app
        scroll_to: Scroll to the edited cell before screenshot
    """
    nb = Notebook(file_path)

    # Find the cell to get its index
    cell = nb.get_cell(cell_id)
    if not cell:
        raise ValueError(f"Cell not found: {cell_id}")

    cell_index = cell.index

    if nb.edit_cell(cell_id, content):
        nb.save()
        time.sleep(0.2)
        reload_notebook(file_path, background=background)
        time.sleep(1.5)  # Wait for render

        # Scroll to the edited cell if requested
        if scroll_to and cell_index > 0:
            scroll_to_cell(cell_index, len(nb.cells))
            time.sleep(0.3)

        screenshot = take_screenshot(background=background)
        return screenshot
    else:
        raise ValueError(f"Cell not found: {cell_id}")


def main():
    parser = argparse.ArgumentParser(
        description="Observable Desktop CLI for Claude Code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s new my-notebook.html
  %(prog)s list notebook.html
  %(prog)s add notebook.html "Plot.plot({marks: [Plot.dot([1,2,3])]})"
  %(prog)s edit notebook.html 0 "// Updated code"
  %(prog)s watch notebook.html
  %(prog)s screenshot
  %(prog)s edit-and-view notebook.html 1 "2 + 2"
        """
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # new
    new_p = subparsers.add_parser('new', help='Create new notebook')
    new_p.add_argument('path', help='Path for new notebook')
    new_p.add_argument('--title', default='New Notebook', help='Notebook title')
    new_p.add_argument('--theme', help='Theme (air, slate, etc.)')

    # open
    open_p = subparsers.add_parser('open', help='Open notebook')
    open_p.add_argument('path', help='Notebook path')

    # list
    list_p = subparsers.add_parser('list', help='List cells')
    list_p.add_argument('path', help='Notebook path')
    list_p.add_argument('--json', action='store_true', help='Output JSON')

    # add
    add_p = subparsers.add_parser('add', help='Add cell')
    add_p.add_argument('path', help='Notebook path')
    add_p.add_argument('content', help='Cell content')
    add_p.add_argument('--type', '-t', default='ojs',
                       help='Cell type: ojs (default), js, md, html, sql, tex')
    add_p.add_argument('--id', help='Cell ID')
    add_p.add_argument('--index', type=int, help='Insert at index')
    add_p.add_argument('--no-pin', action='store_true', help='Do not pin cell')

    # edit
    edit_p = subparsers.add_parser('edit', help='Edit cell')
    edit_p.add_argument('path', help='Notebook path')
    edit_p.add_argument('cell', help='Cell ID or index')
    edit_p.add_argument('content', help='New content')

    # delete
    del_p = subparsers.add_parser('delete', help='Delete cell')
    del_p.add_argument('path', help='Notebook path')
    del_p.add_argument('cell', help='Cell ID or index')

    # get
    get_p = subparsers.add_parser('get', help='Get cell content')
    get_p.add_argument('path', help='Notebook path')
    get_p.add_argument('cell', help='Cell ID or index')

    # watch
    watch_p = subparsers.add_parser('watch', help='Watch and auto-reload')
    watch_p.add_argument('path', help='Notebook path')

    # reload
    reload_p = subparsers.add_parser('reload', help='Reload notebook')
    reload_p.add_argument('path', help='Notebook path')

    # scroll
    scroll_p = subparsers.add_parser('scroll', help='Scroll the notebook')
    scroll_p.add_argument('--down', '-d', type=int, metavar='N', help='Scroll down N pages')
    scroll_p.add_argument('--bottom', '-b', action='store_true', help='Scroll to bottom')
    scroll_p.add_argument('--top', '-t', action='store_true', help='Scroll to top')

    # screenshot
    ss_p = subparsers.add_parser('screenshot', help='Take screenshot')
    ss_p.add_argument('--output', '-o', help='Output path')
    ss_p.add_argument('--foreground', '-f', action='store_true',
                     help='Bring Observable to front (default: background capture)')

    # edit-and-view
    ev_p = subparsers.add_parser('edit-and-view', help='Edit cell and get screenshot')
    ev_p.add_argument('path', help='Notebook path')
    ev_p.add_argument('cell', help='Cell ID or index')
    ev_p.add_argument('content', help='New content')
    ev_p.add_argument('--foreground', '-f', action='store_true',
                     help='Bring Observable to front (default: background)')
    ev_p.add_argument('--no-scroll', action='store_true',
                     help='Do not scroll to edited cell')

    # reload
    reload_p.add_argument('--background', '-b', action='store_true',
                         help='Restore focus to previous app after reload')

    args = parser.parse_args()

    # Type shorthand expansion
    TYPE_MAP = {
        'ojs': 'application/vnd.observable.javascript',
        'js': 'module',
        'md': 'text/markdown',
        'html': 'text/html',
        'sql': 'application/sql',
        'tex': 'application/x-tex',
        'ts': 'text/x-typescript',
        'dot': 'text/vnd.graphviz',
    }

    def expand_type(t):
        return TYPE_MAP.get(t, t)

    try:
        if args.command == 'new':
            nb = Notebook(args.path)
            nb.title = args.title
            nb.theme = args.theme
            nb.add_cell("# " + args.title, "text/markdown", pinned=False)
            nb.add_cell("// Your code here\n1 + 1", "application/vnd.observable.javascript", pinned=True)
            nb.save()
            print(f"Created: {args.path}")
            subprocess.run(['open', '-a', 'Observable Desktop', str(Path(args.path).resolve())])

        elif args.command == 'open':
            subprocess.run(['open', '-a', 'Observable Desktop', str(Path(args.path).resolve())])

        elif args.command == 'list':
            nb = Notebook(args.path)
            cells = nb.list_cells()
            if args.json:
                print(json.dumps(cells, indent=2))
            else:
                print(f"Notebook: {nb.title}")
                print(f"Cells: {len(cells)}")
                print("-" * 60)
                for c in cells:
                    pin = "[pinned]" if c['pinned'] else ""
                    print(f"  {c['index']}: ({c['id']}) [{c['type']}] {pin}")
                    print(f"      {c['preview']}")

        elif args.command == 'add':
            nb = Notebook(args.path)
            cell = nb.add_cell(
                args.content,
                cell_type=expand_type(args.type),
                pinned=not args.no_pin,
                cell_id=args.id,
                index=args.index
            )
            nb.save()
            print(f"Added cell {cell.index} ({cell.id})")

        elif args.command == 'edit':
            nb = Notebook(args.path)
            # Try as int first
            try:
                cell_id = int(args.cell)
            except ValueError:
                cell_id = args.cell

            if nb.edit_cell(cell_id, args.content):
                nb.save()
                print(f"Edited cell {args.cell}")
            else:
                print(f"Cell not found: {args.cell}", file=sys.stderr)
                sys.exit(1)

        elif args.command == 'delete':
            nb = Notebook(args.path)
            try:
                cell_id = int(args.cell)
            except ValueError:
                cell_id = args.cell

            if nb.delete_cell(cell_id):
                nb.save()
                print(f"Deleted cell {args.cell}")
            else:
                print(f"Cell not found: {args.cell}", file=sys.stderr)
                sys.exit(1)

        elif args.command == 'get':
            nb = Notebook(args.path)
            try:
                cell_id = int(args.cell)
            except ValueError:
                cell_id = args.cell

            cell = nb.get_cell(cell_id)
            if cell:
                print(cell.content)
            else:
                print(f"Cell not found: {args.cell}", file=sys.stderr)
                sys.exit(1)

        elif args.command == 'watch':
            watch_file(args.path)

        elif args.command == 'reload':
            reload_notebook(args.path, background=args.background)
            print("Reloaded")

        elif args.command == 'scroll':
            if args.bottom:
                scroll_to_bottom()
                print("Scrolled to bottom")
            elif args.top:
                script = '''
                tell application "System Events"
                    tell process "Observable Desktop"
                        key code 126 using {command down}
                    end tell
                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True)
                print("Scrolled to top")
            elif args.down:
                scroll_down(args.down)
                print(f"Scrolled down {args.down} pages")
            else:
                print("Use --down N, --bottom, or --top")

        elif args.command == 'screenshot':
            path = take_screenshot(args.output, background=not args.foreground)
            print(path)

        elif args.command == 'edit-and-view':
            try:
                cell_id = int(args.cell)
            except ValueError:
                cell_id = args.cell

            screenshot = edit_and_view(
                args.path, cell_id, args.content,
                background=not args.foreground,
                scroll_to=not args.no_scroll
            )
            print(f"Screenshot: {screenshot}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
