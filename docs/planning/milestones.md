# Meilensteine und erste Umsetzung — BoltBots

> Artifact ID: `BOLTBOTS-PLAN-001` · Revision: 1 · Status: candidate
> Owner: /root · Vision: BOLTBOTS-VISION-001 r1 · alle Runs weiterhin proposed

## Reihenfolge und Kapazität

Der Auftrag bleibt [Vision/MVP](../product/vision-and-mvp.md) innerhalb der genehmigten Foundation. Ein Creator/Lead, ein unabhängiger Reviewer und ein separater temporärer Startreviewer, alle Astra/xhigh wie beauftragt. Keine parallelen konkurrierenden Implementierungen. Die sechs Wochen sind relative Planungsfenster ab Umsetzungsfreigabe, keine Terminbehauptung; tatsächlicher Aufwand und verfügbare Geräte/Zugriffe entscheiden am jeweiligen Checkpoint. Pro Zweiwochenfenster rund ein Drittel für Test, Gestaltungskorrektur und Unvorhergesehenes reservieren.

| Inkrement / Zeitraum | Beobachtbares Ergebnis | Slice / Pakete / Abnahme |
|---|---|---|
| **M1 — erste spielbare Qualitätsreferenz**, Woche 1–2 | Neuer Checkout → Codex richtet ein → echter Scout entsteht → Cash → L2-Upgrade → Orbit-Ziel; Fortschritt bleibt nach Wiedereinstieg. Eine überzeugende Referenzszene, vom Agenten selbst gespielt | SL-01 Walking Skeleton; WP-01A Setup/Build, WP-01B spielbarer Kern + dünne Persistenz + Szene. Zusammen ein integrierter Kandidat; kein Release pro Kleinteil |
| **M2 — vollständige kleine Fabrik**, Woche 3–4 | Fünf unterscheidbare Designs, vollständiger Maschinenkatalog, freie Gestaltung/Ausstellung und klares MVP-Endziel; verfeinerter Roboter nach bestätigter Richtung | SL-02, WP-02. Frühestens nach M1-Erkenntnissen konkretisieren; Balance und Modellwerkzeug dann entscheiden |
| **M3 — belastbare private Beta**, Woche 5–6 | Reproduzierbarer Stand auf anderem Rechner, reale Geräte-/Mehrspieler-/Novizentests, Rechte und Recovery geklärt; Human kann privat spielen und Qualität beurteilen | SL-03, WP-03. Private Beta in ausdrücklich benannter Testumgebung; öffentliche Freigabe separat |

Nach jedem Slice und Zweiwochencheckpoint: Originalanforderungen gegen reale Ergebnisse prüfen; nächste zwei Wochen konkret halten, verbleibenden Horizont neu ordnen. Keine weitere Funktion nur weil sie in der alten Roadmap steht. Fachliche Änderungen an Eigentum/Sammelmodell/Speicherbedeutung zur Domainentscheidung zurückführen; unveränderte fachliche Grundlage nicht erneut freigeben lassen.

## M1 im Detail

**Ziel:** Der Human kann eine kleine echte Roboterfabrik auf seinem Mac spielen und anhand der tatsächlichen Szene entscheiden, ob Spielgefühl und Erscheinungsbild tragen. Der Agent führt Erstellung und Test aus. Ein Bildschirmbild oder bestandener Build allein erfüllt dieses Ziel nicht.

### WP-01A — geführte Umgebung und reproduzierbarer Build

Owner MOD-FACTORY/Entwicklungsumgebung, Feature F-CORE, Slice SL-01. Voraussetzungen: genaue Initialisierungsfreigabe, gültiger Umsetzungs-Run und Capability Preflight. Quellen: BOOT-01–04, Human-Setupanforderung.

1. Vorhandene Tools und Versionen erfassen, erfolgreiche Ausführung gesondert prüfen. Studio-Update ist vom Human gemeldet, Login noch nicht durch Agenten nachgewiesen. Persönliche Anmeldung bleibt beim Human; keine Zugangsdaten übernehmen.
2. Fehlende Rojo-/Prüfwerkzeuge mit kleinstem passenden offiziellen Weg einrichten. Projektversionen pinnen. Rokit nur einsetzen, wenn es Reproduzierbarkeit vereinfacht; keine vollständige Toolplattform vorsorglich installieren.
3. Aus der unveränderten Referenz die benötigten Runtime-Dateien bewusst in Produktpfade übernehmen und an neue Verträge anpassen. Referenz nicht direkt ausführen oder als fertiges Spiel deklarieren.
4. Dokumentierte Befehle für Doctor, Build und Checks anlegen. Build nach `build/`, generierte Dateien aus Git ausschließen. Keine unerklärten Doppelklick-Launcher.
5. Studio öffnen, Place laden, Play starten und tatsächliche Logs/Spielzustand festhalten. Rojo-Verbindung nur als erfolgreich melden, wenn Studio sie bestätigt.

