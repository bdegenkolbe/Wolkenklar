# 12. Marktbeispiele: Wie Gesundheitsinstitutionen in die US-Cloud geraten

Die abstrakten Rechtskonflikte aus den Kapiteln 1–11 materialisieren sich in konkreten Beschaffungsentscheidungen. Die folgenden Fälle illustrieren die fünf strukturellen Eintrittspfade: SAP-Migrationsdruck, KIS-Neuausschreibung, IT-Outsourcing, Übernahme durch US-Konzerne, SaaS-Plattformdominanz. Alle sind öffentlich dokumentiert.

---

## 12.1 Eintrittspfad 1: GKV-Rechenzentren — das Cloud-Outsourcing läuft über Intermediäre

GKV-Kernsysteme laufen nicht bei den Kassen selbst — sie liegen bei spezialisierten GKV-Rechenzentren: **BITMARCK** (>80 % aller GKV), **Kubus IT** (AOK Bayern/Plus), **ITSC** (norddeutsche Kassen), **gkv informatik**, **ITSCare** (Baden-Württemberg, Hessen, Rheinland-Pfalz/Saarland) und **MOBIL ISC**. Diese RZ sind die eigentlichen Infrastrukturentscheider — und sie migrieren gerade in Richtung Cloud. Das CLOUD-Act-Risiko entsteht nicht in der Kassensoftware selbst, sondern in der Hosting-Schicht darunter.

**ITSCare — kasseneigenes RZ für 7,5 Millionen Versicherte:** ITSCare ist eine 2007 gegründete IT-Gesellschaft mit den Gesellschaftern AOK Baden-Württemberg, AOK Hessen und AOK Rheinland-Pfalz/Saarland. Mit ~700 Mitarbeitenden und Sitz Frankfurt/Stuttgart verarbeitet ITSCare die Sozialdaten von über 7,5 Millionen Versicherten — Netzwerke, Hardware, Software, Telekommunikation, Rechenzentrum aus einer Hand. Als 100%-Tochter der drei AOKs ist ITSCare strukturell günstig positioniert: kein US-Eigentümer, kein US-Börsenmarkt. Die Stellenprofile zeigen allerdings eine hybride On-Premise/Cloud-Architektur im Aufbau — die Frage ist, welche Public-Cloud-Dienste dabei zum Einsatz kommen. CLOUD-Act-Risiko: strukturell gering solange keine US-Hyperscaler als Primärinfrastruktur gewählt werden.

**Techniker Krankenkasse — Inhouse-IT-Strategie als bewusstes Gegenmodell:** Die TK (Hamburg, ~12 Millionen Versicherte, größte deutsche GKV) betreibt ihre IT mit ~600 internen Mitarbeitenden weitgehend inhouse. Von der IT-Strategie und IT-Architektur bis zum 7×24 active-active Rechenzentrumsbetrieb liegt alles im Verantwortungsbereich der internen IT-Abteilung. Das ist eine bewusste strategische Entscheidung. CIO Aude Vik (seit Januar 2024) formulierte im TK-Geschäftsbericht 2023 direkt: Cloud-Technologie als Krankenkasse zu nutzen erfordert besondere Vorsichtsmaßnahmen, um sensible Daten vor unbefugtem Zugriff zu schützen. Die TK nutzt Cloud-Techniken selektiv — aber Kernsysteme und Kerndaten bleiben on-premise in eigenen Rechenzentren. IBM Cloud Private wurde 2018 für die eGA-Entwicklung eingesetzt — Private Cloud im eigenen RZ, kein US-Public-Cloud-Exposé. CLOUD-Act-Risiko: strukturell gering bei konsequenter Fortsetzung dieser Strategie.

**Kubus IT → Arvato Systems → Google Cloud** (Negativbeispiel, belegt): Kubus IT migrierte sein On-Premise-RZ vollständig zu Arvato Systems für ~17.500 IT-Nutzer. Arvato bietet dabei Google Cloud als Hyperscaler-Option an. Auf dem Google Cloud Summit München 2024 präsentierte Arvato den Kubus-Fall als Beleg für "souveräne GKV-Cloud mit Google". Google Cloud ist CLOUD-Act-Kategorie A — Serverstandort schützt nicht. [Quelle: Arvato Systems Referenz "Cloud migration for kubus IT"]

