# 16. Aufsichts- und Regulierungslandschaft: Wer den Rahmen setzt — und wer nicht durchsetzt

§1.2.2 dokumentiert das Vollzugsdefizit: Kein einziges Bußgeld gegen eine Gesundheitsinstitution wegen US-Cloud-Nutzung ist öffentlich bekannt. Dieses Kapitel zeigt, warum. Die regulatorische Zuständigkeit für Cloud und KI im Gesundheitswesen ist auf mehr als ein Dutzend Institutionen verteilt — keine davon deckt das Gesamtbild ab. Das CLOUD-Act-Problem fällt systematisch zwischen die Zuständigkeiten.

## 16.1 Wer ist zuständig — und wofür nicht

| Institution | Zuständigkeit im Kontext Cloud/KI | Was sie **nicht** prüft |
|---|---|---|
| **BfDI** (Bundesbeauftragter für den Datenschutz) | DSGVO-Aufsicht über Bundesbehörden; KI-Handreichung Dezember 2025 | Keine Fachaufsicht über GKVen oder Kliniken; keine Sanktionskompetenz gegen US-Anbieter |
| **16 Landesaufsichtsbehörden** | DSGVO-Aufsicht über Landesbehörden, Unikliniken, landesunmittelbare GKVen | Kein koordiniertes Enforcement; DSK-Beschlüsse nicht rechtsverbindlich; keine Jurisdiktionsprüfung |
| **BAS** (Bundesamt für Soziale Sicherung) | Rechts- und Fachaufsicht über bundesunmittelbare GKVen (TK, Barmer, DAK, AOK BV u.a.); Digitalausschuss seit 2020; Rundschreiben "Cloud-basierte IT-Lösungen in der Sozialversicherung" (2017) | Kein DSGVO-Enforcement — das bleibt beim BfDI; keine eigene öffentliche Cloud- oder KI-Positionierung; Rundschreiben veraltet (vor § 393 SGB V und vor CLOUD-Act-Debatte) |
| **BMG** (Bundesgesundheitsministerium) | Gesetzgebung: DigiG/§ 393 SGB V (2024), GDNG (2024), GeDIG (Entwurf 2026); Digitalisierungsstrategie | Reguliert Rahmenbedingungen, nicht Einzelfälle; § 393 adressiert IT-Sicherheit (C5), nicht Jurisdiktion; keine Anbieterbewertung |
| **gematik** | TI-Betrieb; Zulassung von TI-Komponenten, TI-Gateways, ePA-Anbietern; C5-Testat-Liste (INA-Portal); TI 2.0 Sicherheitsarchitektur (ZETA/Zero Trust) | Keine DSGVO-Aufsicht; keine Jurisdiktionsprüfung bei Zulassungen; TI-Gateway-Zulassung prüft Sicherheit, nicht CLOUD-Act-Exposition des Betreibers |
| **G-BA** (Gemeinsamer Bundesausschuss) | Höchstes Beschlussgremium der gemeinsamen Selbstverwaltung; DiGA-Aufnahme (BfArM zuständig); Richtlinien für Versorgung | Keine Cloud- oder KI-spezifische Regulierung; keine Datenschutzaufsicht |
| **BfArM** | DiGA-Zulassung; Datensicherheitsanforderungen (mit BSI) für digitale Gesundheitsanwendungen ab 01.01.2025 | Prüft Funktionstauglichkeit und Datensicherheit, nicht Cloud-Jurisdiktion des Herstellers |
| **BSI** | IT-Sicherheit: C5-Testat, C5:2026, BSI-TR Gesundheitsanwendungen; Souveränitätskriterien angekündigt (mit ANSSI, separates Dokument) | C5 prüft Informationssicherheit, **nicht** Jurisdiktion — das ist die dokumentierte Lücke aus §1.1 |
| **KBV** (Kassenärztliche Bundesvereinigung) | IT-Sicherheitsrichtlinie nach § 390 SGB V (verpflichtend ab Oktober 2025); Zertifizierung von IT-Dienstleistern für Praxen | Richtlinie adressiert IT-Sicherheit in Praxen, nicht Cloud-Anbieterjurisdiktion; keine KI-spezifischen Vorgaben |
| **DKG** (Deutsche Krankenhausgesellschaft) | Positionspapier "KI im Krankenhaus" (Oktober 2025): fordert Cloud-Betrieb für KI als Notwendigkeit; KHZG-2.0-Finanzierung | Interessenvertretung, keine Aufsicht; fordert regulatorische Klarstellung, setzt sie nicht selbst |
| **GKV-Spitzenverband** | Digitalstrategie (Dezember 2025): KI-gestützte ePA-Analyse, FDZ-Datennutzung; digitales Primärversorgungssystem | Interessenvertretung der Kassen; keine Aufsichtsfunktion; Cloud-Souveränität kein dokumentierter Schwerpunkt |
| **PKV-Verband** | Digitalisierungsstrategie für private Krankenversicherungen | Keine öffentliche Cloud- oder KI-Positionierung bekannt; PKV unterliegt nicht § 393 SGB V |
| **MD Bund** (Medizinischer Dienst) | Qualitätsprüfungen; KI-Grundregeln (MD Sachsen-Anhalt, 2025): nur geschlossene Systeme, keine kommerziellen KI-Modelle, abschließende Entscheidung beim Menschen | Keine Cloud-Regulierung; KI-Grundregeln nur intern; keine Aufsicht über andere Institutionen |

