# B3-C1 — tatsächlicher Speicher-/Recovery-Nachweis

Gebundener Kandidat: `candidate-manifest.json`; Ausgang `dd6aa9a6fece90f1d59b1bc67654cdea9daef65c`. Review/Autorität und Grenzen im [B3-Run](../../../work/runs/boltbots-m1-b3-001.md). Keine Gesamt-M1-Abnahme.

## Ziel und Methoden

Human hat die neue ausschließlich private eigene Experience **BoltBots B3 Test 20261025**, Universe10772906084/Place112662761038118, Studio-API und isolierten Store **BoltBots_B3_20261025** ausdrücklich freigegeben. `target-created.png`, `target-private.png`, `studio-api-enabled.png` zeigen tatsächliche native Studio-UI; Eigentumsbereich bei Erstellung Me/My Experiences, kein Konto-/Credentialbild. CreatorId war im lokalen Editdokument0 und ist kein Eigentumsbeweis. Bestehende Experience nicht verändert. Initialer Cloudstand war approved B2-C2; B3 wurde per Rojo in demselben privaten Ziel gespielt. Finaler geprüfter B3-Cloudsave wird separat im Run bestätigt.

`studio-observations.log` enthält ausgewählte unveränderte Originalzeilen mit Originalzeilennummern aus `0.744.0.7441077_20261024T193411Z_Studio_4f78a_last.log`, keine vollständige Plattform-/Kontologdatei. Lange Commandbar-Ausdrücke können im Originallog abgeschnitten sein. Die ausführliche synthetische Storeprobe ist deshalb vollständig als `store-fixture-probe.luau` gebunden. Screenshotzuschnitt entfernt Studio-Kontobereiche; Inhalt unverändert, auf1512px Breite skaliert. Keine Konzeptbilder oder fingierte Videos.

## Normales Spiel und tatsächlicher Store

- 09:56:12: fehlender eigener Testeintrag bestätigt, neuer Stand0. Normale Produktion, echter L2-Klick und Orbitwahl; keine Cash-/Profildatenmanipulation.
- 10:02:11: Stop/Leave bestätigt Release/Revision12/Cash1050/44Abschlüsse/L2/Orbit. 10:02:59: echter erneuter Playbeitritt lädt exakt1050/44/L2/Orbit. `before-rejoin.png` und `after-rejoin.png` zeigen normale Spielzeit davor/danach mit925 bzw1150Cash; sie sind **keine exakt gleichzeitigen Snapshotbilder** der Logwerte. Produktion danach ist neuer Fortschritt.
- 10:06:15: weiterer bestätigter Release Revision19/Cash1825/75/L2/Orbit. Studio-API bewusst ausgeschaltet und gespeichert; tatsächliche UpdateAsync-Ablehnung `StudioAccessToApisNotAllowed` beim nächsten Join. Normales Retry weiterhin abgewiesen, kein Default:10:11:46 `ready=false`, `cash=nil`,0aktivePlots. Desktop `load-failed-api.png`, Portrait `load-failed-portrait-level01.png`. API danach wieder eingeschaltet. Join10:20:55 lädt unverändert Revision19/Cash1825/75/L2/Orbit.

## Savefehler, sicherer Ablauf und Retry

Bewusste **Studio-only Fault Injection**, kein behaupteter spontaner Netzwerkausfall: serverseitiges Attribut `B3RejectStoreWrites` lässt den echten UpdateAsync-Transport einen nicht serialisierbaren Wert liefern; Roblox lehnt tatsächlich mit `CantStoreValue` ab. Live-Server ignoriert den Schalter; kein Clientremote aktiviert ihn.

