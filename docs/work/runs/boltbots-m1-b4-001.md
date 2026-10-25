# Execution Run — M1 B4: Mehrspieler und integrierte Grenzen

> Artifact ID: `BOLTBOTS-RUN-M1-B4-001`
> Artifact class: Work contract
> Creator/operative Lead: /root/b4_creator · unabhängiger Reviewer: /root/b4_review · Spawn: /root/b4_spawn · alle Astra/xhigh
> **Aktuell: B4 abgeschlossen und unabhängig approved; M1 70%. Privater Save15:00:28UTC bestätigt. Die tatsächliche Git-/Remote-ID wird in der Abschlussnachricht bestätigt.**
> Historische B4-r1-Rollen: /root/b1_creator, /root/b1_review, /root/b1_spawn; durch explizite Humanfortsetzung ersetzte Kontexte, keine zusätzliche parallele Kapazität.

<!-- run-contract:start -->
```json
{
  "schema_version": "1",
  "revision": 2,
  "status": "completed",
  "harness_version": "1.5.3",
  "run_kind": "product_delivery",
  "decision_class": "D3",
  "targets": [
    {
      "id": "BOLTBOTS-RUN-M1-A2-001",
      "path": "docs/work/runs/boltbots-m1-a2-001.md"
    },
    {
      "id": "BOLTBOTS-RUN-M1-B1-001",
      "path": "docs/work/runs/boltbots-m1-b1-001.md"
    },
    {
      "id": "BOLTBOTS-WP-01B",
      "path": "docs/work/packages/boltbots-wp-01b.md"
    },
    {
      "id": "BOLTBOTS-DOMAIN-FOUNDATION-001",
      "path": "docs/domains/domain-foundation.md"
    },
    {
      "id": "BOLTBOTS-DOMAIN-REVIEW-001",
      "path": "docs/reviews/20261024-1.5.3-boltbots-domain-foundation-review.md"
    },
    {
      "id": "BOLTBOTS-INITIALIZATION-REVIEW-001",
      "path": "docs/reviews/20261024-1.5.3-boltbots-initialization-review.md"
    },
    {
      "id": "BOLTBOTS-VISION-001",
      "path": "docs/product/vision-and-mvp.md"
    },
    {
      "id": "BOLTBOTS-PLAN-001",
      "path": "docs/planning/milestones.md"
    },
    {
      "id": "BOLTBOTS-FACTORY-TARGET-001",
      "path": "docs/specs/factory-module.md"
    },
    {
      "id": "BOLTBOTS-TECH-001",
      "path": "docs/specs/technical-foundation.md"
    },
    {
      "id": "BOLTBOTS-DESIGN-001",
      "path": "docs/design/design-reference.md"
    },
    {
      "id": "BOLTBOTS-RUN-M1-B2-001",
      "path": "docs/work/runs/boltbots-m1-b2-001.md"
    },
    {
      "id": "BOLTBOTS-RUN-M1-B3-001",
      "path": "docs/work/runs/boltbots-m1-b3-001.md"
    }
  ],
  "outcome": "B4: integrierte Wirtschafts-/Manipulations-/Fehlerprüfung mit echten getrennten Studio-Clients, Eigentumsisolation und gemessener 1/2/4-Client-Leistungsbasis.",
  "allowed_paths": [
    "src/",
    "tests/",
    "scripts/",
    "docs/work/packages/boltbots-wp-01b.md",
    "docs/work/runs/boltbots-m1-b4-001.md",
    "docs/reviews/evidence/M1-B4/",
    "docs/handover.md",
    "docs/setup.md",
    "README.md",
    "build/"
  ],
  "non_goals": [
    "B5 Gesamtspiel-/Premiumabnahme oder Versandumbau; neue Spielsysteme, Plattformen und Familien",
    "Core/Import/Frozen Foundation/Designquellen ändern",
    "Öffentlicher Release, neue Experience, Produktions-/fremde Daten, Credentials oder weitere Agenten/Tools"
  ],
  "decision": {
    "authority": "Human Marek",
    "approval_ref": "human-approved:20261025-B4-End-to-End-und-fortsetzen-144019UTC",
    "lead": "/root/b4_creator",
    "reasoning": "xhigh",
    "agents": [
      "/root/b4_creator",
      "/root/b4_review",
      "/root/b4_spawn"
    ],
    "reviewers": [
      "/root/b4_review"
    ],
    "max_corrections": 6,
    "effort_override": "human-approved:20261025-B4-resume-144019-154019UTC-historische5von6genutzt"
  },
  "external_actions": {
    "allowed": [
      "Lokales Studio Server & Clients, 1/2/4 aktive Testclients, begrenzte Diagnose-/Manipulationsproben in dieser Testsession",
      "Ausschließlich bestehende private Universe10772906084/Place112662761038118 (BoltBots B3 Test 20261025), isolierter Store BoltBots_B3_20261025 mit eigenen/synthetischen Profilen; geprüfte B4-Quelländerung dort privat speichern",
      "Normaler Commit/Push codex/initialize-boltbots zu origin ohne Force/Merge"
    ],
    "prohibited": [
      "Öffentliche Veröffentlichung, Produktions-/fremde Daten oder Konto-/Credentialänderung",
      "Bestehenden Standard-Place überschreiben",
      "Core-/Import-/FrozenFoundationmutation, zusätzlicheTools/Plugins/Agenten"
    ]
  },
  "completion_evidence": [
    "Tatsächliche getrennte Clients mit eigenen Plots/Profilen und authentifizierten integrierten Kauf-/Manipulationsproben; normaler Gesamtspiel-/Fremdplotpfad bleibt B5/M1 zugeordnet",
    "Integrierte ungültige/gefälschte/duplizierte/parallele Befehle und Raten-/Sitzungs-/Kapazitätsgrenzen; keine fremde Mutation oder Clientabschluss",
    "Benannte Hardware/Studio/Quelle; feste 1/2/4-Szenarien mit Framezeitverteilung, Speicher, Output-/Instanzzählung und Serverloopbeobachtung",
    "Unveränderte reine Grenz-/Store-/UIbelege wiederverwenden; tatsächliche Mehrclientbelege davon trennen",
    "Unabhängige Ergebnis-/Technikreview und enges Qualitäts-/Spielanreizurteil, ereignisbezogener Drift/KISS, autorisierte Sicherung"
  ],
  "agent_start": {
    "applicability": "required",
    "spawn_reviewer": "/root/b4_spawn",
    "clearance": "pass",
    "cleared_agents": [
      "/root/b4_creator",
      "/root/b4_review",
      "/root/b4_spawn"
    ]
  }
}
```
<!-- run-contract:end -->

