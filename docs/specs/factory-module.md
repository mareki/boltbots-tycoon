# Factory — Modul, Verträge und Spielerabläufe

> Artifact ID: `BOLTBOTS-FACTORY-TARGET-001` · Revision: 1 · Status: candidate target
> Context: CTX-FACTORY · Module: MOD-FACTORY · Owner: /root

Semantischer Eigentümer bleibt die [Foundation r1](../domains/domain-foundation.md), wirksam durch [Humanreview](../reviews/20261024-1.5.3-boltbots-domain-foundation-review.md). SHA256 `2cd9c514b3f1aefc1f7955e5389e75f9912a6f1edd5af1ca84ddbe70359b540f`. Keine neuen Kontexte. AG-FACTORY hält den dauerhaften Fortschritt, AG-PLOTS die temporäre exklusive Sitzungszuordnung. Kein kontextübergreifender Vertrag notwendig.

## Module Entry Map

| Verantwortung | Eigentümer / vorgesehene Implementierung |
|---|---|
| Bedeutung, Invarianten, Lebenszyklen | Foundation C1–C3; nicht hier dupliziert |
| Anwendungsfälle, Transaktionen, Verträge | dieses Dokument; später ein Factory-Modul in ServerScriptService |
| Reine Regeln | später Luau-Funktionen für Preis, Ertrag, Freischaltbedingungen und Zustandsübergänge |
| Daten-/Plattformadapter | später DataStore und Roblox-Player-/Remote-Adapter; kein generisches Adapterframework |
| Darstellung | später Client-HUD/3D-Effekte; liest autorisierte Views und sendet Absichten |
| Konfiguration | später versionierter Shared-Katalog; Server entscheidet, Clientkopie nur Darstellung |
| Tests/Betrieb | [Technik](technical-foundation.md), [M1](../planning/milestones.md), [Setup](../setup.md) |

Die späteren Codepfade sind Vorschläge; gegenwärtig existiert ausführbarer Produktcode nur als ungestartete Referenz im Import.

## Öffentliche Verträge v1

Alle Spielerbefehle verwenden Roblox' authentifizierten Player als Absender. Payload enthält niemals einen vertrauenswürdigen Owner, Cashbetrag oder autoritativen Preis. Unbekannte Felder/Werte ablehnen; endliche Zahlen, Längen, bekannte IDs, Eigentum und Zustand prüfen. Rate-Limits pro Spieler und begrenzte Request-Historie. Einheitliche Antwort: `requestId`, `ok`, `stateVersion`, eigener neuer View oder stabiler Fehlercode. Fehler verändern keinen Fortschritt.

| ID | Ein-/Ausgabe und Wirkung | Guards / Fehler |
|---|---|---|
| Q-FACTORY | Eigener Snapshot: Cash, Maschinen/Level, Produktion, Freischaltungen, Auswahl, Ziel, Save-Status, stateVersion | Nur eigener Fortschritt; loading/failed nicht als Startprofil ausgeben |
| Q-PUBLIC | Öffentliche sichtbare Fabrik: nötige Besitzerreferenz, Maschinen/Optik/Ausstellung | Keine Speicher-/Sessiontoken oder privaten Profildaten; reine Lesesicht |
| C-UPGRADE | requestId, machineId, expectedLevel, catalogVersion → atomar Cash abziehen und Level erhöhen | eigener aktiver bestätigter Zustand; aktueller Level/Katalog; funds/level_limit/stale_state/saving_unavailable/forbidden |
| C-PLACE | requestId, machineTypeId, socketId, catalogVersion → eigene zulässige Maschine kaufen/platzieren | freier eigener Socket, Voraussetzungen und Cash; occupied/invalid_socket/funds |
| C-SELECT | requestId, designId → Produktionswahl ab nächstem Durchlauf | freigeschaltet oder Scout-Startausnahme; locked/unknown_design |
| C-STYLE | requestId, erlaubte colorId/detailId → Gestaltung | eigene Fabrik, bekannte freie Optionen; invalid_style/forbidden |
| C-DISPLAY | requestId, freigeschaltete designId oder null → höchstens eine Ausstellung | locked/forbidden; keine Designübertragung |
| E-COMPLETE | rein serverinterner Produktionsabschluss mit cycleId und gestartetem Design → Ertrag einmal, gegebenenfalls Designfreischaltung | aktiver eigener Fortschritt und noch nicht verarbeiteter Abschluss; Client kann dieses Ereignis nicht auslösen |
| E-UNLOCK | interner Fakt designId, erfüllter Katalogmeilenstein → neue Sammlungsberechtigung | Scout nach erster fertiger Einheit; Orbit nach Starter-L2; übrige Voraussetzungen H-BAL vor M2 konkretisieren |
| C-JOIN / C-LEAVE | rein interne Sitzungsaufnahme/-beendigung, Load/Save und Plotzuteilung | fehlender Platz, unklarer Lade-/Schreiberstatus: keine Produktion; beim Leave erst Mutationen stoppen |

