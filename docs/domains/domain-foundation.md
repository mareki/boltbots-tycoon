# Fachliche Grundlage — BoltBots Tycoon

> Artifact ID: `BOLTBOTS-DOMAIN-FOUNDATION-001`  
> Artifact class: Product specification  
> Authority: vorgeschlagene fachliche Bedeutung für den benannten Horizont  
> Revision status: `in_review`  
> Semantic owner: Human Product Authority; Creator /root  
> Revision: 1  
> Governing artifacts: AH-SPEC-DOMAIN-001, BOLTBOTS-RUN-DOMAIN-001  
> Review/Human decision: unabhängige Review angefordert; Human pending, diese Fassung ist nicht wirksam

## Entscheidung in Spielsprache

Vorgeschlagen ist ein zugängliches Fabrik- und Sammelspiel: Jeder Spieler entwickelt seine eigene Fabrik, sieht Roboter entstehen, verdient dabei Factory Cash und schaltet unterscheidbare Robotertypen frei. Die Sammlung bewahrt freigeschaltete Designs; die vielen produzierten Roboter sind sichtbarer Produktionsoutput, kein Lager einzeln verwalteter Gegenstände. Ein ausgewähltes, bereits freigeschaltetes Design kann ausgestellt werden.

Die Quellen werden mit drei ausdrücklich vorgeschlagenen Präzisierungen übernommen: Cash wird bei fertig verpackter Produktion automatisch gutgeschrieben; zusätzliche Blueprint-XP entfallen im ersten Horizont; „Fabriklevel 2“ als Orbit-Voraussetzung bedeutet hier Level 2 des Starter-Assemblers. Das sind noch **keine Human-Entscheidungen**. Ihre Alternativen und Folgen stehen unter D-01 bis D-03. Zusammen mit den übrigen Ableitungen ist die exakte Fassung am Domain-Gate zu bestätigen oder zu ändern.

## Quellen, Aussageklassen und Horizont

Der [unveränderte Import](../product/input-snapshot-manifest.json) bindet alle Quelldateien. Nachfolgende Kürzel verweisen auf genaue Eigentümer der übernommenen Bedeutung; diese Foundation wiederholt deren bereits ausreichende Beschreibungen nicht.

| Quelle | Übernommene Aussage / Grenze |
|---|---|
| **HUM** — [Gesprächsanforderungen](../product/human-input.md) | Vom Human bestätigt: Agent erstellt/bedient alles; geführtes Setup nach Checkout; echte Spieltests; visuelle Referenzszene und Roboter in zwei Gestaltungsstufen. Das sind Entwicklungs-/Qualitätsanforderungen, keine neuen Spielobjekte. |
| **PRD** — [PRD v0.1](../product/reference/boltbots-v0.2/docs/PRD.md), §§1–4 und IDs | Als Vorschlag übernommen: SYS-01/02/04 (Eigentum, Speichern, autoritative Wirtschaft); LOOP-01–05 (Produktion, Maschinen, fünf Designs, Kosmetik, Ziele); UI-03/04 und ECO-01/02 (freie Progression, gültige Käufe). Keine P0-Abnahme oder Fertigstellungszusage. |
| **GDD** — [GDD v0.1](../product/reference/boltbots-v0.2/docs/GDD.md), §§1–5 | Als Vorschlag übernommen: eigene Fabrik je Spieler; eine Kette; feste Bauplätze; Scout/Bolt/Orbit/Luma/Atlas; freie Farbwahl und ein Ausstellungsplatz; Sammelroboter ohne autonome Helfer-KI. C1-Spielidee und grobe Aufgaben sind dort bereits ausreichend beschrieben. |
| **DESIGN** — [Visual Design Bible](../product/reference/boltbots-v0.2/docs/VISUAL_DESIGN_BIBLE.md) und [Bildreferenzen](../product/reference/boltbots-v0.2/assets/mockups/) | Freundliche, gut lesbare Gestaltung als Eingabe. Bilder sind Konzeptmaterial, keine genehmigte Währungs-, Seltenheits-, Shop- oder Weltenlogik. Konkrete Gestaltung folgt nach Domain-Gate. |
| **CODE** — [Main.server.luau](../product/reference/boltbots-v0.2/src/ServerScriptService/Main.server.luau), [GameConfig](../product/reference/boltbots-v0.2/src/ReplicatedStorage/Shared/GameConfig.luau), [Sprint 01](../product/reference/boltbots-v0.2/docs/SPRINT_01.md) | Nur gelesene Evidenz des kleinen Ausgangsprototyps: vier Plätze, Scout, automatische Cash-Gutschrift und Maschinenupgrade; kein Speichern/kompletter Katalog. Kein Studio-Testnachweis und keine heutige Laufzeitbehauptung. |
| **OPS** — [Bootstrap macOS](../product/reference/boltbots-v0.2/docs/BOOTSTRAP_MACOS.md), [QA](../product/reference/boltbots-v0.2/docs/QA_RELEASE.md), [Beobachtungslog](../product/reference/boltbots-v0.2/docs/COMPETITOR_OBSERVATION_LOG.md) | Einrichtung/Testentwürfe für spätere Planung. Leere Hands-on-Beobachtungen und öffentliche Links belegen keine eigene Spielerfahrung. Importierte Playbooks/Roadmaps/Architektur haben keine aktive Anweisungsautorität. |

**Horizont:** Semantik des vorgeschlagenen ersten MVP und der ersten sechs Entwicklungswochen: eine gemeinsame Welt mit getrennten persönlichen Fabriken, eine Produktionskette, Maschinenfortschritt, fünf Designs, kostenlose Gestaltung und verlässliches Speichern. Das ist eine Modellierungsgrenze, kein Liefertermin und kein detaillierter MVP-Vertrag. Anfangskapazität 1–4 Spieler bleibt ein zu messender Richtwert. Der erste spätere Meilenstein enthält nur den kleineren Setup-/Spiel-/Design-Nachweis gemäß HUM; die übrige Reihenfolge wird erst nach dem Gate geplant.

**Außerhalb:** bezahlte Angebote/Entitlements, Offline-Ertrag, dedizierte Freundbesuch-Funktion, mehrere Welten, freies Förderbandrouting, Trading/PvP/Diebstahl, Prestige, bezahlter Zufall, autonom arbeitende Roboter. Quellen nennen diese als P1/P2 oder Nichtziele. Sie sind keine bereits entdeckten In-Horizon-Kontexte. Bei Aufnahme ist ein Domain-Impact-Vorschlag nötig; keine vorsorglichen Dienste oder Module.

### Was fehlt oder widerspricht sich tatsächlich?

- C1-Spielidee, Rollen und Grobaufgaben sind durch PRD/GDD ausreichend belegt und werden per Referenz übernommen.
- **Konflikte D-01–03:** automatische Gutschrift versus Abholen, Blueprint-XP ohne vollständige Regel, unbestimmtes Fabriklevel. Sie werden unten als konkrete Vorschläge mit Alternativen entschieden, nicht stillschweigend aus Code abgeleitet.
- **Notwendige Konsolidierung A-01:** persönlicher Fabrikfortschritt, Cash, Maschinen und freigeschaltete Designs benötigen gemeinsame Eigentums-/Konsistenzregeln. Dafür wird ein Kontext modelliert, keine aus Bildschirmen abgeleitete Aufteilung.
- **Lücken A-02–05:** Plot ist noch nicht von dauerhaftem Fabrikbesitz getrennt; produzierte Einheit noch nicht von Sammeldesign; Ausfall-/Parallelzugriff und dauerhafte Preis-/Freischaltgrenzen sind nicht zusammenhängend beschrieben. Die nachfolgenden Beziehungen, Invarianten und Szenarien schließen genau diese Lücken.
- Zahlen in GDD und CODE widersprechen sich teilweise (z. B. Anfangsertrag). Das ist **H-BAL**, eine spätere Balancingfrage; keine aktuelle Rate wird zur fachlichen Wahrheit erklärt.

