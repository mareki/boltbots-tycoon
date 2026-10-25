# Lokales Setup — geführt durch Codex

> Artifact ID: `BOLTBOTS-SETUP-001`
> Revision: 8 · Führender Prüfstatus und Grenzen: [Handover](handover.md)

Nach einem Checkout übernimmt Codex Werkzeugprüfung, Installation, Build und die verfügbare Studio-Bedienung. Der Human liefert Ideen, prüft Qualität und erledigt bei Bedarf persönliche Anmeldung oder Systembestätigung. Passwörter, Roblox-Cookies und API-Schlüssel gehören nicht in Chat oder Repository.

## Neuer Mac: bis zum lokalen Build

1. Repository in Codex öffnen und README/Handover lesen lassen. Codex prüft macOS, Python 3 und Git. Falls eine Voraussetzung fehlt, richtet Codex sie über die jeweilige offizielle Quelle ein; Konto-/Administratorbestätigung bleibt gegebenenfalls beim Human. Das Skript unten setzt ein ausführbares Python 3 voraus. Homebrew, Node, Rokit, Aftman, Foreman und Blender sind für diesen Build keine Pflicht.
2. Roblox Studio unter `/Applications/RobloxStudio.app` oder `~/Applications/RobloxStudio.app` prüfen und tatsächlich starten. Wenn fehlend, über die [offizielle Studio-Einrichtung](https://create.roblox.com/docs/studio/setup) installieren. Persönliche Roblox-Anmeldung durch den Human, anschließend arbeitet Codex weiter.
3. Im Repository folgende Befehle ausführen lassen:

```bash
python3 scripts/dev.py setup
python3 scripts/dev.py plugin-install
bash scripts/doctor.sh
bash scripts/check.sh
bash scripts/build.sh
```

`setup` lädt ausschließlich die offiziellen, in `toolchain.json` gepinnten Release-Archive: Rojo 7.7.1 und Luau 0.744. SHA256 wird vor der Ausführung geprüft. Binaries, Downloadcache und lokaler Installationsbeleg liegen unter `.tools/` und werden nicht eingecheckt. Kein Administratorzugriff und keine globale PATH-Änderung für diese Werkzeuge nötig. Der Rojo-Build nutzt stets `.tools/bin/rojo` aus diesem Checkout.

Die Rojo-Auswahl richtet sich nach der ausführenden Python-Architektur. Ein unter Rosetta laufendes Intel-Python wählt das ausführbare x86_64-Rojo; natives ARM-Python die ARM-Ausgabe. Das Luau-macOS-Archiv liefert derzeit ARM-Binaries. Auf Mareks ARM-Mac wurden Intel-Rojo und ARM-Luau tatsächlich ausgeführt. **Ein Intel-Mac und ein zweiter Rechner sind noch nicht nachgewiesen**; bei nicht ausführbarem Binary stoppt das Setup mit konkretem Fehler. Windows/Linux sind hier noch kein verifizierter Setupweg.

`plugin-install` verwendet den [offiziellen CLI-Weg](https://rojo.space/docs/v7/getting-started/installation/), erzeugt `~/Documents/Roblox/Plugins/RojoManagedPlugin.rbxm` und prüft den eingebetteten Pluginhash. Dieser unterscheidet sich beobachtet vom separat veröffentlichten `Rojo.rbxm`-Asset; beide sind im Toolpin ausdrücklich getrennt. Ein bereits vorhandenes abweichendes Managed-Plugin wird nicht automatisch überschrieben. Studio nach der Installation neu starten. Die Startseiten-Verwaltung zeigte das lokale Plugin im beobachteten Ablauf nicht an; maßgeblich ist der Plugin-Nachweis im leeren Studio-Dokument, nicht diese Marketplace-Liste.

`doctor` unterscheidet Dateifund, tatsächliche Ausführung und fehlende Anforderungen. Ein gefundener Studio-/Pluginpfad beweist weder Anmeldung noch funktionierende Verbindung. `check` kompiliert alle aktiven Luau-Dateien, prüft reine Regelmodule auf Typfehler und führt die Basistests aus. Für die Standalone-CLI werden ausschließlich die Roblox-Importzeilen von GameConfig, ProfileSchema und ProfileStore in temporären Kopien auf Dateipfade adaptiert; Regel- und Adapterlogik bleiben unverändert. Keine Simulation behauptet einen Roblox-Spieltest oder vollständige Roblox-API-Typprüfung.

`build` erzeugt `build/BoltBots.rbxlx` und gibt den SHA256 aus. `build/` ist generiert und ignoriert; `src/` plus `default.project.json` sind die Quelle. Die aktive B5-Quelle umfasst neun Runtime-Dateien: Regeln/Konfiguration, Profilformat und Speicheradapter, Serveradapter, Werkstatt, Scout-/Orbit-Bauer und Clientansicht. `development-b5` ist ein Entwicklungslabel. Ein aus dem Checkout gebauter Place bleibt lokale Vorschau ohne Speichern. Nur das unten benannte private Testziel verwendet den echten Store. B4 hat die technische Mehrclientbasis geprüft; B5 jetzt auch den normalen Besuch einer belegten fremden Werkstatt. Die Human-M1-Endabnahme bleibt offen, siehe [Handover](handover.md).

## Studio starten und lokal verbinden — A3, tatsächlich geprüft

Codex hat den folgenden Ablauf auf diesem Mac tatsächlich ausgeführt:

1. In Studio File → Open from File / Cmd-O; `build/BoltBots.rbxlx` öffnen. Im nativen Pfaddialog funktionierte das gezielte Setzen des Pfadfelds zuverlässig. Vor Play ist die Ansicht leer, weil die Diagnosewelt erst serverseitig erzeugt wird.
2. Play über das Dreieck oben links starten. Client-/Server-Tabs erscheinen. Start abwarten; HUD, Fabrik und Spieler werden sichtbar. Diagnosebasis erzeugte Roboter und schrieb automatisch Cash gut: beobachtet 17/425, anschließend 20/500. Stop über das rote Quadrat.
3. Lokalen Rojo-Server starten:

```bash
python3 scripts/dev.py serve
```

Der Server bindet ausschließlich `127.0.0.1`. Im Rojo-Plugin `localhost`, Port `34872`, dann Connect verwenden. [Offizieller Build-/Live-Sync-Ablauf](https://rojo.space/docs/v7/getting-started/new-game/). Rojo benötigt für diesen lokalen Ablauf kein eigenes Konto. Studio zeigte tatsächlich „Connected to session BoltBotsTycoon at localhost:34872“ und Disconnect. Eine ausschließlich im Dateisystem ergänzte Kommentar-Markierung in GameConfig kam im echten Studio-Quelltext an; nach Entfernen der Markierung bestätigte Studio auch die Wiederherstellung. Source und Buildhash blieben anschließend gleich. Für künftiges Aufräumen empfiehlt sich: zuerst Disconnect im Plugin, danach Ctrl-C; andernfalls kann das Plugin den beendeten Server als WebSocketfehler anzeigen. Beobachtet wurde hier der Serverstopp zuerst. Server mit Ctrl-C beenden; der beobachtete Python-Wrapper endete dabei mit normalem Interrupt/Exit130. Ein bloß gestarteter Server reicht weiterhin nicht als Verbindungsbeleg.

A3-Nachweis: [Screens/Logs und Hashbindung](reviews/evidence/M1-A3/studio-verification.json). CreatorOutput meldete Serverboot, Clientboot und ersten Roboter. Keine passenden Produktskriptfehler im untersuchten Zeitfenster; Avatar-Asset-403 und Plattform-Telemetrie-Timeouts wurden separat beobachtet. Keine pauschale Fehlerfreiheit behauptet. Die native Bedienung und visuelle Prüfung gelten für diesen beobachteten Studio-Stand. Bei offenem Menü und fehlendem Screenshot half dessen exponierte Cancel-Aktion, ohne neue Automatisierung.

## Lokaler Start und Bedienung

Nach Build und File → Open startet Play die kleine Werkstatt serverseitig; die leere Editansicht ist erwartet. Scout wird montiert, fährt durch das offene Verpackungsportal und verlässt es als geschlossener Karton. Erst der serverseitige 9-Sekunden-Abschluss schreibt 25 Cash und beim ersten Mal das Scout-Designrecht gut. Die Sammlung ist kein Einzelroboterlager. Bei einem lokalen, unveröffentlichten Build (GameId0) gilt die sichtbare Kennzeichnung „Lokale Vorschau · ohne Speichern“ für die gesamte Sitzung.

„Ausbauen“ zeigt50Cash für AssemblerL2,9→6Sekunden ab dem nächsten Zyklus, unverändert25Cash pro Roboter sowie Orbit und ein sichtbares Maschinenmodul. Abbrechen/×/M/Escape bewirken keinen Kauf. Ein erfolgreicher serverseitiger Kauf zieht genau50Cash ab und gewährt L2 und das Orbit-Designrecht gemeinsam. Die Werte sind lokale Testbalance. Der laufende Zyklus behält seine Dauer und Familie.

„Sammlung“ zeigt getrennte Scout-/Orbit-Details und eine ausdrückliche Produktionswahl für den nächsten Zyklus. Orbit bleibt bis L2 gesperrt; Ansehen allein wählt oder gewährt nichts. Der vollständige Orbit läuft durch dieselbe passende Verpackung. Beide Karten sperren darunterliegende Aktionen. × oder M schließen; Escape öffnet Roblox' reserviertes Menü und schließt dabei die Sammlung. Im Erkunden wird anschließend normale Maus-/Tastaturbewegung wieder frei. „Erkunden“ gibt normale Kamera und Spielersteuerung frei; „Werkstatt“ stellt die eigene feste Ansicht wieder her. „Bewegung: ruhig“ unterdrückt dekoratives Winken/Neigen, der Produktionsweg bleibt sichtbar. In der festen Ansicht werden Nachbarslots lokal ausgeblendet und Touch-Steuerkreise verborgen; Erkunden stellt sie wieder her.

Sichtbare Menü- und Recoverytasten bleiben auch bei maximalem Hineinzoomen per Maus erreichbar. Zum Umschauen dient die normale Roblox-Kamerabedienung; ein verborgenes Tastenkürzel ist zum Öffnen der Sammlung nicht erforderlich.

Das rechte Band führt in die beschriftete Versandannahme. Das Rolltor öffnet vor der Ankunft des verschlossenen Kartons und schließt, bevor dieser wiederverwendet wird. Die Annahme gehört zur Darstellung der bestehenden Produktion; sie hat keinen eigenen Kaufpreis oder zusätzlichen Ertrag.

B1 und B2 wurden in Studio tatsächlich mit Desktop 1511×758 sowie iPhone-XR-Emulation 413×814/801×413 geprüft; dies ist kein physischer Telefontest. Test → Device Simulator ist vor Play zu aktivieren; während Play lässt sich die Ausrichtung drehen. Für reproduzierbare Grafikchecks wurde im laufenden Client über die Studio-Commandbar ausschließlich die Testeinstellung `settings().Rendering.QualityLevel` auf Level01/Level21 gesetzt und auf Automatic zurückgestellt; eine Einstellung vor Play kann beim Start zurückgesetzt werden. Diagnosebefehle sind separat von normalen Spieleraktionen dokumentiert. Keine Grafik-/Kontoeinstellung ist Produktlogik. [B1-Run](work/runs/boltbots-m1-b1-001.md), [C1-Basisbelege](reviews/evidence/M1-B1/README.md) und [B1-C2-HUD-Closure](reviews/evidence/M1-B1/c2/README.md) halten Grenzen, Quellbindung und unabhängige Entscheidung fest.

Aktuelle B2-Bindung und Prüfungen: [B2-Run](work/runs/boltbots-m1-b2-001.md) und [C1-Basisnachweise](reviews/evidence/M1-B2/README.md) und [aktuelle C2-Closure](reviews/evidence/M1-B2/c2/README.md). B2 prüft zusätzlich Kaufablehnung, Duplikate/Guards, Laufzeitwechsel, Orbit-Verpackung sowie Ausbau- und Orbitkarten in beiden schmalen Level01-Formaten. Die C2-Portraitkorrektur ist zusätzlich bei413×756/Level01 belegt. Der führende Abnahmestatus steht im Handover.

## Privates B3-Testziel und Speichern

Produktion, Cash, Upgrade/Abbruch, Sammlung und Plotisolation werden an der echten Szene geprüft. Speichern nur in einer separat benannten und autorisierten privaten Testexperience mit passend eingerichtetem DataStore-Zugriff. Kein Upload-/API-/Cookie-Setup gehört zum lokalen Rojo-Build. Ohne realen Save/Rejoin ist Persistenz nicht abgenommen. Codex hält Build, Aktionen, Screenshots/Logs, Grenzen und nächste Arbeit fest; Human beurteilt die tatsächliche Qualität.

Die ausdrücklich autorisierte eigene private Experience **BoltBots B3 Test 20261025** hat UniverseId `10772906084` und PlaceId `112662761038118`. Nur dieses Paar darf den isolierten Store `BoltBots_B3_20261025` verwenden. Studio API Services sind dort eingeschaltet; eine andere externe Experience wird ohne Storezugriff gesperrt. Den lokalen Build nicht als Ersatz für das private Ziel öffnen, wenn ein realer Save geprüft werden soll: das private Ziel in Studio öffnen und dort Rojo verbinden. Die externe Zielberechtigung ist kein allgemeiner Upload-/Produktionsauftrag.

Das Profil speichert Cash, Abschlüsse, Lifetime-Ertrag, L1/L2, Scout-/Orbitrechte und Produktionswahl. Es speichert keine Plotposition, Einzelroboter oder Offlineproduktion. Schema1 wird ausdrücklich zu Schema2 migriert; unbekannte oder beschädigte Daten werden abgewiesen. Bestätigte exklusive Sitzung90s, Autosave30s/spätestens5s vor Ablauf, manueller Retry frühestens3s und Leave-/Shutdownwartefenster25s. Während Save pausiert die Produktion zeitlich; ein Fehler hält sie und Käufe an. Ungeklärtes Laden erzeugt keine Ersatzdefaults. Bei abgelaufener Sitzung erhält erneuter Beitritt nur den letzten bestätigten Stand; kein Nullverlustversprechen.

[Realer B3-Nachweis](reviews/evidence/M1-B3/README.md) trennt normale Spiel-/Save-/Rejoinaktionen von bewusster API-Abschaltung und Studio-only Schreibfehlerdiagnose. `B3RejectStoreWrites` ist ausschließlich eine serverseitige Studio-Diagnose, kein Spielerfeature; Live-Server ignorieren sie. Nach Tests ist der Schalter aus, die API wieder an. Der approved B3-Stand wurde am25.10.2026 um10:52:01 nach bytegleicher Prüfung aller9Studioquellen erfolgreich privat gespeichert; genaue Bindung und Grenzen stehen im [B3-Run](work/runs/boltbots-m1-b3-001.md).


## Fehler und Wiederholung

Fehlende/abweichende Tools: `setup` erneut ausführen; Downloads werden nur bei passendem Pin wiederverwendet. Keine Hashprüfung abschalten. Abweichendes vorhandenes Plugin: genaue Datei/Version prüfen und gezielt entscheiden, keine pauschale Pluginlöschung. Fehlende persönliche Anmeldung oder Systemfreigabe: nur diesen Schritt an den Human geben. Build kann nach Korrektur neu erzeugt werden. Keine Zugangsdaten weitergeben, keine produktiven Spielstände für Tests verwenden.

Konkrete Versionen, Plugin-/Build-Nachweise und Prüfgrenzen stehen im [A2-Nachweis](reviews/evidence/M1-A2/setup-verification.json); der führende Arbeitsstand steht im [Handover](handover.md). Der vollständige Ablauf auf einem zweiten Rechner bleibt M3-Nachweis.


B4 ergänzt die reale1/2/4-Clientbasis und die fünfteKapazitätsgrenze; hohe lokaleVierclientlast ist keineEndgerätefreigabe. Der unabhängiggeprüfte B4-Stand wurde am25.10.2026 um15:00:28 nach direktemVergleich aller9Studio-Sources mit dem gebundenenBuild durch **Save to Roblox** in demselbenprivatenZiel gespeichert. HistorischerB4-Endzustand undGrenzen: [B4-Run](work/runs/boltbots-m1-b4-001.md). TemporäreB4-Probeskripte undWorkspaceattribute gehören nicht zum Produkt und sind entfernt; StudioEdit/Simulatoraus/Automatic,Rojo getrennt/Serverbeendet. NormalesFremdplot-Erkunden und Gesamtspielabnahme bleiben B5.

Aktueller privater B5-Stand: nach Neun-Sourcevergleich, Fixture-Rücknahme und abgeschalteter Teststörung am25.10.2026 um17:42:43UTC gespeichert; Rojo getrennt/Serve beendet. Eigener normaler Spielweg, Versand und Nahzoom-Bedienung unabhängig geprüft. Der echte Fremdplotbesuch wurde anschließend über offiziellen StudioMCP mit unveränderter Runtime unabhängig abgeschlossen; B5 approved, M180%, Human-Endentscheidung offen. [B5-Run und Transfernachweis](work/runs/boltbots-m1-b5-001.md).

### Offizieller StudioMCP für getrennte Testclients

Am25.10.2026 zusätzlich tatsächlich nachgewiesen: Studio **Assistant Settings → MCP Servers → Enable Studio as MCP server**, Quick connect für Codex; offizieller macOS-Server `/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP` mit stdio-Transport. [Herstelleranleitung](https://create.roblox.com/docs/studio/mcp). Der aktuelle Host lieferte28Tools. Jede Aktion adressiert eine tatsächlich aus `list_roblox_studios` gelesene `studio_id`; Place/Universe vor Änderungen prüfen. `get_studio_state` unterscheidet Edit/Client/Server. Keine Zugangsdaten auslesen und keine fremde Experience verwenden.

`start_stop_play` bietet nur einfachen Start/Stop. Für zwei echte Studio-Testclients unterstützte die vorhandene offizielle [StudioTestService-API](https://create.roblox.com/docs/reference/engine/classes/StudioTestService) über `execute_luau` im Editmodell `ExecuteMultiplayerTestAsync(2, "B5-normal-foreign-visit")`, asynchron in `task.spawn`, damit der MCP-Aufruf zurückkehrt. Erst nach tatsächlicher Startlatenz erschienen Server und beide Clients als eigene IDs. Die ursprüngliche Editor-ID blieb Edit; nicht irrtümlich dessen Zustand als fehlgeschlagenen Teststart deuten.

Normales Spielen funktionierte über `user_keyboard_input`/`user_mouse_input` mit der echten Client-ID und `datamodel_type="Client"`; `screen_capture` lieferte die tatsächliche Clientansicht. Die B5-Probe nutzte normale V-/WASD-/Mausradaktionen, keinen Teleport. `execute_luau` las ausschließlich Identität/Owner/Positionen zur Beobachtung. Reguläres Ende über `StudioTestService:EndTest(...)` im Testserver; danach nur ursprünglicher Editor, Editzustand und unveränderte Sources prüfen. Ein temporärer Standardbibliothek-Caller genügte; keine zusätzliche Plattform. Native macOS-CUA-Childfensterauswahl ist dafür nicht erforderlich. [Exakter B5-Besuchsbeleg und Grenzen](reviews/evidence/M1-B5/mcp-visit.md).
