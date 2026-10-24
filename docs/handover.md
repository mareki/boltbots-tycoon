# Product Handover

> Artifact class: Navigation
> Linked owners: Bootstrap state, Initialization Run, Domain decision, Initialization Review, Product guidance

## Aktueller Stand

**Initialisierung abgeschlossen, Gesamtpaket und M1 vom Human freigegeben. M1 ist noch nicht umgesetzt.** Human verlangt vor der Umsetzung zunächst Überblick und Commit/Push. Diese Freigabe bleibt bestehen; Domain-, Bild- oder Gesamtfreigabe unveränderter Inhalte nicht erneut erfragen.

Wirksame Entscheidung und exakter Umfang: [Initialisierungsreview r3](reviews/20261024-1.5.3-boltbots-initialization-review.md), aktueller oberster Humanentscheid. Geprüfter Kandidat2b343b7 mit15Artefakten und ManifestSHA256e520abddf9328ac87d1d915b1bb5aac300ec15564a212513af904e02206b34f9 bleibt unverändert. Historische `candidate`-/`pending`-Header im Payload ändern nichts an dieser externen Freigabe.

## Was vorliegt

- 39 unverändert importierte Quellen, fachliche Grundlage genehmigt,39/39PRD-Anforderungen disponiert; [Vision r2](product/vision-and-mvp.md), Factory-/Technikziele, Setupguide und [Plan/M1 r2](planning/milestones.md) freigegeben.
- [Designreferenz r3](design/reference/index.html): räumliche Fabrikszene, fünf ausgearbeitete Charakterkonzepte und interaktive Desktop-/Mobilzustände. Acht PNGs tatsächlich geprüft,13gezielteSourceprüfungen undunabhängigeQualitäts-/Spielreizreviewapproved. Human hat Bilder undGesamtpaket angenommen; F-VIS-02geschlossen.
- [Premium-Regel](agent-extensions.md) gilt für jede Gestaltung und Review, bereits für den ersten Bauteil-Roboter und die echte M1-Szene. Frühere Ablehnung r2 bleibt als Historie erhalten.
- Führende abgeschlossene Arbeitsliste, Freigaben und100%-Drift: [Initialisierungs-Run r3](work/runs/boltbots-initialization-001.md).100%beziehtsichaufInitialisierung,nichtaufSpielentwicklung.

## M1 — Arbeitsschritte und laufender Status

**Aktuell: M1 genehmigt, Umsetzung noch nicht begonnen. Nächster Schritt: A1.** Abgeschlossen sind die vorgelagerte Initialisierung, fachliche/visuelle/Gesamtfreigabe und Git-Sicherung bis Commit `c60de92`. Das sind Voraussetzungen für M1, keine bereits gebaute Spielversion.

