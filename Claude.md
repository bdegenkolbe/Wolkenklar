# Claude.md — Projektanweisung

**Projekt:** US CLOUD Act & Deutsche Datensouveränität  
**Organisation:** 4K Analytics GmbH / HIGL – Health Innovators Group Leipzig  
**Autor:** Björn Degenkolbe, Geschäftsführer

---

## 1. Projektbeschreibung

Dieses Projekt pflegt ein umfassendes Analysedokument zur CLOUD-Act-Exposition des deutschen Gesundheitswesens. Das Dokument dient als Wissensgrundlage für GKV/KV/Klinik-IT-Beratung und interne Architekturentscheidungen. Es wird regelmäßig aktualisiert, validiert und als PDF/Word exportiert.

---

## 2. Dateien

| Datei | Zweck |
|---|---|
| `Wolkenfrei.md` | Hauptdokument |
| `Validierung.md` | Prüfprozess — regelt Ablauf, Prüfschritte und Versionierung |
| `Validierung-Ergebnisse.md` | Historisches Protokoll aller Validierungen |
| `Formatvorlage.md` | Gestaltungsrichtlinie für PDF- und Word-Export |
| `Claude.md` | Dieses Dokument — Projektanweisung für Claude |
| `validate.py` | Automatisierte Strukturprüfung |
| `red_thread.py` | Automatisierte Roter-Faden-Prüfung |
| `build_docx.js` | Word-Export-Skript |
| `build_pdf.py` | PDF-Export-Skript |
| `build_wiki.py` | Wiki-Export: splittet Wolkenfrei.md in MkDocs-Seiten |
| `mkdocs.yml` | MkDocs-Konfiguration (Theme, Navigation, Plugins) |

---

## 3. Regeln

### 3.1 Stil und Tonalität

- Sachlich, faktenbasiert, nicht polemisch
- Neutral, aber mit Haltung — das Thema ist dem Autor wichtig
- Fließtext bevorzugt, keine unnötigen Aufzählungen
- Fachbegriffe beim ersten Auftreten erklären
- Abkürzungen beim ersten Auftreten ausschreiben
- Kein Marketing-Sprech
- Persönliche Ich-Perspektive des Autors, wo angemessen

### 3.2 Rechtliche Sorgfalt

- Das Dokument stellt keine Rechtsberatung dar — dieser Hinweis steht im Dokument und muss erhalten bleiben
- Konjunktiv verwenden, wenn auf Gesetzentwürfe Bezug genommen wird, die noch nicht in Kraft sind
- § 393 SGB V und DSGVO Art. 48 ergänzen sich — sie widersprechen sich nicht. Niemals als "Normwiderspruch" formulieren
- Haftungswege (DSGVO-Bußgeld, Organhaftung, NIS2-Lieferkette) sauber trennen und nicht vermischen

### 3.3 Inhaltliche Regeln

- US-Hyperscaler gleichgewichtig behandeln — Azure nicht als Stellvertreter für alle verwenden, außer bei konkreten Einzelfällen
- Alle Fakten müssen belegbar sein — keine Behauptungen ohne Quelle
- Bei Personen: Nur behaupten, was dokumentiert ist (z.B. nicht annehmen, dass jemand GKV-versichert ist)
- Das Dokument wurde mit Claude (Anthropic) erstellt — dieser Hinweis muss im Dokument stehen

### 3.4 Änderungen am Hauptdokument

- Jede Änderung löst eine Validierung gemäß `Validierung.md` aus
- Ergebnisse werden in `Validierung-Ergebnisse.md` protokolliert
- Nach jeder abgeschlossenen Validierung werden PDF und Word neu erstellt gemäß `Formatvorlage.md`
- Versionsnummer wird hochgezählt

### 3.5 Was nicht ohne Rückfrage geändert werden darf

- Kapitelstruktur (Reihenfolge, Anzahl, Nummerierung)
- Zentrale Argumentationslinien (Regelungslücke, Haftungskette, Souveränitätsstufen)
- Autorenname und Organisationszuordnung
- Quellenverzeichnis (keine Quellen löschen, nur ergänzen)

---

## 4. Skills

Folgende Skills werden für dieses Projekt verwendet:

| Skill | Zweck |
|---|---|
| `docx` | Word-Export nach jeder Validierung |
| `pdf` | PDF-Export nach jeder Validierung |
| `file-reading` | Hauptdokument lesen bei Upload |

---

## 5. Typischer Arbeitsablauf

1. Autor bringt inhaltliche Änderung oder neue Information ein
2. Claude setzt die Änderung im Hauptdokument um
3. Claude führt die Validierung gemäß `Validierung.md` durch
4. Ergebnisse werden in `Validierung-Ergebnisse.md` protokolliert
5. Fehler werden behoben, Nachprüfung durchgeführt
6. Neue Version wird vergeben
7. PDF und Word werden neu erstellt
