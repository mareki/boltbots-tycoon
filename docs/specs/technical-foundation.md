# Technische Grundlage und Releasepolitik

> Artifact ID: `BOLTBOTS-TECH-001` · Revision: 1 · Status: candidate, Human approval pending
> Owner: /root · Foundation/Verträge: [Factory](factory-module.md)

## Architektur und Delta

Roblox-Client und Roblox-Server mit Luau, Rojo als Quell-/Place-Brücke, Roblox DataStore für den minimalen dauerhaften Fabrikstand. Ein logisches Factory-Modul mit reinen Regeln, Anwendungsfallfunktionen und kleinen Roblox-Adaptern. Ein versionierter Katalog; Client darf ihn anzeigen, Server bleibt entscheidend. Kein externer Dienst, keine AWS-Ressource, kein eigenes Login und kein neues Domainmodul für Speichern.

Harness `1.5.3`, Manifest SHA256 `e424f12705d41a7df56b8a8563077ce0ad1a5d17570bcfdf4e7a3f93a33a8702`, Payloadbaum `a9a1e42c5aa369d9d7f866544c62a9c0a1623ad7a8291b3daf8152a847443be8`. Organisationsprofil: keines ausgewählt. Das gebündelte `AH-PROFILE-AWS-SERVERLESS-MVP-001/0.2.1` (SHA256 `72fd666556791156b5711b12f8a8ae3dfb381370c43c78ef94573028905a9288`) wird **nicht ausgewählt**: Zielplattform ist Roblox.

| Regelbereich | Klasse | Produktkonkretisierung / Eigentümer |
|---|---|---|
| Domain/Modularität, nachvollziehbare Verträge | conforms | ein CTX-FACTORY/MOD-FACTORY, keine fachlichen Grenzen aus UI-Seiten |
| Sicherheit/Validierung/Privatsphäre | conforms | serverseitiger Owner, Schema-/Preis-/Raten-/Duplikatprüfung; keine Clientautorität |
| Reliability/Migration/Recovery | conforms | Savefehler sichtbar, kein Default nach Ladefehler, Versions-/Migrationsfixture, isolierte Testdaten |
| Testbarkeit/Build/Beobachtbarkeit | conforms | reine Regeltests plus reale Studio-/privaten Testexperience-Nachweise; kein Testdouble als Stagingbeweis |
| Bedienbarkeit/Design | strengthens | visuelle Referenzszene und tatsächlicher Agent-Spieltest im ersten Meilenstein; Design als separater nicht lieferbarer Nachweis |
| Portables Entwickler-Setup | strengthens | Codex-geführtes Onboarding nach Checkout, vorhandene Tools vor Installation prüfen |
| Kosten/Abhängigkeiten | conforms | keine externen Idle-Dienste; nur benötigte gepinnte Werkzeuge, keine Toolbox-Assets ohne Rechte-/Skriptprüfung |
| CDK-/AWS-Deployment in generischem Deliveryablauf | exception | ADR-01 unten, Humanentscheidung im Initialisierungspaket erforderlich |
| Produktversion/Promotion | conforms | Policy unten; Harness-Version niemals als Spielversion verwenden |
| Privileged Product Access | not applicable | Vision: kein Adminprodukt; Plattformentwicklerberechtigung separat schützen |

### ADR-01 — Roblox-Lieferweg statt AWS/CDK

**Vorschlag:** Git/Rojo-Build erzeugt ein unveränderliches Place-Artefakt. Dieses wird nach konkreter Autorisierung in eine getrennte private Roblox-Testexperience übertragen; dort echte Spieler-/Speicher-/Mehrspielertests. Erfolgreiche technische Abnahme plus späteres Human-Promotion-Gate erlauben die benannte Zielumgebung. `staging` bleibt Integrationszweig, `main` erfolgreiche veröffentlichte Linie; Arbeitszweige `codex/...` sind lokale Vorbereitung, Slicezweige gemäß installiertem Deliveryverfahren.

**Grund:** Roblox ist die Laufzeit und besitzt Identität/Rendering/Server/Datenspeicher. CDK würde für diese Funktionen keine passende Liefergrenze herstellen. **Alternative:** unnötiges externes AWS-Backend; zusätzliche Kosten, Konten, Daten-/Ausfallgrenzen ohne aktuelle Anforderung. **Kosten:** keine neue Cloud-Ressource eingeplant; Roblox-/Store-/Toolkosten vor realer extern belastender Aktion aktuell prüfen. **Migration:** späteres Backend nur mit nachgewiesenem Bedarf und neuer Entscheidung. **Authority:** genaue Zustimmung zu ADR-01 im zweiten Human-Gate. Diese Ausnahme ist ein Vorschlag, keine Änderung des Core.

## Daten, Sicherheit und Betrieb

Gespeichert werden Roblox-UserId als technischer Bezug und benötigte Spielstände; keine Namen/E-Mail/Passwörter aus Accounts oder Chatverläufe. Logs enthalten technische Ereignisse, pseudonyme nötige Spielerbezüge und Fehlercodes, niemals Session-/Login-/Cookiegeheimnisse. Dev-Testprofile sind synthetisch; reale Nutzerdaten erst mit entsprechender Releaseentscheidung. Lösch-/Auskunftsweg und Aufbewahrungsfrist vor privater Beta anhand tatsächlicher Plattformanforderungen festlegen, keine unbelegte Rechtskonformität behaupten.