**Abnahme:** sauberer Checkout baut `.rbxlx` mit Exit 0; Doctor nennt gefundene, ausführbare und fehlende Tools getrennt; Guide führt auf einem weiteren Rechner zur gleichen Spielversion. Zweiter Rechner darf später als M3-Nachweis erfolgen, muss bis dahin ausdrücklich offen bleiben. Kein Fake-CLI-Smoke als Spieltest.

### WP-01B — Kernschleife, Speichern und Qualitätsreferenz

Owner CTX-FACTORY, Feature F-CORE, Slice SL-01. Quellen: Factory-Verträge/Flows und alle in deren Trace genannten P0-IDs. Eine vertikale Umsetzung mit kleinen internen Schritten, keine generische Plattform.

1. Eine eigene Fabrik im echten Client: Teile → Assembler → Verpackung; serverseitiger Abschluss erhöht Cash genau einmal, schaltet Scout frei und aktualisiert das nächste Ziel.
2. Gültiges L2-Upgrade zeigt Preis und Wirkung, besitzt Abbruch/Ablehnung und bewirkt sichtbaren Tempounterschied. Orbit-Meilenstein gemäß freigegebener Semantik. Startwerte aus GameConfig sind reversible Testwerte; keine behauptete fertige Balance.
3. Dünner realer Profiladapter mit Versionsfeld, exklusiver Sitzung, Save/Rejoin und definierter Ausfallreaktion. Ein Migrationsfixture. Keine vollständige Persistenzplattform. Lokale Adaptertests und echte private Testumgebung ergänzen einander.
4. Ein Fabrikplatz, eine ausgearbeitete Maschine, ein Scout aus Bauteilen, Förderband/Verpackung, wichtigste Oberfläche. Tageslicht, Materialien, Größen, Kamera und einfache Animationen zusammen prüfen. Ein lokales HTML-Referenzbild ist kein Beleg dieser Studio-Szene.
5. Stufe A: stimmiger Bauteil-Roboter mit erkennbarem Gesicht/Silhouette. Human beurteilt Richtung an echter Szene. Stufe B: anschließend individuelles Modell, frühestens wenn Richtung und Agent-Werkzeugweg nachgewiesen sind. Das kann als M2-Ausarbeitung erfolgen; kein Blender-Zwang und kein Vorgriff auf Modellqualität.
6. Agent spielt mit normaler Spielerberechtigung: Einstieg, Produktion beobachten, Upgrade kaufen/abbrechen, Sammlung öffnen, Save/Rejoin, fremden Plot untersuchen. Erfolg hängt von beobachtetem Ergebnis ab; UI-Tool vorhanden bedeutet noch keinen getesteten Bedienweg.

**Agent-Spielbericht:** konkrete Buildrevision, Umgebung, Bildschirm/Viewport, ausgeführte Aktionen, tatsächliches Ergebnis, Screenshot/kurzer Clip und Bugs. Getrennte Bewertung von Orientierung, Feedback, Tempo, Roboterwirkung und Lesbarkeit, jeweils mit beobachteter Szene. Keine erfundenen Spielhandlungen oder subjektiven Nutzerzahlen. Human beurteilt am Ende selbst die Qualitätsrichtung.

### Konkrete M1-Abnahme

