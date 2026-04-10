# Validierung.md — Prüfprozess für das Hauptdokument

**Gegenstand:** US CLOUD Act & Deutsche Datensouveränität (Hauptdokument)  
**Geltungsbereich:** Jede inhaltliche oder strukturelle Änderung am Hauptdokument löst eine Validierung aus.

---

## 1. Ablauf

1. **Prüfung** — Alle Prüfschritte aus Abschnitt 2 durchlaufen
2. **Dokumentation** — Auffälligkeiten in `Validierung-Ergebnisse.md` protokollieren (Abschnitt 3)
3. **Bereinigung** — Fehler im Hauptdokument beheben
4. **Nachprüfung** — Automatisierte Skripte erneut ausführen, um sicherzustellen, dass die Bereinigung keine neuen Fehler eingeführt hat
5. **Versionierung** — Neue Version vergeben und in `Validierung-Ergebnisse.md` abschließen (Abschnitt 4)
6. **Export** — PDF und Word aus dem Hauptdokument erstellen gemäß `Formatvorlage.md`

Eine Validierung gilt erst als abgeschlossen, wenn alle Prüfschritte durchlaufen, alle Fehler behoben, die Nachprüfung bestanden, die Ergebnisse protokolliert und die Exportdateien erstellt sind.

---

## 2. Prüfschritte

### 2.1 Strukturprüfung

#### 2.1.1 Gliederung

- Stimmen ToC-Einträge und Kapitelüberschriften in Anzahl, Titel und Anker-IDs überein?
- Referenziert jede Unterüberschrift ein existierendes Kapitel?
- Gibt es leere Abschnitte (Überschrift ohne Inhalt)?

#### 2.1.2 Nummerierung

- Ist die Kapitelnummerierung lückenlos und ohne Dopplungen?
- Ist die Unterabschnitt-Nummerierung innerhalb jedes Kapitels lückenlos?
- Stimmen alle Zähler im Dokument mit den tatsächlichen Anzahlen überein (Kernaussagen, Quellen)?

#### 2.1.3 Querverweise

- Zeigt jeder `§X.Y`-Verweis im Fließtext auf eine existierende Unterüberschrift?
- Passt jeder `Kapitel X`-Verweis zum tatsächlichen Kapiteltitel?
- Sind Querverweise nach Kapitelverschiebungen oder Umnummerierungen noch korrekt?

#### 2.1.4 Roter Faden

- Hat jedes Kapitel eine klare, abgegrenzte Funktion im Gesamtdokument?
- Stehen Inhalte dort, wo sie thematisch hingehören?
- Werden Themen, die in früheren Kapiteln analysiert wurden, in späteren Kapiteln nur querverwiesen statt wiederholt?

#### 2.1.5 Formatierung

- Gibt es Formatierungsartefakte (doppelte Trennlinien, überflüssige Leerzeilen)?

### 2.2 Inhaltsprüfung

#### 2.2.1 Sachliche Richtigkeit

- Sind alle genannten Gesetze, Paragraphen und Verordnungen korrekt referenziert?
- Sind alle Fakten (Zahlen, Daten, Unternehmenszuordnungen) aktuell und belegbar?
- Sind alle namentlich genannten Fälle mit Quellen belegt?
- Hat sich der Sachstand seit der letzten Version geändert?

#### 2.2.2 Redundanzprüfung

- Jeden Abschnitt einzeln durchgehen: Werden die Inhalte dieses Abschnitts in anderen Textteilen inhaltlich ähnlich dargestellt?
- Wenn ja: Ist die Doppelung beabsichtigt (Kurzfassung mit Querverweis) oder eine fehlerhafte Redundanz (gleicher Inhalt, gleiche Tiefe, ohne Querverweis)?

#### 2.2.3 Argumentation

- Sind die zentralen Argumentationslinien des Dokuments in sich konsistent?
- Werden rechtliche Zuordnungen sauber getrennt (unterschiedliche Rechtsgrundlagen nicht vermischt)?
- Werden Differenzierungen dort vorgenommen, wo unterschiedliche Sachverhalte unterschiedliche Bewertungen erfordern?

