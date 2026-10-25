# B5 — tatsächlicher Spielweg und Versandabschluss

25.10.2026. Kandidat C1 zur unabhängigen Prüfung, **keine B5-Gesamtabnahme**. Führend: [Run](../../../work/runs/boltbots-m1-b5-001.md). Ein weiterhin unerfülltes ursprüngliches Kriterium ist unten ausdrücklich benannt.

## Quellstand und Testisolation

Ausgangspunkt ist der sauber gepushte B4-Commit `3683527f68150a8905e96530dbf3a482ca697f66`. Drei Runtime-Dateien ändern sich: WorldBuilder ergänzt eine kompakte Versandannahme, Client animiert Rolltor/verdeckt wiederverwendeten Karton und korrigiert Kamera/Sichtbarkeit, GameConfig benennt `development-b5`. Keine Änderung an Preis, Produktionstakt, Käufen, Profiladapter oder Berechtigungen. Keine neue Wirtschaftsphase oder lange Produktionskette.

Aktueller Build: `28b4973ceaa5ccb7ef70fd5c17497f499ca5d4ccf8aeb57e0a3550a2a0aefcae`. Alle neun Edit-Sources wurden jeweils direkt gegen den gebauten XML-Quelltext geprüft; originale `BOLTBOTS_B5_SOURCE_MATCH`-Marker binden die jeweiligen Zwischenstände. Für die Tests wird danach ausschließlich die Profilschlüsselbildung im Studio-Main temporär auf `fixture_b5_gameplay_20261025_<eigene UserId>` umgestellt (`fixture-key-setup.luau`). Gleicher authentifizierter Player, echter Store, echte Serverregeln und normale UI; keine Cash-/Level-/Zeitinjektion. Persönliches `player_`-Profil wird nicht überschrieben. Diese einzelne temporäre Sourceabweichung ist kein Produktcode und muss vor dem privaten Save durch Rojo zurückgenommen und erneut bytegleich geprüft werden.

Einziges genehmigtes Ziel: Universe10772906084 / Place112662761038118 / Store `BoltBots_B3_20261025`. Kein B5-Cloudsave vor unabhängiger Prüfung, kein öffentlicher Release. Screenshots sind unveränderte native Studio-PNGs. `original-lines.json` enthält originale technische Logzeilen mit Dateiname und Zeilennummer; keine rekonstruierten grünen Gesamtlogs.

## Normaler Spielweg

Alle Kauf-/Abbruch-/Sammlungs-/Erkunden-/Retryhandlungen erfolgten als echte CUA-Klicks/Tastaturaktionen. GetSnapshot-Aufrufe beobachten nur, sie ersetzen keine Handlungen.

1. 16:41:55 neues isoliertes Profil: Cash0, completed0, L1, Scout. Natürliche Abschlüsse um16:42:04/13/22 liefern25/50/75Cash im9s-Takt. Bild01 zeigt bereits den späteren laufenden Scout, keinen behaupteten Nullframe.
2. Upgradeangebot geöffnet:50Cash,9→6s undOrbit erklärt (Bild02). Normal abgebrochen:100Cash/4Abschlüsse vor,150/6nach; abzüglich zwei legitimer25Cash-Abschlüsse genau0Kaufkosten, weiterhinL1/Orbitfalse.
3. Erneut geöffnet und gekauft:16:43:12 L2 für50Cash, Cash150 nach200, Orbit freigeschaltet (Bild03). Normal über Sammlung für nächsten Zyklus gewählt.16:43:50 tatsächlichOrbit/6s/L2, nicht bloß ausgewählter Wunsch.
4. Normales Stop/Play: Release16:44:21 Revision5/Cash400/completed18/L2/Orbit; Rejoin16:45:39 lädt exakt denselben Stand. Keine künstliche Reset-/Rejoinprobe.
5. Normal Erkunden, D-Bewegung, Kamera drehen, Sammlung erneut öffnen, Scout und später im schmalen Modal Orbit wählen. Wahl greift erst im folgenden Zyklus. Bewegungsschalter normal bedient: `Bewegung: ruhig`, Bild11 und Originalmarker.

