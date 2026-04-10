#!/usr/bin/env python3
"""
red_thread.py — Automatisierte Roter-Faden-Prüfung für das Hauptdokument.
Prüft: Kapitel-Funktionen, Querverweisstruktur, inhaltliche Abgrenzung.
"""

import re
import sys

DOCUMENT = "Wolkenfrei.md"

# Expected chapter functions (thematische Zuordnung)
CHAPTER_FUNCTIONS = {
    1: "Kernproblem: Regelungslücke, Fallbeispiele, Realitätsgründe, TI-Exposition",
    2: "Rechtliche Grundlagen: CLOUD Act Gesetzestext, Konstellationen A/B/C",
    3: "US-Zugriffsebenen: CLOUD Act, FISA §702, NSL, Grenzkontrolle",
    4: "Europäischer Behördenzugriff: e-Evidence-VO, Five Eyes, ethische Frage",
    5: "Anbieterbewertung: Risikotabellen, Zertifizierungen, Detailanalysen",
    6: "Operator-Modell: S3NS, Delos Cloud, Souveränitätsspektrum",
    7: "Hyperscaling: Kapazitätsvergleich, Service-Tiefe, GPU-Hierarchie",
    8: "EU-Plattformstack: Schleswig-Holstein, Zielarchitektur",
    9: "EU-US-Abkommen: DPF, Executive Agreement, Schrems III",
    10: "Lobbyarbeit: EU-Transparenzregister, Lobbymethoden",
    11: "Berater-Falle: US-Beratungspartnerschaften, Interessenkonflikte",
    12: "Marktbeispiele: GKV-RZ, KVen, KIS, Übernahmen, SaaS",
    13: "Clientseitige Verschlüsselung: BYOK vs HYOK, Grenzen",
    14: "Bewertungsschema: 5 Dimensionen, Länderranking",
    15: "Globaler Vergleich: Regionenanalyse CLOUD-Act-Strategien",
    16: "Handlungsempfehlungen: Sofortmaßnahmen, 4-Stufen-Modell, TIA, Haftung",
    17: "Regulatorischer Ausblick: TI 2.0, GeDIG, EHDS",
    18: "Quellenverzeichnis",
}


def load_document():
    with open(DOCUMENT, "r", encoding="utf-8") as f:
        return f.read()


def extract_chapters(text):
    """Extrahiert Kapiteltext zwischen H2-Überschriften."""
    lines = text.split("\n")
    chapters = {}
    current_chapter = None
    current_lines = []

    h2_pattern = re.compile(r"^## (\d+)\.")
    h2_fazit = re.compile(r"^## Fazit")

    for line in lines:
        m = h2_pattern.match(line.strip())
        if m:
            if current_chapter is not None:
                chapters[current_chapter] = "\n".join(current_lines)
            current_chapter = int(m.group(1))
            current_lines = [line]
            continue
        m2 = h2_fazit.match(line.strip())
        if m2:
            if current_chapter is not None:
                chapters[current_chapter] = "\n".join(current_lines)
            current_chapter = "Fazit"
            current_lines = [line]
            continue
        if current_chapter is not None:
            current_lines.append(line)

    if current_chapter is not None:
        chapters[current_chapter] = "\n".join(current_lines)

    return chapters


def check_chapter_has_content(chapters):
    """Prüft ob jedes Kapitel substantiellen Inhalt hat."""
    errors = []

    for ch_num in range(1, 19):
        if ch_num not in chapters:
            errors.append(f"Kapitel {ch_num} fehlt vollständig.")
            continue
        # Count non-blank, non-heading, non-separator lines
        content_lines = 0
        for line in chapters[ch_num].split("\n"):
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and stripped != "---":
                content_lines += 1
        if content_lines < 5:
            errors.append(
                f"Kapitel {ch_num} hat nur {content_lines} Inhaltszeilen — möglicherweise leer."
            )

    return errors


def check_chapter_cross_references(chapters):
    """Prüft ob Kapitel aufeinander verweisen (roter Faden)."""
    errors = []
    warnings = []

    kap_ref_pattern = re.compile(r"Kapitel\s+(\d+)")
    section_ref_pattern = re.compile(r"§(\d+)\.(\d+)")

    for ch_num in range(1, 18):  # Skip Quellenverzeichnis
        if ch_num not in chapters:
            continue
        text = chapters[ch_num]

        # Check for forward references (Kapitel X with X > ch_num)
        has_forward_ref = False
        has_backward_ref = False

        for m in kap_ref_pattern.finditer(text):
            ref_ch = int(m.group(1))
            if ref_ch > ch_num:
                has_forward_ref = True
            if ref_ch < ch_num:
                has_backward_ref = True

        for m in section_ref_pattern.finditer(text):
            ref_ch = int(m.group(1))
            if ref_ch > ch_num:
                has_forward_ref = True
            if ref_ch < ch_num:
                has_backward_ref = True

        # Chapters should be connected — either forward or backward references
        if ch_num > 1 and not has_backward_ref and ch_num <= 17:
            warnings.append(
                f"Kapitel {ch_num}: Kein Rückverweis auf frühere Kapitel gefunden."
            )

    return errors, warnings


