# 3. Die vier US-Zugriffsebenen im Detail

Es gibt nicht einen, sondern **vier rechtlich verschiedene Wege** für US-Behörden auf Daten zuzugreifen, die bei US-kontrollierten Anbietern liegen. Sie unterscheiden sich erheblich in Voraussetzungen, Hürden und Relevanz für Gesundheitsdaten:

| Rechtsgrundlage | Akteur | Voraussetzungen | Hürde | Relevanz Health |
|---|---|---|---|---|
| **CLOUD Act** (18 U.S.C. § 2713) | FBI, DOJ | Richterlicher Herausgabebeschluss + hinreichender Verdacht auf konkrete Straftat | Mittel | Strafermittlungen gegen Personen/Institutionen |
| **FISA § 702** (Foreign Intelligence Surveillance Act — US-Gesetz zur nachrichtendienstlichen Massenüberwachung) | NSA, CIA, FBI | Keine Einzelfallprüfung. Pauschale Jahreszertifizierung durch geheimen FISC. RISAA 2024 (Reforming Intelligence and Securing America Act) erweiterte Anbieter-Definition massiv. Auslaufdatum: **20. April 2026** — Verlängerung zum Redaktionsschluss offen. | Niedrig | Systematische Erfassung — betrifft potenziell alle US-Server-Daten |
| **National Security Letter** | FBI | Kein Richter. Kein Verdacht. Schweigegebot für Anbieter. Gilt für Metadaten. | Minimal | Metadaten über Arzt-Patienten-Kontakte, Verbindungsdaten |
| **Grenzkontrolle** (Grenzkontrollen-Ausnahme) | CBP | Kein Herausgabebeschluss. Kein Verdacht. Physisches Gerät an US-Grenze. | Null | Relevant für Mitarbeitergeräte bei US-Dienstreisen |

## 3.1 CLOUD Act — Strafverfolgung mit richterlicher Kontrolle

Der CLOUD Act (18 U.S.C. § 2713, in Kraft seit März 2018) ist das bekannteste Instrument — aber nicht das gefährlichste. Er verpflichtet US-Provider zur Herausgabe von Daten, die sich "under the provider's possession, custody, or control" befinden, unabhängig vom Serverstandort.

**Was ihn von den anderen Zugriffsebenen unterscheidet:** Für Inhaltsdaten (E-Mails, Dateien, Kommunikationsinhalte) ist ein richterlicher Herausgabebeschluss erforderlich — mit hinreichendem Tatverdacht auf eine konkrete Straftat. Der Provider kann durch einen Widerspruch (motion to quash) widersprechen, wenn der Zugriff mit dem Recht des Landes kollidiert, in dem die Daten liegen. Ein US-Gericht entscheidet dann nach US-Maßstäben über den Konflikt — ein Verfahren, das strukturell die Interessen der USA priorisiert, aber immerhin juristisch anfechtbar ist.

**Für Metadaten (Verbindungsdaten, IP-Adressen, Zeitstempel)** genügt eine Gerichtsbeschluss mit abgesenkten Anforderungen — kein voller Herausgabebeschluss nötig. Für Abonnentendaten (Name, Adresse, Zahlungsdaten) reicht in vielen Fällen eine behördliche Auskunftsanordnung ohne Richterbeteiligung.

**Relevanz für Gesundheitsdaten:** Der CLOUD Act trifft typischerweise konkrete Strafverfolgungsszenarien — wenn eine Ermittlung gegen eine Person oder Institution läuft, die Daten bei einem US-Provider verwaltet. Für eine GKV mit 5 Millionen Versicherten, die Kernabrechnungsdaten bei Azure hostet, ist das Risiko: bei Ermittlungen gegen einen Leistungserbringer, Arzt oder Versicherten könnten umfangreiche Gesundheitsdaten im Rahmen der Ermittlung mit abgerufen werden, ohne dass die GKV davon erfährt.

**Der Sanktionslisten-Automatismus:** Besonders greifbar wird das Risiko bei US-Sanktions- und Terrorlisten. Wenn eine in Deutschland lebende Person oder eine politische Gruppierung auf eine solche Liste gesetzt wird — etwa auf die Specially Designated Nationals (SDN)-Liste des Office of Foreign Assets Control (OFAC) —, sind alle US-kontrollierten Unternehmen unmittelbar und ohne weitere richterliche Anordnung verpflichtet, sämtliche Daten zu dieser Person einzufrieren und auf Anfrage herauszugeben. Das betrifft nicht nur Bankkonten und Finanzdaten, sondern alle Daten "under the provider's possession, custody, or control" — einschließlich Gesundheitsdaten in Cloud-Systemen. Microsoft, AWS, Google und Oracle können dem nicht widersprechen; ein Verstoß gegen US-Sanktionsrecht wird strafrechtlich verfolgt. Für die Gesundheitsinstitution, deren Daten betroffen sind, entsteht ein Datenschutzvorfall, von dem sie in der Regel nicht einmal erfährt.