## Echte Speicherfehler während B5

Ungeplante Roblox-Storefehler traten tatsächlich auf.16:54:06 `store_error` pausierte bei1525Cash, zuletzt bestätigt waren1400Cash/58Abschlüsse/Revision14. Bild04 zeigt sichere Pause. Nach mehr als90s war die Sitzung beim manuellen Retry abgelaufen; Bild05 fordert korrekt Rejoin.16:56:31 wurde der letzte bestätigte Stand1400/58 wieder geladen. Die unbestätigten125Cash wurden **nicht** als gespeichert behauptet oder künstlich wiederhergestellt.

Beim nächsten echten Fehler16:57:01 wurde der Retry rechtzeitig normal geklickt:16:57:16 bestätigter SaveRevision15/Cash1500/completed62, anschließend normale Produktion wieder sichtbar (Bild06). Damit sind sowohl rechtzeitige Wiederaufnahme als auch sichere Ablehnung nach abgelaufenem Anspruch aktuell beobachtet. Der erste15s-Versandobserver lief noch in der Pause und lieferte nur einen Status; dieser Versuch ist **kein** erfolgreicher Zyklusnachweis. Seine ursprüngliche f-Abfrage berücksichtigte PausedAt noch nicht; die beiliegende korrigierte Beobachtung tut das.

## Versand und Kameras

Die rechte Schranke hat eine freie Durchfahrt. Das vorhandene Band führt in eine geschlossene, zur Fabrik passende Annahme mit Rolltor, Schild und Sicherheitsmarkierung. Das Tor öffnet vor der Ankunft. Ein vollständig verschlossener Karton bleibt nach dem Zykluswechsel innerhalb der Annahme erhalten; Wiederverwendung erfolgt erst nach geschlossenem Tor. Ein Karton pro Plot, kein wachsender Stapel. Die sichtbare Annahme erklärt das Ende der kompakten M1-Kette; keine zusätzliche Belohnung oder Versandwirtschaft.

`shipping-observer.luau` liest nur reale Renderpositionen, Transparenz und Torhöhe, verändert keine Zustände/Posen/Zeit.16:56:42–57: drei natürliche Orbit-Recyclings bei vorheriger geschlossener Torhöhe8.10,0Verletzungen.16:57:59–16:58:14: ein auslaufender Orbit und zwei Scout-Recyclings ebenfalls verdeckt,0Verletzungen. Dieser technische Beleg ergänzt echte Sichtbilder, ersetzt sie nicht. Die Observerphasen können um einen Renderframe gegenüber dem ausgelesenen globalen Zyklus liegen.

Die Folge `13-orbit-inlet-08/12/14/15/16/17.png` zeigt unveränderte natürliche Orbitbewegung, Kartonaufbau, verschlossenen Karton, Einfahrt und anschließende Torphase aus **normalem Erkunden**. Originale Aufnahmezeiten stehen in `inlet-capture-times.json`; keine Animation wurde für Bilder gestellt. Der im Hintergrund sichtbare Nachbarplatz ist frei und ausdrücklich kein erfüllter Fremdplotnachweis.

Im ersten Entwurf war der Versand rechts abgeschnitten. Desktopkamera und später Hochformatkamera wurden im ersten Erstellungs-/Selbstprüfdurchgang verbreitert. Außerdem: nach verzögertem Profilladen wird der Eigentümerfokus erneut angewandt; fremde neu erstellte Roboter bleiben in Übersicht unsichtbar; beim Erkunden verwaltet Roblox die Nahtransparenz des Avatars wieder selbst. Bild14 zeigt normale Nahkamera ohne verdeckenden eigenen Kopf; der separate Marker liest echte Transparenz/Distanz aus.

## Sichtqualität und Grenzen

