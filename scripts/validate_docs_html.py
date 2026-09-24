from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / 'docs'
HTML_FILES = sorted(DOCS_DIR.glob('*.html'))


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: List[Tuple[str, int]] = []
        self.scripts: List[Tuple[str, int]] = []
        self.images: List[Tuple[str, int]] = []
        self.has_main = False
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == 'a' and attributes.get('href'):
            self.links.append((attributes['href'], self.getpos()[0]))
        if tag == 'script' and attributes.get('src'):
            self.scripts.append((attributes['src'], self.getpos()[0]))
        if tag == 'img' and attributes.get('src'):
            self.images.append((attributes['src'], self.getpos()[0]))
        if tag == 'main':
            self.has_main = True
        if tag == 'title':
            self.has_title = True


def is_local_reference(target: str) -> bool:
    if target.startswith(('#', 'mailto:', 'tel:')):
        return False
    parsed = urlparse(target)
    return not parsed.scheme and not parsed.netloc


def validate_reference(source: Path, target: str) -> str | None:
    clean_target = target.split('#', 1)[0]
    if not clean_target:
        return None
    destination = (source.parent / clean_target).resolve()
    try:
        destination.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return f'{source.relative_to(REPO_ROOT)} references a path outside the repository: {target}'
    if not destination.exists():
        return f'{source.relative_to(REPO_ROOT)} references a missing local file: {target}'
    return None


def main() -> int:
    errors: List[str] = []
    if not HTML_FILES:
        errors.append('No HTML files found in docs/.')

    for html_file in HTML_FILES:
        parser = LinkParser()
        parser.feed(html_file.read_text(encoding='utf-8'))
        if not parser.has_title:
            errors.append(f'{html_file.relative_to(REPO_ROOT)} is missing a <title> element.')
        if not parser.has_main:
            errors.append(f'{html_file.relative_to(REPO_ROOT)} is missing a <main> element.')
        for ref, _ in [*parser.links, *parser.scripts, *parser.images]:
            if is_local_reference(ref):
                error = validate_reference(html_file, ref)
                if error:
                    errors.append(error)

    if errors:
        print('Validation failed:')
        for error in errors:
            print(f'- {error}')
        return 1

    print(f'Validated {len(HTML_FILES)} HTML files in {DOCS_DIR.relative_to(REPO_ROOT)}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