**ITSC → OVHcloud** (Positivbeispiel, belegt): Das ITSC migriert mit adesso zu OVHcloud-Rechenzentren in Deutschland und Frankreich. Budget siebenstellig, Start Mai 2024. OVHcloud ist französisch, keine US-Börsennotierung. [Quelle: e-health-com.de, "adesso wird Cloud-Transformationspartner für das ITSC"]

**gkv informatik → T-Systems**: Teile der gkv-informatik-Infrastruktur wurden zu T-Systems ausgelagert — als AWS-Partner und Azure-Reseller tief in US-Hyperscaler eingebettet. CLOUD-Act-Risiko entsteht dort, wo GKV-Workloads auf US-Diensten laufen.

**Die SAP-Zeitbombe:** Alle AOK-Systeme laufen auf `oscare®` (SAP-basiert). Die nächste Migration — SAP S/4HANA Cloud auf Azure oder AWS — wäre ein direkter CLOUD-Act-Eintrittspfad. Mit dem "BITMARCK all in ONE"-Programm und dem govdigital-Beitritt (Oktober 2024) stellt sich dieselbe Frage für BITMARCK. [Quelle: govdigital.de Oktober 2024; BITMARCK-Kundentag 2025]

---

## 12.2 Eintrittspfad 2: KVen — Azure als etablierte Infrastruktur (belegt durch TED-Ausschreibung)

Die 17 deutschen Kassenärztlichen Vereinigungen verwalten die ambulante Versorgung von 75 Millionen gesetzlich Versicherten — Honorarabrechnungen, Zulassungsregister, Qualitätsdaten, Praxisnetze. KVWL (Westfalen-Lippe, >16.000 Mitglieder) und KVNO (Nordrhein, 19.500 Mitglieder, ~9,5 Mio. Versicherte) betreiben ihre IT gemeinsam über die **KV-IT GmbH** in Düsseldorf/Dortmund. [Quelle: kvno.de/kv-it-gmbh]

**Der Beleg — TED-Ausschreibung 98706-2026 (11. Februar 2026):** Die KVNO schrieb unter der Kennung X-KVNO-2025-0023 die "Entwicklung und Betrieb einer KI-Plattform als PaaS-Lösung sowie diverser KI Use Cases" aus. Der Ausschreibungstext ist eindeutig:

> *"Die KI-Plattform wird als Cloud-PaaS-Lösung auf der Azure Cloud der KVNO vom Auftragnehmer bereitgestellt und langfristig im Auftrag der KVNO betrieben."*

Azure ist damit nicht als Option formuliert, sondern als gegebene, bereits bestehende Infrastruktur der KVNO. Der Auftragnehmer soll auf dieser Azure-Umgebung aufbauen — nicht eine neue Cloud-Infrastruktur auswählen. [Quelle: TED 98706-2026, EU-Amtsblatt S 29/2026]

**Was die Ausschreibung außerdem zeigt:**
- Eignungskriterien verlangen **BSI C5 Typ 2-Testate** für Container-Orchestrierung und KI-Dienste — technische Sicherheit wird adressiert
- DSGVO-, BDSG-, EU-KI-VO- und SGB-V-Konformität ist explizite Anforderung
- Der **CLOUD Act** als Risikodimension taucht in der Ausschreibung nicht auf — strukturell nicht adressiert
- Mindestlaufzeit 36 Monate, zweimal verlängerbar um je 12 Monate → langfristige Azure-Bindung

**CLOUD-Act-Bewertung:** Microsoft (NYSE: MSFT) ist CLOUD-Act-Kategorie A — direkte US-Exposition. Die Azure-Infrastruktur der KVNO verarbeitet Honorardaten, die implizit Diagnose- und Leistungsinformationen zu Arzt-Patienten-Beziehungen enthalten. C5 und DSGVO-Konformität adressieren technische Sicherheit und datenschutzrechtliche Verarbeitung — nicht die Frage, ob US-Behörden auf die Infrastruktur zugreifen könnten. Das ist das strukturelle Problem: Die KVNO kauft C5-konformen Betrieb ein, aber C5 ≠ CLOUD-Act-Immunität (→ Kapitel 5.3).

**Das strukturelle KV-Muster:** Als Körperschaften des öffentlichen Rechts sind KVen EU-ausschreibungspflichtig. Vergabekriterien wie "2 vergleichbare Referenzprojekte mit Cloud-PaaS auf Azure" schreiben Microsoft strukturell fest — nicht durch bösen Willen, sondern weil Azure der de-facto-Standard ist, gegen den Referenzen gemessen werden. Ein Umstieg würde einen aktiven Beschluss erfordern, Azure als Referenzplattform zu ersetzen.