Dass das keine Theorie ist, zeigen zwei dokumentierte Fälle: Die USA haben 2019/2020 unter dem PEESCA-Gesetz Sanktionen gegen europäische Unternehmen und namentlich benannte Mitarbeiter des Nord-Stream-2-Projekts verhängt — darunter deutsche Staatsbürger —, die an einem legalen europäischen Infrastrukturprojekt beteiligt waren. Im Dezember 2025 setzte US-Außenminister Rubio die beiden Geschäftsführerinnen der deutschen gemeinnützigen Organisation HateAid auf die Sanktionsliste — weil sie sich für die Durchsetzung des europäischen Digital Services Act auf US-Plattformen einsetzen. Bei sanktionierten ICC-Richtern wurde der Cloud-Zugang bereits abgeschaltet: Microsoft, Amazon, Gmail, Visa, Mastercard, PayPal — alles gesperrt. Die Einstufungskriterien lagen in allen Fällen ausschließlich bei US-Behörden — ohne europäische Beteiligung, ohne richterliche Prüfung, ohne Rechtsschutz für die Betroffenen.

## 3.2 FISA § 702 und RISAA 2024 — die unterschätzte Gefahr

FISA § 702 ist das strukturell riskanteste Instrument für Gesundheitsdaten — weil es keine Einzelfallprüfung erfordert und damit massenweise Daten erfassen kann.

Der Reforming Intelligence and Securing America Act (RISAA, April 2024) verlängerte FISA § 702 und **erweiterte gleichzeitig den Anbieter-Begriff massiv**. Für Gesundheitsdaten bedeutet das: Jedes US-Unternehmen, das Kommunikation oder Daten von Nicht-US-Bürgern verarbeitet, kann unter FISA § 702 zur Herausgabe verpflichtet werden — ohne richterliche Einzelfallprüfung, ohne Information der Betroffenen.

**Wie FISA § 702 funktioniert:** Statt eines Einzelfall-Herausgabebeschlusses genehmigt der geheime Foreign Intelligence Surveillance Court (FISC) einmal jährlich ein pauschales Überwachungsprogramm. Die NSA, CIA und das FBI können dann im Rahmen dieses Programms Daten von Nicht-US-Personen bei US-Providern abfragen — ohne dass der Provider im Einzelfall widersprechen könnte, ohne Benachrichtigung der Betroffenen, ohne nachträgliche gerichtliche Kontrolle für Nicht-US-Bürger.

**RISAA 2024 — die stille Ausweitung:** Die RISAA-Novelle erweiterte die Definition von "Electronic Communication Service Provider" drastisch: Nun können auch Unternehmen, die lediglich Zugang zu Netzwerkinfrastruktur haben — Rechenzentren, Server-Co-Location-Betreiber, Cloud-Infrastruktur — zur Herausgabe verpflichtet werden. Das EFF bezeichnete dies als "Make Everyone a Spy Bill". Für Gesundheits-IT bedeutet das: Auch Dienstleister, die nicht primär Kommunikationsdienste anbieten, aber US-kontrollierte Server betreiben, können erfasst sein.

**Auslaufdatum 20. April 2026 (FISA-Auslaufdatum):** FISA § 702 läuft ohne erneute Verlängerung aus. Zum Redaktionsschluss läuft die Verlängerungsdebatte — Trump unterstützt eine saubere Verlängerung ohne Reformen, eine Reform-Koalition (EFF, Brennan Center, 130+ Organisationen) fordert richterliche Genehmigungspflicht für US-Personen-Abfragen und Schließung des Datenhändler-Lückes. Ein Ablauf würde US-Behördenzugriff temporär blockieren, aber keine strukturelle DSGVO-Lösung schaffen.

## 3.3 National Security Letter — kein Richter, kein Verdacht, Schweigegebot

National Security Letters (NSL, 18 U.S.C. § 2709 und verwandte Statuten) sind behördliche Auskunftsanordnungen, die das FBI ohne richterliche Genehmigung und ohne Verdachtsnachweis ausstellen kann. Sie sind das am wenigsten diskutierte, aber operativ bedeutsame Instrument.

