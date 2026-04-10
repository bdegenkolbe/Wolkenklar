# 6. Das Operator-Modell: US-Technologie unter EU-Kontrolle

## 6.1 Die Grundidee — und warum sie juristisch funktioniert

Frankreich hat mit S3NS (Thales × Google Cloud) einen Weg gefunden, der den scheinbaren Widerspruch auflöst: "Google Cloud kann SecNumCloud nicht erhalten" — und trotzdem trägt S3NS das Zertifikat.

Die Auflösung ist juristisch präzise: **Google LLC (Mountain View, CA)** kann SecNumCloud nie erhalten. Korrekt. Aber **S3NS SAS (Paris, Frankreich)** ist nicht Google. S3NS ist eine 100%-Thales-Tochter, die Google Cloud Technologie als Technologielizenz nutzt — wie ein Softwarehersteller, der eine Bibliothek einbindet. Google hat keine Eigentumsrechte, keine Stimmrechte, keine Kontrollbefugnis über S3NS und keinen Datenzugang.

Das Modell in der Struktur:

```
Thales S.A. (Paris, Frankreich, CAC 40)
        ↓ 100% Eigentum + vollständige Kontrolle
    S3NS SAS (Paris, Frankreich)
        ↓ Technologielizenz / API-Zugang
    Google Cloud Technologie (Compute Engine, Cloud Storage etc.)
```

ANSSI hat dieses Modell nach einem "in-depth risk assessment" als SecNumCloud-3.2-konform anerkannt — inklusive expliziter Validierung der Immunität gegen extraterritoriale Gesetze.

## 6.2 Die konkreten Schutzmaßnahmen im Operator-Modell

Was das Modell technisch und organisatorisch absichert:

| Anforderung | Umsetzung |
|---|---|
| Eigentümer muss EU-Rechtsperson sein | S3NS = 100% Thales-Tochter, französisches Recht |
| Kein US-Unternehmen darf Kontrolle haben | Google hat Null Stimmrechte, kein Datenzugang |
| Ausschließlich EU-Personal im Betrieb | Nur S3NS-Mitarbeiter (Frankreich) |
| Quellcode-Kontrolle | Quarantänezone: alle Google-Updates werden von S3NS analysiert und validiert vor Deployment |
| CLOUD-Act-Immunität | Gilt gegen Google LLC, nicht gegen S3NS SAS |
| Schlüsselverwaltung | Kundenkontrollierte Schlüssel, nie bei Google |

## 6.3 Das deutsche Pendant — Delos Cloud (SAP × Microsoft Azure)

Deutschland hat dasselbe Modell entwickelt, allerdings für Microsoft Azure statt Google Cloud, und mit SAP als Operator statt Thales:

**Delos Cloud GmbH** ist eine 100%-Tochter der SAP SE (Walldorf, DAX-notiert). Microsoft ist ausschließlich Technologielieferant — kein Eigentümer, kein Betreiber.

Die Kernanforderungen laut BSI Cloud Platform Requirements, die Delos erfüllt:
- Alle Daten der deutschen Verwaltung werden ausschließlich innerhalb Deutschlands verarbeitet
- Betrieb durch eine deutsche Betreibergesellschaft mit sicherheitsüberprüftem deutschem Personal
- Microsoft selbst kann in der Delos Cloud keinerlei Daten einsehen
- Updates werden erst vom BSI geprüft; das Funktionieren der Plattform ist auch bei Ablehnung bestimmter Updates gewährleistet
- Delos Cloud GmbH ist Eigentümerin der Infrastruktur, lizenziert und betreibt eigenständig

Der operative Betrieb erfolgt durch **Arvato Systems** (Bertelsmann-Tochter) — ein langjähriger Microsoft-Cloud-Partner mit Rechenzentren in Deutschland.

**Preis der Souveränität:** Die souveränen Microsoft-Dienste aus der Delos Cloud kosten **+15% auf die Microsoft-Listenpreise**. Das ist das messbare Kostenniveau für das Operator-Modell in Deutschland.

## 6.4 Weitere Operator-Modelle in Europa

| Operator-Modell | Operator (EU) | US-Technologie | Zertifizierung | Markt |
|---|---|---|---|---|
| **S3NS PREMI3NS** | Thales (FR) | Google Cloud | SecNumCloud 3.2 ✅ (Dez. 2025) | FR public sector, enterprise |
| **Delos Cloud** | SAP SE (DE) | Microsoft Azure | BSI Cloud Platform Requirements | DE Verwaltung, KRITIS |
| **Bleu** | Orange + Capgemini (FR) | Microsoft Azure | SecNumCloud (in Qualifizierung) | FR public sector |
| **T-Systems × Google** | Deutsche Telekom (DE) | Google Cloud | BSI C5, Gaia-X | DE Verwaltung, Gesundheit |

## 6.5 Kritische Bewertung — was das Modell löst und was nicht

Das Operator-Modell ist eine pragmatische Brücke zwischen Realitätsprinzip und Souveränitätsziel. Es ist kein Sovereignty-Washing — aber auch keine vollständige Souveränität.

**Was gelöst ist:**

- US-Behörden können nicht direkt an Microsoft/Google herantreten und Daten aus Delos/S3NS verlangen — der Operator ist eine EU-Rechtsperson ohne US-Jurisdiktion
- CLOUD Act trifft Google LLC und Microsoft Corp. — nicht Delos Cloud GmbH oder S3NS SAS
- Für Microsoft Office 365 und Azure-abhängige Organisationen, die nicht vollständig migrieren können: eine legitime Compliance-Lösung unter BSI-Aufsicht
- VS-NfD-eingestufte Verwaltungsdaten können auf Azure-Technologie verarbeitet werden — das war vorher nicht möglich

**Was strukturell offen bleibt:**

- Google/Microsoft liefern den Quellcode und die Software-Updates — das ist eine fundamentale Technologieabhängigkeit
- Wenn der US-Anbieter die Technologielizenz kündigt, läuft der Operator nicht mehr (strategisches Klumpenrisiko)
- Ob ein US-Gericht den Technologielieferanten zwingen könnte, eine Hintertür in einen Update einzubauen, der durch die Quarantänezone geht — juristisch offene Frage, praktisch nicht beobachtet
- Die Quarantänezone analysiert Updates auf bekannte Probleme — aber nicht auf theoretisch staatlich aufgezwungene versteckte Hintertüren

## 6.6 Das Souveränitätsspektrum — vier Stufen

```
FULL ISOLATION          OPERATOR MODEL          HYPERSCALER SOVEREIGN    SOVEREIGNTY WASHING
       │                      │                         │                       │
Cloud Temple (FR)         S3NS / Thales           AWS European Sovereign     AWS Frankfurt
3DS Outscale (FR)       Delos Cloud / SAP          Azure EU Boundary         Azure Deutschland
plusserver (DE)       T-Systems × Google           Google Workspace DE        Google Cloud DE
STACKIT (EU-RZ)       Bleu / Orange+Cap.
EWERK Leipzig (DE)

Eigentümer: EU          Eigentümer: EU           Eigentümer: US            Eigentümer: US
Technologie: EU/OSS     Technologie: US (lizenz)  Technologie: US           Technologie: US
CLOUD Act: kein         CLOUD Act: kein direkter  CLOUD Act: nur            CLOUD Act: direkt
Angriffspunkt           Angriff; Restfrage         Data Residency            angreifbar
```

Workload-Zuordnung und vollständige Entscheidungsmatrix: → **Kapitel 16** (Handlungsempfehlungen).

---
