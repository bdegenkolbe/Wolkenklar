# Formatvorlage.md — Gestaltungsrichtlinie für PDF- und Word-Export

**Gilt für:** Alle PDF- und Word-Exporte des Hauptdokuments.

---

## 1. Seitenaufbau

| Eigenschaft | Wert |
|---|---|
| Format | A4 (210 × 297 mm) |
| Seitenränder | oben 2,5 cm, unten 2,5 cm, links 2 cm, rechts 2 cm |
| Inhaltsbreite | Seitenbreite abzüglich Ränder |
| Ausrichtung | Hochformat |

---

## 2. Schriften

| Element | Schrift | Größe | Gewicht | Farbe |
|---|---|---|---|---|
| Dokumenttitel (H1) | Arial / Helvetica | 22 pt | Bold | #1B3A5C |
| Untertitel | Arial / Helvetica | 11 pt | Regular | #2E75B6 |
| Metadaten (Autor, Version etc.) | Arial / Helvetica | 9 pt | Regular | #666666 |
| Kapitelüberschrift (H2) | Arial / Helvetica | 14 pt | Bold | #1B3A5C |
| Abschnittsüberschrift (H3) | Arial / Helvetica | 12 pt | Bold | #2E75B6 |
| Unterabschnitt (H4) | Arial / Helvetica | 10,5 pt | Bold | #333333 |
| Fließtext | Arial / Helvetica | 9,5 pt | Regular | #000000 |
| Tabellenkopf | Arial / Helvetica | 7,5 pt | Bold | #FFFFFF |
| Tabellenzelle | Arial / Helvetica | 7,5 pt | Regular | #000000 |
| Code | Consolas / Courier | 7,5 pt | Regular | #333333 |
| Blockquote | Arial / Helvetica | 9 pt | Italic | #333333 |
| Header/Footer | Arial / Helvetica | 7,5 pt | Regular | #999999 |

Zeilenabstand Fließtext: 1,15 (ca. 13 pt Leading bei 9,5 pt Schrift).  
Absatzabstand: 1 mm vor, 2 mm nach.  
Textausrichtung Fließtext: Blocksatz.

---

## 3. Farben

| Verwendung | Hex-Wert | Beschreibung |
|---|---|---|
| Primary | #1B3A5C | Dunkles Navy — Titel, H2 |
| Accent | #2E75B6 | Stahlblau — H3, Links, Trennlinien |
| Tabellenkopf Hintergrund | #1B3A5C | Navy |
| Tabellenkopf Text | #FFFFFF | Weiß |
| Tabelle alternierende Zeile | #F2F7FB | Hellblau |
| Tabellenrahmen | #B0C4DE | Hellgrau-Blau |
| Blockquote Hintergrund | #F0F5FA | Sehr helles Blau |
| Blockquote Seitenbalken | #2E75B6 | Accent |
| Code Hintergrund | #F5F5F5 | Hellgrau |
| Metadaten / Grautext | #666666 | Mittelgrau |
| Header/Footer Text | #999999 | Hellgrau |
| Header/Footer Linie | #CCCCCC | Sehr hellgrau |

---

## 4. Header und Footer

**Header (jede Seite):**

- Links: Dokumenttitel ("US CLOUD Act & Deutsche Datensouveränität")
- Rechts: Organisation ("4K Analytics GmbH / HIGL")
- Trennlinie darunter (0,5 pt, #CCCCCC)

**Footer (jede Seite):**

- Links: Version und Vertraulichkeitshinweis ("Version X.0 — April 2026 — Vertraulich")
- Rechts: Seitenzahl ("Seite X")
- Trennlinie darüber (0,5 pt, #CCCCCC)

---

## 5. Kapitelgestaltung

- Jedes H2-Kapitel beginnt auf einer neuen Seite (Seitenumbruch vor H2)
- Über jeder H2-Überschrift eine Akzentlinie (1,5 pt, #2E75B6, volle Breite)
- Ausnahme: Das erste H2 im Dokument hat keinen Seitenumbruch davor

---

## 6. Tabellen

- Volle Inhaltsbreite
- Spaltenbreiten gleichmäßig verteilt (außer bei Tabellen mit definierter Gewichtung)
- Kopfzeile: Navy-Hintergrund (#1B3A5C), weißer Text, Bold
- Datenzeilen: Abwechselnd weiß und hellblau (#F2F7FB)
- Rahmen: 0,5 pt, #B0C4DE
- Zellenabstand innen: 3 pt oben/unten, 4 pt links/rechts
- Kopfzeile wird bei Seitenumbruch wiederholt
- Text in Zellen bricht automatisch um

---

## 7. Blockquotes

- Eingerückt (8 mm links)
- Hintergrund #F0F5FA
- Seitenbalken links: 3 mm breit, Vollfarbe #2E75B6
- Schrift: Italic, 9 pt
- Innenabstand: 4 mm (oben/unten/links/rechts im Inhaltsbereich)

**Hinweis zur PDF-Implementierung:** Blockquotes werden als verschachtelte Tabelle realisiert — eine äußere Tabelle (8 mm Einzug-Spalte + Box-Spalte) und eine innere Tabelle (3 mm Balken-Spalte + Inhalts-Spalte mit #F0F5FA-Hintergrund). Innere Aufzählungspunkte (`> -`) werden als separate Bullet-Absätze im Inhaltsbereich dargestellt. Kein `borderPadding` in `ParagraphStyle` verwenden — ReportLab bezieht diesen Wert nicht in die Höhenberechnung ein, was zu Überlappungen mit benachbarten Elementen führt.

---

## 8. Codeblöcke

- Eingerückt (6 mm links)
- Hintergrund #F5F5F5
- Schrift: Consolas / Courier, 7,5 pt
- Innenabstand: 3 mm
- Kein Rahmen

---

## 9. Aufzählungen

- Eingerückt (10 mm links, 4 mm hängend)
- Aufzählungszeichen: Bullet (•)
- Zeilenabstand wie Fließtext

---

## 10. Erstellungsskripte

| Export | Skript | Bibliothek |
|---|---|---|
| Word (.docx) | `build_docx.js` | docx (npm) |
| PDF (.pdf) | `build_pdf.py` | reportlab (pip) |

Beide Skripte lesen das Hauptdokument (`Wolkenfrei.md`) und erzeugen den Export gemäß dieser Formatvorlage. Bei Änderungen an der Formatvorlage müssen beide Skripte entsprechend angepasst werden.
