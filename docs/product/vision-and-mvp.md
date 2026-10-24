# BoltBots Tycoon — Vision und MVP

> Artifact ID: `BOLTBOTS-VISION-001` · Revision: 2 · Status: candidate, Human Initialization Gate pending
> Owner: /root · Foundation: BOLTBOTS-DOMAIN-FOUNDATION-001 r1, Human approved

## Das Spielerlebnis

Du betrittst deine kleine Roboterfabrik, siehst den ersten freundlichen Roboter entstehen und verdienst Factory Cash. Damit verbesserst du deine Maschinen. Neue, sichtbar unterschiedliche Robotertypen geben dem Ausbau ein Ziel; Farben und ein Ausstellungsplatz machen die Fabrik zu deiner eigenen. Der Fortschritt bleibt beim Wiederkommen erhalten.

Wir glauben, dass **sichtbare Produktion, verständlicher Fortschritt und liebenswerte Sammeldesigns** einen zugänglichen Spielkern ergeben. Das ist eine Produkthypothese, noch kein nachgewiesener Spielspaß. Zielgruppe sind Spieler, die ein leicht verständliches Fabrik-/Sammelspiel auf Roblox suchen. Desktop und Touch sind gleichwertige Bedienwege. Es gibt noch keine belastbare Nutzersegmentierung; `personas: not_created`, weil erfundene Biografien keine Designentscheidung begründen würden.

Quellen: [PRD](reference/boltbots-v0.2/docs/PRD.md), [GDD](reference/boltbots-v0.2/docs/GDD.md), [Humananforderungen](human-input.md), [exakte Foundation](../domains/domain-foundation.md) und ihre [wirksame Humanentscheidung](../reviews/20261024-1.5.3-boltbots-domain-foundation-review.md). Importierte Pläne und Anweisungen sind Referenzen, keine Ausführungsautorität. Die genehmigten Entscheidungen automatische Cash-Gutschrift, keine Blueprint-XP und Orbit ab Starter-Assembler-Level 2 bleiben bestehen.

## MVP-Vertrag

Ein Roblox-Erlebnis mit einer Welt, zunächst vier eigenen Fabrikplätzen als zu messender Kapazitätsannahme, einer Kette **Teile → Assembler → Verpackung → Cash**, serverseitigem Maschinenfortschritt, fünf Familien Scout/Bolt/Orbit/Luma/Atlas, mindestens drei kostenlosen Farb-/Detailoptionen und einem gespeicherten Ausstellungsplatz. Der Eigentümer kann seinen Fortschritt nach Verlassen wieder aufnehmen; andere Spieler dürfen ihn nicht verändern. Gesammelt werden freigeschaltete Designs, keine einzeln inventarisierten Produktionsroboter.

Das erste Inkrement ist kleiner: Setup plus tatsächlich spielbarer Scout-/Upgrade-Kern und eine überzeugende Referenzszene. Der komplette MVP ist erst mit den übrigen Designs, Persistenz-/Fehlernachweisen und privater Beta erreicht. Keine Produktionsfreigabe durch Initialisierung.

Nicht enthalten: Offline-Ertrag, dediziertes Freunde-Besuchssystem, Handel/PvP, Helfer-KI, zusätzliche Welten, bezahlte Angebote, Lootboxen oder ein externes Backend. Shopbilder begründen keine Monetarisierung. Diese Funktionen werden erst bei entsprechenden Nutzerbefunden und eigener Freigabe wieder betrachtet; keine vorbereitenden Services dafür.

**Qualität:** Die [verbindliche Premium-Regel aus Spielersicht](../agent-extensions.md) gilt für jede Gestaltung und Review, einschließlich Designreferenz und Bauteil-Roboter in M1. Creator und Reviewer müssen begründen, ob Menschen das Ergebnis ansprechend finden und Lust aufs Spielen bekommen; bei Nein keine Abnahme. Eigenständige attraktive Figuren, überzeugende Formen/Materialien/Licht/Animation, klare Spielkamera, verständliche Bedienung und gemessene Leistung gehören zusammen. Technische Korrektheit allein reicht nicht. Die neue [Designreferenz r3](../design/design-reference.md) konkretisiert die Richtung; tatsächlicher Spielspaß und Qualität der 3D-Szene bleiben in Studio und mit echten Spielern zu prüfen.

**Erfolgsmessung:** Zeit vom spielbereiten Einstieg bis zum ersten sichtbaren Roboter, mit separatem Produktions-/Freischaltereignis; Zielmedian ≤60s in einem echten unerfahrenen Testkollektiv. Technische Agenten-Smokes beweisen keinen Novizenmedian. Tutorialabschluss >75% ist eine Quellhypothese; Stichprobe und tatsächliche Ergebnisse berichten. D1/D7-Retention erst bei realen Kohorten. Keine erfundenen Umsatz-/Retentiongrenzen. Private Beta: keine offenen P0-Defekte, belegter Wiedereinstieg und Zwei-Spieler-Isolation, Rechte-/Performancebefunde geklärt.

