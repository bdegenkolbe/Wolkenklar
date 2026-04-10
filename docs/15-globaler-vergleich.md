# 15. Globaler Vergleich: Wie Regionen dem CLOUD Act entkommen

## 15.1 Das globale Problem in einem Satz

Alle Regionen der Welt stehen vor demselben Problem: Wer Daten bei einem US-Unternehmen speichert — egal ob der Server in Frankfurt, Mumbai oder Nairobi steht — kann von US-Behörden zur Herausgabe gezwungen werden. Die Reaktion weltweit ist dieselbe: raus aus der US-Abhängigkeit. Wie weit jede Region dabei ist, unterscheidet sich dramatisch.

## 15.2 China — vollständige Abschottung durch Industriepolitik

**Strategie:** Staatlich koordinierte nationale Champions, eigene Chips, eigene Protokolle.

- **Markt:** Alibaba Cloud (36%), Huawei Cloud (19%), Tencent Cloud, Baidu AI Cloud — zusammen 75%+ des Inlandsmarkts. AWS/Azure operieren nur über lizenzierte chinesische Partner.
- **Hardware:** Huawei entwickelt eigene Chips (Kunpeng, Ascend) — nach US-Exportverboten erzwungen, jetzt strukturell souverän
- **Open Source:** China Mobile baut Public Cloud auf OpenStack-Basis, gemeinsam mit Huawei und Ministry of Industry standardisiert
- **Staatliche Koordination:** SOEs als Pflicht-Anbieter für Behördendaten; "Made in China 2025" als industriepolitisches Programm

**Caveat:** China entkommt dem US CLOUD Act — aber unterliegt vollständig dem chinesischen Geheimdienstzugriff. Es ist kein Datenschutz, sondern ein Kontrollwechsel.

## 15.3 Russland — sanktionsgetriebene Vollabschottung

**Strategie:** Erzwungene Lokalisierung durch Sanktionen, eigene proprietäre Cloud-Stacks.

- **Gesetz:** Datenlokalisierungsgesetz 2015 + extraterritoriale Anwendung seit 2022 auf alle Unternehmen mit russischen Nutzern, unabhängig vom Firmensitz
- **Pflichtregister:** Seit Februar 2025 kein ausländischer Hosting-Anbieter ohne Roskomnadzor-Eintragung — bis März 2025 kein einziger ausländischer Antrag
- **Anbieter:** Yandex Cloud (30%+ Marktanteil), SberCloud, Rostelecom — 85%+ nationaler Markt
- **Technik:** Sber migriert 2025 von Kubernetes auf eigenen Container-Orchestrator. Sovereign Internet Law: eigenes DNS als Alternative zum globalen System
- **Marktgröße:** 3,1 Mrd. USD 2025, projiziert 7,4 Mrd. USD 2033

**Caveat:** Russland entkommt dem CLOUD Act — ist aber dem FSB-Geheimdienstzugriff vollständig ausgesetzt. Kein Gewinn für Datenschutz.

## 15.4 Arabische Staaten — Petrodollar-finanzierte Souveränität

**Strategie:** US-Anbieter lokal erzwingen, eigene Regeln setzen, mit Finanzmacht durchsetzen.

- **Saudi-Arabien:** 18-Milliarden-Dollar-Rechenzentrum-Strategie. Alle drei großen US-Hyperscaler haben lokale Zonen gebaut. PDPL mit Datenlokalisierungspflicht.
- **UAE:** OneCloud — vollständig innerhalb der Landesgrenzen betriebene souveräne Hyperscale-Plattform auf Oracle Alloy. UAE Digital Government Strategy 2025.
- **Sonderkonditionen:** Arabische Staaten zwingen US-Anbieter zu lokalen Servern, lokalem Personal, lokaler Schlüsselverwaltung und Sonderklauseln, die eigene Gesetze über US-Nutzungsbedingungen stellen.
- **Restrisiko:** Für Verteidigung und kritische Infrastruktur bleibt CLOUD-Act-Risiko strukturell bestehen.

**Caveat:** Sovereignty-Washing auf Hochglanz — aber mit echter Finanzkraft dahinter.

## 15.5 Israel — das lehrreichste Negativbeispiel

**Strategie:** Volle Abhängigkeit von Google und Amazon — mit vertraglich erkauften Sonderklauseln.

