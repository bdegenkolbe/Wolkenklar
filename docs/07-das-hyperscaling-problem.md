# 7. Das Hyperscaling-Problem: Wer kann tatsächlich skalieren?

## 7.1 Was Hyperscaling wirklich bedeutet

Echtes Hyperscaling hat drei Dimensionen:

- **Rohkapazität:** Millionen von Servern, globale Verfügbarkeit innerhalb von Sekunden auf Abruf
- **Service-Breite:** Nicht nur Compute/Storage, sondern hunderte spezialisierte Managed Services von KI bis IoT
- **Economies of Scale:** Hardwareeinkauf in Milliardenvolumen drückt Preise auf ein Niveau, das kein kleinerer Anbieter erreicht

## 7.2 Die Kapazitätslücke — ehrliche Zahlen

**Hinweis zur Methodik:** Physische Serverzahlen werden von Hyperscalern nicht veröffentlicht — alle Zahlen in der Spalte "GPU (H100-Äquivalente)" sind Schätzungen auf Basis von Nvidia-Umsatzdaten, Unternehmensangaben und unabhängigen Analysen (Epoch AI, LessWrong Research, Nov. 2024). Die GPU-Spalte ist für die KI-Bewertung relevanter als Serverzahlen, da GPUs die KI-Trainingsfähigkeit bestimmen.

| Anbieter | RZ-Regionen / Standorte | Server (phys., geschätzt) | GPU (H100-Äquivalente, EOY 2024) | Investitionsvolumen | Services |
|---|---|---|---|---|---|
| **AWS** | 38 Regionen, 121 AZs | ~3,5 Mio. | **~400.000–600.000** (H100-Äq.) | 7,8 Mrd. USD allein DE | ~250 Services |
| **Microsoft Azure** | 60+ Regionen | ~3 Mio. | **~500.000** (H100-Äq., größte NVIDIA-Flotte) | ~100 Mrd. USD/Jahr | ~200 Services |
| **Google Cloud** | 42 Regionen | ~1,5 Mio. | **>1 Mio.** (H100-Äq. inkl. TPUs; davon ~300.000 NVIDIA H100) | — | ~150 Services |
| **Meta** *(kein Cloud-Anbieter)* | Eigene RZ (USA) | k.A. | **~600.000** H100-Äq. (EOY 2024, Zuckerberg bestätigt) | — | — |
| **xAI / Colossus** *(kein Cloud)* | Memphis, Tennessee | — | **100.000 H100** (Cluster 1); Ziel 200.000 H200 | — | — |
| **Alibaba Cloud** | 36 Regionen | ~1 Mio. | ~100.000–200.000 (H100-Äq., Schätzung) | — | ~100 Services |
| **OVHcloud** | 4 EU-Regionen, 43 RZ | ~350.000 | k.A. (limitiert, keine GPU-Fokus-Strategie) | — | ~50 Services |
| **Open Telekom Cloud (T-Systems)** | 2 Regionen (DE+NL), 4 RZ | **~100.000** (Biere allein); 640.000 VMs | k.A. öffentlich (kein GPU-First-Anbieter) | — | ~80 Services |
| **STACKIT** | 4 operative RZ (DE+AT), Lübbenau ab 2027 | Heute: ~15.000–25.000 (Schätzung) · Lübbenau ab 2027: **bis zu 100.000 GPUs**, 200 MW — Ausbau der Schwarz-Gruppe-Rechenleistung auf das **7-fache** | Heute: k.A. · **Ab 2027: bis zu 100.000 GPUs** | **11 Mrd. EUR** bis 2027 | ~40–60 Services |
| **Hetzner** | 5 Standorte (DE/FI/US) | ~100.000 | k.A. (RTX-Pro-6000-Angebot, kein H100-Training) | — | ~20 Services |
| **plusserver** | 4 DE-Standorte | ~20.000 | k.A. (kein GPU-Cloud-Angebot) | — | ~15 Services |
| **Arvato Systems** | 3 eigene RZ Gütersloh + Colocation | k.A. | Nicht-Cloud-Betreiber — MSP (Managed Service Provider) auf Azure/AWS/GCP | — | MSP-Modell |

**Warum Meta und xAI in der Tabelle stehen — obwohl sie keine Cloud-Anbieter sind:**
Meta und xAI kaufen GPU-Kapazitäten in einer Größenordnung, die den gesamten europäischen Cloud-Markt in den Schatten stellt — und sie tun das ausschließlich für eigene KI-Modelle. Ende 2024 hatte Meta ein Portfolio mit einer Rechenleistung entsprechend fast 600.000 H100-Äquivalenten. xAI brachte den Colossus-Cluster mit 100.000 H100-GPUs in Memphis in 122 Tagen online. Diese Zahlen zeigen: STACKIT mit seinen geplanten 100.000 GPUs in Lübbenau ist für Europa ein Meilenstein — im globalen KI-Wettrüsten aber lediglich Aufholen.

**Die GPU-Hierarchie in Zahlen (Epoch AI, Stand EOY 2024):**
Google: >1 Mio. H100-Äquivalente (inkl. TPUs) · Microsoft: ~500.000 H100-Äq. · Meta: ~600.000 H100-Äq. · AWS: ~400.000–600.000 H100-Äq. · STACKIT Lübbenau (ab 2027): 100.000 GPUs. Der Abstand ist erheblich — aber für die meisten GKV- und Klinik-Workloads irrelevant. Keine GKV mit 5 Millionen Versicherten braucht 600.000 GPUs.

**Open Telekom Cloud — Kapazitätszahlen konkret:**
Die OTC verwaltet über 1 Exabyte Speicher, ermöglicht 640.000 virtuelle Maschinen mit über 4,5 Millionen GB RAM und mehr als 910.000 vCPUs. Das RZ in Biere: 20 IT-Räume, Platz für 100.000 Server, 18 Megawatt IT-Leistung. T-Systems betreibt 33 RZ weltweit — 7 im Eigenbetrieb, 26 im Colocation-Modus.

**STACKIT — aktuelle Kapazität und GPU-Roadmap:**
Keine offiziellen Server-Zahlen. Rückrechnung aus dem Lübbenau-Faktor (7-fache Erhöhung) → schätzungsweise **15.000–25.000 physische Server** heute. Lübbenau ab 2027: 200 MW Anschlussleistung (vs. 18 MW in Biere), bis zu **100.000 GPUs** (Dell PowerEdge XE9680, NVIDIA Blackwell, 8 GPUs/Server), Direct Liquid Cooling. STACKIT wird kein Hyperscaler durch CPU-Server-Masse — sondern durch GPU-Dichte für KI-Workloads.