---

## 12.3 Eintrittspfad 3: MDK — Souveräne Branchenlösung auf EWERK-Infrastruktur (Positivbeispiel)

Die **MDK-Gemeinschaft** (15 Medizinische Dienste bundesweit, über 9.000 Mitarbeiter) entschied sich 2018 nach einem europaweiten Vergabeverfahren für ein Konsortium aus **HBSN AG**, **EWERK RZ GmbH** (Leipzig) und **MOBIL ISC GmbH** für den Betrieb ihrer gemeinsamen Branchenlösung. [Quelle: zaronews.world, Pressemitteilung HBSN, Juni 2018]

Das Modell: Homogenisierung der IT aller 15 Medizinischen Dienste auf einer gemeinsamen Plattform — betrieben von EWERK Leipzig, einem deutschen IT-Dienstleister ohne US-Eigentümer und ohne US-Börsennotierung. EWERK betreibt eigene Rechenzentren in Leipzig (ISO 27001, ISAE 3402 Typ II, ISO 20000), nutzt Nutanix-Hyperkonvergenzinfrastruktur und bietet IaaS/PaaS für KRITIS-relevante Kunden im Gesundheitswesen, öffentlicher Verwaltung und Energieversorgung.

**CLOUD-Act-Bewertung:** Soweit öffentlich erkennbar, läuft die MDK-Branchenlösung auf eigener EWERK-Infrastruktur ohne US-Hyperscaler als primäre Plattform. EWERK (NORD Holding als Mehrheitseigentümer, deutsches PE) hat keine US-Jurisdiktion. Das MDK-Modell ist ein funktionierender Gegenfall zur US-Hyperscaler-Dominanz im Gesundheitswesen — entstanden nicht durch politische Vision, sondern durch eine sachgerecht formulierte Ausschreibung.

---

## 12.4 Eintrittspfad 4: KIS-Neuausschreibung — Charité und der Epic-Präzedenzfall

Die Charité (Berlin, 950.000 Patienten/Jahr, Europas größtes Universitätsklinikum) wählte im Dezember 2025 **Epic Systems** (Verona, Wisconsin, US-Privatunternehmen) als KIS-Anbieter — 200 Mio. EUR über zehn Jahre, Implementierung bis Ende 2029. Der Auslöser war erzwungen: SAP kündigt IS-H 2027 ab (Verlängerung bis 2030 zu erhöhten Kosten). [Quelle: Charité Pressemitteilung Dezember 2025]

Epic ist CLOUD-Act-Kategorie A — direkte US-Exposition unabhängig vom Datenstandort. Die Charité betont DSGVO-Konformität und Datenstandort Deutschland/EU, was notwendig aber nicht hinreichend ist. Die Entscheidung ist ein Signal: Mehr als 200 weitere IS-H-Kliniken stehen vor derselben Migration.

**Das Gegenbeispiel — Charité × Schwarz Digits:** Dieselbe Charité gründete im März 2026 mit Schwarz Digits (der Digitalsparte der Schwarz Gruppe, zu der auch STACKIT gehört) die "Schwarz Charité Health Data GmbH". Ziel: medizinische Daten sicher vernetzen und als Grundlage für KI-Anwendungen nutzen — auf STACKIT als Infrastrukturbasis. Das Joint Venture zeigt, dass die Charité den CLOUD-Act-Konflikt sieht: Für das KIS hat sie sich für Epic entschieden (Marktdruck durch IS-H-Abkündigung), für die Forschungsdatenplattform bewusst für einen europäischen Cloud-Anbieter. Zwei parallele Infrastrukturentscheidungen derselben Institution — eine US-exponiert, eine souverän.

---

## 12.5 Eintrittspfad 5: US-Konzernübernahmen und SaaS-Plattformen

**DAVASO/IQVIA — Rezeptabrechnung unter US-Jurisdiktion:** DAVASO (Leipzig) verarbeitet >50 % aller deutschen Apothekenrezepte (450 Mio./Jahr, ~22 Mrd. EUR). 2021 übernahm IQVIA (NYSE: IQV, Durham, North Carolina) DAVASO vollständig. Das Bundeskartellamt genehmigte nach Prüfung gemeinsam mit BMG, BAS und BfDI. CLOUD-Act-Konsequenz: IQVIA ist Kategorie A — Abrechnungsdaten von Millionen Kassenpatienten laufen durch ein US-Unternehmen. Die DSGVO schützt vor *kommerzieller* Weiternutzung — nicht vor US-Behördenzugriff. Seit 2025: IQVIA Health System Services (IQVIA HSS). [Quelle: Apotheke Adhoc, März 2026]

