# B1 — konkrete lokale Nachweise

Kandidat C1: sechs Runtime-Dateien + reine Regeltests, gebunden in `manifest.json`. Build SHA256 `bc1656b51f3af3367a5b1e7b52d36f74fec14f33082605dc2b96765b69794f22`. Studio 0.744.0.7441077, Rojo7.7.1, Luau0.744; lokaler Source-Sync aus dem bestehenden A3-Weg. Kein Upload/Publish/DataStore. Alle gezeigten Ergebnisse sind echte Studioansichten; Screens wurden nur auf Spiel-/Gerätebereich zugeschnitten und proportional verkleinert. Keine generierten Endergebnisbilder, Retusche oder vorgegebenen Cashstände.

## Bilder und Herkunft

| Datei | Tatsächlicher Inhalt |
|---|---|
| 00-human-packaging-defect.png | Originaler Humanbefund des vorherigen Standes: zu niedrige Verpackung, falsche Stützenorientierung, unpassender Karton. Historischer Fehler, kein Endergebnis. |
| 01-workshop-high.png | Normale laufende Szene des korrigierten Kandidaten, Level21, Desktop1511×758. Originalaufnahme 21:56:18 UTC. |
| 02-scout-detail.png | Normal per Sammlung geöffneter, wiederverwendeter 3D-Scout, frische Sitzung nach Diagnoseende. |
| 03-portal-entry.png | Natürliche Durchfahrt: der vollständige Scout passt unter das Portal. Level21; Aufnahme21:56:27. |
| 04-carton-forming-diagnostic.png | **Diagnostisches Standbild**, keine normale Bedien-/Geldevidenz: beim natürlich erreichten Zyklus38, Anteil0,804, wurde ausschließlich der laufende Client-Präsentationsskript deaktiviert. Nichts wurde positioniert, freigeschaltet oder am Serverfortschritt geändert. Anschließend Stop und frische normale Sitzung. |
| 05-sealed-outfeed.png | Normale laufende Szene, geschlossener Karton mit Scout-Etikett und Klebeband auf erweitertem Auslauf; Automatic. Andere natürliche Runde als03/04; keine Behauptung eines lückenlosen Videos. |
| 06-landscape-low.png / 07-landscape-scout-low.png | Korrigierter Kandidat in iPhone-XR-Emulation801×413, Level01; Werkstatt und per Button geöffnete Sammlung. |
| 08-portrait-low.png / 09-portrait-scout-low.png | Derselbe Kandidat hochkant413×814, nutzbarer GUI-Bereich413×756, Level01. Keine überlagerten Touchkreise in Übersicht, vollständiges Scoutporträt. |

Die Bildschirmaufnahme über CUA brauchte teils5–9s und verfehlte dadurch die nur1,8s lange Verpackungsphase. Ein Versuch mit Studio `RunService:Pause()` hielt die lokale, am Serverzeitstempel ausgerichtete Darstellung nicht an; dieses versuchte Pausenbild ist bewusst kein Verpackungsbeleg. Der eine ausdrücklich markierte Diagnose-Freeze sichert die tatsächlich erreichte Zwischengeometrie. Die separate natürliche Bewegungsfolge und räumliche Prüfung tragen die Durchfahrtsaussage.

## Ausgeführte Prüfung