**Was NSLs erfassen:** Primär Metadaten — Verbindungsdaten, E-Mail-Header (nicht Inhalte), Abonnentendaten, IP-Adressen, Zeitstempel von Transaktionen. Für Gesundheitsdaten relevant: Wer hat wann mit welchem Arzt, welcher Klinik, welcher GKV kommuniziert? Welche IP-Adressen haben wann auf welche Gesundheitsportale zugegriffen? Diese Metadaten können im Gesundheitskontext hochsensibel sein — sie erlauben Rückschlüsse auf Diagnosen, Behandlungen und Lebensumstände.

**Das Schweigegebot (Schweigeverfügung):** Provider, die einen NSL erhalten, dürfen die betroffene Person oder Institution in der Regel nicht informieren. Eine automatische, zeitlich unbegrenzte Geheimhaltungspflicht war der Standard — seit einem Urteil des Second Circuit (2013) können Provider dieses Schweigegebot gerichtlich anfechten, aber der Anfechtungsprozess ist langwierig und der Ausgang unsicher.

**HIPAA-Schnittstelle:** US-amerikanische Gesundheitsorganisationen (Krankenhäuser, Versicherungen, Pharmaanbieter) können unter der HIPAA National Security Exception ohne Gerichtsbeschluss Gesundheitsdaten an Bundesbehörden für Geheimdienstzwecke weitergeben — freiwillig, ohne Anfrage der Behörde, ohne Benachrichtigung der Patienten. Diese Exception ist für europäische GKV-Daten nicht direkt anwendbar — aber wenn ein US-Provider beteiligt ist, greift die NSL-Logik.

**Praktische Bedeutung:** Das FBI hat zwischen Dezember 2024 und November 2025 laut offiziellen Berichten 7.413 FISA-Abfragen von US-Personendaten durchgeführt — ein Anstieg von über einem Drittel gegenüber dem Vorjahreszeitraum. NSL-Zahlen werden weniger transparent veröffentlicht, liegen aber im Bereich von mehreren tausend pro Jahr.

## 3.4 CBP-Grenzkontrolle — physischer Gerätezugriff ohne Beschluss

Die Grenzkontrollen-Ausnahme (Grenzkontrollen-Ausnahme) ist der einzige Zugriffsweg, der keinerlei rechtliche Hürde kennt — kein Richter, kein Verdacht, keine Rechtfertigung. Sie betrifft Mitarbeitende mit Zugang zu sensiblen Gesundheitssystemen bei Reisen in die USA.

**Rechtsgrundlage:** US Customs and Border Protection (CBP) hat nach der Grenzkontrollen-Ausnahme das Recht, alle Geräte an US-Grenzen und internationalen Flughäfen ohne Herausgabebeschluss und ohne konkreten Verdacht zu durchsuchen. Grundlagendokument: CBP Directive No. 3340-049B.

**Unterschied Basisdurchsuchung vs. Erweiterte Durchsuchung (Basic Search vs. Advanced Search):**
- **Basisdurchsuchung** (Basic Search — manuelle Durchsicht): Ohne jeden Verdacht zulässig. Jedes Gericht bisher einig. 2024: über 42.000 Basisdurchsuchungen durchgeführt.
- **Erweiterte Durchsuchung** (Advanced Search — forensische Kopie des Geräteinhalts): CBP-Direktive verlangt hinreichenden Verdacht — aber die Umsetzung ist circuit-abhängig und uneinheitlich. Der 11. Circuit erlaubt Erweiterte Durchsuchungen ohne jede Begründung. Der 9. Circuit verlangt zumindest hinreichenden Verdacht. Kein bindender Supreme-Court-Entscheid bisher.

**Aktuelle Entwicklung:** Die Zahl warrantloser Gerätedurchsuchungen hat sich zwischen 2015 und 2024 mehr als verfünffacht — von ~8.500 auf über 47.000 jährlich. 2025 verzeichnet das dritte Quartal mit 14.899 Durchsuchungen einen absoluten Quartalsrekord. Eine Zivilklage (Pacific Legal Foundation, Dezember 2025) fordert ein Herausgabebeschluss-Erfordernis; der Fall ist beim D.C. District Court anhängig.

**Relevanz für Gesundheits-IT-Personal:** Mitarbeitende von Gesundheitsinstitutionen mit VPN-Zugängen, SSH-Keys oder App-Zugriffen auf Kernsysteme sind bei US-Dienstreisen exponiert. CBP kann physische Geräte beschlagnahmen, forensisch kopieren und den Inhalt an andere Bundesbehörden weitergeben — ohne dass die betroffene Person oder ihre Organisation zeitnah informiert wird. Die kopierten Daten bleiben bis zu 75 Tage in CBP-Systemen und können innerhalb der US-Bundesbehörden geteilt werden.

---
