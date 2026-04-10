# 1. Das Kernproblem: Gesundheitsdaten unter US-Zugriff

## 1.1 Die Regelungslücke zwischen IT-Sicherheit und Jurisdiktion

> **Wer ist betroffen?** Dieses Dokument adressiert alle Institutionen der Gesundheitswirtschaft, die Patientendaten verarbeiten — nachfolgend einheitlich **"Gesundheitsinstitutionen"** genannt. Das umfasst:
> - **Kostenträger:** Gesetzliche Krankenversicherungen (GKV), Private Krankenversicherungen (PKV), Berufsgenossenschaften (BG), Unfallkassen
> - **Kassenärztliche und -zahnärztliche Vereinigungen (KV/KZV)** sowie deren Bundesvereinigungen (KBV, KZBV)
> - **Stationäre Leistungserbringer:** Krankenhäuser, Universitätsklinika, Rehabilitationskliniken, Pflegeheime
> - **Ambulante Leistungserbringer:** Arzt- und Zahnarztpraxen, Praxisverbünde, MVZ (Medizinische Versorgungszentren)
> - **Weitere Leistungserbringer:** Apotheken, Physiotherapiepraxen, Hebammen, Rettungsdienste, Pflegedienste
> - **Medizinischer Dienst (MD/MDK):** Gutachter- und Prüforganisation der GKV
> - **Praxisverwaltungssysteme und KIS-Hersteller** als Auftragsverarbeiter der o.g. Institutionen
>
> Alle genannten Institutionen unterliegen § 393 SGB V und DSGVO Art. 9 bei der Cloud-Verarbeitung von Gesundheitsdaten.

Gesundheitsinstitutionen verarbeiten Patientendaten heute auf einem breiten Spektrum von Infrastrukturen: eigene Rechenzentren und On-Premise-Systeme, spezialisierte Gesundheits-IT-Dienstleister mit eigenen RZ (wie EWERK, Arvato Health, Telekom Healthcare), EU-souveräne Cloud-Anbieter (plusserver, STACKIT) — und zunehmend auf Cloud-Infrastruktur US-amerikanischer Hyperscaler wie Microsoft Azure, AWS und Google Cloud. Genau dieser letzte Trend offenbart eine Regelungslücke: Zwei Rechtsnormen regeln unterschiedliche Aspekte derselben Cloud-Nutzung — aber keine von beiden deckt das vollständige Risiko ab.

| Norm | Anforderung | Status |
|---|---|---|
| **DSGVO Art. 9 Abs. 1** | Gesundheitsdaten = besondere Kategorie. Verarbeitung grundsätzlich verboten außer expliziter Rechtsgrundlage. Höchste Schutzkategorie im EU-Recht. | ⚠️ Verletzt durch US-Zugriff |
| **DSGVO Art. 48** | Datentransfer an ausländische Behörden nur über anerkannte Rechtshilfemechanismen — nicht durch einseitige US-Gesetze. | ⚠️ Verletzt durch CLOUD Act |
| **§ 393 SGB V (Juli 2024)** | Cloud-Nutzung durch KVen/GKVen erlaubt, wenn BSI-C5-Typ2-Testat vorhanden (BSI = Bundesamt für Sicherheit in der Informationstechnik). Azure hat C5. Formell compliant. | ✅ Formell erfüllt |
| **BSI C5-Testat** (Cloud Computing Compliance Criteria Catalogue) | Prüft Informationssicherheit und technische Maßnahmen. Prüft **nicht**, ob US-Behörden rechtlich zugreifen können. C5:2026 (April 2026, 168 Kriterien) schließt diese Lücke nicht — das BSI plant Souveränitätskriterien als separates Dokument. | ⚠️ Lücke: kein Rechtsschutz |