**Abbruch-/Änderungsauslöser:** Kernschleife auch nach einer gezielten Verbesserung unverständlich oder uninteressant → Spielkern überarbeiten, keine Inhalte anhäufen. Unzuverlässiges Speichern → Beta sperren. Unzureichende Agent-Bedienbarkeit → konkreten Automatisierungsweg verbessern oder Umfang zur Entscheidung vorlegen; keine manuelle Erstellung beim Human einplanen. Fehlende Rechte → betroffene Assets ersetzen, nicht pauschal das Projekt anhalten.

## Rollen und Aufgaben

| Rolle/Segment | Aufgabe und Grenze | Use Cases |
|---|---|---|
| Neuer Besitzer | Ohne externes Tutorial produzieren und ersten sinnvollen Ausbau verstehen | UC-START, UC-PRODUCE, UC-IMPROVE |
| Wiederkehrender Besitzer | Bestätigten Fortschritt fortsetzen, Designs sammeln und ausstellen | UC-RESUME, UC-COLLECT, UC-EXPRESS |
| Betrachter im selben Server | Öffentliche Fabrik ansehen; keine Schreibrechte | UC-VIEW |
| Codex als Entwickler/Testspieler | Erstellung und Bedienung übernehmen, als Testspieler dieselben Spielrechte | sämtliche Tests; kein versteckter Wirtschaftszugriff |
| Human Product Owner | Ideen, Richtung und Qualität beurteilen; persönliche Anmeldung/Freigaben | bestehende Gates, kein Herstellungsarbeitsplan |

`privileged_product_access: not_applicable`: Der MVP besitzt kein Admin-/Backoffice-Produkt und keine privilegierte Spielerrolle. Roblox-Entwickler-/Publikationszugriff ist ein separater Plattformzugriff, kein Spielkonto mit Cash-Sonderrechten. Neue Adminfunktionen brauchen einen eigenen Umfangsentscheid.

## Vollständige Anforderungsdisposition

Alle Zeilen beziehen sich auf die gleichnamige ID im unveränderten PRD. `mvp` ist geplante Abnahme, kein DONE. M1/M2/M3 und Nachweise: [Plan](../planning/milestones.md). Gemeinsame technische Regeln: [Technik](../specs/technical-foundation.md); Flows/Verträge: [Factory](../specs/factory-module.md).