## 16.2 Datenschutzaufsicht — Flickenteppich bei Microsoft 365 / Azure

Die Positionierung aller deutschen Datenschutzaufsichtsbehörden zu Microsoft 365 / Azure (Stand April 2026):

Die Positionierung aller deutschen Datenschutzaufsichtsbehörden zu Microsoft 365 / Azure (Stand April 2026):

| Behörde | Zuständigkeit | Position Microsoft 365 / Azure | Tendenz |
|---|---|---|---|
| **BfDI** (Bund) | Bundesbehörden, bundesweite GKVen (BAS) | 2022: Rundschreiben an alle Bundesministerien mit Bedenken; kein förmliches Verbot | ⚠️ Kritisch, keine Sanktionen |
| **BAS** | Bundesunmittelbare GKVen (AOK Bund, Barmer, TK, DAK u.a.) | Keine eigene Microsoft-Positionierung öffentlich bekannt; orientiert sich an BfDI | ⚠️ Unklar |
| **Bayern BayLDA** (privat) | Private Unternehmen, GKVen mit Landesaufsicht | DSK-Gesamtbewertung 2022 "zu undifferenziert" — kein Verbot; Freistaat verhandelt Rahmenvertrag M365 für gesamte Verwaltung (Stand 2025) | 🟡 Pragmatisch, Einzelfallprüfung |
| **Bayern BayLfD** (öffentlich) | Landesbehörden, Unikliniken BY | Lehnte M365 an Schulen ab (2021); Einzelfallverbot auf Beschwerde; kein generelles Verbot | ⚠️ Kritisch, aber kein Generalverbot |
| **Baden-Württemberg LfDI** | Landesbehörden, Unikliniken BW | M365 2021 abgelehnt für Schulen; 2022 Ausstiegsgebot; digitaler Arbeitsplatz Lehrkräfte mit M365 gestartet April 2024 — faktische Kehrtwende | 🟡 Kritisch→pragmatisch |
| **Berlin BlnBDI** | Landesbehörden, Unikliniken BE | 2020: "nicht möglich"; Copilot an Berliner Schulen 2024 eingeführt ohne DSB-Einbindung (Tagesspiegel) — faktischer Widerspruch zur eigenen Position | ⚠️ Kritisch, Umsetzung widersprüchlich |
| **Brandenburg LDA** | Landesbehörden, Unikliniken BB | Beteiligt an EDSA-Kontrollaktion 2024; keine spezifische M365-Positionierung öffentlich bekannt | ⚠️ Unklar |
| **Bremen LfDI** | Landesbehörden | 2023/24 Tätigkeitsbericht: iCloud-Nutzung als rechtswidrig eingestuft; M365 mit Bedenken | ⚠️ Kritisch |
| **Hamburg HmbBfDI** | Landesbehörden, Polizei | Signalisierte 2024 Abweichung von Niedersachsen-Modell; Microsoft Teams für Polizei Hamburg trotzdem im Einsatz | 🔴 Kritisch, aber kein Verbot durchgesetzt |
| **Hessen HBDI** | Landesbehörden, Unikliniken HE | Nov. 2025: 137-seitiger Bericht — "Microsoft 365 kann datenschutzkonform genutzt werden" unter Bedingungen; Verhandlungen mit Microsoft direkt | 🟢 Positiv (mit Auflagen) |
| **Mecklenburg-Vorpommern LfDI** | Landesbehörden | Beteiligt an EDSA-Kontrollaktion 2024; keine eigene M365-Positionierung öffentlich bekannt | ⚠️ Unklar |
| **Niedersachsen LfD** | Landesbehörden, Unikliniken NI | April/Mai 2024: Microsoft Teams Vereinbarung als "akzeptabel" bewertet; Rollout 13.500 Arbeitsplätze | 🟢 Positiv (Vorreiter) |
| **NRW LDI** | Landesbehörden, Unikliniken NW, KVNO/KVWL | Mai 2024: "Keine Informationen vor, die Überarbeitung bieten würden" — kritisch zu neuem Outlook; kein Verbot | ⚠️ Kritisch, kein Verbot |
| **Rheinland-Pfalz LfDI** | Landesbehörden, Unikliniken RP | Beteiligt an EDSA-Kontrollaktion 2024; keine eigene M365-Positionierung öffentlich bekannt | ⚠️ Unklar |
| **Saarland LfDI** | Landesbehörden | DSK-Gesamtbewertung 2022 nicht geteilt; signalisierte 2024 Abweichung vom Niedersachsen-Modell | 🟡 Pragmatisch |
| **Sachsen DSB** | Landesbehörden, Unikliniken SN (UKL Dresden!) | Keine spezifische M365-Positionierung öffentlich bekannt | ⚠️ Unklar |
| **Sachsen-Anhalt LfDI** | Landesbehörden, Unikliniken SA | Keine spezifische M365-Positionierung öffentlich bekannt | ⚠️ Unklar |
| **Schleswig-Holstein ULD** | Landesbehörden | Mai 2024: "Teile die Ansicht des EDPS, dass Zwecke nicht transparent genug sind"; bisher keine geänderte Bewertung; SH setzt parallel auf Open-Source-Stack | 🔴 Kritisch |
| **Thüringen TLfDI** | Landesbehörden, Unikliniken TH | Keine spezifische M365-Positionierung öffentlich bekannt | ⚠️ Unklar |
| **Vergabekammer München** | Vergaberechtlich (nicht Datenschutz) | Feb. 2023: Pauschaler Azure-Ausschluss unzulässig — Einzelfallprüfung geboten | 🟡 Pragmatisch (vergaberechtlich) |

