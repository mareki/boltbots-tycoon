# Visuelle Richtung und begrenzter Designvertrag

> Artifact ID: `BOLTBOTS-DESIGN-001` · Revision: 3 · Status: candidate, Humanentscheidung offen
> Creator: /root · independent Product/UX/Engineering reviewer: /root/init_review
> D2 significant_ui innerhalb des D3-Initialisierungs-Runs
> `design_reference_only` · `non_promotable` · kein implementiertes Spiel

## Qualitätsziel und Bedeutung

**Eine einladende Roboterwerkstatt mit Figuren, die man kennenlernen und sammeln möchte.** Räumliche Tiefe, warme Beleuchtung, überzeugende Materialien und eigenständige Charaktere gehören bereits zur Designreferenz. Die [verbindliche Premium-Regel](../agent-extensions.md) verlangt zwei ausdrückliche Urteile: Ist die Gestaltung für Menschen ansprechend? Macht sie Lust, dieses Spiel zu spielen? Ein Nein verhindert die Abnahme; technische Korrektheit gleicht das nicht aus.

Revision 2 wurde vom Human abgelehnt. Revision 3 ersetzt deren flache Weltillustration vollständig durch eine ausgearbeitete räumliche Konzeptszene und neue Charakterporträts mit neu komponiertem HUD. Die abgelehnte Fassung bleibt als historische Evidenz erhalten. Ein Agentenurteil ist keine Messung menschlicher Präferenzen und überstimmt keine Human-Ablehnung.

Ziele, Guards und Fehler stammen unverändert aus [Factory r1, Kernreise](../specs/factory-module.md) und der Human-approved Foundation r1. Besitzer verstehen ihre Produktion, verbessern gezielt den Starter-Assembler und wählen freigeschaltete Designs. Roboter auf dem Band sind Output; Sammlungskarten sind Designrechte. Keine zusätzliche Währung, Inventarinstanz, globale Fabrikstufe oder Shoprolle. Die frühe unabhängige Flow-/Art-Linse im [Run](../work/runs/boltbots-initialization-001.md) bestätigt die unveränderte Bedeutung vor Erstellung; sie ist keine finale Qualitätsabnahme.

## Quellen und bewusste Gestaltung

Unveränderte Eingaben: [Inputmanifest](../product/input-snapshot-manifest.json), darin die drei Bilder `01_factory_world_concept.png`, `02_hud_concept.png`, `03_robot_shop_concept.png`, `VISUAL_DESIGN_BIBLE.md` und `design-tokens.json`. Die Bible nennt die Bilder Konzept-/Moodmaterial, keine pixelgenaue Oberfläche. Sie bleiben vergleichbare Referenzen; Import allein klärt keine Produktionsrechte.

Beibehalten werden freundliche Spielzeugformen, große Augen, helle Fabrik, Cyan für Produktion, Amber für Cash/Fortschritt und dunkle abgerundete Bedienflächen. Diamanten, XP, Shop-/Seltenheitsangebote und manuelles Cash-Abholen entfallen gemäß genehmigter Domain. Bilddetails erzeugen keine neuen Spielregeln.

Neue Bildbasis, erzeugt mit dem eingebauten **image_gen**, ohne Installation/API-Schlüssel:

- [Fabrikszene](reference/assets/factory-r3.png): Tageslicht, räumlich gestaffelte Werkstatt, Scout im Vordergrund, sichtbarer Assembler und Förderband. Bühne und Produktionsweg bleiben gegenüber der Oberfläche dominant.
- [Roboterset](reference/assets/robots-r3.png): Scout neugierig/ivory-cyan, Orbit mit Ring/violett, Bolt energisch/amber, Luma mit blattartigen Formen/coral, Atlas breit/mint. Unterschiedliche Körper, Gesichter und Posen; nicht bloß fünf Umfärbungen.
- [Vollständige Prompts und Herkunft](reference/assets/generation-r3.json): vier Bildaufrufe, zwei Assettypen. Die beiden transparenten Zwischenstände wurden wegen unsauberer Kanten verworfen und sind nicht eingebunden. Der finale Satz besitzt einen bewusst dunklen Studiohintergrund; der SVG-Renderer zeigt Ausschnitte des unveränderten Originals.

