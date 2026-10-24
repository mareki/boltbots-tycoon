# Lokales Setup — geführt durch Codex

> Artifact ID: `BOLTBOTS-SETUP-001` · Revision: 1 · Status: candidate guide für M1

Dieser Guide soll eine andere Person nach einem frischen Checkout bis zum selbst testbaren Spiel führen. Codex prüft und erstellt die Umgebung; der Human meldet sich persönlich an und beurteilt Ergebnisse. **Aktuell befindet sich das Repository in der Initialisierung.** Die folgenden Produktbefehle entstehen in M1 und sind noch keine heute vorhandenen Startbefehle.

## Aktuell belegter Stand auf Mareks Mac

- Git vorhanden. Roblox- und Roblox-Studio-Dateien unter `/Applications/` gefunden; Dateifund allein war kein Nachweis einer nutzbaren Installation.
- Human meldet am 24.10.2026, Studio aktualisiert zu haben und sich anschließend anzumelden. Agent hat Start/Login noch nicht bestätigt.
- Rojo/Rokit/Luau-Prüfer/Blender zuvor nicht im PATH gefunden; das ist kein vollständiges Inventar aller Mac-Dateien. Vor Installation erneut prüfen.
- Import liegt unverändert unter `docs/product/reference/boltbots-v0.2/`; seine Skripte wurden nicht ausgeführt. Fehlender historischer `START_HERE.command` wird nicht als verfügbares Werkzeug ausgegeben.

## Ablauf nach Umsetzungsfreigabe

1. **Checkout und Auftrag:** Repository öffnen, README/Handover lesen, gewünschte freigegebene Spielrevision wählen. Codex erfasst OS/Architektur, Git und benötigte Werkzeuge mit tatsächlicher Version und Probelauf. macOS ist das erste unterstützte Entwicklungsziel; Windows-Anleitung erst nach überprüftem Weg.
2. **Studio:** vorhandene App identifizieren und tatsächlich starten. Wenn fehlend: offizielle Installation; Human führt persönliche Anmeldung durch. Codex übernimmt anschließend Place-/Projektbedienung soweit Werkzeugzugriff nachgewiesen ist. [Offizielle Studio-Einrichtung](https://create.roblox.com/docs/studio/setup).
3. **Rojo:** Projektpin prüfen, CLI und passendes Studio-Plugin einrichten. Die Quellreferenz nennt Rojo 7.7.1. Tatsächliche Kompatibilität und Installationsweg in M1 verifizieren; Versionen protokollieren. Rokit ist eine mögliche Verwaltung, kein Selbstzweck. [Rojo-v7-Installation](https://rojo.space/docs/v7/getting-started/installation/).
4. **Build:** M1 erstellt am Repositoryroot `default.project.json` und `scripts/doctor.sh`, `scripts/build.sh`, `scripts/check.sh`. Erst sobald sie vorhanden sind, lautet der vorgesehene Weg `bash scripts/doctor.sh`, `bash scripts/check.sh`, `bash scripts/build.sh`; Ergebnis `build/BoltBots.rbxlx`. Generierte Artefakte sind nicht die Quelle.
5. **Studio testen:** erzeugten Place öffnen, Play starten, Output prüfen. Für laufende Bearbeitung `rojo serve` und Studio-Plugin verbinden; Erfolg anhand tatsächlicher Verbindung, nicht des gestarteten CLI-Prozesses behaupten. [Rojo-Build/Serve](https://rojo.space/docs/v7/getting-started/new-game/).
6. **Spielprobe:** erster Scout, automatische Cash-Gutschrift, Upgrade/Abbruch und sichtbare Wirkung. Zweiten Client für Plotisolation. Codex hält Build, Aktionen und echte Screenshots/Logs fest. Human kann denselben Stand selbst spielen.
7. **Speichern:** nur in einer gesonderten autorisierten privaten Testexperience mit passend eingerichtetem DataStore-Zugriff. Keine produktive Experience für Studio-Speichertests. Save/Rejoin und Fehlerpfad tatsächlich ausführen; ohne diesen Schritt ist Persistenz nicht abgenommen.
8. **Handover:** genaue funktionierende Befehle, Versionen, Testumgebung, offene Grenzen und nächste Arbeit speichern. Zweiter Rechner prüft denselben Ablauf ohne private Pfade von Mareks Mac.

## Wenn ein Schritt scheitert

Codex nennt den konkreten fehlgeschlagenen Schritt samt Fehlermeldung und engster Reparatur. Fehlendes Tool installieren oder Version anpassen, Pluginverbindung separat prüfen, bei Lade-/Savefehlern nicht mit Defaultdaten überschreiben. Keine systemweite Löschung oder Credentialweitergabe. Ein bekannt falscher Dokumentenstatus ist kein Grund, erneut eine bereits erteilte Freigabe zu verlangen.

Der Human muss keine Roboter modellieren, Dateien manuell zusammenschieben oder Programmcode schreiben. Falls persönliche Kontobestätigung, OS-Zugriff oder nicht verfügbare Geräte einen Schritt begrenzen, wird genau dieser Bedarf benannt. „Agent kann UI steuern“ wird erst nach einem tatsächlichen Bediennachweis als Fähigkeit für Studio oder Blender übernommen.