**Arvato Systems — kein Cloud-Betreiber, sondern MSP:**
3 eigene RZ in Gütersloh für Managed Services und SAP-Hosting. Kein eigenständiger Cloud-Anbieter — relevante Rolle ist der Betrieb der **Delos Cloud** als Betriebsdienstleister.

## 7.3 Service-Tiefe im Vergleich — gesundheitssektorrelevant

Die folgende Tabelle bewertet ausschließlich Services, die für GKVen, KVen und Kliniken tatsächlich relevant sind. Globale CDN für Streaming-Plattformen oder IoT-Hubs für Fahrzeugtelemetrie sind für den deutschen Gesundheitssektor strukturell irrelevant. Entscheidend sind: Collaboration, Identity, Datenbanken, Analytics, KI-Inferenz, Compliance-Tooling und Kerninfrastruktur.

**Legende:** ✅ Vorhanden und produktionsreif · ⚠️ Vorhanden, aber eingeschränkt oder mit Mehraufwand · ❌ Nicht vorhanden / kein souveräner Ersatz

### A — Collaboration & Productivity (tiefstes Lock-in, höchstes CLOUD-Act-Risiko)

| Service | US-Anbieter (direkt) | Operator-Modell | Souveräner EU-Ersatz |
|---|---|---|---|
| **Office-Suite (Word, Excel, PowerPoint)** | Microsoft 365 (MSFT) | Delos Cloud (+15%) | ✅ Euro-Office / Office.eu / LibreOffice |
| **E-Mail & Kalender** | Exchange Online (MSFT) | Delos Cloud | ✅ Open-Xchange + Thunderbird |
| **Dokumentenmanagement / Intranet** | SharePoint Online (MSFT) | Delos Cloud | ✅ Nextcloud Hub, OpenCloud 1.0, GoFAST |
| **Videokonferenz & Chat** | Microsoft Teams (MSFT) | Delos Cloud | ✅ OpenTalk, Jitsi, Matrix/Element |
| **Identity / SSO / RBAC** | Azure Entra ID (MSFT) | Delos Cloud | ✅ Keycloak, Univention Corporate Server |
| **Endpoint-Management (MDM)** | Microsoft Intune (MSFT) | Delos Cloud | ⚠️ Ansible + FreeIPA (Mehraufwand) |
| **E-Signatur** | DocuSign (US), Adobe Sign (US) | — | ✅ Skribble (CH), D-Trust (BSI-akkreditiert) |

### B — Datenbanken & Data Warehouse (Analytics-Fundament für GKV-Scoring)

| Service | US-Anbieter | Operator-Modell | Souveräner EU-Ersatz |
|---|---|---|---|
| **MS SQL Server / Azure SQL** | Microsoft (MSFT) | Delos Cloud | ✅ PostgreSQL, MariaDB (alle EU-Clouds) |
| **Daten-Warehouse (Cloud-native)** | Snowflake (NYSE: SNOW, US) | — | ⚠️ DuckDB (lokal), Apache Doris, ClickHouse (EU-hosted) |
| **Streaming / Event-Hub** | AWS Kinesis, Azure Event Hub | — | ✅ Apache Kafka auf STACKIT / Exoscale |
| **Managed NoSQL** | DynamoDB, CosmosDB (MSFT) | — | ✅ MongoDB, Redis, CassandraDB auf STACKIT |
| **Data Lake / Object Store** | AWS S3, Azure Blob Storage | Delos Cloud | ✅ MinIO, Ceph, STACKIT/plusserver Object Storage |
| **ETL / Datenpipelines** | AWS Glue, Azure Data Factory | — | ✅ Apache Airflow, dbt (selbst-gehostet EU) |

> **Snowflake-Hinweis:** Snowflake Inc. (NYSE: SNOW) ist ein US-Unternehmen mit Hauptsitz in Bozeman/Montana und unterliegt direkt dem CLOUD Act. Daten in Snowflake-EU-Regionen (Frankfurt) sind strukturell nicht geschützt. Für GKV-Scoring-Daten und Morbi-RSA-Analysen: DuckDB on-premise oder ClickHouse auf STACKIT/plusserver sind produktionsreife Alternativen.

> **Qlik Cloud — C5 ≠ CLOUD-Act-Schutz:** Qlik (Hauptsitz King of Prussia, Pennsylvania, US) ist ein US-Unternehmen und unterliegt dem CLOUD Act als Kategorie A — unabhängig von Zertifizierungen. Ein C5-Testat, sofern Qlik Cloud eines erworben hat oder anstrebt, bescheinigt lediglich Informationssicherheit nach BSI-Mindestanforderungen — es schützt **nicht** gegen US-Behördenzugriff. Das ist die Kernaussage von Kapitel 5.3: "C5 belegt technische Sicherheit — nicht rechtliche Souveränität. Azure hat C5 und unterliegt dem CLOUD Act. plusserver hat C5 und unterliegt ihm strukturell nicht." Dasselbe gilt für Qlik Cloud. Ein C5-Testat als Eingangsbedingung nach § 393 SGB V für Patientendaten löst den CLOUD-Act-Konflikt nicht — es verschleiert ihn. Für GKV-Analytics und Versorgungssteuerungsdaten mit Patientenbezug: Qlik on-premise (selbst betriebene Instanz ohne US-Cloud-Verbindung) oder EU-souveräne BI-Alternativen (Metabase, Apache Superset, Grafana) auf STACKIT/plusserver.

### C — KI & Analytik (zunehmend kritisch für GKV-Versorgungsmanagement)

| Service | US-Anbieter | Operator-Modell | Souveräner EU-Ersatz |
|---|---|---|---|
| **LLM-Inferenz / generative KI** | Azure OpenAI / AWS Bedrock (GPT-4, Claude) | S3NS (Google Vertex AI ab H2 2026) | ✅ vLLM + Mistral (lokal / STACKIT / Scaleway) |
| **Mistral AI direkt** | Mistral API (FR-Unternehmen, aber API-Infrastruktur prüfen) | — | ✅ Mistral-Modelle self-hosted via vLLM (bevorzugt) |
| **BI / Dashboarding** | Power BI / Microsoft Fabric (MSFT) · **Qlik Cloud (US, Thoma Bravo — privat)** | Delos Cloud (Power BI) | ✅ Metabase, Apache Superset, Grafana |
| **ML-Plattform / MLOps** | Azure ML, AWS SageMaker | — | ⚠️ MLflow + Kubernetes (selbst-gehostet) |
| **Vektordatenbank (RAG)** | Azure AI Search, Pinecone (US) | — | ✅ Qdrant (DE), Weaviate (NL), Chroma (self-hosted) |
| **Embedding-Modelle** | OpenAI text-embedding, AWS Titan | — | ✅ Sentence-Transformers lokal, Mistral Embed |