## C1 — Sprache, Akteure und Aufgaben

### Gemeinsame Sprache

| ID / Begriff | Genaue Bedeutung | Nicht gemeint | Beleg |
|---|---|---|---|
| T-FACTORY / Fabrik | Ein dauerhaft einem Roblox-Konto zugeordneter Fortschritts- und Gestaltungsstand | Physische Parzelle für immer; gemeinsame Gildenfabrik | PRD SYS-01/02; GDD5.1; A-01/02 |
| T-PLOT / Plot | Begrenzter Platz einer laufenden Serversitzung; zeitweise genau einer aktiven Fabrik zugewiesen | Übertragbarer Besitz oder dauerhaft gespeicherte Weltkoordinate | GDD5.1; A-02 |
| T-DESIGN / Design, Blueprint, Roboterfamilie | Dieselbe stabile Freischaltidentität; Scout/Bolt/Orbit/Luma/Atlas sind vorgeschlagene Inhalte | Verbrauchbares Rezept, individuelle Roboterinstanz oder bezahltes Zufallslos | PRD LOOP-03; GDD5.4; A-03 |
| T-UNIT / Produktionseinheit | Ein abgeschlossener Durchlauf der gewählten Roboterfamilie; erzeugt sichtbaren Output und Ertrag | Ein dauerhaft inventarisiertes Einzelstück | PRD LOOP-01; GDD4/5.2; A-03 |
| T-CASH / Factory Cash | Einzige verdiente, nicht mit Robux kaufbare Währung dieses Horizonts | Robux, Diamanten, Energie oder Blueprint-XP | GDD5.3; D-02 |
| T-MACHINE / Maschine | Eigene platzierte Station mit stabiler Identität, Typ und Upgradelevel innerhalb einer Fabrik | Separate Firma, Dienst oder automatisch eigenständige Navigation | PRD LOOP-02; GDD5.1/5.2 |
| T-LEVEL / Level | Upgradelevel einer bestimmten Maschine | Implizites globales Fabriklevel | PRD FTUE-03; D-03 |
| T-DISPLAY / Ausstellungswahl | Höchstens ein eigenes freigeschaltetes Design mit zulässiger Gestaltung | Übertragung oder Verbrauch dieses Designs | PRD LOOP-04; GDD5.4 |

**Akteure:** ACT-OWNER ist das von Roblox authentifizierte Konto in der Rolle Besitzer seiner Fabrik. Dasselbe Konto ist ACT-VIEWER gegenüber anderen sichtbaren Fabriken: ansehen, nicht ändern. Ein echter Spieler und ein Agent im Spiel haben dieselben Spielrechte; ein Entwickleragent besitzt keine versteckte Wirtschaftsberechtigung. ACT-SYSTEM führt autorisierte Produktions-/Speicherabläufe aus; der Spielclient ist keine Vertrauensquelle. Es gibt in diesem Horizont keine produktseitigen Organisationskonten, Mitgliedschaften, Teams oder delegierten Besitzerrollen. Beleg: PRD SYS-01/04, QA-02; HUM; A-01.

**Externe Konzepte:** EXT-ROBLOX-IDENTITY liefert die vertrauenswürdige Kontoidentität; EXT-STORE bewahrt den bestätigten Fortschritt; EXT-CLIENT sendet Spielerabsichten und stellt freigegebene Ansichten dar. Roblox-Avatare, Plattformchat und Kontoverwaltung bleiben Plattformverantwortung. Die Wahl einer Speicher-API/Integrationsform gehört zur späteren Architektur.

| Use Case | Akteur / gewünschtes Ergebnis | Grobe Erfolgs-/Fehlergrenze | Quelle |
|---|---|---|---|
| UC-START | Owner betritt seine Fabrik / setzt fort | Letzter bestätigter Fortschritt plus eigener freier Plot; kein Platz oder unklarer Ladezustand ergibt keine fremde/neue Ersatzfabrik | SYS-01/02; A-02/04 |
| UC-PRODUCE | System lässt gewählte Produktion laufen | Fertige Einheit genau einmal vergütet; ungeprüfte oder doppelte Abschlussmeldung wirkungslos | LOOP-01; ECO-01; D-01 |
| UC-IMPROVE | Owner kauft/verbessert eine erlaubte Maschine | Voraussetzungen, Platz und Cash passen; sonst unveränderter Zustand | LOOP-02; UI-04; ECO-01 |
| UC-COLLECT | Owner schaltet Designs frei und wählt Produktion | Bekannte Voraussetzung erfüllt; neue Berechtigung bleibt gespeichert; gesperrte Auswahl abgelehnt | LOOP-03/05; GDD5.4 |
| UC-EXPRESS | Owner gestaltet eigene Fabrik/Ausstellung | Zulässige freie Auswahl gespeichert; fremder Plot/unbekanntes Design unverändert | LOOP-04; GDD5.1/5.4 |
| UC-VIEW | Viewer betrachtet eine andere sichtbare Fabrik | Öffentliche Gestaltungs-/Fortschrittsansicht ohne Schreibrecht oder private Profildaten | SYS-01; GDD5.1/5.5; A-05 |
| UC-RESUME | Owner verlässt und kehrt zurück | Bestätigter Stand erhalten; Fehler sichtbar, kein stilles Überschreiben mit Startwerten | SYS-02/03; PRD Reliability; A-04 |

## C2 — Ein Kontext, zwei Konsistenzgrenzen

| Kontext / Domain Target Spec | Eigentum / Grenze | Coverage | Logisches Modul |
|---|---|---|---|
| **CTX-FACTORY — Fabrikfortschritt**, Domain Target Spec `BOLTBOTS-DOMAIN-FACTORY-001` in diesem Dokument (§§C1–C3) | Fabrik, Produktion, Cash, Maschinen, Freischaltungen, Gestaltung und temporäre Plotzuordnung; keine Konten, Zahlungen, Helfer-KI oder Plattformverwaltung | `partially_modeled`, bis exakte Human-Entscheidung wirksam | **MOD-FACTORY**, nur fachliche Grenze, keine festgelegte Verzeichnis-, Prozess- oder Deploymentstruktur |

**A-01 — Kontextentscheidung:** Alle Kernänderungen betreffen denselben Besitzer und verzahnen Cash, Maschinen und Freischaltungen. Ein eigener „Economy“- oder „Collection“-Kontext würde ohne unabhängige Sprache/Verantwortung mehrere Transaktionen für denselben Kauf erzeugen. Ein „Persistence“-Kontext wäre eine technische Schicht, kein fachlicher Bereich. Deshalb ein Kontext mit klaren internen Grenzen. Ein Module Entry Map entsteht erst bei Implementation-Readiness nach dem Gate. Belege: UC-IMPROVE/COLLECT/RESUME, PRD SYS-02/04 und ECO-01.

### Elemente und Beziehungen

Alle nachfolgenden Elemente gehören semantisch CTX-FACTORY. Externe IDs sind Referenzen, keine Übernahme fremder Modelle.