- **Project Nimbus:** 1,2-Milliarden-Dollar-Vertrag mit Google und Amazon für Cloud-Services für Regierung, Verteidigungsapparat und IDF. Lokale Rechenzentren in Israel.
- **Sonderklausel 1:** Vertrag verbietet Google und Amazon explizit, Israel den Dienst zu verweigern — auch wenn israelische Nutzung gegen Nutzungsbedingungen verstößt.
- **Wink-Mechanismus:** Israel bestand auf versteckten Signalen in Zahlungstransaktionen, die geheim anzeigen, wenn ausländische Gerichte Datenzugriff verlangen. Google und Amazon stimmten zu. Microsoft weigerte sich und verlor den Auftrag.
- **Was schiefging:** Microsoft sperrte Azure-Zugang für Geheimdiensteinheit 8200 — ein Knopfdruck in Redmond, der buchstäblich eine Datenkammer in Tel Aviv abdunkelte. Lokale Server bedeuten keine lokale Kontrolle.

**Zitat Israel Democracy Institute:** *"Israel kann von Datensouveränität sprechen, aber sobald Daten auf Microsoft Azure, AWS oder Google Cloud liegen, liegt das Schicksal dieser Daten in den Händen der Unternehmen, nicht des Staates."*

**Caveat:** Israel hat eine der stärksten Cyber-Tech-Industrien der Welt — und hat seine Staatssouveränität dennoch bewusst an zwei US-Konzerne ausgelagert.

## 15.6 Indien — Regulierung mit echtem Biss

**Strategie:** Datenlokalisierung durch Gesetz mit echter Sanktionierung.

- **DPDP Act 2023:** Pflicht zur Datenspeicherung in Indien für sensible Kategorien
- **RBI-Sanktionen:** American Express gesperrt (2021), Mastercard blockiert (2021) — wegen Datenspeicherung außerhalb Indiens. Das ist echter Biss.
- **Staatliche Cloud:** NIC Cloud für Behörden. RBI baut 2025/26 eigene Financial Services Cloud für alle Banken.
- **Problem:** Indien erzeugt 20% der weltweiten Daten — hat aber weniger als 2% der globalen RZ-Kapazität.

## 15.7 Japan — staatlich finanziertes Drei-Souveränitäten-Modell

**Strategie:** Klare Architektur-Vorgabe + 500 Mio. USD Staatsförderung.

- **Drei Souveränitäten (NTT DATA):** Data Sovereignty (Verschlüsselung), System Sovereignty (Software-Spezifikationen, Quellcode), Operational Sovereignty (japanisches Personal, lokale Schlüssel)
- **ESPA:** ca. 500 Mio. USD für souveräne Cloud- und KI-Rechenkapazitäten
- **Government Cloud:** Sakura Internet baut den Government Cloud — japanisches Unternehmen, japanische RZ, japanisches Personal
- **Industriekonzerne:** NTT und Fujitsu bauen souveräne Plattformen für regulierte Industrien

## 15.8 Brasilien & Südamerika — Ansätze ohne Eigenaufbau

- LGPD (Brasiliens DSGVO) seit 2020 — Regulierung vorhanden, Durchsetzung schwächer als Indien
- AWS São Paulo: lokale Region, aber US-Anbieter
- Heimische Anbieter: kaum skalierbar; Rest Südamerikas weitgehend auf US-Hyperscaler angewiesen

## 15.9 Afrika — Wille ohne Infrastruktur

- 223 Rechenzentren auf 54 Länder verteilt (Mitte 2025). Südafrika 56, Kenia 19, Nigeria 17
- Nigeria: 17 RZ in Lagos, Stromnetz liefert im Schnitt 4 Stunden täglich — Dieselgeneratoren erforderlich
- Afrika erzeugt 18% der Weltbevölkerung, aber weniger als 4% der globalen KI-Trainingsdaten
- Strategischer Ausweg: Shared Digital Infrastructure — regionale RZ-Pools statt Einzelkämpfer je Land

## 15.10 Das globale Muster — ein Satz je Region

- **China & Russland:** Souverän — aber wegen staatlicher Kontrolle, nicht Datenschutz. Kein Modell für Europa.
- **Arabische Staaten:** Kaufen Souveränität mit Petrodollar — zwingen US-Anbieter zu lokalen Servern, Schlüsseln, Regeln.
- **Indien & Japan:** Machen es richtig — Regulierung mit Biss plus staatliche Finanzierung eigener Infrastruktur.
- **Europa:** Hat die besten Regeln der Welt — und kauft trotzdem bei US-Hyperscalern ein. Das ist der europäische Widerspruch.
- **Israel:** Das lehrreichste Negativbeispiel — stärkste Cyber-Nation, schwächste Cloud-Souveränität. Microsoft konnte buchstäblich das Licht ausknipsen.
- **Brasilien & Afrika:** Wollen — können noch nicht. Infrastruktur fehlt.

---
