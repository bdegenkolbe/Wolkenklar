# 16. DSGVO-Handlungsempfehlungen

## 16.1 Sofortmaßnahmen — Priorität hoch

| # | Maßnahme | Was konkret zu tun ist |
|---|---|---|
| **1** | Anbieter-Kontrollanalyse | (a) US-Börsennotierung? (b) US-Muttergesellschaft? (c) US-Niederlassung — auch Tochter oder Schwester? Wenn eine Frage Ja: CLOUD-Act-Risiko real — unabhängig von Serverstandort, AVV und SCCs. |
| **2** | Datenklassifizierung | Klasse 1 (ePA, Diagnosedaten, Medikation) → Full-Isolation-Anbieter oder Operator-Modell mit BSI CPR. Klasse 2 (interne Kommunikation, Analytics) → EU-Anbieter akzeptabel. Klasse 3 (öffentliche Daten) → keine Einschränkung. |
| **3** | C5-Testat neu einordnen | Auch C5:2026 (April 2026, 168 Kriterien) belegt **technische Sicherheit**, nicht rechtliche Souveränität. Azure hat C5 und unterliegt dem CLOUD Act. plusserver/STACKIT haben C5 und unterliegen ihm strukturell nicht. Delos Cloud hat BSI Cloud Platform Requirements — strenger als C5. BSI und ANSSI haben im November 2025 gemeinsame Souveränitätskriterien angekündigt — bis zu deren Veröffentlichung bleibt C5 allein kein Souveränitätsnachweis. |
| **4** | DPF nicht als Schutzschild | Das Data Privacy Framework basiert auf einem Präsidialerlass. PCLOB-Aufsicht ausgehöhlt seit Jan. 2025. Schrems III läuft. Keine Infrastrukturentscheidungen auf DPF-Dauerhaftigkeit bauen. |
| **5** | Operator-Modell prüfen | Für Organisationen tief in Microsoft 365 oder Azure integriert: Delos Cloud GmbH (SAP-Tochter) als souveräner Betreiber von Azure-Technologie prüfen. BSI Cloud Platform Requirements erfüllt, VS-NfD-fähig. Preisaufschlag: +15% auf Microsoft-Listenpreise. |

## 16.2 Das Vier-Stufen-Modell — welche Stufe für welchen Workload

Das entscheidende Planungswerkzeug ist nicht mehr die binäre Frage "US-Hyperscaler oder nicht" — sondern die Einordnung jedes Workloads in das Souveränitätsspektrum:

**Stufe 1 — Vollständige Abschottung (Full Isolation)**
Kein US-Technologieanteil, kein US-Eigentümer, kein US-Betrieb. Maximale rechtliche Souveränität.

Anbieter: plusserver, EWERK Leipzig (DE); 3DS Outscale, Cloud Temple (FR); STACKIT (mit Vorbehalt Lidl-US-Schwester)

Geeignet für: ePA-Kerndaten, KRITIS-Systeme, VS-NfD-Infrastruktur, GKV-Kernabrechnungssysteme, genetische Daten, psychiatrische Diagnostik — alles mit höchstem Schutzbedarf nach § 393 SGB V.

Vollständiger Technik-Stack (alle Komponenten heute produktionsreif):

| Funktion | US-Stack (ersetzt) | EU-Stack (Ersatz) |
|---|---|---|
| Office-Suite | Microsoft 365 / Office | Euro-Office, Nextcloud Hub, Office.eu |
| E-Mail / Kalender | Exchange Online / Outlook | Open-Xchange + Thunderbird |
| Dokumentenmanagement | SharePoint Online | Nextcloud, OpenCloud, GoFAST |
| Video / Chat | Microsoft Teams | Jitsi, OpenTalk, Matrix/Element |
| Identity / SSO | Azure Active Directory | Keycloak, Univention Corporate Server |
| Cloud-Infrastruktur | Azure Compute / Storage | STACKIT, plusserver, Hetzner (EU-RZ) |
| Objektspeicher | Azure Blob Storage | MinIO, Ceph, STACKIT Object Storage |
| Datenbank | Azure SQL / CosmosDB | PostgreSQL, MariaDB |
| Container | Azure Kubernetes Service | Kubernetes (self-managed) |
| KI-Inferenz | Azure OpenAI / Copilot | vLLM + Mistral (lokal / STACKIT) |
| Analytics / BI | Power BI / Fabric | Metabase, Apache Superset, Grafana |
| CI/CD | Azure DevOps / GitHub | GitLab (self-hosted) |
| Logging / SIEM | Azure Monitor / Sentinel | Grafana + Loki + OpenSearch / Wazuh |

