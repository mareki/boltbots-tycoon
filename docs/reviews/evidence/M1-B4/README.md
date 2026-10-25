# B4 — reale integrierte Clients und gemessene Basis

25.10.2026; einziges genehmigtes privates Ziel: Universe10772906084, Place112662761038118, Store `BoltBots_B3_20261025`. Quelle ist B3 plus die kleine B4-Owner-/Kapazitätsmeldung. Kein öffentlicher Release. Der führende B4-Run enthält Autorität, Budget, Review und endgültige Bindung.

## Was die Belege bedeuten

`original-lines.json` enthält unveränderte technische CreatorOutput-Zeilen mit Originaldatei/Zeilennummer. `events.json` liest kurze JSON-Zeilen und rekonstruiert die nummerierten `B4_CHUNK`-Teile. Die Studio-Logausgabe kappt lange Einzelzeilen: frühe Zweiclient-Remoteausgaben sind deshalb KEIN vollständiger Erfolgsbeleg. Die aktuellen Vierclientproben sind vollständig zusammengesetzt. Historische Fehlversuche bleiben erkennbar; es wird kein grüner Gesamtlog behauptet.

Die nativen Studio-Funktionen erzeugten tatsächlich getrennte Server-/Clientprozesse. Temporäre, auf Studio und die exakten IDs begrenzte Script/LocalScript-Proben rufen die wirklichen Remotes mit der vom Server authentifizierten jeweiligen Identität auf. Sie injizieren kein Cash und sind ausdrücklich keine normalen GUI-Klicks. Probequellen liegen nur hier als Evidenz, nicht im Rojo-Projekt; vor endgültigem Save werden sie im Edit-Datamodel entfernt.

CUA kann auf diesem Mac nur den ursprünglichen Studioeditor binden. Bounded Diagnose und unabhängige zweite Dokumentations-/Inventarsicht fanden keine unterstützte Childfensterzielwahl. Die ursprünglichen B4-Pflichten sind technische Integration/Isolation und Mehrclientmessung; die anfänglich stärkere Methode „zwei Clients normal spielen“ wurde nach unabhängiger Prüfung der ursprünglichen Handovertabelle, milestones.md:43/52/57 und Technik:41/58 transparent korrigiert. Vollständiges normales Mehrspieler-Erkunden einschließlich fremder Werkstatt bleibt ausdrücklich **B5 / vor M1-Abnahme offen**. B1–B3 liefern getrennte unveränderte normale Einzelclientbedienbelege, keine Mehrspielersicht.

## Integrierte Vierclientproben

Run `four`, Serverdatei `0.744.0.7441077_20261025T120409Z_Studio_07070_last.log`; vier tatsächliche Clients mit UserIds−1…−4, eigenständigen Plots1…4, richtigen Place-/Universe-IDs und `saveStatus=saved`. −1/−2 waren bereits L2; −3/−4 begannen L1 und verdienten Cash durch reale Serverabschlüsse.

Beide Angreiferclients: zusätzliche fremde Player-/Plotfelder und zusätzliche Argumente abgewiesen; fremde Maschinenkennung verboten; negative/NaN/Inf-Level ohne Wirkung; unbekanntes Design und erfundener Clientabschluss abgewiesen. Für jeden gebundenen Vor-/Nachstand gilt `Cashnach−Cashvor−25×(completednach−completedvor)=0`. Ein Stringlevel traf bei−3 eine echte kurze Autosavepause (`inactive`); bei−4 wurde der Typ als `stale_state` abgewiesen. Keine einheitliche Fehlercodebehauptung.

−3 sendete denselben Kauf dreimal gleichzeitig: drei idempotente `upgraded`-Antworten, genau einmal50Cash abgezogen und L2/Orbit gesetzt. −4 sendete drei verschiedene alte Kaufabsichten: `upgraded`, `stale_state`, `stale_state`, ebenfalls genau einmal50Cash. Vor-/Nachstände waren350→300 bzw.325→275. Die frühen `CONTROL_AFTER_OTHER_COMMANDS`-Marker liegen zeitlich vor beziehungsweise fast vor den Angriffen und sind deshalb kein ausreichender Nachherbeleg. Die späteren echten `capacity CLIENT_READY`-Stände tragen die Isolation: −1 3825Cash/155Abschlüsse → 5600/226 und −2 1425/59 → 3250/132, beide weiterhin L2/Scout. Jeweils ist die Cashdifferenz abzüglich25×neuerAbschlüsse exakt0; kein fremder Kauf oder Designwechsel. Explizite Orbitwahl wirkt im folgenden tatsächlichen Orbitzyklus mit6s; laufendes Design/Dauer bleiben getrennt.

