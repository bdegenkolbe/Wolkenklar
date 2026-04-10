#!/usr/bin/env python3
"""
validate.py — Automatisierte Strukturprüfung für das Hauptdokument.
Prüft: Gliederung, Nummerierung, Querverweise, Quellen, Versionskonsistenz, Formatierung.
"""

import re
import sys

DOCUMENT = "Wolkenfrei.md"


def load_document():
    with open(DOCUMENT, "r", encoding="utf-8") as f:
        return f.read()


def extract_lines(text):
    return text.split("\n")


# ─── 2.1.1 Gliederung ───

def check_toc_vs_headings(text, lines):
    """Prüft, ob ToC-Einträge und Kapitelüberschriften übereinstimmen."""
    errors = []

    # Extract ToC entries (numbered 1-18 + Fazit)
    toc_pattern = re.compile(r"^\d+\.\s+\[(.+?)\]\(#(.+?)\)\s*$")
    fazit_toc_pattern = re.compile(r"^\[Fazit\]\(#fazit\)\s*$")
    toc_entries = []
    in_toc = False

    for i, line in enumerate(lines):
        if line.strip() == "## Inhaltsverzeichnis":
            in_toc = True
            continue
        if in_toc:
            if line.strip().startswith("---"):
                break
            m = toc_pattern.match(line.strip())
            if m:
                toc_entries.append({
                    "title": m.group(1),
                    "anchor": m.group(2),
                    "line": i + 1
                })
            m2 = fazit_toc_pattern.match(line.strip())
            if m2:
                toc_entries.append({
                    "title": "Fazit",
                    "anchor": "fazit",
                    "line": i + 1
                })

    # Extract H2 headings with anchor IDs
    h2_pattern = re.compile(r"^## (.+?)\s*\{#(.+?)\}\s*$")
    h2_headings = []

    for i, line in enumerate(lines):
        if line.strip() == "## Inhaltsverzeichnis":
            continue
        m = h2_pattern.match(line.strip())
        if m:
            h2_headings.append({
                "title": m.group(1).strip(),
                "anchor": m.group(2),
                "line": i + 1
            })

    # Compare ToC count to headings count
    if len(toc_entries) != len(h2_headings):
        errors.append(
            f"ToC hat {len(toc_entries)} Einträge, aber {len(h2_headings)} H2-Überschriften im Dokument."
        )

    # Compare anchors
    toc_anchors = [e["anchor"] for e in toc_entries]
    h2_anchors = [h["anchor"] for h in h2_headings]

    for anchor in toc_anchors:
        if anchor not in h2_anchors:
            errors.append(f"ToC-Anker '#{anchor}' hat keine passende H2-Überschrift.")

    for anchor in h2_anchors:
        if anchor not in toc_anchors:
            errors.append(f"H2-Überschrift mit Anker '#{anchor}' fehlt im Inhaltsverzeichnis.")

    return errors, len(toc_entries), len(h2_headings)


# ─── 2.1.2 Nummerierung ───