**Bedeutung für das Gesundheitswesen:** Unikliniken unterstehen ihrer Landesaufsicht — ein Klinikum in Hessen oder Bayern hat strukturell mehr Spielraum für Azure als eines in Hamburg oder Schleswig-Holstein. GKVen unterstehen je nach Kassengröße dem BAS oder Landesaufsichten. Der BAS hat keine eigene öffentliche Microsoft-Positionierung — bundesunmittelbare Kassen wie Barmer oder TK operieren faktisch in einem Vakuum.

**Das Fazit:** Wer bei der "richtigen" Aufsichtsbehörde sitzt, bekommt Azure genehmigt oder zumindest toleriert. Wer Pech hat, bekommt eine Mahnung ohne Konsequenz. **STACKIT und EU-souveräne Alternativen werden primär dort gewählt, wo die Aufsicht Druck macht (Hamburg, Schleswig-Holstein) oder die Ausschreibungsgestaltung es erzwingt.** Das Enforcement-Gap ist das eigentliche strukturelle Problem: Die Regelungslücke existiert — aber sie hat keinen einheitlichen Preis.

## 16.3 DSK- und Landesaufsichts-Hinweise zu Cloud und KI im Gesundheitswesen

Die Microsoft-365-Tabelle bildet nur eine Dimension ab: die Haltung zu einem bestimmten Produkt. Parallel dazu haben DSK und einzelne Landesaufsichtsbehörden zwischen 2023 und 2026 konkrete Orientierungshilfen, Beschlüsse und Prüfaktionen veröffentlicht, die **Cloud-Nutzung für Gesundheitsdaten** und **KI-Anwendungen mit Cloud-Infrastruktur** direkt adressieren. Für Gesundheitsinstitutionen sind diese Dokumente handlungsrelevanter — sie definieren, was Aufsichtsbehörden bei einer Prüfung tatsächlich verlangen.