#### 2.2.4 Ausgewogenheit

- Werden Anbieter und Akteure gleichgewichtig behandelt?
- Ist der Ton sachlich und faktenbasiert?
- Werden Einschränkungen und Gegenargumente fair dargestellt?

### 2.3 Sprachliche Prüfung

#### 2.3.1 Tippfehler und Grammatik

- Stichprobenartige Prüfung auf Rechtschreib- und Grammatikfehler
- Bekannte Fehlermuster aus früheren Validierungen gezielt nachsuchen (dokumentiert in `Validierung-Ergebnisse.md`)

#### 2.3.2 Terminologie

- Werden Fachbegriffe beim ersten Auftreten erklärt?
- Werden Abkürzungen beim ersten Auftreten ausgeschrieben?
- Wird dieselbe Sache durchgängig gleich benannt (keine wechselnde Terminologie für denselben Sachverhalt)?

### 2.4 Quellenprüfung

#### 2.4.1 Vollständigkeit und Nummerierung

- Ist die Quellennummerierung lückenlos (keine Lücken, keine Dopplungen)?
- Stimmen die Quellenanzahlen in Versionshinweis, Abschlusssatz und tatsächlichem Bestand überein?
- Steht der Abschlusssatz am tatsächlichen Dokumentende?
- Gibt es im Fließtext zitierte `[N]`-Verweise, die im Quellenverzeichnis keinen Eintrag haben?
- Gibt es Einträge im Quellenverzeichnis, die im Fließtext nie zitiert werden (unverlinkte Quellen)?

#### 2.4.2 Formale Einheitlichkeit

- Hat jede Quelle das Format `[N] Autor/Herausgeber: "Titel", Quelle, Datum. URL`?
- Sind Quellen ohne URL mit einer nachprüfbaren bibliographischen Angabe versehen?
- Werden URLs vollständig angegeben (kein URL-Shortener, kein Redirect-Link)?
- Sind Datumsangaben einheitlich formatiert (z. B. `Monat YYYY`)?

#### 2.4.3 Thematische Sektionierung

- Ist jede Quelle der inhaltlich passenden Sektion im Quellenverzeichnis zugeordnet?
- Gibt es Quellen, die in die falsche Sektion einsortiert sind?
- Sind alle Sektionsüberschriften im Quellenverzeichnis korrekt benannt?

#### 2.4.4 Aktualität und Belastbarkeit

- Sind Quellen, die als aktuell dargestellt werden, tatsächlich jünger als 24 Monate?
- Werden für zentrale Rechtsaussagen (US CLOUD Act, DSGVO, § 393 SGB V) Primärquellen oder anerkannte Fachgutachten zitiert — keine bloßen Presseartikel?
- Werden Unternehmensangaben (Eigentümerstruktur, Umsatz, Installationszahlen) mit datierten Belegen gestützt?
- Sind Zitate aus Wikipedia durch belastbarere Quellen ergänzt, wo der Sachverhalt rechts- oder faktenkritisch ist?

#### 2.4.5 URL-Prüfung (Stichprobe)

- Mindestens 10 % der URLs stichprobenartig manuell aufrufen — sind sie erreichbar?
- Führen URLs direkt zur zitierten Quelle (kein Redirect auf Startseite oder 404)?
- Wurde eine URL durch eine Paywall oder einen Login gesperrt? Wenn ja: alternative Quelle ergänzen oder Archiv-Link (archive.org) hinterlegen.

#### 2.4.6 Zitatgenauigkeit

- Werden direkte Zitate oder Zahlenangaben aus Quellen korrekt wiedergegeben (Stichprobe: 5 Kernaussagen des Dokuments)?
- Werden Quellen inhaltlich korrekt zusammengefasst, ohne sinnentstellende Verkürzung?
- Werden Meinungen, Prognosen oder Hochrechnungen als solche gekennzeichnet und nicht als Fakten dargestellt?