Aufrufe prüfen serverseitig Identität, Typ/Größe/Endlichkeit, aktive eigene Sitzung, Katalog-/Levelversion, Rate und fachliche Voraussetzung. Unbekannte Remotes, fremde Plot-/Machine-IDs, negative/NaN/unendliche Werte und Doppelaufträge ablehnen. Produktionsabschluss ist ausschließlich intern. Begrenzte Effekte/Verbindungen aufräumen. Keine frei geladenen Skripte oder unkontrollierte Toolbox-Abhängigkeiten.

DataStore-Aufrufe können fehlschlagen. Studio-Zugriff ist standardmäßig aus; zum Testen eine getrennte veröffentlichte Testexperience verwenden, damit keine produktiven Profile überschrieben werden. UpdateAsync eignet sich für konkurrierende serverseitige Änderungen, ersetzt aber keinen getesteten Sitzungs-/Recoveryentwurf. [Roblox Data Stores](https://create.roblox.com/docs/cloud-services/data-stores), [Speichern von Spielerdaten](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data).

ANL-01: `session_start`, `tutorial_step`, `machine_purchase`, `robot_unlocked`, `session_end`, dazu intern erster sichtbarer Output/Savefehler für Debugging. Definierte Zeitbasis und Build-/Environmentkennung; erzwungener Disconnect kann session_end fehlen lassen. Entwicklungslogs sind keine Retentionmessung. Keine externe Analyticsplattform für M1.

**Leistungsbudget:** erste feste Szenarien mit 1, 2 und 4 Clients, benannter Gerätekonfiguration und Laufzeit. Framezeitverteilung, Speicher, aktive Outputs und Serverloops erfassen. Zielwerte erst nach realer Basis messen und vor Beta explizit festlegen; Emulator beweist kein schwaches reales Telefon. Bei Engpass zuerst Instanzzahl/Effekte begrenzen, kein neues Backend.

**Toolabhängigkeiten:** Ursprung pinnt Rojo 7.7.1; M1 prüft Verfügbarkeit/Kompatibilität, hält jede Abweichung fest. Keine Behauptung einer bereits installierten CLI. Studio unterliegt Plattformupdates; verwendete Version bei jedem relevanten Nachweis notieren. Blender nur nach nachgewiesener Agent-Bedienung. Optionen: Python-Skripte/CLI oder tatsächlich verfügbare UI-Steuerung; bislang kein ausgeführter Blender-Test.

## Product Release Policy r1

- Releaseeinheit: ein BoltBots-Roblox-Erlebnis einschließlich Server-/Clientcode, Katalog und gebundener Assets. Kein gesonderter Dienst.
- Schema: SemVer `MAJOR.MINOR.PATCH`, erste echte Kandidatenlinie `0.1.0`; interne Testkandidaten `0.1.0-rc.1` usw. Sourcepaket v0.2 ist keine veröffentlichte Spielversion.
- Zielgruppe der Kompatibilität: Spielstände, Client/Server-Nachrichten, Katalog-/Assetidentitäten. Vor1.0: kompatible neue Fähigkeiten MINOR, Korrekturen PATCH; inkompatible Speicher-/Vertragsänderung braucht sichtbare Migrationsentscheidung und mindestens MINOR. Ab1.0 inkompatibel MAJOR. Profil-schemaVersion ist separat.
- Ein Source-of-truth-Versionswert wird in M1 in Produktkonfiguration angelegt; jetzt keine fiktive Releaseversion aktivieren. Derselbe Wert bindet Client/Server/Artefakt. Aktuell keine Produktversion veröffentlicht.
- Kandidat reserviert die Zielversion; erst erfolgreiche ausdrücklich genehmigte Promotion veröffentlicht sie. Unveränderliches Git-Tag `product/vMAJOR.MINOR.PATCH` an exaktem erfolgreichen Commit. Kein Tag vor Promotion und keine Tagverschiebung.
- Releasebeleg bindet Version/Commit, Buildhash, Rojo-/Studio-Version, Katalog/Assets, Foundation/Specs/Review, tatsächliche Experience-/Place-/Place-Versionen, Prüfungen, Freigabe und Recovery. `current-serving` ergibt sich aus real bestätigtem Plattformstand, nicht allein Branchname.
- Migration vor Upload mit alten/neuen Fixtures und Rückweg prüfen. Rollback nur auf kompatible frühere Place-/Datenversion; Code-Rollback heilt keine inkompatible Datenmigration. Datenfehler zunächst Schreibstopp und betroffene Testprofile isolieren.
- Keine Umgebung, Telemetrie oder Budgetfreigabe erfinden. Vollständiges Release-/Store-/Rechtepaket und Plattformanforderungen vor öffentlicher Veröffentlichung erneut aktuell prüfen.

## Prüfstrategie und Nachweisgrenzen

Reine Luau-Regeln: Nullbetrag, exakter Grenzpreis, Überlauf, ungültige Rate, Duplikate, stale Level/Katalog. Adapterfälle: fehlendes Profil vs Ladefehler, Migration, konkurrierende Session, Savefehler/Wiederholung, Shutdown. Echte Clients: Einstieg/Upgrade/Abbruch/Sammlung/Isolation/Save-Rejoin. Visuell: tatsächliche Kamera, Touchlayout, Feedback und Fehlerzustände im Vergleich zum freigegebenen Entwurf.

CI startet mit reproduzierbarem Build und notwendigen statischen/Regelchecks; Studio-/Gerätetests dokumentieren, wo Headless-Automation nicht belegt ist. Kein erfundener Studio-CLI-Befehl. Publisher/Accountinteraktion und private Testumgebung nur innerhalb genauer Autorisierung. Aktuell wurde kein Spieltest ausgeführt.