| Stabile ID / Art | Verantwortung / Identität | Beziehung mit Kardinalität und Datenumfang | Beleg |
|---|---|---|---|
| **AG-FACTORY**, Aggregate Root Fabrikfortschritt | Ein Konto besitzt genau einen dauerhaften Fortschrittsstand in diesem Horizont; stabile FactoryId, genau ein OwnerAccountId | Owner → Factory 1:1 nach erster erfolgreicher Anlage; davor 0. Factory → Cash genau1, Maschinen 1..n, Freischaltungen 0..5, Ausstellung 0..1 | SYS-01/02; GDD5.1; A-01/03 |
| **EN-MACHINE**, Entity Maschine | Stabile MachineId innerhalb genau einer Factory; Typ, erlaubter Socket und gültiges Upgradelevel | Factory → Machine 1..n nach Initialisierung; Machine → erlaubter Socket genau1; pro Socket höchstens1 Maschine. Starter-Assembler genau1, weitere zulässige Stationen nach Katalog | LOOP-02; GDD5.1/5.3; UC-IMPROVE |
| **EN-UNLOCK**, Entity Freischaltung | Stabile Kombination FactoryId + DesignId; bereits erworbene dauerhafte Designberechtigung | Jede Freischaltung gehört genau1 Factory und genau1 DesignDefinition; keine Duplikate. DesignDefinition → Freischaltungen vieler Fabriken 0..n | LOOP-03; GDD5.4; A-03 |
| **VO-CASH**, Value Object | Endlicher nicht negativer ganzzahliger Betrag innerhalb einer unterstützten Zahlengrenze | Genau1 je Factory; keine globale gemeinsame Kasse | ECO-01/02; SYS-04 |
| **VO-SELECTION**, Value Objects | Aktuelle Produktionsfamilie, erlaubte Farb-/Detailwahl und optionale Ausstellungswahl | Factory → Produktionsauswahl genau1 zulässiges Design; Starter-Scout auch vor erster Freischaltung produzierbar. Ausstellung referenziert0..1 eigene Freischaltung; kein zusätzliches Robotereigentum | LOOP-01/03/04; GDD5.4; A-03 |
| **VO-OUTPUT**, Value Object / flüchtiger Fakt | Produktionsabschluss einer Familie mit eigenem fachlichem Abschlussbezug zur Doppelerkennung | Gehört genau1 Factory und genau1 gestarteter/erlaubter Produktion; kein dauerhaftes Einzelroboterinventar. Sichtbare Effekte dürfen fehlen, Vergütung nicht doppelt erfolgen | LOOP-01; ECO-01; A-03 |
| **AG-PLOTS**, Aggregate Root Sitzungsplätze | Identität einer Weltinstanz; begrenzter Vorrat von Plätzen mit Belegungsstatus | Weltinstanz → Slots1..n; Slot → aktive Zuordnung0..1; Factory → aktive Zuordnung0..1 über alle Sitzungen. Zuordnung enthält nur benötigte Besitzer-/Factoryreferenzen | SYS-01; GDD5.1; A-02/04 |
| **EN-PLOT**, Entity Sitzungsplatz | Stabile SlotId innerhalb genau einer Weltinstanz; temporäre Reservierung/Belegung | AG-PLOTS → EN-PLOT 1..n; EN-PLOT → Factory 0..1; Factory → EN-PLOT 0..1 aktiv | SYS-01; A-02; LC-PLOT |
| **VO-CATALOG**, unveränderliche fachliche Definitionen einer gültigen Version | MachineTypeId/DesignId, erlaubte Sockel, Upgrade-/Freischaltregeln, Kosten/Erträge und zulässige Gestaltung | Definition → verwendende Maschinen/Fabriken0..n; jeder Verweis muss in der verwendeten gültigen Version auflösbar sein. Genau5 Designfamilien im vorgeschlagenen MVP | LOOP-02/03; GDD5.3/5.4; H-BAL |

Der gestartete kostenfreie Zustand enthält den Starter-Assembler und eine zulässige Scout-Produktion. Die erste abgeschlossene Scout-Einheit erteilt dessen Sammlungseintrag; danach können Sammlungs- und Produktionsziele fortschreiten (UC-START/PRODUCE/COLLECT, GDD5.4). „Tutorial“ bezeichnet hier nur nachgewiesene Einstiegsmeilensteine, keine UI-Schrittfolge. Kein neuer Tutorial-Dienst.

### Invarianten, Eigentum und Konsistenz

| ID | Regel / explizit verbotener Zustand | Beleg |
|---|---|---|
| **INV-OWNER** | Nur Owner-Absichten und Systemoperationen innerhalb genau seiner aktiven Fabrik dürfen Fortschritt verändern. Eine Client-FactoryId oder ein Client-Cashbetrag begründet keine Berechtigung. | SYS-01/04; QA-02 |
| **INV-PLOT** | Kein Slot gleichzeitig für zwei Fabriken; kein Fortschritt gleichzeitig in zwei aktiven Schreibern/Sitzungen. Ein Ortswechsel ändert den Owner nicht. Ohne bestätigte Zuordnung keine Produktion. | SYS-01; PRD Security; A-02/04 |
| **INV-CASH** | Cash, Preis, Ertrag und Rate sind gültig, endlich und innerhalb unterstützter Grenzen; Cash niemals negativ. Ein Kauf prüft alle Voraussetzungen und aktualisiert Cash plus gekaufte Wirkung gemeinsam oder gar nicht. | UI-04; ECO-01/02 |
| **INV-ONCE** | Ein identischer Produktionsabschluss oder wiederholter Kaufauftrag wirkt höchstens einmal. Zwei eigenständige Kaufabsichten dürfen nacheinander wirken, aber jeweils nur zum dann gültigen, bestätigten Zustand/Preis; keine doppelte Wirkung einer alten Absicht. | ECO-01; UI-04 |
| **INV-DESIGN** | Freischaltungen sind eindeutig und in diesem Horizont nicht widerrufbar/verbrauchbar. Produktion nur eines erlaubten eigenen Designs, mit Scout-Startausnahme. Ausstellung nur einer eigenen Freischaltung. Kein bezahlter Fortschrittszwang. | LOOP-03/04; UI-03; GDD5.4 |
| **INV-PLACEMENT** | Maschine genau einem erlaubten Socket zugeordnet; keine Überschneidung/Platzierung außerhalb eigener Grenzen. Kein permanenter Verlust durch Fehlklick; Löschen/Verkaufen ist kein Feature dieses Horizonts. | GDD4/5.1; UC-IMPROVE |
| **INV-RECOVERY** | Fehlgeschlagenes/unbekanntes Laden ist nicht „neuer Spieler“. Bestätigter Fortschritt wird nicht mit Defaults überschrieben. Unbestätigte Änderungen werden nie als dauerhaft gespeichert ausgegeben. | SYS-02/03; PRD Reliability; A-04 |
| **INV-READ** | Öffentliche Ansicht enthält nur Fabrikgestaltung, sichtbare Maschinen/Ausstellung und hierfür nötige Besitzerreferenz; keine privaten Kontoinformationen, Speicher-/Sitzungstoken oder vollständigen internen Profile. | SYS-01; UC-VIEW; A-05 |

**Transaktionsgrenzen:** AG-FACTORY fasst Cashänderung, erworbene Maschine/Level oder Design und zugehörige Fortschrittsänderung in einer fachlich unteilbaren Änderung zusammen. Der Abschluss einer Produktion vergütet höchstens einmal und kann den dadurch erfüllten Einstiegs-/Freischaltmeilenstein gemeinsam setzen. Preis-/Levelgrenzen werden innerhalb derselben Entscheidung geprüft. Ein 3D-Effekt gehört nicht zu dieser Transaktion (INV-CASH/ONCE/DESIGN).

AG-PLOTS schützt die exklusive Slotbelegung. Eintritt reserviert erst exklusiv Besitzer/Slot, lädt oder legt den Fortschritt sicher an und aktiviert Produktion erst nach beiden Erfolgen; bei Fehlschlag wird die Reservierung wieder freigegeben. Verlassen stoppt zunächst Produktion und neue Mutationen, sichert den Stand und gibt die Platzbelegung frei. Ein unsicherer Speicher-/Schreiberstatus darf bei Wiederbeitritt keinen zweiten unabhängigen Fortschrittszweig erzeugen. Die konkrete koordinierte Speicher-/Sperrtechnik bleibt nachgelagert; die Invariante und Fehlerentscheidung stehen fest (A-02/04, UC-START/RESUME).

