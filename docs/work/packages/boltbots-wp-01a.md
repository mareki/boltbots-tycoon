# WP-01A — Umgebung und reproduzierbarer Build

> Artifact ID: `BOLTBOTS-WP-01A` · Revision: 1 · Artifact class: Work contract
> Owner / Creator: /root · M1 / SL-01 / F-CORE · Decision class: D1
> Human authority: M1-Gesamtfreigabe und A2-End-to-End-Auftrag am 24.10.2026

Der genehmigte Umfang und die Abnahme stehen in [M1 WP-01A](../../planning/milestones.md#wp-01a--geführte-umgebung-und-reproduzierbarer-build). Dies ist die konkrete Ausführungsbindung, kein neuer Plan. A1 ist nachgewiesen; der aktuelle Auftrag umfasst ausschließlich A2. A3 (Place öffnen, Play und Rojo-Verbindung) bleibt anschließend offen. Führender Arbeitsstand: [Handover](../../handover.md#m1--arbeitsschritte-und-laufender-status).

A2 liefert gepinnte offizielle Rojo-/Luau-Binaries, passendes Studio-Plugin, bewusst übernommene Runtime aus dem unveränderten Import, Root-Rojo-Konfiguration, Doctor-/Build-/Checkbefehle, einen sauberen Quellbuild und eine überprüfte Anleitung. Keine neue Spiellogik oder Gestaltung; die übernommene Basis ist noch keine Qualitätsabnahme. Relevante Quellen: [Technik r1](../../specs/technical-foundation.md), [Factory r1](../../specs/factory-module.md), [Setup](../../setup.md), BOOT-01–04 und Human-Setupanforderung. Keine Veröffentlichung, DataStore-Aktion, Accountänderung, bezahlte Tools oder Credentials.

Betroffener Kontext CTX-FACTORY: Runtime wird ohne fachliche Erweiterung als ausdrücklich unfertige Diagnosebasis übernommen. Foundation r1 und ihre externe Humanentscheidung bleiben wirksam; historische interne Kandidatenfelder werden nicht verändert. Non-visual A2: kein neuer visueller Entwurf. Premium-Abnahme der echten Szene bleibt B1/B5.

Prüfung: ausführbare Tools/Versionen und Plugin-Datei, Syntax aller aktiven Luau-Dateien, gezielte reine Regeltests, Build aus temporärer sauberer Quellkopie mit identischem Artefakthash, unabhängige Review. Zweitrechner und Spiel-/Verbindungstest bleiben offen. Rückweg: Git und ignoriertes build/. Werkzeuge liegen isoliert in .tools/; nur die benannte Rojo-Plugin-Datei wird außerhalb des Repositorys hinzugefügt, vorhandene abweichende Plugins nicht überschreiben.

<!-- domain-binding:start -->
```json
{"schema_version":"1","contexts":[{"id":"CTX-FACTORY","foundation_ref":"docs/domains/domain-foundation.md#revision-1","legacy_exception_ref":"none"}]}
```
<!-- domain-binding:end -->