Die Szene ist eine **Art-Vision**, kein Screenshot eines existierenden Levels. Hintergrundmaschinen sind keine Aussage über bereits gekaufte Starterausstattung. M1 übersetzt Formensprache, Licht, Material, Figurenwirkung und Produktionslesbarkeit in einen kleinen echten Fabrikplatz; nicht die ganze Kulisse oder deren Detailmenge. Diese Konzeptbilder sind keine fertigen 3D-Modelle und keine neue Runtime-Abhängigkeit.

## Design System v0

Tokens: `ink.deep #101B35`, `ink.panel #172B4D`, `cyan #48D8F4`, `amber #FFCE53`, `coral #FF956B`, `violet #A784F7`, `positive #5AD9A6`, `danger #F4747B`, `text.main #F4F8FF`, `text.muted #B9C8DB`. Dunkle Schrift auf farbigen Aktionen; helle Schrift auf dunklen Panels. Nahezu deckende Flächen schützen Text vor dem detailreichen Hintergrund. Kontrastprüfung bezieht sich auf die tatsächlich verwendeten Rollen, zusätzlich echte Bildsicht.

Lokale System-Sans, keine Fontdownloads. Titel 28–36, Cardtitel 20–26, Körper 16, informative Labels mindestens 14 logische Pixel. Abstände 4/8/12/16/24/32, Panels Radius 16–24, Buttons Radius 14. Ziele mindestens 44×44; native beschriftete Buttons, sichtbarer Fokus, Text zusätzlich zur Farbe, Statusansage und reduzierte Bewegung. Kein dekorativer Animationszwang. Interaktion und Fokus sind im Quelltext angelegt; tatsächliche Browser-/Roblox-/Screenreader-Bedienung ist damit noch nicht nachgewiesen.

**Desktop 1280×800:** Welt dominant, Cash/Rate kompakt oben, nächstes Ziel links, Kontextaktion rechts, Navigation unten. Hero-Scout und Assembler bleiben sichtbar. Sammlung mit fünf großen Charakterkarten und klar getrennten Zuständen.

**Mobil 390×844:** eigener Szenenausschnitt und vertikale Aktionskarte. Die Sammlung zeigt einen großen Charakter, fünf Detailwahlen und eine eindeutige Produktionsaktion. Detail ansehen ist nicht Produktion wählen. Kleinere Bildschirme, Zoom/Reflow, Roblox-Core-GUI und Notch müssen in der Runtime gesondert geprüft werden; die beiden Referenzgrößen sind keine universelle Geräteabnahme.

## Kohärenter Ablauf und feste Fixtures

| Zustand / Screen | Sichtbares Ergebnis und erlaubte Aktion | Sourcebindung |
|---|---|---|
| world / S-WORLD | eigene Produktion, Cash/Rate, nächstes Ziel; Ausbau oder Sammlung öffnen | F-FIRST/F-UPGRADE, Q-FACTORY |
| upgrade / S-UPGRADE | Level, Preis 50 Cash und Wirkung sichtbar; ausdrücklich kaufen oder abbrechen | C-UPGRADE |
| upgraded / S-RESULT | Beispielantwort L2, 100 Cash, neue Rate; Orbit als neue Figur entdecken | F-UPGRADE/F-COLLECT, E-UNLOCK |
| collection / S-COLLECTION | fünf Designrechte, Scout/Orbit frei im Nachher-Beispiel; freie Produktion wählen; gesperrte Designs nur ansehen | C-SELECT, E-UNLOCK |
| collection_initial | vor Upgrade nur Scout frei; Öffnen/Schließen gewährt nichts | F-COLLECT, INV-DESIGN |
| orbit_selected | gewähltes Orbit bleibt bei Navigation erhalten, gilt ab nächstem Durchlauf | C-SELECT |
| save_error / S-ERROR | unbestätigtes Speichern, Produktion/Käufe pausiert, Navigation gesperrt; Retry bewahrt Profil und Auswahl | F-RECOVER, INV-RECOVERY |

150→100 Cash, L1→L2 und 25/7s→30/6s sind deterministische Beispielwerte, keine freigegebene Balance. Ein Kauf wirkt im Entwurf einmal, kein Kauf außerhalb des Kaufdialogs. Normaler Ansichtswechsel erhält Profil/Auswahl; nur die außerhalb der Spieleroberfläche liegende Beispielauswahl setzt bewusst ein anderes Fixture. Retry zeigt synthetische Wiederaufnahme, keinen tatsächlichen Speicherversuch. Keine Produktion, Accounts, APIs, Analytics, Zahlungen oder dauerhafte Speicherung.

