#!/usr/bin/env python3
"""
Generate .app bundles for notebooks in ~/Desktop/Notebooks/

Each app is a minimal macOS bundle that opens the notebook in the viewer.
Double-clicking the app opens the notebook.

Usage:
    ./sync-desktop.py              # Sync all notebooks
    ./sync-desktop.py --clean      # Remove apps for deleted notebooks
    ./sync-desktop.py --dry-run    # Show what would be done
"""
import argparse
import os
import plistlib
import re
import shutil
import stat
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent


def instance_name() -> str:
    """Derive instance name from repo directory for multi-worktree isolation."""
    return repo_root().name


def notebooks_dir() -> Path:
    return repo_root() / "notebooks" / "src"


def desktop_notebooks_dir() -> Path:
    return Path.home() / "Desktop" / "Notebooks"


def prettify_name(filename: str) -> str:
    """Convert kebab-case filename to Title Case."""
    name = filename.replace("-", " ").replace("_", " ")
    return name.title()


def app_name_for_notebook(md_path: Path) -> str:
    """Get display name for a notebook (from filename, not frontmatter)."""
    return prettify_name(md_path.stem)


def create_app_bundle(notebook_path: Path, app_dir: Path, viewer_py: Path, instance: str) -> None:
    """Create a minimal .app bundle that opens the notebook."""
    contents = app_dir / "Contents"
    macos = contents / "MacOS"
    macos.mkdir(parents=True, exist_ok=True)

    # Info.plist - minimal app metadata
    info_plist = {
        "CFBundleName": app_dir.stem,
        "CFBundleDisplayName": app_dir.stem,
        "CFBundleIdentifier": f"build.conductor.notebook.{instance}.{notebook_path.stem}",
        "CFBundleVersion": "1.0",
        "CFBundlePackageType": "APPL",
        "CFBundleExecutable": "open-notebook",
        "LSMinimumSystemVersion": "10.13",
        "NSHighResolutionCapable": True,
        # Hide from Dock while running
        "LSUIElement": True,
    }
    plist_path = contents / "Info.plist"
    plist_path.write_bytes(plistlib.dumps(info_plist))

    # Executable script - uses --instance to avoid conflicts with other worktrees
    # Include common paths for Homebrew Python (viewer.py requires Python 3.10+)
    script = f"""#!/bin/bash
# Open notebook: {notebook_path.name}
# Instance: {instance} (for multi-worktree isolation)

# Finder launches with minimal PATH - add common tool locations
# Python 3.10+ for viewer.py, cargo for Tauri build, node for Observable
export PATH="$HOME/.cargo/bin:/opt/homebrew/bin:/opt/homebrew/opt/python@3.12/libexec/bin:/opt/homebrew/opt/python@3.11/libexec/bin:/opt/homebrew/opt/python@3.10/libexec/bin:/usr/local/bin:$PATH"

VIEWER="{viewer_py}"
INSTANCE="{instance}"
NOTEBOOK="{notebook_path}"

# Start viewer if needed (fast if already running)
"$VIEWER" --instance "$INSTANCE" start >/dev/null 2>&1

# Open the notebook and wait for it to be ready
"$VIEWER" --instance "$INSTANCE" open "$NOTEBOOK" --wait >/dev/null 2>&1

# Show the window
"$VIEWER" --instance "$INSTANCE" show >/dev/null 2>&1
"""
    exec_path = macos / "open-notebook"
    exec_path.write_text(script)
    exec_path.chmod(exec_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def list_notebooks() -> list[Path]:
    """List all notebooks in notebooks/src/."""
    ndir = notebooks_dir()
    if not ndir.exists():
        return []
    return sorted(ndir.glob("*.md"))


def sync(dry_run: bool = False, clean: bool = False) -> None:
    viewer_py = repo_root() / "viewer.py"
    if not viewer_py.exists():
        print(f"Error: viewer.py not found at {viewer_py}")
        return

    instance = instance_name()
    desktop_dir = desktop_notebooks_dir()
    notebooks = list_notebooks()

    if not notebooks:
        print("No notebooks found in notebooks/src/")
        return

    # Track expected apps
    expected_apps: set[str] = set()

    print(f"Syncing {len(notebooks)} notebooks to {desktop_dir}/")
    print(f"Instance: {instance} (for multi-worktree isolation)\n")

    if not dry_run:
        desktop_dir.mkdir(parents=True, exist_ok=True)

    for nb in notebooks:
        name = app_name_for_notebook(nb)
        app_name = f"{name}.app"
        app_path = desktop_dir / app_name
        expected_apps.add(app_name)

        if app_path.exists():
            action = "update"
        else:
            action = "create"

        print(f"  {action}: {app_name} → {nb.name}")

        if not dry_run:
            if app_path.exists():
                shutil.rmtree(app_path)
            create_app_bundle(nb, app_path, viewer_py, instance)

    # Clean up orphaned apps
    if clean and desktop_dir.exists():
        for item in desktop_dir.iterdir():
            if item.suffix == ".app" and item.name not in expected_apps:
                print(f"  remove: {item.name} (notebook deleted)")
                if not dry_run:
                    shutil.rmtree(item)

    print("\nDone." if not dry_run else "\nDry run complete (no changes made).")


def main():
    parser = argparse.ArgumentParser(description="Sync notebooks to Desktop as .app launchers")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--clean", action="store_true", help="Remove apps for deleted notebooks")
    args = parser.parse_args()

    sync(dry_run=args.dry_run, clean=args.clean)


if __name__ == "__main__":
    main()