def check_fazit_coverage(chapters):
    """Prüft ob das Fazit die zentralen Kapitelthemen abdeckt."""
    errors = []

    if "Fazit" not in chapters:
        errors.append("Fazit fehlt im Dokument.")
        return errors

    fazit_text = chapters["Fazit"].lower()

    # Key terms that should appear in the Fazit
    key_terms = [
        ("serverstandort", "Kernaussage: Serverstandort"),
        ("c5", "BSI C5 / § 393 SGB V"),
        ("operator", "Operator-Modell"),
        ("eu-plattform", "EU-Plattformstack"),
        ("verschlüsselung", "Verschlüsselung (HYOK)"),
        ("lobbyarbeit", "Lobbyarbeit"),
        ("fisa", "FISA § 702"),
        ("haftung", "Haftungskette"),
    ]

    for term, desc in key_terms:
        if term not in fazit_text:
            errors.append(f"Fazit erwähnt '{desc}' nicht — Thema könnte fehlen.")

    return errors


def check_kernaussagen_count(chapters):
    """Prüft ob die Anzahl der Kernaussagen im Fazit stimmt."""
    errors = []

    if "Fazit" not in chapters:
        return errors

    fazit = chapters["Fazit"]

    # Check stated count
    count_match = re.search(r"(\w+)\s+Kernaussagen", fazit)
    if count_match:
        stated = count_match.group(1).lower()
        number_words = {
            "zwölf": 12, "elf": 11, "zehn": 10, "dreizehn": 13,
            "vierzehn": 14, "fünfzehn": 15
        }
        stated_num = number_words.get(stated, None)
        if stated_num is None:
            try:
                stated_num = int(stated)
            except ValueError:
                stated_num = None

        # Count numbered items
        numbered = re.findall(r"^\d+\.\s+\*\*", fazit, re.MULTILINE)
        actual_num = len(numbered)

        if stated_num and stated_num != actual_num:
            errors.append(
                f"Fazit sagt '{stated}' Kernaussagen, tatsächlich {actual_num} nummerierte Aussagen."
            )

    return errors


def check_redundancy_indicators(chapters):
    """Grobe Prüfung auf redundante Textblöcke zwischen Kapiteln."""
    warnings = []

    # Extract key phrases (sentences > 60 chars) from each chapter
    phrase_map = {}
    for ch_num, text in chapters.items():
        if ch_num == "Fazit" or ch_num == 18:
            continue
        sentences = re.split(r'[.!?]\s+', text)
        for s in sentences:
            s_clean = s.strip()
            if len(s_clean) > 80:
                # Normalize whitespace
                s_norm = " ".join(s_clean.split()).lower()
                if s_norm in phrase_map:
                    if phrase_map[s_norm] != ch_num:
                        warnings.append(
                            f"Mögliche Redundanz: Ähnlicher Satz in Kapitel {phrase_map[s_norm]} "
                            f"und Kapitel {ch_num} ('{s_clean[:60]}...')"
                        )
                else:
                    phrase_map[s_norm] = ch_num

    return warnings


def main():
    text = load_document()
    chapters = extract_chapters(text)

    print("=" * 70)
    print("  RED_THREAD.PY — Roter-Faden-Prüfung Hauptdokument")
    print("=" * 70)
    print()

    all_errors = []
    all_warnings = []

    # 1. Chapter content check
    print("▸ Kapitelinhalt prüfen...")
    errs = check_chapter_has_content(chapters)
    all_errors.extend(errs)
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print(f"  ✅ Alle {len([c for c in chapters if c != 'Fazit' and c != 18])} "
              f"Inhaltskapitel haben substantiellen Inhalt.")

    # 2. Cross-reference network
    print("\n▸ Querverweisstruktur prüfen...")
    errs, warns = check_chapter_cross_references(chapters)
    all_errors.extend(errs)
    all_warnings.extend(warns)
    for e in errs:
        print(f"  ❌ {e}")
    for w in warns:
        print(f"  ⚠️ {w}")
    if not errs and not warns:
        print("  ✅ Alle Kapitel sind über Querverweise vernetzt.")

    # 3. Fazit coverage
    print("\n▸ Fazit-Abdeckung prüfen...")
    errs = check_fazit_coverage(chapters)
    all_errors.extend(errs)
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Fazit deckt alle zentralen Themen ab.")

    # 4. Kernaussagen count
    print("\n▸ Kernaussagen-Zählung prüfen...")
    errs = check_kernaussagen_count(chapters)
    all_errors.extend(errs)
    for e in errs:
        print(f"  ❌ {e}")
    if not errs:
        print("  ✅ Kernaussagen-Anzahl konsistent.")

    # 5. Redundancy check
    print("\n▸ Redundanzprüfung (grob)...")
    warns = check_redundancy_indicators(chapters)
    all_warnings.extend(warns)
    if warns:
        print(f"  ⚠️ {len(warns)} mögliche Redundanzen gefunden:")
        for w in warns[:5]:
            print(f"    {w}")
        if len(warns) > 5:
            print(f"    ... und {len(warns) - 5} weitere")
    else:
        print("  ✅ Keine offensichtlichen Redundanzen gefunden.")

    # Summary
    print("\n" + "=" * 70)
    print("  ZUSAMMENFASSUNG")
    print("=" * 70)
    print()
    print(f"  Fehler:    {len(all_errors)}")
    print(f"  Warnungen: {len(all_warnings)}")
    print()

    if all_errors:
        print("  ❌ Fehler:")
        for e in all_errors:
            print(f"    • {e}")
    if all_warnings:
        print("  ⚠️ Warnungen:")
        for w in all_warnings:
            print(f"    • {w}")
    if not all_errors and not all_warnings:
        print("  ✅ Roter Faden intakt — keine Probleme gefunden.")

    print()
    return 0 if not all_errors else 1


if __name__ == "__main__":
    sys.exit(main())