**Praxisbeleg:** Schleswig-Holstein betreibt diesen Stack für 30.000 Mitarbeitende — mit €15 Millionen jährlichen Einsparungen bei einmalig €9 Millionen Investition. Engpass ist nicht Technologie, sondern Betriebspersonal und Fachverfahren-Integration.

**Stufe 2 — Operator-Modell**
EU-Rechtsperson als Eigentümer und Betreiber, US-Technologie als lizenzierter Lieferant ohne Datenzugang. Operativer Ausschluss von US-Zugriff, strukturelle Technologieabhängigkeit bleibt.

Deutschland: Delos Cloud GmbH (SAP × Microsoft Azure) — BSI Cloud Platform Requirements, VS-NfD-fähig, deutsches Personal, BSI prüft alle Updates. Betrieb durch Arvato Systems. Preis: +15% auf Microsoft-Listenpreise.

Frankreich: S3NS PREMI3NS (Thales × Google Cloud) — SecNumCloud 3.2, Quarantänezone für alle Google-Updates, ANSSI-validierte CLOUD-Act-Immunität. Referenzkunden: EDF, MGEN, Club Med.

Geeignet für: Organisationen, die nicht aus Microsoft 365 / SAP migrieren können; Kliniken mit tiefer M365-Integration; Verwaltungen; regulierte Industrien, die Azure-Service-Breite benötigen — aber keine direkten US-Hyperscaler-Verträge mehr wollen.

Nicht geeignet für: Workloads, die vollständige Unabhängigkeit vom US-Technologiestack erfordern (Verteidigung, nachrichtendienstliche Infrastruktur, höchste Geheimschutzklassen).

**Stufe 3 — Hyperscaler Sovereign Region**
US-Eigentümer und US-Technologie, aber physisch und logisch getrennte EU-Infrastruktur mit EU-Personal und Residency-Garantien. Kein echter CLOUD-Act-Schutz — der Anbieter bleibt US-Rechtsperson.

Anbieter: AWS European Sovereign Cloud (Brandenburg), Azure EU Data Boundary, Google Workspace DE

Geeignet für: Workloads ohne personenbezogene Gesundheitsdaten, globale Entwicklungsumgebungen, öffentliche Webpräsenzen, unkritische Collaboration-Tools.

Nicht geeignet für: Gesundheitsdaten, KRITIS-Infrastruktur, regulierte Daten nach § 393 SGB V.

**Stufe 4 — Standard US-Hyperscaler (Souveränitätswashing)**
US-Eigentümer, US-Technologie, EU-Serverstandort als Marketing-Argument. C5-Testat vorhanden, CLOUD-Act-Risiko direkt und strukturell.

Anbieter: AWS Frankfurt, Azure Deutschland, Google Cloud DE (Standard-Angebote ohne Sovereign-Zusatz)

Geeignet für: Keine personenbezogenen Gesundheitsdaten, keine regulierten Daten, keine KRITIS-Systeme.

## 16.3 Entscheidungsmatrix — Workload-Zuordnung

| Workload | Schutzklasse | Empfohlene Stufe | Konkrete Anbieter / Software |
|---|---|---|---|
| ePA-Kerndaten, Diagnosen, Medikation | KRITIS / § 393 Klasse 1 | **Stufe 1** | plusserver, EWERK Leipzig |
| GKV-Kernabrechnungssysteme | KRITIS / § 393 Klasse 1 | **Stufe 1** | plusserver, STACKIT |
| Klinik-KIS, psychiatr. Daten | KRITIS / § 393 Klasse 1 | **Stufe 1–2** | plusserver oder Delos Cloud |
| **E-Mail (intern, mit Patientenbezug)** | § 393 Klasse 1–2 | **Stufe 1** | Open-Xchange + Thunderbird auf plusserver/STACKIT |
| **E-Mail (allgemein, kein Patientenbezug)** | Klasse 2 | **Stufe 1–2** | Open-Xchange auf EU-Cloud oder Delos |
| **Office-Suite, Dokumente** | § 393 Klasse 2 | **Stufe 1** | Euro-Office / Nextcloud Hub / Office.eu |
| **SharePoint / Dokumentenmanagement** | § 393 Klasse 1–2 | **Stufe 1** | Nextcloud, OpenCloud, GoFAST auf plusserver/STACKIT |
| **Microsoft 365 (tief integriert, nicht migrierbar)** | § 393 Klasse 2 | **Stufe 2** | Delos Cloud (Azure-Basis, BSI CPR, +15%) |
| **Videokonferenz intern** | Klasse 2 | **Stufe 1** | Jitsi / OpenTalk auf EU-Cloud |
| **Identity / Active Directory** | Klasse 1 | **Stufe 1** | Keycloak / Univention Corporate Server |
| KI-Diagnostik (LLM-Inferenz auf Patientendaten) | § 393 Klasse 1 | **Stufe 1** | vLLM + Mistral on-premise / STACKIT |
| Analytics / BI auf GKV-Daten | § 393 Klasse 2 | **Stufe 1–2** | Metabase/Superset auf STACKIT, OVHcloud SNC |
| Telemedizin-Plattform | § 393 Klasse 2 | **Stufe 1–2** | STACKIT, plusserver |
| Dev/Test-Umgebungen | Klasse 3 | **Stufe 3–4** | Hetzner, IONOS |
| Öffentliche Webpräsenz | Klasse 3 | **Stufe 4** | Beliebig |