**Doctolib — 20 Millionen Nutzer, AWS-Infrastruktur:** Doctolib (Paris, FR) dominiert die Online-Terminbuchung in deutschen Arztpraxen. Die Plattform verarbeitet den vollständigen Patientenstammdatensatz jeder angeschlossenen Praxis — auch ohne App-Nutzung der Patienten. Infrastruktur: AWS Frankfurt (primär) und Paris (Spiegelung), explizit in der Datenschutzdokumentation dokumentiert. AWS ist Kategorie A. BSI C5 Typ 2 seit Juli 2025 — bescheinigt Informationssicherheit, nicht Abwesenheit von US-Behördenzugriff. [Quelle: Doctolib Datenschutzhinweise; HNO Nachrichten Dezember 2025]

---

## 12.6 Forschungsinfrastruktur — souverän wo möglich, heterogen in der Breite

**FDZ Gesundheit (BfArM)** — Positivbeispiel mit Vorbehalt: Das Forschungsdatenzentrum beim BfArM (Betrieb seit Oktober 2025) verwaltet GKV-Abrechnungsdaten von 73 Millionen Versicherten (2009–2023) in gesicherten virtuellen Analyseräumen. Daten verlassen den BfArM-Server nicht. Infrastruktur: deutsche Bundesbehörde, aufgebaut mit Bechtle (DE), SAP (DE) und Capgemini (FR). CLOUD-Act-Risiko strukturell gering — kritischer Punkt: externe Cloud-Tools von Forschenden im Analyseraum. [Quelle: BMG Pressemitteilung Oktober 2025]

**MII/DIZ — föderale Heterogenität:** Die Datenintegrationszentren der Medizininformatik-Initiative sind ohne einheitliche Cloud-Strategie entstanden. Einige DIZ betreiben souverän on-premise, andere auf Azure oder AWS. Dieselbe FHIR-basierte Dateninfrastruktur kann im selben Netzwerk auf EU-souveräner und auf US-exponierter Infrastruktur laufen — ohne dass dies für außenstehende Stellen transparent ist.

---

## 12.7 KIS-Markt: Überblick nach SAP IS-H-Abkündigung

| Anbieter | Eigentümer | CLOUD-Act | Installationen DE | Segment |
|---|---|---|---|---|
| **Dedalus/Orbis** | IT — Ardian PE (FR) | 🟢 EU-souverän | 821 | Akut (Marktführer) |
| **Oracle Cerner i.s.h.med** | NYSE: ORCL (US) | 🔴 Kat. A | ~250 | Akut (SAP-gebunden) |
| **NEXUS AG** | DE (börsennotiert) | 🟢 EU-souverän | 326 | Akut/Psychiatrie |
| **CGM Clinical** | DE (CVC-PE 28 %) | 🟡 PE-Vorbehalt | ~350 Akut | Akut + Reha ~900 ges. |
| **Meierhofer M-KIS** | DE/AT privat | 🟢 EU-souverän | ~260 (DACH) | Akut + Reha |
| **iMedOne (Telekom)** | DAX: DTE / T-Systems (C — Konzernhebel) | 🟡 Strukturell | ~240 | Akut |
| **Epic** | US (privat) | 🔴 Kat. A | 1 (Charité ab 2027) | Akut — im Aufbau |
| **Mesalvo** | DE privat | 🟢 EU-souverän | ~100–150 | Akut, wachsend |

---

## 12.8 Eintrittspfad 6: Telematikinfrastruktur — souverän in der Governance, exponiert im Betrieb

Die Telematikinfrastruktur (TI) ist das digitale Nervensystem des deutschen Gesundheitswesens: Sie verbindet alle Leistungserbringer in einem gemeinsamen Sicherheitsnetz und transportiert ePA (elektronische Patientenakte), E-Rezept, elektronische Arbeitsunfähigkeitsbescheinigung (eAU) und Versichertenstammdaten. Die gematik GmbH, die die TI reguliert und weiterentwickelt, steht zu 51 Prozent im Eigentum des Bundesministeriums für Gesundheit — sie ist keine US-Gesellschaft und unterliegt keiner US-Jurisdiktion. Soweit zur guten Nachricht.