- Bild01–03: frühe B5-Fassung `a1ab40a6…f0c`, schon gleiche Versandgeometrie, noch enger Desktopausschnitt; keine endgültigen Kamerabelege.
- Bild04–06: Fassung `6d61f446…fff`, korrigierter Desktop-/Lade-/Nahkamerapfad; gleiche Versandgeometrie.
- Bild07: tatsächliches iPhoneXR-Querformat mitLevel01, noch vor letzter reiner Hochformatkameraänderung.
- Bild08–12 und14 sowie Bildfolge13: aktueller Build `28b4973c…cae`. HochformatHUD413×756, Kamera413×814, tatsächliche Abfrage im laufenden Client **Level01**. Hauptaktionen123×44, Sammlungswahl166×44, Produzieren341×44; Screenshots zeigen Text und beide Porträts vollständig. Die diagnostische Aktionsliste prüft nur lokale `Visible`-Flags und behauptet nicht, versteckte Elternmodalitäten seien gleichzeitig sichtbar.
- Bild12: aktuelle Desktopübersicht mit vollständig enthaltenen Maschinen und Versand. Normale freie Kamera zeigt die Umgebung wieder. Keine behauptete physische Telefon-/Gamepadprüfung.

Creatorurteil: Scout und Orbit sind durch freundliche Gesichter, unterscheidbare Silhouetten und ruhige Farben ansprechend. Die klare Upgradefolge führt innerhalb kurzer Zeit zu einem sichtbaren Ausbau und einem zweiten sympathischen Roboter; das schafft für die kleine M1-Referenz einen nachvollziehbaren Spielanreiz. Navy/Elfenbein/Cyan/Amber bleiben konsistent, Sammlung und Recovery sind lesbar. Die Versandannahme schließt den zuvor kaputten Bewegungsablauf plausibel. Das rechtfertigt ein positives Urteil zum **geprüften eigenen Spielweg**, nicht zu langfristiger Bindung oder einem fertigen Gesamtspiel. Im Hochformat ist die Fabrik kleiner; die Sammlung zeigt die Figuren groß. Human-Endentscheidung bleibt offen.

## Noch offen / Wiederverwendung

**Originales B5/M1-Kriterium „normal zu einem tatsächlich belegten fremden Plot gehen“ ist NICHT erfüllt.** B4 belegt echte authentifizierte getrennte Clients und Eigentums-/Geldisolation, aber CUA auf diesem Mac bindet nur den ursprünglichen Studioeditor. Die bereits fehlgeschlagenen Rebind-/Fensterwechsel-/AddClients-Varianten wurden nicht blind wiederholt; aktuelle Hersteller-Testdokumentation brachte keinen neu belegten passenden Weg. Synthetische Ownerattribute, freie Plätze und Remoteproben werden nicht umetikettiert. Kein Gesamt-B5-PASS und kein80%-Sprung solange das Kriterium offen ist.

Unveränderte B1/B2-Regeln und B3-Adaptertests sind erneut grün:9Runtime-Syntaxprüfungen, reine Typ-/Regeltests,36Profilecallbacks. B3-Migrations-/Sitzungsbelege und B4-authentifizierte Mehrclient-/Kapazitäts-/Manipulationsbelege bleiben separat gültig. B4-Vierclient-Framezeiten70–149msMedian/172–470msp95 auf gemeinsamemM2/16GB bleiben eine reale Einschränkung; keine60FPS-, Flüssigkeits- oder Mobilgerätefreigabe. Der neue kleine Präsentationsdelta ist keine neue Vierclientmessung.

KISS/Drift des Creators: drei Runtime-Dateien, vorhandene Bauteile und eine bestehende Renderverbindung; keine Tools/Plugins/Abhängigkeiten oder Ausweitung nachM2. Lokale gebündelte Bildbibliothek wurde nur zum internen Kontaktbogen vorhandener Screenshots benutzt, nicht installiert oder ins Produkt aufgenommen. Unabhängige Ergebnis-/Driftprüfung, abschließender Source-/Fixturecleanup, privater Save und Git-Sicherung folgen; Teilcheckpoint statt erfundener Erfüllung.