**Drei-Zonen-Migrationsstrategie für GKVen und Kliniken:**

Zone 1 — Jetzt umsetzbar (0–12 Monate): E-Mail (Open-Xchange), Dateiablage (Nextcloud), Videokonferenz (Jitsi/OpenTalk), Identity (Keycloak). Diese Dienste sind heute produktionsreif, tragen die höchsten CLOUD-Act-Risiken durch Kommunikationsdaten und sind technisch am einfachsten zu migrieren.

Zone 2 — Mittelfristig (1–3 Jahre): Office-Suite vollständig (Euro-Office/Nextcloud Workspace), Analytics auf Sozialdaten (EU-Cloud + Metabase/Superset), KI-Dienste (lokal/STACKIT + Mistral), CI/CD-Migration (GitLab).

Zone 3 — Komplex, langfristig (3–5 Jahre): Tief integrierte Fachverfahren (KIS-Systeme, GKV-Primärsoftware), Windows-Desktop-Ablösung (→ Linux, wie Schleswig-Holstein), SAP-Konsolidierung. Hier ist das Operator-Modell (Delos Cloud) der realistische Übergangspfad bis zur vollständigen Migration.

## 16.4 Datentransfer-Folgenabschätzung (TIA) — Pflichtinstrument für bestehende US-Provider

Wer heute Azure, AWS oder andere US-kontrollierte Dienste für Gesundheitsdaten nutzt, muss rechtlich handeln — nicht erst beim nächsten Vertrag, sondern jetzt. Das Instrument dafür heißt Transfer Impact Assessment, kurz TIA — auf Deutsch: Datentransfer-Folgenabschätzung.

**Was ist ein TIA und warum ist er Pflicht?**

Das EuGH-Urteil Schrems II (2020) hat festgestellt: Standardvertragsklauseln (SCCs — das sind Musterverträge, die die EU-Kommission für Datenübermittlungen in unsichere Drittländer bereitstellt) reichen allein nicht mehr aus. Der Grund: Sie garantieren zwar vertraglich Datenschutz, schützen aber nicht davor, dass US-Behörden die Daten auf anderem Weg anfordern können. Deshalb verlangt das Gericht seither zusätzlich eine individuelle Prüfung: Schützen die vertraglichen Garantien die Daten im konkreten Fall tatsächlich — angesichts der Rechtslage im Empfängerland? Diese Prüfung ist das TIA. Sie ergibt sich aus Klausel 14 der aktuellen SCCs (in Kraft seit 2022) und der DSGVO-Rechenschaftspflicht (Art. 5 Abs. 2 DSGVO). EU-Aufsichtsbehörden haben 2023–2024 über 127 Abhilfemaßnahmen wegen unzureichender TIAs verhängt; das BfDI (Bundesbeauftragter für den Datenschutz und die Informationsfreiheit) hat technische Kontrollen als stärkstes Nachweismittel eingestuft.

**Was prüft ein TIA konkret?**

Ein TIA für US-Cloud-Dienste im Gesundheitsbereich durchläuft vier Schritte:

Erstens die Bestandsaufnahme: Welche Daten fließen genau wohin? Dabei sind Kategorie (Diagnosen, Medikation, Versichertendaten), Menge, Format (verschlüsselt oder im Klartext) und Übertragungskanal zu dokumentieren. Gesundheitsdaten nach Art. 9 DSGVO erfordern eine besondere Begründung.

Zweitens die Rechtslageprüfung im Empfängerland: Gibt es Gesetze, die den US-Anbieter zur Herausgabe an Behörden verpflichten, obwohl die Daten in der EU liegen? Für US-Anbieter lautet die Antwort strukturell: Ja — CLOUD Act, FISA § 702, NSL. Diese Gesetze müssen im TIA namentlich analysiert werden.