> **Mistral-Hinweis:** Mistral AI ist ein französisches Unternehmen (Paris, SAS) — kein US-CLOUD-Act-Risiko strukturell. Die Mistral-API läuft jedoch auf Scaleway-Infrastruktur. Für höchste Schutzklasse (ePA-Daten): Mistral-Modelle lokal über vLLM deployen, nicht via API. Für unkritische Workloads ist die Mistral-API akzeptabel.

### D — Infrastruktur & DevOps (Basis-Schicht)

| Service | US-Anbieter | Souveräner EU-Ersatz |
|---|---|---|
| **Compute / VM** | EC2, Azure VM | ✅ STACKIT, plusserver, Hetzner |
| **Managed Kubernetes** | EKS, AKS | ✅ STACKIT SKE, plusserver managed K8s |
| **Serverless / Functions** | Lambda, Azure Functions | ⚠️ STACKIT Functions (früh), Knative self-hosted |
| **CI/CD & Versionskontrolle** | GitHub, Azure DevOps | ✅ GitLab (self-hosted) |
| **Monitoring & Observability** | Azure Monitor, CloudWatch | ✅ Grafana + Prometheus + Loki + OpenSearch |
| **SIEM / Security** | Microsoft Sentinel (MSFT) | ✅ Wazuh, OpenSearch Security Analytics |
| **Backup & DR** | Azure Backup, AWS Backup | ✅ Veeam auf EU-Storage, Restic |

### E — Compliance & Gesundheitsspezifisch

| Service | US-Anbieter | Souveräner EU-Ersatz |
|---|---|---|
| **ePA-Infrastruktur** | gematik-Pflicht: TI-Anbindung | ✅ nur zertifizierte TI-Anbieter (kein US-Hyperscaler direkt) |
| **KIS (Krankenhausinformationssystem)** | Oracle Health / Cerner (US!) | ⚠️ CGM, iMedOne, SAP IS-H (DE/EU) |
| **PVS (Praxisverwaltungssystem)** | US-Abhängigkeit über KIS-Backend | ✅ Medatixx, Turbomed, CompuMed (DE) |
| **Abrechnungssystem GKV** | SAP IS-H, Eigensysteme | ✅ SAP on-premise oder EU-Cloud |
| **Dokumentenarchiv / §630f BGB** | SharePoint/Azure (MSFT) | ✅ OpenCloud, d.velop, Fabasoft (AT) |

> **Oracle Health / Cerner-Warnung:** Oracle Corporation (NYSE: ORCL) hat Cerner 2022 für 28 Mrd. USD übernommen. Cerner-Systeme (u.a. in UKL Dresden, UKL Freiburg geplant) laufen mittlerweile auf Oracle Cloud Infrastructure (OCI) — einem US-Cloud-Anbieter mit direktem CLOUD-Act-Risiko. Für Kliniken, die Cerner/Oracle Health evaluieren: OCI ist strukturell gleichwertig mit Azure aus CLOUD-Act-Perspektive.

## 7.4 Was das für den Gesundheitssektor bedeutet

Keine GKV mit 5 Millionen Versicherten braucht 3,5 Millionen Server. STACKIT ist heute bereits ausreichend skaliert für GKV- und Klinik-Kernworkloads. Lücken bestehen bei Data Warehouse (Snowflake-Ebene), MLOps-Plattformen und Endpoint-Management — nicht bei Kapazität.

**Die vier größten blinden Flecken** der aktuellen Souveränitätsdebatte im Gesundheitswesen:
1. **Snowflake** für GKV-Analytics — NYSE: SNOW, US-Hauptsitz, direktes CLOUD-Act-Risiko trotz Frankfurter Region
2. **Oracle Health / Cerner auf OCI** für Kliniken — NYSE: ORCL, strukturell gleichwertig mit Azure aus CLOUD-Act-Perspektive
3. **Qlik Cloud** für GKV-BI und Versorgungssteuerung — US-Unternehmen (PA, Thoma Bravo), Kategorie A; Qlik Cloud läuft auf AWS und hat EU-Regionen in Frankfurt, Irland, Paris, London und Mailand — die Frankfurt-Region ändert die US-Jurisdiktion nicht; BSI C5-Testat noch nicht erteilt (Stand April 2026), schützt ohnehin nicht gegen CLOUD Act
4. **KI-Dienste** (Azure OpenAI, Google Gemini, AWS Bedrock) — verarbeiten Patientendaten zwangsläufig im Klartext; clientseitige Verschlüsselung unmöglich; cloudbasierte Integrationsplattformen (Zapier, Power Automate) als versteckte Datenflüsse. Ausführlich analysiert in §7.5.

Die ersten drei werden in der Praxis kaum als CLOUD-Act-Risiko diskutiert — obwohl sie tägliche Kernsysteme für Gesundheitsdaten betreiben. Der vierte wächst am schnellsten.

## 7.5 KI-Anbieter und Integrationsplattformen — der blinde Fleck bei Klartextverarbeitung

Die Tabelle in §7.3 C zeigt die Anbieter-Landschaft für KI-Services. Dieser Abschnitt behandelt ein spezifischeres Problem: **KI-Dienste verarbeiten Eingabedaten zwangsläufig im Klartext.** Verschlüsselung hilft nicht (vgl. §13.4) — ein LLM muss den Prompt lesen, ein Sprachmodell muss das Audio hören, ein Zusammenfassungsmodell muss den Text verstehen. Das unterscheidet KI-Services fundamental von Speicher- oder Compute-Diensten, bei denen clientseitige Verschlüsselung die Exposition begrenzen kann.

### Gesundheitsspezifische KI-Anwendungsfälle und ihre CLOUD-Act-Exposition

Im Gesundheitswesen entstehen gerade vier KI-Anwendungsmuster, die alle Klartextverarbeitung **sensibler Patientendaten** erfordern:

**1. Transkription und Zusammenfassung von Arzt-Patienten-Gesprächen.** Ambient-Listening-Systeme wie Nuance DAX (Microsoft/MSFT), Nabla (FR), oder Google-Gemini-basierte Lösungen zeichnen das Gespräch auf und erzeugen automatisch eine strukturierte Dokumentation. Die Audiodaten — Stimme des Patienten, Symptombeschreibungen, Diagnosen — werden an den KI-Dienst übertragen und dort im Klartext verarbeitet. Bei US-Anbietern sind diese Rohdaten CLOUD-Act-exponiert.

