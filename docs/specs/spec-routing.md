# Product Spec Routing

> Artifact class: Navigation
> Linked owners: `.agentic-harness/core/routing.md`, product specifications, Work Contracts, and evidence indexes named below

## Startup

Für jede Gestaltung und Spiel-/Designreview verpflichtend: [Produktregel Premium-Qualität und menschlicher Spielanreiz](../agent-extensions.md). Design r2 wurde abgelehnt; die neue Gestaltung r3 und anschließend das Gesamtpaket für M1 sind jetzt vom Human genehmigt. Wirksame externe Entscheidung: [Initialisierungsreview r3](../reviews/20261024-1.5.3-boltbots-initialization-review.md).

Before task routing, read root `README.md`, `docs/handover.md`, `.agentic-harness/manifest.md`, and
the effective Domain Foundation and active Product Vision Brief when they exist. Only
`domain_foundation` may start from exact Human/Bootstrap/input authority; after its Human Gate,
`bootstrap_initialization` binds the effective Foundation while creating the candidate Vision.

## Initial State

- New-product initialization: `.agentic-harness/workflows/initialize-product.md`
- Domain Foundation, Bounded Contexts, Context Map, domain review/gate, or Context coverage: `.agentic-harness/core/domain-modeling-and-bounded-context-architecture.spec.md`
- Existing-product staged adoption and coverage ratchet: `.agentic-harness/workflows/adopt-existing-product.md`
- Delivery Slice execution and Product Delivery Release Candidate: `.agentic-harness/workflows/execute-work.md`
- Product application version, Product Release Policy, intended version/tag, release record, or current-serving version: `.agentic-harness/core/product-release-versioning.spec.md`; execute publication only through `.agentic-harness/workflows/promote-production.md`
- Privileged Product access applicability/bootstrap planning: initialize via `.agentic-harness/workflows/initialize-product.md`; execute Staging evidence via `.agentic-harness/workflows/execute-work.md`; authorize any real Production enrollment only through `.agentic-harness/workflows/promote-production.md`
- Resume/transfer of a Slice, Package, Experiment, or Run: `.agentic-harness/workflows/resume-work.md`
- Optional task logging or requested analysis of existing reports: `.agentic-harness/workflows/harness-logging.md`; disabled by default, not another proposal intake.
- Product-originated Harness learning or observed Harness failure: `.agentic-harness/workflows/propose-harness-improvement.md`; use only one dated narrative file under `docs/harness-proposals/**`
- Core topic-to-file route: `.agentic-harness/core/routing.md`; then read only the exact installed core file named for the task.
- Role selection and review questions: `.agentic-harness/roles/team.md`; exact Agent-start control role: `.agentic-harness/roles/spawn-reviewer.md`
- Current product state and next action: `docs/handover.md`
- Bootstrap/install/integrity state: `docs/harness-state/bootstrap-and-installation.md`
- Human-provided input: `product-input/README.md` and named files beneath `product-input/`

Initialization replaces this initial map with narrow routes to actual global specs, Product/Vision Brief, Domain Module Entry Maps, public contracts, orchestration, design, planning, work, reviews, evidence, and proposals. Do not add routes to empty or hypothetical directories.

## BoltBots Domain-Phase

- Aktive Autorität, Arbeitsliste und Kontrollen: [Domain-Run](../work/runs/boltbots-domain-foundation-001.md).
- Benannte alternative Humanquelle, statt eines künstlich duplizierten product-input/prd.md: [unveränderter PRD-Snapshot](../product/reference/boltbots-v0.2/docs/PRD.md), [Inputmanifest](../product/input-snapshot-manifest.json), [Gesprächsergänzungen](../product/human-input.md).
- Alle importierten Playbooks, Roadmaps, Architektur- und Codevorlagen sind nicht normative Eingaben. Es gilt der installierte Core mit dem aktuellen Humanauftrag.
- Fachliche Grundlage (Humanfreigabe im verlinkten Review erteilt; Kandidatenbytes unverändert): [Domain Foundation, Kontext CTX-FACTORY und gebundene Diagramme](../domains/domain-foundation.md).
- Human-Domain-Entscheidung und unabhängige Review: [Review-Paket](../reviews/20261024-1.5.3-boltbots-domain-foundation-review.md). Der Run hält den offenen Validatorbefund F-02 und den sicheren Wiederaufnahmestand.

## Freigegebene Produktgrundlage und nächster M1-Schritt

- Abgeschlossener führender [Initialisierungs-Run](../work/runs/boltbots-initialization-001.md); Domain-Run ist historischer Vorgänger.
- Pflichtkontext nach Foundation: [Vision/MVP r2](../product/vision-and-mvp.md), wirksam durch die externe Human-Gesamtfreigabe. Die eingefrorenen Kandidatenheader sind historische Metadaten; genehmigte Inhalte bleiben bytegleich.
- CTX-FACTORY Module Entry Map, öffentliche Target-Verträge, Userflows/Trace: [Factory r1](factory-module.md).
- Globale Technik, ADR-01 Roblox-Lieferweg, Releasepolitik: [Technik r1](technical-foundation.md).
- Visuelle Quellen/Design System/Mockupvertrag: [Design r3](../design/design-reference.md).
- Meilensteine, Walking Skeleton, WP/Run-Vorschläge: [Plan r2](../planning/milestones.md).
- Lokale Einrichtung und nachgewiesene Grenzen: [Setup r1](../setup.md).

M1 ist vom Human genehmigt, aber noch nicht umgesetzt. Nächster Ausführungsschritt: bestehenden Plan in den konkreten M1-Auftrag übernehmen, tatsächliche Fähigkeiten/Tools prüfen und anschließend lokale Umgebung sowie erste echte Spielversion aufbauen. Keine erneute Fach-/Bild-/Initialisierungsfreigabe für unveränderte Inhalte.