Drittens die Risikoabwägung: Sind zusätzliche Schutzmaßnahmen (Verschlüsselung mit eigenem Schlüssel, Pseudonymisierung, technische Zugangssperren) geeignet, das Restrisiko auf ein akzeptables Maß zu senken? Für personenbezogene Gesundheitsdaten im Klartext auf US-Infrastruktur: in der Regel nein — der EuGH hat in Schrems II explizit klargestellt, dass FISA § 702 kein angemessenes Schutzniveau bietet.

Viertens die Dokumentation und Schlussfolgerung: Das TIA ist schriftlich zu dokumentieren, mit Datum und Unterschrift des Datenschutzbeauftragten, und bei Veränderungen der Rechtslage zu aktualisieren. Wenn das Ergebnis ist, dass kein angemessenes Schutzniveau erreichbar ist, darf der Transfer nicht stattfinden — oder er muss auf Basis einer anderen DSGVO-Ausnahme rechtlich begründet werden.

**Was bedeutet das für Gesundheitsinstitutionen konkret?**

Eine GKV, die Microsoft 365 mit Exchange Online für interne Kommunikation nutzt, bei der Patientenbezüge in E-Mails vorkommen, muss ein TIA für diese Datenübermittlung erstellt und dokumentiert haben. Liegt kein TIA vor, ist die Verarbeitung formell rechtswidrig — auch wenn § 393 SGB V und C5 eingehalten werden. Das TIA ist nicht die Lösung des CLOUD-Act-Problems, sondern der dokumentarische Nachweis, dass die Organisation das Problem kennt, bewertet hat und Maßnahmen ergreift. Als Überbrückungsmaßnahme bis zur vollständigen Migration zur EU-Infrastruktur (Kap. 8, 15.2) ist es das Mindestdokument, das jede Aufsichtsbehörde erwarten wird.

## 16.5 Vertragliche Absicherung — AVV-Erweiterungen

Unabhängig von der gewählten Stufe: AVV-Erweiterungen (AVV = Auftragsverarbeitungsvertrag, der Standardvertrag zwischen einer Organisation und ihrem Cloud-Anbieter nach Art. 28 DSGVO) für CLOUD-Act-Schutz aufnehmen:

- **Informationspflicht:** Verarbeiter muss unverzüglich informieren, wenn eine CLOUD-Act- oder vergleichbare Anfrage eingeht
- **Ablehnungspflicht:** Explizite Pflicht, DSGVO-widrigen Herausgabeanordnungen zu widersprechen, solange kein Art.-48-DSGVO-konformes Rechtshilfeabkommen besteht
- **Haftungsklausel:** Verarbeiter haftet für Schäden aus nicht gemeldeten Herausgaben
- **Audit-Recht:** Regelmäßiges Recht auf Kontrolle der tatsächlichen Datenflüsse und Zugriffsprotokoll-Einsicht
- **Technologieänderungs-Klausel** (für Operator-Modell): Delos/S3NS müssen Veränderungen im Verhältnis zum US-Technologielieferanten melden, die die Souveränitätsarchitektur berühren
- **Change-of-Control-Klausel:** Bei Eigentümerwechsel des Anbieters (z.B. Übernahme durch US-Unternehmen) ist der Vertrag neu zu prüfen und ggf. zu kündigen — besonders relevant für PE-geführte Anbieter wie EWERK

## 16.6 Exit-Strategie und Cloud-Portabilität — der unterschätzte Engpass

Das häufigste Missverständnis in der Souveränitätsdebatte: Organisationen glauben, sie können Azure oder AWS jederzeit verlassen, wenn es nötig wird. In der Praxis ist ein Anbieterwechsel ohne Vorbereitung ein Mehrjahresprojekt mit erheblichen versteckten Kosten. Diesen Effekt nennt man Anbieterabhängigkeit (englisch: Vendor Lock-in) — die wachsende Schwierigkeit, einen einmal gewählten Cloud-Anbieter zu verlassen.

**Warum ist der Ausstieg so schwer?**

Drei Mechanismen binden Organisationen an ihren Cloud-Anbieter:

Technischer Lock-in entsteht durch proprietäre Dienste — das sind Funktionen, die ein Anbieter exklusiv anbietet und die kein direktes Äquivalent beim Wettbewerber haben. AWS Lambda (Programmierumgebung ohne eigene Server), Azure Active Directory (Nutzerverwaltung und Zugriffssteuerung), Microsoft 365-Datenformate für E-Mails und Kalender — all das lässt sich nicht mit einem Knopfdruck exportieren und anderswo weiterbetreiben. Je tiefer eine Organisation in anbieter-eigene Funktionen investiert hat, desto teurer und zeitaufwändiger wird der Wechsel.