def check_chapter_numbering(lines):
    """Prüft lückenlose Kapitelnummerierung."""
    errors = []

    # H2 chapter numbers
    h2_nums = []
    h2_pattern = re.compile(r"^## (\d+)\.")
    for i, line in enumerate(lines):
        m = h2_pattern.match(line.strip())
        if m:
            h2_nums.append((int(m.group(1)), i + 1))

    for idx in range(len(h2_nums)):
        expected = idx + 1
        actual, lineno = h2_nums[idx]
        if actual != expected:
            errors.append(
                f"Kapitelnummerierung: Erwartet {expected}, gefunden {actual} (Zeile {lineno})."
            )

    # H3 subsection numbering within each chapter
    h3_pattern = re.compile(r"^### (\d+)\.(\d+)\s")
    current_chapter = 0
    expected_sub = 1

    for i, line in enumerate(lines):
        m_h2 = h2_pattern.match(line.strip())
        if m_h2:
            current_chapter = int(m_h2.group(1))
            expected_sub = 1
            continue

        m_h3 = h3_pattern.match(line.strip())
        if m_h3:
            ch = int(m_h3.group(1))
            sub = int(m_h3.group(2))
            if ch == current_chapter:
                if sub != expected_sub:
                    errors.append(
                        f"Unterabschnitt-Nummerierung: Erwartet {ch}.{expected_sub}, "
                        f"gefunden {ch}.{sub} (Zeile {i + 1})."
                    )
                expected_sub = sub + 1

    # H4 subsection numbering
    h4_pattern = re.compile(r"^#### (\d+)\.(\d+)\.(\d+)\s")
    current_h3 = (0, 0)
    expected_h4 = 1

    for i, line in enumerate(lines):
        m_h3 = h3_pattern.match(line.strip())
        if m_h3:
            current_h3 = (int(m_h3.group(1)), int(m_h3.group(2)))
            expected_h4 = 1
            continue

        m_h4 = h4_pattern.match(line.strip())
        if m_h4:
            ch = int(m_h4.group(1))
            sub = int(m_h4.group(2))
            subsub = int(m_h4.group(3))
            if (ch, sub) == current_h3:
                if subsub != expected_h4:
                    errors.append(
                        f"Unterabschnitt-Nummerierung: Erwartet {ch}.{sub}.{expected_h4}, "
                        f"gefunden {ch}.{sub}.{subsub} (Zeile {i + 1})."
                    )
                expected_h4 = subsub + 1

    return errors


# ─── 2.1.3 Querverweise ───

def check_cross_references(text, lines):
    """Prüft §-Querverweise und Kapitelverweise."""
    errors = []

    # Collect all existing section numbers (H2, H3, H4)
    existing_sections = set()
    h2_p = re.compile(r"^## (\d+)\.")
    h3_p = re.compile(r"^### (\d+)\.(\d+)\s")
    h4_p = re.compile(r"^#### (\d+)\.(\d+)\.(\d+)\s")

    for line in lines:
        m = h2_p.match(line.strip())
        if m:
            existing_sections.add(m.group(1))
        m = h3_p.match(line.strip())
        if m:
            existing_sections.add(f"{m.group(1)}.{m.group(2)}")
        m = h4_p.match(line.strip())
        if m:
            existing_sections.add(f"{m.group(1)}.{m.group(2)}.{m.group(3)}")

    # Find §X.Y references in body text (not in headings)
    # Exclude German law references (§393, §630, §38, §43, §45, §93 etc.)
    # Only check references that look like document cross-refs: §X.Y (with dot)
    ref_pattern = re.compile(r"§(\d+\.\d+(?:\.\d+)*)")
    for i, line in enumerate(lines):
        if line.strip().startswith("#"):
            continue
        for m in ref_pattern.finditer(line):
            ref = m.group(1)
            if ref not in existing_sections:
                errors.append(
                    f"Querverweis §{ref} in Zeile {i + 1} zeigt auf keinen existierenden Abschnitt."
                )

    # Find "Kapitel X" references
    kap_pattern = re.compile(r"Kapitel\s+(\d+)")
    chapter_nums = set()
    for line in lines:
        m = h2_p.match(line.strip())
        if m:
            chapter_nums.add(int(m.group(1)))

    for i, line in enumerate(lines):
        if line.strip().startswith("#"):
            continue
        for m in kap_pattern.finditer(line):
            kap = int(m.group(1))
            if kap not in chapter_nums:
                errors.append(
                    f"Kapitelverweis 'Kapitel {kap}' in Zeile {i + 1} — kein Kapitel mit dieser Nummer."
                )

    return errors


# ─── 2.1.5 Formatierung ───

