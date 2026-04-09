#!/usr/bin/env python3
"""
build_wiki.py — Generiert MkDocs-Wiki-Seiten aus Wolkenfrei.md (Single Source of Truth).
Splittet das Hauptdokument an H2-Grenzen, konvertiert §-Querverweise in Links,
verschiebt Heading-Levels und erzeugt index.md.
"""

import re
import os
import shutil

DOCUMENT = "Wolkenfrei.md"
DOCS_DIR = "docs"

# --- Chapter mapping: H2 title pattern → (filename, nav_title) ---
# Built dynamically from the document, but we define slug rules here.

UMLAUT_MAP = str.maketrans({
    'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
    'Ä': 'ae', 'Ö': 'oe', 'Ü': 'ue',
    'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a',
})


def slugify(text):
    """Convert heading text to ASCII-only slug for filenames."""
    text = text.lower().strip()
    text = re.sub(r'[{#][^}]*[}]', '', text)    # Remove {#anchor-id}
    text = text.translate(UMLAUT_MAP)            # Umlauts → ASCII
    text = re.sub(r'[^\w\s-]', '', text)         # Remove special chars
    text = re.sub(r'[\s]+', '-', text)           # Spaces → hyphens
    text = re.sub(r'-+', '-', text)              # Collapse hyphens
    return text.strip('-')


def mkdocs_anchor(text):
    """Generate anchor matching MkDocs/Python-Markdown toc slugify behavior."""
    import unicodedata
    text = text.lower().strip()
    text = re.sub(r'[{#][^}]*[}]', '', text)    # Remove {#anchor-id}
    # MkDocs uses NFKD normalization + strip combining chars (ä→a, ö→o, ü→u)
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def parse_chapters(text):
    """Split document at H2 boundaries into chapters."""
    lines = text.split('\n')
    chapters = []
    current_lines = []
    current_title = None
    header_lines = []  # Lines before first H2 (document header)

    for line in lines:
        if line.startswith('## ') and not line.startswith('### '):
            if current_title is not None:
                chapters.append((current_title, '\n'.join(current_lines)))
            elif current_lines:
                header_lines = current_lines[:]
            current_title = line
            current_lines = [line]
        else:
            current_lines.append(line)

    # Last chapter
    if current_title is not None:
        chapters.append((current_title, '\n'.join(current_lines)))

    return header_lines, chapters


def chapter_filename(title, index):
    """Generate filename for a chapter based on its title."""
    # Extract chapter number if present
    m = re.match(r'##\s+(\d+)\.\s+(.+?)(?:\s*\{|$)', title)
    if m:
        num = int(m.group(1))
        short_title = m.group(2).strip()
        # Use just the first meaningful part of the title (before colon or dash)
        short = re.split(r'[:\—–]', short_title)[0].strip()
        return f"{num:02d}-{slugify(short)}.md"

    # Special cases
    title_clean = title.replace('## ', '').split('{')[0].strip().lower()
    if 'inhaltsverzeichnis' in title_clean:
        return None  # Skip TOC — we generate our own index
    if 'rechtliche analyse' in title_clean:
        return None  # Skip subtitle line
    if 'fazit' in title_clean:
        return "fazit.md"
    if 'quellenverzeichnis' in title_clean:
        return "18-quellenverzeichnis.md"

    return f"misc-{slugify(title_clean)}.md"


def build_section_map(chapters, filenames):
    """Build mapping from §X.Y references to file#anchor URLs."""
    section_map = {}

    for (title, content), filename in zip(chapters, filenames):
        if filename is None:
            continue

        # Find all ### X.Y and #### X.Y.Z headings in this chapter
        for line in content.split('\n'):
            # Match ### 5.3 or #### 1.2.1 style headings
            m = re.match(r'^(#{2,4})\s+(\d+\.[\d.]+)\s+(.+)', line)
            if m:
                section_num = m.group(2).rstrip('.')
                heading_text = m.group(3).split('{')[0].strip()
                # After heading level shift: ### → ## means slug is based on shifted heading
                slug = mkdocs_anchor(f"{section_num} {heading_text}")
                section_map[section_num] = (filename, f"#{slug}")

            # Also match ## X. Chapter headings (top-level sections)
            m2 = re.match(r'^##\s+(\d+)\.\s+(.+?)(?:\s*\{|$)', line)
            if m2:
                chapter_num = m2.group(1)
                section_map[chapter_num] = (filename, "")

    return section_map


def convert_cross_references(text, section_map, current_file):
    """Convert §X.Y textual references to markdown links."""
    def replace_ref(match):
        full_match = match.group(0)
        section_num = match.group(1)

        # Try exact match, then parent section
        for ref in [section_num, section_num.split('.')[0]]:
            if ref in section_map:
                target_file, anchor = section_map[ref]
                if target_file == current_file:
                    # Same page — anchor-only link
                    if anchor:
                        return f"[{full_match}]({anchor})"
                    return full_match
                else:
                    return f"[{full_match}]({target_file}{anchor})"

        return full_match  # No mapping found — leave as-is

    # Match §X.Y patterns but not inside markdown links already
    return re.sub(r'(?<!\[)§\s*(\d+(?:\.\d+)*)', replace_ref, text)