**Kaufabsicht:** Vor dem Kauf zeigt die Oberfläche den Server-View mit Preis/Level. Der Server prüft bei Ausführung erneut. Bei abweichendem Level/Katalog lehnt er ab und liefert aktualisierte Daten; der Spieler bestätigt neu. Derselbe requestId wirkt höchstens einmal, wiederholte Zustellung liefert das bekannte Ergebnis. Zwei getrennte Absichten sind zwei Käufe, jeweils nur bei aktuell passenden Guards. Keine unbeschränkte dauerhafte Ereignisliste: Entscheidung über kompakte Deduplikation/Save-Grenze im M1-Code mit Wiederverbindungstests.

**Persistenzvorschlag:** Ein versioniertes Profil je UserId mit Cash, Maschinen, Designfreischaltungen, Auswahl, Stil und Ausstellung; keine Plotposition oder gerenderten Outputs speichern. UpdateAsync schützt atomare Profiländerung und einen exklusiven Server-Schreibanspruch mit begrenzter Gültigkeit. Netzwerkfehler/ungeklärter Anspruch sperren neue Fortschrittsänderungen; Wiederaufnahme nur nach bestätigtem Anspruch und Stand. Keine neue Defaultdatei nach Ladefehler. Bereits bestätigtes Profil nie durch ältere Revision überschreiben. Absicht/Bestätigung/Speicherstatus müssen im Code getrennt sein; erst reales Save/Rejoin beweist dauerhafte Wirkung. Adaptertests prüfen Konflikt, Wiederholung, Timeout und verlorenen Anspruch. Konkrete Timeout-/Checkpointwerte nach Messung, keine unbewiesene Dauerhaftigkeitsgarantie durch jeden lokalen Klick.

## Kernreise mit Fehlern und Wiederaufnahme

Alle folgenden Schritte gehören CTX-FACTORY. Bildschirme sind Aufgabenansichten, keine neuen Domainobjekte. Der Produktionsroboter ist ein Effekt; die Sammlungskarte steht für ein gespeichertes Designrecht.

