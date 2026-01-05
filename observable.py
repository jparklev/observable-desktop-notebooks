#!/usr/bin/env python3
"""
Observable Desktop CLI - Integration toolkit for Claude Code

Essential commands for silent notebook development:
- new, open, list, add, edit, delete, get: Notebook/cell management
- capture-cell: Silent cell verification (primary visual feedback)
"""

import argparse
import json
import subprocess
import sys
import tempfile
import time
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import html


@dataclass
class Cell:
    """Represents a notebook cell"""
    id: Optional[str]
    type: str
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
            attrs.append(f'type="{cell.type}"')
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
        """Add a new cell"""
        cell = Cell(
            id=cell_id or f"cell-{len(self.cells) + 1}",
            type=cell_type,
            content=content,
            pinned=pinned,
            index=len(self.cells)
        )

        if index is not None and 0 <= index <= len(self.cells):
            self.cells.insert(index, cell)
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

    swift_file.write_text(swift_code)
    if not binary_file.exists():
        subprocess.run(['swiftc', str(swift_file), '-o', str(binary_file)],
                      capture_output=True)

    result = subprocess.run([str(binary_file)], capture_output=True, text=True)
    if result.stdout.strip():
        try:
            return int(result.stdout.strip())
        except ValueError:
            pass
    return None


def reload_notebook(file_path: str, background: bool = True):
    """Close and reopen notebook in Observable Desktop (background by default)"""
    full_path = str(Path(file_path).resolve())

    # Remember current frontmost app
    prev_app = None
    if background:
        result = subprocess.run([
            'osascript', '-e',
            'tell application "System Events" to get name of first process whose frontmost is true'
        ], capture_output=True, text=True)
        prev_app = result.stdout.strip()

    # Close all Observable windows using Accessibility
    script = '''
    tell application "System Events"
        if exists process "Observable Desktop" then
            tell process "Observable Desktop"
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
    subprocess.run(['open', '-g', '-a', 'Observable Desktop', full_path], capture_output=True)

    # Restore focus if needed
    if background and prev_app and prev_app != "Observable Desktop":
        check = subprocess.run([
            'osascript', '-e',
            'tell application "System Events" to get name of first process whose frontmost is true'
        ], capture_output=True, text=True)

        if check.stdout.strip() == "Observable Desktop":
            subprocess.run([
                'osascript', '-e',
                f'tell application "{prev_app}" to activate'
            ], capture_output=True)


def capture_cell(file_path: str, cell_index: int, output_path: Optional[str] = None,
                 wait: float = 2.0) -> str:
    """Capture a specific cell by temporarily moving it to the top (completely silent)

    1. Reorders cells to put target at top
    2. Reloads notebook in background
    3. Captures top section
    4. Restores original order
    5. Reloads again

    Returns path to screenshot.
    """
    nb = Notebook(file_path)

    if cell_index < 0 or cell_index >= len(nb.cells):
        raise ValueError(f"Cell index {cell_index} out of range (0-{len(nb.cells)-1})")

    if output_path is None:
        output_path = tempfile.mktemp(suffix='.png')

    # Save original order
    original_cells = nb.cells.copy()

    # Move target cell to top
    target_cell = nb.cells.pop(cell_index)
    nb.cells.insert(0, target_cell)

    # Re-index
    for i, c in enumerate(nb.cells):
        c.index = i

    # Save and reload
    nb.save()
    time.sleep(0.2)
    reload_notebook(file_path, background=True)
    time.sleep(wait)

    # Capture (silent)
    window_id = get_observable_window_id()
    if window_id:
        subprocess.run(['screencapture', '-l', str(window_id), '-o', '-x', output_path],
                      capture_output=True)

    # Restore original order
    nb.cells = original_cells
    for i, c in enumerate(nb.cells):
        c.index = i
    nb.save()
    time.sleep(0.2)
    reload_notebook(file_path, background=True)

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Observable Desktop CLI for Claude Code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s new my-notebook.html --title "Analysis"
  %(prog)s list notebook.html
  %(prog)s add notebook.html "Plot.plot({marks: [Plot.dot([1,2,3])]})"
  %(prog)s edit notebook.html 0 "// Updated code"
  %(prog)s capture-cell notebook.html 3
  %(prog)s open notebook.html
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
                       help='Cell type: ojs (default), md, sql')
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

    # capture-cell
    cc_p = subparsers.add_parser('capture-cell', help='Capture cell silently (moves to top, captures, restores)')
    cc_p.add_argument('path', help='Notebook path')
    cc_p.add_argument('cell', type=int, help='Cell index to capture')
    cc_p.add_argument('--output', '-o', help='Output path (default: temp)')
    cc_p.add_argument('--wait', '-w', type=float, default=2.0,
                     help='Seconds to wait for render (default: 2.0)')

    args = parser.parse_args()

    # Type shorthand expansion
    TYPE_MAP = {
        'ojs': 'application/vnd.observable.javascript',
        'md': 'text/markdown',
        'sql': 'application/sql',
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

        elif args.command == 'capture-cell':
            screenshot = capture_cell(
                args.path,
                args.cell,
                output_path=args.output,
                wait=args.wait
            )
            print(screenshot)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
