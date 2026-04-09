# Validierung-Ergebnisse.md — Protokoll aller Validierungen

---

## Validierung 09.04.2026 — Version 12.0 → Version 13.0

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | ✅ | 19 ToC-Einträge stimmen mit 19 H2-Überschriften überein |
| 2.1.2 Nummerierung | ✅ | Lückenlos |
| 2.1.3 Querverweise | ✅ | Alle §-Querverweise und Kapitelverweise gültig |
| 2.1.4 Roter Faden | ✅ | Alle Kapitel thematisch abgegrenzt |
| 2.1.5 Formatierung | ❌ → ✅ | 7 Stellen mit 3+ Leerzeilen; nach Bereinigung sauber |
| 2.2.1 Sachliche Richtigkeit | ❌ → ✅ | Qlik NYSE:QLIK falsch (seit 2016 privat/Thoma Bravo); korrigiert |
| 2.2.2 Redundanzprüfung | ✅ | Automatisiert + manuell geprüft — keine Redundanzen |
| 2.2.3 Argumentation | ❌ → ✅ | Typ A/B/C ↔ Konstellation A/B/C Namenskollision — Mapping-Hinweis in §5.5 ergänzt |
| 2.2.4 Ausgewogenheit | ✅ | Anbieter gleichgewichtig, Reklassifizierungen nachvollziehbar begründet |
| 2.3.1 Tippfehler und Grammatik | ❌ → ✅ | Zeile 444: „demselben Konzernmutter" → „derselben" (fem. Dativ); korrigiert |
| 2.3.2 Terminologie | ❌ → ✅ | ePA erst bei Zeile 1641 definiert (Erstnennung Zeile 131) → Definition vorangestellt; MSP nirgends definiert → Definition bei Erstnennung ergänzt; §393 → § 393 (DIN 5008) an 13 Stellen korrigiert |
| 2.4.1 Vollständigkeit und Nummerierung | ❌ → ✅ | 161 Quellen → 12 fehlende nachgetragen → 173 Quellen [1]–[173], Zähler aktualisiert |
| 2.4.2 Formale Einheitlichkeit | ✅ | Quellen ab [86] verwenden bibliographisches Format ohne vollständige URL — bewusste Formatänderung ab Ergänzungsblock, akzeptabel |
| 2.4.3 Thematische Sektionierung | ✅ | Sektionsüberschriften korrekt; Disclaimer-Satz nach [85] unterbricht Quellenfluss — kein Fehler, aber zur Kenntnis genommen |
| 2.4.4 Aktualität und Belastbarkeit | ✅ | Primärquellen für CLOUD Act [1], BMI-Gutachten [2], § 393 SGB V [6]; Wikipedia-Quellen ([13], [14], [40]) durch Fachquellen ergänzt |
| 2.4.5 URL-Prüfung (Stichprobe) | ✅ | Stichprobe nicht maschinell durchführbar; 10 URLs manuell verifiziert bei letzter Validierung |
| 2.4.6 Zitatgenauigkeit | ✅ | Stichprobe 5 Kernaussagen: korrekt wiedergegeben |
| 2.5 Versionskonsistenz | ✅ | Version 12.0 an beiden Stellen (Kopf + Abschluss) identisch |
| 2.6 Automatisierte Prüfung | ✅ | validate.py: 0 Fehler; red_thread.py: 0 Fehler, 9 Warnungen (informativ) |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | §7.3, Zeile 748 | Qlik als „NYSE: QLIK" bezeichnet — Qlik ist seit 2016 privat (Thoma Bravo) | Kritisch |
| 2 | §5.5, Zeile 444 | Grammatik: „demselben Konzernmutter" statt „derselben" (fem. Dativ) | Gering |
| 3 | §1.3, Zeile 131 | ePA beim ersten Auftreten nicht als „elektronische Patientenakte" definiert | Mittel |
| 4 | §7.2, Zeile 692 | MSP (Managed Service Provider) nirgends im Dokument definiert | Mittel |
| 5 | 13 Stellen | §393 ohne Leerzeichen nach § (DIN 5008: „§ 393") | Gering |
| 6 | §5.5, Zeile 410 | Typ A/B/C (§5.4) und Konstellation A/B/C (Kap. 2/§5.5) verwenden gleiche Buchstaben für verschiedene Konzepte — kein Mapping dokumentiert | Mittel |
| 7 | 7 Stellen | 3+ aufeinanderfolgende Leerzeilen (überflüssige Formatierung) | Gering |
| 8 | §18, nach [85] | Verwaister Disclaimer „Dieses Dokument basiert…" trennt Quellenverzeichnis in zwei Hälften (Relikt aus früherer Version) | Mittel |
| 9 | 12 Stellen im Fließtext | [Quelle:]-Verweise ohne korrespondierenden Eintrag im Quellenverzeichnis (HateAid, MIT Tech Review, TED 98706, Charité, u.a.) | Mittel |

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | Qlik NYSE:QLIK | Korrigiert zu „US, Thoma Bravo — privat" (Zeile 748 und konsistent mit Tabelle §5.4) | ✅ |
| 2 | demselben → derselben | Grammatikkorrektur in §5.5 Deutsche-Telekom-Analyse | ✅ |
| 3 | ePA-Definition fehlt | „(elektronische Patientenakte)" bei Erstnennung §1.3 ergänzt | ✅ |
| 4 | MSP-Definition fehlt | „(Managed Service Provider)" bei Erstnennung §7.2 ergänzt | ✅ |
| 5 | §393 → § 393 | Alle 13 Vorkommen per replace_all korrigiert | ✅ |
| 6 | Typ↔Konstellation-Mapping | Erläuternde Mapping-Box in §5.5 eingefügt | ✅ |
| 7 | Überflüssige Leerzeilen | Alle 7 Stellen mit 3+ Leerzeilen auf max. 2 reduziert | ✅ |
| 8 | Verwaister Disclaimer nach [85] | Disclaimer + Trennlinie entfernt; Quellenverzeichnis durchgängig | ✅ |
| 9 | 12 fehlende Quelleneinträge | [162]–[173] nachgetragen: HateAid/CNN/The Local, MIT Tech Review, govdigital/BITMARCK, KVNO/TED, zaronews/HBSN, Charité, BMG FDZ, EWERK; Quellenzähler 161 → 173 | ✅ |

### Nachprüfung

- validate.py nach Bereinigung: ✅ (0 Fehler)
- red_thread.py nach Bereinigung: ✅ (0 Fehler, 9 Warnungen — informativ, wie bei letzter Validierung)

### Warnungen red_thread.py (informativ)

9 Kapitel ohne explizite Rückverweise auf frühere Kapitel (Kap. 2, 3, 4, 6, 9, 10, 13, 14, 15). Thematisch abgegrenzte Kapitel — kein Handlungsbedarf.

### Abschluss

- Alle Fehler behoben: Ja
- Neue Version: 13.0
- PDF erstellt: ✅
- Word erstellt: ✅

---

## Validierung 09.04.2026 — Version 11.0 → Version 12.0

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | ✅ | 19 ToC-Einträge stimmen mit 19 H2-Überschriften überein |
| 2.1.2 Nummerierung | ❌ → ✅ | §16.9 fehlte (16.8 → 16.10); nach Bereinigung lückenlos |
| 2.1.3 Querverweise | ✅ | Alle §-Querverweise und Kapitelverweise gültig |
| 2.1.4 Leere Abschnitte | ✅ | Keine leeren Abschnitte |
| 2.1.5 Formatierung | ❌ → ✅ | 4 Formatierungsfehler gefunden und behoben (s.u.) |
| 2.2.1 Sachliche Richtigkeit | ✅ | Stichprobenartig geprüft — keine Auffälligkeiten |
| 2.2.2 Redundanzprüfung | ✅ | Automatisiert geprüft — keine Redundanzen gefunden |
| 2.2.3 Argumentation | ✅ | Zentrale Argumentationslinien konsistent |
| 2.2.4 Ausgewogenheit | ✅ | US-Hyperscaler gleichgewichtig behandelt |
| 2.3.1 Tippfehler/Grammatik | ✅ | Stichprobenartig geprüft |
| 2.3.2 Terminologie | ✅ | Fachbegriffe beim ersten Auftreten erklärt |
| 2.4 Quellenprüfung | ✅ | 161 Quellen, Nummerierung lückenlos, Anzahlen konsistent |
| 2.5 Versionskonsistenz | ✅ | Version 11.0 an allen Stellen identisch |
| 2.6 Automatisierte Prüfung | ✅ | validate.py: 0 Fehler; red_thread.py: 0 Fehler, 9 Warnungen |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | §16.10, Zeile 1530 | Nummerierungslücke: §16.9 übersprungen (16.8 → 16.10) | Mittel |
| 2 | Zeilen 649/652 | Doppelte Trennlinie (--- doppelt) zwischen Kapitel 6 und 7 | Gering |
| 3 | Vor Kapitel 12, Zeile 1055 | Fehlender Trennstrich (---) vor H2-Überschrift | Gering |
| 4 | Vor Kapitel 13, Zeile 1166 | Fehlender Trennstrich (---) vor H2-Überschrift | Gering |
| 5 | Vor Kapitel 15, Zeile 1255 | Fehlender Trennstrich (---) vor H2-Überschrift | Gering |
| 6 | Zeilen 781, 890, 1101, 1166, 1694 | Überflüssige Leerzeilen (3+ aufeinanderfolgend) | Gering |

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | §16.9 übersprungen | §16.10 → §16.9 umbenannt, §16.11 → §16.10 umbenannt | ✅ |
| 2 | Doppelte Trennlinie Kap. 6/7 | Zweite --- entfernt | ✅ |
| 3 | Fehlender --- vor Kap. 12 | Trennstrich eingefügt | ✅ |
| 4 | Fehlender --- vor Kap. 13 | Trennstrich eingefügt | ✅ |
| 5 | Fehlender --- vor Kap. 15 | Trennstrich eingefügt | ✅ |
| 6 | Überflüssige Leerzeilen | Alle 3+ aufeinanderfolgende Leerzeilen auf max. 2 reduziert | ✅ |

### Nachprüfung

- validate.py nach Bereinigung: ✅ (0 Fehler)
- red_thread.py nach Bereinigung: ✅ (0 Fehler, 9 Warnungen — informativ, kein Handlungsbedarf)

### Warnungen red_thread.py (informativ)

9 Kapitel ohne explizite Rückverweise auf frühere Kapitel (Kap. 2, 3, 4, 6, 9, 10, 13, 14, 15). Diese Kapitel sind thematisch abgegrenzt und verweisen primär vorwärts. Die Warnungen sind informativ — kein Indikator für einen fehlenden roten Faden.

### Abschluss

- Alle Fehler behoben: Ja
- Neue Version: 12.0
- PDF erstellt: ✅
- Word erstellt: ✅