- `checks.txt`: tatsächlicher Exit0; sechs Runtime-Dateien syntaxgeprüft, reine Regeln analysiert und getestet. Früher/alter/unbekannter/duplizierter Abschluss, atomare Cash-/Scouterteilung, Stop, NaN/Infinity/Geldgrenzen. Keine vollständige Roblox-API-Typprüfung.
- Serverlog zeigt in frischen Sitzungen erste Abschlüsse1/2/3 mit Cash25/50/75 und genau ein erstmaliges Scout-Unlock; später normal300Cash bei12Abschlüssen. Sammlung bleibt Designrecht. Kein Client-Awardremote; Query mit View, Produktion serverintern. Kein Saveclaim.
- Normale Sammlung öffnen/× schließen sowie Escape/Menu-Rückweg, Kamerawechsel und reduzierte Bewegung wurden ausgeführt. `PHONE_STATE` belegt nach Escape: Overlayfalse, Touchfalse, Cash275/11, Scouttrue. `PHONE_FINAL` belegt „Bewegung: ruhig“. Die unveränderten UI-Funktionen wurden nach der Verpackungskorrektur in aktuellen Bildern und `FINAL_STATE` nochmals beobachtet.
- Der Initialtest fand festgehaltenen GUI-Fokus nach Sammlung. In „Erkunden“ wird er jetzt aufgehoben. Echte Desktop-W-Bedienung bewegte den Avatar vom Spawn(0;4,98;12) nach(−12,54;6,00;−3,71), `MOVE_FOCUS`: Custom, SelectedObjectnil. Dieser unveränderte Fokuszweig wurde vor der reinen Verpackungsänderung nachgewiesen. Frühe Mobile-W-/Dragversuche änderten die Position nicht; daraus wird ausdrücklich kein erfolgreicher Touch-Bewegungstest behauptet.
- Human-Verpackungsbefund: Portalöffnung ab2,7 bis10,4Stud, Scout ca.6,6Stud, passender Karton7,34Stud inklusive Tape. Stützen stehen seitlich außerhalb der Route. 70 natürliche Laufzeitstichproben im Abstandca.0,2s prüften sichtbare Produktions-BaseParts mittels `Workspace:GetPartsInPart` gegen alle tatsächlichen „Packager“-Bauteile: **0 Überschneidungen**. Durchlauf wird nach Montage/Band zum stehenden Kartonaufbau, Deckelschließen, anschließend Auslauf; Cash erst beim echten serverseitigen Ende.
- 180 RenderStepped-Frames bei Level21: ca.48,0FPS im Mittel, größte einzelne Framezeit91ms. Nur kurze Studio-Stichprobe auf diesem Mac mit einem Client; kein60FPS-Versprechen und keine Geräte-/4-Client-Performanceabnahme. Sichtbare Objektzahl ist begrenzt (je Plot ein wiederverwendeter Scout/Karton), kein wachsendes Roboterlager.
- Aktueller Client.Source im echten Studio:21552Bytes; `C1_MOBILE_LOW` bestätigt aktuelle Quelle, Level01 und tatsächlich aktiven Client. `FINAL_STATE`:413×814, Overlayfalse, Cash300,12Abschlüsse, Scouttrue, ClientEnabledtrue. RenderQuality und EditorQuality wiederAutomatic; Play gestoppt. Originale Logs im untersuchten21:21–22:04-Fenster enthalten keine passenden CreatorOutput-Skriptfehler; bereits bestehende Avatar403-/Plattformtelemetrieprobleme werden nicht als globale Fehlerfreiheit umgedeutet.

## Creatorurteil, separat von der unabhängigen Review

**Ansprechend für Menschen: ja, für den begrenzten B1-Einstieg.** Der Scout hat einen klaren freundlichen Gesichtsausdruck, großen abgerundeten Helm, bewegte Grußhand und eine zusammenhängende ivory/cyan-Materialfamilie. Maschinen, Band, warme Akzente und lesbares HUD geben der kleinen Werkstatt einen erkennbaren Zusammenhang. Er ist auch bei Level01 und auf der großen schmalen Sammlungskarte klar lesbar. Die hohe r3-Konzeptdichte ist nicht schon als fertige gesamte Spielwelt erreicht.

**Macht Lust zu spielen: ja, als erster kurzer B1-Moment.** Der nachvollziehbare Weg bis zum fertigen Karton, bestätigte Cashzuwachs und die entdeckte Scoutkarte laden zum Beobachten/Erkunden ein. Langfristiger Spielanreiz ist damit noch nicht nachgewiesen: Ausbau/Orbit(B2), Save/Rejoin(B3), integrierter Mehrspieler(B4) und vollständiger Spieltest/Human-Endqualität(B5) bleiben offen. Kein Kaufbutton täuscht diese fehlenden Funktionen vor.

Der Humanbefund wurde nicht technisch schöngeredet: altes Bild bleibt erhalten, relevante neue Quellen/Bilder sind gebunden. Konservative kumulative Reserve2/3genutzt,1verbleibt; feste B1-Grenze23:09:52UTC bleibt. Finale unabhängige Entscheidung und40%-Drift stehen im B1-Run; bis dahin bleibt M1bei30%.

Primäre API-Nachschlagequellen: [Serverzeit](https://create.roblox.com/docs/reference/engine/classes/Workspace#GetServerTimeNow), [ViewportFrame](https://create.roblox.com/docs/reference/engine/classes/ViewportFrame), [Rendering](https://create.roblox.com/docs/reference/engine/classes/RenderSettings), [räumliche Abfrage](https://create.roblox.com/docs/reference/engine/classes/WorldRoot#GetPartsInPart), [RunService](https://create.roblox.com/docs/reference/engine/classes/RunService). Keine externen Kunstassets oder neuen Laufzeitabhängigkeiten.