Die schlechte: Im operativen Betrieb der TI sind US-Unternehmen tief verankert.

**IBM betreibt zwei Kerndienste.** IBM (Hauptsitz Armonk, New York — vollständig CLOUD-Act-exponiert) hat 2020 den Ausschreibungsgewinn für den Rezeptserver-Fachdienst erhalten und wurde im Dezember 2023 von der gematik als Identity-Provider-Anbieter zugelassen. IBM hat damit gleichzeitig Zugang zu Authentifizierungsinfrastruktur und zum zentralen eRezept-Transaktionsdienst. Die gematik betonte bei der Vergabe, der Betreiber könne Gesundheitsdaten "nicht auslesen". Das ist für Inhaltsdaten korrekt — aber CLOUD Act erfasst auch Metadaten, Verbindungsprotokolle und Systemzugriffe, nicht nur Klartextinhalte. [Quelle: Apotheke Wirtschaft, Heft 16/2025]

**Arvato Systems (Bertelsmann) trägt die Sicherheitsinfrastruktur.** Arvato Systems betreibt den zentralen Verzeichnisdienst, die KIM-Dienste (Kommunikation im Medizinwesen) und die übergreifende TI-Sicherheitsarchitektur. Arvato ist eine Tochter der deutschen Bertelsmann SE — formal kein US-Unternehmen. Das CLOUD-Act-Risiko ist deutlich geringer als bei IBM, aber nicht null, sofern Bertelsmann US-Tochtergesellschaften mit Datenzugang unterhält.

**TI 2.0 öffnet neue Einfallstore.** Unter TI 2.0 ersetzen cloudbasierte TI-Gateways die bisherigen Hardware-Konnektoren: Praxen und Kliniken mieten TI-Zugang als Managed Service von zertifizierten Anbietern. Wer diese Gateway-Betreiber sein werden und ob darunter US-Konzerne zugelassen werden, ist regulatorisch noch nicht abschließend definiert. Hier entsteht mit der Umstellung ein strukturell neues CLOUD-Act-Einfallstor. Die regulatorischen Auswirkungen von TI 2.0 werden in §17.1 vertieft.

**Risikomatrix TI:**

| TI-Komponente | Betreiber | CLOUD-Act-Risiko |
|---|---|---|
| Regulierung / Governance | gematik GmbH (BMG 51 %) | 🟢 Keines |
| Rezeptserver-Fachdienst | IBM (US) | 🔴 Real |
| Identity Provider | IBM (US, seit Dez. 2023) | 🔴 Real |
| Verzeichnisdienst / KIM | Arvato Systems (DE/Bertelsmann) | 🟡 Gering–mittel |
| Datenverschlüsselung | Ende-zu-Ende | 🟢 Strukturell geschützt |
| TI-Gateway-Betreiber (TI 2.0) | Noch offen | 🟡 Regulatorisch ungeklärt |

**Fazit:** Die TI ist kein US-Cloud-Problem im klassischen Sinne — ihre Governance und Verschlüsselung sind konzeptionell souverän. Aber IBM als CLOUD-Act-exponierter Betreiber von Rezeptserver und Identity Provider ist eine strukturelle Schwachstelle, die in der öffentlichen Debatte kaum thematisiert wird.

---

## 12.9 Sechs Eintrittspfade — Zusammenfassung

| Pfad | Mechanismus | Lösungsansatz |
|---|---|---|
| **GKV-Outsourcing** | RZ migriert zu Intermediär → US-Hyperscaler | EU-souveräne Cloud im AVV vorschreiben (OVHcloud-Modell) |
| **KV-IT-Abhängigkeit** | KV-Gemeinschaftsgesellschaft auf M365/Azure | Ausschreibungsgestaltung mit CLOUD-Act-Kriterium |
| **KIS-Neuausschreibung** | IS-H-Abkündigung → Epic/OCI-Migration | Dedalus/NEXUS als EU-Alternativen stärken |
| **US-Übernahme** | DAVASO/IQVIA — Übernahme nach Kartellprüfung | Nicht rückgängig zu machen; AVV-Schutzmechanismen |
| **SaaS-Plattform** | Doctolib auf AWS — C5 schützt nicht vor CLOUD Act | EU-Alternative fördern oder Migration zu EU-Anbietern |
| **Telematikinfrastruktur** | IBM betreibt TI-Kerndienste (Rezeptserver, IdP) | Nicht auflösbar — TI ist gesetzlich verpflichtend; Restrisiko dokumentieren |

---