### Context Map und öffentliche fachliche Grenze

| Richtung | Übergebene Bedeutung / Übersetzung | Verantwortung bei Fehler / Nicht-Eigentum |
|---|---|---|
| EXT-CLIENT → CTX-FACTORY | Absicht „verbessern“, „freischalten“, „gestalten“; Serverkontext übersetzt authentifizierten Akteur und prüft Werte/Owner/aktuellen Zustand | Factory lehnt ab; keine Zustandsänderung bei unerlaubter/veralteter Absicht. Client besitzt weder Preise noch Erträge. |
| CTX-FACTORY → EXT-CLIENT | Eigene Fortschrittsansicht, erlaubte öffentliche Fabrikansicht und Erfolg/Ablehnung | Darstellung kann wiederholt aufgebaut werden; kein eigener Wirtschaftszustand im Renderer. Animation ist kein Beweis einer gespeicherten Änderung. |
| CTX-FACTORY → EXT-ROBLOX-IDENTITY | Benötigte vertrauenswürdige AccountId/Sitzungsidentität aus Plattformkontext verwenden | Keine lokale Konto-/Passwortverwaltung; ungeklärte Identität aktiviert keine Fabrik. |
| CTX-FACTORY ↔ EXT-STORE | Bestätigten Fortschritt laden/sichern; Übersetzung von Speicherfehlern in fachlich lesbare Verfügbarkeit | Factory besitzt INV-RECOVERY, Speicheradapter später Format/Transport/Versionsmigration. Kein Datenschema oder API-Kontrakt hier. |

Es gibt **keinen In-Horizon-Verkehr zwischen verschiedenen Bounded Contexts**. AG-FACTORY und AG-PLOTS sind interne Konsistenzgrenzen desselben Kontexts. Plattform, Client und Speicher sind externe/technische Nachbarn, keine aus Bequemlichkeit abgespaltenen Domänen. Quelle: A-01, UC-START/RESUME/VIEW.

## C3 — Verhalten, Berechtigungen und Auswirkungen

### Fachliche Lebenszyklen

| ID / Gegenstand | Zustand → erlaubter Übergang / Initiator und Guard | Wirkung / verweigerter Übergang | Beleg |
|---|---|---|---|
| **LC-FACTORY** / Zugriff auf Fortschritt | nicht geladen → wird geladen, System bei authentifiziertem Eintritt und exklusiver Reservierung; wird geladen → aktiv nur bei eindeutigem bestätigtem Stand/neuer erfolgreicher Anlage | Fehler → nicht verfügbar; keine Defaultproduktion auf Ladefehler | UC-START; INV-PLOT/RECOVERY |
| LC-FACTORY | aktiv → wird gesichert, System bei Checkpoint/Verlassen; bestätigt → aktiv oder beendet nach Verlassen | Bei unbestätigtem Speicherfehler → Sicherung ausstehend; Stand und Fehlermeldung erhalten, neue Fortschrittsmutationen pausieren, begrenzter Wiederholversuch möglich. Erfolg → aktiv/beendet. Endgültiger Fehler → nicht verfügbar; kein Erfolg vortäuschen. | UC-RESUME; A-04 |
| **LC-PLOT** | frei → reserviert → aktiv → frei; System mit exklusiver Zuordnung und abgeschlossenem Eintritt/Verlassen | Reservierungsfehler/Abbruch → frei; aktiv → zweiter Besitzer verboten | UC-START/RESUME; INV-PLOT |
| **LC-MACHINE** | nicht vorhanden → platziert, System beim Starter oder Owner bei gültigem Kauf; Level n → n+1, Owner mit gültigem Cash/aktuellem Preis und unter Maximallevel | Keine Sprünge, negative Level, Überschneidung oder bezahlter Kauf bei erreichter Obergrenze; kein Verlust-/Verkaufszustand | UC-IMPROVE; INV-CASH/PLACEMENT |
| **LC-DESIGN** | gesperrt → freigeschaltet; System bei bekanntem Meilenstein oder Owner bei gültigem freigegebenem Kauf samt Voraussetzungen | Freigeschaltet bleibt freigeschaltet; doppelte Wiederholung ohne zweiten Cashabzug. Unbekannte ID oder fehlende Voraussetzung abgelehnt | UC-COLLECT; INV-DESIGN/ONCE |
| **LC-PRODUCTION** | bereit → laufend → abgeschlossen, System mit aktiver Fabrik, gültiger Familie und Rate | Abschluss führt genau einmal zur Vergütung; Abbruch bei Ende/Verlust aktiver Sitzung vor Abschluss ohne nachträglichen Ertrag. Kein Offline-Fortschreiben | UC-PRODUCE; D-01; INV-ONCE |
| **LC-DISPLAY** | leer → gültige eigene Freischaltung → andere gültige eigene Freischaltung oder leer, Owner | Wechsel verbraucht weder Design noch Cash; fremde/gesperrte Auswahl abgelehnt | UC-EXPRESS; LOOP-04 |

Katalogdefinitionen und Cash als Betrag besitzen keinen eigenständigen spielseitigen Objektlebenszyklus (`not_applicable`); ihr Bearbeiten durch Entwickler ist kein Spielerprozess. Katalogversionierung und Datenmigration werden später als technische/inhaltliche Änderung unter Domain-Impact geprüft (LOOP-02, SYS-03).

### Befehle, Anfragen und Rechte

- **CMD-JOIN/LEAVE/SAVE**, nur System im vertrauenswürdigen Sitzungsbezug: UC-START/RESUME; Gate LC-FACTORY/LC-PLOT. Fehler verhindert Aktivierung bzw. bestätigt kein erfolgreiches Speichern.
- **CMD-COMPLETE**, nur System: UC-PRODUCE; nur tatsächlich fälliger Abschluss einer erlaubten aktiven Produktion. Clientmeldungen über Cash oder „fertig“ sind niemals Vergütungsautorität.
- **CMD-BUY-MACHINE / CMD-UPGRADE / CMD-UNLOCK**, Owner seiner Factory: UC-IMPROVE/COLLECT; prüfen Absicht, Owner, Voraussetzungen, Cash, aktuelle Definition/Preis und Wiederholung. Ablehnung lässt Cash und erworbene Rechte unverändert.
- **CMD-SELECT-PRODUCTION / CMD-CUSTOMIZE / CMD-SET-DISPLAY**, Owner: UC-COLLECT/EXPRESS; nur erlaubte eigene Auswahl und gültige Inhalte. Keine Änderung fremder Fabrik, auch wenn deren ID bekannt ist.
- **Q-OWN-PROGRESS**, nur Owner: Cash, eigene Maschinen/Designs, aktuelles Ziel und Sicherungsstatus; **Q-PUBLIC-FACTORY**, Viewer in sichtbarer Welt: begrenzte öffentliche Ansicht gemäß INV-READ; **Q-CATALOG**, Spieler: bekannte kostenlose Inhalte/Voraussetzungen. Kein Zugriff auf interne Speicher-/Sitzungsdaten. Alle Denials sind sichtbar/rückmeldbar, kein scheinbarer erfolgreicher Kauf.

Dies sind fachliche Operationen, noch keine festgelegten Remote-Namen, Schemas, Screens oder Interaktionsabläufe.

### First-Class-Entscheidungen