| ID | Disposition | Einordnung / geplanter Nachweis |
|---|---|---|
| BOOT-01 | mvp | M1: geführter Toolcheck, tatsächliche Versionen/Zugriff, keine Installation nur aufgrund eines Pfades behaupten |
| BOOT-02 | mvp | M1: sauberer Checkout baut mit dokumentiertem Befehl .rbxlx |
| BOOT-03 | mvp | M1: echtes Studio Play mit Boot-/Modulnachweis; CLI nur bei bestätigter Fähigkeit |
| BOOT-04 | mvp | M1–3: Anforderungen ↔ beobachtete Nachweise; bestehende konkrete Freigaben |
| SYS-01 | mvp | M1: zwei Clients, eigene Plots; fremde IDs abgewiesen |
| SYS-02 | mvp | M1: dünner Save/Rejoin-Pfad; M2/M3 volle Daten und Ausfalltests |
| SYS-03 | mvp | M1: schemaVersion und echte Migrationsfixture |
| SYS-04 | mvp | M1: Server berechnet Produktion, Preis, Ausgaben und Freischaltung |
| FTUE-01 | mvp | M1: ein klares nächstes Ziel auf Desktop/Touch |
| FTUE-02 | mvp | M1 instrumentieren; M3 realen Novizenmedian berichten, Ziel ≤60s |
| FTUE-03 | mvp | M1: L2-Kauf, erkennbares Ergebnis, unveränderte Cash bei Ablehnung |
| LOOP-01 | mvp | M1: sichtbare ganze Kette, Abschluss genau einmal vergütet |
| LOOP-02 | mvp | M1 Starter-Level; M2 vollständiger versionierter Maschinenkatalog |
| LOOP-03 | mvp | M1 Scout/Orbit-Kern; M2 fünf unterscheidbare, gespeicherte Designs |
| LOOP-04 | mvp | M2: ≥3 freie Optionen und ein gespeicherter Ausstellungsplatz |
| LOOP-05 | mvp | M1 nächstes Ziel; M2 Endziel und vollständige Übergänge |
| LOOP-06 | later | Offline-Ertrag erst nach Bedarf; neue Zeit-/Missbrauchsregeln nötig |
| SOC-01 | later | Eigene Besuchsvermittlung/Privatsphäre nach MVP; öffentliche Sicht im selben Server bleibt M1 |
| UI-01 | mvp | M1: Cash/Rate/Ziel/Menüs auf Desktop und Touch nutzbar |
| UI-02 | mvp | M1: Text plus Zustand, Fokus, ausreichend große Ziele |
| UI-03 | mvp | M1–3: gesamte Progression ohne Robux und Shop |
| UI-04 | mvp | M1: klare Kaufabsicht, Preis, Abbruch und Ablehnungszustände |
| UI-05 | later | Vollständige Settings später; keine obligatorische Daueranimation, reduzierte Bewegung bereits im Design beachten |
| PERF-01 | mvp | M1 Basisprofil; M3 tatsächliches schwächeres Zieltelefon, Framezeiten/Speicher berichten |
| PERF-02 | mvp | M1/M3: 2–4 Spieler, begrenzte Outputs/Loops und Profiling |
| ECO-01 | mvp | M1: Preise/Parallelität/Duplikate serverseitig geprüft |
| ECO-02 | mvp | M1: Null/Grenzpreis/Überlauf/Duplikat/ungültige Rate getestet |
| MON-01 | later | Kosmetikpass erst nach expliziter Monetarisierungsentscheidung |
| MON-02 | later | Keine Receipts vor Freigabe; dann dauerhafte Idempotenz nötig |
| MON-03 | later | Commerceprüfung bei Commerce; Plattform-/Assetprüfung für kostenlose Beta bleibt Pflicht |
| ANL-01 | mvp | M1: fünf Quellereignisse lokal messbar; M3 private Beta, keine sensiblen Logs |
| ANL-02 | later | Mangels Shop kein Commerce-Tracking |
| LIVE-01 | later | Live-Balancing-Verwaltung später; versionierte lokale Konfiguration/Rollback schon M1 |
| QA-01 | mvp | M1–3: tatsächliche Build-/Testläufe, keine fiktionalen grünen Checks |
| QA-02 | mvp | M1: manipulierte Remote-Aufrufe erzeugen keinen unverdienten/fremden Fortschritt |
| QA-03 | mvp | M1 Kernpfad, M3 vollständiger E2E-Beleg mit Bildern/Logs |
| QA-04 | mvp | M1: eigenes Assetregister; importierte Rechte noch nicht als geklärt behandeln |
| REL-01 | mvp | M1 private Testumgebung nach genauer Autorisierung; M3 private Beta mit Supportroute |
| REL-02 | mvp | Veröffentlichungs-Gate als Releasebedingung; öffentliche Veröffentlichung bleibt außerhalb dieser Initialisierung und privaten Beta |

O1–O5 werden durch FTUE, LOOP/SYS, SYS-04/QA-02, UI/PERF und QA/REL abgedeckt. Qualitätsabschnitt des PRD wird in Technik und Design konkretisiert. Die Eingabe hat 39 einzelne Anforderungs-IDs; keine davon wird durch den Import als erledigt gewertet.

## Richtung und offene Hypothesen

| Horizont | Gewünschtes Ergebnis / Entscheidungsauslöser |
|---|---|
| nächste sechs Wochen | Drei überprüfbare Inkremente gemäß Plan; relative Planungsfenster, kein garantierter Termin |
| etwa 3 Monate | Reale private Spieler verstehen Produktion/Ausbau/Sammeln; Daten entscheiden über Balancing und weitere Inhalte |
| etwa 6 Monate | Nur bei tragfähigem Kern: verbesserte Sammlung und soziale Ausstellung; kein zugesagtes Featurepaket |
| etwa 12 Monate | Wiederkehrende Nutzung und tragbarer Betrieb; freiwillige Kosmetik nur nach eigener Produkt-/Rechteentscheidung |
| 12–18 Monate | Eine wiedererkennbare, gepflegte Roboterfabrik mit konsistentem Qualitätsniveau, ohne vorsorglich mehrere Welten oder Dienste zu bauen |

Offen bleiben H-BAL (Preise/Raten), H-CAP (gemessene Kapazität), H-SAVE (gewählte Technik im Test), H-LOOK (echte Szene), H-AUTO (tatsächliche Agent-Bedienung). Owner jeweils Lead, Validierung M1; unwirksame Defaults reversibel ändern, fachliche Bedeutungsänderungen dem Human vorlegen. Preiswerte aus dem Prototyp sind Startfixtures, keine genehmigte Balance. Keine bezahlte Drittleistung ist eingeplant.
