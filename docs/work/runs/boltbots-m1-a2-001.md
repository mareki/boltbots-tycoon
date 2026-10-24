# Execution Run — M1 A2: lokale Einrichtung und Build

> Artifact ID: `BOLTBOTS-RUN-M1-A2-001`
> Artifact class: Work contract
> Owner: /root

<!-- run-contract:start -->
```json
{
  "schema_version": "1",
  "revision": 1,
  "status": "completed",
  "harness_version": "1.5.3",
  "run_kind": "product_delivery",
  "decision_class": "D1",
  "targets": [
    {
      "id": "BOLTBOTS-WP-01A",
      "path": "docs/work/packages/boltbots-wp-01a.md"
    },
    {
      "id": "BOLTBOTS-DOMAIN-FOUNDATION-001",
      "path": "docs/domains/domain-foundation.md"
    },
    {
      "id": "BOLTBOTS-DOMAIN-REVIEW-001",
      "path": "docs/reviews/20261024-1.5.3-boltbots-domain-foundation-review.md"
    },
    {
      "id": "BOLTBOTS-PLAN-001",
      "path": "docs/planning/milestones.md"
    },
    {
      "id": "BOLTBOTS-TECH-001",
      "path": "docs/specs/technical-foundation.md"
    }
  ],
  "outcome": "A2: frischer Quellstand erzeugt lokal einen reproduzierbaren Roblox-Place mit gepinnten Werkzeugen und installiertem Rojo-Plugin; kein Spieltest behauptet.",
  "allowed_paths": [
    ".tools/",
    "src/",
    "tests/",
    "scripts/",
    "default.project.json",
    "toolchain.json",
    ".gitignore",
    "README.md",
    "docs/setup.md",
    "docs/handover.md",
    "docs/work/",
    "docs/reviews/evidence/M1-A2/"
  ],
  "non_goals": [
    "A3 Studio Play/Verbindung",
    "neue Spielfunktionen oder Gestaltung",
    "DataStore/Upload/Publish",
    "Core oder Import verändern"
  ],
  "decision": {
    "authority": "Human Marek",
    "approval_ref": "human-approved: A2 end-to-end, Sol/High, 2026-10-24; M1-Gesamtfreigabe in docs/reviews/20261024-1.5.3-boltbots-initialization-review.md",
    "lead": "/root",
    "reasoning": "high",
    "agents": [
      "/root",
      "/root/a2_review",
      "/root/a2_spawn"
    ],
    "reviewers": [
      "/root/a2_review"
    ],
    "max_corrections": 3,
    "effort_override": "human-approved:20261024-A2-Sol-High"
  },
  "external_actions": {
    "allowed": [
      "offizielle Rojo/Luau-Release-Binaries nach .tools herunterladen und ausführen",
      "passendes lokales Rojo Studio-Plugin installieren und in nativer UI prüfen",
      "normaler Commit/Push codex/initialize-boltbots"
    ],
    "prohibited": [
      "Credentials lesen/speichern",
      "Roblox Upload/Publish oder DataStore",
      "Core-Mutation",
      "fremde Plugins überschreiben"
    ]
  },
  "completion_evidence": [
    "Toolversionen und offizieller Ursprung/Hashes",
    "Plugin-Installation und Studio-Sichtbarkeit",
    "Syntax/gezielte Regelchecks",
    "Build aus sauberem Quellstand und Hashvergleich",
    "aktualisierter Setupguide und unabhängige Ergebnisreview"
  ],
  "agent_start": {
    "applicability": "required",
    "spawn_reviewer": "/root/a2_spawn",
    "clearance": "pass",
    "cleared_agents": [
      "/root",
      "/root/a2_review",
      "/root/a2_spawn"
    ]
  }
}
```
<!-- run-contract:end -->

## Progress und Evidence