### 2.5 Versionskonsistenz

- Ist die Versionsnummer an allen Stellen identisch?
- Ist der Autorenname korrekt?

### 2.6 Automatisierte Prüfung

- `python3 validate.py` ausführen → Ergebnis protokollieren
- `python3 red_thread.py` ausführen → Ergebnis protokollieren

---

## 3. Dokumentation in Validierung-Ergebnisse.md

Jede Validierung wird in `Validierung-Ergebnisse.md` als eigener Block protokolliert:

```
## Validierung [Datum] — Version X.0 → Version Y.0

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | ✅ / ❌ | Beschreibung |
| 2.1.2 Nummerierung | ✅ / ❌ | Beschreibung |
| 2.1.3 Querverweise | ✅ / ❌ | Beschreibung |
| 2.1.4 Roter Faden | ✅ / ❌ | Beschreibung |
| 2.1.5 Formatierung | ✅ / ❌ | Beschreibung |
| 2.2.1 Sachliche Richtigkeit | ✅ / ❌ | Beschreibung |
| 2.2.2 Redundanzprüfung | ✅ / ❌ | Beschreibung |
| 2.2.3 Argumentation | ✅ / ❌ | Beschreibung |
| 2.2.4 Ausgewogenheit | ✅ / ❌ | Beschreibung |
| 2.3.1 Tippfehler und Grammatik | ✅ / ❌ | Beschreibung |
| 2.3.2 Terminologie | ✅ / ❌ | Beschreibung |
| 2.4.1 Vollständigkeit und Nummerierung | ✅ / ❌ | Beschreibung |
| 2.4.2 Formale Einheitlichkeit | ✅ / ❌ | Beschreibung |
| 2.4.3 Thematische Sektionierung | ✅ / ❌ | Beschreibung |
| 2.4.4 Aktualität und Belastbarkeit | ✅ / ❌ | Beschreibung |
| 2.4.5 URL-Prüfung (Stichprobe) | ✅ / ❌ | Beschreibung |
| 2.4.6 Zitatgenauigkeit | ✅ / ❌ | Beschreibung |
| 2.5 Versionskonsistenz | ✅ / ❌ | Beschreibung |
| 2.6 Automatisierte Prüfung | ✅ / ❌ | Beschreibung |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | §X.Y, Zeile Z | Beschreibung | Kritisch / Mittel / Gering |

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | Beschreibung | Was wurde geändert | ✅ |

### Nachprüfung

- validate.py nach Bereinigung: ✅ / ❌
- red_thread.py nach Bereinigung: ✅ / ❌

### Abschluss

- Alle Fehler behoben: Ja / Nein
- Neue Version: Y.0
- PDF erstellt: ✅ / ❌
- Word erstellt: ✅ / ❌
```

Jeder Block bleibt dauerhaft stehen. Die Historie wird nicht gelöscht.

---

## 4. Versionierung

### Wann wird eine neue Version vergeben?

- Nach jeder abgeschlossenen Validierung mit mindestens einem behobenen Fehler
- Bei inhaltlichen Ergänzungen oder strukturellen Änderungen

### Versionsformat

`X.0` — ganzzahlig, aufsteigend.

### Wo wird die Version eingetragen?

- Versionshinweis im Dokumentkopf
- Abschlusssatz am Dokumentende
- PDF/Word Footer (bei Neuerstellung)
- Abschlussblock in `Validierung-Ergebnisse.md`

---

## 5. Dateien

| Datei | Zweck |
|---|---|
| `Wolkenfrei.md` | Hauptdokument |
| `Validierung.md` | Dieses Dokument — Prüfprozess |
| `Validierung-Ergebnisse.md` | Protokoll aller Validierungen, Fehler und Bereinigungen |
| `validate.py` | Automatisierte Strukturprüfung |
| `red_thread.py` | Automatisierte Roter-Faden-Prüfung |