<!-- task-controls:start -->
```json
{
  "checked_revision": 2,
  "progress": 70,
  "updates": [
    {
      "percent": 10,
      "evidence": "A1 abgeschlossen und unabhängig approved; übernommen aus docs/handover.md. A2 Vorbereitung seit 19:27UTC, keine Installation. Nächster Schritt: exakter Aktivierungs-Pass und lokale Einrichtung; kein fachlicher Blocker."
    },
    {
      "percent": 20,
      "evidence": "A2 technisch nachgewiesen: Rojo/Luau und Plugin7.7.1; Doctor/5Syntax-/reineTyp-/Regelchecks/Build Exit0; sauberer Clone42c4c6d mit frischem Download erzeugt identischen SHA256 f7642a8d. Unabhängige Ergebnisreview folgt, A3 offen, kein Ausführungsblocker."
    },
    {
      "percent": 30,
      "evidence": "A3 technisch nachgewiesen: tatsächliches StudioPlay mit Bootlogs undCash425→500/Roboter17→20, Rojoverbunden undDateimarker imStudio.Source gesehen, Rücknahmebestätigt, Source/Buildunverändert. Ergebnisreview folgt; keine fachlicheErweiterung."
    },
    {
      "percent": 40,
      "evidence": "B1-C2 unabhängig approved durch /root/b1_review um22:46UTC: tatsächliche kleine Werkstatt/Scout/Produktionskette, serverfälliger einmaliger Cash-/Scoutabschluss; Human-Verpackungsbefund und beide HUD-Findings geschlossen. Manifest9770d0d3…03128, Build677027e5…1a3b7. Separate positive B1-Premiumurteile und unabhängiger40%-Drift liegen vor. Nächster Schritt nur Git-Sicherung; B2–B5 offen."
    },
    {
      "percent": 50,
      "evidence": "B2-C2 unabhängig approved durch /root/b1_review: serveratomarer50Cash-L2-/Orbiterwerb, sichtbarerAusbau/6sFolgetakt, eigeneOrbitfigur/Produktionswahl, vollständigeVerpackung sowie Desktop/schmaleLevel01- undModalnachweise. Portrait-/Belegfindings geschlossen; getrennte positivePremium-/Spielanreizurteile und ereignisbezogenerKISSentscheid liegen vor. Manifestdb9e3807…570ed, Buildfba4955d…9388c. NächsterSchritt Abschluss/Git; B3–B5offen."
    },
    {
      "percent": 60,
      "evidence": "B3-C1 unabhängig approved10:50UTC: realer versionierter Profiladapter, exklusiver Anspruch, Migration, normales Save/Rejoin und sichere Load-/Savefehlerreaktion samt Retry. Manifest7a6715d1…edf29, Build1879055e…93e3b. Zusätzlicher eigener Reviewer-Rejoin exakt2675/109/L2/Orbit; getrennte positive B3-Recovery-UI-/Spielanreizurteile und unabhängiger60%-Drift. Exakter privater B3-Save nach bytegleicher9-Sourceprüfung10:52:01 bestätigt. Abschluss/Git; B4/B5 und Humanversand-/Gesamtqualität offen."
    },
    {
      "percent": 70,
      "evidence": "B4 unabhängig approved durch /root/b4_review auf Manifest41ff75e3…af7b/30Dateien und Build28c95843…2654. Reale1/2/4Clients, Eigentum/Geld/Manipulation/Parallelität und5.Join/Retry belegt; kleineOwner-/no_plotSichtclosure positiv. AktuellerCleanup bestätigt. NeunStudioquellen direkt gegenapprovedBuild15:00:04 bytegleich; gleicherprivaterSave15:00:28, Transfermechanik unabhängig bestätigt. KeinFlüssigkeits-/Mobil-/Gesamtspielpass. NächsterSchrittGitabschluss; B5/normalerFremdplotpfad/Humanversand-/Endqualität offen."
    }
  ],
  "drift_checks": [
    {
      "percent": 20,
      "reviewer": "/root",
      "decision": "continue",
      "evidence": "Originalauftrag A2/BOOT-01–04 erfüllt technisch; kein A3/Play/Save/Cloud/Design. Zwei direkt gepinnte Tools, ein kleines Standardbibliotheks-Skript; kein zusätzlicher Manager/Framework. Ein Toolhash-Missverständnis in einer kohärenten Korrektur behoben,2Reserven bleiben. Preparation+Umsetzung seit19:27UTC, deutlich vor21:00:10Hardstop; verbleibend unabhängige Review und Git-Sicherung. Risiko: noch kein echter Spiel-/Zweitrechnertest, ausdrücklich nachgelagert.",
      "origin_run": {
        "id": "BOLTBOTS-RUN-M1-A2-001",
        "revision": 1
      }
    },
    {
      "percent": 40,
      "reviewer": "/root/b1_review",
      "decision": "continue",
      "evidence": "Originales B1-Ziel erreicht, B2–B5 nicht vorgezogen. Sechs Runtime-Dateien, gemeinsamer Scoutbauer und bestehende Studio-/Rojo-Kette angemessen; letzte Korrektur nur Clientlayout/Eingabe, keine neue Plattform/Agenten/Assets. Continue ausschließlich zur dokumentierten B1-Fertigstellung und normalem Commit/Push; keine weitere Produktmutation/Gesamtprüfung. Um22:46UTC ca96/120Minuten genutzt, Ende23:09:52 bleibt; kumulativ3/3Korrekturen genutzt,0übrig. Physische Mobil-/Gamepad- und integrierte Mehrspieler-/Persistenz-/Langzeitqualitätsnachweise bleiben offen.",
      "origin_run": {
        "id": "BOLTBOTS-RUN-M1-B1-001",
        "revision": 1
      }
    },
    {
      "percent": 60,
      "reviewer": "/root/b1_creator",
      "decision": "continue",
      "evidence": "Leadentscheid auf eigener Scope-/Ergebnisprüfung und ausdrücklich übernommenem unabhängigen60%-Urteil von /root/b1_review: OriginalB3 erreicht mit zwei kleinen Profil-/Storemodulen und bestehendem Main/HUD; keine B4/B5-/Art-/Plattformausweitung. Reale API-/UI-Belege tragen Ergebnis. Continue nur zu autorisiertem privatem Save und Git. Review10:50UTC83/120min, Deadline11:27 unverändert;4/6Korrekturen genutzt2übrig. Humanversandbefund bleibt offen, kein Gesamt-M1-Premiumpass.",
      "origin_run": {
        "id": "BOLTBOTS-RUN-M1-B3-001",
        "revision": 1
      }
    }
  ],
  "obligations": {
    "entry_integrity": {
      "state": "satisfied",
      "evidence": "Wiedereinstieg25.10.14:40UTC: Pflichtkette und gerouteterB4Run gelesen. Spawn/Root bestätigen externenManifestanker und95Payloadbytes, HEADee37eaa640fe4be3234c2931a912f8d0a4f1cbf8 sauber, branchcodex/initialize-boltbots; lokalerCheckpoint vorPush."
    },
    "scope_authority": {
      "state": "satisfied",
      "evidence": "Human fortsetzen erneuert begrenzteB4-Fortsetzungsautorität im selbenWorkspace; ursprünglicherEnd-to-End-Auftrag und einzigesprivateZiel gelten. Originalkriterien undB5-Abgrenzung unverändert."
    },
    "agent_start_review": {
      "state": "satisfied",
      "evidence": "AktuellerCreatorstart aufr2 undb4_review-Teilstart durchb4_spawn pass; finalerSicht-/Cleanupreviewstart aufManifest41ff75…af7b pass. b4_review Ergebnisapproved undseparateTransfermechanik bestätigt; SpawnkeinInhaltsvotum."
    },
    "human_gates": {
      "state": "satisfied",
      "evidence": "Domain/Designr3/M1 wirksam genehmigt, alle3Agenten Astra/xhigh. Humanversandbefund und Gesamt-M1-Endentscheidung bleiben offen."
    },
    "capability": {
      "state": "satisfied",
      "evidence": "BeideTestsregulärgestoppt, Simulatoraus/Automatic,Proben+Attribute+Faultabwesend;RojoPlugin getrennt/Serve91043 beendet/Portfrei auchReviewerbestätigt. Alle9Sources15:00:04direktgegenBuildbytegleich; SaveToRoblox15:00:28erfolgreich."
    },
    "mutation_boundary": {
      "state": "satisfied",
      "evidence": "EinzigerWriter b4_creator, b4_review unabhängigread-only, b4_spawnstart-only, RootRelay/Keepawake/mechanischeGitprüfung. KeineParallel-UI; exklusivCreatorbisHandoff."
    },
    "budget_stop": {
      "state": "satisfied",
      "evidence": "Fortsetzung14:40:19–15:40:19UTCinklVorbereitung; fachlicherB4Abschluss/Save15:00:28innerhalbFenster.6/6Korrekturen verbraucht0verbleiben;letzteBelegclosureapproved. M170%,keineautomatischeB5Fortsetzung."
    },
    "routed_requirements": {
      "state": "satisfied",
      "evidence": "Factory C-UPGRADE/C-SELECT/Q-FACTORY/C-JOIN/C-LEAVE und Cash/Once/Plot/Recoveryguards, Foundation H-CAP, Technikperformance1/2/4, M1-B4, Design/Premium und approvedB3-C1 gebunden."
    }
  }
}
```
<!-- task-controls:end -->

