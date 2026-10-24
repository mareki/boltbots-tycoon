# Lokales Setup — geführt durch Codex

> Artifact ID: `BOLTBOTS-SETUP-001`
> Revision: 3 · Status: A2 und A3 lokal nachgewiesen

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

`build` erzeugt `build/BoltBots.rbxlx` und gibt den SHA256 aus. `build/` ist generiert und ignoriert; `src/` plus `default.project.json` sind die Quelle. Die aktive A2-Basis stammt bewusst aus fünf Dateien des unveränderten v0.2-Imports. Sie ist noch **keine** abgenommene M1-Spiellogik oder Premium-Szene: aktuelle Kaufverträge, Sammlung, Persistenz und Gestaltung folgen in B1–B5. `development-a2` ist ein Entwicklungslabel, keine veröffentlichte Produktversion.

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

## Spiel und Speichern — weitere M1-Schritte

Produktion, Cash, Upgrade/Abbruch, Sammlung und Plotisolation werden an der echten Szene geprüft. Speichern nur in einer separat benannten und autorisierten privaten Testexperience mit passend eingerichtetem DataStore-Zugriff. Kein Upload-/API-/Cookie-Setup gehört zum lokalen Rojo-Build. Ohne realen Save/Rejoin ist Persistenz nicht abgenommen. Codex hält Build, Aktionen, Screenshots/Logs, Grenzen und nächste Arbeit fest; Human beurteilt die tatsächliche Qualität.

## Fehler und Wiederholung

Fehlende/abweichende Tools: `setup` erneut ausführen; Downloads werden nur bei passendem Pin wiederverwendet. Keine Hashprüfung abschalten. Abweichendes vorhandenes Plugin: genaue Datei/Version prüfen und gezielt entscheiden, keine pauschale Pluginlöschung. Fehlende persönliche Anmeldung oder Systemfreigabe: nur diesen Schritt an den Human geben. Build kann nach Korrektur neu erzeugt werden. Keine Zugangsdaten weitergeben, keine produktiven Spielstände für Tests verwenden.

Konkrete Versionen, Plugin-/Build-Nachweise und Prüfgrenzen stehen im [A2-Nachweis](reviews/evidence/M1-A2/setup-verification.json); der führende Arbeitsstand steht im [Handover](handover.md). Der vollständige Ablauf auf einem zweiten Rechner bleibt M3-Nachweis.
