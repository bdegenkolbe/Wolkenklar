# 4. Europäischer Behördenzugriff: e-Evidence-VO, Five Eyes und die ethische Frage

## 4.1 Die blinde Seite der Souveränitätsdebatte

In der Diskussion um CLOUD Act und Datensouveränität wird eine naheliegende Gegenfrage oft nicht gestellt: **Was können europäische Behörden eigentlich?** Und: Warum sollte man nicht einfach darauf vertrauen, dass westliche Verbündete — NATO, Five Eyes, EU-Partner — ähnliche Sicherheitsinteressen teilen und damit ethisch akzeptabler sind als ein "Souveränitäts"-Denken, das Kooperation verhindert?

Die Antwort auf diese Frage ist differenziert — und für die Architekturentscheidung wichtiger als häufig angenommen.

## 4.2 Die e-Evidence-Verordnung — der europäische CLOUD Act

Die EU hat mit der Verordnung (EU) 2023/1543 ein Instrument geschaffen, das strukturell dem CLOUD Act ähnelt: **grenzüberschreitender Direktzugriff auf elektronische Daten ohne klassisches Rechtshilfeverfahren.** Ab 18. August 2026 verbindlich.

Das Instrumentarium:

- **EPOC (Europäische Herausgabeanordnung):** Strafverfolgungsbehörde eines EU-Mitgliedstaats fordert direkt bei einem Anbieter in einem anderen EU-Staat Daten an — Abonnentendaten, Verkehrsdaten, Inhaltsdaten. Keine vorherige Einschaltung der Justiz des Providerstaats erforderlich.
- **EPOC-PR (Sicherungsanordnung):** Sofortige Datensicherung, damit keine Daten gelöscht werden können.
- **Frist:** Zehn Tage im Normalfall, sechs bis acht Stunden im Notfall.
- **Sanktionen:** Bis zu 500.000 EUR oder 2% des weltweiten Jahresumsatzes bei Nichtbefolgung.
- **Reichweite:** Gilt auch für Anbieter aus Drittstaaten (USA, UK, Schweiz), sofern sie Dienste in der EU anbieten — diese müssen einen EU-Rechtsvertreter benennen.

Das klingt zunächst symmetrisch zum CLOUD Act. Aber es gibt fundamentale strukturelle Unterschiede.

## 4.3 Der strukturelle Vergleich: CLOUD Act vs. e-Evidence-VO

| Dimension | US CLOUD Act | EU e-Evidence-VO |
|---|---|---|
| **Anknüpfungspunkt** | Jurisdiktion über den Provider (Possession, Custody, Control) | Erbringung von Diensten im EU-Markt |
| **Gerichtliche Kontrolle (Inhaltsdaten)** | Richterlicher Herausgabebeschluss erforderlich | Richterliche Genehmigung + Prüfung durch Vollstreckungsbehörde |
| **Gerichtliche Kontrolle (Metadaten)** | Gerichtsbeschluss mit abgesenkten Anforderungen, teilweise nur behördliche Auskunftsanordnung | Richterliche Kontrolle abhängig von Datenkategorie |
| **Kontrolle ohne Richter** | NSL: kein Richter, kein Verdacht, für Metadaten | Kein strukturelles Äquivalent |
| **Massenüberwachung** | FISA § 702: Pauschale Jahreszertifizierung, kein Einzelfall | Kein Äquivalent in der e-Evidence-VO |
| **Ablehnungsgründe** | Nur Comity-Verfahren (völkerrechtliche Rücksichtnahme), entschieden nach US-Maßstäben | Katalog EU-Ablehnungsgründe: Grundrechtsverletzung, ne bis in idem, Immunität, fehlende beiderseitige Strafbarkeit |
| **Benachrichtigung Betroffener** | Kann durch Schweigeverfügung dauerhaft blockiert werden | Pflicht bei Inhaltsdaten; Ausnahmen, aber keine unbegrenzte Sperrung |
| **Rechtsschutz für Nicht-US-Bürger** | Faktisch nicht vorhanden vor US-Gerichten | EU-Grundrechtecharta (Art. 8, Art. 47), nationaler Rechtsweg |
| **Verhältnismäßigkeit** | Nicht strukturell verankert für Nicht-US-Bürger | DSGVO + GRCh Art. 52 als fester Maßstab |
| **Geheimdienstlicher Zugriff** | FISA § 702, EO 12.333, NSL — ohne richterliche Einzelfallkontrolle | Kein Äquivalent; nationale Nachrichtendienste agieren nach nationalem Recht |
| **DSGVO-Konformität** | Strukturell verletzt Art. 48 DSGVO (verbietet Datentransfer in Drittstaaten ohne EU-rechtliche Grundlage) | Ist EU-Recht — kein Konflikt |
| **Überprüfbarkeit** | US-Gerichte, US-Maßstäbe | EuGH, Grundrechtecharta, nationale Verfassungsgerichte |

