#!/usr/bin/env python3
"""Fetch Observable Plot examples directly from Observable's embedded JSON."""

import re
import json
import time
import requests
from pathlib import Path
from html import unescape

GALLERY_FILE = Path("/Users/joshlevine/Downloads/019ba6a8-5da4-766a-861b-861c04ffbce8/observablehq.com_@observablehq_plot-gallery.md")
OUTPUT_DIR = Path("/Users/joshlevine/Downloads/observable-plot-docs/examples")


def extract_urls(gallery_path: Path) -> list[str]:
    """Extract all Observable notebook URLs from the gallery file."""
    content = gallery_path.read_text()
    urls = re.findall(r'https://observablehq\.com/@[^)"]+', content)
    urls = [u.strip() for u in urls if not u.endswith('@observablehq') and not u.endswith('@fil')]
    return sorted(set(urls))


def fetch_notebook(url: str) -> dict | None:
    """Fetch notebook data from Observable's embedded __NEXT_DATA__."""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code != 200:
            print(f"  HTTP {response.status_code}")
            return None

        # Extract __NEXT_DATA__ JSON
        match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.+?)</script>', response.text, re.DOTALL)
        if not match:
            print("  No __NEXT_DATA__ found")
            return None

        data = json.loads(match.group(1))
        return data.get('props', {}).get('pageProps', {}).get('initialNotebook')

    except Exception as e:
        print(f"  Exception: {e}")
        return None


def clean_markdown_cell(value: str) -> str:
    """Clean HTML from markdown cell content and extract useful parts."""
    # First, remove the breadcrumb div entirely
    value = re.sub(r'<div[^>]*>.*?</div>', '', value, flags=re.DOTALL)

    # Remove remaining HTML tags but keep content
    value = re.sub(r'<[^>]+>', ' ', value)
    value = unescape(value)
    value = re.sub(r'\s+', ' ', value)  # Normalize whitespace
    return value.strip()


def format_notebook(notebook: dict, url: str) -> str:
    """Format notebook as clean markdown."""
    lines = []

    # Get title (remove "Plot:" prefix if present)
    title = notebook.get('title', '')
    if title.startswith('Plot:'):
        title = title[5:].strip()
    if not title:
        title = url.split('/')[-1].replace('-', ' ').title()

    # Frontmatter
    lines.append('---')
    lines.append(f'url: "{url}"')
    lines.append(f'title: "{title}"')
    lines.append('---')
    lines.append('')

    # Title
    lines.append(f'# {title}')
    lines.append('')

    # Process cells
    nodes = notebook.get('nodes', [])
    description_added = False

    for node in nodes:
        value = node.get('value', '')
        mode = node.get('mode', '')

        if not value:
            continue

        if mode == 'md':
            # Markdown cell
            cleaned = clean_markdown_cell(value)

            # Skip navigation breadcrumbs and boilerplate
            if 'Observable Plot ›' in cleaned:
                continue
            if cleaned.startswith('Plot:') and 'Gallery' in cleaned:
                continue
            if cleaned.startswith('---') and len(cleaned) < 10:
                continue
            if cleaned == '_data_':
                continue

            # Handle headings
            if cleaned.startswith('# '):
                header_text = cleaned[2:].strip()
                title_lower = title.lower()
                header_lower = header_text.lower()

                # If header starts with title, extract description after it
                if header_lower.startswith(title_lower):
                    description = header_text[len(title):].strip()
                    if description:
                        lines.append(description)
                        lines.append('')
                    continue

                # Check for "Plot:" prefix variant
                plot_title = 'plot: ' + title_lower
                if header_lower.startswith(plot_title):
                    description = header_text[len('Plot: ' + title):].strip()
                    if description:
                        lines.append(description)
                        lines.append('')
                    continue

                # Otherwise add as section header
                lines.append(cleaned)
                lines.append('')
            else:
                lines.append(cleaned)
                lines.append('')

        elif mode == 'js':
            # JavaScript cell
            lines.append('```js')
            lines.append(value.strip())
            lines.append('```')
            lines.append('')

    return '\n'.join(lines)


def url_to_filename(url: str) -> str:
    """Convert URL to clean filename."""
    match = re.search(r'@[^/]+/([^/]+)', url)
    if match:
        name = match.group(1)
        name = re.sub(r'/\d+$', '', name)
        return name + '.md'
    return 'unknown.md'


def main(test_mode: bool = False, test_count: int = 5):
    """Main entry point."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    urls = extract_urls(GALLERY_FILE)
    print(f"Found {len(urls)} unique notebook URLs")

    if test_mode:
        urls = urls[:test_count]
        print(f"Test mode: processing only {test_count} URLs")

    success, failed = 0, 0

    for i, url in enumerate(urls):
        filename = url_to_filename(url)
        output_path = OUTPUT_DIR / filename

        if output_path.exists() and output_path.stat().st_size > 100:
            print(f"[{i+1}/{len(urls)}] Skipping (exists): {filename}")
            success += 1
            continue

        print(f"[{i+1}/{len(urls)}] Fetching: {url}")
        notebook = fetch_notebook(url)

        if notebook:
            output = format_notebook(notebook, url)
            cell_count = len([n for n in notebook.get('nodes', []) if n.get('value')])
            output_path.write_text(output)
            print(f"  -> Saved: {filename} ({len(output)} bytes, {cell_count} cells)")
            success += 1
        else:
            print(f"  -> Failed to fetch")
            failed += 1

        # Rate limit to be nice to Observable
        if i < len(urls) - 1:
            time.sleep(0.5)

    print(f"\nDone! Success: {success}, Failed: {failed}")


if __name__ == '__main__':
    import sys
    test_mode = '--test' in sys.argv
    main(test_mode=test_mode)