−3s 12er Burst enthielt zwei `rate_limited`; −4s durch Last zeitlich verteilter Burst wurde vollständig akzeptiert. Keine Behauptung, jeder sequenzielle Burst überschreite die Zeitschranke. Verschmutzte Snapshotabfrage liefert nur „Ungültige Anfrage“, kein Fremdprofil. Öffentliche Plotattribute enthalten Ownerreferenz, Geometrie und sichtbaren Zyklus/Level; keine Speicher-/Sitzungstoken oder vollständigen Profile.

## Gemessene 1/2/4-Basis — keine Flüssigkeitsfreigabe

Host: `host.json`, AppleM2/16GB, macOS26.5.2, Studio0.744.0.7441077. Alle Prozesse auf demselben Rechner; ursprünglicher Editor bei CUA-Aktionen vorn, Child-Foreground nicht separat kontrollierbar, weitere normale Desktopanwendungen vorhanden. Parentgrafik Automatic; Childqualität durfte durch Clientcode nicht privilegiert ausgelesen werden und wird nicht erfunden. Viewports1081×693. Nach vollständiger Population weitere15s Warmlauf, Messfenster jeweils≥60s. Mehrere Studio-Prozesse und mögliche Hintergrunddrosselung begrenzen die Übertragung auf echte Endgeräte; Hostkonkurrenz ist eine plausible Einordnung, keine isolierte Ursachenmessung.

| Tatsächliche Clients | Server Heartbeat median/p95 ms | Client Render-dt median/p95 ms |
|---|---|---|
| 1 (`one-r2`,11:38) |16,67 /22,50|33,72 /60,27|
| 2 (`two`,11:56–11:57)|16,82 /57,86|−2:52,10 /81,20; −1:68,66 /121,27|
| 4 (`four`,12:07–12:08)|17,72 /78,24|−1:149,37 /470,08; −2:100,98 /401,82; −3:130,23 /292,48; −4:70,10 /171,91|

Diese hohen Clientzeiten belegen **keine flüssige Vierclientdarstellung und keine60fps**. Sie sind die verlangte ehrliche lokale Basis, keine Endgeräte-/Mobilfreigabe. Serverzyklen liefen bei vier getrennten Profilen weiter. Serverinstanzen blieben je Fenster49357/50274/52108 konstant. Lokale Produktvisuals je Client blieben4Container/8Modelle/12direkteKinder, also pro Plot ein aktueller Roboter und ein wiederverwendeter ShippingCarton. Ein Designwechsel zerstört den bisherigen Roboter und erstellt den neuen; Abschlüsse häufen keine Modelle an. Allgemeine Clientinstanzen stiegen bei zwei Vierclientfenstern noch durch Laufzeitaufbau, daher kein pauschaler Plateau-/Leakfreiheitsclaim. Speicherwerte sind Stats-Prozessspeicher, nicht einzelne Profile: Server1Client2069,90→2075,77MB,2Clients2202,46→2174,16MB,4Clients2202,30→2208,17MB; Clients grob2,1–2,4GB pro Prozess, genaue Anfang/Endwerte in den Events.

Die erste Einclientprobe scheiterte nur beim privilegierten Grafiklesen; `one-r2` ist die korrigierte Messung. Ein früher `two`-Tag um11:51 enthält tatsächlich nur einen Client und wird ausgeschlossen. Ein eingebetteter normaler Play mit dem angemeldeten Konto ist ebenfalls kein Mehrclientmessfenster. Einclientbasis entstand vor der reinen B4-Beschriftungskorrektur; zwei/vier Clients verwenden aktuelle B4-Quelle. Unveränderter Produktionstakt/Visualaufbau tragen die Wiederverwendung, keine bitgleiche Einclient-B4-Fassung behauptet.

## Wiederverwendung und verbleibende Grenze

