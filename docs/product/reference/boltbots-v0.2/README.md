# BOLTBOTS TYCOON
## Agent-first Roblox Game Studio | Projektpaket v0.2

**Status:** Agentenpaket mit erster Gameplay-Implementierung in Quelltexten; weder Roblox Studio noch Spielerlebnis wurden bisher auf deinem Mac verifiziert.  
**Stand:** 24. Oktober 2026 | **Plattform:** Roblox | **Primäre lokale Umgebung:** macOS + Codex  
**Sprache der Produktdokumente:** Deutsch | **Agentensteuerung:** Englisch (für reproduzierbare Aufträge)

> **Mission:** Ein eigenständiges, zugängliches und hochwertiges Free-to-Play-Fabrikspiel mit sammelbaren Robotern entwickeln; Entwicklung und QA so weit wie verantwortbar über lokale Codex-Agenten automatisieren. Der Mensch genehmigt Kontoaktionen, Käufe, externe Veröffentlichung und bedeutende Produktentscheidungen.

## Einstieg auf dem Mac

1. ZIP entpacken, diesen Ordner lokal auf dem Mac ablegen.
2. `START_HERE.command` im Terminal mit `bash START_HERE.command` starten. Das Skript bittet vor allen OS-Installationen um konkrete Freigabe, installierte Codex-Versionen werden wiederverwendet.
3. Falls Codex nach einer Neuinstallation noch nicht in PATH auftaucht: neues Terminal oeffnen und `bash scripts/start-codex-macos.sh` starten.
4. Codex liest `AGENTS.md` und den ersten Auftrag; es diagnostiziert und korrigiert die Umgebung, erstellt Build und Studio-Testbeweise und meldet nur notwendige Nutzeraktionen.

**Alternativ, wenn Codex bereits installiert ist:** `bash scripts/start-codex-macos.sh` direkt ausfuehren. Das aktualisiert nichts im System.

## Dokumente und Reihenfolge

| Datei | Zweck |
|---|---|
| `docs/BOOTSTRAP_MACOS.md` | Lokale Installation, Voraussetzungen und Freigabepunkte |
| `docs/ARCHITECTURE.md` | Rojo-Workflow, Komponenten, Datenhoheit, Security und Tests |
| `docs/GDD.md` | Vision, Game Loop, Economy, Maschinen, Roboter, Inhalte |
| `docs/PRD.md` | Implementierungsfähige Anforderungen mit IDs, Kriterien und Prioritäten |
| `docs/VISUAL_DESIGN_BIBLE.md` | Design-Tokens, Interface-, World- und Asset-Vorgaben |
| `docs/COMPETITOR_BENCHMARK.md` | Nachweisbare Benchmarks + Differenzierungsentscheidungen |
| `docs/MONETIZATION_LIVEOPS.md` | Shop, Produktlogik, Guardrails, KPI und Experimente |
| `docs/AGENT_PLAYBOOK.md` | Rollen, Task-Protokoll, Worktrees, Definition of Done |
| `docs/QA_RELEASE.md` | Testmatrix, Device-Matrix und Publishing-Freigaben |
| `docs/ROADMAP.md` | Meilensteine, Abhängigkeiten, Aufgabenreihenfolge |
| `docs/FIRST_CODEX_TASK.md` | Direkt verwendbarer Bootstrap- und M1-Verifikationsauftrag an Codex |
| `docs/SPRINT_01.md` | Implementierter Prototyp und offene echte Studio-Testfaelle |
| `docs/SOURCES.md` | Offizielle technische und beobachtbare Marktquellen |
| `docs/DECISIONS.md` | ADRs, offene Fragen und Produktentscheidungen |
| `docs/IMPLEMENTATION_LOG.md` | Evidenzprotokoll für Agenten und Reviews |

## Repository-Skelett

```text
BoltBotsTycoon_Codex_Starter/
├── AGENTS.md                     # Bindende Projektregeln für Codex
├── README.md
├── rokit.toml                    # Rojo gepinnt
├── default.project.json         # Rojo-Datenmodell
├── src/                         # Erster Luau-Prototyp, noch nicht Studio-getestet
├── assets/mockups/               # Original-KI-Konzeptbilder, keine Roblox-Screenshots
├── scripts/
│   ├── doctor-macos.sh           # Diagnostik ohne Änderungen
│   ├── bootstrap-macos.sh        # Zustimmungsbasierte lokale Einrichtung
│   ├── build.sh                  # Rojo Build
│   └── studio-smoke.sh           # Studio-CLI-Smoke-Test
└── docs/
```

## Sofortige Grenzen

- Ich habe **keinen Zugriff auf deinen lokalen Mac**; die hier erzeugten Dateien wurden in einer isolierten Erstellungsumgebung erzeugt. Installationen und Studio-Tests müssen von Codex **auf deinem Mac** durchgeführt und protokolliert werden.
- Das `src/`-Verzeichnis enthält jetzt die erste komplette Gameplay-Vertikalscheibe, aber sie ist **ungetestet in der Roblox-Engine**, besitzt noch keine Persistenz und ist keine Beta.
- Die visuellen Referenzen sind eigene synthetische Konzeptbilder. Typografische Werte, interne UI-Zahlen und generierte Layouts sind **Designhypothesen**, nicht valide Live-UI oder Informationen über Wettbewerber.
- Produktzahlen, Retention-Ziele, Einnahmen und Termine sind Hypothesen und müssen durch Live-Tests validiert werden.

## Leitidee

**Build delightful robots, not manipulative monetization.** Spieler haben schnelle Erfolge, erhalten durch clevere Fabrikautomatisierung neue Ausdrucksmöglichkeiten und kommen wegen eigenen Zielen und Freunden zurück, nicht wegen künstlicher Kaufzwänge.

## Dokumenten- und Rechtsstatus

Interne Designgrundlage; Konkurrenzanalysen beruhen auf öffentlichen Quellen und sind keine Genehmigung zur Übernahme fremder Assets, Texte, Marken, Musik, Skripte, Karten, Charakterdesigns oder spezifischer UI-Kompositionen. Vor kommerziellem Launch rechtliche und steuerliche Pflichten prüfen.

## Ausgeführter Entwicklungsstand v0.2

Quelltext angelegt: 4 instanzierte Fabriken, automatische Scout-Produktion, serverseitiger Cash-Loop, Upgrades, Spieler-HUD. `docs/SPRINT_01.md` enthält die notwendige Funktions-/Exploittest-Matrix. Erst Codex auf deinem Mac kann daraus ein verifiziert spielbares Studio-Projekt machen.
