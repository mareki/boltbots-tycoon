# Lokales Setup — geführt durch Codex

> Artifact ID: `BOLTBOTS-SETUP-001`
> Revision: 6 · Status: A2/A3, B1 und B2-C2 unabhängig approved; Grenzen siehe Run

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

`doctor` unterscheidet Dateifund, tatsächliche Ausführung und fehlende Anforderungen. Ein gefundener Studio-/Pluginpfad beweist weder Anmeldung noch funktionierende Verbindung. `check` kompiliert alle aktiven Luau-Dateien, prüft reine Regelmodule auf Typfehler und führt die Basistests aus. Für die Standalone-CLI wird ausschließlich die Roblox-`script.Parent.GameConfig`-Importzeile in einer temporären Kopie auf einen Dateipfad adaptiert; die Regellogik bleibt unverändert. Keine Simulation behauptet einen Roblox-Spieltest oder vollständige Roblox-API-Typprüfung.

`build` erzeugt `build/BoltBots.rbxlx` und gibt den SHA256 aus. `build/` ist generiert und ignoriert; `src/` plus `default.project.json` sind die Quelle. Die aktive B2-Quelle umfasst sieben Runtime-Dateien: Regeln/Konfiguration, Serveradapter, Werkstatt, Scout-/Orbit-Bauer und Clientansicht. Sie ersetzt die frühere A2-Diagnosebasis. `development-b2` ist ein lokales Entwicklungslabel. Persistenz, integrierte Mehrspielerprüfung und vollständige M1-Spielabnahme bleiben B3–B5.

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

## Aktueller B2-Start und Bedienung

Nach Build und File → Open startet Play die kleine Werkstatt serverseitig; die leere Editansicht ist erwartet. Scout wird montiert, fährt durch das offene Verpackungsportal und verlässt es als geschlossener Karton. Erst der serverseitige 9-Sekunden-Abschluss schreibt 25 Cash und beim ersten Mal das Scout-Designrecht gut. Die Sammlung ist kein Einzelroboterlager. Die sichtbare Kennzeichnung „Lokale Vorschau · ohne Speichern“ gilt für die gesamte Sitzung.

„Ausbauen“ zeigt50Cash für AssemblerL2,9→6Sekunden ab dem nächsten Zyklus, unverändert25Cash pro Roboter sowie Orbit und ein sichtbares Maschinenmodul. Abbrechen/×/M/Escape bewirken keinen Kauf. Ein erfolgreicher serverseitiger Kauf zieht genau50Cash ab und gewährt L2 und das Orbit-Designrecht gemeinsam. Die Werte sind lokale Testbalance. Der laufende Zyklus behält seine Dauer und Familie.

„Sammlung“ zeigt getrennte Scout-/Orbit-Details und eine ausdrückliche Produktionswahl für den nächsten Zyklus. Orbit bleibt bis L2 gesperrt; Ansehen allein wählt oder gewährt nichts. Der vollständige Orbit läuft durch dieselbe passende Verpackung. Beide Karten sperren darunterliegende Aktionen. × oder M schließen; Escape öffnet Roblox' reserviertes Menü und schließt dabei die Sammlung. Im Erkunden wird anschließend normale Maus-/Tastaturbewegung wieder frei. „Erkunden“ gibt normale Kamera und Spielersteuerung frei; „Werkstatt“ stellt die eigene feste Ansicht wieder her. „Bewegung: ruhig“ unterdrückt dekoratives Winken/Neigen, der Produktionsweg bleibt sichtbar. In der festen Ansicht werden Nachbarslots lokal ausgeblendet und Touch-Steuerkreise verborgen; Erkunden stellt sie wieder her.

B1 und B2 wurden in Studio tatsächlich mit Desktop 1511×758 sowie iPhone-XR-Emulation 413×814/801×413 geprüft; dies ist kein physischer Telefontest. Test → Device Simulator ist vor Play zu aktivieren; während Play lässt sich die Ausrichtung drehen. Für reproduzierbare Grafikchecks wurde im laufenden Client über die Studio-Commandbar ausschließlich die Testeinstellung `settings().Rendering.QualityLevel` auf Level01/Level21 gesetzt und auf Automatic zurückgestellt; eine Einstellung vor Play kann beim Start zurückgesetzt werden. Diagnosebefehle sind separat von normalen Spieleraktionen dokumentiert. Keine Grafik-/Kontoeinstellung ist Produktlogik. [B1-Run](work/runs/boltbots-m1-b1-001.md), [C1-Basisbelege](reviews/evidence/M1-B1/README.md) und [B1-C2-HUD-Closure](reviews/evidence/M1-B1/c2/README.md) halten Grenzen, Quellbindung und unabhängige Entscheidung fest.

Aktuelle B2-Bindung und Prüfungen: [B2-Run](work/runs/boltbots-m1-b2-001.md) und [C1-Basisnachweise](reviews/evidence/M1-B2/README.md) und [aktuelle C2-Closure](reviews/evidence/M1-B2/c2/README.md). B2 prüft zusätzlich Kaufablehnung, Duplikate/Guards, Laufzeitwechsel, Orbit-Verpackung sowie Ausbau- und Orbitkarten in beiden schmalen Level01-Formaten. Die C2-Portraitkorrektur ist zusätzlich bei413×756/Level01 belegt. Der führende Abnahmestatus steht im Handover.

## Spiel und Speichern — weitere M1-Schritte

Produktion, Cash, Upgrade/Abbruch, Sammlung und Plotisolation werden an der echten Szene geprüft. Speichern nur in einer separat benannten und autorisierten privaten Testexperience mit passend eingerichtetem DataStore-Zugriff. Kein Upload-/API-/Cookie-Setup gehört zum lokalen Rojo-Build. Ohne realen Save/Rejoin ist Persistenz nicht abgenommen. Codex hält Build, Aktionen, Screenshots/Logs, Grenzen und nächste Arbeit fest; Human beurteilt die tatsächliche Qualität.

## Fehler und Wiederholung

Fehlende/abweichende Tools: `setup` erneut ausführen; Downloads werden nur bei passendem Pin wiederverwendet. Keine Hashprüfung abschalten. Abweichendes vorhandenes Plugin: genaue Datei/Version prüfen und gezielt entscheiden, keine pauschale Pluginlöschung. Fehlende persönliche Anmeldung oder Systemfreigabe: nur diesen Schritt an den Human geben. Build kann nach Korrektur neu erzeugt werden. Keine Zugangsdaten weitergeben, keine produktiven Spielstände für Tests verwenden.

Konkrete Versionen, Plugin-/Build-Nachweise und Prüfgrenzen stehen im [A2-Nachweis](reviews/evidence/M1-A2/setup-verification.json); der führende Arbeitsstand steht im [Handover](handover.md). Der vollständige Ablauf auf einem zweiten Rechner bleibt M3-Nachweis.