**2. Automatisierte Arztbriefe.** LLMs generieren Entlassungsbriefe, Befundberichte oder Überweisungsschreiben auf Basis der Patientenakte. Die Eingabe umfasst Diagnosen, Medikation, Verlaufsdaten — die sensibelsten Daten im Gesundheitswesen. Wenn der LLM-Service bei einem US-Anbieter läuft, liegen diese Daten während der Verarbeitung im Klartext auf US-kontrollierter Infrastruktur.

**3. E-Mail- und Dokumentenzusammenfassung.** Microsoft Copilot, Google Gemini oder vergleichbare Assistenten fassen E-Mails, Aktenvermerke und Dokumente zusammen. Im GKV-Kontext können diese E-Mails Versichertendaten, Leistungsanträge oder MDK-Gutachten enthalten. Die KI liest den vollständigen Inhalt — HYOK ist nicht möglich (vgl. §13.4).

**4. KI-gestützte Kodierung und Abrechnung.** ICD-10-Kodierung, DRG-Gruppierung oder Morbi-RSA-Prüfungen auf Basis von KI erfordern die Übermittlung klinischer Informationen an den KI-Dienst. Systeme wie 3M/Solventum (US), ID Berlin (DE) oder DeepL-basierte Übersetzungsdienste für mehrsprachige Patientenakten verarbeiten jeweils Patientendaten im Klartext.

### CLOUD-Act-Risikobewertung der großen KI-Anbieter

| Anbieter | Eigentümer | Infrastruktur | CLOUD-Act-Risiko | Gesundheitseinsatz |
|---|---|---|---|---|
| **OpenAI (GPT-4o, o3)** | US (Microsoft-Partnerschaft) | Azure (MSFT) | 🔴 Direkt — US-Unternehmen auf US-Infrastruktur | Azure OpenAI Service in KVNO-KI-Plattform (TED 98706-2026) |
| **Google Gemini** | NYSE: GOOGL | Google Cloud (US) | 🔴 Direkt | Ambient Clinical Intelligence in Pilotprojekten |
| **Anthropic (Claude)** | US (Amazon-Beteiligung) | AWS / GCP | 🔴 Direkt — US-Unternehmen | Enterprise-API für Dokumentenanalyse |
| **Microsoft Copilot** | NYSE: MSFT | Azure (US) | 🔴 Direkt | M365-Integration in Kliniken/GKVen |
| **Nuance DAX (Microsoft)** | NYSE: MSFT (Übernahme 2022, 18,8 Mrd. USD) | Azure (US) | 🔴 Direkt | Marktführer klinische Sprachdokumentation |
| **DeepSeek** | CN (Hangzhou) | China-basiert | 🔴 Nicht CLOUD Act, aber CN-Datengesetze | Open-Source-Modelle lokal deploybar |
| **Mistral AI** | FR (Paris, SAS) | Scaleway (FR) | 🟢 EU-souverän | Self-hosted oder API; bevorzugte EU-Option |
| **Aleph Alpha (Luminous)** | DE (Heidelberg) | IONOS / STACKIT | 🟢 EU-souverän (DE) | BW-Verwaltung; Gesundheitssektor noch begrenzt |
| **Kimi (Moonshot AI)** | CN (Peking) | China-basiert | 🔴 Nicht CLOUD Act, aber CN-Datengesetze | Kimi 2.5 — leistungsfähig, aber chinesische Jurisdiktion |
| **OpenEuroLLM** | EU-Konsortium (13 Partner) | EuroHPC (LUMI, Leonardo) | 🟢 EU-souverän | Forschung; produktiver Einsatz ab 2026 |

### Integrationsplattformen — der versteckte Datenfluss

Neben den KI-Anbietern selbst entsteht ein zweites, oft übersehenes Risiko durch **cloudbasierte Integrationsplattformen**:

| Plattform | Eigentümer | CLOUD-Act-Risiko | Typischer Einsatz im Gesundheitswesen |
|---|---|---|---|
| **Zapier** | US (San Francisco) | 🔴 Direkt | Automatisierung: "Wenn neue E-Mail mit Befund, dann an KI-Zusammenfassung" |
| **Make (Integromat)** | CZ (Prag) | 🟢 EU-souverän | Workflow-Automatisierung, EU-Alternative zu Zapier |
| **Microsoft Power Automate** | NYSE: MSFT | 🔴 Direkt | M365-Workflows: Dokumentenfreigabe, Benachrichtigungen mit Patientendaten |
| **n8n** | DE (Berlin) | 🟢 EU-souverän (self-hosted möglich) | Open-Source-Automatisierung; self-hosted auf EU-Infrastruktur bevorzugt |
| **IFTTT** | US (San Francisco) | 🔴 Direkt | Consumer-Automatisierung, vereinzelt in Praxis-IT |

Das Problem: Integrationsplattformen sind **Datendrehscheiben**. Sie lesen, transformieren und weiterleiten Daten zwischen Systemen — häufig einschließlich Patientendaten, Termindetails, Befunde, Abrechnungsinformationen. Eine Zapier-Automatisierung, die E-Mails mit Befunden an eine GPT-Zusammenfassung weiterleitet, erzeugt eine **doppelte CLOUD-Act-Exposition**: einmal bei Zapier (US), einmal bei OpenAI (US). n8n (self-hosted auf EU-Infrastruktur) + Mistral (self-hosted oder Scaleway) ist die souveräne Alternative für denselben Workflow.

### Kernaussage — warum KI der vierte blinde Fleck ist

Die ersten drei blinden Flecken (Snowflake, Oracle Health, Qlik Cloud — §7.4) betreffen klassische Datenhaltung und Analytics. Der vierte blinde Fleck ist gravierender: **KI-Dienste verarbeiten die sensibelsten Daten im Gesundheitswesen — Arzt-Patienten-Gespräche, Diagnosen, Behandlungsverläufe — zwangsläufig im Klartext.** Clientseitige Verschlüsselung, die bei Datenspeichern funktioniert, versagt hier strukturell. Wer eine Transkriptions-KI oder einen Arztbrief-Generator auf Azure OpenAI, Google Gemini oder AWS Bedrock betreibt, übergibt die unverschlüsselten Rohdaten an eine CLOUD-Act-exponierte Infrastruktur.

**Die souveräne Alternative existiert:** Mistral-Modelle (oder vergleichbare Open-Source-LLMs) lassen sich über vLLM auf STACKIT, plusserver oder eigenem GPU-Cluster betreiben — vollständig innerhalb EU-Jurisdiktion, ohne API-Calls an US-Anbieter. Für Sprachtranskription: Whisper (OpenAI, aber Open-Source-Modell, lokal deploybar) auf eigener GPU. Für Integrationsplattformen: n8n (self-hosted, Berlin) statt Zapier. Der Funktionsumfang ist für 80 % der Gesundheits-KI-Anwendungsfälle ausreichend — und wächst mit jeder Mistral/Llama-Generation.