**Das Kernresultat:** Europäische Strafverfolgungsbehörden können auf Basis der e-Evidence-VO auf Daten zugreifen — aber in einem Rechtssystem, das an Grundrechte gebunden, verhältnismäßig angewendet und durch unabhängige Gerichte überprüfbar ist. Das ist strukturell ein anderes Vertrauensniveau als FISA § 702 oder National Security Letters.

## 4.4 Ist DSGVO relevant für europäischen Behördenzugriff?

**Direkt: Nein.** Die DSGVO regelt die Verarbeitung personenbezogener Daten durch private Verantwortliche — nicht die staatliche Strafverfolgung. Strafverfolgungsbehörden agieren auf Basis der JI-Richtlinie (2016/680) und nationalen Strafprozessordnungen. Das ist keine Lücke — es ist bewusste Systemtrennung.

**Indirekt: Ja.** Die DSGVO setzt — zusammen mit der EU-Grundrechtecharta — den übergeordneten Grundrechtsrahmen, in dem jede EU-Behördenhandlung stattfinden muss. Art. 52 GRCh verlangt Verhältnismäßigkeit bei Grundrechtseingriffen. Dieser Maßstab ist in EU-Recht strukturell eingebaut und durch den EuGH einklagbar. Im US-System ist er für Nicht-US-Bürger strukturell nicht eingebaut.

## 4.5 Five Eyes, NATO und die ethische Frage

Die naheliegende Position lautet: NATO-Verbündete teilen Sicherheitsinteressen, gemeinsame Werte, gemeinsame Bedrohungsanalysen. Mit Ländern, mit denen wir Geheimdienstinformationen teilen und gemeinsam kämpfen, könnten wir doch auch Gesundheitsdaten teilen — ethisch vertretbar im Sinne eines westlichen Werteverbunds?

Diese Position verdient eine ehrliche Auseinandersetzung in drei Dimensionen:

**Dimension 1: Was Five Eyes strukturell ist**

Five Eyes (USA, UK, Kanada, Australien, Neuseeland) ist ein Geheimdienstkooperationsrahmen auf Basis des UKUSA-Abkommens von 1946, der alle SIGINT (Fernmeldeaufklärung)-Daten standardmäßig teilt. Das bedeutet: Daten, die US-Behörden über FISA § 702 oder NSL erfassen, fließen strukturell in die Five-Eyes-Partner. Enthüllungen durch Edward Snowden und parlamentarische Untersuchungen haben gezeigt, dass Five Eyes-Staaten die eigenen Bürger der Partner ausspioniert haben — weil heimisches Recht die Überwachung der eigenen Bürger verbietet, nicht aber die Überwachung fremder Bürger durch Partnerstaaten.

Hinzu kommen 9 Eyes (+ Dänemark, Frankreich, Niederlande, Norwegen), 14 Eyes (+ Deutschland, Belgien, Italien, Spanien, Schweden) und Tier-B-Kooperationen, zu denen auch Deutschland gehört. Diese Ebenen haben unterschiedliche Kooperationstiefe, teilen aber alle das Grundprinzip: Nachrichtendienste sind keine Datenschutzbehörden.

**Dimension 2: Der Kategorieunterschied**