| Entscheidung | Begründung / Aufgaben und unabhängige Rechte | Grenze / Beleg |
|---|---|---|
| **FC-FACTORY: ja**, persönliche Fabrik | Stabile Identität, dauerhafter Fortschritt, Besitzer-/Viewer-Unterscheidung, eigenständig fortsetzen und gestalten | Nicht automatisch eigene Seite/Service. UC-START/EXPRESS/VIEW; AG-FACTORY |
| **FC-MACHINE: ja**, platzierte Maschine | Stabile MachineId, Kauf-/Upgradelebenszyklus, gezielt verbessern; nur Besitzer darf die konkrete Maschine ändern | Entity innerhalb Factory, kein zusätzlicher Aggregate Root nötig. UC-IMPROVE; EN-MACHINE |
| **FC-DESIGN: ja**, sammelbares Design | Stabile DesignId, gesperrt/freigeschaltet pro Besitzer; gezielt erwerben, auswählen, ausstellen; Auswahlrecht hängt vom eigenen Besitz ab | First-Class-Sammelgegenstand ist das Design, nicht ein produziertes Einzelstück; gemeinsame Definition plus besitzerspezifische Freischaltung. UC-COLLECT/EXPRESS; EN-UNLOCK |
| **FC-PLOT: nein** | Nur zugewiesener Sitzungsplatz, kein unabhängiger dauerhafter Besitz-/Verwaltungsprozess | AG-PLOTS trotzdem eigene Konsistenzgrenze; First-Class ≠ Aggregate. A-02 |
| **FC-CASH / FC-OUTPUT / FC-DISPLAY: nein** | Betrag, flüchtiger Abschluss bzw. Auswahlwert haben keinen unabhängigen Verwaltungslebenszyklus | Keine Wallet-, Einzelroboter- oder Sockelverwaltung erfinden. A-03; UC-PRODUCE/EXPRESS |
| **FC-ACCOUNT / FC-TUTORIAL: nein im Produkt** | Roblox verwaltet Konto; Einstiegsmeilensteine sind Factory-Fortschritt | Kein paralleles Identity-/Quest-System. C1; UC-START/COLLECT |

### Szenarien: positiv, negativ und an Grenzen

| ID | Konkretes Beispiel und erwartetes fachliches Ergebnis | Trace |
|---|---|---|
| SC-01 | Neuer authentifizierter Spieler, Platz frei, eindeutig kein gespeicherter Stand: kostenlose Fabrik/Assembler/Scout-Produktion; erster echter Abschluss gibt einmal Cash und Scout-Freischaltung. | UC-START/PRODUCE; INV-OWNER/ONCE; LC-FACTORY/DESIGN |
| SC-02 | Besitzer hat genau den aktuellen Upgradepreis: Kauf erhöht genau eine Maschine um ein Level und reduziert Cash auf0. Einen Cash weniger: keinerlei Änderung. | UC-IMPROVE; INV-CASH; CMD-UPGRADE |
| SC-03 | Derselbe Kaufauftrag wird doppelt gesendet oder nach unklarer Antwort erneut versucht: maximal eine Wirkung. Zwei andere gleichzeitige Absichten auf alten Preis/Level können nicht beide dieselbe veraltete Kaufentscheidung erzwingen. | INV-ONCE/CASH; ECO-01 |
| SC-04 | Spieler A sendet gültige MachineId von B: abgelehnt. A sieht Bs öffentliche Ausstellung, aber keine privaten internen Profildaten und kann nichts platzieren. | UC-VIEW/IMPROVE; INV-OWNER/READ |
| SC-05 | Ein Design ist gesperrt: Produktions-/Ausstellungswahl verweigert. Nach gültiger Freischaltung nutzbar, wiederholte Freischaltung ohne doppelten Abzug; Farbwechsel nimmt nichts weg. | UC-COLLECT/EXPRESS; INV-DESIGN |
| SC-06 | Platzkapazität erreicht oder zwei Spieler konkurrieren um letzten Slot: höchstens eine erfolgreiche Zuordnung; anderer bleibt ohne aktive Produktion, fremde Fabriken unverändert. | UC-START; INV-PLOT; LC-PLOT |
| SC-07 | Erneuter Login während altem aktiven/ungeklärten Schreiber: keine zweite Fortschrittskopie. Nach geklärtem Abschluss gleicher dauerhafter Besitzerstand auf beliebigem freien Slot. | INV-PLOT/RECOVERY; A-02/04 |
| SC-08 | Laden schlägt fehl: keine neue Startfabrik speichern. Sichern schlägt fehl: „ausstehend“, Mutationen pausiert; Erfolg/Fehler eindeutig; Wiederbeitritt überschreibt nie bestätigten Stand durch Defaults. | UC-RESUME; LC-FACTORY; INV-RECOVERY |
| SC-09 | Falsche ID, unzulässiger Socket, Maximallevel, negativer/NaN-/überlaufender Betrag oder ungültige Rate: verweigert, ohne Cash-/Maschinenänderung. | ECO-02; INV-CASH/PLACEMENT; CMD-BUY-MACHINE |
| SC-10 | Animation fehlt oder Client trennt Verbindung: fehlende Darstellung erzeugt keinen zweiten Ertrag. Bei Verlassen vor fachlichem Abschluss kein nachträglicher Offline-Ertrag. | UC-PRODUCE; LC-PRODUCTION; INV-ONCE |
| SC-11 | Letzte bekannte Familie freigeschaltet: Sammlung vollständig; keine weitere kostenpflichtige Pflichtstufe, kein Prestige-/Weltwechsel aus Mockups ableiten. | UC-COLLECT; LOOP-05; UI-03; D-02 |

Diese Szenarien sind Prüfanforderungen, keine durchgeführten Softwaretests.

## Explizite Vorschläge und verbleibende Hypothesen

Alle A-/D-Entscheidungen gehören dieser vorgeschlagenen Revision und werden nur mit deren Human-Freigabe wirksam. A-01 bis A-05 sind oben vollständig ausgeführt; ihre Eigentümerin ist Human Product Authority.

| ID | Empfehlung / konkreter Quellenkonflikt | Echte Alternative und Folge |
|---|---|---|
| **D-01** | Automatische Cash-Gutschrift bei verpacktem Abschluss; kein Ansammeln unbezahlter Pickups. PRD LOOP-01 sagt Verpackungsreward, GDD5.2 Cash-Pickup, CODE vergütet automatisch. | Manuelles Einsammeln: zusätzlicher ungelöster Ertragsvorrat, Abhol-/Abbruch-/Speicherregeln und Spielhandlung nötig. Weniger Leerlauf ist nur eine erwartete Wirkung automatischer Gutschrift, später spielerisch prüfen. |
| **D-02** | Kein Blueprint-XP im Horizont. Freischaltungen durch bekannte Meilensteine und ggf. Factory-Cash-Käufe, ohne weitere Währung. GDD4/5.3 erwähnt XP, liefert aber keine vollständige Regel; PRD LOOP-03/05 benötigt es nicht. | XP behalten: eigenen Fortschrittswert, Vergabe-/Ausgabebedeutung und Verhältnis zu Cash/Meilensteinen festlegen. Mehr Erklärung/Balancing; nicht einfach aus HUD-Diamanten ableiten. |
| **D-03** | Orbit-Bedingung „Fabriklevel2“ auf Level2 des Starter-Assemblers beziehen. Das nutzt das bereits belegte Upgradeobjekt ohne globales neues Fabriklevel. | Eigenes Fabriklevel: zusätzliche Definition, Berechnung, Fortschrittsübergänge und Abgrenzung zu Maschinenlevel erforderlich. Andere Orbit-Bedingung wäre ebenfalls Änderung dieser Entscheidung. |