Diese Übersicht fasst den [genehmigten M1-Plan](planning/milestones.md#m1-im-detail) zusammen. Es bleiben **zwei Arbeitspakete in einem gemeinsamen Inkrement SL-01**: WP-01A Umgebung/Build und WP-01B spielbarer Kern mit Persistenz und Qualitätsreferenz. A1–B5 sind lesbare Teilschritte, keine zusätzlichen Arbeitspakete oder Freigabetore. Umfang und Abnahme des genehmigten Plans bleiben unverändert.

| Schritt | Arbeitspaket / Arbeit | Fertig, wenn tatsächlich nachgewiesen | Status / Ergebnisbeleg |
|---|---|---|---|
| **A1** | **WP-01A:** Tools und Agent-Bedienweg prüfen | Gefundene, ausführbare und fehlende Tools getrennt erfasst; Studio-/Accountzugriff und tatsächlich möglicher Agent-Bedienweg geklärt. Persönlicher Login bleibt beim Human. | **Offen — als Nächstes.** Human meldete Studio-Update; kein Agent-Start-/Loginbeleg. |
| **A2** | **WP-01A:** Projekt und reproduzierbaren Build einrichten | Benötigte Werkzeuge eingerichtet/versioniert, Runtime bewusst aus Referenz übernommen; Doctor-/Build-/Checkbefehle vorhanden, sauberer Checkout erzeugt eine `.rbxlx`-Datei. | **Offen.** Nach A1; noch keine Runtime-/Buildeinrichtung. |
| **A3** | **WP-01A:** Erste Version wirklich in Studio starten | Place geladen, Play tatsächlich gestartet, Logs und sichtbarer Zustand erfasst; Rojo-Verbindung nur bei bestätigter Verbindung als erfolgreich gewertet. Setup-Guide entspricht dem beobachteten Ablauf. | **Offen.** Nach A2; noch kein Studio-Spieltest. |
| **B1** | **WP-01B:** Kleine attraktive Fabrikszene und sichtbare Produktion | Fabrikplatz, Bauteil-Scout, Maschine, Förderband/Verpackung und HUD wirken zusammen; echter serverseitiger Abschluss schreibt Cash genau einmal gut und schaltet Scout frei. Gestaltung wird von Anfang an mit der Produktion entwickelt. | **Offen.** Nach A3; Konzeptbilder vorhanden, echte Szene fehlt. |
| **B2** | **WP-01B:** Ausbau und Orbit-Ziel | L2-Kauf zeigt Preis/Wirkung, Abbruch/Ablehnung bewahren den Stand; Upgrade wirkt sichtbar, Orbit wird regelgerecht frei und lässt sich auswählen. | **Offen.** Baut auf B1 auf; bisher nur Designfixtures. |
| **B3** | **WP-01B:** Fortschritt sicher wiederaufnehmen | Dünner realer Profiladapter mit Versionsfeld/exklusiver Sitzung, Migrationsfixture, Save/Rejoin und sicherer Fehlerreaktion nachgewiesen; Ladefehler erzeugt kein Ersatzprofil. | **Offen.** Profilregeln bereits genehmigt; reale private Testexperience vor externem Schreibtest genau benennen und Berechtigung prüfen. |
| **B4** | **WP-01B:** Technische und integrierte Prüfungen | Käufe/Geldgrenzen/Duplikate/Manipulationen geprüft; zwei Clients können fremde Fabriken nicht ändern; Fehlerpfade und begrenzte Ressourcen bei 2–4 Clients beobachtet. | **Offen.** Tests entstehen mit B1–B3; hier wird der integrierte Nachweis zusammengeführt. |
| **B5** | **WP-01B:** Agent-Spieltest, Qualitätsreview und Übergabe | Agent spielt den vollständigen Kernpfad mit normaler Spielerberechtigung; Build/Umgebung/Aktionen/Bilder/Bugs dokumentiert. Unabhängige Review bewertet Technik, Premium-Gestaltung und Spielanreiz getrennt; Setup-/Startanleitung stimmt. | **Offen.** Benötigt B1–B4; anschließend bestehende Human-Qualitätsentscheidung an der echten M1-Spielversion. |

**Abhängigkeiten:** A1 → A2 → A3 → B1; darauf Ausbau und Persistenz (B2/B3), anschließend integrierte Prüfung und Spielreview (B4/B5). Die technische Vorbereitung von Persistenz sowie passende Tests gehören bereits zu den jeweiligen Implementierungsschritten; die Tabelle ist keine Anweisung, Risiken oder Gestaltung bis zum Schluss aufzuschieben.

**Fortschreibung:** Nach jedem Teilschritt Status, beobachteten Nachweis und nächsten Schritt aktualisieren. Zustände: `offen`, `in Arbeit`, `in Prüfung`, `erledigt`; ein Hindernis wird mit konkreter Ursache und betroffener Abhängigkeit benannt. `Erledigt` verlangt das genannte tatsächliche Ergebnis und die jeweils nötige Prüfung; geschriebener Code oder ein schönes Konzeptbild allein genügt nicht. Der nächste konkrete Ausführungs-Run übernimmt diese Arbeitsliste; dann verweist die Übergabe auf dessen führenden Fortschrittsabschnitt, statt einen zweiten manuellen Tracker zu führen.

**M1-Abschluss:** gemeinsamer spielbarer und geprüfter Stand, echter Save/Rejoin, Agent-Spielnachweis und Humanbewertung der tatsächlichen Szene. Keine neue Konzept-/Bild-/Initialisierungsfreigabe für unveränderte Inhalte. Danach folgt M2 mit vollständiger Sammlung/Gestaltung, anschließend M3 mit belastbarer privater Beta; beide bleiben gemäß Plan später zu konkretisieren.

Noch keine Agent-Installation, kein ausgeführter importierter Produktcode und keine neue lauffähige Spielversion. Die Bilder sind Konzeptbilder, keine spielbare 3D-Welt. Persönliche Anmeldung bleibt beim Human; Erstellung, Bedienung und Tests übernimmt Codex.

## Sicherung und Grenzen

Lokaler Branch `codex/initialize-boltbots`; vorhandenes `origin`: `https://github.com/mareki/boltbots-tycoon.git`. Human hat Commit und normalenPush dieses aktuellenStandes ausdrücklichangeordnet; keinForce,keinMerge. TatsächlicherTransfer wirdmitPush-Ergebnis undgleicherRemote-Commit-ID bestätigt; Git-Tracking istderaktuelleRemote-Nachweis.

Drei bestehende Astra/xhigh-Rollen; Initialisierung endetmit4/6verbrauchtenKorrekturzyklen und4/4Bildaufrufen, keineweitereDesignarbeit. Bekannter engerStatusprüferfehler bleibt durchHumanoverride nichtblockierend, keinPASS/Core-Reparaturbehauptet. Kein aktuell behaupteter Wachhalteprozess.