| Dokument | Herausgeber | Datum | Kernaussage für Gesundheitsinstitutionen |
|---|---|---|---|
| **Positionspapier cloudbasierte digitale Gesundheitsanwendungen** | DSK | 06.11.2023 | Cloud-Funktionen standardmäßig deaktiviert (Privacy by Default); Nutzung ohne Benutzerkonto möglich, es sei denn Cloud ist therapeutisch zwingend; BSI-TR "Anforderungen an Anwendungen im Gesundheitswesen" als Maßstab |
| **Orientierungshilfe KI-Systeme** (TOM für Entwicklung und Betrieb) | DSK (KI-Taskforce + AG KI) | Mai/Juni 2025 | Erste koordinierte KI-Orientierungshilfe aller Aufsichtsbehörden; Risikoanalyse für LLMs als Kernstück; auch pseudonymisierte Eingaben = personenbezogene Daten; DSFA nach Art. 35 DSGVO erforderlich; 3 Phasen: Konzeption → Implementierung → Betrieb |
| **Entschließung Confidential Cloud Computing** | DSK | 16.06.2025 | Cloud-Betreiber behalten "umfassenden physischen und technischen Zugriff" — Marketingversprechen halten "regelmäßig einer Prüfung nicht stand"; Vertraulichkeit nur gegeben wenn Betreiber **keinerlei** Zugriff auf Entschlüsselungsschlüssel hat; Confidential Computing = ein Baustein, kein Allheilmittel |
| **Positionspapier Terminverwaltung Heilberufspraxen** | DSK | 16.06.2025 | Patientenstammdaten dürfen nicht pauschal an Cloud-Termindienstleister übermittelt werden; nur Minimum für konkreten Termin; zeitnahe Löschung |
| **KI-Handreichung Bundesverwaltung** ("KI in Behörden — Datenschutz von Anfang an mitdenken") | BfDI | 22.12.2025 | Leitfaden für Bundesbehörden inkl. bundesunmittelbare GKVen; Fokus LLMs und cloud-basierte KI-Dienste; Datenschutz ab Konzeptionsphase |
| **Diskussionspapier "Rechtsgrundlagen Datenschutz + KI"** (v2.0) | LfDI Baden-Württemberg | 17.10.2024 | Rechtsgrundlage für jede KI-Phase separat erforderlich; cloud-basierte KI = eigene Rechtsgrundlage wenn Nutzerdaten Modell verbessern; EHDS-VO für sekundäre Gesundheitsdatennutzung referenziert |
| **Checkliste "Datenschutz und KI"** + Flyer "Next-Level-Bausteine für KI" | BayLDA | 2024/2025 | AI-as-a-Service = Auftragsverarbeitung (Art. 28 DSGVO); Drittlandstransfer bei US-Anbietern prüfen; Halluzinationen und Bias in DSFA einbeziehen |
| **Aktive KI-Prüfung im Gesundheitswesen** (Auskunftsersuchen nach Art. 58 Abs. 1 lit. a DSGVO) | LfDI Rheinland-Pfalz | März 2026 | **Erste dokumentierte Enforcement-Aktion KI + Gesundheitswesen:** Prüft KI-Telefonanlagen, KI-Dokumentenmanagement, KI-Websites in Arztpraxen; verlangt vollständiges Verzeichnis aller KI-Tools inkl. Einsatzzweck und zugrundeliegende Modelle; fehlende Dokumentation = Verstoß gegen Rechenschaftspflicht |
| **Positionspapier "Kriterien für Souveräne Clouds"** | DSK | 11.05.2023 | Souveräne Cloud nur wenn Verantwortlicher Datenschutzpflichten "wirksam, überprüfbar und dauerhaft" erfüllen kann; Drittlandszugriffsrisiko muss **ausgeschlossen** sein; Open-Source-Basis empfohlen; offene Standards und Exportmöglichkeiten |
| **Empfehlungen zu KI-Anbietern außerhalb der EU** (inkl. koordiniertes Verfahren gegen DeepSeek) | LfDI Baden-Württemberg | 2025 | Warnung vor KI-Anbietern ohne Art.-27-DSGVO-Vertreter in der EU; koordinierte Verfahren gegen DeepSeek eingeleitet; Drittstaatentransfer bei KI-as-a-Service systematisch prüfen |
| **Orientierungshilfe Gesundheitsdatennutzungsgesetz (GDNG)** | BayLfD | Januar 2026 | Orientierungshilfe zu §§ 5 und 6 GDNG und EHDS; Muster-Einwilligung nach § 6; Living Document mit regelmäßigen Updates |
| **Leitfaden Datenschutz in der medizinischen Forschung** (mit DGIM) | HBDI | Dezember 2025 | Vier konkrete Use Cases aus der medizinischen Forschung; Pseudonymisierung über Treuhandstelle; föderierte Datenmodelle; Living Document |
| **CEF Cloud-Nutzung öffentlicher Stellen** | EDPB (7 deutsche Landesbehörden beteiligt) | 2023 (Bericht) | Koordinierte Prüfung der Cloud-Nutzung durch öffentliche Stellen inkl. Gesundheitswesen; nur 32 von 86 geprüften Stellen hatten vor Cloud-Einsatz eine DSFA durchgeführt; Ergebnisbericht mit Empfehlungen zu Auftragsverarbeitung und Drittlandstransfer |