Loading/funds/stale/denied folgen den bereits beschriebenen Factory-Texten/Guards und sind ergänzend annotiert, nicht zusätzlich gerendert. Die genauen Freischaltbedingungen späterer Familien werden vor M2 konkretisiert; die Referenz erfindet dafür keine Werte. Gestaltungs-/Platzierungsdialoge sind dort ebenfalls annotiert und werden vor M2 ausgearbeitet. Kein Login-/Shop-/Adminscreen.

## Maintained Source, Nachweis und Review

[Interaktive HTML-Referenz](reference/index.html), gemeinsamer [SVG-/Zustandsrenderer](reference/design.js), [Render-Skript](reference/render.cjs). HTML und PNGs benutzen dieselbe Layoutquelle und identische Bildbytes. HTML ist lokal ohne Backend oder Build zu öffnen. Bei vorhandenem Node und `sharp`: `node docs/design/reference/render.cjs`. Hier verwendet: bereits gebündeltes Node24.19.0 und sharp0.35.5; nichts installiert. Native Bildverarbeitung ist keine Browseremulation. Ein gesperrter Browserzugriff wird nicht umgangen und kein erfolgreicher Klicktest behauptet.

Acht repräsentative PNGs: Desktop Welt/Upgrade/Erfolg/Sammlung/Fehler, Mobile Upgrade/Sammlung/Fehler. [Rendermanifest r3](../reviews/evidence/BOLTBOTS-RUN-INITIALIZATION-001/r3/render-manifest.json) bindet Quelle, Assets, Fixture, Viewport und Bilder; drei unveränderte Quellenbilder und abgelehnte r2-Welt liegen zum direkten Vergleich daneben. [Gezielte Prüfungen](../reviews/evidence/BOLTBOTS-RUN-INITIALIZATION-001/r3/focused-checks.json) prüfen Übergänge, Auswahl-/Retry-Erhalt, Schrift-/Aktionsgrenzen, Syntax und Kontrast. Sie ersetzen keine qualitative Abnahme.

Creator und unabhängiger Reviewer sehen die tatsächlichen PNGs und vergleichen Komposition, Charakterwirkung, räumliche Tiefe, Materialien/Licht, Familienkohärenz, Lesbarkeit und Bedienweg mit den Quellen. **Eigenes begründetes Urteil zu visueller Qualität und menschlichem Spielanreiz**, getrennt von Technik. Das exakte [Review-Paket](../reviews/20261024-1.5.3-boltbots-initialization-review.md) bindet die Fassung und Humanentscheidung. Bild-/Quelländerungen erfordern betroffene neue Sichtprüfung. F-VIS-02 ist erst mit tragfähigem Ergebnis und unabhängiger Bewertung agentenseitig schließbar; die Humanfreigabe bleibt eigenständig.

Arbeits-/Korrekturgrenze im selben Run r2: 17:41:54–19:41:54 UTC, kumulativ sechs Zyklen einschließlich drei historischer; Neuherstellung Zyklus vier. Vier von vier Bildaufrufen verwendet. Drei bestehende Astra/xhigh-Identitäten, keine neue Rendererplattform oder Teamrolle.

## Verbindlicher Transfer nach Studio

M1 baut Fabrikplatz, Bauteil-Scout, eine ausgearbeitete Maschine, Förderband/Verpackung und HUD als echte Szene. **Auch Stufe A muss Menschen ansprechen und Lust aufs Spielen machen.** „Bauteile“ entschuldigen keine unattraktiven Figuren. Prüfen: prägnante Silhouette/Gesicht, Proportionen, Material-/Lichtwirkung, Produktionsrichtung, Kamera-/Avatarmaßstab, Feedback/Animation und gemessene Leistung, auch bei niedriger Grafikstufe.

Der Agent baut und spielt die Szene; der Human beurteilt die Richtung. Anschließend Stufe B des individuell verfeinerten Roboters, gegebenenfalls in M2. Blender bleibt optional und benötigt zuvor nachgewiesene Agent-Bedienbarkeit. Kein schönes Konzeptbild ersetzt eine überzeugende tatsächliche Spielszene oder die Bewertung echter Spieler.