| Flow / Schritt | Auslöser, Kontrolle, Ergebnis und nächster Schritt | Verträge / Nachweis |
|---|---|---|
| F-START / S-LOAD | Spielbeitritt → „Fabrik wird geladen“; auf eigene bestätigte Sitzung warten → S-WORLD. Laden fehlgeschlagen → Fehler mit erneut versuchen; kein Reset | C-JOIN, Q-FACTORY; SYS-01/02, FTUE-01 |
| F-FIRST / S-WORLD | Ziel „Sieh deinem ersten Scout zu“; Teile/Assembler/Verpackung sichtbar. Abschluss → Cashfeedback, Scout-Sammlungseintrag und neues Ziel | E-COMPLETE/E-UNLOCK, Q-FACTORY; LOOP-01, FTUE-02, ANL-01 |
| F-UPGRADE / S-UPGRADE | Owner wählt eigene Maschine/„Ausbauen“ → Level, Preis, Wirkung sehen. Abbrechen → Welt unverändert. „Für … Cash verbessern“ → C-UPGRADE, bis Antwort keine zweite Absicht | FTUE-03, ECO-01/02, UI-04 |
| F-UPGRADE / S-RESULT | Erfolg → neuer Level/Cash/Tempo, erfüllter Orbit-Meilenstein, sichtbare Rückmeldung → Welt/Sammlung. Zu wenig Cash → Fehlbetrag; stale → neue Daten/erneut bestätigen. Fremde Maschine → keine Aktion | C-UPGRADE, E-UNLOCK, Q-FACTORY; kein clientseitiges Buchen |
| F-COLLECT / S-COLLECTION | Sammlung zeigt fünf Designkarten, freigeschaltet/gesperrt mit verständlicher Voraussetzung. Freies Design „Produzieren“ → neue Auswahl ab nächstem Zyklus. Gesperrt → Grund und Ziel, keine Kaufattrappe | C-SELECT, Q-FACTORY; LOOP-03/05 |
| F-EXPRESS / S-STYLE | Freie Farbe/Detail wählen, eigenes freies Design ausstellen → Feedback und bestätigter View. Fehler → vorheriger bestätigter Zustand | C-STYLE/C-DISPLAY; LOOP-04; im Entwurf annotiert, M2 detaillieren |
| F-VIEW / S-WORLD | fremden Plot ansehen → öffentliche Optik; keine Bearbeitungskontrollen. Manipulierte Schreibabsicht serverseitig abweisen | Q-PUBLIC; SYS-01, QA-02 |
| F-RECOVER / S-ERROR | Save nicht bestätigt → „Speichern nicht bestätigt — Fortschritt pausiert“, Käufe/Produktion pausiert. Wiederholung nur nach serverseitig sicherem Zustand. Bei Leave/Rejoin letzten bestätigten Stand laden | C-JOIN/C-LEAVE, Q-FACTORY; SYS-02/03, QA-03 |

Desktop nutzt Maus/Tastatur, Touch große Buttons; gleiche Bedeutung, schmale Ansichten erhalten Cash/Ziel/primäre Aktion vor sekundären Details. Fokus bleibt nach Dialogschließen am Auslöser. Kein fortlaufender Echtgeld-/Shop-/XP-Weg. Kein Accountlogin im Mockup: Roblox übernimmt die Anmeldung außerhalb des Spiels.

## Trace zur Lieferung

| Anforderungen | Flow / Vertrag | Feature → Slice → Work Package | geplante Evidenz |
|---|---|---|---|
| BOOT-01–04 | Entwicklung, kein Spielvertrag | F-CORE → SL-01 → WP-01A | sauberer Build, Toolreport, Studio-Start |
| SYS-01/04, FTUE, LOOP-01, ECO, UI-01–04 | F-START/F-FIRST/F-UPGRADE; Q-FACTORY/C-UPGRADE/E-COMPLETE | F-CORE → SL-01 → WP-01B | echte Spielaufnahme, Grenz-/Exploit-/Isolationsfälle |
| SYS-02/03, QA-03 | F-RECOVER; Join/Leave/Profiladapter | F-CORE → SL-01 → WP-01B | Testumgebung Save/Rejoin/Fehler/Migration |
| LOOP-02–05 | F-COLLECT/F-EXPRESS; C-PLACE/SELECT/STYLE/DISPLAY | F-COLLECT → SL-02 → WP-02 | fünf Designs, gespeicherte Gestaltung, Endziel |
| PERF, ANL-01, QA, REL | vorgenannte Flows in realen Testbedingungen | F-QUALITY → SL-03 → WP-03 | reale Geräte-/Mehrspieler-/Rechte-/Betanachweise |

Alle Paketnamen verweisen auf den [Plan](../planning/milestones.md); bisher geplante Abnahmen. Nicht implementierte Verträge werden durch Initialisierungsfreigabe nur `approved target`, nie automatisch aktiv.
