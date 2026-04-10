# 17. Regulatorischer Ausblick 2025–2027

Dieses Kapitel behandelt regulatorische Entwicklungen, die bis 2027 neue CLOUD-Act-Relevanz entfalten. Bereits abgeschlossene oder im Dokument ausführlich analysierte Regelwerke werden hier nicht wiederholt, sondern querverwiesen: CLOUD Act und FISA § 702 (→ Kap. 3), e-Evidence-VO (→ Kap. 4), Data Privacy Framework und Executive Agreement (→ Kap. 9), Digital Omnibus und Lobbyarbeit (→ Kap. 10), EU Data Act und Cloud-Portabilität (→ §16.6).

Die folgende Tabelle gibt den Überblick über laufende und kommende Entwicklungen mit unmittelbarer Relevanz für die CLOUD-Act-Exposition des Gesundheitswesens. Die drei wichtigsten werden im Anschluss vertieft: TI 2.0, GeDIG und EHDS.

| Instrument / Entwicklung | Status | CLOUD-Act-Relevanz |
|---|---|---|
| **TI 2.0 (Telematikinfrastruktur)** | Migration ab 2025, Vollbetrieb 2027 | Cloud-basierte TI-Gateways ersetzen Hardware-Konnektoren. Offene Frage: US-Konzerne als Gateway-Betreiber? (→ §17.1) |
| **GeDIG** | Referentenentwurf April 2026 | ePA-Ausbau auf 20 Mio. Nutzer, automatische FDZ-Ausleitung Ende 2026. Vergrößert CLOUD-Act-Angriffsfläche erheblich. (→ §17.2) |
| **EHDS (European Health Data Space)** | Ab 2026 schrittweise | Sekundärnutzung erhöht Datenpool-Attraktivität. Keine Cloud-Infrastrukturvorgaben — CLOUD-Act-Lücke. (→ §17.3) |
| **Schrems III (EuGH)** | Anhängig | Kippt das DPF, ändert sich das Enforcement-Bild schlagartig — sofortiger Handlungsdruck für alle US-Cloud-Nutzer. (Analyse: → §9.1) |
| **FISA § 702 Verlängerung** | Auslaufdatum 20. April 2026 | Verlängerung ohne Reformen zementiert RISAA-Erweiterungen. Ablauf würde US-Zugriff temporär einschränken. (Analyse: → §3.2) |
| **NIS2-Richtlinie** | In deutsches Recht umgesetzt (BSIG-Novelle) | Lieferketten-Risikobewertung ist Pflicht (Art. 21 Abs. 2 lit. d) — erfasst CLOUD-Act-exponierte Anbieter. GF-Haftung nach § 38 BSIG bei Verletzung der Sorgfaltspflicht. |
| **SharePoint On-Premise End-of-Life** | Juli 2026 | SharePoint 2013/2016/2019 verliert Support. Erzwingt Entscheidung: SharePoint Online (US-Cloud) oder souveräne Alternative (→ §8.3). |
| **STACKIT Lübbenau-RZ** | Fertigstellung 2027 | 11 Mrd. EUR, bis zu 100.000 GPUs. Erster EU-Anbieter mit Hyperscaler-Kapazität. (Analyse: → §5.5, §7.2) |
| **Euro-Office / Office.eu** | Rollout ab März–Q2 2026 | Erste produktionsreife souveräne M365-Alternative. (Analyse: → §8.3) |
| **BSI C5:2026** | Veröffentlicht 7. April 2026 | 168 Kriterien (Nachfolger C5:2020). Technische Sicherheit modernisiert (Container, PQC, Confidential Computing). Souveränität weiterhin nicht geprüft — separate Kriterien angekündigt. (Analyse: → §5.3) |
| **ANSSI-BSI Souveränitätskriterien** | Joint Statement 17. Nov. 2025 | ANSSI und BSI entwickeln gemeinsam Souveränitätskriterien auf Basis des EU Cloud Sovereignty Framework. Drei-Stufen-Progressionsmodell. Veröffentlichung "in Kürze". (Analyse: → §5.3) |
| **EuroHPC AI Factories** | 19 Standorte, laufend seit 2025 | Souveräne GPU-Infrastruktur für KI-Training. Zugang für Gesundheitsorganisationen. |

## 17.1 Telematikinfrastruktur (TI 2.0) — was sich durch die Migration ändert

Die CLOUD-Act-Exposition der heutigen TI ist in §12.8 dokumentiert: IBM betreibt zwei Kerndienste (Rezeptserver, Identity Provider), Arvato Systems trägt die Sicherheitsinfrastruktur mit US-Technologieabhängigkeit. An dieser Bestandsaufnahme ändert sich kurzfristig nichts. Was sich ändert, ist die Architektur selbst.

**Der Übergang von TI 1.0 zu TI 2.0:** Die bisherige TI setzte auf physische Konnektoren in jeder Praxis — teuer und wartungsintensiv, aber vollständig in Deutschland kontrolliert. TI 2.0 ersetzt diese Hardware durch cloud-basierte TI-Gateways: Praxen und Kliniken mieten TI-Zugang als Managed Service von zertifizierten Dienstleistern. Das macht die TI flexibler und günstiger — öffnet sie aber für die CLOUD-Act-Problematik, weil die Gateway-Betreiber US-kontrollierte Anbieter sein könnten.

**Die offene Frage:** Wer die TI-Gateway-Betreiber sein werden und ob darunter US-Konzerne zugelassen werden, ist regulatorisch nicht abschließend definiert. Hier entsteht ein strukturell neues CLOUD-Act-Einfallstor — zusätzlich zu den bestehenden IBM- und Arvato-Abhängigkeiten.

