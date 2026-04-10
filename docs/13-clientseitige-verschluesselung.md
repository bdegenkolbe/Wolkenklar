# 13. Clientseitige Verschlüsselung: Teilschutz, kein Allheilmittel

## 13.1 Die Grundidee

Wenn ein US-Anbieter nur verschlüsselte Daten sieht und nie die Schlüssel besitzt, kann er einer CLOUD-Act-Anordnung technisch nicht nachkommen — er hat schlicht keine lesbaren Daten. Das ist richtig — aber nur unter bestimmten Bedingungen.

## 13.2 Die drei Verschlüsselungsmodelle

| Modell | Beschreibung | Schutz vs. CLOUD Act |
|---|---|---|
| **Provider-Managed Keys** (Standard) | Anbieter verschlüsselt mit eigenen Schlüsseln. Kann jederzeit entschlüsseln. | ❌ Kein Schutz |
| **BYOK** (Bring Your Own Key) | Kunde generiert eigene Schlüssel, übergibt sie dem Anbieter-KMS. Anbieter verwaltet Schlüssel in eigenem System. | ⚠️ Schwacher Schutz — Anbieter hat technisch Zugriff |
| **HYOK** (Hold Your Own Key) | Schlüssel bleiben ausschließlich beim Kunden in eigenem HSM. Anbieter empfängt nur verschlüsselte Daten. Anbieter kann technisch **nicht** entschlüsseln. | ✅ Struktureller Schutz |

**Der kritische Unterschied BYOK vs. HYOK:**

Beim BYOK speichert der Cloud-Anbieter die Schlüssel in seinem eigenen Key Management System — er hat unter Umständen technisch Zugriff. Law Enforcement kann den Anbieter zwingen, BYOK-Schlüssel zur Entschlüsselung einzusetzen. Der CLOUD Act schreibt Providern nicht explizit vor, Daten entschlüsseln zu müssen — **verbietet es aber auch nicht**. Beim HYOK liegen Schlüssel nie in der Umgebung des Anbieters — die Anforderung ist technisch nicht ausführbar.

## 13.3 Wo HYOK funktioniert

HYOK schützt strukturell vor CLOUD-Act-Zugriff bei:

- Statischen Datenspeichern (Archivdaten, Backup, Objektspeicher)
- File-Storage (Dokumente, Bilder, PDFs auf US-Cloud-Infrastruktur)
- Eigener Software mit Client-Anbindung (Anwendungslogik läuft lokal, nur verschlüsselte Blobs in der Cloud)
- Backup-Lösungen (Verschlüsselung vor Upload, Schlüssel on-premise)

## 13.4 Wo HYOK nicht funktioniert — die entscheidende Grenze

| Anwendungsfall | Warum HYOK nicht hilft |
|---|---|
| **Microsoft 365 / SharePoint** | Suchindex, Co-Authoring, Teams-KI benötigen unverschlüsselten Inhalt server-seitig |
| **E-Mail (Exchange Online / Gmail)** | Spam-Filter, Virenscanner, Regelverarbeitung, KI-Zusammenfassungen laufen auf unverschlüsselten Inhalten |
| **KI / LLM-Services (Azure OpenAI, AWS Bedrock)** | KI-Modell muss Prompt lesen — verschlüsselte Prompts kann kein Modell verarbeiten |
| **SaaS-Anwendungen (Salesforce, SAP Cloud)** | Jede SaaS-Funktion (Suche, Filter, Analyse) erfordert Klartextdaten im Provider-Speicher |
| **Real-time Analytics / BI (Qlik Cloud, Power BI)** | Aggregation, Filterung, Visualisierung erfordern Klartextdaten |

Das Grundprinzip: **Ein System kann nur verarbeiten, was es lesen kann.** HYOK ist Schutz für ruhende Daten (Data at Rest), nicht für verarbeitete Daten (Data in Use).

## 13.5 Gesundheitssektor-Matrix

| Workload | HYOK-Schutz möglich? | Empfehlung |
|---|---|---|
| ePA-Datenspeicherung (statisch) | ✅ Ja | HYOK auf EU-Infrastruktur |
| Patientendaten-Archiv | ✅ Ja | HYOK + EU-Anbieter |
| KIS-Software (Krankenhausinformationssystem) | ⚠️ Nur wenn lokal | On-Premise oder EU-Anbieter |
| Telemedizin-Plattform | ❌ Nein | Nur EU-souveräne Anbieter |
| KI-gestützte Diagnostik (US-LLM) | ❌ Nein | On-Premise vLLM auf eigenem GPU-Cluster |
| SharePoint/Teams für Klinik | ❌ Nein | Nextcloud auf STACKIT/Hetzner |
| Buchhaltung/ERP auf US-SaaS | ❌ Nein | SAP on-premise oder EU-ERP |

---