**Was das für Gesundheitsinstitutionen bedeutet:**

1. **Cloud-Gesundheitsanwendungen** unterliegen seit dem DSK-Beschluss November 2023 konkreten Anforderungen an Privacy by Default — Cloud-Funktionen müssen deaktivierbar sein. Jede GKV oder Klinik, die eine Cloud-basierte Gesundheitsanwendung einführt (z.B. DiGA-ähnliche Apps, Patientenportale), muss diese Anforderungen nachweisen können.

2. **KI-Anwendungen** mit Cloud-Backend erfordern seit der DSK-Orientierungshilfe Mai/Juni 2025 eine eigene DSFA — insbesondere für LLMs. Das betrifft direkt die KI-Anwendungsfälle aus §7.5: Arztbrief-Generierung, Transkription, Kodierung. Wer Azure OpenAI, Google Gemini oder AWS Bedrock für Gesundheitsdaten nutzt, muss eine DSFA vorlegen, die explizit die Klartextverarbeitung und den Drittlandstransfer adressiert.

3. **Confidential Cloud Computing** schützt laut DSK-Entschließung Juni 2025 **nicht** vor Provider-Zugriff — das bestätigt die CLOUD-Act-Analyse aus §1 und §13: Technische Maßnahmen allein lösen das Jurisdiktionsproblem nicht.

4. **Rheinland-Pfalz macht ernst:** Die Art.-58-Auskunftsersuchen des LfDI Rheinland-Pfalz ab März 2026 sind die erste dokumentierte anlassbezogene Prüfung von KI im Gesundheitswesen durch eine Landesaufsicht. Gesundheitsinstitutionen müssen ein vollständiges Verzeichnis aller eingesetzten KI-Tools vorhalten — inklusive der zugrundeliegenden Modelle und deren Infrastruktur. Wer nicht dokumentieren kann, welches Modell seine Arztbrief-KI antreibt und wo es läuft, riskiert einen Rechenschaftspflicht-Verstoß nach Art. 5 Abs. 2 DSGVO.

5. **BfDI-Handreichung** (Dezember 2025) gilt für alle bundesunmittelbaren Stellen — das schließt die großen bundesunmittelbaren GKVen (Barmer, TK, DAK, AOK-Bundesverband) ein, die bislang im "Vakuum" operierten (s.o.). Für diese Kassen ist die BfDI-Handreichung die erste konkrete Erwartungshaltung des Bundesbeauftragten zu KI und Cloud.

## 16.4 Das Gesamtbild — warum niemand das CLOUD-Act-Problem "besitzt"

Die Tabelle in §16.1 zeigt das strukturelle Problem: Die CLOUD-Act-Exposition von Gesundheitsdaten fällt zwischen alle Zuständigkeiten.