### Vier Fallbeispiele — das Spektrum von 🔴 bis 🟢

Die Theorie wird greifbar an konkreten Produkten, die heute im deutschen Gesundheitswesen eingesetzt werden oder werden sollen:

**Plaud AI (CN/US) — 🔴 Dreifache Exposition.** Plaud ist ein chinesisches Unternehmen (Shenzhen), das KI-gestützte Aufnahmegeräte für Arzt-Patienten-Gespräche vermarktet. Die Audiodaten werden zur Transkription an AWS US West (Oregon) übertragen und dort über OpenAI Whisper V3 und GPT verarbeitet. Plaud wirbt mit GDPR-Compliance, SOC 2 und HIPAA — verschweigt aber die strukturelle Dreifachexposition: chinesischer Eigentümer (CN-Datengesetze), US-Cloud-Infrastruktur (AWS Oregon, CLOUD Act) und US-KI-Backend (OpenAI). "Zero Data Retention" beim LLM-Provider bedeutet: nicht gespeichert nach Verarbeitung — aber während der Verarbeitung liegt die Stimme des Patienten im Klartext auf US-Servern. Für Gesundheitsdaten nach § 393 SGB V: nicht geeignet.

**Tandem Health (SE) — 🟡 EU-Firma mit US-KI-Backend.** Tandem Health (Stockholm, $50 Mio. Funding) ist ein schwedisches Unternehmen, das KI-gestützte Dokumentation für Kliniken anbietet — aktuell expandierend nach Deutschland (Partnerschaft mit Eterno). Tandem nutzt OpenAI Whisper für Transkription und GPT-4 für Zusammenfassung. Audio wird nach Transkription gelöscht, keine Modeltraining auf Patientendaten (ISO 27001, ISO 13485, GDPR). Alle Daten sollen "ausschließlich in europäischen Rechenzentren" verarbeitet werden. Die offene Frage: Ob die OpenAI-Modelle via Azure OpenAI EU (Microsoft-Jurisdiktion, vgl. §5.3) oder über die direkte OpenAI-API (US-Server) angebunden sind, ist nicht öffentlich dokumentiert. Im besten Fall (Azure EU): Microsoft-CLOUD-Act-Restrisiko wie bei den KI-Brokern. Im schlechtesten Fall (direkte API): US-Serververarbeitung.

**Doctolib (FR/AWS) — 🟡 Strukturelles Restrisiko trotz Verschlüsselung.** Doctolib (Paris, bereits in §12.5 bewertet) hostet auf AWS Frankfurt und Paris, hat BSI C5 Typ 2 seit 2025 und verschlüsselt Gesundheitsdaten zusätzlich auf Applikationsebene (AES-256, HSM-Schlüsseltrennung über HashiCorp). Ein französisches Gericht wertete dies 2021 als ausreichend. Aber: AWS (NASDAQ: AMZN) unterliegt dem CLOUD Act, HashiCorp (NYSE: HCP) ebenfalls — Serverstandort Frankfurt ändert die Jurisdiktion über den Provider nicht. Die Applikationsverschlüsselung schützt ruhende Daten, aber Doctolibs SaaS-Funktionen (Terminbuchung, Patientenkommunikation, Videosprechstunde) erfordern Klartextverarbeitung im laufenden Betrieb. C5 Typ 2 belegt technische Sicherheit — nicht CLOUD-Act-Immunität.

**Averbis (DE) — 🟡 Souveräne NLP, aber Azure OpenAI für Arztbriefe.** Averbis (Freiburg, Spin-off Universitätsklinikum 2007) bietet zwei Produkte mit fundamental unterschiedlichem Risikoprofil: **Health Discovery** (NLP/Informations-Extraktion) läuft als eigene Engine on-premise im Krankenhaus-Netzwerk — strukturell souverän, keine US-Abhängigkeit. **Medical Summary** (automatische Arztbrief-Generierung) nutzt jedoch **Azure OpenAI in der EU Datazone**, wie das Architekturdiagramm von Averbis selbst zeigt: Patientendaten (PID, Diagnosen, Laborwerte, Medikation) fließen aus dem Krankenhaus-Netzwerk an Azure OpenAI, wo sie "temporär verarbeitet" werden. Das ist exakt das Muster, das §5.3 beschreibt: Azure EU-Region ändert nichts an der Microsoft-Jurisdiktion. CLOUD Act greift über die Unternehmensstruktur, nicht den Serverstandort. Für die reine NLP-Extraktion (Health Discovery on-premise) bleibt Averbis souverän. Für die generative KI-Funktion (Medical Summary) gilt dasselbe Restrisiko wie bei allen Azure-OpenAI-basierten Diensten.

| Anbieter | Sitz | KI-Backend | Infrastruktur | Risiko | Eignung § 393 Klasse 1 |
|---|---|---|---|---|---|
| **Plaud AI** | CN (Shenzhen) | OpenAI Whisper + GPT (US) | AWS Oregon (US) | 🔴 Dreifach (CN + US-Cloud + US-KI) | ❌ Nicht geeignet |
| **Tandem Health** | SE (Stockholm) | OpenAI Whisper + GPT-4 | "EU-Rechenzentren" (Details offen) | 🟡 EU-Firma, aber OpenAI-Abhängigkeit | ⚠️ Nur wenn Azure EU + Risikoakzeptanz |
| **Recare Voice** | DE (Berlin) | Nicht offengelegt | EU (ISO 27001, C5 Typ 2) | 🟡 DE-Firma, EU-Hosting, aber KI-Backend unklar | ⚠️ KI-Modell-Transparenz einfordern |
| **Doctolib** | FR (Paris) | Eigene Plattform | AWS Frankfurt/Paris (C5 Typ 2) | 🟡 FR-Firma auf US-Infra, verschlüsselt | ⚠️ Verschlüsselung reduziert, eliminiert nicht |
| **myScribe** | DE (Mannheim) | "Eigenes NLP" laut Website — KI-Backend nicht verifiziert | KIS-Add-on (HL7-FHIR) | 🟡 DE-Firma, KIS-Integration, aber KI-Modell unklar | ⚠️ KI-Backend vertraglich klären |
| **Averbis** | DE (Freiburg) | Health Discovery: eigene NLP; Medical Summary: **Azure OpenAI** (EU Datazone) | On-Premise NLP + Azure OpenAI extern | 🟡 NLP souverän, aber Arztbrief-KI auf Azure OpenAI | ⚠️ Medical Summary: Microsoft-CLOUD-Act-Risiko |
| **hAIppokrates (Greenbay)** | DE (Leipzig) | GPT + Whisper **lokal on-premise** | UKL-eigenes Rechenzentrum | 🟢 Vollständig souverän — kein externer API-Call | ✅ Alle Patientendaten bleiben im Klinikum |

