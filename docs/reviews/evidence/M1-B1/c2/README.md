# B1-C2 — gezielte HUD-Closure

Nach der unabhängigen C1-Review wurden ausschließlich `Client.client.luau` und der daraus erzeugte Build geändert. F-B1-UI-01: informative Schrift mindestens14 logische Pixel, Querformat-Zielfläche passend erweitert. F-B1-UI-02: Modal schluckt Hintergrundklicks, deaktiviert Hintergrundaktionen und deren Auswahl; Maus/Tastatur erhalten beim Schließen normale Bewegung zurück, Controller-Auswahl kehrt zum Sammlungsbutton zurück. M schließt auch bei aktiver GUI-Auswahl. Keine Änderung an Wirtschaft, Geometrie, Scout oder Verpackung.

Build SHA256 `677027e5d10d25bc7ea1ee1912f79166ae731fd4a63bde864f33ec9d7a61a3b7`; echte Studio-Quelle22298Bytes. C1 bleibt im Commit `869208e89385ff17fcb1421ec43d0666cc19fbf3` und im unveränderten übergeordneten Manifest nachvollziehbar. Seine bereits unabhängig positiven Regeln-/Premium-/Verpackungsbelege werden weiterverwendet. Dritte kohärente M1-Korrektur:3/3genutzt,0verbleiben; Ende23:09:52UTC unverändert.

## Tatsächlich ausgeführte betroffene Prüfung

- Syntax aller sechs Runtime-Dateien, reine Regeltests und Build nach Änderung erfolgreich. Exakte Ausgabe in `checks.txt`; kein neuer vollständiger Spiel-/Mehrspielernachweis.
- Normale Desktop-Bedienung: Erkunden → Sammlung → darunter sichtbare Kamera klicken →1s W. Kamera bleibtCustom, Modaltrue, AuswahlClose, Position unverändert(0;4,98;12), HintergrundActive/Selectablefalse. Danach × und1s W: Modalfalse, Auswahlnil, Position(0,27;7,40;−0,44). Reine Zustandsabfragen protokollieren die normalen Aktionen, lösen sie nicht aus.
- M normal geöffnet/geschlossen; Escape öffnete das Roblox-Menü und schloss dabei die Sammlung. Ein erster Weiterlauf traf die Maschine und ist kein Bewegungsnachweis. Separate frische Prüfung auf freier Startfläche: nach M-Schließen und0,7s S von(0;4,98;12) nach(6,14;3,24;21,04); nach Escape/Resume und0,7s A nach(−3,13;3,24;27,33). Modalfalse, Auswahlnil. Kein Teleport oder künstlicher Fortschritt.
- Desktop1511×758 mit nutzbarem GUI1511×700, XR-Querformat801×413 mit GUI801×355 und Hochformat413×814 mit GUI413×756. Laufzeit-Abfrage aller HUD-TextLabels/TextButtons: keine TextSize<14 und kein `TextFits=false`. Bilder zeigen die umliegenden Flächen ohne Abschneidung oder Überlagerung.
- Erste schmale Wiederholungsaufnahme warAutomatic, weil eine im Editmodus gesetzte Grafikstufe beim Playstart zurückgesetzt wurde. Die hier abgelegten vier `*-low.png` stammen aus dem späteren laufenden Client mit bestätigter **Level01** um22:38:05–22:39:06UTC. Abschließend RenderQuality und EditQualityAutomatic bestätigt; Play danach tatsächlich gestoppt. Kein physischer Mobilgeräte-/Gamepadtest behauptet; der Controller-Rückfokus ist quellgeprüft, noch nicht am realen Controller bedient.

## Bilder

`desktop.png` und `scout.png`: aktuelle normale C2-Werkstatt und per Sammlungsbutton geöffnetes Scoutporträt, Automatic. `landscape-low.png` / `landscape-scout-low.png`: echte XR-Querformatemulation, normale Karte. `portrait-low.png` / `portrait-scout-low.png`: echte Hochformatemulation und normale Karte. Nur Spiel-/Gerätebereich zugeschnitten und proportional verkleinert, keine Retusche; keine Identitäts-/Dateidialogaufnahmen gespeichert.

Creator urteilt weiterhin getrennt: **ansprechend für Menschen: ja; Lust auf den kurzen B1-Einstieg: ja**. Der freundliche Scout und die sichtbare Produktion bleiben unverändert; lesbarere Information und verlässlicher Rückweg stärken die Bedienbarkeit. Langfristiger Spielreiz, Ausbau/Orbit, Persistenz, integrierter Mehrspieler und Human-Endqualität bleiben B2–B5. Finale unabhängige Closure und40%-Disposition stehen im Run, nicht in diesem eingefrorenen Nachweispayload.
