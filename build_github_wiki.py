#!/usr/bin/env python3
"""
build_github_wiki.py — Generiert GitHub-Wiki-Seiten aus Wolkenfrei.md.
Splittet das Hauptdokument an H2-Grenzen, konvertiert §-Querverweise
in Wiki-Links, erzeugt Home.md und _Sidebar.md.

Nutzung:
  python3 build_github_wiki.py              # Generiert in wiki/
  python3 build_github_wiki.py --push       # Generiert und pusht ins Wiki-Repo
"""

import re
import os
import sys
import subprocess
import unicodedata

DOCUMENT = "Wolkenfrei.md"
WIKI_DIR = "wiki"
WIKI_REPO = "https://github.com/bdegenkolbe/Wolkenklar.wiki.git"

UMLAUT_MAP = str.maketrans({
    'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
    'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
    'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a',
})


def slugify(text):
    """Convert heading text to ASCII-only slug for filenames."""
    text = text.strip()
    text = re.sub(r'[{#][^}]*[}]', '', text)
    text = text.translate(UMLAUT_MAP)
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def github_anchor(text):
    """Generate anchor matching GitHub's heading-to-anchor behavior."""
    text = text.lower().strip()
    text = re.sub(r'[{#][^}]*[}]', '', text)
    # GitHub uses NFKD normalization, strips combining chars, then removes non-alphanum
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
    header_lines = []

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

    if current_title is not None:
        chapters.append((current_title, '\n'.join(current_lines)))

    return header_lines, chapters


def chapter_filename(title):
    """Generate GitHub Wiki filename for a chapter."""
    m = re.match(r'##\s+(\d+)\.\s+(.+?)(?:\s*\{|$)', title)
    if m:
        num = int(m.group(1))
        short_title = m.group(2).strip()
        short = re.split(r'[:\u2014\u2013]', short_title)[0].strip()
        return f"{num:02d}-{slugify(short)}"

    title_clean = title.replace('## ', '').split('{')[0].strip()
    lower = title_clean.lower()
    if 'inhaltsverzeichnis' in lower:
        return None
    if 'rechtliche analyse' in lower and '·' in lower:
        return None
    if 'fazit' in lower:
        return "Fazit"
    if 'quellenverzeichnis' in lower:
        return "18-Quellenverzeichnis"

    return slugify(title_clean)


def build_section_map(chapters, filenames):
    """Build mapping from §X.Y references to wiki page links."""
    section_map = {}

    for (title, content), filename in zip(chapters, filenames):
        if filename is None:
            continue

        for line in content.split('\n'):
            m = re.match(r'^(#{2,4})\s+(\d+\.[\d.]+)\s+(.+)', line)
            if m:
                section_num = m.group(2).rstrip('.')
                heading_text = m.group(3).split('{')[0].strip()
                anchor = github_anchor(f"{section_num} {heading_text}")
                section_map[section_num] = (filename, f"#{anchor}")

            m2 = re.match(r'^##\s+(\d+)\.\s+(.+?)(?:\s*\{|$)', line)
            if m2:
                chapter_num = m2.group(1)
                section_map[chapter_num] = (filename, "")

    return section_map


def convert_cross_references(text, section_map, current_file):
    """Convert §X.Y textual references to GitHub Wiki links."""
    def replace_ref(match):
        full_match = match.group(0)
        section_num = match.group(1)

        for ref in [section_num, section_num.split('.')[0]]:
            if ref in section_map:
                target_file, anchor = section_map[ref]
                if target_file == current_file:
                    if anchor:
                        return f"[{full_match}]({anchor})"
                    return full_match
                else:
                    # GitHub Wiki links: use page name without .md
                    return f"[{full_match}]({target_file}{anchor})"

        return full_match

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
    """Remove {#anchor-id} from headings."""
    return re.sub(r'\s*\{#[^}]+\}', '', text)