Kommerzieller Lock-in kommt durch Rabattverträge: Cloud-Anbieter bieten erhebliche Preisnachlässe für mehrjährige Abnahmeverpflichtungen (sogenannte Reserved Instances oder Enterprise Agreements). Wer solche Verträge abgeschlossen hat, zahlt für einen vorzeitigen Ausstieg doppelt — einmal für die Migration und einmal für die nicht genutzten, bereits bezahlten Kapazitäten.

Betrieblicher Lock-in ist der subtilste: Wenn ein IT-Team jahrelang ausschließlich mit Azure-Tools gearbeitet hat, ist ein Wechsel zu STACKIT oder plusserver nicht nur eine technische, sondern auch eine Qualifikationsfrage. Schulung und Umgewöhnung kosten Zeit.

**Was der EU Data Act ab September 2025 ändert**

Der EU Data Act (in Kraft seit Januar 2024, Cloud-Bestimmungen vollständig anwendbar seit September 2025) verpflichtet Cloud-Anbieter erstmals rechtlich zu Portabilität: Kunden haben das Recht auf Datenexport in offenen, maschinenlesbaren Formaten, und Anbieter müssen den Wechsel technisch erleichtern. Ab 2027 entfallen auch Datenausgangsgebühren (sogenannte Egress-Kosten — Gebühren, die Anbieter bisher für den Datenabzug erhoben haben) vollständig. OVHcloud hat diese Gebühren bereits seit Dezember 2025 abgeschafft. Der EU Data Act senkt die Wechselkosten, ersetzt aber keine strategische Exit-Planung.

**Wie eine Exit-Strategie aussieht**

Eine Exit-Strategie ist keine Drohung gegenüber dem Anbieter, sondern die strukturierte Vorbereitung auf den Fall, dass ein Wechsel nötig wird — durch regulatorischen Zwang (Schrems III), politische Eskalation oder eine Übernahme des Anbieters durch ein US-Unternehmen. Sie umfasst:

Inventur: Welche Systeme laufen wo, mit welchen anbieter-spezifischen Funktionen? Wer einen Überblick hat, kann priorisieren — und findet meist, dass die Abhängigkeit an wenigen kritischen Diensten hängt, nicht gleichmäßig verteilt ist.

Datenexporttests: Können alle Daten vollständig und in offenen Formaten exportiert werden? Das sollte regelmäßig geprüft werden — nicht erst im Notfall. Besonders problematisch: E-Mail-Archive in Exchange-Formaten, SharePoint-Dokumentenbibliotheken und Azure-Active-Directory-Nutzerdaten.

Architektur für Portabilität: Workloads, die in Containern (standardisierte Software-Pakete, die auf jeder kompatiblen Infrastruktur laufen) auf Kubernetes (dem gängigen Standard zur Verwaltung von Containern) betrieben werden, lassen sich deutlich leichter migrieren als solche, die tief in anbieter-eigene Dienste integriert sind. Wer heute neu aufbaut, sollte offene Standards konsequent bevorzugen.

Migrationspfad für kritische Workloads: Die realistischen Kosten einer Migration — Personentage, Schulung, Ausfallzeiten, Vertragsrestlaufzeiten — sollten geschätzt und dokumentiert sein, damit die Entscheidung im Bedarfsfall schnell getroffen werden kann.

Für GKVen und Kliniken gilt: Ein Anbieterwechsel für Kernsysteme dauert 6 bis 18 Monate. Wer 2026 nicht beginnt zu planen, handelt 2028 unter Druck. Die Drei-Zonen-Strategie in §16.3 ist die praktische Umsetzung dieser Reihenfolge.

## 16.7 Verschlüsselung — wo HYOK hilft und wo nicht

Clientseitige Verschlüsselung mit eigener Schlüsselhoheit (HYOK — Hold Your Own Key) schützt strukturell vor CLOUD-Act-Zugriff, aber nur bei ruhenden Daten: Archivdaten, Backups, Objektspeicher, File-Storage. Für Daten, die der Anbieter verarbeiten muss — Microsoft 365, E-Mail-Spam-Filter, KI-Inferenz, SaaS-Anwendungen, Real-time-Analytics — funktioniert HYOK nicht, weil das System Klartextzugang benötigt. BYOK (Bring Your Own Key) bietet nur schwachen Schutz, weil der Anbieter die Schlüssel in seinem eigenen Key Management System verwaltet und technisch Zugriff hat. Die vollständige Analyse der drei Verschlüsselungsmodelle und die Gesundheitssektor-Matrix: → Kapitel 13.

## 16.8 Reise-Hygiene bei US-Einreisen

Betrifft Mitarbeitende mit Zugang zu sensiblen Gesundheitssystemen:

- Reisegerät ohne lokale Mail-Caches, VPN-Zugangsdaten und Gesundheitsdaten nutzen
- Apps vor Einreise ausloggen — CBP (US Customs and Border Protection) darf physische Geräte ohne richterlichen Herausgabebeschluss durchsuchen (vgl. §3.4)
- Keine KRITIS-relevanten Zugangsdaten, SSH-Schlüssel oder API-Tokens auf Reisegeräten
- Für hochsensible Positionen: dediziertes Reisegerät mit frischer Installation

## 16.9 Haftungskette: Wer haftet, wenn der Patient klagt?

Die bisherigen Kapitel haben das CLOUD-Act-Risiko als regulatorisches und technisches Problem beschrieben. Dieser Abschnitt zeigt die zivilrechtliche Konsequenz — in zwei Szenarien, die sich fundamental unterscheiden.

**Szenario 1 — Latentes Risiko: Kein konkreter Zugriff, aber CLOUD-Act-exponierter Anbieter**

Ein Patient erfährt, dass seine Krankenkasse oder sein Krankenhaus Gesundheitsdaten bei einem US-Hyperscaler verarbeitet. Er klagt auf Schadensersatz nach Art. 82 DSGVO. In diesem Szenario muss kein tatsächlicher US-Zugriff stattgefunden haben. Die EuGH-Rechtsprechung entwickelt sich in die Richtung, dass bereits der Kontrollverlust über die eigenen Daten einen immateriellen Schaden begründen kann — also die Tatsache, dass die Daten bei einem Anbieter liegen, der einer US-Herausgabepflicht unterliegt, und die verantwortliche Institution das wusste oder hätte wissen müssen. Bei einem US-Hyperscaler mit öffentlicher NYSE-Notierung ist das schwer zu bestreiten. Die Schadensersatzsummen in diesem Szenario sind individuell gering — einige hundert bis wenige tausend Euro pro Person. Das ändert sich bei Sammelklagen: Eine GKV mit fünf Millionen Versicherten, deren Abrechnungsdaten auf US-Infrastruktur laufen, ist ein strukturelles Ziel für Musterfeststellungsklagen oder Beschwerden durch Datenschutz-NGOs wie noyb.

**Szenario 2 — Konkreter Zugriff: US-Behörden haben auf Gesundheitsdaten zugegriffen und der Vorfall ist gemeldet**

Dieses Szenario ist der harte Fall. Er wird greifbar, wenn man ihn an den dokumentierten Beispielen durchspielt.

Angenommen, eine der sanktionierten HateAid-Geschäftsführerinnen ist bei einer GKV versichert, die ihre Abrechnungsdaten auf Azure verarbeitet. Ab dem Zeitpunkt der Sanktionierung ist Microsoft verpflichtet, alle Daten zu dieser Person einzufrieren und auf Anfrage herauszugeben — Diagnosen, Medikation, Behandlungsverläufe, Arzt-Patienten-Kontakte. Oder eine FISA-§-702-Abfrage erfasst im Rahmen eines pauschalen Überwachungsprogramms die Daten von tausenden GKV-Versicherten bei einem US-Anbieter. Oder ein CLOUD-Act-Herausgabebeschluss in einer Strafermittlung gegen einen einzelnen Arzt zieht die Abrechnungsdaten seiner gesamten Patientenschaft mit.

Irgendwann wird der Zugriff bekannt — durch Aufhebung einer Schweigeverpflichtung, durch einen Whistleblower, durch ein US-Gerichtsverfahren, das öffentlich wird, oder durch eine Transparenzpflicht des Anbieters. Bei den ICC-Richtern war der Zugriff sofort sichtbar: Microsoft, Amazon und Gmail sperrten die Accounts. Bei den HateAid-Geschäftsführerinnen wird geprüft, ob Zahlungsdienstleister und Cloud-Konten betroffen sind. Die Gesundheitsinstitution meldet den Vorfall nach Art. 33 DSGVO an die zuständige Aufsichtsbehörde. Ab diesem Moment läuft eine Kaskade:

**Stufe 1 — Bußgeld durch die Aufsichtsbehörde.** Die Aufsichtsbehörde prüft nach Art. 58 DSGVO. Sie fragt: Lag ein TIA vor? Hat die Institution das CLOUD-Act-Risiko dokumentiert? Wurden EU-souveräne Alternativen evaluiert? Wenn nichts davon vorliegt — und das ist bei der Mehrheit der Gesundheitsinstitutionen der Fall —, ist die Verletzung der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO offensichtlich. Das Bußgeld nach Art. 83 DSGVO kann bis zu 20 Millionen Euro oder 4 Prozent des Jahresumsatzes betragen. Bei einer großen GKV oder einem Universitätsklinikum sind das relevante Summen.