§ 393 SGB V und DSGVO Art. 48 widersprechen sich nicht — sie regeln unterschiedliche Fragen. § 393 SGB V ist eine sozialrechtliche Erlaubnisnorm: Sie erlaubt die Cloud-Verarbeitung von Gesundheitsdaten unter der Bedingung, dass ein BSI C5 Typ 2 Testat die IT-Sicherheit nachweist. Das ist ihr Regelungsgegenstand — und das ist auch der richtige Ort dafür. Die Frage, ob ein Anbieter unter US-Jurisdiktion steht und von einem US-Gericht zur Datenherausgabe gezwungen werden kann, ist hingegen keine Frage der IT-Sicherheit. Sie gehört nicht in § 393 SGB V — sie gehört in die DSGVO und ins internationale Recht. DSGVO Art. 48 beantwortet diese Frage klar: Datentransfer an ausländische Behörden nur über anerkannte Rechtshilfemechanismen. Das BSI C5 Testat prüft Informationssicherheit, nicht Jurisdiktion. Es kann einem US-Anbieter technische Sicherheit attestieren, obwohl US-Bundesbehörden diesen Anbieter per CLOUD Act zur Datenweitergabe verpflichten können — das BSI-Testat ändert daran nichts, weil es dafür nicht gemacht ist.

Die Lücke liegt nicht im Gesetz, sondern im Verständnis: § 393 SGB V wird in der Beschaffungspraxis häufig als ausreichender Compliance-Nachweis missverstanden. Aber § 393 entbindet nicht von der DSGVO. Jede Gesundheitsinstitution bleibt unabhängig vom C5-Testat verpflichtet, die DSGVO einzuhalten — einschließlich Art. 48. Ein C5-konformer Anbieter, der dem CLOUD Act unterliegt, erfüllt § 393 SGB V. Er löst aber nicht die DSGVO-Pflicht ein. Wenn US-Behörden tatsächlich auf Gesundheitsdaten zugreifen, ist das ein meldepflichtiger Datenschutzvorfall nach Art. 33 DSGVO — unabhängig davon, ob § 393 eingehalten wurde, und unabhängig davon, ob die Organisation davon erfährt.

Keine Norm verlangt heute, die CLOUD-Act-Exposition eines Anbieters als Kriterium neben dem C5-Testat in Ausschreibungen zu prüfen. C5 ist Pflicht. Eine Jurisdiktionsprüfung ist es nicht. Also wird sie in Vergabeverfahren regelmäßig weggelassen — nicht aus bösem Willen, sondern weil die DSGVO-Pflicht neben § 393 SGB V unsichtbar bleibt. Das Ergebnis: Eine Organisation kann § 393 SGB V vollständig einhalten, ein gültiges C5-Testat vorlegen und gleichzeitig ein latentes DSGVO-Risiko tragen, das bei einem US-Behördenzugriff schlagartig zum Datenschutzvorfall wird.

Microsoft hat das in einer offiziellen Anhörung vor dem französischen Senat (Juni 2025) selbst bestätigt: **Eine Garantie, dass keine Daten an US-Behörden weitergegeben werden, ist nicht möglich.**

**Was das konkret bedeutet — dokumentierte Beispiele:**

Das ist kein hypothetisches Szenario. Es gibt mehrere belegte Fälle, in denen die USA europäische Staatsbürger auf Sanktionslisten gesetzt haben — nicht wegen Straftaten, sondern wegen politischer Konflikte.