B1/B2-Regel-, Kauf-/Abbruch-/Modal-/schmaleLevel01-/Verpackungsbelege und B3-Store-/Recovery-/Migrations-/Rejoinbelege bleiben gültig. Reine Grenztests ersetzen keine aktuellen Netzwerkbelege. Neue B4-Diagnosebilder zur Owner-/Kapazitätslesbarkeit werden separat als solche bezeichnet, kein normaler Fremdplot-Spielbeleg.

Humanbefund zum unplausiblen rechten Versandabschluss bleibt vor Gesamt-M1-Qualität offen. B4 bewertet nur den kleinen Owner-/Recoverydelta sowie technische Integration, keine gesamte Spielqualität oder B5-Abnahme.

## Reale Kapazitätsgrenze und historischer Sicht-/Cleanupstand

`capacity`: fünf native Clients, serverseitig genau vier aktive Plots. Um12:24:52 diagnostisch genau den nachweislich aktiven Owner−1 getrennt. Client−5 erhielt `ready=false/saveError=no_plot` ohne Cash-/Level-/Profildaten; sein tatsächlicher HUD-Text lautet „Alle Werkstätten sind belegt“, Body/Title `TextFits=true`. Um12:26:54 nahm derselbe Client über den echten Retry Plot1 an: `ready=true`, `saveStatus=saved`, Cash0, L1, Scoutzyklus1/9s, eigene neue Produktion. Der Servermarker `CAPACITY_AFTER_RETRY`12:25:37 war trotz des Namens **vor** dem tatsächlichen Retry, zeigt daher korrekt drei aktive Plots und gilt nicht als Nachherbeweis. Die danach gebundene echte Clientantwort ist der Wiederaufnahmebeleg; ein späterer normaler Spiel-/Cashabschluss dieses Clients ist nicht separat aufgenommen.

**Stand12:48UTC: technische Teilfassung, keine B4-Gesamtabnahme.** Neue Ownerbeschriftung ist quellgebunden und mit realen öffentlichen Ownerattributen technisch konsistent, aber tatsächlicher visueller Eigene-/Andere-Nachweis fehlt. no_plot wurde im echten fünften Client als gerenderter sichtbarer Text mit TextFits bestätigt; der zusätzliche repräsentative Desktop-/Portrait-Screenshot fehlt. Das ist ausdrücklich keine endgültige Premium-/Sichtfreigabe.

Nach den benötigten Proben wurden reguläre Test→EndSession-/Editorzugriffe versucht; CUA wurde durch die hohe Hostlast nach73/91/81s abgebrochen. Prozessidentifikation über `ps` scheiterte im Sandboxmodus; zwei exakt begrenzte automatische Genehmigungsprüfungen liefen ihrerseits in Timeout. Kein PID geraten oder Prozess abgeschossen. Studio-Childprozesse, temporäre Proben und Rojo sind deshalb am Freeze **nicht als beendet/entfernt bestätigt**. Vor Cloudsave ist reguläre Beendigung, Entfernung beider `B4TemporaryProbe`-Objekte/Workspaceattribute und Sourcegleichheit zwingend. Kein B4-Cloudsave durchgeführt; private Cloudfassung bleibt approvedB3. Keine weitere UI-Diagnoseplattform.


## Fortsetzung — gebundene Sichtprüfung und aktueller Cleanup

25.10.2026, nach Humanfortsetzung. Der bestehende private Place wurde über die Studio-Recents wieder geöffnet. Dies ist kein belegter Kaltabruf der Cloudfassung. Die UI zeigte zunächst Home; keine alte Session wurde durch uns rückwirkend als regulär beendet behauptet. Bei Rojo-Synchronisierung wurde die temporäre Clientprobe entfernt; der gezielte Commandbar-Cleanup entfernte genau eine verbliebene Serverprobe sowie beide Workspaceattribute. `resume-observations.log` bindet Originaldatei/Zeile und tatsächliche Ausgaben. Um14:48:18 bestätigten neun direkte Source-Gleichheitsassertions im richtigen Place sämtliche B4-Quellbytes gegen Build `28c95843…82654`.

Die neuen Bilder sind echte Studio-Screenshots mit unveränderter B4-Quelle:

- `owner-own-desktop.png`: normaler eingebetteter Spielstart mit eigener aktiver Werkstatt und sichtbarem „DEINE WERKSTATT“.
- `owner-other-diagnostic-desktop.png` und `owner-free-diagnostic-desktop.png`: ausschließlich das lokale öffentliche Ownerattribut derselben Darstellung wurde auf−999 beziehungsweise nil gesetzt; der unveränderte Clientrenderer schrieb „ANDERE WERKSTATT“ und „WERKSTATT / FREI“. Danach Ownerattribut lokal wiederhergestellt. Kein echtes Fremdplot-Erkunden und keine serverseitige Besitzänderung behauptet.
- `no-plot-diagnostic-desktop.png`, `no-plot-diagnostic-landscape-automatic.png`, `no-plot-diagnostic-portrait-automatic.png`: der echte bestehende StateChanged-Renderer erhielt über die Studio-Servercommandbar einen kontrollierten View mit `ready=false`, `load_failed`, `no_plot`, `canRetry=true`. Profil/Plots/Store wurden hierfür nicht geändert. Dies sind ergänzende Darstellungsbelege; tatsächliche Kapazitätsablehnung und Retry tragen weiterhin die vorherigen fünf realen Clients.
- Portrait ist tatsächlich413×756 logische HUDpixel, Titel24px und Text17px, beide `TextFits=true`; Retry349×48. Die Aufnahme zeigt vollständigen Text und Aktion ohne Abschneiden. iPhoneXR-Simulator, kein physisches Mobilgerät. Vor Play gesetztes Level01 blieb im Client nicht erhalten: die tatsächliche Abfrage ergab **Automatic**. Deshalb kein neuer Low-Grafiknachweis; die unveränderten B3-Recovery-/Layoutbelege beiLevel01 bleiben separat bestehen.
- `edit-clean-disconnected.png`: abschließend Editmodus, Simulatoraus, Rojo-Plugin mit Connect statt Disconnect. Der verbliebene Verbindungshinweis ist ein alter Toast, kein Listenerbeweis. Eigener Serveprozess91043 regulär durchCtrl-C beendet, anschließend `lsof -nP -iTCP:34872 -sTCP:LISTEN` Exit1 ohneAusgabe. Um14:54:21 bestätigten Assertions keinen Play, keine beiden Probeobjekte, keine beiden B4-Attribute und keinen B3-Faultschalter; GrafikAutomatic.

Die zwei Sichttests wurden regulär gestoppt. Der echte Store bestätigte Release38/3725Cash/151Abschlüsse und Release41/4050Cash/164Abschlüsse, jeweilsL2/Orbit. Diagnostische Views sind mit dem Testdatamodel beendet. Keine erneuten1/2/4-Messserien, keine neue Runtime-/Tool-/Plattformänderung. Der autorisierte private B4-Cloudsave folgt erst auf unabhängige Ergebnisabnahme und erneute Sourcegleichheit; bis dahin kein B4-Saveclaim.

Creatorurteil zum engen B4-Delta: Die bündige helle Beschriftung auf dem dunklen Werkstattschild passt zur bestehenden Fabrik und benennt den Besitz ohne einen fremden Ort fälschlich als eigenen auszugeben. Die ruhige navy/cyan Recoverykarte bewahrt die erkennbare Spielwelt, erklärt den freien Platz und bietet einen eindeutigen Rückweg. Das wirkt für Menschen ansprechend und unterstützt die Lust, zur eigenen Roboterproduktion zurückzukehren. Dies ist ein begründetes Agentenurteil zu Beschriftung und Kapazitätsmeldung, keine Präferenzmessung oder Gesamtspiel-Premiumfreigabe. Die Human-Versandlücke bleibt ausdrücklich offen.

Die unabhängige technische Teilreview bestätigte den ursprünglichen Kandidaten, verlangte nur die oben korrigierte Nachherisolation und Modellzählungsbeschreibung. Beide minor/evidence_accuracy-Findings werden zusammen in dieser Abschlussfassung korrigiert; rohe Events/Logs und sämtliche Runtimebytes bleiben unverändert. Konservativ ein zusammenhängender letzter Dokumentationskorrekturzyklus, kumulativ6/6 genutzt; keine weitere Produktkorrektur autorisiert. Finale unabhängige Sicht-/Cleanup-/Evidenzclosure ist noch ausstehend.