- Letzter bestätigter Save10:21:58: Revision21/Cash2050/84. Fehler10:22:28: aktueller unbestätigter Stand2175/89 bleibt pausiert.10:23:14 und10:23:22 identische Werte und Pausenzeit; Selectabsicht wird `inactive` abgewiesen. `save-failed-landscape-level01.png` ist **Querformat**, nicht Portrait.
- Der Operatorretry verzögerte sich durch Kontext-/Creditunterbrechung über90s. Normaler Klick10:28:44 ergibt korrekt `lease_lost`; `lease-expired-landscape.png` verlangt erneuten Beitritt und behauptet keinen Save. Keine künstliche Leaseverlängerung. Neuer Join10:33:07 lädt genau den letzten bestätigten Stand2050/84/Revision21. Die125unbestätigtenCash wurden nicht als dauerhaft gesichert ausgegeben.
- Zweite kurze FaultInjection10:33:37, echte Ablehnung10:33:38; automatisch nach beobachteter Pause+2s deaktiviert10:33:40. Snapshot10:33:46:2150/88/Revision21/save_failed. Normaler Retryklick10:33:58 bestätigt10:33:59 exakt2150/88 alsRevision22.10:34:09 Fehlerkartefalse, Pausenzeitnil, Fokusnil, normaleProduktion2200/90;10:34:17 weitere2250/92. `retry-resumed-landscape-level01.png` zeigt fortgesetztesSpiel. FinalStop10:35:09 bestätigtReleaseRevision25/Cash2450/100/L2/Orbit.

## Reale synthetische Fixture, getrennt vom Spielerpfad

`store-fixture-probe.luau` nutzt ausschließlich `fixture_schema1_session_b3_20261025` im autorisierten Store, nie das Spielerprofil. Erster Diagnoseaufruf scheiterte vor jedem Write am falschen Rojo-Modulpfad; im gebundenen Probe korrigiert. Tatsächlich ausgeführter erfolgreicher Lauf10:32:34–37:

Schema1/Revision4/Cash75/L2/Orbit wird zuSchema2 migriert; zweiter Handle wird `session_locked` abgewiesen. Nach echtem Roblox-Commit wird einmal bewusst die Transportbestätigung verworfen. Retry übernimmt denselben Write genau einmal (Revision5/Cash100); Release und Rejoin über zweiten Handle erhalten100/Orbit; EndstandSchema2/Revision7/sessionnil. Originalmarker `BOLTBOTS_B3_REAL_FIXTURE migrated session_locked ambiguous_write_once 2 7 100 orbit released`. Vollständige Probe ist gebunden; kein zweiter physischer Client/Mehrspielergesamttest behauptet.

## Layout, Qualität und Grenzen

Portrait tatsächlich413×756, Querformat801×355 logische GUIpixel; iPhoneXR-Emulation, keine physische Mobilhardware. Portraittextprüfung10:16:55 ohne unter14px/Abschneiden, zunächstAutomatic; anschließend10:17:40 Level01 tatsächlich gesetzt und **danach** das gebundene Portraitbild erstellt. Querformat10:33:46 und vollständiger Textcheck10:35:06 mitLevel01, keinezuKlein-/TextFitsBefunde. Ladefehlerkarte erklärt die fehlende Bestätigung ohne0Cash-Fiktion; Savefehler zeigt Pause und sinnvollen Retry, abgelaufeneSitzung klaren Wiedereintritt. Während bestätigter Autosaves zeigt die bestehende Kopfzeile den Status. B1/B2-Kunst, Geometrie und Regeln unverändert wiederverwendet.

Creatorurteil getrennt: **menschlich ansprechend: ja für die B3-Zustände** — ruhige Navy-/Cyanflächen, ausreichend große Schriften und klare einzige Aktion passen zur bestehenden Werkstatt. **Lust weiterzuspielen: ja, soweit Recovery betroffen** — erarbeitete L2-/Orbitfortschritte kehren erkennbar zurück, Fehler erklären den sicheren nächsten Schritt ohne fiktiven Erfolg. Kein neuer Gesamt-Premiumpass: der Humanbefund zum unplausiblen rechten Versandabschluss bleibt ausdrücklich vor M1-Endabnahme offen.

Lease90s; Autosave30s/spätestens5s vorAblauf; Retry≥3s; Leave/Shutdown25s. Normales unbestätigtes Fenster bis30s, beiAusfall Pause; kein Nullverlustversprechen nachabgelaufenerSitzung/Crash. PureTests prüfen wiederholteCallbacks, eingefrorenenSnapshot, Korruption/Neuerschema, CAS/Claimverlust und unklareSave-/Releasebestätigung; sie ersetzen den obigen realenAPIweg nicht. Leave während ausstehendemLoad/Save ist quellgeprüfte Guardlogik, kein künstlich behaupteter eigener zeitlich erzwungener Runtimebeleg. B4integrierte2–4Clients, B5vollständigeSpiel-/Human-Endqualität, physischeMobil-/Gamepad- undLasttests bleiben offen.