**A-02** trennt dauerhafte Factory von Sitzungsplot (Identität/Resume-Lücke). **A-03** trennt Sammeldesign von Produktionsoutput (Inventarbedeutung). **A-04** setzt exklusiven Schreiber, ehrliche Speichersicherung und Pause bei unbestätigtem Fehler (Reliability-/Parallelzugriffslücke). **A-05** begrenzt öffentliche Sicht auf für die Darstellung nötige Daten (Privacy-/Viewer-Lücke). Ihre Konsequenzen stehen in C2/C3; keine verdeckten Grundsatzentscheidungen für später.

| Nicht fundamentale Resthypothese / Owner | Auflösungsauslöser und Grenze |
|---|---|
| **H-BAL — Product Authority**, mit Agenten-Balancing-/Spieltestbelegen | Nach Domain-Gate vor ausführbarer Wirtschaft: konkrete Cashpreise, Erträge, Raten, Levelgrenzen und Luma-/Atlas-Meilensteinwerte. Regeln bleiben deterministisch, erreichbar ohne Robux und innerhalb der modellierten Maschinen-/Design-/Einstiegsmeilensteine; neuer Fortschrittstyp erfordert Domain-Impact. |
| **H-CAP — Technical Lead**, Human entscheidet Qualität | Vor erstem Mehrspielernachweis: gemessene Spieler-/Slotgrenze statt bloßer1–4-Annahme; eindeutige Kapazitätsablehnung bleibt Pflicht. |
| **H-SAVE — Technical Lead** | Nach Gate vor Persistenzumsetzung: konkretes Fehler-/Wiederhol-/Recovery-Verfahren, maximal unbestätigtes Zeitfenster und Benutzerfeedback. INV-PLOT/RECOVERY und Pause bei ungeklärter Sicherung dürfen nicht aufgeweicht werden. |
| **H-LOOK — Human Product Authority** | Erster visueller Meilenstein: tatsächliche Szene mit Bauteilroboter prüfen, danach Verfeinerung. Namen, Farben, Formen, Animation und Werkzeugwahl sind nicht durch Konzeptbilder endgültig gebunden. |
| **H-AUTO — Lead**, Human beurteilt Ergebnis | Vor jeweiliger Werkzeug-/Spieltestaufgabe: Codex-Bedienbarkeit und echte Ausführung nachweisen; insbesondere Studio und mögliches Blender. Fehlende Fähigkeit offenlegen, keine manuelle Produktionsarbeit stillschweigend auf den Human verlagern. |

## Folgen für die spätere Ausarbeitung

- **MVP und Planung:** Diese Semantik begrenzt den späteren detaillierten Umfang. Setup, erster laufender Produktionskreislauf und visuelle Referenzszene samt Agent-Spieltest werden im ersten Meilenstein ausgearbeitet; dieser Run erzeugt noch keine Slices oder Implementierungspläne.
- **Architektur und Verträge:** Ein fachliches Modul genügt voraussichtlich. Separate Clients/Server/Speicheranbindung müssen die vorhandenen Vertrauensgrenzen wahren; kein Microservice-Vorschlag. Öffentliche Daten und Fehlerentscheidungen leiten sich aus C2/C3 ab, ihre Schemas folgen später.
- **Persistenz/Migration:** Owner, Cash, Maschinen/Socketbezüge, Freischaltungen und Auswahl müssen fortsetzbar sein; der physische Sitzungsplot ist flüchtig. Kein Datenbankschema hier. Ein Prototyp mit nur Arbeitsspeicher erfüllt SYS-02/03 noch nicht; es gibt keine nachgewiesenen bestehenden Produktionsdaten, die stillschweigend migriert werden dürften.
- **UX/Qualität/Sicherheit:** Erwerb, Ablehnung und Speicherstatus müssen verständlich sein; kein Farbe-allein-Feedback und kein Erfolgsversprechen auf bloßer Animation. Tatsächliche Studio-/Mobil-/Mehrspielerbelege und Assetrechteprüfung bleiben spätere Abnahmepflichten. Diagrammstruktur ist kein Beleg für Spielqualität.

## Gebundene Kontextansicht

Die [Diagrammquelle](diagrams/context-map.json), der [kleine lokale Generator](diagrams/render_context.py) und die [SVG-Ansicht](diagrams/context-map.svg) bilden genau diese Revision ab. Die Textdefinition bleibt Eigentümer der Semantik. Generatoridentität und Hashes folgen im maschinenlesbaren Bindungsblock. Struktur, vollständiger Text und reproduzierbare Bytes werden geprüft; eine optische Sichtprüfung wird mangels verfügbarem unterstütztem lokalen Renderer nicht behauptet.

<!-- domain-foundation:start -->
```json
{
  "schema_version": "1",
  "foundation_id": "BOLTBOTS-DOMAIN-FOUNDATION-001",
  "revision": 1,
  "revision_status": "in_review",
  "effectiveness": "pending_human_decision",
  "horizon": {
    "mvp": "Eine Welt, eine persönliche Fabrik je Spieler, eine Produktionskette, fünf sammelbare Designs, kostenlose Gestaltung und bestätigter fortsetzbarer Fortschritt.",
    "six_week": "Derselbe fachliche Horizont für die ersten sechs Entwicklungswochen; Umfang und Termine noch kein Liefervertrag, erster Nachweis gemäß HUM kleiner."
  },
  "contexts": [
    {
      "id": "CTX-FACTORY",
      "name": "Fabrikfortschritt",
      "coverage": "partially_modeled",
      "domain_spec": "docs/domains/domain-foundation.md",
      "logical_module": "MOD-FACTORY"
    }
  ],
  "diagram": {
    "source": "docs/domains/diagrams/context-map.json",
    "render": "docs/domains/diagrams/context-map.svg",
    "generator": "render_context.py v1; Python3 standard library; generator SHA256 9b1affac326e873444dc563e87dcc40cdb91bfb7268de4dac8381801c275816c",
    "source_sha256": "6d62efbcd900445b25199360e7ed00b6d49125da8550b22c4e2bbaa437204b20",
    "render_sha256": "38e303d688c63442f61a1b88508cc36cd2102987f5f21ff30c9e9bfb55814eca"
  },
  "open_decisions": [
    "D-01: automatische Gutschrift statt manuellem Cash-Pickup, Empfehlung zur Human-Bestätigung",
    "D-02: keine zusätzliche Blueprint-XP im Horizont, Empfehlung zur Human-Bestätigung",
    "D-03: Orbit-Voraussetzung Starter-Assembler Level2 statt neuem Fabriklevel, Empfehlung zur Human-Bestätigung"
  ],
  "review_ref": "BOLTBOTS-DOMAIN-REVIEW-001",
  "human_decision_ref": "BOLTBOTS-DOMAIN-REVIEW-001"
}
```
<!-- domain-foundation:end -->

Das [Review-/Entscheidungspaket](../reviews/20261024-1.5.3-boltbots-domain-foundation-review.md) bindet die exakten Kandidatenbytes. Keine Domain-Wirksamkeit vor der dort dokumentierten Human-Entscheidung. Bei Änderung von Kontext, Eigentum, Kardinalität, Invariante, Lifecycle, Berechtigung oder First-Class-Entscheidung folgt ein Domain-Impact mit neuer exakter Review-/Humanbindung.

## Strukturierter Kontextindex

Dieser Block indexiert die oben definierten Bedeutungen im selben Eigentümerdokument; er schafft keine weiteren Objekte oder Freigaben.