**Recare Voice — das Transparenzproblem.** Recare Deutschland GmbH (Berlin, €37 Mio. Funding, DNV als größter Anteilseigner) bietet mit Recare Voice KI-gestützte Echtzeit-Dokumentation von Patientengesprächen für über 1.000 Krankenhäuser. Die Plattform ist ISO 27001- und BSI-C5-Typ-2-zertifiziert, verarbeitet Daten in Europa und wirbt mit "Zero Knowledge"-Architektur. Das Problem: **Welches Sprachmodell die Transkription und Zusammenfassung antreibt, ist nicht öffentlich dokumentiert.** Wenn Recare im Backend OpenAI Whisper oder GPT nutzt (direkt oder via Azure), gelten dieselben Vorbehalte wie bei Tandem Health. Wenn ein eigenes oder EU-gehostetes Modell verwendet wird, wäre das Risikoprofil deutlich besser. Für Kliniken, die Recare Voice evaluieren: Die Frage "Welches KI-Modell verarbeitet unsere Patientengespräche, und auf welcher Infrastruktur?" muss vertraglich beantwortet sein — nicht auf der Marketingseite.

**myScribe — KIS-Integration, aber KI-Backend unklar.** myScribe GmbH (Mannheim, gegründet von der Ärztin Ira Stoll am Universitätsklinikum Heidelberg) generiert mehrseitige Arztbriefe aus Visite-Notizen, Laborbefunden, Bildgebung, Diagnosen und Medikation über HL7-FHIR-Schnittstellen zum KIS. Die Website behauptet ein "eigenentwickeltes NLP-Modell" — aber ein Startup mit ~14 Mitarbeitenden, das mehrseitige Fließtext-Arztbriefe in Sekundenbruchteilen generiert, setzt mit hoher Wahrscheinlichkeit ein großes Sprachmodell (GPT, Claude oder vergleichbar) als Backend ein. **Welches Modell die Textgenerierung antreibt und auf welcher Infrastruktur es läuft, ist nicht öffentlich dokumentiert.** Für Kliniken gilt dieselbe Empfehlung wie bei Recare Voice: Das KI-Backend muss vertraglich offengelegt sein, bevor Patientendaten verarbeitet werden. Wenn myScribe im Hintergrund Azure OpenAI nutzt, gelten dieselben Vorbehalte wie bei Averbis Medical Summary.

**hAIppokrates (Greenbay Healthcare, Leipzig) — 🟢 Der Beweis, dass es geht.** hAIppokrates ist ein KI-System für Arztbrief-Generierung und Transkription von Arzt-Patienten-Gesprächen, das **vollständig on-premise im Rechenzentrum des Universitätsklinikums Leipzig (UKL)** betrieben wird. Die Architektur: GPT als Sprachmodell und OpenAI Whisper als Transkriptionsengine laufen lokal auf klinikeigener Hardware — kein API-Call an OpenAI, kein Azure, kein externer Cloud-Dienst. Alle Patientendaten (Diagnosen, Medikation, Gesprächsaufnahmen, Laborwerte) sind dem lokalen Modell verfügbar, verlassen aber zu keinem Zeitpunkt das Krankenhaus-Netzwerk. Das System wurde von der Greenbay Healthcare GmbH (Leipzig) in Zusammenarbeit mit 4K Analytics GmbH und dem UKL entwickelt. Nach einer erfolgreichen Pilotphase mit über 100 Nutzern befindet sich hAIppokrates im Roll-out.

**Warum das wichtig ist:** hAIppokrates widerlegt die verbreitete Annahme, dass generative KI im Gesundheitswesen zwangsläufig US-Cloud-Infrastruktur erfordert. GPT-Modelle und Whisper sind als Open-Source- oder Open-Weight-Modelle verfügbar und lokal deploybar — die Infrastruktur (GPU-Server im eigenen RZ) ist die Investition, nicht die Modellverfügbarkeit. Was das UKL Leipzig vormacht, können andere Kliniken und GKVen nachbauen: **Souveräne generative KI für Gesundheitsdaten ist kein Zukunftsversprechen — sie läuft produktiv in einem deutschen Universitätsklinikum.**

> **Transparenzhinweis:** Greenbay Healthcare GmbH und 4K Analytics GmbH (Herausgeber dieses Dokuments) gehören zum selben Unternehmensverbund. Die Bewertung folgt denselben Kriterien wie bei allen anderen Anbietern: Eigentümerschaft, Infrastruktur-Standort, KI-Backend, Datenfluss. Die On-Premise-Architektur des UKL Leipzig ist durch die IT-Abteilung des UKL verifizierbar.

> **Das Muster:** Plaud demonstriert das Worst-Case: CN-Firma sendet Arzt-Patienten-Audio an US-Server und US-KI. Averbis zeigt die **typische Hybridlösung**: eigene NLP souverän, generative KI auf Azure OpenAI. myScribe und Recare Voice zeigen das **Transparenzproblem**: deutsche Firmen, die ihr KI-Backend nicht offenlegen. hAIppokrates am UKL Leipzig zeigt den **souveränen Weg**: GPT und Whisper lokal on-premise, alle Patientendaten im Klinik-Netzwerk, kein US-Cloud-Kontakt. Der Unterschied ist nicht das Modell — sondern wo es läuft.

### Vibecoding-Plattformen — KI-Entwicklung mit doppelter Bindung

Ein wachsender Trend im Gesundheitswesen: Fachabteilungen und IT-Teams nutzen KI-gestützte Entwicklungsplattformen ("Vibecoding"), um interne Tools, Dashboards oder Patientenportale per natürlichsprachigem Prompt zu erstellen — ohne klassische Softwareentwicklung. Das CLOUD-Act-Problem ist hier **doppelt**:

**Erstens — die KI im Hintergrund.** Vibecoding-Plattformen nutzen große Sprachmodelle (typischerweise GPT-4o, Claude oder Gemini) als Code-Generatoren. Jeder Prompt — "Erstelle eine Anwendung, die Patientendaten aus unserem KIS lädt und eine Übersicht nach ICD-10-Diagnosen erstellt" — wird an den KI-Dienst übertragen und dort im Klartext verarbeitet. Die Prompts enthalten Geschäftslogik, Datenstrukturen, API-Schlüssel, und beschreiben im Detail, wie die Organisation Patientendaten verarbeitet. Bei US-KI-Anbietern sind diese Prompts CLOUD-Act-exponiert.

