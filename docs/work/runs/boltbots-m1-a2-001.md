# Execution Run — M1 A2: lokale Einrichtung und Build

> Artifact ID: `BOLTBOTS-RUN-M1-A2-001`
> Artifact class: Work contract
> Owner: /root

<!-- run-contract:start -->
```json
{
  "schema_version": "1",
  "revision": 1,
  "status": "active",
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
      "/root"
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
  "progress": 10,
  "updates": [
    {
      "percent": 10,
      "evidence": "A1 abgeschlossen und unabhängig approved; übernommen aus docs/handover.md. A2 Vorbereitung seit 19:27UTC, keine Installation. Nächster Schritt: exakter Aktivierungs-Pass und lokale Einrichtung; kein fachlicher Blocker."
    }
  ],
  "drift_checks": [],
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
      "evidence": "/root/a2_spawn preparation pass; Aktivierung wird vor erster Produktmutation an diesem Run geprüft. Reviewer erst am exakten Kandidaten."
    },
    "human_gates": {
      "state": "satisfied",
      "evidence": "Domain/Bilder/Gesamt-M1 bereits genehmigt. Aktueller Human setzt alle Rollen Sol/High. Kein neuer Human-Gate für lokale A2-Schritte."
    },
    "capability": {
      "state": "satisfied",
      "evidence": "A1 belegt Git/Python/Studio/basicUI; Rojo/Luau fehlen. Offizielle Release-Metadaten geprüft. Download mit enger Netzwerkfreigabe; Installation/Plugin empirisch zu prüfen."
    },
    "mutation_boundary": {
      "state": "satisfied",
      "evidence": "Nur benannte Produktpfade, isolierte .tools und ein offizielles lokales Plugin. Core und passive Referenz bleiben unverändert; keine Secrets/Cloud."
    },
    "budget_stop": {
      "state": "satisfied",
      "evidence": "Gemeinsame erste M1-Arbeitseinheit seit19:00:10UTC bis21:00:10UTC; A2 Vorbereitung seit19:27UTC. Drei neue A2-Rollen, maximal3gleichzeitig, drei Korrekturen,0verbraucht; keine Imagegen-Aufrufe."
    },
    "routed_requirements": {
      "state": "satisfied",
      "evidence": "BOOT-01–04 und WP-01A Quellen geladen; non_visual Diagnosebasis, Premium-Abnahme nicht vorweggenommen. Ein bestehender Handovertracker, kein zweiter."
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
- Ergebnisreview und Nachweise: pending.

- Direkter Check nach Formkorrektur: einzig AHV-RUN-CHECK-001, CTX-FACTORY fehlt interne effektive Foundationrevision. Exakte unveränderte r1 ist extern freigegeben; bekannter Humanoverride gilt. Kein PASS behauptet, kein Coreeingriff.

- Diagnose/Korrektur 1: offizielles CLI installiert eingebettetes Plugin nach ~/Documents/Roblox/Plugins/RojoManagedPlugin.rbxm; dessen Hash unterscheidet sich vom separat veröffentlichten Release-Asset. Herkunft bleibt das SHA256-gepinnte offizielle CLI-Archiv. Eingebetteten Pluginhash separat gebunden, kein Hashcheck ausgeschaltet. Ein zusammenhängender technischer Korrekturzyklus verbraucht, 2 verbleiben. Studio-Verwaltung vor Neustart zeigt noch keinen Eintrag; tatsächliche Sichtbarkeit bleibt zu prüfen.

- Plugin-UI-Nachweis: nach Studio-Neustart in einem ausschließlich zur Pluginprüfung erstellten leeren Place1 ist Rojo 7.7.1 sichtbar und geöffnet; Connect nicht betätigt. Leeres Dokument über Don't Save verworfen. /root/a2_spawn bestätigte die bestehende A2-Clearance für diesen engen Nachweisschritt.
- Code/Tools nicht mehr in Bearbeitung: Doctor, 5 Syntaxprüfungen, reine Typ-/Regeltests und Build Exit0. Sauberer Checkout und unabhängige Ergebnisreview folgen am exakten Kandidaten.