<!-- domain-context:start -->
```json
{
  "schema_version": "1",
  "context_id": "CTX-FACTORY",
  "foundation_id": "BOLTBOTS-DOMAIN-FOUNDATION-001",
  "foundation_revision": 1,
  "status": "draft",
  "implementation_readiness": "modeled",
  "module_entry": "not_required",
  "review_ref": "BOLTBOTS-DOMAIN-REVIEW-001",
  "elements": [
    {
      "id": "AG-FACTORY",
      "kind": "aggregate_root",
      "responsibility": "Dauerhafter Besitzerfortschritt; siehe C2",
      "aggregate": "AG-FACTORY",
      "ownership": "genau ein OwnerAccountId",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-SYSTEM/ACT-OWNER gemäß LC-FACTORY",
      "trace_refs": [
        "UC-START",
        "A-01"
      ]
    },
    {
      "id": "EN-MACHINE",
      "kind": "entity",
      "responsibility": "Platzierte Maschine mit stabiler MachineId",
      "aggregate": "AG-FACTORY",
      "ownership": "Owner der Factory",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-SYSTEM/ACT-OWNER gemäß LC-MACHINE",
      "trace_refs": [
        "UC-IMPROVE"
      ]
    },
    {
      "id": "EN-UNLOCK",
      "kind": "entity",
      "responsibility": "Designberechtigung FactoryId+DesignId",
      "aggregate": "AG-FACTORY",
      "ownership": "Owner der Factory",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-SYSTEM/ACT-OWNER gemäß LC-DESIGN",
      "trace_refs": [
        "UC-COLLECT",
        "A-03"
      ]
    },
    {
      "id": "VO-CASH",
      "kind": "value_object",
      "responsibility": "Einziger nicht negativer Cashbetrag",
      "aggregate": "AG-FACTORY",
      "ownership": "Owner der Factory",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "not_applicable: Wert; Änderungen gemäß INV-CASH",
      "trace_refs": [
        "UC-IMPROVE",
        "UC-PRODUCE"
      ]
    },
    {
      "id": "VO-SELECTION",
      "kind": "value_object",
      "responsibility": "Produktions-, Gestaltungs- und optionale Ausstellungswahl",
      "aggregate": "AG-FACTORY",
      "ownership": "Owner der Factory",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-OWNER; Auswahl gemäß INV-DESIGN/LC-DISPLAY",
      "trace_refs": [
        "UC-EXPRESS"
      ]
    },
    {
      "id": "VO-OUTPUT",
      "kind": "value_object",
      "responsibility": "Flüchtiger echter Produktionsabschluss, kein Inventarobjekt",
      "aggregate": "AG-FACTORY",
      "ownership": "Owner der Factory",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-SYSTEM gemäß LC-PRODUCTION",
      "trace_refs": [
        "UC-PRODUCE",
        "A-03"
      ]
    },
    {
      "id": "AG-PLOTS",
      "kind": "aggregate_root",
      "responsibility": "Exklusive Sitzungsplatzbelegung",
      "aggregate": "AG-PLOTS",
      "ownership": "Weltinstanz, Zuordnung nur System",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-SYSTEM gemäß LC-PLOT",
      "trace_refs": [
        "UC-START",
        "A-02"
      ]
    },
    {
      "id": "EN-PLOT",
      "kind": "entity",
      "responsibility": "SlotId mit höchstens einer aktiven Fabrikzuordnung",
      "aggregate": "AG-PLOTS",
      "ownership": "Weltinstanz, temporär zugewiesene Factory",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-SYSTEM gemäß LC-PLOT",
      "trace_refs": [
        "UC-START",
        "A-02"
      ]
    },
    {
      "id": "VO-CATALOG",
      "kind": "value_object",
      "responsibility": "Gültige Definitionen/DesignIds, keine Kontodaten",
      "aggregate": "not_applicable: gemeinsame Definitionen",
      "ownership": "Product Authority; lesbar für Spieler",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "not_applicable: kein Spielerprozess, versionierte Inhalte",
      "trace_refs": [
        "UC-COLLECT",
        "H-BAL"
      ]
    },
    {
      "id": "EXT-ROBLOX-IDENTITY",
      "kind": "external_concept",
      "responsibility": "Vertrauenswürdige AccountId",
      "aggregate": "not_applicable: Roblox",
      "ownership": "Roblox",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "not_applicable: außerhalb Produktverwaltung",
      "trace_refs": [
        "UC-START"
      ]
    },
    {
      "id": "EXT-STORE",
      "kind": "external_concept",
      "responsibility": "Dauerhafter bestätigter Fortschritt",
      "aggregate": "not_applicable: externer Speicher",
      "ownership": "Factory besitzt Semantik, Transport nachgelagert",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "ACT-SYSTEM gemäß INV-RECOVERY",
      "trace_refs": [
        "UC-RESUME"
      ]
    },
    {
      "id": "EXT-CLIENT",
      "kind": "external_concept",
      "responsibility": "Absicht und erlaubte Darstellung",
      "aggregate": "not_applicable: Darstellung",
      "ownership": "Je angemeldetem Spieler",
      "tenancy": "Owner-skopiert nach C2; gemeinsame Definitionen/Weltinstanz und externe Systeme nur im dort genannten Datenumfang",
      "lifecycle_authority": "not_applicable: keine autoritative Fortschrittsinstanz",
      "trace_refs": [
        "UC-VIEW"
      ]
    }
  ],
  "relationship_disposition": "modeled",
  "relationships": [
    {
      "id": "REL-OWNER",
      "from": "EXT-ROBLOX-IDENTITY",
      "from_cardinality": "one",
      "semantics": "besitzt nach Anlage genau eine Factory; davor0",
      "to": "AG-FACTORY",
      "to_cardinality": "zero_or_one",
      "boundary": "externe Identität, INV-OWNER",
      "trace_refs": [
        "UC-START",
        "A-01"
      ]
    },
    {
      "id": "REL-MACHINES",
      "from": "AG-FACTORY",
      "from_cardinality": "one",
      "semantics": "enthält genau einen Starter und erlaubte weitere Maschinen",
      "to": "EN-MACHINE",
      "to_cardinality": "one_or_more",
      "boundary": "atomarer Factory-Fortschritt",
      "trace_refs": [
        "UC-IMPROVE"
      ]
    },
    {
      "id": "REL-UNLOCKS",
      "from": "AG-FACTORY",
      "from_cardinality": "one",
      "semantics": "besitzt0..5 eindeutige Designfreischaltungen",
      "to": "EN-UNLOCK",
      "to_cardinality": "zero_or_more",
      "boundary": "atomarer Factory-Fortschritt",
      "trace_refs": [
        "UC-COLLECT",
        "A-03"
      ]
    },
    {
      "id": "REL-CASH",
      "from": "AG-FACTORY",
      "from_cardinality": "one",
      "semantics": "enthält genau einen Cashbetrag",
      "to": "VO-CASH",
      "to_cardinality": "one",
      "boundary": "INV-CASH",
      "trace_refs": [
        "UC-PRODUCE",
        "UC-IMPROVE"
      ]
    },
    {
      "id": "REL-SELECTION",
      "from": "AG-FACTORY",
      "from_cardinality": "one",
      "semantics": "enthält Produktions-/Gestaltungsauswahl, darin Ausstellung0..1",
      "to": "VO-SELECTION",
      "to_cardinality": "one",
      "boundary": "INV-DESIGN",
      "trace_refs": [
        "UC-EXPRESS"
      ]
    },
    {
      "id": "REL-OUTPUT",
      "from": "AG-FACTORY",
      "from_cardinality": "one",
      "semantics": "erzeugt flüchtige Produktionsabschlüsse",
      "to": "VO-OUTPUT",
      "to_cardinality": "zero_or_more",
      "boundary": "INV-ONCE",
      "trace_refs": [
        "UC-PRODUCE"
      ]
    },
    {
      "id": "REL-SLOTS",
      "from": "AG-PLOTS",
      "from_cardinality": "one",
      "semantics": "enthält begrenzte Zahl von Slots",
      "to": "EN-PLOT",
      "to_cardinality": "one_or_more",
      "boundary": "exklusive Weltinstanzbelegung",
      "trace_refs": [
        "UC-START",
        "A-02"
      ]
    },
    {
      "id": "REL-OCCUPANCY",
      "from": "EN-PLOT",
      "from_cardinality": "zero_or_one",
      "semantics": "zugeordnet; je Slot0..1Factory und jeFactory0..1aktiverSlot",
      "to": "AG-FACTORY",
      "to_cardinality": "zero_or_one",
      "boundary": "interne Aggregate, INV-PLOT",
      "trace_refs": [
        "UC-START",
        "A-02",
        "A-04"
      ]
    },
    {
      "id": "REL-DEFINITIONS",
      "from": "VO-CATALOG",
      "from_cardinality": "one",
      "semantics": "eine gültige Katalogfassung informiert viele Factory-Stände",
      "to": "AG-FACTORY",
      "to_cardinality": "zero_or_more",
      "boundary": "Definitionen nicht durch Spieler schreibbar",
      "trace_refs": [
        "H-BAL",
        "UC-COLLECT"
      ]
    },
    {
      "id": "REL-STORE",
      "from": "AG-FACTORY",
      "from_cardinality": "zero_or_more",
      "semantics": "lädt/sichert bestätigten eigenen Fortschritt über gemeinsame Speicherfähigkeit",
      "to": "EXT-STORE",
      "to_cardinality": "one",
      "boundary": "Anti-Corruption: Speicherstatus→LC-FACTORY, kein interner Formatdurchgriff",
      "trace_refs": [
        "UC-RESUME",
        "A-04"
      ]
    },
    {
      "id": "REL-CLIENT",
      "from": "EXT-CLIENT",
      "from_cardinality": "zero_or_more",
      "semantics": "sendet Absichten für eigene oder liest öffentliche Factory-Ansicht; aktuelle Sichtbezüge",
      "to": "AG-FACTORY",
      "to_cardinality": "zero_or_more",
      "boundary": "INV-OWNER/READ, keine Client-Cashautorität",
      "trace_refs": [
        "UC-IMPROVE",
        "UC-VIEW"
      ]
    }
  ],
  "invariants": [
    {
      "id": "INV-OWNER",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-OWNER",
      "failure_or_denial": "Gemäß INV-OWNER und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-IMPROVE",
        "UC-VIEW"
      ]
    },
    {
      "id": "INV-PLOT",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-PLOT",
      "failure_or_denial": "Gemäß INV-PLOT und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-START",
        "A-02",
        "A-04"
      ]
    },
    {
      "id": "INV-CASH",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-CASH",
      "failure_or_denial": "Gemäß INV-CASH und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-IMPROVE",
        "UC-PRODUCE"
      ]
    },
    {
      "id": "INV-ONCE",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-ONCE",
      "failure_or_denial": "Gemäß INV-ONCE und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-PRODUCE",
        "UC-IMPROVE"
      ]
    },
    {
      "id": "INV-DESIGN",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-DESIGN",
      "failure_or_denial": "Gemäß INV-DESIGN und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-COLLECT",
        "UC-EXPRESS"
      ]
    },
    {
      "id": "INV-PLACEMENT",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-PLACEMENT",
      "failure_or_denial": "Gemäß INV-PLACEMENT und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-IMPROVE"
      ]
    },
    {
      "id": "INV-RECOVERY",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-RECOVERY",
      "failure_or_denial": "Gemäß INV-RECOVERY und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-RESUME",
        "A-04"
      ]
    },
    {
      "id": "INV-READ",
      "rule": "Vollständige normative Regel: C2, Invarianten, INV-READ",
      "failure_or_denial": "Gemäß INV-READ und zugehörigem C3-Szenario; ungültige Änderung verweigern, unbestätigte Sicherung sichtbar halten.",
      "trace_refs": [
        "UC-VIEW",
        "A-05"
      ]
    }
  ],
  "use_cases": [
    {
      "id": "UC-START",
      "actor_or_role": "ACT-OWNER/ACT-SYSTEM",
      "permission_boundary": "eigener Fortschritt, exklusiver Plot",
      "preconditions": "Identität und freier Platz; eindeutiger bestätigter Stand",
      "success": "Factory aktiv",
      "failure_or_denial": "Keine Ersatzfabrik auf Fehler",
      "first_class_disposition": "FC-FACTORY ja; FC-PLOT nein",
      "trace_refs": [
        "A-02",
        "A-04",
        "PRD SYS-01/02"
      ]
    },
    {
      "id": "UC-PRODUCE",
      "actor_or_role": "ACT-SYSTEM",
      "permission_boundary": "eigene aktive Factory",
      "preconditions": "Gültige laufende Produktion, echter Abschluss",
      "success": "Einmalige Gutschrift",
      "failure_or_denial": "Kein Ertrag auf Clientbehauptung/Abbruch",
      "first_class_disposition": "FC-OUTPUT nein",
      "trace_refs": [
        "PRD LOOP-01",
        "D-01"
      ]
    },
    {
      "id": "UC-IMPROVE",
      "actor_or_role": "ACT-OWNER",
      "permission_boundary": "eigene Maschine/Factory",
      "preconditions": "Cash, Platz, Preis, Level gültig",
      "success": "Kaufwirkung und Abzug gemeinsam",
      "failure_or_denial": "Alle unverändert bei Ablehnung",
      "first_class_disposition": "FC-MACHINE ja",
      "trace_refs": [
        "PRD LOOP-02",
        "PRD ECO-01"
      ]
    },
    {
      "id": "UC-COLLECT",
      "actor_or_role": "ACT-OWNER/ACT-SYSTEM",
      "permission_boundary": "eigene Freischaltung",
      "preconditions": "Katalogbedingung erfüllt",
      "success": "Designberechtigung dauerhaft",
      "failure_or_denial": "Unbekannte/unerfüllte Auswahl abgelehnt",
      "first_class_disposition": "FC-DESIGN ja",
      "trace_refs": [
        "PRD LOOP-03/05",
        "D-02",
        "D-03"
      ]
    },
    {
      "id": "UC-EXPRESS",
      "actor_or_role": "ACT-OWNER",
      "permission_boundary": "eigene Factory",
      "preconditions": "Zulässige Gestaltung/eigenes Design",
      "success": "Auswahl gesichert",
      "failure_or_denial": "Kein Verbrauch; fremde/gesperrte Auswahl verweigert",
      "first_class_disposition": "FC-FACTORY/DESIGN ja; FC-DISPLAY nein",
      "trace_refs": [
        "PRD LOOP-04"
      ]
    },
    {
      "id": "UC-VIEW",
      "actor_or_role": "ACT-VIEWER",
      "permission_boundary": "öffentliche Teilansicht",
      "preconditions": "Sichtbare Factory",
      "success": "Begrenzte lesbare Ansicht",
      "failure_or_denial": "Keine Schreib-/privaten Datenrechte",
      "first_class_disposition": "FC-FACTORY ja",
      "trace_refs": [
        "A-05",
        "PRD SYS-01"
      ]
    },
    {
      "id": "UC-RESUME",
      "actor_or_role": "ACT-OWNER/ACT-SYSTEM",
      "permission_boundary": "bestätigter eigener Stand",
      "preconditions": "Exklusiver Schreiber/zugehörige Sicherung",
      "success": "Bestätigter Stand fortgesetzt",
      "failure_or_denial": "Lade-/Speicherfehler sichtbar, keine Defaults überschreiben",
      "first_class_disposition": "FC-FACTORY ja",
      "trace_refs": [
        "A-04",
        "PRD SYS-02/03"
      ]
    }
  ]
}
```
<!-- domain-context:end -->
