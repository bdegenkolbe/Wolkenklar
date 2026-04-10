# 8. Der vollständige EU-Plattformstack: US-Hyperscaler ersetzen

## 8.1 Das eigentliche Problem — nicht eine Datenbank, sondern ein Ökosystem

Ein US-Hyperscaler-Stack ist kein einzelner Dienst, sondern ein Ökosystem aus 15–20 miteinander integrierten Schichten — am deutlichsten bei Azure/M365, aber strukturell vergleichbar bei AWS und Google Workspace. Wer nur seine CPU auf EU-Cloud verschiebt, aber E-Mails bei Exchange Online, Dateien bei SharePoint und Identitäten bei Azure Entra ID lässt, hat keine Cloud-Souveränität. Das gilt sinngemäß auch für Organisationen auf AWS (WorkMail, WorkDocs, IAM Identity Center) oder Google Workspace (Gmail, Drive, Cloud Identity). Kapitel 7.3 zeigt für jede dieser Schichten den souveränen EU-Ersatz. Kapitel 8 zeigt, dass dieser Ersatz in der Praxis funktioniert und wie er als Gesamtarchitektur aussieht.

## 8.2 Der Praxisbeweis: Schleswig-Holstein

Das überzeugendste Argument gegen "das ist nicht praxistauglich" ist ein laufendes Produktivsystem auf Bundesland-Ebene. Schleswig-Holstein (30.000 Mitarbeitende, 9 Ministerien, 20 Behörden) hat migriert: Microsoft Office → LibreOffice (80% abgeschlossen), Exchange → Open-Xchange + Thunderbird (40.000 Accounts, abgeschlossen), SharePoint → Nextcloud (laufend), Teams → Jitsi/OpenTalk (abgeschlossen), Active Directory → Univention Corporate Server (in Umsetzung).

Das finanzielle Ergebnis: **€15 Millionen jährliche Einsparungen** bei €9 Millionen Migrationsinvestition — positiver ROI ab Jahr 1.

**Was bleibt schwierig:** Komplexe VBA-Makros, proprietäre Excel-Formeln und tief integrierte Fachverfahren (KIS, GKV-Primärsysteme, SAP) haben keine 1:1-Entsprechung. Schleswig-Holsteins 80/20-Regel ist realistisch: 80% voller Open-Source-Betrieb, 20% verbleibende Abhängigkeit — mit dem Ziel, auch diese schrittweise abzulösen. Für Organisationen, die heute nicht vollständig migrieren können: das Operator-Modell (Delos Cloud) ist die Brücke.

## 8.3 Die vollständige souveräne Zielarchitektur

```
IDENTITÄT & ZUGANG (Zero-Trust)
  Keycloak (Open Source, Red Hat) ← ersetzt Azure AD/Entra ID
  Univention Corporate Server     ← ersetzt Active Directory
  FreeIPA                         ← Linux-Integration

COLLABORATION & OFFICE
  Nextcloud Hub / Euro-Office     ← ersetzt M365 / SharePoint / OneDrive
  Open-Xchange + Thunderbird      ← ersetzt Exchange / Outlook
  OpenTalk / Jitsi / Matrix       ← ersetzt Teams

INFRASTRUKTUR (EU-Cloud)
  STACKIT / plusserver (IaaS)     ← ersetzt Azure Compute
  MinIO / Ceph (Objektspeicher)   ← ersetzt Azure Blob Storage
  PostgreSQL / MariaDB            ← ersetzt Azure SQL / CosmosDB
  Kubernetes (self-managed)       ← ersetzt AKS

KI & ANALYTICS
  vLLM + Mistral (lokal/STACKIT)  ← ersetzt Azure OpenAI / Copilot
  Metabase / Apache Superset      ← ersetzt Power BI / Fabric
  Grafana + Prometheus            ← ersetzt Azure Monitor

CI/CD & DEVOPS
  GitLab (self-hosted)            ← ersetzt Azure DevOps / GitHub

SECURITY & COMPLIANCE
  OpenSearch / Wazuh (SIEM)       ← ersetzt Microsoft Sentinel
  Veeam auf EU-Storage            ← Backup / DR
```

**Gesamtbewertung:** Dieser Stack ist heute technisch vollständig produktionsreif. Der Engpass ist nicht die Technologie — es ist Betriebspersonal, Integrationskompetenz und Change Management. Schleswig-Holstein zeigt, dass es geht. Die Kosten sind mit einem ROI von Jahr 1 darstellbar. Der strategische Vorteil: dauerhafte Unabhängigkeit von US-Lizenzpreisen, US-Recht und US-Plattformentscheidungen.

---