NATO und Five Eyes sind für einen spezifischen Zweck konstruiert: Sicherheit und Gefahrenabwehr gegen externe Bedrohungen. GKV-Gesundheitsdaten — Krebsdiagnosen, psychiatrische Befunde, HIV-Status, Medikamentenpläne von 74 Millionen Versicherten — sind nicht Gegenstand dieser Kooperation und es gibt keinen Legitimitätsgrund, warum sie es sein sollten.

Der CLOUD Act ist kein Geheimdienstgesetz — er ist ein Strafverfolgungsgesetz. Ein FBI-Agent, der in einer Drogenermittlung E-Mails eines Verdächtigen anfordert und dabei die Gesundheitsakten unbeteiligter GKV-Versicherter miterfasst, handelt nicht im Sinne eines "westlichen Werteverbunds." Er handelt im Rahmen eines Gesetzes, das keine adäquaten Schutzmechanismen für Nicht-US-Bürger enthält.

**Dimension 3: Die geopolitische Realität 2025/2026**

Der "westliche Verbund"-Gedanke hat seit 2025 eine neue Dimension bekommen. Die US-Regierung hat EU-Handelspartner mit Zöllen belegt, Druck auf europäische Institutionen ausgeübt und — im ICC-Präzedenzfall — demonstriert, dass Cloud-Dienste als politisches Druckmittel eingesetzt werden können. Wer Infrastrukturarchitektur auf politischem Vertrauen in einen spezifischen Verbündeten aufbaut, macht diese Architektur von politischen Konstellationen abhängig, die sich ändern.

**Fazit zur ethischen Frage:**

Es gibt keinen pauschalen "westlichen Verbund", dem man Gesundheitsdaten strukturell anvertrauen kann oder sollte. Es gibt Rechtssysteme — und europäisches Recht ist für diese Zwecke strukturell vertrauenswürdiger als US-Recht, weil es:

1. An Verhältnismäßigkeit gebunden ist (GRCh Art. 52)
2. Durch unabhängige Gerichte überprüfbar ist (EuGH, BVerfG)
3. Rechtsschutz für alle Betroffenen — nicht nur für eigene Bürger — vorsieht
4. Keine Massenüberwachung ohne Einzelfallprüfung kennt (kein FISA-Äquivalent)
5. Nicht von politischen Konstellationen einer einzelnen Regierung abhängt

Das ist kein antiamerikanisches Argument. Es ist ein rechtsstaatliches. Und es trägt die Konsequenz: Wer Gesundheitsdaten auf EU-souveräner Infrastruktur mit EU-rechtlichem Behördenzugriff hält, hat strukturell einen höheren Schutz — nicht weil Europa besser ist, sondern weil das europäische Recht für diesen Zweck besser konstruiert ist.

## 4.6 Praktische Konsequenz: Was dieser Vergleich für Architekturentscheidungen bedeutet

| Szenario | Bewertung |
|---|---|
| Strafverfolgungszugriff EU-Behörde mit Richtererlaubnis (e-Evidence-VO) | ✅ Rechtsstaatlich, DSGVO-kompatibel, anfechtbar |
| Strafverfolgungszugriff US-Behörde mit Herausgabebeschluss (CLOUD Act, Inhaltsdaten) | 🟡 Formal gerichtlich, aber kein Rechtsschutz für EU-Bürger |
| Strafverfolgungszugriff US-Behörde ohne Richter (NSL, Metadaten) | 🔴 Kein Richter, kein Verdacht, Schweigegebot |
| Geheimdienstlicher Zugriff (FISA § 702) | 🔴 Keine Einzelfallprüfung, kein EU-Rechtsschutz, Five-Eyes-Weitergabe |
| Five-Eyes-Intelligence-Sharing auf Basis US-erfasster Daten | 🔴 Kein transparentes Rechtsregime für Betroffene |

Für Gesundheitsdaten nach § 393 SGB V gilt: Nur Stufe 1 (EU-rechtlicher Strafverfolgungszugriff) ist akzeptabel. Alle anderen Szenarien sind mit dem DSGVO-Schutzniveau für besondere Datenkategorien (Art. 9) unvereinbar.

---