**Stufe 2 — Schadensersatz pro betroffenem Patienten.** Parallel können betroffene Patienten nach Art. 82 DSGVO Schadensersatz fordern — und in diesem Szenario geht es nicht mehr um abstrakten Kontrollverlust, sondern um einen dokumentierten Zugriff auf konkrete Gesundheitsdaten. Diagnosen, Medikationspläne, psychiatrische Befunde, HIV-Status, Suchterkrankungen — Daten, deren Offenlegung gegenüber einer ausländischen Behörde ohne Rechtsgrundlage einen massiven Eingriff in die Persönlichkeitsrechte darstellt.

Die Schadensersatzsummen pro Person liegen bei dokumentiertem Zugriff auf sensible Gesundheitsdaten nach bisheriger europäischer Rechtsprechung im Bereich von mehreren tausend bis fünfstelligen Euro-Beträgen — abhängig von der Sensitivität der betroffenen Daten und den Umständen der Offenlegung. Ein konkretes Rechenbeispiel: Bei einer FISA-§-702-Abfrage, die 100.000 Versichertendatensätze einer GKV erfasst hat, und einem durchschnittlichen Schadensersatz von 5.000 Euro pro Person ergibt sich eine Gesamtforderung von 500 Millionen Euro. Selbst bei konservativen 1.000 Euro pro Person wären es 100 Millionen Euro. Das sind keine theoretischen Zahlen — das ist die Arithmetik, die ein Gericht anwenden wird, multipliziert mit der Zahl der Betroffenen.

**Stufe 3 — Sammelklagen und NGO-Beschwerden.** Einzelne Patienten werden selten klagen. Aber Verbraucherschutzorganisationen, Datenschutz-NGOs wie noyb oder Anwaltskanzleien, die sich auf DSGVO-Sammelklagen spezialisiert haben, suchen gezielt nach genau solchen Fällen. Eine GKV mit Millionen Versicherten, bei der ein dokumentierter US-Behördenzugriff auf Gesundheitsdaten stattgefunden hat, ist der perfekte Musterfeststellungsklage-Fall. Die Haftungssummen werden dann nicht mehr individuell, sondern existenziell.

**Die doppelte Haftung — Verantwortlicher und Auftragsverarbeiter.** Die Klinik, Krankenkasse oder Kassenärztliche Vereinigung ist als Verantwortlicher nach Art. 4 Nr. 7 DSGVO haftbar. Sie bestimmt Zweck und Mittel der Verarbeitung und hat nach Art. 28 Abs. 1 DSGVO die Pflicht, nur Auftragsverarbeiter einzusetzen, die hinreichende Garantien bieten. Wenn sie wissentlich einen Anbieter unter US-Jurisdiktion gewählt hat und die CLOUD-Act-Exposition nicht dokumentiert und bewertet hat, haftet sie für diese Entscheidung.

Der Cloud-Anbieter haftet als Auftragsverarbeiter nach Art. 82 Abs. 2 DSGVO direkt gegenüber Betroffenen, wenn er einer CLOUD-Act-Anordnung nachgekommen ist, ohne den Verantwortlichen zu informieren und ohne alle verfügbaren Rechtsmittel auszuschöpfen. In der Praxis wendet sich die Aufsichtsbehörde aber zuerst an den Verantwortlichen — an die GKV oder die Klinik. Liegt kein TIA vor (vgl. §16.4), ist die Haftungsfrage schnell beantwortet.

**Die persönliche Geschäftsführerhaftung — drei Wege, sauber getrennt.**

Die DSGVO selbst kennt keine explizite persönliche GF-Haftung. Bußgelder nach Art. 83 DSGVO treffen die Organisation — die GKV, die Klinik, die KV. Nicht den Geschäftsführer als Person. Aber die persönliche Haftung kommt über zwei andere Wege:

Der erste Weg ist die gesellschaftsrechtliche Organhaftung nach § 43 GmbHG beziehungsweise § 93 AktG. Wenn ein Geschäftsführer eine Entscheidung trifft, die vorhersehbar zu einem DSGVO-Bußgeld oder zu Schadensersatzansprüchen führt — etwa die bewusste Wahl eines CLOUD-Act-exponierten Anbieters ohne dokumentierte Risikoabwägung und ohne Prüfung europäischer Alternativen —, kann die Organisation ihren Geschäftsführer in Regress nehmen. Ein Bußgeld von 20 Millionen Euro oder Schadensersatzforderungen von hunderttausenden Patienten sind ein bezifferbarer Schaden, der auf eine konkrete Leitungsentscheidung zurückgeführt werden kann. Voraussetzung: Die Entscheidung beruhte nicht auf einer sorgfältigen, dokumentierten Abwägung. Liegt kein TIA vor (vgl. §16.4), fehlt genau diese Dokumentation.