Führende M1-Arbeitsliste bleibt im [Handover](../../handover.md#m1--arbeitsschritte-und-laufender-status); dieser Run verweist darauf statt sie zu duplizieren. A2 ist die nächste offene Zeile.

<!-- task-controls:start -->
```json
{
  "checked_revision": 1,
  "progress": 20,
  "updates": [
    {
      "percent": 10,
      "evidence": "A1 abgeschlossen und unabhängig approved; übernommen aus docs/handover.md. A2 Vorbereitung seit 19:27UTC, keine Installation. Nächster Schritt: exakter Aktivierungs-Pass und lokale Einrichtung; kein fachlicher Blocker."
    },
    {
      "percent": 20,
      "evidence": "A2 technisch nachgewiesen: Rojo/Luau und Plugin7.7.1; Doctor/5Syntax-/reineTyp-/Regelchecks/Build Exit0; sauberer Clone42c4c6d mit frischem Download erzeugt identischen SHA256 f7642a8d. Unabhängige Ergebnisreview folgt, A3 offen, kein Ausführungsblocker."
    }
  ],
  "drift_checks": [
    {
      "percent": 20,
      "reviewer": "/root",
      "decision": "continue",
      "evidence": "Originalauftrag A2/BOOT-01–04 erfüllt technisch; kein A3/Play/Save/Cloud/Design. Zwei direkt gepinnte Tools, ein kleines Standardbibliotheks-Skript; kein zusätzlicher Manager/Framework. Ein Toolhash-Missverständnis in einer kohärenten Korrektur behoben,2Reserven bleiben. Preparation+Umsetzung seit19:27UTC, deutlich vor21:00:10Hardstop; verbleibend unabhängige Review und Git-Sicherung. Risiko: noch kein echter Spiel-/Zweitrechnertest, ausdrücklich nachgelagert."
    }
  ],
  "obligations": {
    "entry_integrity": {
      "state": "satisfied",
      "evidence": "Mandatory Entry und wirksame Foundation/Vision gelesen; externer Manifesthash und alle95Corehashes am A2-Einstieg bestätigt."
    },
    "scope_authority": {
      "state": "satisfied",
      "evidence": "Human beauftragt A2 end-to-end am24.10.2026; genehmigter WP-01A, nur A2. A3 und weitere Spielarbeit bleiben offen."
    },
    "agent_start_review": {
      "state": "satisfied",
      "evidence": "Root preparation/run_activation und Reviewerstart vom separaten /root/a2_spawn freigegeben. /root/a2_review hat exakten Codecommit42c4c6d plus Evidenzhash905ad0e0 unabhängig approved; Review unten."
    },
    "human_gates": {
      "state": "satisfied",
      "evidence": "Domain/Bilder/Gesamt-M1 bereits genehmigt. Aktueller Human setzt alle Rollen Sol/High. Kein neuer Human-Gate für lokale A2-Schritte."
    },
    "capability": {
      "state": "satisfied",
      "evidence": "Rojo7.7.1/Luau0.744 tatsächlich ausgeführt; Plugin7.7.1 im leeren Studio-Dokument geöffnet. Sauberer Checkout identischer Build. A3/Roblox-Spiel/Verbindung nicht behauptet."
    },
    "mutation_boundary": {
      "state": "satisfied",
      "evidence": "Nur benannte Produktpfade, isolierte .tools und ein offizielles lokales Plugin. Core und passive Referenz bleiben unverändert; keine Secrets/Cloud."
    },
    "budget_stop": {
      "state": "satisfied",
      "evidence": "A2 am24.10.2026 innerhalb erster M1-Einheit vor21:00:10UTC abgeschlossen. DreiSol/HighIdentitäten, initialeReview approved,1/3Korrekturen verbraucht,2verbleiben für fortgesetzten M1-Umsetzungsauftrag. Kein weiterer Agent/Runde."
    },
    "routed_requirements": {
      "state": "satisfied",
      "evidence": "A2/BOOT-01–04 lokal erfüllt und unabhängig geprüft. A3/Studio-Spiel/Verbindung, vollständige Factory-Verträge, Premium-Szene, Save/Rejoin und Zweitrechner bleiben offen; führender Handover fortgeschrieben."
    }
  }
}
```
<!-- task-controls:end -->

- Finite Grenze: erste M1-Einheit bis 21:00:10 UTC, einschließlich Vorbereitung; kein Budgetreset.
- Korrekturreserve für neuen M1-Umsetzungsauftrag: 3, verbraucht 1, verbleibend 2. A1 hatte keine Korrektur.
- Scope/Annahmen: fünf Referenzdateien als unfertige Diagnosebasis; keine Behauptung vollständiger Factory-Verträge, Persistenz oder Premium-Szene.
- Ansatz: offizielle gepinnte ZIP-Binaries ohne zusätzlichen Toolmanager; repositorylokal und mit SHA256 geprüft. macOS als nachgewiesenes Ziel; andere Systeme erst nach realer Prüfung.
- Startcommit: `c0cabf6412355b8c797fd381953360d194baaa84`. Aktueller und Push-Zielbranch: `codex/initialize-boltbots` → `origin/codex/initialize-boltbots`.
- Branch: genehmigter bestehender codex/initialize-boltbots, kein neuer Deployment-/Slicezweig für lokale Vorbereitung.
- Bekannter Prüferfehler: interne eingefrorene Foundationfelder widersprechen externer Humanfreigabe; enger Statusfehler ist durch Humanoverride nicht blockierend. Kein Coreeingriff, kein erfundenes PASS.
- Startreview: preparation pass durch /root/a2_spawn; run_activation pass durch /root/a2_spawn nach Pfad-/Startcommitbindung; Installation/Umsetzung jetzt innerhalb A2 freigegeben.
- Ergebnisreview und Nachweise: lokal approved; exakte Bindung und unabhängige Beobachtungen unten.

- Direkter Check nach Formkorrektur: einzig AHV-RUN-CHECK-001, CTX-FACTORY fehlt interne effektive Foundationrevision. Exakte unveränderte r1 ist extern freigegeben; bekannter Humanoverride gilt. Kein PASS behauptet, kein Coreeingriff.

- Diagnose/Korrektur 1: offizielles CLI installiert eingebettetes Plugin nach ~/Documents/Roblox/Plugins/RojoManagedPlugin.rbxm; dessen Hash unterscheidet sich vom separat veröffentlichten Release-Asset. Herkunft bleibt das SHA256-gepinnte offizielle CLI-Archiv. Eingebetteten Pluginhash separat gebunden, kein Hashcheck ausgeschaltet. Ein zusammenhängender technischer Korrekturzyklus verbraucht, 2 verbleiben. Studio-Verwaltung vor Neustart zeigt noch keinen Eintrag; tatsächliche Sichtbarkeit bleibt zu prüfen.

- Plugin-UI-Nachweis: nach Studio-Neustart in einem ausschließlich zur Pluginprüfung erstellten leeren Place1 ist Rojo 7.7.1 sichtbar und geöffnet; Connect nicht betätigt. Leeres Dokument über Don't Save verworfen. /root/a2_spawn bestätigte die bestehende A2-Clearance für diesen engen Nachweisschritt.
- Code/Tools nicht mehr in Bearbeitung: Doctor, 5 Syntaxprüfungen, reine Typ-/Regeltests und Build Exit0. Sauberer Checkout und unabhängige Ergebnisreview folgen am exakten Kandidaten.

- 20%-Drift am24.10.2026 tatsächlich gemeldet: Entscheidung continue zur unabhängigen Ergebnisprüfung. Quellkandidat42c4c6daab6b3dc6dff6a3e319c6179f7332b8bb; sauberer Checkout bleibt tracked-clean, frische Downloads, Buildhash identisch.

- Reviewerstart: /root/a2_spawn pass für /root/a2_review am exakten Quellcommit42c4c6d und zusätzlichem Evidenz-SHA256905ad0e0e501221084ab4f0563f19d4e8542216eb4a2e1bb0ac9915db38422d9. Reviewer führt nur Ergebnisprüfung durch, keine Installation/Produktänderung.

## Unabhängige A2-Ergebnisreview

**Entscheidung: `approved` ausschließlich für das lokale A2-Ergebnis**, 24.10.2026, Reviewer `/root/a2_review`, unabhängig vom Creator `/root`, nach dokumentiertem exaktem Spawn-Pass. Geprüft: Quellcommit `42c4c6daab6b3dc6dff6a3e319c6179f7332b8bb` und ergänzender Nachweis `docs/reviews/evidence/M1-A2/setup-verification.json`, SHA256 `905ad0e0e501221084ab4f0563f19d4e8542216eb4a2e1bb0ac9915db38422d9`. Code, Befehle, Pins, Setupguide und WP stimmen unabhängig mit dem Commit überein; sämtliche zehn gebundenen Nachweisdateien und fünf Import-/Runtimepaare passen zu ihren Hashes. Externer Manifesthash und alle95Coredateien erneut bestätigt. Der bekannte, vom Human ausgenommene interne Foundation-Statusfehler bleibt unverändert; kein Validator-PASS behauptet.

Zielverständnis: Die zugängliche persönliche Roboterfabrik braucht einen verlässlichen lokalen Bauweg, damit Codex anschließend das echte Spiel und die attraktive Szene erstellen und prüfen kann. A2 trägt hierzu Werkzeug-/Buildreproduzierbarkeit bei; Spielspaß, Gestaltung, Persistenz und Factory-Verträge sind keine durch diesen Schritt erfüllten Zusagen. Maßstab waren die ursprünglichen BOOT-/Humananforderungen, genehmigter Plan/WP-01A sowie die konkrete A2-Zeile; A3 und der ausdrücklich spätere Zweitrechnernachweis bleiben erhalten.

| Kriterium | Unabhängige Beobachtung / Grenze |
|---|---|
| Werkzeuge, Herkunft und minimale Einrichtung | Zwei offizielle Releasequellen mit festen Versionen/Archivhashes; vorhandene Downloads unabhängig gehasht, alle vier installierten Binaries bytegleich den jeweiligen ZIP-Mitgliedern. Prüfung erfolgt vor Ausführung. Plugininstaller verweigert ein vorhandenes abweichendes Managed-Plugin. Kein zusätzlicher Manager, Dienst oder Framework nötig. ARM-/Rosetta-Auswahl und fehlender Intel-/Zweitrechnernachweis sind ehrlich dokumentiert. |
| Plugin tatsächlich sichtbar | `studio-rojo-7.7.1.png` mit `view_image` tatsächlich angesehen: leeres Place1, Rojo7.7.1 geöffnet, Connect verfügbar; keine erfolgreiche Verbindung daraus abgeleitet. Doctor bestätigt separat passenden Plugin-Dateihash. Keine eigene Studioaktion durchgeführt. |
| Doctor, Checks und aktive Übernahme | Doctor, Check und Build im Hauptcheckout unabhängig Exit0. Fünf Runtime-Dateien kompiliert; reine Regel-/Typprüfungen testen Anfangszustand, Vergütung, fehlende/exakte Mittel, L2 und Levelgrenzen. Adapter ändert ausschließlich die eine Modulimportzeile einer temporären Kopie; keine Roblox-API-Simulation. Drei Runtime-Dateien unverändert übernommen; zwei unterscheiden sich nur durch Entwicklungslabel beziehungsweise Klarstellung der offenen Arbeit. Factory-Verträge, Missbrauchsschutz und Save/Rejoin bleiben unbewiesen. |
| Sauberer Quellbuild | Vorhandenen temporären Clone unabhängig beobachtet: HEAD exakt42c4c6d, tracked-clean, eigene gehashte Archive/Binaries. Dort Check und Build erneut Exit0; danach weiterhin tracked-clean. Build-SHA256 in beiden Checkouts `f7642a8dea683cd8b65b4312a2670c8ee87f82dacc8706fa2c6c8e822a255937`. Initial fehlende Tools und frische Installation sind durch die gebundenen Creatorlogs dokumentiert; der Reviewer hat keinen erneuten Netzwerkdownload ausgeführt. |
| Bedienbarkeit und Übergabe | Setupguide nennt die tatsächlich vorhandenen Befehle, Python-Voraussetzung, Architekturgrenzen, Pluginneustart und getrennte spätere Studio-/Speichertests. Keine Herstellung an den Human verlagert; persönliche Anmeldung bleibt dort. Keine angenommene Premiumgestaltung oder vollständige WP-/Slice-/M1-Abnahme. |

**Findings:** keine materiellen Findings, keine blockierenden Befunde, keine angeforderte Korrektur und kein Dissens. Closure ist für diese Revision abgeschlossen; keine zusätzliche Korrekturrunde verbraucht. Die überschaubare Standardbibliothekslösung erfüllt A2 ohne unnötige Infrastruktur. Nächster fachlicher Nachweis ist A3: BoltBots-Place tatsächlich laden und Play/Output beobachten; B1–B5 einschließlich Premium-Szene, vollständiger Regeln und Persistenz bleiben offen. Geänderte Implementierung oder Evidenz erfordert nur die betroffene erneute Prüfung.

## Abschluss und nächste Arbeit

A2 vollständig lokal nachgewiesen und unabhängig approved; M1-Fortschritt bleibt20%. Unveränderte Source/Tools/Tests/Setup aus42c4c6d. Abschließende Änderungen betreffen nur tatsächliche Clean-Checkout-Evidenz, Review und Navigation/Status. Direkter Checker wird erneut aufgerufen; die bereits ausdrücklich Human-disponierte Frozen-Foundation-Statusabweichung ist kein neuer Blocker und kein behauptetes PASS. Nächster Schritt A3, hierfür kein Spieltest vorweggenommen.

- Abschluss-Metadaten: cleared_agents enthält auch /root/a2_spawn aufgrund des tatsächlich erfolgten direkten Bootstraps aus verifiziertem Entry/Spawn-Rollenprofil (Collaboration§1.1-Rekursionsexzeption). Das behauptet weder eine Selbstreview noch einen zusätzlichen Spawn-Reviewer oder Inhaltsquorum. Root und Ergebnisreviewer haben die getrennten exakten Startpässe.