**Das BSI** prüft Informationssicherheit — nicht Jurisdiktion. C5 zertifiziert Azure, obwohl Azure dem CLOUD Act unterliegt. Das BSI weiß das, hat Souveränitätskriterien deshalb als separates Dokument angekündigt, aber noch nicht veröffentlicht.

**Das BMG** hat mit § 393 SGB V die Cloud-Nutzung erlaubt und C5 als Mindeststandard festgelegt — ohne die Jurisdiktionsfrage zu adressieren. Das GeDIG (Entwurf 2026) erweitert den Datenpool (ePA-Ausbau, FDZ-Ausleitung), adressiert aber ebenfalls nicht, auf welcher Infrastruktur diese Daten verarbeitet werden dürfen.

**Das BAS** beaufsichtigt die bundesunmittelbaren GKVen (TK, Barmer, DAK — zusammen > 30 Mio. Versicherte), hat aber keine eigene öffentliche Cloud- oder KI-Positionierung. Das Rundschreiben zu Cloud-IT-Lösungen stammt von 2017 — vor § 393 SGB V, vor der CLOUD-Act-Debatte, vor KI im Gesundheitswesen. Der BAS-Digitalausschuss berät Kassen zu Digitalisierungsfragen, aber eine CLOUD-Act-Bewertung gehört nicht zum dokumentierten Prüfprogramm.

**Die gematik** vergibt TI-Gateway-Zulassungen, die bestimmen, über welchen Anbieter Praxen und Kliniken künftig ihre TI-Anbindung beziehen. Ob ein TI-Gateway-Betreiber dem CLOUD Act unterliegt, ist kein Zulassungskriterium. Die TI-2.0-Architektur (ZETA/Zero Trust, seit Dezember 2025 quelloffen auf GitHub) ist ein Sicherheitskonzept — kein Souveränitätskonzept.

**Die Datenschutzaufsichtsbehörden** könnten das Problem adressieren — und tun es punktuell (Rheinland-Pfalz März 2026). Aber DSK-Beschlüsse sind nicht rechtsverbindlich, Prüfungen erfolgen anlassbezogen, und die 16 Landesaufsichten plus BfDI kommen zu unterschiedlichen Ergebnissen (§16.2). Die DSK hat mit dem Positionspapier "Kriterien für Souveräne Clouds" (Mai 2023) klar formuliert, dass Drittlandszugriffsrisiken **ausgeschlossen** sein müssen — aber dieses Papier hat keine Bindungswirkung und wird in Vergabeverfahren regelmäßig nicht herangezogen.

**Die Selbstverwaltung** (KBV, DKG, GKV-Spitzenverband) vertritt Interessen, hat aber keine Aufsichtsfunktion. Die DKG fordert in ihrem KI-Positionspapier (Oktober 2025) explizit Cloud-Betrieb als Notwendigkeit für KI — ohne die Jurisdiktionsfrage zu stellen. Der GKV-Spitzenverband fordert in seiner Digitalstrategie (Dezember 2025) KI-gestützte ePA-Analyse — ohne Cloud-Souveränität als Anforderung zu definieren.

**Das Ergebnis:** Jede Institution erfüllt ihren Auftrag korrekt — aber niemand ist dafür zuständig, die Frage zu stellen: "Unterliegt der Cloud-Anbieter, bei dem wir Gesundheitsdaten von 74 Millionen GKV-Versicherten verarbeiten, einer US-Herausgabepflicht?" Das BSI sagt: "Nicht mein Prüfgegenstand." Das BMG sagt: "C5 regelt die Sicherheit." Das BAS sagt: nichts Öffentliches. Die gematik sagt: "Wir prüfen Sicherheit, nicht Jurisdiktion." Die Datenschutzaufsicht sagt: "Problematisch" — und verhängt kein Bußgeld.

Dieses Muster — regulatorische Vollständigkeit bei gleichzeitiger Zuständigkeitslücke für das Kernrisiko — ist der institutionelle Grund für das Vollzugsdefizit aus §1.2.2. Es ist kein Versagen einzelner Behörden, sondern ein Systemdesign, das die CLOUD-Act-Frage strukturell unsichtbar macht.


---
