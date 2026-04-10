# 5. Anbieterbewertung: CLOUD-Act-Risiko und EU-Marktübersicht

## 5.1 Marktkontext

Die EU-Kommission hat im Oktober 2025 einen **180-Millionen-Euro-Tender** für souveräne Cloud-Services ausgeschrieben — die erste direkte Umsetzung des Cloud Sovereignty Framework mit 8 messbaren Souveränitätskriterien. Frankreich migriert seinen nationalen Gesundheitsdaten-Hub (67 Millionen Bürger) bis 2026 von Microsoft Azure zu einem SecNumCloud-zertifizierten Anbieter (SecNumCloud: strengstes EU-Cloud-Sicherheitszertifikat der französischen Behörde ANSSI). Die Suche nach "European cloud alternatives" ist 2025 um 660% gestiegen.

Marktverteilung Europa 2025: AWS ~30%, Microsoft Azure ~25%, Google Cloud ~15%, EU-Anbieter gesamt ~15%, Sonstige ~15%.

## 5.2 Die drei Risikofragen — Bewertungslogik

Das entscheidende Kriterium ist **nicht der Serverstandort, sondern die Unternehmensstruktur.** Für jeden Anbieter sind drei Fragen maßgeblich:

1. Ist das Unternehmen oder seine Muttergesellschaft in den USA börsennotiert oder hat Hauptsitz in den USA?
2. Unterhält das Unternehmen Niederlassungen, Tochtergesellschaften oder signifikante Geschäftsaktivitäten in den USA?
3. Gibt es eine indirekte Druckposition über eine US-Schwester- oder Tochtergesellschaft?

Wenn eine dieser Fragen mit Ja beantwortet wird: CLOUD-Act-Risiko real — unabhängig von Serverstandort, AVV (Auftragsverarbeitungsvertrag nach Art. 28 DSGVO) und SCCs (Standard Contractual Clauses — EU-Standardvertragsklauseln).

## 5.3 Zertifizierungsstandards im Vergleich

| Standard | Land | CLOUD-Act-Immunität | Stärke |
|---|---|---|---|
| **BSI C5:2026** | Deutschland | ❌ Nicht geprüft — nur technische Sicherheit (168 Kriterien, Apr. 2026) | Technische Mindestsicherheit |
| **BSI Souveränitätskriterien** | Deutschland | ⏳ Angekündigt — gemeinsam mit ANSSI (Nov. 2025), Veröffentlichung "in Kürze" | Noch nicht verfügbar |
| **SecNumCloud 3.2** | Frankreich | ✅ Explizit — max. 24%/39% nicht-EU-Anteile, EU-Personal | Strenger Souveränitätsstandard |
| **BSI Cloud Platform Requirements** | Deutschland | ✅ Implizit — deutsches Personal, kein US-Zugang | Für VS-NfD-Daten |
| **ISO 27001** | International | ❌ Nicht geprüft | Informationssicherheits-Baseline |
| **HDS** | Frankreich | ❌ Nicht direkt | Gesundheitsdaten-Hosting |
| **EUCS (blockiert)** | EU | Souveränitätsstufe gestrichen; Pattsituation seit 2024 | Nicht absehbar |

> **Kernaussage:** C5 belegt technische Sicherheit — nicht rechtliche Souveränität. Azure hat C5 und unterliegt dem CLOUD Act. plusserver hat C5 und unterliegt ihm strukturell nicht.

### Warum Frankreich SecNumCloud hat und Deutschland nicht

Die Tabelle oben zeigt eine auffällige Asymmetrie: Frankreich hat mit SecNumCloud 3.2 einen Cloud-Zertifizierungsstandard, der explizit vor extraterritorialen Gesetzen wie dem CLOUD Act schützt. Deutschland hat mit BSI C5 einen Standard, der nur technische Informationssicherheit prüft — die Jurisdiktionsfrage bleibt ausgeklammert. Diese Lücke ist kein Zufall, sondern das Ergebnis unterschiedlicher politischer Traditionen, konkreter Krisen und divergierender Lobbykonstellationen.

**Frankreichs Weg: Von der Souveränitätstradition zum Zertifizierungsstandard**

Frankreich hat eine gewachsene Tradition der *souveraineté numérique*. Der Begriff wurde 2014 von Pierre Bellanger (Gründer des Radiosenders Skyrock) in seinem gleichnamigen Buch geprägt und zwischen 2014 und 2017 auf drei nationalen Gipfeltreffen politisch verankert — aus diesen entstand das Institut de la Souveraineté Numérique als permanente Denkfabrik [174]. Diese Tradition speist sich aus demselben strategischen Denken, das auch Frankreichs nukleare Eigenständigkeit (*force de frappe*) begründet: Souveränität als nicht-delegierbare Kernaufgabe des Staates.