Der zweite Weg ist die NIS2-Richtlinie, umgesetzt durch die BSIG-Novelle. NIS2 regelt Cybersicherheit, nicht Datenschutz — die Haftung nach § 38 BSIG greift bei Verletzung von Cybersicherheitspflichten. Ein US-Behördenzugriff per CLOUD Act ist kein Cyberangriff im klassischen Sinne. Aber NIS2 verlangt in Art. 21 Abs. 2 lit. d ausdrücklich die Bewertung von Sicherheitsrisiken in der Lieferkette — und ein CLOUD-Act-exponierter Cloud-Anbieter ist ein Lieferkettenrisiko. Wer als GKV oder Klinik unter NIS2 fällt und seine Cloud-Lieferkette nicht auf Jurisdiktionsrisiken geprüft hat, verletzt die NIS2-Sorgfaltspflicht. Für diese Verletzung haften Geschäftsführer nach § 38 BSIG persönlich — unabhängig davon, ob jemals ein US-Zugriff stattfindet.

In der Praxis verstärken sich beide Wege: Die fehlende DSGVO-Dokumentation (kein TIA) ist gleichzeitig der Nachweis einer fehlenden NIS2-Lieferkettenprüfung. Ein einziges fehlendes Dokument öffnet zwei Haftungspfade.

**Die Dokumentationsfalle.** Dieses Dokument — und zahlreiche vergleichbare Analysen, Aufsichtsbehörden-Beschlüsse und EuGH-Urteile — sind öffentlich zugänglich. Für eine Gesundheitsinstitution wird es zunehmend schwer zu argumentieren, sie habe von dem Risiko nichts gewusst. Das Wissen ist verfügbar. Die Frage vor Gericht wird sein: Hat die Leitung es zur Kenntnis genommen und darauf reagiert — oder hat sie es ignoriert?

## 16.10 Grundprinzip: Rechtsstaatlicher Zugriff als Maßstab — nicht politisches Vertrauen

Aus der Analyse in Kapitel 4 ergibt sich ein handlungsleitendes Prinzip für Infrastrukturentscheidungen:

**Das richtige Kriterium ist nicht "Verbündeter oder nicht-Verbündeter" — es ist "rechtsstaatlich gebunden oder nicht."**

Vier Leitfragen für jede Infrastrukturentscheidung im Gesundheitsbereich:

1. **Unabhängige richterliche Kontrolle für alle Betroffenen?** Gilt nicht nur für eigene Staatsbürger, sondern auch für EU-Bürger? Wenn nein: strukturell inakzeptabel für Art.-9-Daten.

2. **Anlassbezogen oder anlasslos?** FISA § 702 und NSL erlauben Massenerfassung ohne Einzelfallverdacht. Kein System, das das ermöglicht, ist eine akzeptable Grundlage für Gesundheitsdaten von 74 Millionen GKV-Versicherten.

3. **Politisch instrumentalisierbar?** Der ICC-Präzedenzfall (2025): Cloud-Dienste wurden als Druckmittel in einer politischen Auseinandersetzung eingesetzt. Infrastruktur, die von der politischen Konstellation eines einzelnen Verbündeten abhängt, ist strategisch vulnerabel — unabhängig davon, wie eng die Allianz heute ist.

4. **Stabiles Recht oder Präsidialerlass?** EU-Recht und GRCh überdauern Regierungswechsel. Das Data Privacy Framework hängt an einem Präsidialerlass und kann durch eine gegenteilige Executive Order aufgehoben werden.

**Für europäischen Behördenzugriff (e-Evidence-VO):** Akzeptabel — rechtsstaatlich gebunden, verhältnismäßig, für alle Betroffenen anfechtbar.

**Für US-Behördenzugriff (FISA § 702, NSL):** Für Gesundheitsdaten strukturell nicht akzeptabel — nicht weil die USA ein Feind sind, sondern weil diese Instrumente den Anforderungen an Grundrechtsschutz für EU-Bürger nicht genügen.

**Für den "westlichen Verbund"-Gedanken (NATO/Five Eyes):** Militärische und geheimdienstliche Kooperation legitimiert keinen anlasslosen Zugriff auf Krankenakten. Der Kategorieunterschied zwischen SIGINT (Fernmeldeaufklärung)-Kooperation und Gesundheitsdaten ist nicht akademisch — er ist die Grundlage jeder verhältnismäßigen Abwägung.

## 16.11 Aufsichtsbehörden-Flickenteppich — wer was toleriert

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

---