**Was Organisationen konkret tun können:** Die TI-Abhängigkeit ist derzeit nicht auflösbar — die TI-Nutzung ist gesetzlich verpflichtend und die gematik legt die Anbieter fest. Was zählt: eigene Systeme, die über die TI kommunizieren, sollten so gebaut sein, dass Daten auf dem Transportweg und im eigenen System verschlüsselt sind. Inhalte, die nicht zwingend im Klartext übertragen werden müssen, sollten Ende-zu-Ende verschlüsselt werden. Für die Architekturentscheidung eigener Gesundheits-IT-Systeme bleibt die TI ein Systembestandteil mit Restrisiko, das transparent dokumentiert werden sollte — auch im TIA (vgl. §16.4).

## 17.2 GeDIG 2026 — wie das neue Digitalgesetz die CLOUD-Act-Exposition erhöht

Das Gesetz für Daten und digitale Innovation im Gesundheitswesen (GeDIG) ist das Nachfolgeprojekt des DigiG und GDNG. Bundesgesundheitsministerin Nina Warken (CDU) hat den Referentenentwurf im ersten Quartal 2026 vorgelegt. Das Gesetz hat erhebliche Konsequenzen für die CLOUD-Act-Exposition des deutschen Gesundheitswesens — obwohl der Begriff im Gesetzentwurf nicht vorkommt.

**Was GeDIG im Kern vorhat**

Die ePA (elektronische Patientenakte) soll vom passiven Datenspeicher zum aktiven Navigationssystem für das Gesundheitssystem werden. Bis 2030 sollen rund 20 Millionen Versicherte (aktuell: ca. 4 Millionen) die ePA aktiv nutzen. Neue Funktionen: digitale Ersteinschätzung, automatische Terminvermittlung, E-Überweisungen, digitaler Medikationsprozess (ab Oktober 2026), Volltextsuche über alle ePA-Inhalte (Ende 2026). Die ePA wird damit zur zentralen Schaltstelle für Versorgungsdaten eines erheblichen Teils der deutschen Bevölkerung.

**Was das für die CLOUD-Act-Frage bedeutet**

Je mehr Versicherte die ePA nutzen und je mehr Daten in ihr gespeichert werden, desto größer ist die potenzielle CLOUD-Act-Exposition — falls die ePA-Infrastruktur bei US-kontrollierten Anbietern liegt. Die gematik hat die ePA auf einer Infrastruktur aufgebaut, die TI-zertifizierte Anbieter nutzen. Für den Vollbetrieb mit 20 Millionen aktiven Nutzern werden erhebliche Skalierungskapazitäten benötigt — genau die Kapazitäten, bei denen europäische Anbieter noch Aufholbedarf haben (vgl. Kap. 7).

Hinzu kommt der geplante FDZ-Ausbau: Ab Ende 2026 soll die automatische Ausleitung von ePA-Daten an das Forschungsdatenzentrum Gesundheit beim BfArM starten (aktuelle CLOUD-Act-Bewertung des FDZ: §12.6). Eine zentrale Plattform mit pseudonymisierten Gesundheitsdaten von Millionen Versicherten ist ein hochattraktives Ziel für CLOUD-Act-Zugriffe — auch pseudonymisierte Daten bleiben im Kontext einer großen Gesundheitsdatenbank re-identifizierbar. Die Frage, auf welcher Infrastruktur das FDZ für diese Skalierung betrieben wird, ist regulatorisch noch nicht abschließend festgelegt.

## 17.3 EHDS — der europäische Gesundheitsdatenraum und seine Grenzen

Der European Health Data Space (EHDS — Europäischer Gesundheitsdatenraum) ist eine EU-Verordnung, die ab 2026 schrittweise anwendbar wird. Sie schafft einen einheitlichen Rahmen für die Nutzung von Gesundheitsdaten in der EU — für die Versorgung (Primärnutzung) und für Forschung, Regulierung und Politikgestaltung (Sekundärnutzung).

**Was der EHDS regelt und was nicht**

Der EHDS verpflichtet Mitgliedstaaten, nationale Gesundheitsdatenzugangsstellen einzurichten, die Forschern und Behörden unter definierten Bedingungen Zugang zu anonymisierten Gesundheitsdaten geben. Er schafft EU-weit einheitliche Formate (z.B. für die Patientenzusammenfassung und das E-Rezept) und ermöglicht grenzüberschreitende Versorgung — ein Patient kann seine ePA-Daten künftig auch bei einem Arzt in Frankreich nutzen.

Was der EHDS nicht regelt: die CLOUD-Act-Frage. Der EHDS schreibt keine spezifischen Anforderungen an die Cloud-Infrastruktur vor, auf der Gesundheitsdaten verarbeitet werden. Eine nationale Gesundheitsdatenzugangsstelle könnte theoretisch bei einem US-Hyperscaler betrieben werden — und damit dem CLOUD Act unterliegen. Der EHDS ist ein Daten-Governance-Rahmen, kein Infrastruktur-Souveränitätsgesetz.

Für GKVen und Kliniken relevant: Der EHDS-Pflichten zur Sekundärnutzung — also die Möglichkeit, dass Forscher und Behörden Daten anfragen können — erhöhen den Wert und damit die Attraktivität der Datenpools. Umso wichtiger wird die Frage, auf welcher Infrastruktur diese Daten liegen und wer außer autorisierten europäischen Nutzern potenziell darauf zugreifen kann.

---