def generate_home(header_lines, chapters, filenames):
    """Generate Home.md (wiki start page)."""
    lines = [
        "# US CLOUD Act & Deutsche Datensouveränität",
        "",
        "**Rechtliche Analyse · Anbieterbewertung · Globale Strategien · DSGVO-Handlungsempfehlungen**",
        "",
    ]

    for hl in header_lines:
        if hl.startswith('**') and ('Version' in hl or 'Autor' in hl or 'Organisation' in hl):
            lines.append(hl)

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Inhaltsverzeichnis")
    lines.append("")

    for (title, _content), filename in zip(chapters, filenames):
        if filename is None:
            continue
        title_clean = re.sub(r'^##\s+', '', title)
        title_clean = re.sub(r'\s*\{#[^}]+\}', '', title_clean)
        if 'Inhaltsverzeichnis' in title_clean:
            continue
        lines.append(f"1. [{title_clean}]({filename})")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Dieses Wiki wird automatisch aus dem Hauptdokument [Wolkenfrei.md](https://github.com/bdegenkolbe/Wolkenklar/blob/main/Wolkenfrei.md) generiert.*")

    return '\n'.join(lines)


def generate_sidebar(chapters, filenames):
    """Generate _Sidebar.md (wiki navigation)."""
    lines = [
        "**[🏠 Start](Home)**",
        "",
    ]

    for (title, _content), filename in zip(chapters, filenames):
        if filename is None:
            continue
        title_clean = re.sub(r'^##\s+', '', title)
        title_clean = re.sub(r'\s*\{#[^}]+\}', '', title_clean)
        if 'Inhaltsverzeichnis' in title_clean:
            continue

        # Short nav title
        m = re.match(r'(\d+)\.\s+(.+?)(?:\s*[:—–]|$)', title_clean)
        if m:
            short = f"{m.group(1)}. {m.group(2).strip()}"
        elif 'Fazit' in title_clean:
            short = "Fazit"
        else:
            short = title_clean

        lines.append(f"- [{short}]({filename})")

    return '\n'.join(lines)


def main():
    push = '--push' in sys.argv

    # Read source document
    with open(DOCUMENT, 'r', encoding='utf-8') as f:
        text = f.read()

    # Parse into chapters
    header_lines, chapters = parse_chapters(text)

    # Generate filenames (without .md for GitHub Wiki)
    filenames = []
    for title, _content in chapters:
        fn = chapter_filename(title)
        filenames.append(fn)

    # Build section map for cross-references
    section_map = build_section_map(chapters, filenames)

    # Prepare output directory
    if push:
        # Clone or update wiki repo
        if os.path.exists(WIKI_DIR) and os.path.exists(os.path.join(WIKI_DIR, '.git')):
            subprocess.run(['git', '-C', WIKI_DIR, 'pull'], check=True)
        else:
            if os.path.exists(WIKI_DIR):
                import shutil
                shutil.rmtree(WIKI_DIR)
            subprocess.run(['git', 'clone', WIKI_REPO, WIKI_DIR], check=True)
    else:
        os.makedirs(WIKI_DIR, exist_ok=True)

    # Clean old .md files (except .git)
    for fn in os.listdir(WIKI_DIR):
        if fn.endswith('.md'):
            os.remove(os.path.join(WIKI_DIR, fn))

    # Write chapter files
    written = 0
    for (title, content), filename in zip(chapters, filenames):
        if filename is None:
            continue

        processed = content
        processed = clean_anchors(processed)
        processed = shift_headings(processed)
        processed = convert_cross_references(processed, section_map, filename)

        filepath = os.path.join(WIKI_DIR, f"{filename}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(processed)
        written += 1

    # Write Home.md
    home = generate_home(header_lines, chapters, filenames)
    with open(os.path.join(WIKI_DIR, 'Home.md'), 'w', encoding='utf-8') as f:
        f.write(home)

    # Write _Sidebar.md
    sidebar = generate_sidebar(chapters, filenames)
    with open(os.path.join(WIKI_DIR, '_Sidebar.md'), 'w', encoding='utf-8') as f:
        f.write(sidebar)

    print(f"GitHub Wiki generiert: {written} Seiten + Home.md + _Sidebar.md in {WIKI_DIR}/")
    print(f"Sektions-Map: {len(section_map)} §-Referenzen gemappt")

    if push:
        print("\nPushe ins Wiki-Repo...")
        subprocess.run(['git', '-C', WIKI_DIR, 'add', '-A'], check=True)
        subprocess.run(['git', '-C', WIKI_DIR, 'commit', '-m',
                        'Wiki aktualisiert aus Wolkenfrei.md'], check=True)
        subprocess.run(['git', '-C', WIKI_DIR, 'push'], check=True)
        print("✅ Wiki gepusht!")
    else:
        print(f"\nZum Pushen: python3 build_github_wiki.py --push")


if __name__ == "__main__":
    main()
