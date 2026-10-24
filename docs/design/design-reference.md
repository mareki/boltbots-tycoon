# Visuelle Richtung und begrenzter Designvertrag

> Artifact ID: `BOLTBOTS-DESIGN-001` · Revision: 1 · Status: candidate
> Creator: /root · independent Product/UX/Engineering reviewer: /root/init_review
> Design subwork: D2 significant_ui innerhalb des D3-Initialisierungs-Runs
> `design_reference_only` · `non_promotable` · kein implementiertes Spiel

## Bedeutung vor Darstellung

Quelle für Ziele/Guards/Fehler ist [Factory r1, Kernreise](../specs/factory-module.md), gebunden an die Human-approved Foundation r1. Der Entwurf zeigt einen Besitzer, der seine Produktion versteht, den Starter-Assembler gezielt verbessert und seinen Sammlungsfortschritt erkennt. Ein Roboter auf dem Band ist Output; eine Sammlungskarte ist ein Designrecht. Keine zusätzliche Währung, Inventarinstanz, globale Fabrikstufe oder Kaufrolle.

Frühe unabhängige Flowprüfung erfolgt vor UI-Erstellung gegen diese vorhandenen Quellen; Resultat im führenden [Run](../work/runs/boltbots-initialization-001.md). Es ist eine Linse der gleichen budgetierten Review, kein zusätzlicher Human-Gate.

## Eingabe und erlaubte Übernahme

Unveränderte Originale und genaue SHA256 stehen im [Inputmanifest](../product/input-snapshot-manifest.json). Betroffen: `assets/mockups/01_factory_world_concept.png`, `02_hud_concept.png`, `03_robot_shop_concept.png`, `docs/VISUAL_DESIGN_BIBLE.md`, `assets/design-tokens.json` unter der importierten v0.2-Referenz. Die Bible §§Einleitung/3/5 bezeichnet die Bilder ausdrücklich als Konzept-/Moodmaterial, nicht pixelgenaue Spieloberfläche. Sie bleiben sichtbar vergleichbare Eingabe, keine final freigegebenen Spielassets; Produktionsrechte noch nicht allein durch Import geklärt.

**Beibehalten:** freundliche Spielzeugformen, große Augen, warme Tageslichtfabrik, cyanfarbene Produktion, amberfarbene Cash-/Fortschrittsakzente, dunkle abgerundete HUD-Flächen und ein klares nächstes Ziel. **Konkrete Anpassungen:** erfundene Diamanten/XP/Shopangebote aus den Bildern entfallen gemäß freigegebener Domain/MVP; keine Bargeld-Abholung wegen automatischer Gutschrift. Typografie/Buttons werden lesbar und responsive aus den Textregeln abgeleitet. Keine Umdeutung von Bilddetails zu neuen Spielregeln. Sammlung übernimmt Familienidentität, keine Shop-/Seltenheits-/Kaufbehauptung.

Originalbilder werden für die Review unverändert ins Run-Evidenzverzeichnis kopiert und per Hash verglichen. Eigene SVG-Illustrationen sind neu erstellte Entwurfsgeometrie, keine endgültigen 3D-Assets oder Konkurrenzkopien.

## Design System v0

Tokens aus der Bible: `ink.deep #101B35`, `ink.panel #172B4D`, `brand.cyan #48D8F4`, `brand.amber #FFCE53`, `brand.coral #FF956B`, `brand.violet #A784F7`, `positive #5AD9A6`, `danger #F4747B`, `text.main #F4F8FF`, `text.muted #B9C8DB`, `surface.light #E7F3FF`.

Rollen: dunkle Schrift auf hellen/amber/cyan Buttons; helle Haupt-/Sekundärschrift auf dunklen Panels. Textkontrast für diese Paare berechnen und die wirklichen PNGs ansehen; Palette allein genügt nicht. Typografie lokale System-Sans, später passende Roblox-Sans ohne Fontdownload; Titel 28–36, Cardtitel 20–24, Körper 16, ergänzende Labels mindestens14 logische Pixel. Abstandsskala 4/8/12/16/24/32, Radius16 für Panels/12 für Buttons. Fokusring2px plus Abstand, Touchziele mindestens44px. Keine dekorative Daueranimation; reduzierte Bewegung ohne Informationsverlust.

Komponenten ausschließlich aus Kernflows: Statusleiste (Cash/Rate/Save), Zielkarte, beschriftete Hauptaktion, Produktionsszene, Maschinenkarte mit Kauf/Abbruch, Designkarte frei/gesperrt, eine textliche Erfolgs-/Fehlermeldung, untere Navigation. Kein generischer Dashboardbaukasten.

Desktop 1280×800: Weltfläche dominant, Ziel links oben, Maschine/Upgrade rechts, Navigation unten. Schmale Ansicht 390×844: oberer Cash-/Zielbereich, verkleinerte eigene Szene und vertikale Aktionskarte, kein winzig skaliertes Desktoplayout. Mobile Priorität bleibt Ziel → Welt → Handlung. Sichere Ränder; Runtime berücksichtigt Roblox-Core-GUI/Notch separat. Text und Aktionen dürfen nicht abgeschnitten sein.

## Kleinster kohärenter Entwurf