**Zweitens — die Plattform als Laufzeitumgebung.** Der entscheidende Unterschied zu klassischen KI-Assistenten: Vibecoding-Plattformen sind darauf ausgelegt, dass die erstellten Anwendungen **auf der Plattform gehostet bleiben** — nicht exportiert und selbst betrieben werden. Lovable, Bolt, Replit und v0 bieten integrierten Hosting-Service: Die Anwendung wird auf der Plattform entwickelt, getestet und produktiv betrieben. Wenn diese Anwendung Patientendaten verarbeitet, liegen die Daten dauerhaft auf der Plattform-Infrastruktur — und unterliegen der Jurisdiktion des Plattformbetreibers.

| Plattform | Eigentümer | KI-Backend | Hosting | CLOUD-Act-Risiko |
|---|---|---|---|---|
| **Lovable** | SE (Stockholm) | GPT-4o / Claude (US) | Plattform-hosted (AWS/Vercel) | 🟡 EU-Eigentümer, aber US-KI + US-Hosting-Infrastruktur |
| **Bolt.new (StackBlitz)** | US (San Francisco) | GPT-4o / Claude (US) | StackBlitz Cloud (US) | 🔴 Direkt — US-Unternehmen, US-KI, US-Hosting |
| **Replit** | US (San Francisco) | Eigene + GPT-4o (US) | Replit Cloud (GCP, US) | 🔴 Direkt — US-Unternehmen auf Google Cloud |
| **v0 (Vercel)** | US (San Francisco) | GPT-4o (US) | Vercel Edge (AWS, US) | 🔴 Direkt — US-Unternehmen, US-Infrastruktur |
| **Cursor** | US (San Francisco) | GPT-4o / Claude (US) | Lokale IDE, aber Prompts an US-KI | 🟠 Code bleibt lokal, Prompts an US-Cloud |
| **GitHub Copilot** | US (Microsoft/GitHub) | GPT-4o (US) | Cloud-basiert (Azure) | 🔴 Direkt — Microsoft-Tochter |
| **Windsurf (Codeium)** | US (Mountain View) | Eigene Modelle (US) | Cloud-basiert | 🔴 Direkt — US-Unternehmen |

**Das Muster:** Bei Lovable (schwedischer Eigentümer) entsteht der Eindruck eines EU-Produkts. Aber die KI-Verarbeitung läuft über US-Modelle (OpenAI/Anthropic), und das Hosting der fertigen Anwendungen erfolgt typischerweise auf AWS oder Vercel — beides US-Infrastruktur. Der EU-Eigentümer ändert nichts an der US-Jurisdiktion über die Datenverarbeitung. Bei Bolt, Replit und v0 ist die Kette durchgängig US: US-Unternehmen → US-KI → US-Hosting.

**Warum das im Gesundheitswesen relevant ist:** Der Vibecoding-Trend senkt die Hürde für Fachanwendungen drastisch. Eine GKV-IT-Abteilung kann in Stunden ein internes Analysetool bauen, das Versichertendaten visualisiert. Eine Klinik-Verwaltung erstellt ein Patientenportal per Prompt. Das Problem: Wenn diese Anwendungen auf der Plattform verbleiben und Patientendaten verarbeiten, entsteht eine dauerhafte CLOUD-Act-Exposition, die weder durch C5 noch durch die DSGVO-Einwilligung des Patienten gedeckt ist.

**Base44 (Wix):** Eine Sonderstellung nimmt Base44 ein — ein Vibecoding-Tool, das 2025 von Wix (NASDAQ: WIX, Israel/US) übernommen wurde. Base44 wählt automatisch zwischen Claude Sonnet und Gemini 2.5 Pro, bietet integriertes Hosting mit Datenbank und Authentifizierung. Die gesamte Anwendung verbleibt auf der Plattform. Da Wix an der NASDAQ gelistet und US-kontrolliert ist, gilt für Base44-gehostete Anwendungen mit Patientendaten dasselbe Risiko wie für andere US-Plattformen — unabhängig davon, wo die Server stehen.

**Die souveräne Alternative:** Für die Entwicklungsphase können Open-Source-KI-Assistenten (Mistral Codestral, StarCoder, lokal via Continue.dev oder Tabby) auf eigener Infrastruktur genutzt werden. Entscheidend ist die Trennung: KI-gestütztes Entwickeln auf EU-Infrastruktur, Hosting der fertigen Anwendung auf EU-Infrastruktur (STACKIT, plusserver, eigenes RZ). Die Plattform-Bequemlichkeit von Lovable oder Replit geht verloren — aber die Datenhoheit bleibt gewahrt. Für unkritische Anwendungen ohne Patientendaten (interne Dashboards, öffentliche Informationsseiten) ist das Risiko geringer, aber auch hier sollte die Plattformwahl dokumentiert werden.

### KI-Broker — das DSGVO-Versprechen und seine Grenzen

Ein wachsender Markt deutscher und europäischer Anbieter verspricht "DSGVO-konforme KI" für Unternehmen: sogenannte KI-Broker oder KI-Gateways, die als Zwischenschicht zwischen der Organisation und den großen Sprachmodellen (OpenAI, Claude, Gemini) fungieren. Das Versprechen klingt überzeugend: **EU-gehostet, ISO 27001-zertifiziert, DSGVO-konform — und trotzdem GPT-4o, Claude und Gemini nutzen.** Für den Gesundheitssektor ist dieses Versprechen kritisch zu hinterfragen.

**Das Grundproblem:** Ein KI-Broker kann die eigene Plattform DSGVO-konform betreiben — Nutzerauthentifizierung, Audit-Logs, Datenverarbeitung in der EU. Aber wenn der Prompt mit Patientendaten an ein US-Sprachmodell weitergeleitet wird, verlässt er die EU-Jurisdiktion — zumindest für die Dauer der Verarbeitung. Die Optionen der Broker:

1. **Direkte OpenAI-API (US-Server):** Prompt geht an OpenAI in den USA. "Zero Data Retention" (OpenAI speichert nichts nach Verarbeitung) — aber während der Verarbeitung liegen die Daten im Klartext auf US-Infrastruktur und sind CLOUD-Act-exponiert.
2. **Azure OpenAI (EU-Region, z.B. Schweden/Frankfurt):** Prompt bleibt physisch in der EU, aber Azure ist ein Microsoft-Dienst (MSFT) — CLOUD Act greift über die Unternehmensstruktur, nicht den Serverstandort (vgl. §1.1).
3. **Self-hosted Modelle (Mistral, Llama):** Kein US-Anbieter involviert — die einzige Option ohne CLOUD-Act-Exposition. Aber nicht alle Broker bieten das an, und die Modellqualität ist für manche Anwendungsfälle noch eingeschränkt.

