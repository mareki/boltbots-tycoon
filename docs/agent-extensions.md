# Produktregeln — Qualität aus Spielersicht

> Artifact class: Product guidance
> Authority: ausdrückliche Humananweisung vom 24. Oktober 2026
> Applies to: jede Gestaltung und jede Spiel-/Designreview dieses Projekts

## Verbindliche Abnahmebedingung

**Premium-Qualität ist Pflicht.** Bei jedem gestalteten Ergebnis prüfen Creator und unabhängiger Reviewer ausdrücklich: **Ist das für Menschen ansprechend? Macht es Lust, dieses Spiel zu spielen?** Bei einer negativen Antwort wird das Ergebnis nicht abgenommen. Technische Korrektheit, vollständige Abläufe, Lesbarkeit oder erfolgreiche automatische Checks gleichen fehlende visuelle Qualität und fehlenden Spielanreiz nicht aus.

Das gilt für Welt/Bühne, Roboter, Maschinen, Oberflächen, Animationen und ihr Zusammenspiel — ausdrücklich auch für eine interaktive Designreferenz. Ein grober Strukturentwurf darf als Arbeitsmittel dienen, aber weder als Premium-Referenz noch als freigegebene Gestaltungsgrundlage ausgegeben werden.

## Anwendung in der vorhandenen Review

- Tatsächlich gerenderte Ansichten und, sobald vorhanden, echte Spielszenen ansehen. Mit den benannten menschlichen Referenzen und dem zugesagten Qualitätsniveau vergleichen.
- Eigenständige, attraktive Charaktere; überzeugende Formgebung, räumliche Wirkung, Materialien und Licht; bewusste Komposition; zusammenhängende Farb-/Formensprache; visuelle Belohnung und ein einladendes Spielerlebnis beurteilen. Ein fachlich korrekter Wireframe beantwortet diese Fragen nicht.
- **Visuelle Qualität und Spielanreiz getrennt von Technik/Bedienbarkeit bewerten.** Im bestehenden Review klar begründen, warum das konkrete Ergebnis Menschen ansprechen soll; tatsächliche Schwächen benennen. Keine pauschale Zustimmung aufgrund einer Checkliste oder erfüllter Mindestschriftgrößen.
- Fehlt eine tragfähige positive Bewertung, bleibt die Designabnahme offen. Bei „Nein“ lautet das Ergebnis `changes_requested` beziehungsweise `rejected`; weder Zeitdruck noch bisheriger Aufwand machen daraus `approved`.
- Die Bewertung eines Agenten ist keine Messung der Präferenz aller Menschen. Echte Spielerreaktionen und die Qualitätsentscheidung des Human bleiben maßgeblich. Eine ausdrückliche Human-Ablehnung kann nicht durch ein früheres Agent-`approved` übergangen werden.

Diese Regel ergänzt die bestehenden fachlichen, technischen und visuellen Prüfungen. Sie benötigt keine zusätzlichen Agenten, Formulare oder Freigabestufen; sie ist ein harter Bestandteil der ohnehin erforderlichen Review.

## Konkreter Ausgangsbefund

Die interaktive Referenz unter `docs/design/reference/`, Designrevision 2 / Kandidat `89a83ae`, wurde vom Human als minderwertig und nicht spielanregend abgelehnt. Sie ist historische Arbeitsevidenz und **keine freigegebene Designgrundlage**. Ein zukünftiger Kandidat muss diesen Qualitätsmangel beheben; die bisherige technische/lesbarkeitsbezogene Review ersetzt das nicht.