| Zustand | Sichtbares Ergebnis / erlaubte Interaktion | Flowbindung |
|---|---|---|
| world | eigene Fabrik, Scout, Ziel Starter-L2, Cash/Rate; „Ausbauen“ öffnet Detail | F-FIRST/F-UPGRADE, Q-FACTORY |
| upgrade | Starter-Level, Preis/Wirkung, explizites Kaufen und Abbrechen | C-UPGRADE, Guard aktuelle Serverdaten im späteren Spiel |
| upgraded | Beispielantwort: L2, weniger Cash, neue Rate, Orbit freigeschaltet; Sammlung öffnen | F-UPGRADE/F-COLLECT |
| collection | fünf Familien, Scout/Orbit frei im Beispiel, andere mit „Noch gesperrt“; genaue noch offene Voraussetzung nur als Reviewannotation außerhalb der Spieleroberfläche; freie Auswahl simulieren | C-SELECT, E-UNLOCK |
| save_error | Fehlertext, pausierte Fortschrittsaktionen, Wiederholung als separater synthetischer Zustand | F-RECOVER |
| loading / funds / stale / denied | genaue Texte und Guards aus Factory; annotierte nicht gerenderte ergänzende Zustände | keine neue Semantik |

Die Beispielwerte 150Cash, Upgradepreis50, L1→L2 und Raten sind deterministische Designfixtures, keine freigegebene Balance. Ein Klick schaltet zwischen festen Ansichten; keine echte Produktion, Speicherung, Cloud, Account-/Analytics-/Zahlungsaufrufe. Spätere Runtime übernimmt beobachtbare Bedeutung und Stil, nicht diese Simulationslogik.

Abdeckung: Desktop Welt/Upgrade/Erfolg/Sammlung/Fehler, Mobile Upgrade/Sammlung/Fehler. Drei Ansichten mit Varianten genügen; kein Login-/Shop-/Adminscreen. Stil-/Platzierungsdialoge sind präzise im Factory-Flow annotiert und vor M2-Umsetzung weiter auszuarbeiten. Keine Screenshotquote für irrelevante Seiten.

## Quelle, Reproduktion und Review

Maintained source unter `docs/design/reference/`: lokales `index.html`, ein gemeinsamer SVG-/Fixture-Renderer und ein kleines Render-Skript. HTML nutzt genau denselben Renderer wie die PNG-Erzeugung; native Buttons/Keyboardbedienung mit sichtbarem Fokus, textlich beschriftete Zustände. Lokal ohne Backend/Netzwerk zu öffnen. Die PNG-Prüfung beweist Bildinhalt, keine browserseitige Interaktionsabnahme oder Studiofunktion.

Rendern mit Node und `sharp`; die aktuelle Arbeitsumgebung enthält beides bereits, kein Download. Auf anderem Rechner nur bei bewusst eingerichteter Render-Abhängigkeit erforderlich; interaktive HTML-Datei braucht keinen Build. Ergebnisse/Hashmanifest unter `docs/reviews/evidence/BOLTBOTS-RUN-INITIALIZATION-001/`. Quelle/Fixture/Viewport/Zustand und konkrete Bilder werden in der finalen Review gebunden.

Vor UI-Erstellung: predeclared operative Authority /root/init_review entscheidet über begrenzte Standalone-Erstellung aus den illustrativen Quellen; endgültige Designentscheidung bleibt beim Human Initialization Gate. Keine bereits aktive Referenz wird ersetzt. Root erstellt, Reviewer liest Quellen und sieht tatsächlich jedes erforderliche Bild mit image_tool an. Prüfung: Bedeutung, Hierarchie, Proportionen, Komposition, Dichte, Leerraum, Clipping, Konsistenz und Nutzbarkeit; Abweichungen zur Eingabe mit obiger Begründung dokumentieren.

Budget: Teil des unveränderten Phase-B-Fensters bis18:38:45UTC und bestehender drei Identitäten; maximal diese Ansichten/Varianten, eine gemeinsame Schlussreview und gegebenenfalls verbleibende eine fokussierte Korrektur. Kein eigenes Renderingframework oder zusätzlicher Agent. Stop bei tatsächlicher Bedeutungsabweichung oder außerhalb der Autorität liegender Veränderung, nicht bei fehlender pixelgenauer Eingabe.

## Späterer Qualitätsnachweis in Studio

M1 baut den wirklichen Fabrikplatz, Bauteil-Scout, eine Maschine und HUD zusammen. Prüfen: charakteristische Silhouette, klarer Produktionsfluss, Kamera/Avatarmaßstab, Text-/Touchlesbarkeit, Materialien/Licht auch niedriger Grafikstufe, verständliche Animation/Rückmeldung, gemessene Leistung. Der Human beurteilt diese Szene, danach Stufe B des Roboters. Blender bleibt Option mit zuvor demonstrierter Agent-Bedienbarkeit; Werkzeugwahl allein garantiert keine Qualität.

Frühe Flow-Linse: /root/init_review `pass`, begrenzte `owner_approved_standalone`-Erstellung genehmigt. Fehler-/Retryfixture bewahrt den bestätigten Stand; Designauswahl gilt ab nächstem Produktionszyklus. M2-/Implementierungsfragen bleiben Reviewannotationen außerhalb der Spielansicht.

### Ausführbare Referenz und Renderbefehl

[HTML öffnen](reference/index.html). Quellrenderer: [design.js](reference/design.js); Reproduktion: [render.cjs](reference/render.cjs). In einer Umgebung mit Node und lokal verfügbarem `sharp`: `node docs/design/reference/render.cjs`. Hier wurde das bereits gebündelte sharp0.35.5 mit Node24.19.0 verwendet, ohne Installation. Genau acht Kandidaten-PNGs plus drei unveränderte Baselinebilder stehen im [Rendermanifest](../reviews/evidence/BOLTBOTS-RUN-INITIALIZATION-001/render-manifest.json). Zusätzlich besitzt die Sammlung eine feste Vor-Upgrade-Variante, damit Navigation keine Freischaltung erfindet.