def check_formatting(lines):
    """Prüft auf Formatierungsartefakte."""
    errors = []

    # Check for double separators (--- on consecutive non-blank lines)
    prev_was_separator = False
    prev_sep_line = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "---":
            if prev_was_separator:
                errors.append(
                    f"Doppelte Trennlinie in Zeilen {prev_sep_line} und {i + 1}."
                )
            prev_was_separator = True
            prev_sep_line = i + 1
        elif stripped == "":
            pass  # blank lines don't reset
        else:
            prev_was_separator = False

    # Check for missing --- before H2 chapters (except first H2 and ToC)
    h2_pattern = re.compile(r"^## \d+\.")
    h2_fazit = re.compile(r"^## Fazit")
    first_h2_found = False

    for i, line in enumerate(lines):
        if h2_pattern.match(line.strip()) or h2_fazit.match(line.strip()):
            if not first_h2_found:
                first_h2_found = True
                continue
            # Look backwards for ---
            found_separator = False
            for j in range(i - 1, max(i - 6, 0), -1):
                if lines[j].strip() == "---":
                    found_separator = True
                    break
                if lines[j].strip() != "":
                    break
            if not found_separator:
                errors.append(
                    f"Fehlender Trennstrich (---) vor H2-Überschrift in Zeile {i + 1}."
                )

    # Check for triple+ blank lines
    blank_count = 0
    for i, line in enumerate(lines):
        if line.strip() == "":
            blank_count += 1
        else:
            if blank_count >= 3:
                errors.append(
                    f"Mehr als 2 aufeinanderfolgende Leerzeilen vor Zeile {i + 1} ({blank_count} Leerzeilen)."
                )
            blank_count = 0

    return errors


# ─── 2.4 Quellenprüfung ───

def check_sources(text, lines):
    """Prüft Quellennummerierung und -anzahl."""
    errors = []

    # Find all source numbers [X]
    source_pattern = re.compile(r"^\- \[(\d+)\]")
    source_nums = []
    in_sources = False

    for i, line in enumerate(lines):
        if "## 18. Quellenverzeichnis" in line:
            in_sources = True
            continue
        if in_sources:
            m = source_pattern.match(line.strip())
            if m:
                source_nums.append((int(m.group(1)), i + 1))

    if not source_nums:
        errors.append("Keine Quellen im Quellenverzeichnis gefunden.")
        return errors, 0

    actual_count = len(source_nums)

    # Check sequential numbering
    for idx, (num, lineno) in enumerate(source_nums):
        expected = idx + 1
        if num != expected:
            errors.append(
                f"Quellennummerierung: Erwartet [{expected}], gefunden [{num}] (Zeile {lineno})."
            )
            break  # stop at first gap

    # Check count matches header
    header_count_match = re.search(r"(\d+)\s+Quellen", text)
    if header_count_match:
        stated_count = int(header_count_match.group(1))
        if stated_count != actual_count:
            errors.append(
                f"Quellenanzahl im Header: {stated_count}, tatsächlich: {actual_count}."
            )

    # Check closing sentence mentions correct count
    closing_pattern = re.compile(r"(\d+)\s+Quellen.*Es stellt keine Rechtsberatung dar\.")
    closing_match = closing_pattern.search(text[-500:])
    if closing_match:
        closing_count = int(closing_match.group(1))
        if closing_count != actual_count:
            errors.append(
                f"Quellenanzahl im Abschlusssatz: {closing_count}, tatsächlich: {actual_count}."
            )
    else:
        errors.append("Abschlusssatz mit Quellenanzahl nicht gefunden.")

    return errors, actual_count


# ─── 2.5 Versionskonsistenz ───

def check_version_consistency(text):
    """Prüft ob Versionsnummer überall identisch ist."""
    errors = []

    # Find version in header
    header_match = re.search(r"\*\*Version:\*\*\s+(\d+\.\d+)", text)
    if not header_match:
        errors.append("Versionsnummer im Header nicht gefunden.")
        return errors, None

    version = header_match.group(1)

    # Check in closing sentence
    closing_match = re.search(r"Version\s+(\d+\.\d+).*Es stellt keine Rechtsberatung dar\.", text[-500:])
    if closing_match:
        closing_version = closing_match.group(1)
        if closing_version != version:
            errors.append(
                f"Versionsinkonsistenz: Header sagt {version}, Abschlusssatz sagt {closing_version}."
            )
    else:
        errors.append("Versionsnummer im Abschlusssatz nicht gefunden.")

    # Check author
    author_match = re.search(r"\*\*Autor:\*\*\s+(.+?)(?:\s{2}|\n)", text)
    if not author_match:
        errors.append("Autorenname nicht gefunden.")

    return errors, version


