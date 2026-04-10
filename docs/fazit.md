# Fazit

> **"Die Frage ist nicht mehr ob US-Behörden auf Daten in Europa zugreifen können. Die Frage ist, unter welchen Umständen sie es tun — und ob wir das als akzeptables Restrisiko bezeichnen wollen, wenn es um Diagnosen, Medikation und Krankenversicherungsdaten von 74 Millionen GKV-Versicherten geht."**

Zwölf Kernaussagen:

1. **Serverstandort schützt nicht.** Entscheidend ist, wer die Kontrolle über die Daten hat — Unternehmensstruktur, nicht Geographie.

2. **§ 393 SGB V und DSGVO Art. 48 ergänzen sich — die eine regelt IT-Sicherheit, die andere Jurisdiktion.** § 393 entbindet nicht von der DSGVO. Ein C5-konformer Anbieter unter US-Jurisdiktion erfüllt § 393, aber nicht Art. 48. Wenn US-Behörden zugreifen, ist das ein meldepflichtiger Datenschutzvorfall — unabhängig vom C5-Testat. Die Lücke liegt in der Beschaffungspraxis: C5 ist Pflicht, eine Jurisdiktionsprüfung nicht.

3. **US-Hyperscaler sind de facto akzeptiert — trotz DSGVO-Widerspruch. Und der Aufsichts-Flickenteppich macht es noch verwirrender.** Das ist die ehrlichste Zusammenfassung des Status quo. Die KVNO betreibt ihre KI-Plattform auf Azure (TED 98706-2026). Kubus IT hostet GKV-Daten über Arvato bei Google Cloud. Dutzende Kliniken laufen auf Oracle OCI. Die vollständige Positionierung aller 16 Landesbehörden + BfDI + BAS ist in §16.11 dokumentiert — das Bild reicht von 🟢 (Hessen, Niedersachsen) bis 🔴 (Hamburg, Schleswig-Holstein). Wer bei der "richtigen" Aufsichtsbehörde sitzt, bekommt Azure toleriert. Das Enforcement-Gap ist das eigentliche strukturelle Problem.

4. **Das Operator-Modell ist der pragmatische Mittelweg** für Organisationen, die heute in Microsoft- oder Google-Ökosysteme integriert sind: Delos Cloud (SAP × Azure) für Verwaltung und Kliniken, S3NS (Thales × Google) als europäisches Referenzmodell mit SecNumCloud. Preis der Souveränität: +15% auf Listenpreise.

5. **Der vollständige EU-Plattformstack existiert und ist produktionsreif.** US-Hyperscaler ersetzen bedeutet E-Mail (Open-Xchange), Office (Euro-Office/Nextcloud), SharePoint (Nextcloud/OpenCloud), Teams (Jitsi/OpenTalk), Active Directory (Keycloak) und KI (vLLM/Mistral) zu migrieren. Schleswig-Holstein macht das für 30.000 Mitarbeitende mit €15 Millionen jährlichen Einsparungen.

6. **Europäischer Behördenzugriff ist strukturell anders als US-Zugriff** — nicht weil Europa besser ist, sondern weil die e-Evidence-VO an Verhältnismäßigkeit, unabhängige Gerichte und Grundrechtsschutz für alle Betroffenen gebunden ist. FISA § 702 und NSL sind das nicht.

7. **Ein EU-US Executive Agreement ist juristisch möglich** — der CLOUD Act hat den Mechanismus eingebaut, das UK hat ihn 2019 genutzt. Aber: seit sieben Jahren keine EU-Einigung, weil die USA FISA § 702 und NSL nicht einschränken wollen.

8. **151 Millionen Euro** investiert Big Tech jährlich in EU-Lobbyarbeit — 19-mal mehr als die Automobilindustrie. Dieser strukturelle Vorteil prägt die Regulierungslandschaft direkt.

9. **Clientseitige Verschlüsselung (HYOK) schützt bei statischen Datenspeichern** — nicht bei KI, E-Mail, SharePoint oder SaaS. Die Grenze liegt bei "Data in Use".

10. **Kein europäischer Anbieter ist heute ein echter Hyperscaler** — aber die Frage ist nicht "kann STACKIT wie AWS skalieren?", sondern "braucht eine GKV das überhaupt?" STACKIT investiert 11 Milliarden Euro und wird 2027 ausreichend sein.

11. **Vier Souveränitätsstufen, nicht zwei:** Full Isolation (plusserver, Cloud Temple, EU-Open-Source-Stack) → Operator-Modell (Delos, S3NS) → Hyperscaler Sovereign (AWS ESC, Azure EU Boundary) → Sovereignty Washing (AWS Frankfurt, Azure DE). Für KRITIS-Gesundheitsdaten: mindestens Operator-Modell. Der Maßstab für jede Stufe ist nicht "Verbündeter oder nicht" — sondern "rechtsstaatlich gebunden oder nicht."

12. **Patienten können klagen — und die Haftung erreicht die Leitung auf drei Wegen.** Art. 82 DSGVO gibt Betroffenen einen direkten Schadensersatzanspruch gegen die Organisation. Die Organisation kann ihren GF über die Organhaftung (§ 43 GmbHG / § 93 AktG) in Regress nehmen, wenn die Entscheidung nicht auf einer dokumentierten Risikoabwägung beruhte. Und NIS2 begründet eine eigenständige persönliche GF-Haftung für fehlende Lieferketten-Risikobewertung — ein CLOUD-Act-exponierter Anbieter ist ein Lieferkettenrisiko. Wer kein TIA erstellt hat, hat auf keinem der drei Wege eine Entlastung.

---