| Kriterium | Erforderlicher Nachweis / Anti-Kriterium |
|---|---|
| Einstieg → erster Scout → Upgrade | echte Aufnahme mit Events/Zeitpunkten; kein bloßes Rendering oder Testharness als Spiel |
| Geld und Eigentum | Null/Grenzpreis/Überlauf/ungültige Daten/Doppelauftrag/Parallelität; zwei Clients können fremde Plots nicht ändern |
| dauerhaft fortsetzen | realer Save/Rejoin in separater autorisierter Testexperience; Ladefehler erzeugt kein neues Defaultprofil |
| Fehler verständlich | Save unbestätigt → Produktion/Käufe pausieren, sichtbare Rückmeldung; sichere Wiederaufnahme demonstriert |
| Szene stimmig | Desktop und schmale Ansicht aus echter Spielkamera, lesbarer HUD, klare Silhouette/Produktionsrichtung, keine verdeckte Hauptaktion |
| Interaktion zugänglich | Touchziele ≥44px in UI-Referenz, ausreichender Kontrast, Text zusätzlich zu Farbe, sichtbarer Fokus; tatsächliche Roblox-Bedienung separat prüfen |
| Laufzeit begrenzt | bei 2–4 Clients keine unbeschränkt wachsende Outputzahl/Verbindungsliste; Profiling, nicht nur Augenschein |
| Agent kann arbeiten/spielen | tatsächlich ausgeführter Bedienweg inklusive Nachweis; bei Grenze konkrete alternative Automatisierung prüfen, keine stille Verlagerung an den Human |
| Weiterarbeit möglich | README/Setup/Befehle/Versionspins/Recovery stimmen mit frischem Build überein |

**Noch kein M1-Abnahmepunkt:** komplette fünf Familien, fertige Monetarisierung, finaler Kunststil sämtlicher Assets, universelle Cross-Plattform-Automatisierung. Die sichtbare Qualitätsreferenz und Save/Rejoin gehören dagegen ausdrücklich in M1.

## Vorgeschlagener erster Ausführungsauftrag

`RUN-M1-001`, Status **proposed**, D3 wegen gebündelter Tool-/Plattformaktionen und M1-Freigabe; daraus keine aktuelle Ausführungsautorität. Nach Gate in einen konkreten Run mit Pfaden, Nachweisen und aktueller Capability übernehmen, ohne das Konzept erneut zu planen.

- Outcome: SL-01 mit WP-01A/B und obigen Kriterien.
- Vorgesehene Pfade: Runtime `src/**`, Tests `tests/**`, Entwicklungsbefehle `scripts/**`, Rojo-Konfiguration und Toolpins, Setup-/Nachweisunterlagen. Referenz/Designpfade bleiben nicht importierbar; Core bleibt unverändert.
- Team: bestehende drei Rollen Astra/xhigh. Erste überprüfbare Arbeitseinheit maximal 120 aktive Minuten einschließlich Vorbereitung; danach realen Stand berichten, nicht automatisch Fertigstellung versprechen. Drei zusammenhängende technische Korrekturzyklen für den späteren neuen Umsetzungsauftrag, keine zusätzlichen verdeckten Reviewer-Runden.
- Externe Aktionen: lokale Toolinstallation/Studio-Bedienung nur im genau genehmigten M1-Auftrag. Private Testexperience erst mit exaktem Konto/Experience-Ziel und Autorisierung; keine öffentliche Veröffentlichung, Käufe, echte Nutzerdaten oder Produktionsspeicher.
- Rollback: Git-Diff/Commit, erzeugten Build neu erstellen; keine fremden Dateien entfernen. Testdaten isolieren; Schreibzugriffe bei Saveproblemen stoppen. Vor Schemaänderung Fixture-/Kompatibilitätspfad beweisen.
- Stop: fehlende echte Konto-/Zielberechtigung nur für betroffene externe Aktion; dokumentarische bekannte Statusabweichung hält unabhängige Arbeit nicht auf. Budgetende, neue fachliche Grundsatzfrage oder M1-Qualitätsentscheidung prägnant vorlegen.

## Release- und Testgrenzen

SL-01 endet für lokale Teilpakete bei lokal nachgewiesenem Ergebnis. Technische Slice-Abnahme braucht realen integrierten Test in einer ausdrücklich autorisierten privaten Roblox-Testexperience; der lokale Build ersetzt diesen Nachweis nicht. M1 darf deshalb nicht vollständig abgeschlossen gemeldet werden, solange echter Save/Rejoin oder die Testumgebung fehlt. Die genaue Umgebung wird bei Umsetzung benannt, kein erfundener Place-ID-Platzhalter als Freigabe.

Ein Kandidat je kohärentem Slice, nicht je Datei. Branch-/Versions-/Rollbackregeln und vorgeschlagene Roblox-Anpassung des generischen CDK-Ablaufs stehen in [Technik](../specs/technical-foundation.md). Öffentliche Veröffentlichung bleibt eigenes Human-Gate.