def shift_headings(text):
    """Shift heading levels: H2→H1, H3→H2, H4→H3."""
    lines = text.split('\n')
    result = []
    for line in lines:
        if line.startswith('#### '):
            result.append('### ' + line[5:])
        elif line.startswith('### '):
            result.append('## ' + line[4:])
        elif line.startswith('## '):
            result.append('# ' + line[3:])
        else:
            result.append(line)
    return '\n'.join(result)


def clean_anchors(text):
    """Remove {#anchor-id} from headings — MkDocs generates its own."""
    return re.sub(r'\s*\{#[^}]+\}', '', text)


def generate_index(header_lines, chapters, filenames):
    """Generate docs/index.md with title and linked table of contents."""
    lines = [
        "# US CLOUD Act & Deutsche Datensouveranitat",
        "",
        "## Rechtliche Analyse · Anbieterbewertung · Globale Strategien · DSGVO-Handlungsempfehlungen",
        "",
    ]

    # Extract metadata from header
    for hl in header_lines:
        if hl.startswith('**') and ('Version' in hl or 'Autor' in hl or 'Organisation' in hl):
            lines.append(hl)
            lines.append("")

    lines.append("")
    lines.append("## Inhaltsverzeichnis")
    lines.append("")

    for (title, _content), filename in zip(chapters, filenames):
        if filename is None:
            continue
        # Clean title
        title_clean = re.sub(r'^##\s+', '', title)
        title_clean = re.sub(r'\s*\{#[^}]+\}', '', title_clean)

        if 'Inhaltsverzeichnis' in title_clean:
            continue

        lines.append(f"- [{title_clean}]({filename})")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Dieses Wiki wird automatisch aus dem Hauptdokument Wolkenfrei.md generiert.*")

    return '\n'.join(lines)


def generate_nav(chapters, filenames):
    """Generate nav section content for mkdocs.yml."""
    nav_items = ['  - Start: index.md']

    for (title, _content), filename in zip(chapters, filenames):
        if filename is None:
            continue
        title_clean = re.sub(r'^##\s+', '', title)
        title_clean = re.sub(r'\s*\{#[^}]+\}', '', title_clean).strip()

        if 'Inhaltsverzeichnis' in title_clean:
            continue
        if 'Rechtliche Analyse' in title_clean and '·' in title_clean:
            continue

        nav_items.append(f'  - "{title_clean}": {filename}')

    return '\n'.join(nav_items)


def main():
    # Read source document
    with open(DOCUMENT, 'r', encoding='utf-8') as f:
        text = f.read()

    # Parse into chapters
    header_lines, chapters = parse_chapters(text)

    # Generate filenames
    filenames = []
    for i, (title, _content) in enumerate(chapters):
        fn = chapter_filename(title, i)
        filenames.append(fn)

    # Build section map for cross-references
    section_map = build_section_map(chapters, filenames)

    # Create docs directory
    # Preserve stylesheets subdirectory if it exists
    stylesheets_exists = os.path.exists(os.path.join(DOCS_DIR, "stylesheets"))
    stylesheets_content = None
    if stylesheets_exists:
        stylesheets_content = {}
        ss_dir = os.path.join(DOCS_DIR, "stylesheets")
        for fn in os.listdir(ss_dir):
            with open(os.path.join(ss_dir, fn), 'r') as f:
                stylesheets_content[fn] = f.read()

    # Clean and recreate docs dir (except stylesheets)
    if os.path.exists(DOCS_DIR):
        for fn in os.listdir(DOCS_DIR):
            path = os.path.join(DOCS_DIR, fn)
            if fn == 'stylesheets':
                continue
            if os.path.isfile(path) and path.endswith('.md'):
                os.remove(path)

    os.makedirs(DOCS_DIR, exist_ok=True)

    # Write chapter files
    written = 0
    for (title, content), filename in zip(chapters, filenames):
        if filename is None:
            continue

        # Process content
        processed = content
        processed = clean_anchors(processed)
        processed = shift_headings(processed)
        processed = convert_cross_references(processed, section_map, filename)

        filepath = os.path.join(DOCS_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(processed)
        written += 1

    # Write index.md
    index_content = generate_index(header_lines, chapters, filenames)
    with open(os.path.join(DOCS_DIR, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(index_content)

    # Print nav for mkdocs.yml reference
    nav = generate_nav(chapters, filenames)

    print(f"Wiki generiert: {written} Seiten in {DOCS_DIR}/")
    print(f"Sektions-Map: {len(section_map)} §-Referenzen gemappt")
    print(f"\nNav-Konfiguration für mkdocs.yml:")
    print(f"nav:\n{nav}")


if __name__ == "__main__":
    main()