**Fall 1 — Nord Stream 2 (2019/2020):** Die USA haben unter dem PEESCA-Gesetz (Protecting Europe's Energy Security Act) Sanktionen gegen Unternehmen und einzelne Mitarbeiter verhängt, die am Bau der Gaspipeline Nord Stream 2 beteiligt waren — einem legalen europäischen Infrastrukturprojekt. Betroffen waren unter anderem die Nord Stream 2 AG mit Sitz in der Schweiz, das niederländische Verlegeschiff-Unternehmen Allseas und namentlich benannte Führungskräfte und Mitarbeiter, darunter deutsche Staatsbürger. Diese Personen standen auf der SDN-Liste des Office of Foreign Assets Control (OFAC) — der zentralen US-Sanktionsliste.

**Fall 2 — HateAid (Dezember 2025):** Am 23. Dezember 2025 setzte US-Außenminister Marco Rubio die beiden Geschäftsführerinnen der deutschen gemeinnützigen Organisation HateAid — Josephine Ballon und Anna-Lena von Hodenberg — auf die US-Sanktionsliste. HateAid unterstützt Opfer von Hass und Gewalt im Internet und setzt sich für die Durchsetzung europäischen Rechts auf US-Plattformen ein, insbesondere des Digital Services Act. Die USA stuften sie als "radical activists" und ihre Organisation als "weaponized NGO" ein. Gleichzeitig wurden der ehemalige EU-Kommissar Thierry Breton sowie Vertreter britischer Anti-Desinformations-Organisationen sanktioniert. Die Bundesregierung verurteilte die Maßnahme; Bundestags-Vizepräsident Nouripour forderte die Einbestellung des US-Geschäftsträgers. [Quellen: HateAid Pressemitteilung, 14. Januar 2026; CNN, 24. Dezember 2025; The Local, 24. Dezember 2025]

**Was bei den ICC-Richtern bereits geschehen ist:** Der MIT Technology Review dokumentierte im Januar 2026, was Sanktionen in der Praxis bedeuten: Ein sanktionierter Richter des Internationalen Strafgerichtshofs verlor nach seiner Sanktionierung den Zugang zu Microsoft, Amazon, Gmail, Visa, Mastercard, American Express und PayPal — sein gesamtes digitales Leben wurde abgeschaltet. HateAid-Geschäftsführerin Ballon wird dazu zitiert: "If Microsoft does that to someone who is a lot more important than we are, they will not even blink to shut down the email accounts from some random human rights organization in Germany." [Quelle: MIT Technology Review, 19. Januar 2026]

In dem Moment, in dem eine Person auf der US-Sanktionsliste steht, ist jeder US-kontrollierte Anbieter rechtlich verpflichtet, sämtliche Daten zu dieser Person einzufrieren und auf Anfrage herauszugeben. Microsoft, AWS, Google, Oracle — sie haben keine Wahl. Ein Verstoß gegen US-Sanktionsrecht wird strafrechtlich verfolgt.

Wenn eine sanktionierte HateAid-Mitarbeiterin oder ein sanktionierter Nord-Stream-2-Ingenieur bei einer deutschen Krankenkasse versichert ist, deren Abrechnungsdaten auf Azure laufen, werden Diagnosen, Medikationspläne, Behandlungsverläufe und Arzt-Patienten-Kontakte automatisch Teil der Herausgabepflicht. Nicht weil diese Personen eine Straftat begangen haben, sondern weil die US-Regierung europäische Rechtsdurchsetzung als "Zensur" oder europäische Energiepolitik als Bedrohung eingestuft hat. Wenn ein Universitätsklinikum sein KIS bei Oracle Cerner betreibt, werden die klinischen Daten — Anamnese, Operationsberichte, psychiatrische Befunde — Teil der Herausgabepflicht. Die Kasse oder die Klinik erfährt davon in der Regel nicht, weil US-Recht eine Schweigeverpflichtung vorsehen kann.

Für die betroffene Gesundheitsinstitution ist das ein meldepflichtiger Datenschutzvorfall nach Art. 33 DSGVO — den sie nicht melden kann, weil sie nicht weiß, dass er stattgefunden hat. Und für den betroffenen Patienten ist es ein Eingriff in seine sensibelsten Grundrechte, gegen den er keinen Rechtsschutz vor US-Gerichten hat.

## 1.2 Warum es trotzdem passiert — sieben Realitätsgründe

### 1.2.1 Pragmatismus — Service-Tiefe und Ökosystem-Sogwirkung

Azure und AWS bieten je über 200 verwaltete Dienste — EU-Anbieter wie STACKIT 40–60. Für eine GKV oder Klinik, die erstmals eine Cloud-basierte KI-Plattform, ein Analytics-System oder eine moderne Collaboration-Umgebung aufbaut, ist ein US-Hyperscaler schlicht der Weg des geringsten Widerstands: ein Anbieter, ein Vertrag, ein integriertes Ökosystem. Die CLOUD-Act-Frage stellt sich im Beschaffungsprozess nicht, weil § 393 SGB V mit C5-Testat die formale Erlaubnis gibt und die Jurisdiktionsprüfung kein Vergabekriterium ist. Details in Kapitel 7 und 8.

### 1.2.2 Kein Enforcement — dokumentiertes Vollzugsdefizit

Die DSK (Datenschutzkonferenz — Koordinierungsgremium aller 17 deutschen Datenschutzaufsichtsbehörden) hat Microsoft 365 zweimal als nicht DSGVO-konform eingestuft — 2020 und 2022. Kein einziges Bußgeld gegen eine Gesundheitsinstitution wegen US-Cloud-Nutzung ist öffentlich bekannt. Artikel91.eu fasste es 2021 präzise zusammen: "Viel Dialog, fast keine Sanktionen."

Das hat strukturelle Gründe: DSK-Beschlüsse sind nicht rechtsverbindlich, Prüfungen erfolgen nur anlassbezogen, und grenzüberschreitende Verfahren gegen US-Anbieter dauern Jahre. Das einzige nennenswerte deutsche GKV-Bußgeld — 1,2 Mio. EUR gegen die AOK Baden-Württemberg 2020 — betraf Gewinnspielmissbrauch, nicht Cloud-Datenschutz.

Das Vollzugsdefizit ist kein Freifahrtschein. Bei einem Schrems-III-Urteil des EuGH (Europäischer Gerichtshof, Luxemburg) würde sich das Enforcement-Bild schlagartig ändern — mit sofortigem Handlungsdruck für alle Organisationen, die dann noch auf US-Cloud setzen.

### 1.2.3 Legislative Umgehung — § 393 SGB V als Kompromissnorm

§ 393 SGB V (in Kraft seit 1. Juli 2024 durch das Digital-Gesetz / DigiG) erlaubt die Cloud-Verarbeitung von Gesundheitsdaten unter drei Bedingungen: EU-Rechtsraum, BSI C5 Typ 2 Testat und Umsetzung kundenseitiger Sicherheitsmaßnahmen. Die Norm ist ein politischer Kompromiss, kein datenschutzrechtliches Konzept. Drei strukturelle Schwächen:

**Erstens — CLOUD Act bleibt unberührt:** § 393 SGB V adressiert ausschließlich die Frage, *ob* Gesundheitsdaten in einer Cloud verarbeitet werden dürfen. Die Frage, ob ein US-Anbieter diese Daten auf Anfrage einer US-Behörde herausgeben muss, regelt § 393 SGB V nicht. Das C5-Testat prüft Informationssicherheit, nicht Jurisdiktion. Ein AWS- oder Azure-Rechenzentrum in Frankfurt mit gültigem C5-Testat ist § 393-konform — und gleichzeitig CLOUD-Act-exponiert.

**Zweitens — DPF als Lückenbüßer:** Die zulässige Nutzung von US-Cloud-Diensten stützt sich auf das Data Privacy Framework (DPF) als Angemessenheitsbeschluss. Das DPF hängt an einer US-Präsidialverordnung, nicht an einem Gesetz. Schrems II (2020) hat das identische Vorgängermodell gekippt. Ein Schrems-III-Verfahren ist bei noyb (None of Your Business — europäische Datenschutz-NGO von Max Schrems) bereits anhängig.

**Drittens — C5 als regulatorische Mindestanforderung, nicht als Souveränitätsnachweis:** Der Gesetzgeber hat mit § 393 SGB V BSI C5 als Pflichtstandard eingeführt, weil er verfügbar und praxistauglich ist — nicht weil er vor US-Behördenzugriff schützt. Auch der am 7. April 2026 veröffentlichte C5:2026 (168 Kriterien, Nachfolger des C5:2020) ändert daran nichts: Das BSI hat Souveränitätskriterien bewusst als separates Dokument angekündigt, das "in Kürze" erscheinen soll [188]. C5 zertifiziert Informationssicherheit, nicht Datensouveränität im geopolitischen Sinne.

### 1.2.4 Struktureller Interessenkonflikt bei Beratern

Die IT-Strategie- und Digitalisierungsberatung für Gesundheitsinstitutionen wird überwiegend von US-amerikanischen Beratungshäusern erbracht — Deloitte, EY, McKinsey, PwC, KPMG, Accenture — die ihrerseits tiefe kommerzielle Partnerschaften mit denselben US-Hyperscalern unterhalten, die sie empfehlen könnten. Accenture und Microsoft betreiben gemeinsam Avanade (50.000 Mitarbeitende, ausschließlich Microsoft-Implementierung). McKinsey hat die Amazon McKinsey Group (AMG) für AWS-Migrationen gegründet. KPMG hat 2 Milliarden Dollar über fünf Jahre in die Microsoft-Partnerschaft investiert. McKinsey, BCG, Accenture und Capgemini sind Gründungspartner von OpenAIs Frontier Alliance mit Vorabzugang zu GPT-Modellen. Wer die Strategie entwirft, verdient an der Umsetzung — und erhält Partnerprovisionen vom Cloud-Anbieter, den er empfiehlt. Ausführlich dokumentiert in Kapitel 12.

### 1.2.5 Aktiver Vertrieb der Hyperscaler

Microsoft, AWS und Google betreiben in Deutschland dedizierte Public-Sector- und Healthcare-Vertriebsteams, die aktiv auf Gesundheitsinstitutionen zugehen — mit maßgeschneiderten Angeboten, Förderbudgets, KHZG-Beratung (KHZG = Krankenhauszukunftsgesetz, Digitalisierungsförderung) und kostenloser Proof-of-Concept-Infrastruktur. EU-souveräne Alternativen wie STACKIT, plusserver (deutscher Cloud-Anbieter, Tochter der Ionos Group SE) oder EWERK verfügen über deutlich kleinere Vertriebsorganisationen und sind in Beschaffungsprozessen häufig nicht vertreten, wenn Anforderungen formuliert werden. Wer nicht im Raum ist, wenn die Ausschreibung entsteht, wird selten berücksichtigt.

### 1.2.6 Sovereignty Washing — irreführendes Marketing als Beschaffungstreiber

Microsoft, AWS, Google und Oracle vermarkten aktiv Produkte unter den Bezeichnungen "Sovereign Cloud", "EU Data Boundary", "Isolated Realm" oder "European Sovereign Cloud" — und suggerieren eine Datensouveränität, die rechtlich nicht besteht. Das ist nicht nur ungenau, sondern irreführend im Sinne wettbewerbsrechtlicher Maßstäbe: Ein Anbieter, der "souverän" vermarktet, obwohl er als US-Unternehmen dem CLOUD Act unterliegt und das — wie Microsoft vor dem französischen Senat — selbst bestätigt hat, erzeugt bei der einkaufenden Institution einen Vertrauensschutz, der juristisch nicht existiert.

Das C5-Testat verstärkt diesen Effekt. Es ist ein Informationssicherheitsnachweis — kein Souveränitätsnachweis. Aber in Kombination mit der Marketingbezeichnung "Sovereign Cloud" entsteht in der Beschaffungspraxis der Eindruck, die Souveränitätsfrage sei gelöst. "Daten in Deutschland" plus "C5-zertifiziert" plus "Sovereign Cloud" klingt nach dreifacher Absicherung — tatsächlich adressiert keine der drei Komponenten die Jurisdiktionsfrage.

Für die Haftungsbewertung ist das relevant: Eine Gesundheitsinstitution, die sich auf die "Sovereign Cloud"-Vermarktung eines US-Anbieters verlassen hat, ohne eine eigene Jurisdiktionsprüfung durchzuführen, kann sich im Schadensfall nicht auf das Marketing des Anbieters berufen. Die DSGVO-Verantwortung liegt beim Verantwortlichen — nicht beim Anbieter, der seine Produkte geschickt benennt. 25 CEOs europäischer Cloud-Anbieter haben in einem offenen Brief an die EU-Kommission (CISPE, 17. März 2026) genau dieses Phänomen als irreführend kritisiert. Ausführlich dokumentiert in [§5.5](05-anbieterbewertung.md#55-juristische-detailanalysen) und [§5.6](05-anbieterbewertung.md#56-frankreich-secnumcloud-okosystem).

### 1.2.7 Politische Einflussnahme der Hyperscaler

Big Tech gibt 19-mal mehr für EU-Lobbyarbeit aus als die Automobilindustrie. 890 Digital-Lobbyisten arbeiten Vollzeit in Brüssel — mehr als Sitze im Europäischen Parlament. Das Google-Lobbypapier vom August 2025 zur Einschränkung des DSGVO-Auskunftsrechts wurde wortgleich in den Digital-Omnibus-Entwurf der EU-Kommission übernommen. Datenschutz gilt — aber seine Weiterentwicklung und Durchsetzung wird durch diese Finanzasymmetrie systematisch gebremst. Ausführlich dokumentiert in Kapitel 11.

---