## Zweck, Grenze und Aufwand

Ein Besitzer soll seine eigene CTX-FACTORY-Werkstatt gemeinsam mit anderen Spielern zuverlässig benutzen können: Cash und Kauf bleiben serverseitig korrekt, fremde Fabriken nur sichtbar. B4 konkretisiert den bestehenden [WP01B](../packages/boltbots-wp-01b.md), keine neue Funktion. Führende [A1–B5-Arbeitsliste](../../handover.md#m1--arbeitsschritte-und-laufender-status); M1 bleibt60%, B4-Ergebnis führt erst nach tatsächlicher Abnahme zu70%. B3-C1 approved und privat gespeichert, Baseline`8857572c891fc87970f38199e5a07a7d21702ebe` sauber/gepusht.

Human B4 analog end-to-end, Fenster **25.10.2026 11:03–13:03UTC**,120min einschließlich Vorbereitung. Historische Startreserve: **4/6 Korrekturen genutzt,2verbleiben** (A2Werkzeug, B1Verpackung, B1HUD, B2Portrait/Beleg). B3 benötigte keine. KeinReset/Extension. Root hält Mac wach; keine zweite Wakeinstanz. Bei zwei erfolglosen Diagnoseversuchen enger Ansatzentscheid statt neuer Plattform. B5 und Humanbefund „Karton fährt rechts gegen Schranke/verschwindet, plausibler Versandabschluss fehlt; kurze Strecke nicht endgültiges Layout“ bleiben vor M1-Gesamtqualität ausdrücklich offen, kein Umbau in B4.

## Quellengebundener Interaktions- und Prüfdelta

Bestehende B1–B3-UI/Art/Store sind die Ausgangsfassung. Kein vorgesehener Workflowumbau. Native Studiofunktion **Server & Clients** erzeugt echte getrennte Clients und einen Server. Offizielle aktuelle [Testmodi](https://create.roblox.com/docs/studio/testing-modes) bestätigen Auswahl/Clientzahl/Start sowie EndSession. CUA bedient ausschließlich diese vorhandene Oberfläche; Diagnosebefehle in der Studio-Commandbar sind als solche gekennzeichnet und kein normaler Spielnachweis.

1. Feste Szenarien1/2/4 tatsächliche aktive Clients auf demselben Mac, gleiche Quelle und benannte Fenster-/Grafikbedingungen. Je mindestens60s Messfenster nach Ladebeginn und warmem Zustand; pro Client Frame-dt median/p95/max, OS-bezogenen Stats-Speicher Anfang/Ende, Instanzen und lokale Outputcontainer zählen; ServerHeartbeat und aktivePlots/Produktionszyklen erfassen. Mehrere Studio-Prozesse/Foreground-/Backgrounddrosselung ausdrücklich benennen, keine60fps-/Telefonbehauptung. Messverbindungen werden nach dem Fenster getrennt. [Stats](https://create.roblox.com/docs/reference/engine/classes/Stats) liefert Speicher-/Instanzwerte; Frame-dt direkt aus RunService. Aktuelle neun Runtime-Dateien: ein Server-Takt und je Client eine Renderverbindung mit30Hz-Darstellung, ein wiederverwendeter Bot/Karton pro Plot. Quelle und tatsächliche Zählung tragen die Aussage, keine vorgetäuschte globale Connectionzählung.
2. Zwei echte Clients integriert prüfen: individuelle Plots und bestätigte Profile, authentifizierte Kauf-/Design-/Manipulationsaufrufe, eigener Preis/Cash. Normale GUI-Abläufe ausB1–B3 sind getrennte unveränderte Belege; der vollständige normale Mehrspieler-/Fremdplotspielpfad bleibtB5/M1. Snapshots nur eigenes Profil ohne Sitzungs-/Storetoken. Kontrollierte echte Remoteproben: zusätzliche fremde Player-/Plotfelder, fremde machineId, falsche Typen/NaN/Inf/negative Version, unbekannter Befehl/Design, fehlender Clientabschluss, Wiederholung desselben Request und gleichzeitig ausgelöste Käufe. Vor-/Nachsnapshots jedes betroffenen Clients; währenddessen legitime Produktion über completed/earned vom Kaufdelta trennen. Null/exakterPreis/Overflow-Grenzen aus unveränderten reinen Tests übernehmen; nötige begrenzte synthetische Integration am autorisierten Testprofil klar kennzeichnen, keine ungeprüfte Geldinjektion als normale Bedienung.
3. Vier Clients müssen vier verschiedene Plots mit boundedOutputs benutzen. H-CAP verlangt klare Kapazitätsablehnung: ein zusätzlicher kurzer Beitrittsversuch darf keinen fünften aktiven Plot/Profil erzeugen; dies ist nur die Kapazitätsgrenzprobe, kein fünftes Profilszenario. Aktuelle Quelle liefertno_plot mit generischem Ladefehlertext; falls tatsächlich bestätigt, kleinste gezielte Meldung „Alle Werkstätten belegt …“ innerhalb vorhandener Recoveryfläche. Keine neue Lobby/Queue. Die unabhängige frühe Linse beurteilt diese Bedeutung vor eventueller UIänderung.
4. B3realeStore-/Fehler-/Retry-/Migrationsbelege und B1/B2Regel-/schmaleLevel01-/Modal-/Verpackungsbelege bleiben gültig. B4prüft neu gemeinsame Sitzung/Leave-Rejoin und fremdeIsolation; erforderliche Fehlerreaktion unter Mehrclientbedingungen begrenzt. Produktfehler innerhalb desselbenScopes zu einer kohärenten Korrektur bündeln, dann nur betroffene Closure.

## Historie r1 — Aktivierung und nächste Schritte

assignment_preparation pass von /root/b1_spawn für genau diesen Auftrag liegt vor. Nächster Schritt: exakte Aktivierung und frühe unabhängige Prüfung dieses Deltas; danach native Testsession/gebundene Mess- und Manipulationsbelege. Keine Produktmutation vor Startpass. Der direkte Validator darf den bekannten Human-disponierten CTX-FACTORY-Foundationbefund weiter melden; kein unechterPASS, keine Core-/Foundationänderung.

## Historie r1 — geplantes Ergebnis und offene Arbeit

Noch keine B4-Laufzeit-/Mehrclient-/Leistungsbehauptung. Offen sind nativer Start, integrierte Proben/Messung, gebundener Kandidat mit unabhängiger Ergebnisreview, mögliche in-scope Closure, aktuelle Übergabe und normale Git-Sicherung. Nur falls Produktquellen geändert werden folgt nach approval ein bytegebundener Save ins bestehende private Ziel; keine öffentliche Promotion.

## Dokumentierter Start

11:16UTC /root/b1_spawn: **pass run_activation** für Creator/Lead auf B4-Runr1, separat **pass früher Reviewerauftrag** an /root/b1_review auf exakt §Quellengebundener Interaktions- und Prüfdelta. H-CAP/SC-06 tragen kurzen abgewiesenen zusätzlichen Beitritt ohne fünften aktiven Slot. Keine Ergebnisabnahme. NativeFähigkeit wird erst jetzt tatsächlich ausgeführt. Bestehende Quelle/Core/Autorität/Budget unverändert.

## Frühe Inhaltsreview und begrenzter Ansatzentscheid

11:19UTC /root/b1_review **approved** auf den exakten frühen Delta. Je Sitzung tatsächliche IDs/saveStatus/Player-Plotzuordnung; Remoteproben mit beiden Vor-/Nachständen und legitimen Abschlüssen; Kapazitätsretry nach freiem Slot; wirklich warme60s-Messung und Host-/Fensterbedingungen sind verbindliche Nachweispräzisierungen. Kein neuer Scope. no_plot braucht die bereits vorgesehene klare Meldung; keine Queue/Lobby.

Native Test→Start Test Session→Server and Clients startet tatsächlich getrennte Prozesse. Leerer0Clientstart ordentlich beendet; anschließend1Client eingestellt und gestartet, OriginalLogs zeigenServer/Clientboot und neuesProfil0Cash. CUA macOS bindet aber nur den ursprünglichen Editor; erneute Appbindung und normale Fensterumschaltung erreichen den Childclient nicht. Nach begrenzten Fehlversuchen stoppt dieser Diagnoseweg. Kleinster bestehender Ersatz: zwei zeitbegrenzte Studio-/Ziel-geguardete Diagnose-Skripte im Testdatamodel über vorhandene Commandbar, echte Netzwerkaufrufe und Messung in jedem Client, OriginalLogs. Sie sind ausschließlich in evidence/M1-B4 dokumentiert, werden vor endgültigem Source-/Build-/Cloudstand aus Studio entfernt und gehören nicht zum Produktprojekt. Keine virtuelle GUI-Eingabe/Steuerplattform. Diese Proben sind keine normalen Kauf-/Abbruch-/Erkunden-Klickbelege; gültige normaleB1–B3Belege separat, tatsächliche verbleibende ursprüngliche Kriterien durch Reviewer beurteilen. Root ist über die konkrete Nachweisgrenze informiert.

## Kohärente B4-Korrektur und verbleibende Abdeckungsgrenze

Die unabhängige enge Abdeckungsprüfung bestätigt: Remote-/Attribut-/Messproben ersetzen den normalen integrierten Mehrspielerweg und tatsächliches Ansehen einer fremden Werkstatt nicht. Unveränderte Einzelclientbelege bleiben gültig, die konkrete neue Bedienlücke bleibt offen bis realem Nachweis oder ausdrücklicher Human-Disposition. Der letzte enge native Ansatz „eingebettetes Play → Add Clients“ wurde geprüft: AddClients ist dort deaktiviert; Test wieder gestoppt. Keine weitere Steuerplattform.

Eine zusammenhängende Korrektur der ursprünglichen Owner-/Recoverylesbarkeit: öffentliche technische OwnerUserId am Plot ohne Namen/Privatprofil; derselbe vorhandene Text zeigt lokal eigene/andere/freie Werkstatt. Die falsche globale „DEINE“-Beschriftung entfällt. no_plot erhält klare Vier-Slot-/Retryerklärung im bestehenden Recoverydialog. Keine neue Oberfläche/Queue. Mit dieser B4-Korrektur kumulativ **5/6 genutzt,1verbleibt**; Fenster13:03UTC unverändert. Temporäre Probe wurde vor eigentlichen2/4-Szenarien um verschiedene konkurrierende Request-IDs und explizit aktiven Owner beim diagnostischen Freigeben ergänzt. Erste1Clientprobe hatte lediglich einen unzulässigen privilegierten settings()-Lesezugriff; korrigierte betroffene Erfassung ist getrennt alsone-r2 belegt.

## Unabhängig korrigierte B4-/B5-Zuordnung

/root/b1_review hat anhand der ursprünglichen Baseline8857572c…2ebe eigenständig geprüft und die vorher zu weit gefasste Blockerzuordnung ausdrücklich korrigiert: Führende Handovertabelle ordnet integrierte Geld-/Kauf-/Manipulations-/Fehlerprüfung und2–4Clients B4 zu, vollständigen normalen Agent-Spielpfad/Qualitätsreview B5. Genehmigter Plan milestones.md:43 verlangt normalen Agent-Spielpfad einschließlich fremdenPlot für WP01B/M1 insgesamt; :52 echteZwei-Client-Isolation, :57 Profiling2–4; Technik:41 verlangt1/2/4Basis, :58 echteClientpfade insgesamt. Keine Quelle verlangt normaleGUI-Handlungen in jedem Client oder deren Abschluss bereitsB4.

Die anfängliche Runmethode „Zwei Clients normal spielen“ war daher stärker als das ursprüngliche B4-Ergebnis. Sie wird transparent präzisiert: tatsächliche getrennte Childclients und authentifizierte integrierte Proben können B4 technisch belegen; kein normalerKlickbeleg wird daraus abgeleitet. Vollständiger normaler Spiel-/Erkundungs-/Fremdplotnachweis bleibt **OFFEN beiB5 und vorM1-Gesamtabnahme**, mit bestätigter macOS-CUA-Childfenstergrenze. Keine Anforderung gestrichen, kein Humanwaiver nötig. B4 nicht vorabapproved: technischePflichtbelege, H-CAP/Retry und betroffene Owner-/Recovery-UI bleiben zuprüfen. DirekterCheck auf geänderte Abgrenzung folgt; bekannteFoundationausnahme bleibt unverändert.


## B4-C1 — gebundener technischer Teilkandidat / offener Abschluss

Manifest [candidate-manifest.json](../../reviews/evidence/M1-B4/candidate-manifest.json), SHA256 `f1d0cab146d65fef05ff76c06dc656385c708c959bf82ac6758858617e58e16c`,22Dateien; Build`28c95843a8fb9ecc12d1abf4f9b26e99a819e2a24b771b2d670903b1e5882654`. [Belegindex](../../reviews/evidence/M1-B4/README.md) trennt tatsächliche normale historische Wege, echte aktuelle Netzwerk-/Kapazitätsproben und Messgrenzen. scripts/check.sh erfolgreich; vier kleine Runtimeänderungen fürOwner-/Kapazitätsorientierung, keine neue Plattform.

Reale1/2/4Nativeclients, richtige privateIDs, getrennteProfile/Plots, echteManipulationsablehnungen, je einmal50Cash bei gleichen bzw. verschiedenen konkurrierendenKaufabsichten undOrbitfolgezyklus belegt. Fünf tatsächliche Beitritte erzeugen vieraktiveSlots;−5 erhältno_plotohneProfilersatz und nimmt nach diagnostischemLeave vonOwner−1 überechtenRetryPlot1/Scoutproduktionan. Speicher-/Fehlerregeln ausapprovedB3unverändert. Hohe lokaleClientframezeiten auf16GB/M2, kein60fps-/flüssigeVierclient-/Endgeräteclaim.

**Offen bleiben** tatsächlicher Screenshotvergleich eigene/andereOwnerbeschriftung und zusätzliche schmaleSicht des neuenno_plotTexts. Letzterer ist im wirklichen fünftenClient als sichtbar undTextFits=true geloggt, aber keinScreenshot. KeineB4-Premium-/GesamtabnahmeausQuelltext. Der vollständige normaleSpiel-/Fremdplotweg bleibt originalB5/M1, Humanversandbefund ebenfalls offen.

Hostlast verhinderte nach den Proben den regulärenEndSession-/Editorzugriff: CUA73/91/81sTimeout. Sandboxpsverweigert; zwei engeautomatischeGenehmigungsprüfungenliefeninTimeout, keineSicherheitsablehnung und keineTerminierungausgeführt. KeinePIDgeraten/Umgehung. **Cleanup nicht bestätigt**: Testchildprozesse, zweiB4TemporaryProbe-Objekte undWorkspaceattribute könnennochaktivsein; RojoServeSession56649 ebenfallsbisbereinigtemAbschluss. Originaleditor/ungespeicherterStandnichtverworfen. VorprivatemB4Save zwingend regulärstoppen,Probeobjekte/Attributeentfernen,alle9Sourcesbytegleichprüfen. **KeinB4Cloudsave**, genehmigteprivateFassungbleibtB3.

Finaler enger Reviewerauftrag: technischeOriginalabdeckung/Belegbindung, echteKapazitäts-/Manipulationsregeln,Leistungsgrenzen, kleinerOwner-/Recoverydelta unddrift/KISS; fehlendeSicht/Cleanupoffenlassen, keinenGesamtpasskonstruieren. ExakterSpawnstartangefordert; M1bleibt60%. Fenster11:03–13:03UTC,5/6Korrekturengenutzt1übrig; keinReset/Verlängerung. BeiFensterende sichererTeilcheckpoint stattfalschemB4-done.


## Fortsetzung r2 — 25.10.2026,14:40:19–15:40:19UTC

Human „fortsetzen“ gilt als neue begrenzte Fortsetzungsautorität für den unvollständigenB4-Auftrag, nicht als neuerRun oderBudgetreset. GleichesRepository/Workspace, lokaler saubererCheckpoint`ee37eaa640fe4be3234c2931a912f8d0a4f1cbf8`; NormalerPush undliveRemote-ID`ee37eaa640fe4be3234c2931a912f8d0a4f1cbf8` durchRoot14:46UTC bestätigt. Keine Personen-/Maschinenübergabe: derselbe lokaleHumanauftrag wird mit ausdrücklich ersetzten Agentkontexten fortgesetzt; Originalzustand/Belege bleiben erhalten. Zwei arbeitendeRollen plusStartreviewer, max3operativ; Root ausschließlichRelay/Keepawake/Gitmechanik. HistorischeRollenaktivierungen plus dreiErsatzkontexte transparent, keinvierterarbeitenderReviewer.

Ziel bleibt eine zugängliche attraktiveRoboterfabrik fürRoblox-Fabrik-/Sammelspieler inCTX-FACTORY; M1 ist die kleineQualitätsreferenz. B4 liefert zuverlässigesGeld/Eigentum undgemesseneMehrclientgrenzen. KeineGesamtspiel-Premiumfreigabe; normalerFremdplotpfad undHumanversandbefundbleibenB5/M1.

Aktueller nächsterSchritt: r2direktprüfen/aktivieren; danach bestehendesprivateZielöffnen und aktuelleB4Byteswiederherstellen. Studiozeigt14:44UTC Home, keinoffenesEditdokument, UIantwortetwieder. HistorischeTestsessionnichtalsdurchunsregulärbeendetbehaupten; tatsächlicheneueSession mussProbe-/Attributfreiheitund9Sourcesprüfen. RootbestätigtRojo34872ohneListener. DiefehlendenSichtbelege werden ineinerleichten eingebettetenPlay-Sitzung alsdiagnostischeDarstellung eigener/anderer/freierOwnertexte unddesno_plotRecoveryzustands erstellt, ausdrücklichkeinneuernormalerMehrspielerbeleg. Keineerneuten1/2/4-Messserien. ReviewerprüftparallelgebundenenTechnikteil; spätereSicht-/Cleanupbindung alsengerDelta. Danach nurbeiunabhängigemPass bytegebundenerSaveinsgleicheprivateZiel undGitabschluss.

Ansatzentscheid nach historischenCUA-Timeouts: NeueEvidenzistdererreichbareHomezustandohnealteLast. KleinsterWegbleibt vorhandenesStudio/Rojo, eineeingebetteteSession. NachhöchstenszweierneutengezieltenUIfehlschlägen erneuterStopp/Ansatzentscheid, keineChildroutingexperimenteoderneuePlattform. NochkeineProduktänderung/zusätzlicheKorrektur.

AktuellerStart vor14:47UTC: /root/b4_spawn **PASS run_activation** fürCreatoraufexakterr2/Fortsetzungsroute. Separater**PASS** fürb4_reviewauftechnischenTeilmanifestf1d0cab…e16c/22Dateien, ohneSicht-/Gesamtabnahme.


## Abschlusskandidat der Fortsetzung — Sicht und Cleanup

Alle ursprünglichen B4-Technikkriterien sind durch /root/b4_review unabhängig positiv geprüft. Die aktuellen PNGs/Originalzeilen im Belegindex ergänzen eigene normale Beschriftung, diagnostische andere/freie Beschriftung und tatsächliche no_plot-Darstellung auf Desktop/Portrait/Querformat. Portrait413×756, Titel/Text passen, Retry349×48. Tatsächliche GrafikAutomatic; kein erfundenerLevel01-Nachweis. Die ursprünglichen1/2/4-Messungen werden nicht wiederholt. B5-Spiel-/Fremdplotweg und Humanversandbefund bleiben offen.

Aktueller Cleanup bestätigt: beide eingebetteten Tests regulär gestoppt; keine B4Probeobjekte/Attribute oder B3Fault, Simulatoraus, GrafikAutomatic, RojoPlugin getrennt, eigener Serve91043 beendet, Port34872ohneListener. Historischer unbeobachteter Abbruch bleibt als solcher erhalten. Sourcegleichheitaller9Dateien im echtenprivatenPlace14:48:18 nachgewiesen; unmittelbar vor dem autorisiertenSave nochmals fällig. NochkeinB4Cloudsave.

Die unabhängige Technikreview hat zwei minor/evidence_accuracy-Präzisierungen konsolidiert: früheControlMarker sindkeinNachherbeleg, vorhandene spätereCapacityProfiletragenIsolation; 8Modelle sind4Roboter+4Kartonmodelle, keinScout-/Orbitpaar. Belegindex jetzt entsprechendkorrigiert. Kein Runtimebefund, keine neue Messung. Konservativ zählt diese kohärente Dokumentationskorrektur als letzterZyklus: **6/6genutzt,0verbleiben**, Closure diesesZyklus bleibt zulässig. KeinBudgetreset. Neuer finalerSicht-/Cleanupreviewstart wird exaktmanifestgebunden angefordert.

Finaler enger Start: /root/b4_spawn **PASS** für /root/b4_review auf Manifest`41ff75e3d4f3aaa19304653755f6d77e1b629e5fc882b18d152ba2b6c418af7b`,30Dateien und unverändertenBuild. Nachweisbindungen mechanisch bestätigt; keineInhaltsabnahme durchSpawn. Reviewer prüft Sicht/Premiumeng,Diagnostikgrenzen,beideBelegkorrekturen und aktuellenCleanup. CreatorUIbisErgebnispausiert.


## Finale unabhängige Ergebnisreview — B4 approved

`/root/b4_review` bestätigt **APPROVED** auf Manifest `41ff75e3d4f3aaa19304653755f6d77e1b629e5fc882b18d152ba2b6c418af7b` mit30Dateien und Build `28c95843a8fb9ecc12d1abf4f9b26e99a819e2a24b771b2d670903b1e5882654`. Alle31Bindungen unabhängig geprüft, siebenPNG tatsächlich angesehen,13Resumezeilen bytegleich mit dem OriginalStudioLog. Die technische Teilreview rekonstruierte79Events aus192Originalzeilen in20Logdateien. Runtime/Tests/Build sind seit dem technischen Teilcheckpoint unverändert; keine zusätzliche breite Testsuite ohne geänderten Input.

Beide minor/evidence_accuracy-Findings geschlossen: spätere echteCapacity-Snapshots tragen die Nachherisolation; achtModelle bedeuten vierRoboter und vierKartonmodelle. Eigene/andere/freie Schilder sowie no_plot auf Desktop/Querformat/Portrait sind vollständig gerendert. Diagnostische Darstellung ist sauber von echter Mehrclientkapazität und normalem Spielen getrennt. Aktueller Cleanup durch Edit-/Connectbild und Originalzeilen bestätigt; Reviewer sah Port34872 ebenfalls ohneListener.

**Unabhängiges visuelles Urteil: ansprechend — ja.** Helles Werkstattschild und ruhige navy/cyan Fehlerkarte passen zur bestehenden Szene und bewahren eine klare Hierarchie. **Unabhängiger Fortsetzungsanreiz: ja, für diesen engen Delta.** Richtige Besitzorientierung und der verständliche freie-Platz-/Retryweg nehmen Unsicherheit und führen zur eigenen Roboterproduktion zurück. Die Creatorurteile im gebundenen Belegindex sind getrennt positiv. Keine Nutzerpräferenzmessung, kein Gesamtspiel-/Versandpass; die Humanablehnung zum Versandabschluss bleibt maßgeblich offen.

### Originalkriterien und tatsächliche Abdeckung

| Quelle / Pflicht | Tatsächlicher Nachweis und Grenze |
|---|---|
| M1-Plan Geld/Eigentum; Factory C-UPGRADE/C-SELECT/Q-FACTORY; Foundation SC03/04 | Vier authentifizierte Clients mit eigenen Profilen/Plots,20 ungültige Grenz-/Fremd-/Abschlussfälle ohne Zusatzcash; gleicheRequestIDs und verschiedenealteAbsichten jeweils genau50Cash/einL2+Orbit. Spätere Kontrollstände ergeben Netto0 nach legitimen25erAbschlüssen. |
| Foundation SC06/H-CAP, C-JOIN/INV-PLOT/RECOVERY | Fünf realeBeitritte, genauvieraktiveSlots; −5no_plotohneProfilersatz; nachLeave eines aktivenOwners echterRetryzuPlot1/Scout. NeueScreens ergänzen ausschließlich die Lesbarkeit. |
| Technik Leistungsbasis, M1 begrenzteLaufzeit | Reale1/2/4-Szenarien jeweils mindestens60s, Frameverteilungen/Prozessspeicher/ServerHeartbeat; lokaleOutputs begrenzt. Hohe4Clientwerte70–149msMedian/172–470msp95 erlauben keinen Flüssigkeits-,60FPS- oderEndgeräteclaim. |
| Q-PUBLIC/INV-READ und engePremiumregel | Nur nötigeOwnerreferenz/öffentlicheGeometrie/Zyklus/Level; keinePrivatprofile/Storetoken. TatsächlicheSchilder/Recoverybilder, positivegetrennteCreator-/Reviewerurteile. |
| B3 und unveränderteB1/B2-Regeln/UI | BytegleicheRegel-/Storetests und approvedSave/Recovery-/Migrations-/Kauf-/Abbruchbelege wiederverwendet. Kein erneuterTest allein wegenResume. |
| WP01B/M1 normalerAgent-Spielpfad, Humanversandfeedback | BleibtB5/M1offen. MehrclientRemoteproben sind kein normalesFremdplot-Erkunden. KeinScopewegfall und keineGesamtspiel-Premiumabnahme. |

### Ereignisbezogener Abschluss-Drift und KISS

Originalziel ist verlässliches eigenes Geld/Eigentum in der gemeinsamen Roboterfabrik plus ehrliche lokale Leistungsbasis. Tatsächlich geändert wurden vier kleine Runtime-Dateien für die öffentliche Besitzerreferenz, die lokale Beschriftung und den klaren Kapazitätstext; vorhandeneRecoveryfläche und Testwerkzeuge genügen. Temporäre Proben sind entfernt. Keine neue Plattform, Welt, Versandfunktion oder abstrakte Infrastruktur. Unabhängiger Reviewer bestätigt diese Zuordnung und den einfachen Ansatz. Entscheidung: **continue ausschließlich zur autorisierten Sicherung, danach complete fürB4**; B5 wird nicht automatisch begonnen.

CumulativeM1Reserve6/6genutzt,0verbleiben; letztegebündelteBelegkorrektur undClosure abgeschlossen. HistorischesB4Fenster11:03–13:03bleibt erhalten. Die ausdrücklicheHumanfortsetzung14:40:19–15:40:19UTC einschließlichVorbereitung ermöglichte den konkretenRest; Ergebnis/Save nach rund20Minuten. Keine nachträglich erfundeneTimeliness für die frühereUnterbrechung. OriginalEinclientbasis vorreinemBeschriftungsdelta, aktuelleZwei-/Vierclientbasis undaktuellerSichtdelta sindweiter klar getrennt.

### Autorisierter privater Save und aktueller Übergabestand

[Separater Transferbeleg](../../reviews/evidence/M1-B4/approved-private-transfer.log) liegt außerhalb des eingefrorenen Reviewpayloads.15:00:04UTC wurden alle neun tatsächlichen Studio-Sources direkt mit den aus dem gebundenen `.rbxlx` gelesenen Sourcebytes verglichen; alleAssertions bestanden. RichtigeUniverse10772906084/Place112662761038118, Editmodus, keineB4Probeobjekte/Attribute, keinB3Fault, GrafikAutomatic.

NativeAktion **File → Save to Roblox**:15:00:27.954UTC bestätigteStudioSavePlaceToCloud1791ms, anschließendPublishSuccessful und15:00:28.101UTC „Saved new changes“ im gleichen privatenZiel. Der aktuelleFenstertitel schreibt „BoltBots B3-Test 20261025“ mitBindestrich; die IDs sind unverändert, keineRenameaktion. KeinöffentlicherPublish und keinCloud-Kaltabruf behauptet. Reviewer bestätigte alle vier Transferzeilen gegen das OriginalLog sowie unveränderte30Dateien/Build und leerenRojoport.

**B4 abgeschlossen, M1 70%.** Studio verbleibt Edit/Playstop/Simulatoroff/Automatic; Rojo getrennt undServerbeendet. Die normaleGit-Sicherung diesesAbschlusses wird durch die abschließende lokale/Remote-ID belegt. Nächste fachlicheArbeit ist B5 einschließlichnormalemSpiel-/Fremdplotweg und Humanversand-/Gesamtqualität, unter eigener weitererAutorität und ohne verfügbarenKorrekturreset.


### Abschlussmetadaten zur Spawn-Startdisposition

Der direkteCompleted-Check verlangte zunächst eineStartdisposition für jede derdrei zuRechtallokiertenIdentitäten. `decision.agents` behält gemäßAdmission§2 alle drei Rollen. `cleared_agents` enthält nun auch `/root/b4_spawn` ausdrücklich aufgrund des tatsächlich erfolgten Bootstrap aus integritätsgeprüfter Rolle und Pflichtkette, der einzigen Rekursionsausnahme aus Collaboration§1.1 / `.agentic-harness/roles/spawn-reviewer.md`. Dies ist **keine Selbstreview, kein eigener Spawn-pass und keine Produkt-/Quorumstimme**. Spawn hat diese genaue Metadatenzuordnung bestätigt. Keine neueAktivierung, fachlicheÄnderung, Korrektur oder Ergebnisreview; der gebundeneInhalts-/Savepass bleibt unverändert. Danach meldet derdirekteCheck nur noch den bekannten ausdrücklichHuman-disponiertenFoundationbefund, keinunechterGesamt-PASS.