ANSSI (Agence nationale de la sécurité des systèmes d'information) veröffentlichte die erste SecNumCloud-Version 2016. Version 3.1 (2018) strich die Differenzierung in "Essential" und "Advanced" zugunsten eines einheitlichen Labels und harmonisierte mit der DSGVO. Der entscheidende Schritt war **Version 3.2 (März 2022)**: Erstmals enthielt der Standard explizite **Souveränitätsanforderungen** — über 360 Anforderungen in 14 Sicherheitsthemen, darunter die Kernklausel, dass qualifizierte Anbieter mehrheitlich in EU-Hand sein, ihren Hauptsitz in der EU haben und **nicht dem Recht von Nicht-EU-Staaten unterliegen** dürfen [175]. Konkret: maximal 24 % nicht-EU-Kapitalanteile pro Einzelaktionär und 39 % kollektiv, kein Vetorecht und keine Vorstandsmehrheit für Nicht-EU-Entitäten, ausschließlich EU-Personal mit Zugang zu Kundendaten, vollständige Immunität gegen extraterritoriale Gesetze.

**Der Auslöser: Die Health-Data-Hub-Krise**

Der konkrete Katalysator für die Souveränitätswende war die Kontroverse um den französischen Health Data Hub (Plateforme des données de santé). Die Plattform — konzipiert als zentraler Gesundheitsdatenpool für 67 Millionen Franzosen — wurde ursprünglich auf Microsoft Azure betrieben. 2020 intervenierte die CNIL (französische Datenschutzbehörde) und der Conseil d'État ordnete zusätzliche Schutzmaßnahmen an: Das Risiko eines US-Behördenzugriffs über den CLOUD Act sei real und durch technische Maßnahmen allein nicht eliminierbar. Die französische Regierung beschloss daraufhin die Migration zu einem SecNumCloud-zertifizierten Anbieter — eine Migration, die bis 2026 abgeschlossen wird [62]. Der Health Data Hub wurde zum politischen Symbol: Frankreich demonstrierte, dass Souveränität für Gesundheitsdaten keine abstrakte Forderung ist, sondern eine konkrete Infrastrukturentscheidung.

**Die Doctrine "Cloud au centre"**

Im Juli 2021 formalisierte Premierminister Jean Castex per Rundschreiben die *Doctrine Cloud au centre*: Cloud-Computing wird Voraussetzung für alle neuen digitalen Projekte des Staates. Für Daten "besonderer Sensibilität" — auch wenn sie keine personenbezogenen Daten im DSGVO-Sinne sind — ist die Nutzung eines **SecNumCloud-qualifizierten Anbieters verpflichtend** [176]. Die Doctrine wurde im Mai 2023 unter Premierministerin Borne aktualisiert und der Sensibilitätsbegriff erweitert. Im Januar 2026 bekräftigte Digitalministerin Anne Le Hénanff auf den *Rencontres de la souveraineté numérique* die Forderung nach einer "préférence européenne". Das Ergebnis: Ein wachsendes SecNumCloud-Ökosystem mit mittlerweile über einem halben Dutzend qualifizierten Anbietern (3DS Outscale, S3NS, Cloud Temple, OVHcloud, NumSpot, Scaleway in Prüfung) — ein Markt, den es ohne die staatliche Nachfragepolitik so nicht gäbe.

**Deutschlands Weg: C5 als pragmatischer Kompromiss**

Deutschland hat eine andere Tradition. Das BSI hat sich historisch als Behörde für **technische** Informationssicherheit definiert — nicht für geopolitische Souveränitätsfragen. Der BSI C5-Katalog (Cloud Computing Compliance Criteria Catalogue) wurde 2016 veröffentlicht, zeitgleich mit SecNumCloud 1.0, aber mit einem fundamental anderen Ansatz. Die am 7. April 2026 veröffentlichte aktuelle Version **C5:2026** prüft 168 Kriterien in 17 Domänen — Verschlüsselung, Zugriffskontrolle, Netzwerksicherheit, Container-Management, Post-Quanten-Kryptographie, Confidential Computing — und beantwortet die Frage "Ist der Cloud-Dienst technisch sicher?" [188]. Die Frage "Kann eine ausländische Regierung den Anbieter zur Herausgabe zwingen?" wird auch in C5:2026 **bewusst nicht gestellt** — obwohl der Katalog strukturell an das europäische EUCS angelehnt wurde [177].

Für den Bereich der Verschlusssachen (VS-NfD und höher) existiert mit den **BSI Cloud Platform Requirements** ein strengerer Maßstab, der de facto Souveränitätsanforderungen stellt: deutsches Personal, keine US-Zugriffsmöglichkeit, BSI-Prüfung aller Updates. Aber dieses Instrument ist nicht als öffentlicher Marktstandard konzipiert — es gilt nur für die Bundesverwaltung und Delos Cloud ist der erste (und bisher einzige) Nutzer im US-Technologie-Kontext. Für den regulären Gesundheitsmarkt bleibt C5 der Referenzstandard — und § 393 SGB V hat C5 als Pflichttestat verankert, ohne eine Souveränitätsprüfung danebenzustellen. Symptomatisch: Das BSI hat mit AWS eine Kooperationsvereinbarung unterzeichnet und begrüßte die AWS European Sovereign Cloud in Brandenburg als Beitrag zur europäischen Souveränität [185] — eine Position, die diametral zu ANSSIs Haltung steht, wonach US-Hyperscaler ohne strukturelle Trennung grundsätzlich nicht souveränitätsfähig sind.

C5:2026 (veröffentlicht 7. April 2026) ist ein substanzieller Fortschritt bei der technischen Sicherheit — 168 statt 121 Kriterien, erstmals Confidential Computing und Post-Quanten-Kryptographie, strukturell an EUCS angelehnt [188]. Aber die Souveränitätsfrage bleibt auch in C5:2026 **ausgeklammert**: Das BSI hat angekündigt, Souveränitätskriterien als **separates Dokument** "in Kürze" zu veröffentlichen — nicht als integralen Bestandteil der Zertifizierung [186]. Der Unterschied zu Frankreich bleibt damit strukturell: ANSSI hat Souveränität in den Zertifizierungsstandard selbst eingebaut. Das BSI hält Souveränität und technische Sicherheit getrennt — auch in der neuesten Version.

**Das EUCS-Scheitern — und Deutschlands Rolle**

Die Chance auf eine europäische Harmonisierung bestand im EUCS (European Cybersecurity Certification Scheme for Cloud Services), das unter dem Cybersecurity Act von ENISA entwickelt wurde. Der ursprüngliche Entwurf sah eine höchste Stufe ("High+") mit Souveränitätsanforderungen nach SecNumCloud-Vorbild vor: EU-Eigentum, EU-Hauptsitz, Immunität gegen extraterritoriale Gesetze. Frankreich, Italien und Spanien unterstützten diese Stufe.

Die Opposition kam aus zwei Richtungen: Erstens lobbyierten US-Industrieverbände massiv gegen die Souveränitätsstufe — der US Council for International Business (USCIB), die US Chamber of Commerce und der Information Technology Industry Council (ITI) forderten öffentlich die Streichung der Souveränitätsanforderungen [178]. The Register dokumentierte, dass US-Lobbyisten Studien finanzierten, die die EU-Regulierung als handelsfeindlich darstellten [179]. Zweitens reichten sieben EU-Mitgliedstaaten — darunter die Niederlande, Dänemark, Schweden und Estland — ein Non-Paper ein, das die Souveränitätsstufe als "diskriminierend gegenüber Nicht-EU-Anbietern" ablehnte [180].

Deutschlands Position war ambivalent: Anfangs unterstützte Deutschland in Abstimmung mit Frankreich die Souveränitätsstufe, schwenkte dann aber unter innenpolitischem Industriedruck um und schloss sich der Oppositionsgruppe an [180]. Die European Business Review beschrieb die Situation 2024 als zunehmendes "Auseinanderdriften" von Frankreich und Deutschland in der Cloud-Souveränitätsfrage [181]. Bitkom — Deutschlands größter Digitalverband, dessen Mitglieder sowohl deutsche als auch US-Anbieter umfassen — unterstützte zwar grundsätzlich digitale Souveränität (78 % der befragten Unternehmen im Bitkom Cloud Report 2025 halten Deutschland für zu abhängig von US-Cloud-Anbietern), vermied aber die Forderung nach harten Eigentümerschaftskriterien [182]. Das Ergebnis: Die Souveränitätsstufe wurde aus dem EUCS-Entwurf gestrichen. Stand April 2026 befindet sich das EUCS in einer Pattsituation — das cep (Centrum für Europäische Politik) bezeichnete die Situation im April 2025 als "Impasse" [183]. Frankreich behält SecNumCloud als nationalen Standard bei. Deutschland hat nichts Vergleichbares.

**Gaia-X — der gescheiterte gemeinsame Ansatz**

Gaia-X, 2019 als deutsch-französisches Prestigeprojekt unter Bundeswirtschaftsminister Altmaier und seinem französischen Amtskollegen Le Maire gestartet, sollte ein europäisches Cloud-Ökosystem mit gemeinsamen Souveränitätsstandards schaffen. Das Projekt scheiterte an der Governance: US-Hyperscaler (AWS, Microsoft, Google) wurden als Mitglieder aufgenommen, Souveränitätsanforderungen blieben als "Labels" unverbindlich [184]. Frankreich zog daraus den Schluss, den eigenen Weg mit SecNumCloud zu vertiefen. Deutschland verblieb ohne gleichwertigen Standard.

**Ansätze zur Konvergenz — und ihre Grenzen**

Drei jüngere Entwicklungen deuten auf ein deutsches Umdenken hin — wobei die Lücke bis heute fortbesteht:

**Erstens** veröffentlichten ANSSI und BSI am 17. November 2025 ein **gemeinsames Statement zu Cloud-Souveränitätskriterien**, unterzeichnet von ANSSI-Generaldirektor Vincent Strubel und BSI-Präsidentin Claudia Plattner [189]. Darin verpflichten sich beide Behörden, gemeinsam Souveränitätskriterien auf Basis des EU Cloud Sovereignty Framework zu entwickeln — mit konkreten Anforderungen: strikte Datenlokalisierung, ausschließliche Anwendung europäischen Rechts, **kein Zugang durch nicht-europäische Dritte**, und Geschäftskontinuität ohne außereuropäische Akteure oder Technologien. Entscheidend: Das Statement führt eine **Progressionslogik** ein — nicht binär (souverän/nicht-souverän), sondern drei Stufen: minimale Rechtskonformität, erweiterter operativer Kontrolle und volle strategische Autonomie. Wo das Nicht-Erfüllen disqualifizierend wirkt, soll die Methodik festlegen.

**Zweitens** veranstalteten Macron und Bundeskanzler Merz am 18. November 2025 den **Gipfel für Europäische Digitale Souveränität** in Berlin (900+ Teilnehmer) mit privatwirtschaftlichen Investitionszusagen von über 12 Mrd. EUR und einer gemeinsamen Task Force [187].

**Drittens** schlug die EU-Kommission im März 2025 eine Überarbeitung des Cybersecurity Act vor, die erstmals "nicht-technische Anforderungen" in Zertifizierungsschemata ermöglichen würde — ein Türöffner, um Souveränitätskriterien doch noch in EUCS zu verankern [183].

Das ANSSI-BSI-Statement ist der bislang konkreteste Schritt. Aber: Die angekündigten gemeinsamen Souveränitätskriterien sind bislang nicht veröffentlicht. C5:2026 (7. April 2026) enthält sie nicht. Solange die Kriterien nicht vorliegen, bleibt die Lücke operativ bestehen: Frankreich zertifiziert Souveränität seit 2022. Deutschland plant es — noch.

**Die strukturelle Konsequenz für das Gesundheitswesen**

| Dimension | Frankreich | Deutschland |
|---|---|---|
| **Zertifizierungsstandard** | SecNumCloud 3.2 (seit 2022) | BSI C5:2026 (April 2026, nur technische Sicherheit) |
| **Souveränitätsprüfung** | ✅ Seit 2022 in Zertifizierung integriert | ⏳ ANSSI-BSI-Statement Nov. 2025: Souveränitätskriterien angekündigt, noch nicht veröffentlicht |
| **Staatliche Nachfragepolitik** | Doctrine "Cloud au centre" (2021, 2023) | § 393 SGB V: C5 als Pflicht, keine Souveränitätspflicht |
| **Gesundheitsdaten-Konsequenz** | Health Data Hub → Migration weg von Azure | ePA / FDZ: Keine vergleichbare Migrationsentscheidung |
| **Zertifizierte souveräne Anbieter** | 6+ (Outscale, S3NS, Cloud Temple, OVHcloud, NumSpot…) | 0 (C5:2026 prüft Souveränität nicht) |
| **EU-Harmonisierung (EUCS)** | Aktiv für Souveränitätsstufe | Seit Nov. 2025: gemeinsamer Ansatz mit FR (ANSSI-BSI-Statement) |

Die Konsequenz ist konkret: In Frankreich kann ein Krankenhaus einen SecNumCloud-zertifizierten Anbieter auswählen und darauf vertrauen, dass die Zertifizierung die CLOUD-Act-Frage adressiert. In Deutschland muss jede Organisation die Jurisdiktionsprüfung eigenständig durchführen — das C5-Testat sagt darüber nichts aus. Frankreich hat den Markt durch regulatorische Nachfrage geschaffen. Deutschland überlässt die Souveränitätsentscheidung dem Einzelnen.

## 5.4 DACH-Kernmarkt: Risikoübersicht

Die Tabelle unterscheidet drei Risikotypen, die unterschiedliche CLOUD-Act-Konsequenzen haben:

- **Typ A — Direkte US-Institution:** Eigene US-Niederlassung, US-Tochtergesellschaft oder US-Muttergesellschaft, die denselben Cloud-Dienst betreibt oder direkten Datenzugriff hat. Herausgabepflicht direkt erzwingbar.
  - *Direkt:* US-Hauptsitz / US-Mutter (Oracle, Microsoft, AWS, Qlik)
  - *Indirekt:* EU-Mutter mit US-Cloud-Tochter im gleichen Geschäftsfeld (Hetzner US LLC, IONOS Cloud Inc., OVH US Corp.)
- **Typ B — US-Technologieabhängigkeit:** Europäischer Anbieter, aber US-Software, US-Lizenz oder US-Infrastrukturpartner. Kein direkter CLOUD-Act-Zugriff auf EU-Kundendaten, aber Restrisiko über den Lieferanten.
- **Typ C — Konzernhebel:** EU-Unternehmen mit US-Tochter oder US-Schwester in einem *anderen* Geschäftsfeld, die keinen operativen Zugriff auf Cloud-Kundendaten hat. CLOUD-Act-Zugriff nur über indirekten Unternehmensdruck möglich — nicht über direkte Datenhoheit. Gilt sowohl für formale Tochterbeziehungen (Deutsche Telekom → T-Mobile US/Telekommunikation) als auch für eigentümerschaftlich verbundene Schwestergesellschaften (Schwarz-Gruppe → Lidl US/Handel).

| Anbieter | C5 | Börse / Eigentümer | US-Verbindung | Risikotyp | CLOUD-Act-Risiko | Regionale Datenhaltung | Empfehlung |
|---|---|---|---|---|---|---|---|
| **Oracle Cerner / OCI** | Nein | NYSE: ORCL | US-Hauptsitz Austin/TX | **A — direkt** | 🔴 Hoch | Frankfurt (EU Sovereign), Madrid | KIS-Migration (KIS = Krankenhausinformationssystem) auf OCI: CLOUD-Act-Exposition ungelöst |
| **Microsoft Azure** | ✅ | NYSE: MSFT | US-Muttergesellschaft | **A — direkt** | 🔴 Hoch | Frankfurt (GWC), Amsterdam | Nicht für Gesundheitsdaten |
| **AWS Germany** | ✅ | NASDAQ: AMZN | AWS Germany = US-Tochter | **A — direkt** | 🔴 Hoch | Frankfurt (eu-central-1) | Nicht für Gesundheitsdaten |
| **Qlik Cloud** | Nein (C5 geplant Q1 2026) | US-Unternehmen (PA, Thoma Bravo) | US-Hauptsitz | **A — direkt** | 🔴 Hoch | Frankfurt, Irland, Paris, London, Mailand (alle auf AWS) | Nicht für Gesundheitsdaten — Frankfurt-Region ändert US-Jurisdiktion nicht |
| **OVHcloud** | ✅ 2025 | Euronext Paris | OVH US Corp. (eigene US-Tochter) | **A — indirekt** | 🔴 Bestätigt | Strasbourg, Roubaix, Paris, Frankfurt | SNC-Tier für regulierte Workloads |
| **Hetzner (EU-RZ)** | ✅ Feb. 2026 | Privat (DE) | Hetzner US LLC (eigene US-Cloud-Tochter) | **A — indirekt** | 🟠 Bedingt | Nürnberg, Falkenstein (DE); Helsinki (FI) | Dev/SMB; nicht für § 393-Daten |
| **Arvato Systems** | ✅ | Bertelsmann (privat, DE) | AWS + Azure als Infrastrukturpartner | **B — Technologie** | 🔴 Indirekt | Gütersloh (3 eigene RZ, DE) | Eigene RZ, aber US-Software-Risiko |
| **Delos Cloud (SAP × Azure)** | BSI CPR | SAP SE (DAX) | Microsoft = Technologielieferant (lizenziert) | **B — Technologie** | 🟡 Operator-Modell | Frankfurt (Azure Germany West Central) | Für M365/Azure-abhängige Verwaltung |
| **SAP BTP / RISE** | Teilweise | DAX: SAP SE | Eigene US-Niederlassungen (SAP America) | **A + B** | 🟡 Infrastrukturell | Frankfurt (Azure GWC + AWS eu-central-1) | Je nach Hosting-Variante prüfen |
| **IONOS** | ✅ 2023 | MDAX: UTDI | IONOS Cloud Inc. (eigene US-Cloud-Tochter) | **A — indirekt** | 🟠 BMI-bestätigt | Karlsruhe, Berlin, Frankfurt, Nürnberg (DE) | Prüfung erforderlich |
| **Deutsche Telekom / OTC** | ✅ | DAX: DTE (ADR: NYSE DTEGY) | T-Mobile US = Telekom-Tochter, kein Cloud-Betrieb | **C — Konzernhebel** | 🟡 Strukturell | Biere/Sachsen-Anhalt, Magdeburg (DE); NL | Mit Vorbehalt — T-Mobile US hat keinen Zugriff auf OTC-Daten |
| **STACKIT** | ✅ C5 Typ 2 (Aug. 2024) | Privat (Schwarz Gruppe, DE) | Lidl US = Handelsschwester (kein Datenzugriff) | **C — Konzernhebel** | 🟡 Juristisch unklar | Neckarsulm, Düsseldorf (DE); Wien (AT) | Valide mit Vorbehalt |
| **plusserver** | ✅ C5 | Privat (DE) | Keine | **Keiner** | 🟢 Gering | Köln, Hamburg, Frankfurt (DE) | Sauberste DE-Option |
| **EWERK Leipzig** | ISO 27001, ISAE 3402 Typ II (C5 in Vorbereitung) | NORD Holding (DE, privat) + Gründer | Keine | **Keiner** | 🟢 Gering | Leipzig (DE) | KRITIS-Spezialist (Kritische Infrastrukturen — gesetzliche Einstufung systemrelevanter Sektoren); C5-Testat angestrebt |

## 5.5 Juristische Detailanalysen

Die Tabelle in 5.4 zeigt die Risikoeinstufung — dieser Abschnitt erklärt für die kritischen Fälle, **warum** die jeweilige US-Verbindung zum CLOUD-Act-Risiko führt. Die Logik folgt den drei Konstellationen aus Kapitel 2:

- **Konstellation A:** US-Mutter → EU-Tochter. Herausgabepflicht direkt durchsetzbar, kein Widerspruch möglich.
- **Konstellation B:** EU-Mutter → US-Tochter. EU-Mutter kann widersprechen, aber US-Tochter ist Druckmittel.
- **Konstellation C:** Schwestergesellschaften oder Konzernhebel über ein anderes Geschäftsfeld. Juristisch unklar, praktisch geringes Risiko wenn kein operativer Datenzugriff besteht.

> **Hinweis Konstellationen ↔ Risikotypen (§5.4):** Die juristischen Konstellationen (A/B/C aus Kapitel 2) beschreiben die *Rechtsbeziehung* zwischen EU- und US-Entität. Die Risikotypen in der Tabelle §5.4 fassen die daraus resultierenden *praktischen Risiken* zusammen: Typ A-direkt = Konstellation A, Typ A-indirekt = Konstellation B, Typ B = kein Konstellation-Äquivalent (reine Technologieabhängigkeit), Typ C = Konstellation C.

### Hetzner — eigene US-Tochter als Druckmittel (Konstellation B)

Hetzner Online GmbH (Gunzenhausen/Bayern) ist ein deutsches Privatunternehmen mit C5-Testat seit Februar 2026. Auf den ersten Blick souverän. Aber: Hetzner betreibt **Hetzner US LLC** in Ashburn, Virginia — eine eigene US-Tochtergesellschaft für den US-Rechenzentrumsmarkt. Hetzner dokumentiert selbst: "Hetzner kann nicht damit dienen, keine Verbindung zu den USA zu haben."

Die juristische Konsequenz (Konstellation B): Hetzner Online GmbH (EU-Mutter) kann einer CLOUD-Act-Anfrage widersprechen und DSGVO Art. 48 geltend machen. Aber US-Behörden können die Hetzner US LLC unter Druck setzen — Geschäftslizenzen, Strafen, Betriebsaussetzung — als indirekten Hebel gegen die deutsche Mutter. Das ist strukturell risikoreicher als ein Anbieter ohne jede US-Präsenz, aber kein direkter Herausgabezwang.

Callista-Benchmark (Februar 2026): Hetzner liefert das 14,3-fache Preis-Leistungs-Verhältnis gegenüber AWS on-demand. Für Dev-Teams und unkritische Workloads weiterhin erste Wahl. Für KRITIS-relevante Gesundheitsdaten nach § 393 SGB V: plusserver oder EWERK Leipzig bevorzugen.

### STACKIT / Schwarz Gruppe — Schwestergesellschaft ohne Konzernverbund (Konstellation C)

STACKIT (Schwarz Digits KG, Neckarsulm) ist die Cloud-Marke der Schwarz Gruppe. Zur Schwarz Gruppe gehören auch Lidl und Kaufland — mit über 200 Filialen an der US-Ostküste sowie PreZero (Umweltdienstleistungssparte der Schwarz Gruppe) mit 430 US-Standorten. Diese US-Aktivitäten sind der Kern des Risikoverdachts.

Die entscheidende gesellschaftsrechtliche Besonderheit: Die Schwarz Gruppe ist **kein Konzern im handelsrechtlichen Sinne**. Lidl Stiftung, Schwarz Digits (STACKIT) und PreZero sind Schwestergesellschaften unter demselben Privateigentümer (Dieter Schwarz) — aber **gesellschaftsrechtlich nicht miteinander verbunden**. Es gibt keine Beherrschungs- oder Gewinnabführungsverträge. STACKIT ist nicht Tochter von Lidl — beide sind eigenständige Gesellschaften.

**Warum das relevant ist:** Der CLOUD Act knüpft an "possession, custody, or control" an — nicht an bloße Eigentümeridentität. US-Gerichte müssten nachweisen, dass Lidl US tatsächlich Kontrolle über STACKIT-Daten hat, was bei gesellschaftsrechtlicher Trennung und ohne operative Verbindung schwer zu begründen ist. STACKIT-CEO Bernd Wagner: *"Wir investieren nicht in den USA. Es ergibt keinen Sinn, denn somit würden wir sofort den Regularien des US Cloud Act unterliegen."*

**Bewertung:** STACKIT ist strukturell besser aufgestellt als Hetzner und IONOS (keine eigene US-Cloud-Tochter, keine US-Primärnotierung). Gegenüber der Open Telekom Cloud (OTC) / Deutsche Telekom ist STACKIT auf vergleichbarer Risikostufe: Beide sind Typ-C-Konstellationen, bei denen die US-Präsenz in einem anderen Geschäftsfeld liegt und keinen direkten Zugriff auf Cloud-Kundendaten hat — der Unterschied ist, dass die Schwarz-Gruppe-Verbindung informell (Eigentümerschaft) ist, während Deutsche Telekom AG formal die Muttergesellschaft von T-Mobile US ist. Die Unsicherheit liegt in der bislang ungeklärten Frage, ob US-Gerichte die Eigentümeridentität als "control" werten würden — juristisch nicht abschließend beantwortet, praktisch unwahrscheinlich solange STACKIT auf US-Investitionen verzichtet.

### Arvato Systems — US-Softwareabhängigkeit ohne eigene US-Institution (Typ B)

Arvato ist der Sonderfall Typ B: keine eigene US-Tochter, keine US-Börsennotierung, kein US-Eigentümer — aber operative Abhängigkeit von US-Software. Arvato ist AWS Premier Partner und betreibt als Technologiepartner die Delos Cloud auf Azure-Basis. Das bedeutet: Die US-Unternehmen AWS und Microsoft haben über ihre Software-/Lizenzbeziehung mit Arvato einen potenziellen Ansatzpunkt.

Der CLOUD Act gilt für den US-Provider (AWS, Microsoft) — nicht für Arvato selbst. Arvato ist nicht zur Herausgabe verpflichtet. Aber: AWS oder Microsoft könnten ihrerseits verpflichtet werden, Zugang zu Daten zu verschaffen, die auf Arvato-Hardware mit AWS- oder Azure-Software laufen. Das Risiko liegt also auf der Software-Ebene, nicht auf der Arvato-Unternehmensebene.

### Deutsche Telekom / Open Telekom Cloud — Telekomtochter als Konzernhebel (Konstellation C)

Deutsche Telekom AG (Bonn, DAX: DTE) ist ein deutsches Unternehmen — die NYSE-Notierung DTEGY ist ein American Depositary Receipt (ADR), kein primäres US-Listing. Die entscheidende US-Verbindung ist T-Mobile US Inc., eine börsennotierte US-Mobilfunktochtergesellschaft, an der Deutsche Telekom rund 48 % hält.

**Warum das weniger riskant ist als zunächst sichtbar:** T-Mobile US ist ein Telekommunikationsunternehmen. Es betreibt keine Cloud-Infrastruktur, hat keinen Zugriff auf Daten der Open Telekom Cloud und teilt keine IT-Systeme mit T-Systems (dem OTC-Betreiber). T-Mobile US und T-Systems sind Schwestergesellschaften unter derselben Konzernmutter — operativ vollständig getrennt.

**Die CLOUD-Act-Mechanik in dieser Konstellation:** US-Behörden könnten T-Mobile US nutzen, um Druck auf Deutsche Telekom AG auszuüben — und Deutsche Telekom AG könnte theoretisch zur Herausgabe von T-Systems/OTC-Daten angehalten werden, weil sie als Konzernmutter Kontrolle über T-Systems ausübt. Aber dieser Weg ist lang: (1) CLOUD-Act-Beschluss gegen T-Mobile US, (2) Übertragung auf Deutsche Telekom AG als Mutter, (3) Verpflichtung Deutsche Telekoms zur Weitergabe von T-Systems-Daten — gegen ausdrückliches DSGVO-Widerspruchsrecht. Kein direkter Datenzugriff, keine geteilte Infrastruktur.

**Abgrenzung zu Hetzner / IONOS:** Hetzner US LLC und IONOS Cloud Inc. sind US-Cloud-Betreiber im selben Sektor. Sie haben strukturell administrativen Zugriff auf Systeme, die zum selben Unternehmensverbund gehören. T-Mobile US hat das nicht. Deshalb ist Deutsche Telekom / OTC als **C — Konzernhebel** einzustufen, nicht als A — indirekt.

**OTC-Rechenzentren:** Sachsen-Anhalt (Biere, 100.000 Server, 18 MW) + Magdeburg-Region; sowie eine Niederlande-Region. T-Systems betreibt 33 RZ weltweit, 7 im Eigenbetrieb — ausschließlich europäischer Standortbetrieb für OTC.

### IONOS — US-Tochter trotz europäischer Börsennotierung (Konstellation B)

IONOS SE ist an der MDAX-notierten United Internet AG (DE) angebunden — auf den ersten Blick ein europäisches Unternehmen. Das Problem: IONOS betreibt **IONOS Cloud Inc.** in den USA als eigene US-Tochtergesellschaft.

Das BMI-Gutachten der Universität Köln stellt klar: Für die Anwendbarkeit des CLOUD Act reicht eine US-Niederlassung aus — unabhängig davon, wo die Mutter börsennotiert ist. IONOS US Inc. ist eine US-Person im Sinne des CLOUD Act. Über sie können US-Behörden Druck auf die europäische Mutter ausüben (Konstellation B). IONOS wirbt mit CLOUD-Act-Schutz für EU-Daten — diese Aussage ist formal nicht falsch (direkte Herausgabe wäre anfechtbar), unterschlägt aber den indirekten Druckmechanismus.

### EWERK Leipzig — Private-Equity-Übernahme: Auswirkung auf CLOUD-Act-Bewertung

EWERK Leipzig hat 2024 mit der NORD Holding einen neuen Mehrheitsgesellschafter erhalten. Die relevante Frage für die CLOUD-Act-Bewertung: Ändert ein Private-Equity-Eigentümer das Risikoprofil?

**NORD Holding:** Deutsches Private-Equity-Unternehmen mit Sitz in Hannover, gegründet 1969, ~4 Mrd. EUR verwaltetem Vermögen, ausschließlich DACH-fokussiert (Deutschland, Österreich, Schweiz). Betrieb als "Evergreen Fund" aus eigener Bilanz ohne Laufzeitbeschränkung. Keine US-Börsennotierung, keine US-Niederlassungen, keine US-Investoren in der Struktur öffentlich erkennbar. Rechtsform: GmbH, Registrierung Amtsgericht Hannover.

**CLOUD-Act-Konsequenz:** Entscheidend ist nicht der PE-Eigentümer als solcher, sondern ob der Eigentümer "possession, custody, or control" über Daten im Sinne des CLOUD Act ausübt und ob dieser Eigentümer unter US-Jurisdiktion fällt. Beides ist bei NORD Holding nach aktuellem Kenntnisstand nicht der Fall. Die Übernahme ändert das CLOUD-Act-Risikoprofil von EWERK nicht.

**BSI C5 — aktueller Stand:** EWERK ist nach ISO 27001, ISO 20000 und ISAE 3402 Typ II zertifiziert — die unmittelbare Voraussetzung für eine C5-Zertifizierung ist damit geschaffen. Ein BSI C5 Typ 2 Testat für die Cloud-Infrastruktur ist nach Unternehmensangaben in Vorbereitung. Sobald dieses vorliegt, ist EWERK vollständig § 393 SGB V-konform für die Verarbeitung von Gesundheitsdaten in der Cloud. Zum Vergleich: STACKIT hat C5 Typ 2 bereits seit August 2024, plusserver seit längerer Zeit. Für Ausschreibungen ab Juli 2025 sollte der C5-Status im Vertrag explizit als Bedingung verankert und nach Vorliegen des Testats erneut geprüft werden. [Quelle: Energieforen Leipzig, EWERK Zertifizierungsseite; Trusted Cloud, EWERK Digital Profil]

**Vorbehalt:** PE-Eigentümer können Portfoliounternehmen weiterveräußern. Falls EWERK in Zukunft an einen US-kontrollierten Käufer verkauft werden sollte, würde sich das Risikoprofil ändern. Für GKVen und Kliniken, die EWERK als souveränen Anbieter einplanen, empfiehlt sich eine Change-of-Control-Klausel im AVV, die eine Neuprüfung bei Eigentümerwechsel vorsieht.

### Oracle / Oracle Cerner — der unsichtbare Marktführer im Klinik-KIS

Oracle spielt im deutschen Gesundheitswesen eine strukturell wichtige, aber in der öffentlichen CLOUD-Act-Debatte völlig übersehene Rolle. Der Konzern ist in zwei Funktionen präsent, die beide relevant sind:

**Funktion 1 — Krankenhausinformationssysteme (KIS):** Oracle Cerner betreibt das KIS i.s.h.med, das in rund 250 deutschen Krankenhäusern eingesetzt wird — darunter viele Universitätsklinika und große kommunale Häuser. i.s.h.med ist das einzige vollständig in SAP IS-H integrierte Klinik-IT-System; es erfasst medizinische Daten von der Anamnese über die Diagnose bis zur Nachbehandlung. Oracle hat Cerner 2022 für 28 Milliarden US-Dollar übernommen. [Quelle: Wikipedia i.s.h.med; kma-online.de, April 2024]

Damit ist Oracle — ein US-Konzern mit Hauptsitz in Austin, Texas, NYSE: ORCL — der direkte Verarbeiter sensibelster klinischer Patientendaten in einem Viertel der deutschen Kliniken. Oracle unterliegt dem CLOUD Act uneingeschränkt: direkte US-Muttergesellschaft, NYSE-Notierung, US-Hauptsitz. Kein Konnektor zur TI, keine Middleware — Oracle Cerner ist der direkte Betreiber des klinischen Kernsystems.

**Die Managed-Service-Frage — reduziert das Risiko, eliminiert es aber nicht:** Viele Kliniken betreiben i.s.h.med nicht auf Oracle-Cloud-Infrastruktur, sondern auf eigenen Servern oder bei einem deutschen Rechenzentrumsbetreiber. Oracle Cerner übernimmt in diesem Fall den Managed Service — Administration, Updates, Second-Level-Support — ohne das Rechenzentrum selbst zu betreiben. Die naheliegende Annahme ist: Wenn die Server in Deutschland stehen und dem Klinikum gehören, ist das CLOUD-Act-Risiko gebannt.

Diese Annahme ist falsch. Der CLOUD Act knüpft an "possession, custody, or control" an — nicht an den Besitz der Hardware. Oracle Cerner hat als Managed-Service-Betreiber in der Regel administrativen Fernzugriff auf die Systeme: um Patches einzuspielen, Konfigurationen anzupassen, Fehler zu analysieren. Dieser Fernzugriff bedeutet "control" im Sinne des CLOUD Act. Es ist technisch irrelevant, wem der Server gehört — entscheidend ist, ob Oracle Cerner auf die Daten zugreifen kann. Und bei einem KIS-Managed-Service ist genau das der Fall, weil Support und Wartung eines Krankenhausinformationssystems ohne Klartextzugriff auf Patientendaten praktisch nicht möglich sind.

Die Differenzierung ist dennoch wichtig: Ein Managed Service ohne Cloud-Migration ist eine geringere Exposition als eine vollständige OCI-Migration, bei der Oracle nicht nur den Zugriff, sondern auch den physischen Besitz aller Daten hat. Bei einer OCI-Migration liegt alles — Speicher, Compute, Backup — bei einem US-Hyperscaler. Beim Managed Service liegt die Infrastruktur beim Klinikum oder bei einem deutschen Betreiber; Oracle hat "nur" den administrativen Zugang. Das ist ein gradueller Unterschied, kein kategorischer. Für die DSGVO-Bewertung bleibt in beiden Fällen ein TIA erforderlich (vgl. §17.4), und in beiden Fällen muss der Auftragsverarbeitungsvertrag die CLOUD-Act-Exposition adressieren (vgl. §16.5).

Für Kliniken, die heute i.s.h.med im Managed-Service-Modell betreiben und eine Entscheidung über die Zukunft treffen müssen, ergibt sich eine klare Reihenfolge: Die Migration auf OCI vertieft die Exposition. Der Verbleib im Managed-Service-Modell auf eigener Infrastruktur reduziert sie relativ, löst sie aber nicht. Nur der Wechsel auf ein europäisches KIS — Dedalus, CGM, NEXUS, Meierhofer — oder ein Betriebsmodell, bei dem Oracle keinen administrativen Klartextzugriff mehr hat, eliminiert das CLOUD-Act-Risiko strukturell.

**Funktion 2 — Oracle Cloud Infrastructure (OCI) als geplanter Nachfolger:** Oracle entwickelt eine cloud-basierte Nachfolgelösung für i.s.h.med auf der Oracle Cloud Infrastructure (OCI). Der Hintergrund: SAP hat die Branchenlösung IS-H, auf der i.s.h.med aufbaut, zum Ende 2027 abgekündigt (optional erweiterte Wartung bis 2030). Damit stehen bis zu 300 Kliniken vor einem KIS-Wechsel. [Quelle: DSAG-Aussage, kma-online.de, April 2024] Oracle positioniert OCI als die natürliche Migrationsplattform für bestehende i.s.h.med-Kunden.

**Was OCI ist und wie Oracle die CLOUD-Act-Frage kommuniziert:** OCI ist Oracles Hyperscaler-Cloud — direkt vergleichbar mit Azure oder AWS. Oracle betreibt in Frankfurt und Madrid sogenannte EU Sovereign Cloud Regionen, die physisch von der US-Infrastruktur getrennt sind und von EU-Ansässigen betrieben werden sollen. Oracle argumentiert, dass eine separate EU-Rechtseinheit eine CLOUD-Act-Anfrage wegen fehlender "possession, custody, or control" über EU-Daten ablehnen könne. [Quelle: Oracle Blog, "Oracle sovereign cloud solutions: Providing transparent review of data access requests", 2024]

**CLOUD-Act-Bewertung für OCI EU Sovereign Cloud:** Dieselbe Argumentation verfolgen auch Microsoft (Azure EU Data Boundary) und AWS (European Sovereign Cloud) — und die juristische Bewertung ist die gleiche: Oracle Corp. ist das US-Mutterunternehmen. Ob eine EU-Tochtergesellschaft tatsächlich vor einem US-Herausgabebeschluss schützt, ist rechtlich offen und nicht durch eine EU-Tochterstruktur allein auflösbar. Die Oracle EU Sovereign Cloud ist Risikotyp A (eigene US-Mutter) mit Operator-Modell-Argumentation — ähnlich wie Delos Cloud, aber ohne die BSI-CPR-Zertifizierung und ohne unabhängige staatliche Prüfung der Souveränitätsarchitektur.

**Die strategische Bedeutung:** Die SAP-IS-H-Abkündigung löst bis 2030 eine massive KIS-Migrationswelle aus. Oracle Cerner ist bereits in 250 deutschen Kliniken verankert und bietet den "natürlichsten" Migrationspfad auf OCI an. Kliniken, die diesem Weg folgen, migrieren ihre sensibelsten Patientendaten von einem US-Primärsystem (i.s.h.med on-premise) auf eine US-Cloud (OCI) — ohne dass die CLOUD-Act-Exposition strukturell gelöst wird. Europäische KIS-Alternativen, die keine US-Cloud-Abhängigkeit haben: CompuGroup Medical (Medico, ~850 Installationen, DE), Dedalus (Orbis, ~830 Installationen, IT/FR), NEXUS (DE), Meierhofer (DE). Diese laufen auf europäisch kontrollierbarer Infrastruktur. [Quelle: rewion.com KIS-Marktübersicht, Stand 2022/2024]

| Anbieter | C5 | US-Börse / Eigentümer | US-Präsenz | Risikotyp | CLOUD-Act-Risiko | Empfehlung |
|---|---|---|---|---|---|---|
| **Oracle Cerner (KIS i.s.h.med)** | Nein | NYSE: ORCL | US-Hauptsitz Austin | **A — direkt** | 🔴 Hoch | Nicht für Gesundheitsdaten auf OCI |
| **Oracle Cloud Infrastructure (OCI)** | Nein (kein C5) | NYSE: ORCL | US-Muttergesellschaft | **A — direkt** | 🔴 Hoch | EU Sovereign Cloud-Argumentation offen |

### Sovereignty-Washing — warum Serverstandort nicht schützt

Das übergeordnete Muster: 25 CEOs europäischer Cloud-Anbieter warnten in einem offenen Brief an die EU-Kommission (CISPE, 17. März 2026) vor diesem Phänomen. US-Hyperscaler vermarkten EU-Rechenzentren als souveräne Lösung — aber der Serverstandort ändert nichts an der Jurisdiktion über den Provider. Die entscheidende Frage ist nicht "Wo stehen die Server?" sondern "Wer kontrolliert den Provider und unterliegt damit dem CLOUD Act?"

## 5.6 Frankreich — SecNumCloud-Ökosystem

| Anbieter | Eigentümer | US-Präsenz | SecNumCloud | CLOUD Act | Health | Empfehlung |
|---|---|---|---|---|---|---|
| **OVHcloud** | OVH Groupe (FR, Euronext) | OVH US Corp. | ✅ Bare Metal Pod + IaaS (2026) | 🔴 US Corp. + Kanada-Urteil 2024 | ✅ HDS | SNC-Tier für regulierte Workloads |
| **3DS Outscale** | Dassault Systèmes (FR) | Keine | ✅ 3.2 (Erster!) | 🟢 Sauber | ✅ HDS | Referenz FR Health |
| **Cloud Temple** | 100% FR privat | Keine | ✅ IaaS + PaaS | 🟢 Sauber | ✅ HDS | FR KRITIS/Health |
| **S3NS (Thales×Google)** | Thales S.A. (FR) | Google = Lieferant | ✅ 3.2 Dez. 2025 | 🟡 Operator-Modell | — | Funktionsreichste SNC-Option; Vertex AI ab H2 2026 |
| **Scaleway** | Iliad Group (FR) | Keine direkte | ✅ (in Prüfung) | 🟢 Weitgehend | — | Dev/KI/GPU; Mistral-Anbieter |
| **NumSpot** | Banque des Territoires et al. (FR, staatlich) | Keine | ✅ (via Outscale-Basis) | 🟢 Sauber | ✅ HDS | FR Public Health |

**OVHcloud-Vorbehalt:** Kanada-Urteil 2024 — OVH-Kanada-Tochter musste europäische Serverdaten herausgeben. Zeigt strukturelles Restrisiko trotz EU-Hauptsitz. **S3NS:** Mechanismus erklärt in Kapitel 6 (Operator-Modell).

## 5.7 Weitere europäische Länder

| Anbieter | Land/Eigentümer | US-Präsenz | Zertifizierung | CLOUD Act | Stärke |
|---|---|---|---|---|---|
| **Exoscale** | AT — A1/América Móvil | América Móvil (MX) | ISO 27001, SOC 2 | 🟡 Nicht-EU-Eigentum | Beste DBaaS-Breite (Kafka, OpenSearch, Grafana) |
| **UpCloud** | FI — privat | Keine | ISO 27001 | 🟢 Sauber | Developer UX, 15 RZ weltweit |
| **Infomaniak** | CH — privat | Keine | ISO 27001, CH-Recht | 🟢 Sauber | Ab 5,84 €/Monat; Schweizer Datenschutz (strenger als DSGVO) |
| **Aruba Cloud** | IT — Aruba SpA | Keine | ISO 27001, AgID | 🟢 Sauber | Größter IT-Anbieter, günstig |
| **ELASTX** | SE — privat | Keine | ISO 27001 | 🟢 Sauber | OpenStack/Kubernetes, 100% erneuerbar |
| **Cyso Cloud** | NL — privat | Keine | ISO 27001 | 🟢 Sauber | NL-Workloads, OpenStack |

**Exoscale-Vorbehalt:** A1 gehört zu América Móvil (Carlos Slim, Mexiko) — kein direktes US-CLOUD-Act-Risiko, aber nicht-europäische Ultimateigentümerschaft.

## 5.8 Vollständige Zertifizierungsmatrix

| Anbieter | BSI C5 | SecNumCloud | ISO 27001 | HDS | CLOUD Act | § 393 SGB V |
|---|---|---|---|---|---|---|
| Oracle Cerner / OCI | — | — | — | — | 🔴 Direkt | ❌ KIS-Migration kritisch prüfen |
| Microsoft Azure | ✅ | — | ✅ | — | 🔴 Direkt | ❌ Nicht geeignet |
| AWS Germany | ✅ | — | ✅ | — | 🔴 Direkt | ❌ Nicht geeignet |
| STACKIT | ✅ C5 Typ 2 | — | ✅ | — | 🟡 Unklar | Gut (Vorbehalt) |
| plusserver | ✅ | — | ✅ | — | 🟢 Sauber | **Beste DE-Option** |
| Open Telekom Cloud | ✅ | — | ✅ | — | 🟡 Konzernhebel (C) | Mit Vorbehalt |
| Hetzner (EU-RZ) | ✅ | — | ✅ | — | 🟠 US Cloud-LLC | Dev/SMB |
| IONOS | ✅ | — | ✅ | — | 🟠 BMI-bestätigt (A-ind.) | Prüfung erforderlich |
| EWERK Leipzig | — | — | ✅ | — | 🟢 Sauber | Lokal KRITIS |
| Delos Cloud | BSI CPR | — | ✅ | — | 🟡 Operator | M365-Org. |
| Arvato Systems | ✅ | — | ✅ | — | 🔴 Indirekt | US-Software-Risiko |
| OVHcloud (SNC) | ✅ | ✅ | ✅ | ✅ | 🔴 US Corp. | SNC-Tier |
| 3DS Outscale | — | ✅ 3.2 | ✅ | ✅ | 🟢 Sauber | **Referenz FR Health** |
| Cloud Temple | — | ✅ IaaS+PaaS | ✅ | ✅ | 🟢 Sauber | FR KRITIS |
| S3NS | — | ✅ 3.2 | ✅ | — | 🟡 Operator | Funktionsreich |
| Scaleway | — | ⚠️ Prüfung | ✅ | — | 🟢 Weitgehend | Dev/KI/GPU |
| NumSpot | — | ✅ (Outscale) | ✅ | ✅ | 🟢 Sauber | FR Public Health |
| Exoscale | — | — | ✅ | — | 🟡 MX-Eigentum | DBaaS-Stärke |
| UpCloud | — | — | ✅ | — | 🟢 Sauber | Dev/SMB |
| Infomaniak | — | — | ✅ | — | 🟢 Sauber | KMU |
| Aruba Cloud | — | — | ✅ | — | 🟢 Sauber | IT-Markt |

## 5.9 Empfehlungen nach Anwendungsfall

> Vollständige Entscheidungsmatrix mit Workload-Zuordnung, AVV-Klauseln und Migrationsstrategie: **Kapitel 17** (Handlungsempfehlungen).

**Tier 1 — ePA / KRITIS / § 393 Klasse 1:** plusserver · EWERK Leipzig · 3DS Outscale · Cloud Temple

**Tier 2 — Regulierte Enterprise-Workloads / Microsoft-Migration:** STACKIT · Open Telekom Cloud (C — Konzernhebel) · Delos Cloud (+15%) · OVHcloud SNC-Tier · Scaleway (GPU/KI)

**Tier 3 — Dev/Test, unkritische Workloads:** Hetzner (EU-RZ) · IONOS · Infomaniak

---