# ─── 2.1.4 Leere Abschnitte ───

def check_empty_sections(lines):
    """Prüft ob es Überschriften ohne nachfolgenden Inhalt gibt."""
    errors = []
    heading_pattern = re.compile(r"^#{2,4}\s+")
    sub_heading = re.compile(r"^#{3,4}\s+")

    for i, line in enumerate(lines):
        if heading_pattern.match(line.strip()):
            # Look at next non-blank line
            has_content = False
            for j in range(i + 1, min(i + 10, len(lines))):
                stripped = lines[j].strip()
                if stripped == "":
                    continue
                if stripped == "---":
                    break
                # A sub-heading counts as content for the parent heading
                has_content = True
                break
            if not has_content:
                errors.append(
                    f"Möglicherweise leerer Abschnitt: '{line.strip()}' (Zeile {i + 1})."
                )

    return errors


# ─── Main ───

def main():
    text = load_document()
    lines = extract_lines(text)

    print("=" * 70)
    print("  VALIDATE.PY — Strukturprüfung Hauptdokument")
    print("=" * 70)
    print()

    all_errors = []
    results = {}

    # 2.1.1 Gliederung
    print("▸ 2.1.1 Gliederung (ToC vs. Überschriften)...")
    errs, toc_count, h2_count = check_toc_vs_headings(text, lines)
    all_errors.extend(errs)
    results["2.1.1"] = "✅" if not errs else "❌"
    print(f"  ToC-Einträge: {toc_count}, H2-Überschriften: {h2_count}")
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Alle ToC-Einträge stimmen mit H2-Überschriften überein.")

    # 2.1.2 Nummerierung
    print("\n▸ 2.1.2 Nummerierung...")
    errs = check_chapter_numbering(lines)
    all_errors.extend(errs)
    results["2.1.2"] = "✅" if not errs else "❌"
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Kapitel- und Unterabschnitt-Nummerierung lückenlos.")

    # 2.1.3 Querverweise
    print("\n▸ 2.1.3 Querverweise...")
    errs = check_cross_references(text, lines)
    all_errors.extend(errs)
    results["2.1.3"] = "✅" if not errs else "❌"
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Alle §-Querverweise und Kapitelverweise gültig.")

    # 2.1.4 Leere Abschnitte
    print("\n▸ 2.1.4 Leere Abschnitte...")
    errs = check_empty_sections(lines)
    all_errors.extend(errs)
    results["2.1.4"] = "✅" if not errs else "❌"
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Keine leeren Abschnitte gefunden.")

    # 2.1.5 Formatierung
    print("\n▸ 2.1.5 Formatierung...")
    errs = check_formatting(lines)
    all_errors.extend(errs)
    results["2.1.5"] = "✅" if not errs else "❌"
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Keine Formatierungsartefakte gefunden.")

    # 2.4 Quellenprüfung
    print("\n▸ 2.4 Quellenprüfung...")
    errs, source_count = check_sources(text, lines)
    all_errors.extend(errs)
    results["2.4"] = "✅" if not errs else "❌"
    print(f"  Quellen gefunden: {source_count}")
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Quellenverzeichnis konsistent.")

    # 2.5 Versionskonsistenz
    print("\n▸ 2.5 Versionskonsistenz...")
    errs, version = check_version_consistency(text)
    all_errors.extend(errs)
    results["2.5"] = "✅" if not errs else "❌"
    if version:
        print(f"  Version: {version}")
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Versionsnummer konsistent.")

    # Summary
    print("\n" + "=" * 70)
    print("  ZUSAMMENFASSUNG")
    print("=" * 70)
    print()
    for step, status in results.items():
        print(f"  {step}: {status}")
    print()

    total_errors = len(all_errors)
    if total_errors == 0:
        print(f"  ✅ Keine Fehler gefunden.")
    else:
        print(f"  ❌ {total_errors} Fehler gefunden.")

    print()
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