Die meisten KI-Broker nutzen Option 1 oder 2 — und kommunizieren das als "DSGVO-konform", weil sie einen Auftragsverarbeitungsvertrag (AVV) mit OpenAI/Microsoft haben und das DPF als Rechtsgrundlage anführen. Für den Gesundheitssektor ist das aus denselben Gründen unzureichend, die §1.2 und §9 dokumentieren: Das DPF ist anfechtbar (Schrems III), der AVV schützt nicht vor CLOUD-Act-Herausgabepflichten, und "Zero Data Retention" bedeutet "nicht gespeichert" — nicht "nicht verarbeitet".

| KI-Broker / Gateway | Sitz | KI-Backend | Hosting | CLOUD-Act-Risiko des KI-Backends |
|---|---|---|---|---|
| **Langdock** | DE (Berlin) | OpenAI, Claude, Mistral, Aleph Alpha | EU (ISO 27001, SOC 2) | 🟡 EU-Plattform, aber Prompts an US-Modelle (je nach Konfiguration) |
| **DeutschlandGPT** | DE (Berlin) | GPT-4o, Claude, Gemini, Mistral, Llama | Open Telekom Cloud (DE, C5) | 🟡 DE-Hosting, aber GPT/Claude-Prompts via Azure/API an US-Modelle |
| **meinGPT** | DE | OpenAI (Azure EU), Claude, Mistral | DE-hosted | 🟡 Azure OpenAI EU = Microsoft-Jurisdiktion |
| **Plotdesk** | DE | GPT-4o via Azure OpenAI (EU) | EU | 🟡 Explizit Azure OpenAI — Microsoft-CLOUD-Act-Risiko bleibt |
| **Omnifact** | DE | Diverse; Privacy Filter™ maskiert Daten vor KI-Übergabe | EU | 🟡 Maskierung reduziert Exposition, löst Grundproblem nicht (s.u.) |
| **Neuroflash** | DE (Hamburg) | GPT-4o, eigene Modelle | EU | 🟡 OpenAI-Abhängigkeit für Kernfunktionen |
| **kamium** | DE | ChatGPT, Gemini, Claude, Perplexity | Eigener Azure-Tenant (EU) | 🟡 Azure = Microsoft-Jurisdiktion |
| **Dust.tt** | FR (Paris) | OpenAI, Claude, Mistral, Gemini | EU/US (wählbar, SOC 2) | 🟡 EU-Hosting wählbar, aber US-Modelle verarbeiten Prompts |
| **nexos.ai** | LT (Vilnius) | 200+ Modelle (OpenAI, Claude, Mistral…) | EU (ISO 27001, SOC 2) | 🟡 EU-Gateway, US-Modelle im Backend |

**Omnifact-Sonderfall — und warum Maskierung kein Souveränitätsersatz ist:** Omnifact bietet als einziger Broker in dieser Übersicht einen "Privacy Filter", der sensible Daten (Namen, Diagnosen, Versichertennummern) **vor** der Übergabe an das KI-Modell maskiert. Die Rücktransformation erfolgt lokal. Das klingt nach Lösung — bei genauerer Analyse bleiben jedoch fünf strukturelle Probleme:

1. **Kontextuelle Re-Identifizierbarkeit.** Medizinische Daten sind strukturell identifizierend. "43-jährige Patientin, bilaterale Mastektomie 2024, BRCA1-positiv, Olaparib-Therapie" ist auch ohne Namen einem überschaubaren Personenkreis zuordenbar — insbesondere in Kombination mit Zeitstempel, behandelnder Einrichtung oder Diagnosesequenz. Je seltener die Erkrankung, desto geringer die Anonymisierungswirkung.
2. **Maskierungslücken.** Kein regelbasierter oder KI-gestützter Filter erkennt alle sensiblen Informationen zuverlässig. Medizinischer Freitext enthält unstrukturierte Angaben, Abkürzungen, kontextabhängige Sensitivität ("Ehemann positiv getestet" ist ohne medizinischen Kontext harmlos, im HIV-Kontext hochsensibel). Wenn der Filter eine Information übersieht, gehen ungeschützte Patientendaten an das US-Modell.
3. **Funktionale Grenze.** Ein Arztbrief-Generator, der den klinischen Kontext benötigt, funktioniert mit maskierten Daten nur eingeschränkt oder gar nicht. "Patient [MASKIERT], Diagnose [MASKIERT], Therapie [MASKIERT]" kann kein Modell zu einem sinnvollen Arztbrief verarbeiten. Je aggressiver die Maskierung, desto nutzloser die KI-Ausgabe — je weniger maskiert wird, desto größer die Exposition.
4. **Wer führt die Maskierung durch?** Wenn der Privacy Filter selbst ein KI-Modell nutzt, um sensible Daten zu erkennen, sieht dieses Modell die vollständigen Rohdaten. Die Frage verschiebt sich nur: Auf welcher Infrastruktur und bei welchem Anbieter läuft der Maskierungsfilter?
5. **Pseudonymisierung ≠ Anonymisierung.** Maskierte Daten sind pseudonymisiert, nicht anonymisiert im DSGVO-Sinne (Art. 4 Nr. 5). Pseudonymisierte Daten bleiben personenbezogene Daten — mit allen DSGVO-Pflichten inklusive Art. 48. Die CLOUD-Act-Exposition wird reduziert, nicht eliminiert.

Omnifacts Ansatz ist der beste unter den Brokern — aber "besser als die anderen" ist nicht dasselbe wie "ausreichend für Gesundheitsdaten". Für unkritische Workloads (Klasse 2–3) ist Maskierung ein pragmatischer Teilschutz. Für Klasse-1-Daten (ePA, Diagnosen, Medikation) bleibt das Urteil: Nur vollständig EU-gehostete Modelle ohne US-Anbieter-Beteiligung bieten strukturellen Schutz.

**Kernaussage für den Gesundheitssektor:** "DSGVO-konformer KI-Broker" ist kein Souveränitätsnachweis. Ein Broker kann DSGVO-konform betrieben werden und gleichzeitig Patientendaten an CLOUD-Act-exponierte Infrastruktur weiterleiten. Für Gesundheitsdaten nach § 393 SGB V Klasse 1 (ePA, Diagnosedaten, Medikation) gilt: Nur KI-Modelle, die vollständig auf EU-Infrastruktur ohne US-Anbieter-Beteiligung laufen (Mistral self-hosted, Aleph Alpha auf STACKIT/IONOS, OpenEuroLLM auf EuroHPC), bieten strukturellen CLOUD-Act-Schutz. KI-Broker mit US-Backend-Modellen sind für unkritische Workloads (Klasse 2–3) akzeptabel — für Patientendaten nicht.

---
