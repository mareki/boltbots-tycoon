#!/usr/bin/env python3
"""Read-only structural validator for Master, release, and Product repositories."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


KNOWN_CLASSES = {"Constitutional", "Harness specification", "Profile", "Product specification", "Decision record", "Review record", "Work contract", "Editable source", "Generated view", "Evidence", "Navigation", "Reference"}
RELEASE_INSTALL_TOKEN = re.compile("<" + r"<AH_(?:RELEASE|INSTALL):[A-Z][A-Z0-9_]*>" + ">")
INSTANCE_MARKER = re.compile(r"\{\{[A-Z][A-Z0-9_\.]*\}\}")
ARTIFACT_ID = re.compile(r"^> Artifact ID:\s*`?([^`\s]+)`?", re.MULTILINE)
ARTIFACT_CLASS = re.compile(r"^> Artifact class:\s*([^\n]+?)\s*$", re.MULTILINE)
STATUS = re.compile(r"^> (?:Status|Revision status):\s*`?([^`\n]+)`?\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
RELEASE_TAG = re.compile(r"^([0-9]{8})-((?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*))-[a-z0-9]+(?:-[a-z0-9]+)*$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
SECRET_PATTERNS = {
    "aws-access-key": re.compile("AKIA" + r"[0-9A-Z]{16}"),
    "private-key": re.compile("-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github-token": re.compile("gh" + r"[pousr]_[A-Za-z0-9]{30,}"),
}
RUN_TRANSITIONS = {
    ("none", "proposed"), ("proposed", "preflight"), ("preflight", "preflight_blocked"),
    ("preflight_blocked", "preflight"), ("preflight", "authorized"), ("authorized", "active"),
    ("active", "verification"), ("active", "paused"), ("verification", "paused"),
    ("active", "blocked"), ("verification", "blocked"), ("paused", "active"),
    ("blocked", "preflight"), ("blocked", "active"), ("verification", "changes_requested"),
    ("changes_requested", "active"), ("verification", "completed"),
}


def valid_release_tag(value: str, version: str | None = None) -> bool:
    match = RELEASE_TAG.fullmatch(value)
    if not match or (version is not None and match.group(2) != version):
        return False
    try:
        datetime.strptime(match.group(1), "%Y%m%d")
    except ValueError:
        return False
    return True

EFFORT_PROFILES = {
    "D0": {"implementers": 1, "reviewers": 0, "active": 1, "initial_reviews": 0, "corrections": 0, "closures": 0},
    "D1": {"implementers": 1, "reviewers": 1, "active": 2, "initial_reviews": 1, "corrections": 1, "closures": 1},
    "D2": {"implementers": 1, "reviewers": 2, "active": 3, "initial_reviews": 1, "corrections": 2, "closures": 2},
    "D3": {"implementers": 1, "reviewers": 2, "active": 3, "initial_reviews": 1, "corrections": 2, "closures": 2},
}
CLASS_TRIGGERS = {
    "D0": {"mechanical"},
    "D1": {"bounded_reversible"},
    "D2": {"delivery_slice", "material_user_flow", "significant_ui", "public_contract", "multi_domain", "architecture_boundary", "security_privacy_design", "material_reslice"},
    "D3": {"initialization", "mvp_milestone_acceptance", "production", "live_customer_data", "destructive_irreversible", "material_cost", "harness_evolution"},
}
NON_TERMINAL = {"proposed", "preflight", "preflight_blocked", "authorized", "active", "verification", "paused", "blocked", "changes_requested"}
SPEC_REQUIRED = ("Artifact ID", "Artifact class", "Authority", "Status", "Semantic owner", "Version", "Review")
HIP_FILENAME = re.compile(r"^docs/harness-proposals/[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
REVIEW_FILENAME = re.compile(
    r"^(?P<date>[0-9]{8})-(?P<version>(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*))-(?P<name>[a-z0-9]+(?:-[a-z0-9]+)*)-review\.md$"
)
HIP_REQUIRED_METADATA = (
    "Artifact ID", "Version", "Status", "Decision class", "Submitted at",
    "Source Product ID", "Installed Harness version", "Installed Harness manifest SHA-256",
    "Evidence custodian/access/retention", "Author/material contributors",
    "Independent reviewers", "Semantic owner", "Human Proposal Authority", "Confidentiality",
)
HIP_REQUIRED_HEADINGS = (
    "## Executive Narrative",
    "## Original Human Assignment And Reasonable Expectation",
    "## Observed Product And Agent Chronology",
    "## Agent Collaboration And Review Behavior",
    "## Evaluation Of The Result",
    "## Product, User, Cost, Rework, And Trust Impact",
    "## Confirmed Observations, Human Reports, Hypotheses, And Open Decisions",
    "## Generalization, Applicability, And Counterexamples",
    "## Requested Reusable Outcomes",
    "## Alternatives, Simplicity, And Cost",
    "## Expected Compatibility, Migration, Validation, And Evaluation",
    "## Acceptance Criteria",
    "## Anti-Criteria And Non-Goals",
    "## Evidence, Provenance, Rights, And Data Minimization",
    "## Independent Findings, Dispositions, Dissent, And Human Decision",
)
SCOPE_PATH_MAP = re.compile(
    r"<!-- scope-path-map:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- scope-path-map:end -->",
    re.DOTALL,
)
MISSION_CONTRACT_BLOCK = re.compile(r"<!-- mission-contract:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- mission-contract:end -->", re.DOTALL)
MISSION_CHECKPOINT_BLOCK = re.compile(r"<!-- mission-checkpoint:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- mission-checkpoint:end -->", re.DOTALL)
MISSION_PACKAGE_BLOCK = re.compile(r"<!-- mission-package:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- mission-package:end -->", re.DOTALL)
CONVERGENCE_BUDGET_BLOCK = re.compile(r"<!-- convergence-budget:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- convergence-budget:end -->", re.DOTALL)
CONVERGENCE_COUNTERS = {"agent_activations", "review_cycles", "remediation_attempts"}
CORRECTION_AMENDMENT_BLOCK = re.compile(r"<!-- correction-amendment:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- correction-amendment:end -->", re.DOTALL)
CORRECTION_AUTHORITY_MIN_VERSION = (1, 0, 11)
DIRECT_RUN_MIN_VERSION = (1, 2, 7)
DOMAIN_FOUNDATION_MIN_VERSION = (1, 3, 0)
DOMAIN_FREE_DELIVERY_MIN_VERSION = (1, 4, 1)
LEAN_WORKING_TEAM_MIN_VERSION = (1, 4, 0)
PROPORTIONATE_EXECUTION_MIN_VERSION = (1, 5, 0)
LEASE_FREE_MIN_VERSION = (1, 5, 2)
DIRECT_RUN_BLOCK = re.compile(r"<!-- run-contract:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- run-contract:end -->", re.DOTALL)
DIRECT_RUN_STATUSES = {"approved", "active", "verification", "blocked", "completed", "cancelled"}
TASK_CONTROLS_MIN_VERSION = (1, 3, 1)
TASK_CONTROLS_BLOCK = re.compile(r"<!-- task-controls:start -->\s*```json\s*(.*?)\s*```\s*<!-- task-controls:end -->", re.DOTALL)
TASK_OBLIGATIONS = {
    "entry_integrity", "scope_authority", "agent_start_review", "human_gates",
    "capability_lease", "mutation_boundary", "budget_stop", "routed_requirements",
}
TASK_CONDITIONAL_OBLIGATIONS = {"agent_start_review", "human_gates", "capability_lease"}
DRIFT_DECISIONS = {"continue", "simplify", "rollback", "reimplement", "checkpoint_and_escalate"}
DOMAIN_FOUNDATION_BLOCK = re.compile(r"<!-- domain-foundation:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- domain-foundation:end -->", re.DOTALL)
DOMAIN_REVIEW_BLOCK = re.compile(r"<!-- domain-review:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- domain-review:end -->", re.DOTALL)
DOMAIN_CONTEXT_BLOCK = re.compile(r"<!-- domain-context:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- domain-context:end -->", re.DOTALL)
BROWNFIELD_ADOPTION_BLOCK = re.compile(r"<!-- brownfield-adoption:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- brownfield-adoption:end -->", re.DOTALL)
DOMAIN_BINDING_BLOCK = re.compile(r"<!-- domain-binding:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- domain-binding:end -->", re.DOTALL)
LEGACY_DOMAIN_EXCEPTION_BLOCK = re.compile(r"<!-- legacy-domain-exception:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- legacy-domain-exception:end -->", re.DOTALL)
DOMAIN_COVERAGE = {"legacy_unmodeled", "partially_modeled", "domain_model_effective"}
ADMISSION_PROJECTION_BLOCK = re.compile(r"<!-- admission-projection:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- admission-projection:end -->", re.DOTALL)
ADMISSION_REPORT_BLOCK = re.compile(r"<!-- admission-report:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- admission-report:end -->", re.DOTALL)
ADMISSION_RULESET = "AH-ORDINARY-ADMISSION-1"
ADMISSION_MIN_VERSION = (1, 0, 10)
ADMISSION_ACTIVE_TRANSITIONS = {("authorized", "active"), ("paused", "active"), ("blocked", "active"), ("changes_requested", "active")}
ADMISSION_RULE_RESULTS = (
    "contract_identity", "run_kind_context", "installed_core_integrity",
    "scope_reasoning_budget", "lease", "transition_binding",
)
CONTRACT_REVISION_MIN_VERSION = (1, 1, 0)
CONTRACT_REVISION_BLOCK = re.compile(r"<!-- contract-revision:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- contract-revision:end -->", re.DOTALL)
CONTRACT_REVISION_EVENT_BLOCK = re.compile(r"<!-- contract-revision-event:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- contract-revision-event:end -->", re.DOTALL)
VISUAL_ASSURANCE_MIN_VERSION = (1, 0, 13)
VISUAL_ASSURANCE_BLOCK = re.compile(r"<!-- visual-assurance:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- visual-assurance:end -->", re.DOTALL)
VISUAL_REVIEW_BLOCK = re.compile(r"<!-- visual-review-evidence:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- visual-review-evidence:end -->", re.DOTALL)
VISUAL_REVIEW_AXES = {"composition", "hierarchy", "proportions", "density_whitespace", "clipping", "consistency", "usability"}
AGENT_START_MIN_VERSION = (1, 2, 0)
AGENT_START_PLAN_MIN_VERSION = (1, 2, 1)
AGENT_START_CONTROL_BLOCK = re.compile(r"<!-- agent-start-control:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- agent-start-control:end -->", re.DOTALL)
AGENT_ACTIVATION_BLOCK = re.compile(r"<!-- agent-activation:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- agent-activation:end -->", re.DOTALL)
SPAWN_REVIEWER_ROLE_PATH = ".agentic-harness/roles/spawn-reviewer.md"


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    blocking: bool
    path: str
    evidence: str
    remediation: str


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def semver_tuple(value: str) -> tuple[int, int, int]:
    core = value.split("+", 1)[0].split("-", 1)[0]
    major, minor, patch = core.split(".")
    return int(major), int(minor), int(patch)


def canonical_json_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "{{" not in value and "<<" not in value


def unique_strings(value: Any, *, allow_empty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def file_at_git_commit(root: Path, commit: str, relative: str) -> bytes | None:
    result = subprocess.run(["git", "show", f"{commit}:{relative}"], cwd=root, capture_output=True, check=False)
    return result.stdout if result.returncode == 0 else None


def release_commit_for_version(root: Path, version: str) -> str | None:
    tags = subprocess.run(
        ["git", "tag", "--list", f"*-{version}-*"], cwd=root,
        capture_output=True, text=True, check=False,
    )
    names = [line for line in tags.stdout.splitlines() if line]
    if tags.returncode != 0 or len(names) != 1:
        return None
    resolved = subprocess.run(
        ["git", "rev-list", "-n", "1", names[0]], cwd=root,
        capture_output=True, text=True, check=False,
    )
    value = resolved.stdout.strip()
    return value if resolved.returncode == 0 and re.fullmatch(r"[0-9a-f]{40,64}", value) else None


def json_at_git_commit(root: Path, commit: str, relative: str) -> dict[str, Any] | None:
    payload = file_at_git_commit(root, commit, relative)
    if payload is None:
        return None
    try:
        value = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def current_harness_version(root: Path, mode: str) -> str | None:
    if mode == "master":
        relative = "harness/release/release-plan.json"
        path = root / relative
        field = "release_version"
    else:
        relative = ".agentic-harness/release-metadata.json"
        path = root / relative
        field = "harness_version"
    if not path.is_file():
        return None
    try:
        value = load_object(path)
    except (OSError, ValueError, json.JSONDecodeError):
        return None
    version = value.get(field)
    return str(version) if isinstance(version, str) and SEMVER.fullmatch(version) else None


def same_git_remote(left: str, right: str) -> bool:
    """Treat Git's optional terminal .git suffix as transport syntax, not identity."""
    return left.removesuffix(".git") == right.removesuffix(".git")


def evidence_reference(root: Path, value: str) -> tuple[str, dict[str, Any]]:
    match = re.fullmatch(r"([^@]+)@sha256:([0-9a-f]{64})", value)
    if not match:
        raise ValueError("evidence reference must be <relative-path>@sha256:<digest>")
    relative = safe_relative(match.group(1)).as_posix()
    path = root / relative
    if not path.is_file() or path.is_symlink() or digest(path) != match.group(2):
        raise ValueError("evidence path is missing, non-regular, symlinked, or digest-mismatched")
    data = load_object(path)
    return relative, data


def git_dirty_paths(root: Path) -> tuple[set[str], str]:
    output = git_output(root, ["status", "--porcelain=v1", "-z", "--untracked-files=all"])
    items = output.split("\0")
    paths: set[str] = set()
    index = 0
    while index < len(items):
        item = items[index]
        index += 1
        if not item:
            continue
        if len(item) < 4:
            raise ValueError(f"invalid Git status row: {item!r}")
        status = item[:2]
        path = item[3:]
        safe_relative(path)
        paths.add(path)
        if status[0] in {"R", "C"} and index < len(items) and items[index]:
            old_path = items[index]
            index += 1
            safe_relative(old_path)
            paths.add(old_path)
    return paths, hashlib.sha256(output.encode("utf-8", errors="surrogateescape")).hexdigest()


def normalized_relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def safe_relative(value: str, prefix: str | None = None) -> PurePosixPath:
    if not value or "\\" in value or any(char in value for char in ("\x00", "\n", "\r", "\t")):
        raise ValueError(f"unsafe relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"unsafe relative path: {value!r}")
    if prefix and not (value == prefix or value.startswith(prefix.rstrip("/") + "/")):
        raise ValueError(f"path outside required prefix {prefix}: {value}")
    return path


def legacy_domain_exception_problems(value: dict[str, Any]) -> list[str]:
    fields = {
        "schema_version", "context_id", "change_scope", "exact_change", "reason",
        "alternatives", "decision", "human_authority", "owner",
        "expiry_or_review_trigger", "accepted_risk", "affected_runs",
        "modeling_disproportionate_because",
    }
    problems: list[str] = []
    if set(value) != fields or value.get("schema_version") != "1" or value.get("decision") != "approved":
        problems.append("fields/schema/decision")
    required_strings = (
        "context_id", "exact_change", "reason", "human_authority", "owner",
        "expiry_or_review_trigger", "accepted_risk", "modeling_disproportionate_because",
    )
    if not all(nonempty_string(value.get(item)) for item in required_strings):
        problems.append("identity/rationale/authority/risk")
    if not unique_strings(value.get("alternatives")):
        problems.append("alternatives")
    if not unique_strings(value.get("affected_runs")):
        problems.append("affected_runs")
    scopes = value.get("change_scope")
    if not unique_strings(scopes):
        problems.append("change_scope")
    else:
        for item in scopes:
            try:
                path = safe_relative(item)
            except ValueError:
                problems.append(f"unsafe change scope {item!r}")
                continue
            if any(character in item for character in "*?[]{}") or (len(path.parts) == 1 and not path.suffix):
                problems.append(f"overbroad change scope {item!r}")
    return problems


def domain_review_structure_problems(review: dict[str, Any]) -> list[str]:
    """Select quorum from this Review, never retroactively from installed Core."""
    fields = {
        "schema_version", "review_id", "foundation_id", "foundation_revision",
        "candidate_sha256", "creator", "reviewers", "blocking_findings_closed",
        "review_outcome", "human_decision",
    }
    problems: list[str] = []
    if set(review) not in (fields, fields | {"harness_version"}) or review.get("schema_version") != "1":
        problems.append("review fields/schema")
    version = review.get("harness_version")
    current = False
    if "harness_version" in review:
        if not isinstance(version, str) or not SEMVER.fullmatch(version):
            problems.append("review harness_version must be an exact SemVer")
        else:
            current = semver_tuple(version) >= LEAN_WORKING_TEAM_MIN_VERSION
    reviewers = review.get("reviewers")
    if (not nonempty_string(review.get("creator")) or not unique_strings(reviewers)
            or len(reviewers) not in ({1, 2} if current else {2})
            or review.get("creator") in reviewers):
        problems.append("one or two independent working reviewers" if current else "exactly two independent reviewers")
    return problems


def domain_review_approval_problems(
    root: Path,
    foundation_relative: str,
    foundation: dict[str, Any],
    review: dict[str, Any],
) -> list[str]:
    problems = domain_review_structure_problems(review)
    review_id = review.get("review_id")
    if (
        not nonempty_string(review_id)
        or foundation.get("review_ref") != review_id
        or foundation.get("human_decision_ref") != review_id
        or review.get("foundation_id") != foundation.get("foundation_id")
        or review.get("foundation_revision") != foundation.get("revision")
    ):
        problems.append("Foundation/Review identity or revision binding")
    if review.get("blocking_findings_closed") is not True or review.get("review_outcome") != "approved":
        problems.append("open findings or unapproved review")
    decision = review.get("human_decision")
    if (
        not isinstance(decision, dict)
        or set(decision) != {"outcome", "authority", "decided_at", "overrides"}
        or decision.get("outcome") not in {"approved", "approved_with_overrides"}
        or not nonempty_string(decision.get("authority"))
        or not nonempty_string(decision.get("decided_at"))
        or not isinstance(decision.get("overrides"), list)
    ):
        problems.append("approved Human Domain Decision")
    try:
        foundation_path = root / safe_relative(foundation_relative).as_posix()
    except ValueError:
        foundation_path = None
    if (
        foundation_path is None
        or not foundation_path.is_file()
        or foundation_path.is_symlink()
        or review.get("candidate_sha256") != digest(foundation_path)
    ):
        problems.append("Foundation candidate_sha256 binding")
    return problems


def repository_files(root: Path, mode: str, add) -> list[Path]:
    """Return files owned by the validation surface, not every file on disk."""
    if mode != "product":
        return sorted(
            (path for path in root.rglob("*") if path.is_file() and not path.is_symlink() and ".git" not in path.parts),
            key=lambda path: normalized_relative(path, root).encode("utf-8"),
        )

    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=root, capture_output=True, check=False,
    )
    if result.returncode:
        add("AHV-INVENTORY-001", "error", ".", "Product-owned file inventory is unavailable", "run Product validation inside its Git repository")
        candidates: set[Path] = set()
    else:
        candidates = set()
        for raw in result.stdout.split(b"\0"):
            if not raw:
                continue
            try:
                relative = raw.decode("utf-8", errors="strict")
                safe_relative(relative)
            except (UnicodeDecodeError, ValueError):
                add("AHV-INVENTORY-001", "error", ".", "Product-owned file inventory contains an unsafe path", "restore a valid Git worktree")
                continue
            path = root / relative
            if path.is_file() or path.is_symlink():
                candidates.add(path)

    # Installed Core integrity is independent of Product ownership and remains a
    # raw-filesystem check even when the payload is intentionally Git-ignored.
    candidates.update(protected_inventory(root))
    manifest = root / ".agentic-harness/manifest.md"
    if manifest.is_file() and not manifest.is_symlink():
        candidates.add(manifest)
    return sorted(candidates, key=lambda path: normalized_relative(path, root).encode("utf-8"))


def markdown_files(files: Iterable[Path]) -> Iterable[Path]:
    return (path for path in files if path.suffix.lower() == ".md" and path.is_file() and not path.is_symlink())


def pinned_history_commit(root: Path, version: str, paths: Iterable[Path]) -> str | None:
    relatives = [normalized_relative(path, root) for path in paths]
    history = subprocess.run(
        ["git", "log", "--format=%H", "--", ".agentic-harness/release-metadata.json", *relatives],
        cwd=root, capture_output=True, text=True, check=False,
    )
    if history.returncode:
        return None
    current = {relative: (root / relative).read_bytes() for relative in relatives}
    for commit in history.stdout.splitlines():
        metadata = json_at_git_commit(root, commit, ".agentic-harness/release-metadata.json")
        if not metadata or metadata.get("harness_version") != version:
            continue
        if all(file_at_git_commit(root, commit, relative) == payload for relative, payload in current.items()):
            return commit
    return None


def pinned_history_exists_in_git(root: Path, version: str, paths: Iterable[Path]) -> bool:
    return pinned_history_commit(root, version, paths) is not None


def terminal_historical_contracts(root: Path, files: Iterable[Path], mode: str) -> set[str]:
    """Identify old pinned contracts only when their terminal ledger proves it."""
    if mode != "product":
        return set()
    installed = current_harness_version(root, mode)
    if not installed:
        return set()

    records: dict[str, tuple[Path, str]] = {}
    raw_event_counts: dict[str, int] = {}
    parsed_events: dict[str, list[dict[str, Any]]] = {}
    no_op = lambda *_args: None
    for path in markdown_files(files):
        text = path.read_text(encoding="utf-8")
        identifier = ARTIFACT_ID.search(text)
        if identifier:
            records[identifier.group(1)] = (path, text)
        if "/run-events/" not in f"/{normalized_relative(path, root)}":
            continue
        subject = re.search(r"^> Immutable subject:\s*(?:Run Contract\s*)?`([^`]+)`", text, re.MULTILINE)
        if not subject:
            continue
        run_id = subject.group(1)
        raw_event_counts[run_id] = raw_event_counts.get(run_id, 0) + 1
        parsed = parse_event(path.relative_to(root), text, mode, no_op)
        if parsed:
            parsed_events.setdefault(run_id, []).append(parsed)

    terminal: set[str] = set()
    for run_id, chain in parsed_events.items():
        contract = records.get(run_id)
        if not contract or len(chain) != raw_event_counts.get(run_id):
            continue
        contract_path, contract_text = contract
        version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", contract_text, re.MULTILINE)
        if not version or not SEMVER.fullmatch(version.group(1)) or semver_tuple(version.group(1)) >= semver_tuple(installed):
            continue
        contract_digest = digest(contract_path)
        chain.sort(key=lambda event: event["sequence"])
        valid = bool(
            chain[0]["sequence"] == 1
            and chain[0]["previous"] == "genesis"
            and chain[0]["from"] == "none"
            and chain[-1]["to"] in {"completed", "cancelled"}
        )
        terminal_seen = False
        for index, event in enumerate(chain):
            transition = (event["from"], event["to"])
            valid = valid and event["contract_digest"] == contract_digest
            valid = valid and all(nonempty_string(event[field]) for field in ("actor", "authority", "guard", "lease"))
            valid = valid and (transition in RUN_TRANSITIONS or (event["from"] in NON_TERMINAL and event["to"] == "cancelled"))
            if terminal_seen:
                valid = False
            terminal_seen = event["to"] in {"completed", "cancelled"}
            if index:
                prior = chain[index - 1]
                valid = valid and event["sequence"] == prior["sequence"] + 1
                valid = valid and event["previous"] == digest(root / prior["path"])
                valid = valid and event["from"] == prior["to"]
        if valid and pinned_history_exists_in_git(root, version.group(1), [contract_path, *(root / event["path"] for event in chain)]):
            terminal.add(run_id)
    return terminal


def protected_inventory(root: Path) -> list[Path]:
    items: list[Path] = []
    protected = root / ".agentic-harness"
    if protected.exists():
        items.extend(path for path in protected.rglob("*") if path.is_file() and not path.is_symlink() and path != protected / "manifest.md")
    return sorted(items, key=lambda item: normalized_relative(item, root).encode("utf-8"))


def tree_digest(paths: Iterable[Path], root: Path) -> str:
    rows: list[bytes] = []
    for path in paths:
        relative = normalized_relative(path, root)
        safe_relative(relative)
        rows.append(f"{relative}\t{digest(path)}\n".encode("utf-8"))
    return hashlib.sha256(b"".join(rows)).hexdigest()


def parse_manifest_inventory(text: str) -> tuple[dict[str, str], str | None]:
    expected: dict[str, str] = {}
    tree_match = re.search(r"Protected-payload tree SHA-256:\s*`([0-9a-f]{64})`", text)
    for line in text.splitlines():
        if not line.startswith("| `"): continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if len(cells) == 4 and HEX64.fullmatch(cells[3]):
            safe_relative(cells[0]); expected[cells[0]] = cells[3]
    return expected, tree_match.group(1) if tree_match else None


def load_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict): raise ValueError(f"JSON object required: {path}")
    return value


def validate_release_metadata(root: Path, add) -> None:
    relative = ".agentic-harness/release-metadata.json"
    path = root / relative
    if not path.is_file() or path.is_symlink():
        add("AHV-METADATA-001", "error", relative, "protected Release Metadata missing or not regular", "restore the authenticated release payload"); return
    try:
        value = load_object(path)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        add("AHV-METADATA-001", "error", relative, f"invalid Release Metadata: {error}", "restore supported machine-readable metadata"); return
    required = {"schema_version", "harness_version", "release_channel", "release_tag", "source_commit", "overlay_schema", "repository_id", "owner_id", "supported_starting_versions", "upgrade_history", "release_evidence_policy_sha256", "release_attestation_sha256"}
    if set(value) != required or value.get("schema_version") != "1":
        add("AHV-METADATA-002", "error", relative, "Release Metadata shape/schema mismatch", "use the exact released schema"); return
    if not SEMVER.fullmatch(str(value["harness_version"])) or not valid_release_tag(str(value["release_tag"]), str(value["harness_version"])) or not str(value["overlay_schema"]).isdigit():
        add("AHV-METADATA-003", "error", relative, "invalid version/tag/overlay schema", "bind exact SemVer/tag/schema")
    if value["release_channel"] != "stable" or not re.fullmatch(r"[0-9a-f]{40,64}", str(value["source_commit"])) or not str(value["repository_id"]).isdigit() or not str(value["owner_id"]).isdigit() or not HEX64.fullmatch(str(value["release_evidence_policy_sha256"])) or not HEX64.fullmatch(str(value["release_attestation_sha256"])):
        add("AHV-METADATA-009", "error", relative, "invalid release channel or provenance/evidence identity", "use authenticated Release Metadata")
    manifest = root / ".agentic-harness/manifest.md"
    if manifest.is_file():
        text = manifest.read_text(encoding="utf-8")
        projections = {
            "harness_version": re.search(r"^- Harness version:\s*`([^`]+)`", text, re.MULTILINE),
            "release_channel": re.search(r"^- Release channel:\s*`([^`]+)`", text, re.MULTILINE),
            "release_tag": re.search(r"^- Release tag:\s*`([^`]+)`", text, re.MULTILINE),
            "source_commit": re.search(r"^- Source commit:\s*`([^`]+)`", text, re.MULTILINE),
            "overlay_schema": re.search(r"^- Overlay schema:\s*`([^`]+)`", text, re.MULTILINE),
        }
        for field, match in projections.items():
            if not match or match.group(1) != str(value[field]): add("AHV-METADATA-010", "error", relative, f"Manifest projection disagrees for {field}", "assemble Manifest and Release Metadata from one Release Plan")
        structured = {
            "supported_starting_versions": re.search(r"^- Supported starting versions/schemas:\s*`([^`]+)`", text, re.MULTILINE),
            "history_ids": re.search(r"^- Required adjacent history:\s*`([^`]+)`", text, re.MULTILINE),
        }
        for field, match in structured.items():
            try: observed = json.loads(match.group(1)) if match else None
            except json.JSONDecodeError: observed = None
            expected = value["supported_starting_versions"] if field == "supported_starting_versions" else [item.get("id") for item in value["upgrade_history"] if isinstance(item, dict)]
            if observed != expected: add("AHV-METADATA-010", "error", relative, f"Manifest projection disagrees for {field}", "assemble Manifest and Release Metadata from one Release Plan")
        digest_projections = {
            "release_evidence_policy_sha256": re.search(r"^- Release Evidence Policy SHA-256:\s*`([^`]+)`", text, re.MULTILINE),
            "release_attestation_sha256": re.search(r"^- External Release Attestation SHA-256:\s*`([^`]+)`", text, re.MULTILINE),
        }
        for field, match in digest_projections.items():
            if not match or match.group(1) != value[field]: add("AHV-METADATA-010", "error", relative, f"Manifest projection disagrees for {field}", "assemble Manifest and Release Metadata from one Release Plan")
    if not isinstance(value["supported_starting_versions"], list) or not isinstance(value["upgrade_history"], list):
        add("AHV-METADATA-004", "error", relative, "compatibility/history are not lists", "restore the exact released metadata"); return
    for start in value["supported_starting_versions"]:
        valid = start == {"kind": "fresh_install"} or (isinstance(start, dict) and set(start) == {"version", "overlay_schema"} and SEMVER.fullmatch(str(start["version"])) and str(start["overlay_schema"]).isdigit())
        if not valid: add("AHV-METADATA-005", "error", relative, f"invalid supported start: {start}", "declare fresh or exact version/schema")
    seen: set[str] = set(); prior: str | None = None
    for history in value["upgrade_history"]:
        fields = {"id", "from_version", "to_version", "release_path", "sha256"}
        if not isinstance(history, dict) or set(history) != fields:
            add("AHV-METADATA-006", "error", relative, "invalid history entry shape", "use the released adjacent-history schema"); continue
        try: history_path = safe_relative(history["release_path"], ".agentic-harness/history")
        except ValueError as error: add("AHV-METADATA-006", "error", relative, str(error), "use a protected relative history path"); continue
        if history["id"] in seen or not HEX64.fullmatch(str(history["sha256"])):
            add("AHV-METADATA-006", "error", relative, f"duplicate/invalid history {history['id']}", "use unique digest-bound history"); continue
        if not SEMVER.fullmatch(str(history["from_version"])) or not SEMVER.fullmatch(str(history["to_version"])):
            add("AHV-METADATA-006", "error", relative, f"invalid history version: {history['id']}", "bind exact adjacent SemVer"); continue
        seen.add(history["id"])
        artifact = root / history_path
        if not artifact.is_file() or artifact.is_symlink() or digest(artifact) != history["sha256"]:
            add("AHV-METADATA-007", "error", relative, f"history artifact mismatch: {history['id']}", "restore exact protected history")
        if prior and prior != history["from_version"]: add("AHV-METADATA-008", "error", relative, "history chain is non-contiguous", "restore ordered adjacent history")
        prior = history["to_version"]


def validate_source_lock(root: Path, add) -> None:
    relative = "harness/release/source-lock.json"; path = root / relative
    if not path.is_file() or path.is_symlink():
        add("AHV-SOURCE-001", "error", relative, "source lock missing or not regular", "restore the source lock"); return
    try: value = load_object(path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        add("AHV-SOURCE-001", "error", relative, f"invalid source lock: {error}", "restore schema 1 lock"); return
    if value.get("schema_version") != "1" or not isinstance(value.get("artifacts"), list):
        add("AHV-SOURCE-002", "error", relative, "source lock schema mismatch", "use schema 1") ; return
    ids: set[str] = set(); sources: set[str] = set(); installed: set[str] = set()
    for item in value["artifacts"]:
        fields = {"id", "version", "kind", "source", "installed", "sha256"}
        if not isinstance(item, dict) or set(item) != fields:
            add("AHV-SOURCE-004", "error", relative, "source-lock entry shape mismatch", "use the exact entry schema"); continue
        try: source_rel = safe_relative(item["source"], "docs/specs"); safe_relative(item["installed"], ".agentic-harness/core")
        except ValueError as error: add("AHV-SOURCE-004", "error", relative, str(error), "use safe bounded paths"); continue
        if item["id"] in ids or item["source"] in sources or item["installed"] in installed:
            add("AHV-SOURCE-005", "error", relative, f"duplicate lock identity/path: {item['id']}", "deduplicate the lock")
        ids.add(item["id"]); sources.add(item["source"]); installed.add(item["installed"])
        source = root / source_rel
        if not source.is_file() or source.is_symlink() or not HEX64.fullmatch(str(item["sha256"])) or digest(source) != item["sha256"]:
            add("AHV-SOURCE-006", "error", item["source"], "source digest missing/mismatched", "refresh through reviewed source-lock update"); continue
        text = source.read_text(encoding="utf-8")
        found_id = ARTIFACT_ID.search(text); found_version = re.search(r"^> Version:\s*`?([^`\n]+)", text, re.MULTILINE); found_status = re.search(r"^> Status:\s*([^\n]+)", text, re.MULTILINE)
        if not found_id or found_id.group(1) != item["id"] or not found_version or found_version.group(1).strip() != item["version"]:
            add("AHV-SOURCE-007", "error", item["source"], "source identity/version mismatch", "bind exact artifact identity")
        if not found_status or "Active" not in found_status.group(1):
            add("AHV-SOURCE-008", "error", item["source"], "release source is not Active", "approve/activate or exclude")
    actual = {path.relative_to(root).as_posix() for path in (root / "docs/specs").glob("*.spec.md")}
    if sources != actual: add("AHV-SOURCE-009", "error", relative, f"source-lock completeness mismatch; missing={sorted(actual-sources)}, extra={sorted(sources-actual)}", "inventory every canonical top-level Harness spec/profile")
    routing = (root / "docs/specs/spec-routing.md")
    if routing.is_file():
        routing_text = routing.read_text(encoding="utf-8")
        for source in sorted(sources):
            if source not in routing_text: add("AHV-SOURCE-010", "error", source, "locked source absent from routing", "add one exact routing entry")


def validate_master_release_controls(root: Path, id_paths: dict[str, Path], add) -> None:
    plan_path = root / "harness/release/release-plan.json"; evidence_path = root / "harness/release/release-evidence-lock.json"; trust_path = root / "harness/release/upstream-trust.json"; case_lock_path = root / "evals/cases/case-lock.json"
    try:
        plan = load_object(plan_path); evidence = load_object(evidence_path); trust = load_object(trust_path); case_lock = load_object(case_lock_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        add("AHV-CONTROL-001", "error", "harness/release", f"release control file invalid/missing: {error}", "restore all governed release controls"); return
    plan_fields = {"schema_version", "release_version", "release_tag", "release_channel", "overlay_schema", "source_branch", "approved_base_commit", "approved_pull_request", "supported_starting_versions", "upgrade_history", "release_notes", "required_evidence_policy"}
    if set(plan) != plan_fields or plan.get("schema_version") != "1" or not SEMVER.fullmatch(str(plan.get("release_version", ""))) or not valid_release_tag(str(plan.get("release_tag", "")), str(plan.get("release_version", ""))): add("AHV-CONTROL-002", "error", "harness/release/release-plan.json", "release plan shape/version/tag invalid", "use governed Release Plan schema")
    evidence_fields = {"schema_version", "policy_version", "release_version", "external_attestation_required", "required_evidence_ids", "required_eval_case_ids", "judgment_case_ids", "minimum_judgment_trials"}
    exact_evidence_ids = {"independent-council-review", "deterministic-ci", "agentic-eval-suite", "provider-human-merge-approval"}
    exact_case_ids = [f"AH-EVAL-{number:03d}" for number in range(1, 21)]
    exact_judgment_ids = {"AH-EVAL-002", "AH-EVAL-003", "AH-EVAL-004", "AH-EVAL-005", "AH-EVAL-007", "AH-EVAL-009", "AH-EVAL-011", "AH-EVAL-013", "AH-EVAL-014", "AH-EVAL-015", "AH-EVAL-017", "AH-EVAL-018", "AH-EVAL-019"}
    if set(evidence) != evidence_fields or evidence.get("schema_version") != "2" or evidence.get("release_version") != plan.get("release_version") or evidence.get("external_attestation_required") is not True: add("AHV-CONTROL-003", "error", "harness/release/release-evidence-lock.json", "Release Evidence Policy shape/version invalid", "restore exact policy")
    elif set(evidence.get("required_evidence_ids", [])) != exact_evidence_ids or len(evidence.get("required_evidence_ids", [])) != len(exact_evidence_ids) or evidence.get("required_eval_case_ids") != exact_case_ids or set(evidence.get("judgment_case_ids", [])) != exact_judgment_ids or evidence.get("minimum_judgment_trials") != 3: add("AHV-CONTROL-005", "error", "harness/release/release-evidence-lock.json", "required Evidence/Eval ID or trial policy mismatch", "restore exact fixed release requirements")
    if trust.get("schema_version") != "1" or trust.get("repository_id") != "1328705370" or trust.get("owner_id") != "288767329" or trust.get("repository_full_name") != "langvis/agentic_harness": add("AHV-CONTROL-007", "error", "harness/release/upstream-trust.json", "canonical provider identity drift", "restore reviewed descriptive identity and verify externally at release")
    case_fields = {"schema_version", "suite_id", "suite_revision", "case_ids", "case_contract_path", "case_contract_sha256", "case_input_path", "case_input_sha256", "variant_lock_path", "variant_lock_sha256", "base_fixture_path", "base_fixture_tree_sha256", "result_evidence_path", "result_evidence_sha256", "result"}
    if set(case_lock) != case_fields or case_lock.get("schema_version") != "1": add("AHV-EVAL-001", "error", "evals/cases/case-lock.json", "Eval Case Lock shape invalid", "restore the exact Eval lock")
    else:
        if evidence.get("required_eval_case_ids") != case_lock.get("case_ids"): add("AHV-EVAL-014", "error", "evals/cases/case-lock.json", "Evidence Policy case IDs differ from Eval Case Lock", "bind one exact ordered required case set")
        try: contract_rel = safe_relative(case_lock["case_contract_path"], "evals/cases"); inputs_rel = safe_relative(case_lock["case_input_path"], "evals/fixtures"); base_rel = safe_relative(case_lock["base_fixture_path"], "evals/fixtures"); variant_rel = safe_relative(case_lock["variant_lock_path"], "evals/fixtures"); result_rel = safe_relative(case_lock["result_evidence_path"], "evals/results")
        except ValueError as error: add("AHV-EVAL-002", "error", "evals/cases/case-lock.json", str(error), "use bounded Eval fixture paths"); return
        contract_path = root / contract_rel; inputs_path = root / inputs_rel; base = root / base_rel
        if not contract_path.is_file() or contract_path.is_symlink() or digest(contract_path) != case_lock.get("case_contract_sha256"): add("AHV-EVAL-015", "error", "evals/cases/case-lock.json", "full case contract digest mismatch", "restore the locked shared configuration/actions/blind spots")
        if not inputs_path.is_file() or digest(inputs_path) != case_lock.get("case_input_sha256"): add("AHV-EVAL-003", "error", "evals/cases/case-lock.json", "case-input digest mismatch", "refresh through reviewed Eval change")
        else:
            case_inputs: dict[str, Any] = {}
            try: case_inputs = load_object(inputs_path); observed_ids = [item["id"] for item in case_inputs.get("cases", [])]
            except (OSError, ValueError, json.JSONDecodeError, KeyError) as error: add("AHV-EVAL-004", "error", case_lock["case_input_path"], f"case inputs invalid: {error}", "restore exact cases"); observed_ids = []
            if observed_ids != case_lock.get("case_ids") or len(observed_ids) != len(set(observed_ids)): add("AHV-EVAL-005", "error", case_lock["case_input_path"], "case ID order/set differs from lock", "bind exact unique case IDs")
            variant_path = root / variant_rel
            if not variant_path.is_file() or digest(variant_path) != case_lock.get("variant_lock_sha256"): add("AHV-EVAL-009", "error", case_lock["variant_lock_path"], "variant lock digest mismatch", "restore exact deterministic variant lock")
            else:
                variant_lock = load_object(variant_path); generator = root / safe_relative(variant_lock.get("generator", ""), "evals/fixtures")
                if set(variant_lock) != {"schema_version","generator","generator_sha256","tree_digest_algorithm","visibility_rule","variants"} or variant_lock.get("schema_version") != "2" or not generator.is_file() or digest(generator) != variant_lock.get("generator_sha256"): add("AHV-EVAL-010", "error", case_lock["variant_lock_path"], "variant generator identity/digest mismatch", "restore exact generator and separated visibility contract")
                referenced = {variant for case in case_inputs.get("cases", []) for variant in case.get("variants", [])}
                variant_values = variant_lock.get("variants", {})
                valid_boundaries = isinstance(variant_values, dict) and all(isinstance(value, dict) and set(value) == {"agent_input_sha256","evaluator_private_sha256"} and all(HEX64.fullmatch(str(item)) for item in value.values()) for value in variant_values.values())
                if referenced != set(variant_values) or not valid_boundaries: add("AHV-EVAL-011", "error", case_lock["variant_lock_path"], "variant set/visibility-boundary digest coverage mismatch", "bind every and only referenced agent/private variant boundary")
            result_path = root / result_rel
            if not result_path.is_file() or digest(result_path) != case_lock.get("result_evidence_sha256"): add("AHV-EVAL-012", "error", case_lock["result_evidence_path"], "candidate result index digest mismatch", "restore exact honest result index")
            else:
                results = load_object(result_path); result_cases = results.get("cases", [])
                expected_trials = {case["id"]: case["trials"] for case in case_inputs.get("cases", [])}
                if [case.get("id") for case in result_cases] != observed_ids or any(case.get("required_trials") != expected_trials.get(case.get("id")) for case in result_cases) or results.get("aggregate_result") != case_lock.get("result"): add("AHV-EVAL-013", "error", case_lock["result_evidence_path"], "candidate result index differs from locked case contracts", "align exact case order/trials/result without claiming unobserved pass")
        if not base.is_dir(): add("AHV-EVAL-006", "error", case_lock["base_fixture_path"], "base fixture missing", "restore fixture")
        else:
            paths = sorted((path for path in base.rglob("*") if path.is_file() and not path.is_symlink()), key=lambda path: path.relative_to(base).as_posix().encode("utf-8"))
            if tree_digest(paths, base) != case_lock.get("base_fixture_tree_sha256"): add("AHV-EVAL-007", "error", "evals/cases/case-lock.json", "base fixture tree digest mismatch", "refresh through reviewed fixture change")


def parse_admission_projection(relative: str, text: str, identifier: str | None, add, known_ids: set[str] | None = None) -> dict[str, Any] | None:
    blocks = ADMISSION_PROJECTION_BLOCK.findall(text)
    if len(blocks) != 1:
        add("AHV-ADMISSION-001", "error", relative, f"Harness >=1.0.10 ordinary Run requires exactly one Admission Projection; observed {len(blocks)}", "instantiate one compact run-kind-specific admission-projection block")
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-ADMISSION-001", "error", relative, f"Admission Projection JSON is invalid: {error}", "use one valid exact JSON projection")
        return None

    version = value.get("harness_version") if isinstance(value, dict) else None
    if isinstance(version, str) and uses_lease_free_contract(version):
        add("AHV-ADMISSION-001", "error", relative, "current Runs use the direct Run Contract, not historical lease-based admission", "use the released execution-run template and --check-run; do not create lease evidence")
        return None

    top_fields = {
        "schema_version", "ruleset_id", "run_id", "run_kind", "harness_version",
        "repository", "targets", "ordered_boundary", "scope_lock", "authority",
        "external_actions", "capabilities", "lease", "completion", "context",
    }
    repository_fields = {"remote", "start_commit", "current_branch", "target_branch", "git_mutation", "non_git_rationale"}
    scope_fields = {"required_outcomes", "minimum_change", "allowed_paths", "prohibited_outcomes", "verification_mapping", "adjacent_findings", "expansion_rule", "expansion_authority"}
    authority_fields = {"decision_authority_ref", "lead", "active_roles", "reasoning", "reviewers", "human_gate_owner", "classification_trigger", "agent_budget", "review_budget", "correction_budget"}
    external_fields = {"allowed", "excluded"}
    capability_fields = {"id", "status", "evidence"}
    lease_fields = {"disposition", "reason", "key", "target", "owner", "claim_timing", "recovery"}
    completion_fields = {"target_levels", "evidence", "stop_boundary", "pause_triggers", "recovery_owner"}
    context_fields = {
        "product_delivery": {"slice_id", "work_package_ids", "environment_disposition"},
        "technical_risk_experiment": {"experiment_id", "hypothesis", "observation", "cleanup", "environment_disposition"},
        "bootstrap_initialization": {"bootstrap_work_ids", "input_boundary", "environment_disposition"},
        "governance": {"objective_id", "authority_ref", "protected_invariants", "repository_target", "environment_disposition"},
    }
    problems: list[str] = []
    if not isinstance(value, dict) or set(value) != top_fields:
        problems.append("top-level fields")
        value = value if isinstance(value, dict) else {}
    run_kind = value.get("run_kind")
    if value.get("schema_version") != "1" or value.get("ruleset_id") != ADMISSION_RULESET:
        problems.append("schema_version/ruleset_id")
    if not nonempty_string(value.get("run_id")) or value.get("run_id") != identifier:
        problems.append("run_id")
    if run_kind not in context_fields:
        problems.append("run_kind")
    harness_version = value.get("harness_version")
    if not isinstance(harness_version, str) or not SEMVER.fullmatch(harness_version) or semver_tuple(harness_version) < ADMISSION_MIN_VERSION:
        problems.append("harness_version")
    elif semver_tuple(harness_version) >= AGENT_START_MIN_VERSION:
        authority_fields.add("agent_ids")

    repository = value.get("repository")
    if not isinstance(repository, dict) or set(repository) != repository_fields or not isinstance(repository.get("git_mutation"), bool):
        problems.append("repository shape")
    elif repository["git_mutation"]:
        if not all(nonempty_string(repository.get(field)) and repository[field] != "not_applicable" for field in ("remote", "current_branch", "target_branch")) or not re.fullmatch(r"[0-9a-f]{40,64}", str(repository.get("start_commit", ""))) or repository.get("non_git_rationale") != "not_applicable":
            problems.append("Git repository identity")
    elif any(repository.get(field) != "not_applicable" for field in ("remote", "start_commit", "current_branch", "target_branch")) or not nonempty_string(repository.get("non_git_rationale")) or repository.get("non_git_rationale") == "not_applicable":
        problems.append("non-Git rationale")

    targets = value.get("targets")
    if not unique_strings(targets) or not nonempty_string(value.get("ordered_boundary")):
        problems.append("targets/ordered_boundary")
    elif known_ids is not None:
        missing_targets = sorted(set(targets) - known_ids)
        if missing_targets:
            problems.append(f"unknown target IDs {missing_targets}")
    scope = value.get("scope_lock")
    if not isinstance(scope, dict) or set(scope) != scope_fields:
        problems.append("scope_lock shape")
    else:
        valid_scope_lists = {
            field: unique_strings(scope.get(field))
            for field in ("required_outcomes", "allowed_paths", "prohibited_outcomes")
        }
        for field, valid in valid_scope_lists.items():
            if not valid:
                problems.append(f"scope_lock.{field}")
        for field in ("minimum_change", "expansion_authority"):
            if not nonempty_string(scope.get(field)):
                problems.append(f"scope_lock.{field}")
        for path in scope.get("allowed_paths", []) if valid_scope_lists["allowed_paths"] else []:
            try:
                safe_relative(path)
            except ValueError:
                problems.append(f"unsafe allowed path {path!r}")
        expected_scope = {"verification_mapping": "required_at_verification", "adjacent_findings": "follow_up_only", "expansion_rule": "stop_and_amend_before_mutation"}
        for field, expected in expected_scope.items():
            if scope.get(field) != expected:
                problems.append(f"scope_lock.{field}")

    authority = value.get("authority")
    if not isinstance(authority, dict) or set(authority) != authority_fields:
        problems.append("authority shape")
    else:
        for field in ("decision_authority_ref", "lead", "human_gate_owner", "classification_trigger"):
            if not nonempty_string(authority.get(field)):
                problems.append(f"authority.{field}")
        prospective_agent_ids = bool(isinstance(harness_version, str) and SEMVER.fullmatch(harness_version) and semver_tuple(harness_version) >= AGENT_START_MIN_VERSION)
        if not unique_strings(authority.get("active_roles")) or not unique_strings(authority.get("reviewers"), allow_empty=True):
            problems.append("authority roles/reviewers")
        if prospective_agent_ids:
            if not unique_strings(authority.get("agent_ids")):
                problems.append("authority planned Agents")
            elif authority.get("lead") not in authority["agent_ids"] or not set(authority.get("reviewers", [])).issubset(set(authority["agent_ids"])):
                problems.append("authority planned-Agent identity coverage")
        if authority.get("reasoning") not in {"high", "xhigh"}:
            problems.append("authority.reasoning")
        if authority.get("lead") in authority.get("reviewers", []):
            problems.append("creator self-review")
        for field in ("agent_budget", "review_budget", "correction_budget"):
            if isinstance(authority.get(field), bool) or not isinstance(authority.get(field), int) or authority[field] < 0:
                problems.append(f"authority.{field}")

    external = value.get("external_actions")
    external_allowed_valid = isinstance(external, dict) and unique_strings(external.get("allowed"))
    external_excluded_valid = isinstance(external, dict) and unique_strings(external.get("excluded"))
    if not isinstance(external, dict) or set(external) != external_fields or not external_allowed_valid or not external_excluded_valid:
        problems.append("external_actions")
    capabilities = value.get("capabilities")
    capability_ids: list[str] = []
    if not isinstance(capabilities, list) or not capabilities:
        problems.append("capabilities")
    else:
        for capability in capabilities:
            if not isinstance(capability, dict) or set(capability) != capability_fields or not nonempty_string(capability.get("id")) or capability.get("status") not in {"available", "required_blocker", "degradable", "not_applicable"} or not nonempty_string(capability.get("evidence")):
                problems.append("capability item")
                continue
            capability_ids.append(capability["id"])
        if len(capability_ids) != len(set(capability_ids)):
            problems.append("duplicate capability id")
        if any(isinstance(item, dict) and item.get("status") == "required_blocker" for item in capabilities):
            problems.append("required capability blocker")
        integrity = [item for item in capabilities if isinstance(item, dict) and item.get("id") == "installed_core_integrity"]
        if len(integrity) != 1 or integrity[0].get("status") != "available":
            problems.append("installed_core_integrity capability")

    lease = value.get("lease")
    if not isinstance(lease, dict) or set(lease) != lease_fields or lease.get("disposition") not in {"required", "not_applicable"} or not nonempty_string(lease.get("reason")):
        problems.append("lease shape/disposition")
    elif lease["disposition"] == "required":
        if any(not nonempty_string(lease.get(field)) or lease[field] == "not_applicable" for field in ("key", "target", "owner", "claim_timing", "recovery")) or lease.get("claim_timing") != "before_active":
            problems.append("required lease facts")
    elif any(lease.get(field) != "not_applicable" for field in ("key", "target", "owner", "claim_timing", "recovery")) or lease.get("reason") == "not_applicable":
        problems.append("lease not_applicable rationale")
    if isinstance(repository, dict) and repository.get("git_mutation") is True and isinstance(lease, dict) and lease.get("disposition") != "required":
        problems.append("Git mutation without required lease")

    completion = value.get("completion")
    if not isinstance(completion, dict) or set(completion) != completion_fields or not unique_strings(completion.get("target_levels")) or not unique_strings(completion.get("evidence")) or not unique_strings(completion.get("pause_triggers")) or not nonempty_string(completion.get("stop_boundary")) or not nonempty_string(completion.get("recovery_owner")):
        problems.append("completion")
    context = value.get("context")
    if run_kind in context_fields:
        if not isinstance(context, dict) or set(context) != context_fields[run_kind]:
            problems.append(f"{run_kind} context shape")
        else:
            environment = context.get("environment_disposition")
            if not nonempty_string(environment):
                problems.append("context.environment_disposition")
            elif isinstance(external, dict):
                normalized_environment = environment.lower()
                allowed_actions = " ".join(item.lower() for item in external["allowed"]) if external_allowed_valid else ""
                excluded_actions = " ".join(item.lower() for item in external["excluded"]) if external_excluded_valid else ""
                if "local_only_no_deploy" in normalized_environment and any(token in allowed_actions for token in ("deploy", "production", "provider", "aws")):
                    problems.append("local-only environment contradicts allowed actions")
                if "production" in normalized_environment and ("production" not in allowed_actions or "production" in excluded_actions):
                    problems.append("Production environment/action contradiction")
            if run_kind == "product_delivery":
                if not nonempty_string(context.get("slice_id")) or not unique_strings(context.get("work_package_ids")) or context.get("slice_id") not in (targets or []) or not set(context.get("work_package_ids", [])).issubset(set(targets or [])):
                    problems.append("Product Delivery target binding")
            elif run_kind == "technical_risk_experiment":
                if any(not nonempty_string(context.get(field)) for field in ("experiment_id", "hypothesis", "observation", "cleanup")) or context.get("experiment_id") not in (targets or []):
                    problems.append("Experiment target/hypothesis/cleanup")
            elif run_kind == "bootstrap_initialization":
                if not unique_strings(context.get("bootstrap_work_ids")) or not nonempty_string(context.get("input_boundary")) or not set(context.get("bootstrap_work_ids", [])).issubset(set(targets or [])):
                    problems.append("Bootstrap target/input boundary")
            elif run_kind == "governance":
                if any(not nonempty_string(context.get(field)) for field in ("objective_id", "authority_ref", "repository_target")) or not unique_strings(context.get("protected_invariants")) or context.get("objective_id") not in (targets or []) or context.get("authority_ref") != authority.get("decision_authority_ref"):
                    problems.append("Governance objective/authority/invariants")

    visible_kind = re.search(r"^> Run kind:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
    visible_version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
    classification = re.search(r"^> Decision class / classification trigger ID:\s*`?(D[0-3])`?\s*/\s*`?([a-z0-9_]+)`?\s*$", text, re.MULTILINE)
    reasoning = re.search(r"^- Reasoning:\s*`?(high|xhigh)`?\s*$", text, re.MULTILINE)
    authority_line = re.search(r"^> Decision Authority / Final Approver / Human Gate Owner:\s*(\S.+)$", text, re.MULTILINE)
    if not visible_kind or visible_kind.group(1) != run_kind:
        problems.append("visible Run kind mismatch")
    if not visible_version or visible_version.group(1) != harness_version:
        problems.append("visible Harness version mismatch")
    if not classification or not isinstance(authority, dict) or classification.group(2) != authority.get("classification_trigger"):
        problems.append("classification trigger mismatch")
    else:
        decision_class = classification.group(1)
        expected_reasoning = "xhigh" if decision_class == "D3" or run_kind == "governance" else None
        effort_override = re.search(r"^- Effort-profile override or `none`:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
        human_high_override = bool(
            reasoning
            and reasoning.group(1) == "high"
            and effort_override
            and isinstance(authority, dict)
            and re.fullmatch(r"human-approved:[A-Za-z0-9._-]+", effort_override.group(1).strip())
            and effort_override.group(1).strip() == authority.get("decision_authority_ref")
        )
        if not reasoning or reasoning.group(1) != authority.get("reasoning") or (expected_reasoning and reasoning.group(1) != expected_reasoning and not human_high_override):
            problems.append("reasoning floor/binding")
        visible_budget_labels = {"agent_budget": "Max active Agents total", "review_budget": "Initial full-review count", "correction_budget": "Consolidated correction-pass ceiling"}
        for field, label in visible_budget_labels.items():
            match = re.search(rf"^- {re.escape(label)}:\s*`?([0-9]+)`?\s*$", text, re.MULTILINE)
            if not match or int(match.group(1)) != authority.get(field):
                problems.append(f"{field} binding")
        reviewer_count = re.search(r"^- Independent reviewer count:\s*`?([0-9]+)`?\s*$", text, re.MULTILINE)
        if not reviewer_count or not isinstance(authority.get("reviewers"), list) or int(reviewer_count.group(1)) != len(authority["reviewers"]):
            problems.append("reviewer count binding")
    if not authority_line or not isinstance(authority, dict) or authority.get("decision_authority_ref") not in authority_line.group(1):
        problems.append("Decision Authority binding")
    visible_scope_labels = {
        "required_outcomes": "Required outcomes",
        "minimum_change": "Minimum sufficient change",
        "allowed_paths": "Allowed path families",
        "prohibited_outcomes": "Prohibited outcomes",
        "expansion_authority": "Scope expansion authority/reference or `none`",
    }
    if isinstance(scope, dict):
        for field, label in visible_scope_labels.items():
            match = re.search(rf"^- {re.escape(label)}:\s*(\S.+)$", text, re.MULTILINE)
            values = scope.get(field)
            expected_values = values if isinstance(values, list) else [values]
            if not match or any(not isinstance(item, str) or item not in match.group(1) for item in expected_values):
                problems.append(f"visible Scope Lock mismatch: {field}")

    if problems:
        add("AHV-ADMISSION-002", "error", relative, f"Admission Projection is incomplete or contradictory: {sorted(set(problems))}", "correct only the named owner field or applicability decision; do not add irrelevant run-kind data")
        return None
    return value


def admission_environment(projection: dict[str, Any]) -> str:
    return str(projection["context"]["environment_disposition"])


def expected_admission_rule_results(projection: dict[str, Any]) -> dict[str, str]:
    results = {
        rule: ("not_applicable" if rule == "lease" and projection["lease"]["disposition"] == "not_applicable" else "observed")
        for rule in ADMISSION_RULE_RESULTS
    }
    if semver_tuple(projection["harness_version"]) >= AGENT_START_MIN_VERSION:
        results["agent_start_control"] = "observed"
    return results


def agent_start_subject_sha256(control: dict[str, Any], item: dict[str, Any]) -> str:
    return canonical_json_sha256({
        "schema_version":"1",
        "run_id":control.get("run_id"),
        "contract_revision":control.get("contract_revision"),
        "admission_projection_sha256":control.get("admission_projection_sha256"),
        "spawn_reviewer":control.get("spawn_reviewer"),
        "agent_id":item.get("agent_id"),
        "brief_sha256":item.get("brief_sha256"),
    })


def historical_agent_commit(root: Path, relative: str, projection: dict[str, Any] | None,
                            mode: str) -> str | None:
    """Read old evidence from its proven context; this never grants current admission."""
    version = projection.get("harness_version") if isinstance(projection, dict) else None
    installed = current_harness_version(root, mode)
    if (not isinstance(version, str) or not SEMVER.fullmatch(version)
            or not installed or not SEMVER.fullmatch(installed)
            or semver_tuple(version) >= semver_tuple(installed)):
        return None
    if mode == "master":
        return release_commit_for_version(root, version)
    record = root / relative
    if mode == "product" and record.is_file() and not record.is_symlink():
        return pinned_history_commit(root, version, [record])
    return None


def spawn_role_digest_matches(root: Path, role_path: Path, expected: Any,
                              projection: dict[str, Any] | None, mode: str, relative: str) -> bool:
    if not role_path.is_file() or role_path.is_symlink() or not isinstance(expected, str) or not HEX64.fullmatch(expected):
        return False
    if digest(role_path) == expected:
        return True
    commit = historical_agent_commit(root, relative, projection, mode)
    payload = file_at_git_commit(root, commit, role_path.relative_to(root).as_posix()) if commit else None
    return payload is not None and hashlib.sha256(payload).hexdigest() == expected


def parse_agent_start_plan_v2(
    root: Path,
    relative: str,
    text: str,
    run_id: str,
    projection: dict[str, Any] | None,
    mode: str,
    value: dict[str, Any],
    add,
) -> dict[str, Any] | None:
    fields = {
        "schema_version", "run_id", "contract_revision", "admission_projection_sha256",
        "applicability", "rationale", "spawn_reviewer", "planned_agents",
    }
    reviewer_fields = {"agent_id", "role_path", "role_sha256"}
    planned_fields = {"agent_id", "functions", "activation_stage"}
    problems: list[str] = []
    if set(value) != fields or value.get("schema_version") != "2" or value.get("run_id") != run_id:
        problems.append("schema/top-level/run_id")
    revision = re.search(r"^> Contract revision:\s*`?([0-9]+)`?\s*$", text, re.MULTILINE)
    if not revision or value.get("contract_revision") != int(revision.group(1)):
        problems.append("Contract revision binding")
    expected_projection_sha = canonical_json_sha256(projection) if isinstance(projection, dict) else None
    if value.get("admission_projection_sha256") != expected_projection_sha:
        problems.append("Admission Projection binding")
    if not nonempty_string(value.get("rationale")):
        problems.append("rationale")
    classification = re.search(r"^> Decision class / classification trigger ID:\s*`?(D[0-3])`?\s*/", text, re.MULTILINE)
    decision_class = classification.group(1) if classification else None
    applicability = value.get("applicability")
    reviewer = value.get("spawn_reviewer")
    planned = value.get("planned_agents")
    if not isinstance(reviewer, dict) or set(reviewer) != reviewer_fields:
        problems.append("spawn_reviewer shape")
        reviewer = {}
    if not isinstance(planned, list):
        problems.append("planned_agents shape")
        planned = []
    if applicability == "not_applicable_d0":
        if decision_class != "D0" or planned or reviewer != {"agent_id":"not_applicable", "role_path":"not_applicable", "role_sha256":"not_applicable"}:
            problems.append("D0 proportionality")
    elif applicability == "required":
        if decision_class not in {"D1", "D2", "D3"}:
            problems.append("required applicability/classification")
        spawn_id = reviewer.get("agent_id")
        role_root = root / "harness/product-repo-overlay" if mode == "master" else root
        role_path = role_root / SPAWN_REVIEWER_ROLE_PATH
        if not nonempty_string(spawn_id) or spawn_id == "not_applicable": problems.append("Spawn Reviewer identity")
        if reviewer.get("role_path") != SPAWN_REVIEWER_ROLE_PATH: problems.append("Spawn Reviewer role path")
        if not spawn_role_digest_matches(root, role_path, reviewer.get("role_sha256"), projection, mode, relative): problems.append("Spawn Reviewer role digest")
        agent_ids: list[str] = []
        creators: list[str] = []
        for item in planned:
            if not isinstance(item, dict) or set(item) != planned_fields:
                problems.append("planned Agent shape"); continue
            agent_id = item.get("agent_id")
            functions = item.get("functions")
            stage = item.get("activation_stage")
            if not nonempty_string(agent_id) or agent_id == spawn_id: problems.append("planned Agent identity")
            else: agent_ids.append(agent_id)
            if not unique_strings(functions) or stage not in {"implementation", "review"}: problems.append(f"planned Agent function/stage {agent_id!r}")
            if isinstance(functions, list) and "Creator / Implementer" in functions:
                creators.append(agent_id)
                if stage != "implementation": problems.append("creator activation stage")
        authority = projection.get("authority", {}) if isinstance(projection, dict) else {}
        expected_agents = set(authority.get("agent_ids", [])) if isinstance(authority.get("agent_ids"), list) else set()
        independent_reviewers = set(authority.get("reviewers", [])) if isinstance(authority.get("reviewers"), list) else set()
        if len(agent_ids) != len(set(agent_ids)) or set(agent_ids) != expected_agents: problems.append("planned Agent identity coverage")
        if len(creators) != 1 or set(creators) & independent_reviewers: problems.append("exactly one non-reviewer Creator / Implementer")
        if spawn_id in expected_agents: problems.append("Spawn Reviewer domain/quorum conflict")
        for item in planned:
            if isinstance(item, dict) and item.get("agent_id") in independent_reviewers and item.get("activation_stage") != "review": problems.append("reviewer activation stage")
        budget_blocks = CONVERGENCE_BUDGET_BLOCK.findall(text)
        try:
            budget = json.loads(budget_blocks[0]) if len(budget_blocks) == 1 else {}
            allocated = budget.get("current_run_allocation", {}).get("agent_activations")
        except json.JSONDecodeError:
            allocated = None
        if isinstance(allocated, bool) or not isinstance(allocated, int) or allocated < len(agent_ids) + 1:
            problems.append("cumulative Agent activation budget including Spawn Reviewer")
    else:
        problems.append("applicability")
    if problems:
        add("AHV-AGENT-START-001", "error", relative, f"Agent-start plan is incomplete or contradictory: {sorted(set(problems))}", "correct only the exact topology/identity/role binding")
        return None
    return value


def parse_agent_start_control(
    root: Path,
    relative: str,
    text: str,
    run_id: str,
    projection: dict[str, Any] | None,
    mode: str,
    add,
) -> dict[str, Any] | None:
    historical_commit = historical_agent_commit(root, relative, projection, mode)
    blocks = AGENT_START_CONTROL_BLOCK.findall(text)
    if len(blocks) != 1:
        add("AHV-AGENT-START-001", "error", relative, f"Harness 1.2.0+ Run requires exactly one Agent-start projection; observed {len(blocks)}", "bind one required or not_applicable_d0 Agent-start projection")
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-AGENT-START-001", "error", relative, f"Agent-start JSON is invalid: {error}", "restore one exact compact Agent-start projection")
        return None

    if isinstance(value, dict) and value.get("schema_version") == "2":
        visible_version = projection.get("harness_version") if isinstance(projection, dict) else None
        if not isinstance(visible_version, str) or not SEMVER.fullmatch(visible_version) or semver_tuple(visible_version) < AGENT_START_PLAN_MIN_VERSION:
            add("AHV-AGENT-START-001", "error", relative, "Agent-start plan schema 2 requires Harness 1.2.1+", "retain schema-1 clearance for a pinned 1.2.0 Run or authorize a current Contract migration")
            return None
        return parse_agent_start_plan_v2(root, relative, text, run_id, projection, mode, value, add)

    fields = {"schema_version", "run_id", "contract_revision", "admission_projection_sha256", "applicability", "rationale", "spawn_reviewer", "briefs"}
    reviewer_fields = {"agent_id", "role_path", "role_sha256"}
    item_fields = {"agent_id", "brief", "brief_sha256", "clearance"}
    brief_fields = {
        "functions", "objective", "authority_boundary", "routed_sources", "expected_outputs",
        "required_evidence", "review_questions", "stop_conditions",
    }
    source_fields = {"path", "sha256"}
    clearance_fields = {"reviewer_id", "outcome", "reviewed_subject_sha256", "reviewed_at", "evidence_ref"}
    problems: list[str] = []
    if not isinstance(value, dict) or set(value) != fields:
        problems.append("top-level fields")
        value = value if isinstance(value, dict) else {}
    if value.get("schema_version") != "1" or value.get("run_id") != run_id:
        problems.append("schema/run_id")
    revision = re.search(r"^> Contract revision:\s*`?([0-9]+)`?\s*$", text, re.MULTILINE)
    if not revision or value.get("contract_revision") != int(revision.group(1)):
        problems.append("Contract revision binding")
    expected_projection_sha = canonical_json_sha256(projection) if isinstance(projection, dict) else None
    if value.get("admission_projection_sha256") != expected_projection_sha:
        problems.append("Admission Projection binding")
    if not nonempty_string(value.get("rationale")):
        problems.append("rationale")
    classification = re.search(r"^> Decision class / classification trigger ID:\s*`?(D[0-3])`?\s*/", text, re.MULTILINE)
    decision_class = classification.group(1) if classification else None
    applicability = value.get("applicability")
    reviewer = value.get("spawn_reviewer")
    briefs = value.get("briefs")
    if not isinstance(reviewer, dict) or set(reviewer) != reviewer_fields:
        problems.append("spawn_reviewer shape")
        reviewer = {}
    if not isinstance(briefs, list):
        problems.append("briefs shape")
        briefs = []

    if applicability == "not_applicable_d0":
        if decision_class != "D0":
            problems.append("D0 applicability/classification")
        if reviewer != {"agent_id":"not_applicable", "role_path":"not_applicable", "role_sha256":"not_applicable"} or briefs:
            problems.append("D0 proportionality")
    elif applicability == "required":
        if decision_class not in {"D1", "D2", "D3"}:
            problems.append("required applicability/classification")
        spawn_id = reviewer.get("agent_id")
        if not nonempty_string(spawn_id) or spawn_id == "not_applicable":
            problems.append("Spawn Reviewer identity")
        if reviewer.get("role_path") != SPAWN_REVIEWER_ROLE_PATH:
            problems.append("Spawn Reviewer role path")
        role_root = root / "harness/product-repo-overlay" if mode == "master" else root
        role_path = role_root / SPAWN_REVIEWER_ROLE_PATH
        if not spawn_role_digest_matches(root, role_path, reviewer.get("role_sha256"), projection, mode, relative):
            problems.append("Spawn Reviewer role digest")
        if not briefs:
            problems.append("planned Agent briefs")
        target_ids: list[str] = []
        creator_implementer_ids: list[str] = []
        for item in briefs:
            if not isinstance(item, dict) or set(item) != item_fields:
                problems.append("brief item shape")
                continue
            target_id = item.get("agent_id")
            if not nonempty_string(target_id) or target_id == spawn_id:
                problems.append("target Agent identity/independence")
            else:
                target_ids.append(target_id)
            brief = item.get("brief")
            if not isinstance(brief, dict) or set(brief) != brief_fields:
                problems.append(f"brief shape {target_id!r}")
                continue
            if not unique_strings(brief.get("functions")) or not nonempty_string(brief.get("objective")) or not nonempty_string(brief.get("authority_boundary")):
                problems.append(f"brief role/objective/boundary {target_id!r}")
            elif "Creator / Implementer" in brief["functions"] and nonempty_string(target_id):
                creator_implementer_ids.append(target_id)
            for field in ("expected_outputs", "required_evidence", "review_questions", "stop_conditions"):
                if not unique_strings(brief.get(field)):
                    problems.append(f"brief.{field} {target_id!r}")
            sources = brief.get("routed_sources")
            source_paths: list[str] = []
            if not isinstance(sources, list) or not sources:
                problems.append(f"brief.routed_sources {target_id!r}")
            else:
                for source in sources:
                    if not isinstance(source, dict) or set(source) != source_fields or not nonempty_string(source.get("path")) or HEX64.fullmatch(str(source.get("sha256", ""))) is None:
                        problems.append(f"routed source shape {target_id!r}")
                        continue
                    try:
                        source_relative = safe_relative(source["path"]).as_posix()
                    except ValueError:
                        problems.append(f"unsafe routed source {target_id!r}")
                        continue
                    source_paths.append(source_relative)
                    source_path = root / source_relative
                    current_match = source_path.is_file() and not source_path.is_symlink() and digest(source_path) == source["sha256"]
                    prior = file_at_git_commit(root, historical_commit, source_relative) if historical_commit else None
                    if not current_match and not (prior is not None and hashlib.sha256(prior).hexdigest() == source["sha256"]):
                        problems.append(f"stale routed source {source_relative!r}")
                if len(source_paths) != len(set(source_paths)):
                    problems.append(f"duplicate routed source {target_id!r}")
            observed_brief_digest = canonical_json_sha256(brief)
            if item.get("brief_sha256") != observed_brief_digest:
                problems.append(f"brief digest {target_id!r}")
            clearance = item.get("clearance")
            if not isinstance(clearance, dict) or set(clearance) != clearance_fields:
                problems.append(f"clearance shape {target_id!r}")
                continue
            expected_subject_sha = agent_start_subject_sha256(value, item)
            if clearance.get("reviewer_id") != spawn_id or clearance.get("outcome") != "pass" or clearance.get("reviewed_subject_sha256") != expected_subject_sha or not nonempty_string(clearance.get("evidence_ref")):
                problems.append(f"clearance binding/outcome {target_id!r}")
            try:
                reviewed_at = datetime.fromisoformat(str(clearance.get("reviewed_at", "")).replace("Z", "+00:00"))
                if reviewed_at.tzinfo is None:
                    raise ValueError
            except ValueError:
                problems.append(f"clearance timestamp {target_id!r}")
        if len(target_ids) != len(set(target_ids)):
            problems.append("duplicate target Agent")
        authority = projection.get("authority", {}) if isinstance(projection, dict) else {}
        expected_agents = set(authority.get("agent_ids", [])) if isinstance(authority.get("agent_ids"), list) else set()
        independent_reviewers = set(authority.get("reviewers", [])) if isinstance(authority.get("reviewers"), list) else set()
        if expected_agents != set(target_ids):
            problems.append(f"planned Agent coverage missing={sorted(expected_agents - set(target_ids))} extra={sorted(set(target_ids) - expected_agents)}")
        if len(creator_implementer_ids) != 1 or set(creator_implementer_ids) & independent_reviewers:
            problems.append("exactly one non-reviewer Creator / Implementer function")
        if spawn_id in expected_agents:
            problems.append("Spawn Reviewer domain/quorum conflict")
        budget_blocks = CONVERGENCE_BUDGET_BLOCK.findall(text)
        try:
            budget = json.loads(budget_blocks[0]) if len(budget_blocks) == 1 else {}
            allocated_activations = budget.get("current_run_allocation", {}).get("agent_activations")
        except json.JSONDecodeError:
            allocated_activations = None
        if isinstance(allocated_activations, bool) or not isinstance(allocated_activations, int) or allocated_activations < len(target_ids) + 1:
            problems.append("cumulative Agent activation budget including Spawn Reviewer")
    else:
        problems.append("applicability")

    if problems:
        add("AHV-AGENT-START-001", "error", relative, f"Agent-start control is incomplete, non-independent, or stale: {sorted(set(problems))}", "correct only the exact brief/source/identity/clearance binding; do not add a second criterion model")
        return None
    return value


def agent_activation_subject_sha256(value: dict[str, Any]) -> str:
    return canonical_json_sha256({
        "schema_version":"1", "phase":value.get("phase"), "authority_ref":value.get("authority_ref"),
        "run_id":value.get("run_id"), "contract_revision":value.get("contract_revision"),
        "admission_projection_sha256":value.get("admission_projection_sha256"),
        "spawn_reviewer":value.get("spawn_reviewer"), "agent_id":value.get("agent_id"),
        "brief_sha256":value.get("brief_sha256"),
    })


def agent_assignment_subject_sha256(value: dict[str, Any]) -> str:
    return canonical_json_sha256({
        "schema_version":"1", "phase":"assignment_preparation",
        "authority_ref":value.get("authority_ref"), "spawn_reviewer":value.get("spawn_reviewer"),
        "agent_id":value.get("agent_id"), "brief_sha256":value.get("brief_sha256"),
    })


def parse_agent_activation_record(
    root: Path,
    relative: str,
    text: str,
    plan: dict[str, Any],
    projection: dict[str, Any],
    mode: str,
    add,
    pinned_release_commit: str | None = None,
) -> dict[str, Any] | None:
    pinned_release_commit = pinned_release_commit or historical_agent_commit(root, relative, projection, mode)
    blocks = AGENT_ACTIVATION_BLOCK.findall(text)
    if len(blocks) != 1:
        add("AHV-AGENT-START-003", "error", relative, f"Agent Activation Record blocks={len(blocks)}", "retain one exact activation block")
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-AGENT-START-003", "error", relative, f"Agent Activation JSON is invalid: {error}", "restore one exact activation record")
        return None
    fields = {
        "schema_version", "phase", "method", "authority_ref", "run_id", "contract_revision",
        "admission_projection_sha256", "agent_id", "brief", "brief_sha256", "spawn_reviewer",
        "pre_run_clearance_subject_sha256", "clearance",
    }
    brief_fields = {"functions", "objective", "authority_boundary", "routed_sources", "expected_outputs", "required_evidence", "review_questions", "stop_conditions"}
    source_fields = {"path", "sha256"}
    reviewer_fields = {"agent_id", "role_path", "role_sha256"}
    clearance_fields = {"reviewer_id", "outcome", "reviewed_subject_sha256", "reviewed_at", "evidence_ref"}
    problems: list[str] = []
    if not isinstance(value, dict) or set(value) != fields:
        problems.append("fields"); value = value if isinstance(value, dict) else {}
    if value.get("schema_version") != "1" or value.get("phase") != "run_activation" or value.get("method") not in {"spawn_review_pass", "deterministic_unchanged_assignment"}:
        problems.append("schema/phase/method")
    if value.get("run_id") != plan.get("run_id") or value.get("contract_revision") != plan.get("contract_revision") or value.get("admission_projection_sha256") != plan.get("admission_projection_sha256"):
        problems.append("Run/Projection binding")
    if value.get("authority_ref") != projection.get("authority", {}).get("decision_authority_ref"):
        problems.append("authority binding")
    planned = {item.get("agent_id"): item for item in plan.get("planned_agents", []) if isinstance(item, dict)}
    agent_id = value.get("agent_id")
    if agent_id not in planned:
        problems.append("planned Agent identity")
    brief = value.get("brief")
    if not isinstance(brief, dict) or set(brief) != brief_fields:
        problems.append("brief shape"); brief = {}
    else:
        if brief.get("functions") != planned.get(agent_id, {}).get("functions") or not nonempty_string(brief.get("objective")) or not nonempty_string(brief.get("authority_boundary")):
            problems.append("brief function/objective/boundary")
        for field in ("expected_outputs", "required_evidence", "review_questions", "stop_conditions"):
            if not unique_strings(brief.get(field)): problems.append(f"brief.{field}")
        sources = brief.get("routed_sources")
        source_paths: list[str] = []
        if not isinstance(sources, list) or not sources:
            problems.append("brief.routed_sources")
        else:
            for source in sources:
                if not isinstance(source, dict) or set(source) != source_fields or not nonempty_string(source.get("path")) or HEX64.fullmatch(str(source.get("sha256", ""))) is None:
                    problems.append("routed source shape"); continue
                try: source_relative = safe_relative(source["path"]).as_posix()
                except ValueError: problems.append("unsafe routed source"); continue
                source_paths.append(source_relative)
                source_path = root / source_relative
                current_match = source_path.is_file() and not source_path.is_symlink() and digest(source_path) == source["sha256"]
                baseline_match = False
                if not current_match and planned.get(agent_id, {}).get("activation_stage") == "implementation" and projection.get("repository", {}).get("git_mutation"):
                    prior = file_at_git_commit(root, projection["repository"]["start_commit"], source_relative)
                    baseline_match = prior is not None and hashlib.sha256(prior).hexdigest() == source["sha256"]
                pinned = file_at_git_commit(root, pinned_release_commit, source_relative) if pinned_release_commit else None
                pinned_match = pinned is not None and hashlib.sha256(pinned).hexdigest() == source["sha256"]
                if not current_match and not baseline_match and not pinned_match: problems.append(f"stale routed source {source_relative!r}")
            if len(source_paths) != len(set(source_paths)): problems.append("duplicate routed source")
    if value.get("brief_sha256") != canonical_json_sha256(brief): problems.append("brief digest")
    reviewer = value.get("spawn_reviewer")
    role_root = root / "harness/product-repo-overlay" if mode == "master" else root
    role_path = role_root / SPAWN_REVIEWER_ROLE_PATH
    if not isinstance(reviewer, dict) or set(reviewer) != reviewer_fields or reviewer != plan.get("spawn_reviewer"):
        problems.append("Spawn Reviewer binding")
    elif not spawn_role_digest_matches(root, role_path, reviewer.get("role_sha256"), projection, mode, relative):
        problems.append("Spawn Reviewer role digest")
    clearance = value.get("clearance")
    if not isinstance(clearance, dict) or set(clearance) != clearance_fields:
        problems.append("clearance shape"); clearance = {}
    method = value.get("method")
    expected_subject = (
        agent_assignment_subject_sha256(value)
        if method == "deterministic_unchanged_assignment"
        else agent_activation_subject_sha256(value)
    )
    if clearance.get("reviewer_id") != reviewer.get("agent_id") or clearance.get("outcome") != "pass" or clearance.get("reviewed_subject_sha256") != expected_subject or not nonempty_string(clearance.get("evidence_ref")):
        problems.append("clearance binding/outcome")
    try:
        reviewed_at = datetime.fromisoformat(str(clearance.get("reviewed_at", "")).replace("Z", "+00:00"))
        if reviewed_at.tzinfo is None: raise ValueError
    except ValueError: problems.append("clearance timestamp")
    pre_subject = value.get("pre_run_clearance_subject_sha256")
    if method == "deterministic_unchanged_assignment":
        if pre_subject != agent_assignment_subject_sha256(value): problems.append("pre-Run rebind subject")
    elif pre_subject != "not_applicable":
        problems.append("fresh pass pre-Run applicability")
    if problems:
        add("AHV-AGENT-START-003", "error", relative, f"Agent activation is incomplete, stale, or contradictory: {sorted(set(problems))}", "refresh only the exact responsibility-time brief/clearance binding")
        return None
    value["_path"] = relative
    return value


def pre_agent_start_boundary_commit(root: Path, mode: str) -> str | None:
    if not (root / ".git").exists():
        return None
    metadata_relative = "harness/release/release-plan.json" if mode == "master" else ".agentic-harness/release-metadata.json"
    history = subprocess.run(
        ["git", "rev-list", "--reverse", "HEAD", "--", metadata_relative],
        cwd=root, text=True, capture_output=True, check=False,
    )
    if history.returncode:
        return None
    records: list[tuple[str, str, str]] = []
    version_field = "release_version" if mode == "master" else "harness_version"
    for commit in history.stdout.splitlines():
        observed = subprocess.run(
            ["git", "show", f"{commit}:{metadata_relative}"],
            cwd=root, text=True, capture_output=True, check=False,
        )
        if observed.returncode:
            continue
        try:
            metadata = json.loads(observed.stdout)
            version = metadata.get(version_field)
            release_tag = metadata.get("release_tag")
        except json.JSONDecodeError:
            continue
        if isinstance(version, str) and SEMVER.fullmatch(version) and isinstance(release_tag, str):
            records.append((commit, version, release_tag))
    first_current = next((
        commit for commit, version, release_tag in records
        if semver_tuple(version) >= AGENT_START_MIN_VERSION
        and re.fullmatch(r"[0-9]{8}-[0-9]+\.[0-9]+\.[0-9]+-[a-z0-9][a-z0-9-]*", release_tag)
    ), None)
    if first_current is None:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, text=True, capture_output=True, check=False)
        return head.stdout.strip() if head.returncode == 0 else None
    parent = subprocess.run(["git", "rev-parse", f"{first_current}^"], cwd=root, text=True, capture_output=True, check=False)
    return parent.stdout.strip() if parent.returncode == 0 else None


def event_predates_agent_start_control(root: Path, event_path: Path, mode: str) -> bool:
    boundary = pre_agent_start_boundary_commit(root, mode)
    if not boundary:
        return False
    relative = event_path.as_posix()
    observed = subprocess.run(
        ["git", "show", f"{boundary}:{relative}"],
        cwd=root, capture_output=True, check=False,
    )
    current = root / relative
    return observed.returncode == 0 and current.is_file() and observed.stdout == current.read_bytes()


def validate_agent_start_controls(
    root: Path,
    records: dict[str, tuple[Path, str, bool]],
    events: list[dict[str, Any]],
    mode: str,
    add,
) -> None:
    event_subjects = {event["subject_id"] for event in events}
    installed_version = current_harness_version(root, mode)
    activation_records = [
        (relative, text)
        for relative, (_path, text, is_template) in records.items()
        if not is_template and AGENT_ACTIVATION_BLOCK.search(text)
    ]
    for relative, (_path, text, is_template) in records.items():
        identifier = ARTIFACT_ID.search(text)
        run_id = identifier.group(1) if identifier else None
        is_run = bool(
            run_id and "/run-events/" not in f"/{relative}" and "-EVENT-" not in run_id
            and (run_id in event_subjects or run_id.startswith("AH-RUN-") or re.search(r"^# (?:Execution )?Run(?: Contract)?\b", text, re.MULTILINE))
        )
        if is_template or not is_run:
            continue
        if DIRECT_RUN_BLOCK.search(text):
            continue
        version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
        applicable = bool(version and SEMVER.fullmatch(version.group(1)) and semver_tuple(version.group(1)) >= AGENT_START_MIN_VERSION)
        if not applicable:
            if AGENT_START_CONTROL_BLOCK.search(text):
                add("AHV-AGENT-START-001", "error", relative, "an Agent-start projection cannot be hidden under a pre-1.2.0 Harness binding", "use the authorized pinned rules or migrate the Contract before current activation")
            if SEMVER.fullmatch(installed_version) and semver_tuple(installed_version) >= AGENT_START_MIN_VERSION:
                activations = [event for event in events if event["subject_id"] == run_id and event["event_kind"] == "state" and event["to"] == "active"]
                for activation in activations:
                    if not event_predates_agent_start_control(root, activation["path"], mode):
                        add("AHV-AGENT-START-002", "error", activation["path"].as_posix(), "pre-1.2.0 activation lacks byte-identical pre-upgrade Git lineage", "retain a proven pre-upgrade active event or migrate the Contract and obtain current Agent-start clearance before activation")
            continue
        projection: dict[str, Any] | None = None
        projection_blocks = ADMISSION_PROJECTION_BLOCK.findall(text)
        if len(projection_blocks) == 1:
            try:
                candidate = json.loads(projection_blocks[0])
                projection = candidate if isinstance(candidate, dict) else None
            except json.JSONDecodeError:
                projection = None
        plan = parse_agent_start_control(root, relative, text, run_id, projection, mode, add)
        if not plan or plan.get("schema_version") != "2" or plan.get("applicability") != "required" or not isinstance(projection, dict):
            continue
        pinned_release_commit = None
        if mode == "master" and version and SEMVER.fullmatch(installed_version):
            if semver_tuple(version.group(1)) < semver_tuple(installed_version):
                pinned_release_commit = release_commit_for_version(root, version.group(1))
        activated: list[str] = []
        parsed_activations: list[dict[str, Any]] = []
        for activation_relative, activation_text in activation_records:
            blocks = AGENT_ACTIVATION_BLOCK.findall(activation_text)
            if len(blocks) != 1:
                continue
            try: raw = json.loads(blocks[0])
            except json.JSONDecodeError: continue
            if not isinstance(raw, dict) or raw.get("run_id") != run_id:
                continue
            parsed = parse_agent_activation_record(
                root, activation_relative, activation_text, plan, projection, mode, add,
                pinned_release_commit=pinned_release_commit,
            )
            if parsed:
                activated.append(parsed["agent_id"])
                parsed_activations.append(parsed)
        if len(activated) != len(set(activated)):
            add("AHV-AGENT-START-003", "error", relative, "duplicate current Agent activation record", "retain one exact current record per Agent/Run revision")
        active_events = [event for event in events if event["subject_id"] == run_id and event["event_kind"] == "state" and event["to"] == "active"]
        admission_time: datetime | None = None
        if active_events:
            blocks = ADMISSION_REPORT_BLOCK.findall(sorted(active_events, key=lambda item: item["sequence"])[0]["text"])
            if len(blocks) == 1:
                try:
                    evaluated_at = json.loads(blocks[0]).get("evaluated_at")
                    admission_time = datetime.fromisoformat(str(evaluated_at).replace("Z", "+00:00"))
                except (AttributeError, json.JSONDecodeError, TypeError, ValueError):
                    admission_time = None
        planned_by_id = {item["agent_id"]: item for item in plan.get("planned_agents", [])}
        for activation in parsed_activations:
            if planned_by_id.get(activation["agent_id"], {}).get("activation_stage") != "review" or admission_time is None:
                continue
            reviewed_at = datetime.fromisoformat(str(activation["clearance"]["reviewed_at"]).replace("Z", "+00:00"))
            if reviewed_at <= admission_time:
                add("AHV-AGENT-START-003", "error", activation["_path"], "reviewer activation predates the implementation candidate boundary", "activate the reviewer only after initial admission against exact candidate/evidence sources")
        latest = sorted((event for event in events if event["subject_id"] == run_id), key=lambda item: item["sequence"])
        if latest and latest[-1]["to"] == "completed":
            planned_ids = {item["agent_id"] for item in plan.get("planned_agents", [])}
            if set(activated) != planned_ids:
                add("AHV-AGENT-START-004", "error", relative, f"completed Run lacks claimed-participant activation; missing={sorted(planned_ids - set(activated))}", "activate each actual reviewer against the exact candidate before completion")


def parse_event(path: Path, text: str, mode: str, add) -> dict[str, Any] | None:
    relative = path.as_posix()
    subject = re.search(r"^> Immutable subject:\s*(?:Run Contract\s*)?`([^`]+)`(?:\s+revision\s+`?([0-9]+)`?)?(?:\s+revision)?(?:\s+[^\n]*?)?SHA-256\s*`([0-9a-f]{64})`", text, re.MULTILINE)
    sequence = re.search(r"^- Sequence:\s*`([0-9]+)`", text, re.MULTILINE)
    previous = re.search(r"^- Previous-event SHA-256:\s*`([^`]+)`", text, re.MULTILINE)
    combined = re.search(r"^- Sequence / previous-event SHA-256:\s*`?([0-9]+)`?\s*/\s*`([^`]+)`", text, re.MULTILINE)
    transition = re.search(r"^- From / to:\s*`([^`]+)`\s*/\s*`([^`]+)`", text, re.MULTILINE)
    actor = re.search(r"^- Actor(?: / Decision Authority)?:\s*(.+)$", text, re.MULTILINE)
    authority = re.search(r"^- Decision Authority reference:\s*(.+)$", text, re.MULTILINE)
    guard = re.search(r"^- Guard(?: and)? evidence:\s*(.+)$", text, re.MULTILINE)
    lease = re.search(r"^- Lease (?:evidence|event/key/claim(?: digest)?):\s*(.+)$", text, re.MULTILINE)
    if combined and not sequence: sequence = combined
    previous_value = previous.group(1) if previous else combined.group(2) if combined else None
    if not all((subject, sequence, previous_value, transition, actor, guard, lease)):
        add("AHV-RUN-001", "error", relative, "incomplete Run State Event metadata", "bind subject, sequence, previous, transition, actor, authority, guard, and lease"); return None
    legacy = mode == "master" and path.as_posix() == "docs/work/run-events/AH-RUN-MASTER-001-004-active.md" and previous_value == "genesis-migration" and int(sequence.group(1)) == 4 and transition.groups() == ("authorized", "active") and subject.group(1) == "AH-WORK-MASTER-BUILD-001"
    if not authority and not legacy:
        add("AHV-RUN-012", "error", relative, "Decision Authority reference is missing", "record the exact separate authority reference"); authority_value = ""
    else:
        authority_value = authority.group(1).strip() if authority else actor.group(1).split(" / ")[-1].strip()
    revision_blocks = CONTRACT_REVISION_EVENT_BLOCK.findall(text)
    revision_event: dict[str, Any] | None = None
    if revision_blocks:
        if len(revision_blocks) != 1:
            add("AHV-CONTRACT-002", "error", relative, f"Contract revision event blocks={len(revision_blocks)}", "retain one exact Contract Revision Event block")
        else:
            try:
                candidate = json.loads(revision_blocks[0])
                revision_event = candidate if isinstance(candidate, dict) else None
            except json.JSONDecodeError:
                revision_event = None
            if revision_event is None:
                add("AHV-CONTRACT-002", "error", relative, "Contract Revision Event JSON is invalid", "use one valid revision-event projection")
    values = {
        "subject_id": subject.group(1), "contract_revision": int(subject.group(2)) if subject.group(2) else None,
        "contract_digest": subject.group(3), "sequence": int(sequence.group(1)), "previous": previous_value,
        "from": transition.group(1), "to": transition.group(2), "actor": actor.group(1).strip(),
        "authority": authority_value, "guard": guard.group(1).strip(), "lease": lease.group(1).strip(),
        "path": path, "text": text, "event_kind": "contract_revision" if revision_blocks else "state",
        "revision_event": revision_event,
    }
    for name in ("actor", "authority", "guard", "lease"):
        if not values[name] or "{{" in values[name] or values[name].lower() in {"none", "tbd", "todo"}: add("AHV-RUN-005", "error", relative, f"Run event has unresolved {name}", "record exact observed evidence/reference")
    return values


def validate_event_chains(root: Path, events: list[tuple[Path, str]], id_paths: dict[str, Path], mode: str, add) -> list[dict[str, Any]]:
    parsed = [event for path, text in events if (event := parse_event(path.relative_to(root), text, mode, add))]
    by_contract: dict[str, list[dict[str, Any]]] = {}
    for event in parsed:
        transition = (event["from"], event["to"])
        revision_transition = event["event_kind"] == "contract_revision" and (
            (event["from"] in {"proposed", "preflight", "preflight_blocked", "paused", "blocked", "changes_requested"} and event["to"] == "preflight")
            or (
                event["from"] in {"completed", "cancelled"} and event["to"] == event["from"]
                and isinstance(event["revision_event"], dict)
                and event["revision_event"].get("change_kind") == "schema_migration"
            )
        )
        if not revision_transition and transition not in RUN_TRANSITIONS and not (event["from"] in NON_TERMINAL and event["to"] == "cancelled"):
            add("AHV-RUN-003", "error", event["path"].as_posix(), f"invalid transition {event['from']} -> {event['to']}", "use AH-SPEC-WORK-001")
        by_contract.setdefault(event["subject_id"], []).append(event)
    for contract, chain in by_contract.items():
        subject_path = id_paths.get(contract)
        current_digest = digest(subject_path) if subject_path else None
        current_text = subject_path.read_text(encoding="utf-8") if subject_path else ""
        visible_version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", current_text, re.MULTILINE)
        revision_match = re.search(r"^> Contract revision:\s*`?([0-9]+)`?\s*$", current_text, re.MULTILINE)
        current_revision = int(revision_match.group(1)) if revision_match else 1
        revision_blocks = CONTRACT_REVISION_BLOCK.findall(current_text)
        requires_revision_field = bool(
            visible_version and SEMVER.fullmatch(visible_version.group(1))
            and semver_tuple(visible_version.group(1)) >= CONTRACT_REVISION_MIN_VERSION
        )
        if not subject_path:
            add("AHV-RUN-002", "error", chain[0]["path"].as_posix(), f"missing Contract {contract}", "restore the current Contract")
        if requires_revision_field and not revision_match:
            add("AHV-CONTRACT-001", "error", subject_path.relative_to(root).as_posix() if subject_path else contract, "current-schema Run Contract lacks a positive Contract revision", "record Contract revision 1 or the authorized successor revision")
        if current_revision < 1:
            add("AHV-CONTRACT-001", "error", subject_path.relative_to(root).as_posix() if subject_path else contract, "Contract revision must be positive", "use a positive contiguous revision")

        revision_events = [event for event in chain if event["event_kind"] == "contract_revision" and event["revision_event"]]
        allowed_digests = {current_digest} if current_digest else set()
        prior_new_revision = 1
        prior_new_digest: str | None = None
        last_projection: dict[str, Any] | None = None
        for event in sorted(revision_events, key=lambda item: item["sequence"]):
            value = event["revision_event"]
            required = {
                "schema_version", "event_kind", "run_id", "previous_revision", "previous_contract_sha256",
                "new_revision", "new_contract_sha256", "change_kind", "reason", "authority_ref", "previous_git_commit",
            }
            valid_shape = isinstance(value, dict) and set(value) == required
            previous_revision = value.get("previous_revision") if valid_shape else None
            new_revision = value.get("new_revision") if valid_shape else None
            previous_sha = value.get("previous_contract_sha256") if valid_shape else None
            new_sha = value.get("new_contract_sha256") if valid_shape else None
            fields_valid = bool(
                valid_shape and value.get("schema_version") == "1" and value.get("event_kind") == "contract_revision"
                and value.get("run_id") == contract and isinstance(previous_revision, int) and not isinstance(previous_revision, bool)
                and isinstance(new_revision, int) and not isinstance(new_revision, bool) and new_revision == previous_revision + 1
                and HEX64.fullmatch(str(previous_sha or "")) and HEX64.fullmatch(str(new_sha or ""))
                and value.get("change_kind") in {"amendment", "schema_migration"}
                and nonempty_string(value.get("reason")) and nonempty_string(value.get("authority_ref"))
                and re.fullmatch(r"[0-9a-f]{40,64}", str(value.get("previous_git_commit", "")))
                and event["contract_digest"] == new_sha and event["contract_revision"] in {None, new_revision}
                and event["authority"] == value.get("authority_ref")
            )
            if prior_new_digest is None:
                fields_valid = fields_valid and previous_revision == 1
            else:
                fields_valid = fields_valid and previous_revision == prior_new_revision and previous_sha == prior_new_digest
            if fields_valid and subject_path:
                previous_bytes = file_at_git_commit(root, value["previous_git_commit"], subject_path.relative_to(root).as_posix())
                previous_text = previous_bytes.decode("utf-8", errors="replace") if previous_bytes is not None else ""
                previous_revision_match = re.search(r"^> Contract revision:\s*`?([0-9]+)`?\s*$", previous_text, re.MULTILINE)
                previous_visible_revision = int(previous_revision_match.group(1)) if previous_revision_match else 1
                fields_valid = bool(
                    previous_bytes is not None and hashlib.sha256(previous_bytes).hexdigest() == previous_sha
                    and previous_visible_revision == previous_revision
                    and ARTIFACT_ID.search(previous_text)
                    and ARTIFACT_ID.search(previous_text).group(1) == contract
                )
            if not fields_valid:
                add("AHV-CONTRACT-002", "error", event["path"].as_posix(), "Contract Revision Event is incomplete, non-contiguous, unauthorized, or lacks exact Git/digest evidence", "bind one increment, prior/new digests, reason, authority, and Git commit containing the prior revision")
            else:
                allowed_digests.update({previous_sha, new_sha})
                prior_new_revision = new_revision
                prior_new_digest = new_sha
                last_projection = value

        if current_revision == 1 and revision_blocks:
            add("AHV-CONTRACT-001", "error", subject_path.relative_to(root).as_posix() if subject_path else contract, "revision 1 must not carry a predecessor block", "remove the block or increment through an authorized revision event")
        if current_revision > 1:
            current_projection: dict[str, Any] | None = None
            if len(revision_blocks) == 1:
                try:
                    candidate = json.loads(revision_blocks[0]); current_projection = candidate if isinstance(candidate, dict) else None
                except json.JSONDecodeError:
                    current_projection = None
            required_current = {"schema_version", "revision", "previous_revision", "previous_contract_sha256", "change_kind", "reason", "authority_ref", "previous_git_commit", "target_harness_version"}
            matches_last = bool(
                current_projection and set(current_projection) == required_current and last_projection
                and current_projection["schema_version"] == "1"
                and current_projection["revision"] == current_revision == last_projection["new_revision"]
                and current_projection["previous_revision"] == last_projection["previous_revision"]
                and current_projection["previous_contract_sha256"] == last_projection["previous_contract_sha256"]
                and current_projection["change_kind"] == last_projection["change_kind"]
                and current_projection["reason"] == last_projection["reason"]
                and current_projection["authority_ref"] == last_projection["authority_ref"]
                and current_projection["previous_git_commit"] == last_projection["previous_git_commit"]
                and visible_version and current_projection["target_harness_version"] == visible_version.group(1)
                and last_projection["new_contract_sha256"] == current_digest
            )
            if not matches_last:
                add("AHV-CONTRACT-001", "error", subject_path.relative_to(root).as_posix() if subject_path else contract, "current Contract revision lacks its exact authorized predecessor/event lineage", "align the current revision block with the latest valid Contract Revision Event")

        for event in chain:
            if event["contract_digest"] not in allowed_digests:
                add("AHV-RUN-002", "error", event["path"].as_posix(), f"unrecognized Contract revision digest for {contract}", "bind the current digest or an authorized revision-lineage digest")
        sequence_values = [event["sequence"] for event in chain]
        if len(set(sequence_values)) != len(sequence_values): add("AHV-RUN-006", "error", contract, "duplicate/forked event sequence", "retain one immutable event per sequence")
        chain.sort(key=lambda event: event["sequence"])
        genesis = chain[0]["previous"]
        start = chain[0]["sequence"]
        if genesis == "genesis" and start != 1: add("AHV-RUN-007", "error", contract, "normal genesis must start at sequence 1", "restore contiguous ledger")
        elif genesis == "genesis-migration":
            event = chain[0]
            valid_legacy = mode == "master" and event["path"].as_posix() == "docs/work/run-events/AH-RUN-MASTER-001-004-active.md" and event["subject_id"] == "AH-WORK-MASTER-BUILD-001" and event["sequence"] == 4 and (event["from"], event["to"]) == ("authorized", "active")
            if not valid_legacy: add("AHV-RUN-013", "error", contract, "genesis-migration is forbidden outside the one bound Master legacy event", "use a normal genesis and complete chain")
        elif genesis not in {"genesis", "genesis-migration"}: add("AHV-RUN-007", "error", contract, "first event lacks valid genesis", "start with genesis or documented genesis-migration")
        terminal_seen = False
        for index, current in enumerate(chain):
            if terminal_seen and current["event_kind"] != "contract_revision":
                add("AHV-RUN-011", "error", current["path"].as_posix(), "state event follows terminal state", "retain terminal state; only an audit-only Contract Revision Event may follow")
            if current["to"] in {"completed", "cancelled"}:
                terminal_seen = True
            if index == 0:
                continue
            prior = chain[index - 1]
            if current["sequence"] != prior["sequence"] + 1: add("AHV-RUN-008", "error", contract, "event sequence is not contiguous", "restore the missing immutable event")
            prior_digest = digest(root / prior["path"])
            if current["previous"] != prior_digest: add("AHV-RUN-009", "error", current["path"].as_posix(), "previous digest does not bind immediate prior event", "use exact prior event digest")
            if current["from"] != prior["to"]: add("AHV-RUN-010", "error", current["path"].as_posix(), "state continuity mismatch", "set from state to prior event to state")
    return parsed


def validate_admission_report(
    root: Path,
    event: dict[str, Any],
    contract_path: Path,
    projection: dict[str, Any],
    mode: str,
    add,
) -> tuple[str, dict[str, Any]] | None:
    relative = event["path"].as_posix()
    blocks = ADMISSION_REPORT_BLOCK.findall(event["text"])
    report_digest = re.search(r"^- Admission report SHA-256:\s*`([0-9a-f]{64})`\s*$", event["text"], re.MULTILINE)
    if len(blocks) != 1 or not report_digest:
        add("AHV-ADMISSION-003", "error", relative, f"active transition requires one embedded Admission Report and digest; reports={len(blocks)}, digest={bool(report_digest)}", "generate one green report with this validator and embed it in the active Run State Event")
        return None
    try:
        report = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-ADMISSION-003", "error", relative, f"Admission Report JSON is invalid: {error}", "embed the exact generated JSON report")
        return None
    fields = {
        "schema_version", "report_id", "subject_run_id", "contract_sha256", "ruleset_id",
        "harness_version", "intended_transition", "repository", "authority_ref",
        "environment_disposition", "lease", "evaluated_at", "tool_id", "rule_results", "claims",
    }
    agent_start_applicable = semver_tuple(projection["harness_version"]) >= AGENT_START_MIN_VERSION
    if agent_start_applicable:
        fields.add("agent_start_control_sha256")
    problems: list[str] = []
    if not isinstance(report, dict):
        problems.append("report fields")
        report = {}
    if report.get("schema_version") != "1" or not nonempty_string(report.get("report_id")):
        problems.append("schema/report_id")
    expected_transition = {"from": event["from"], "to": event["to"]}
    if report.get("subject_run_id") != projection["run_id"] or report.get("contract_sha256") != digest(contract_path):
        problems.append("Contract ID/digest")
    if report.get("ruleset_id") != projection["ruleset_id"] or report.get("harness_version") != projection["harness_version"]:
        problems.append("Harness release/ruleset")
    if report.get("intended_transition") != expected_transition or (event["from"], event["to"]) not in ADMISSION_ACTIVE_TRANSITIONS:
        problems.append("intended transition")
    if event["authority"] != projection["authority"]["decision_authority_ref"]:
        problems.append("active Event authority")
    repository = report.get("repository")
    expected_repository = dict(projection["repository"])
    if not isinstance(repository, dict) or set(repository) != set(expected_repository) | {"observed_head_commit", "observed_dirty_sha256"}:
        problems.append("repository report shape")
    else:
        observed_head = repository.get("observed_head_commit")
        observed_dirty = repository.get("observed_dirty_sha256")
        if any(repository.get(field) != value for field, value in expected_repository.items()):
            problems.append("repository baseline/branch target")
        if expected_repository["git_mutation"]:
            valid_observed_head = bool(re.fullmatch(r"[0-9a-f]{40,64}", str(observed_head or "")))
            if not valid_observed_head:
                problems.append("observed head commit")
            if not HEX64.fullmatch(str(observed_dirty or "")):
                problems.append("observed dirty-state digest")
            if valid_observed_head and (root / ".git").exists():
                result = subprocess.run(["git", "cat-file", "-e", f"{observed_head}^{{commit}}"], cwd=root, capture_output=True, check=False)
                if result.returncode:
                    problems.append("unresolvable observed head commit")
                ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", projection["repository"]["start_commit"], observed_head], cwd=root, capture_output=True, check=False)
                if ancestor.returncode:
                    problems.append("observed head outside starting-commit ancestry")
        elif observed_head != "not_applicable" or observed_dirty != "not_applicable":
            problems.append("non-Git observed repository state")
    if report.get("authority_ref") != projection["authority"]["decision_authority_ref"]:
        problems.append("authority")
    if report.get("environment_disposition") != admission_environment(projection):
        problems.append("environment disposition")
    lease = report.get("lease")
    if not isinstance(lease, dict) or set(lease) != {"key", "owner", "evidence"}:
        problems.append("lease report shape")
    else:
        expected_lease = projection["lease"]
        if lease.get("key") != expected_lease["key"] or lease.get("owner") != expected_lease["owner"] or not nonempty_string(lease.get("evidence")) or lease.get("evidence") != event["lease"]:
            problems.append("lease key/owner/evidence")
        elif expected_lease["disposition"] == "required":
            try:
                _lease_path, lease_data = evidence_reference(root, lease["evidence"])
                required_lease = {"schema_version":"1", "key":expected_lease["key"], "target":expected_lease["target"], "owner":expected_lease["owner"], "run_id":projection["run_id"], "state":"claimed"}
                if any(lease_data.get(field) != expected for field, expected in required_lease.items()):
                    problems.append("lease evidence content")
            except (OSError, ValueError, json.JSONDecodeError):
                problems.append("lease evidence reference")
        elif not str(lease.get("evidence", "")).startswith("not_applicable:"):
            problems.append("lease non-applicability evidence")
    parsed_time: datetime | None = None
    try:
        evaluated = str(report.get("evaluated_at", "")).replace("Z", "+00:00")
        parsed_time = datetime.fromisoformat(evaluated)
        if parsed_time.tzinfo is None:
            raise ValueError("timezone missing")
    except ValueError:
        problems.append("evaluation timestamp")
    if report.get("tool_id") != f"validate_harness.py@{projection['harness_version']}":
        problems.append("tool identity")
    if agent_start_applicable:
        identifier = ARTIFACT_ID.search(contract_path.read_text(encoding="utf-8"))
        control = parse_agent_start_control(
            root,
            contract_path.relative_to(root).as_posix(),
            contract_path.read_text(encoding="utf-8"),
            identifier.group(1) if identifier else projection["run_id"],
            projection,
            mode,
            lambda *_args: None,
        )
        expected_control_digest = canonical_json_sha256(control) if control else None
        if report.get("agent_start_control_sha256") != expected_control_digest:
            problems.append("Agent-start control digest")
        if control and control.get("schema_version") == "2":
            fields.update({"agent_activation_record_sha256s", "pending_agent_ids"})
            actual_digests: list[str] = []
            activated_ids: set[str] = set()
            required_now = {
                item["agent_id"] for item in control.get("planned_agents", [])
                if item.get("activation_stage") == "implementation"
            }
            for path in markdown_files(repository_files(root, mode, lambda *_args: None)):
                activation_text = path.read_text(encoding="utf-8")
                blocks = AGENT_ACTIVATION_BLOCK.findall(activation_text)
                if len(blocks) != 1: continue
                try: raw = json.loads(blocks[0])
                except json.JSONDecodeError: continue
                if not isinstance(raw, dict) or raw.get("run_id") != projection["run_id"]: continue
                parsed_activation = parse_agent_activation_record(root, normalized_relative(path, root), activation_text, control, projection, mode, lambda *_args: None)
                if not parsed_activation: continue
                if parsed_activation["agent_id"] not in required_now:
                    continue
                actual_digests.append(digest(path)); activated_ids.add(parsed_activation["agent_id"])
                if parsed_time:
                    try: clearance_time = datetime.fromisoformat(str(parsed_activation["clearance"]["reviewed_at"]).replace("Z", "+00:00"))
                    except (KeyError, TypeError, ValueError): clearance_time = None
                    if clearance_time is None or clearance_time >= parsed_time: problems.append("Agent-start clearance chronology")
            planned_ids = {item["agent_id"] for item in control.get("planned_agents", [])}
            if not required_now or not required_now.issubset(activated_ids): problems.append("initial implementation activation")
            if len(actual_digests) != len(activated_ids): problems.append("duplicate implementation activation")
            if report.get("agent_activation_record_sha256s") != sorted(actual_digests): problems.append("Agent activation record digests")
            if report.get("pending_agent_ids") != sorted(planned_ids - activated_ids): problems.append("pending Agent identities")
        elif control and parsed_time:
            for item in control.get("briefs", []):
                try:
                    clearance_time = datetime.fromisoformat(str(item["clearance"]["reviewed_at"]).replace("Z", "+00:00"))
                except (KeyError, TypeError, ValueError):
                    clearance_time = None
                if clearance_time is None or clearance_time >= parsed_time:
                    problems.append("Agent-start clearance chronology")
    if not isinstance(report, dict) or set(report) != fields:
        problems.append("report fields")
    expected_results = expected_admission_rule_results(projection)
    if report.get("rule_results") != expected_results:
        problems.append("individual rule results")
    expected_claims = {"contract_admission": "pass", "event_chain_integrity": "not_observed", "semantic_review": "not_observed"}
    if report.get("claims") != expected_claims:
        problems.append("claim limits")
    observed_digest = canonical_json_sha256(report)
    if report_digest and report_digest.group(1) != observed_digest:
        problems.append("report digest")
    if problems:
        add("AHV-ADMISSION-004", "error", relative, f"Admission Report is stale, mismatched, or overclaims: {sorted(set(problems))}", "regenerate the report for the exact Contract, repository, authority, environment, lease, and intended active transition")
        return None
    return observed_digest, report


def parse_single_json_block(pattern: re.Pattern[str], relative: str, text: str, label: str, add) -> dict[str, Any] | None:
    blocks = pattern.findall(text)
    if len(blocks) != 1:
        add("AHV-DOMAIN-001", "error", relative, f"{label} blocks={len(blocks)}", f"retain one exact {label} JSON block")
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-DOMAIN-001", "error", relative, f"{label} JSON is invalid: {error.msg}", f"correct the {label} JSON")
        return None
    if not isinstance(value, dict):
        add("AHV-DOMAIN-001", "error", relative, f"{label} must be a JSON object", f"use one object for {label}")
        return None
    return value


def revision_reference(value: Any) -> tuple[str, int] | None:
    if not isinstance(value, str):
        return None
    match = re.fullmatch(r"([^#]+)#revision-([1-9][0-9]*)", value)
    if not match:
        return None
    try:
        path = safe_relative(match.group(1)).as_posix()
    except ValueError:
        return None
    return path, int(match.group(2))


def domain_free_binding_problems(value: dict[str, Any]) -> list[str]:
    """Check only Domain §12's explicit variant; prose applicability remains reviewed evidence."""
    problems: list[str] = []
    if set(value) != {"schema_version", "contexts", "not_applicable_reason"}:
        problems.append("not_applicable_reason variant fields must be schema_version, contexts, not_applicable_reason")
    if value.get("schema_version") != "1":
        problems.append("not_applicable_reason requires schema_version 1")
    if value.get("contexts") != []:
        problems.append("not_applicable_reason requires contexts to be an empty list")
    if not nonempty_string(value.get("not_applicable_reason")):
        problems.append("not_applicable_reason must be a nonempty string explaining the effective scope/context decision")
    return problems


def validate_domain_artifacts(
    root: Path,
    records: dict[str, tuple[Path, str, bool]],
    add,
) -> None:
    parsed: dict[str, dict[str, Any]] = {}
    for relative, (_path, text, is_template) in records.items():
        if is_template:
            continue
        status = STATUS.search(text)
        if INSTANCE_MARKER.search(text) and status and status.group(1).strip().lower() == "draft":
            continue
        for name, pattern in (
            ("foundation", DOMAIN_FOUNDATION_BLOCK), ("review", DOMAIN_REVIEW_BLOCK),
            ("context", DOMAIN_CONTEXT_BLOCK), ("adoption", BROWNFIELD_ADOPTION_BLOCK),
            ("binding", DOMAIN_BINDING_BLOCK), ("legacy_exception", LEGACY_DOMAIN_EXCEPTION_BLOCK),
        ):
            if pattern.search(text):
                value = parse_single_json_block(pattern, relative, text, name, add)
                if value is not None:
                    parsed[f"{relative}:{name}"] = value

    foundations: dict[str, tuple[str, dict[str, Any]]] = {}
    reviews: dict[str, tuple[str, dict[str, Any]]] = {}
    domain_contexts: dict[str, tuple[str, dict[str, Any]]] = {}
    for key, value in parsed.items():
        relative, kind = key.rsplit(":", 1)
        problems: list[str] = []
        if kind == "foundation":
            fields = {
                "schema_version", "foundation_id", "revision", "revision_status", "effectiveness",
                "horizon", "contexts", "diagram", "open_decisions", "review_ref", "human_decision_ref",
            }
            if set(value) != fields or value.get("schema_version") != "1":
                problems.append("fields/schema")
            foundation_id = value.get("foundation_id")
            revision = value.get("revision")
            if not nonempty_string(foundation_id) or isinstance(revision, bool) or not isinstance(revision, int) or revision < 1:
                problems.append("identity/revision")
            if value.get("revision_status") not in {"draft", "in_review", "approved", "active", "superseded", "withdrawn"}:
                problems.append("revision_status")
            effectiveness = value.get("effectiveness")
            if effectiveness not in {"pending_human_decision", "domain_model_effective", "invalidated"}:
                problems.append("effectiveness")
            horizon = value.get("horizon")
            if not isinstance(horizon, dict) or set(horizon) != {"mvp", "six_week"} or not all(nonempty_string(horizon.get(item)) for item in ("mvp", "six_week")):
                problems.append("horizon")
            contexts = value.get("contexts")
            context_ids: list[str] = []
            if not isinstance(contexts, list) or not contexts:
                problems.append("contexts")
            else:
                for index, context in enumerate(contexts):
                    context_fields = {"id", "name", "coverage", "domain_spec", "logical_module"}
                    if not isinstance(context, dict) or set(context) != context_fields:
                        problems.append(f"contexts[{index}].fields"); continue
                    if not all(nonempty_string(context.get(item)) for item in ("id", "name", "domain_spec", "logical_module")):
                        problems.append(f"contexts[{index}].values"); continue
                    context_ids.append(context["id"])
                    if context.get("coverage") not in DOMAIN_COVERAGE:
                        problems.append(f"contexts[{index}].coverage")
                    try: domain_spec_path = root / safe_relative(context["domain_spec"]).as_posix()
                    except ValueError: problems.append(f"contexts[{index}].domain_spec"); domain_spec_path = None
                    if effectiveness == "domain_model_effective" and (domain_spec_path is None or not domain_spec_path.is_file() or domain_spec_path.is_symlink()):
                        problems.append(f"contexts[{index}].effective Domain Spec")
                if len(context_ids) != len(set(context_ids)):
                    problems.append("duplicate context IDs")
            diagram = value.get("diagram")
            diagram_fields = {"source", "render", "generator", "source_sha256", "render_sha256"}
            if not isinstance(diagram, dict) or set(diagram) != diagram_fields:
                problems.append("diagram.fields")
            elif effectiveness == "domain_model_effective":
                for item in ("source", "render"):
                    try: diagram_path = root / safe_relative(str(diagram.get(item))).as_posix()
                    except ValueError: problems.append(f"diagram.{item}"); continue
                    expected_digest = diagram.get(f"{item}_sha256")
                    if not diagram_path.is_file() or diagram_path.is_symlink() or not HEX64.fullmatch(str(expected_digest or "")) or digest(diagram_path) != expected_digest:
                        problems.append(f"diagram.{item} binding")
            if not isinstance(value.get("open_decisions"), list):
                problems.append("open_decisions")
            if effectiveness == "domain_model_effective":
                if value.get("revision_status") != "active":
                    problems.append("effective Foundation must be active")
                if value.get("review_ref") == "pending" or value.get("human_decision_ref") == "pending":
                    problems.append("effective Foundation lacks review/Human decision")
                if isinstance(contexts, list) and any(context.get("coverage") != "domain_model_effective" for context in contexts if isinstance(context, dict)):
                    problems.append("effective Foundation has uncovered Context")
            if nonempty_string(foundation_id):
                foundations[foundation_id] = (relative, value)
        elif kind == "review":
            problems.extend(domain_review_structure_problems(value))
            review_id = value.get("review_id")
            if not all(nonempty_string(value.get(item)) for item in ("review_id", "foundation_id", "creator")):
                problems.append("identity")
            if isinstance(value.get("foundation_revision"), bool) or not isinstance(value.get("foundation_revision"), int) or value.get("foundation_revision", 0) < 1:
                problems.append("foundation_revision")
            if not HEX64.fullmatch(str(value.get("candidate_sha256", ""))): problems.append("candidate_sha256")
            if not isinstance(value.get("blocking_findings_closed"), bool): problems.append("blocking_findings_closed")
            if value.get("review_outcome") not in {"open", "approved", "changes_requested", "rejected"}: problems.append("review_outcome")
            decision = value.get("human_decision")
            decision_fields = {"outcome", "authority", "decided_at", "overrides"}
            if not isinstance(decision, dict) or set(decision) != decision_fields:
                problems.append("human_decision.fields")
            elif decision.get("outcome") not in {"pending", "approved", "approved_with_overrides", "changes_requested", "paused", "rejected"} or not isinstance(decision.get("overrides"), list):
                problems.append("human_decision.values")
            elif decision.get("outcome") in {"approved", "approved_with_overrides"}:
                if value.get("review_outcome") != "approved" or value.get("blocking_findings_closed") is not True or not nonempty_string(decision.get("authority")) or not nonempty_string(decision.get("decided_at")):
                    problems.append("approved decision prerequisites")
            if nonempty_string(review_id): reviews[review_id] = (relative, value)
        elif kind == "context":
            fields = {
                "schema_version", "context_id", "foundation_id", "foundation_revision", "status",
                "implementation_readiness", "module_entry", "review_ref", "elements",
                "relationship_disposition", "relationships", "invariants", "use_cases",
            }
            if set(value) != fields or value.get("schema_version") != "1": problems.append("fields/schema")
            if not all(nonempty_string(value.get(item)) for item in ("context_id", "foundation_id", "module_entry", "review_ref", "relationship_disposition")):
                problems.append("values")
            if value.get("status") not in {"draft", "approved"}: problems.append("status")
            if isinstance(value.get("foundation_revision"), bool) or not isinstance(value.get("foundation_revision"), int) or value.get("foundation_revision", 0) < 1:
                problems.append("foundation_revision")
            readiness = value.get("implementation_readiness")
            if readiness not in {"modeled", "implementation_ready"}:
                problems.append("implementation_readiness")
            elif readiness == "modeled" and value.get("module_entry") != "not_required":
                problems.append("modeled Context must not require Module Entry")
            elif readiness == "implementation_ready":
                try: module_path = root / safe_relative(str(value.get("module_entry"))).as_posix()
                except ValueError: problems.append("module_entry"); module_path = None
                if module_path is None or not module_path.exists(): problems.append("implementation-ready Context lacks Module Entry")

            elements = value.get("elements")
            element_ids: set[str] = set()
            element_fields = {"id", "kind", "responsibility", "aggregate", "ownership", "tenancy", "lifecycle_authority", "trace_refs"}
            element_kinds = {"aggregate_root", "entity", "value_object", "domain_service", "external_concept"}
            if not isinstance(elements, list) or not elements:
                problems.append("elements")
            else:
                for index, element in enumerate(elements):
                    if (not isinstance(element, dict) or set(element) != element_fields
                            or not all(nonempty_string(element.get(item)) for item in ("id", "responsibility", "aggregate", "ownership", "tenancy", "lifecycle_authority"))
                            or element.get("kind") not in element_kinds or not unique_strings(element.get("trace_refs"))):
                        problems.append(f"elements[{index}]"); continue
                    if element["id"] in element_ids: problems.append("duplicate element IDs")
                    element_ids.add(element["id"])

            relationships = value.get("relationships")
            relation_fields = {"id", "from", "from_cardinality", "semantics", "to", "to_cardinality", "boundary", "trace_refs"}
            cardinalities = {"one", "zero_or_one", "one_or_more", "zero_or_more", "many"}
            relation_ids: set[str] = set()
            if not isinstance(relationships, list):
                problems.append("relationships")
            elif not relationships:
                disposition = value.get("relationship_disposition")
                if not isinstance(disposition, str) or not disposition.startswith("none_with_reason: ") or not disposition.removeprefix("none_with_reason: ").strip():
                    problems.append("empty relationships lack domain reason")
            else:
                if value.get("relationship_disposition") != "modeled": problems.append("relationship_disposition")
                for index, relation in enumerate(relationships):
                    if (not isinstance(relation, dict) or set(relation) != relation_fields
                            or not all(nonempty_string(relation.get(item)) for item in ("id", "from", "semantics", "to", "boundary"))
                            or relation.get("from_cardinality") not in cardinalities or relation.get("to_cardinality") not in cardinalities
                            or not unique_strings(relation.get("trace_refs"))):
                        problems.append(f"relationships[{index}]"); continue
                    if relation["id"] in relation_ids: problems.append("duplicate relationship IDs")
                    if relation["from"] not in element_ids or relation["to"] not in element_ids: problems.append(f"relationships[{index}].element refs")
                    relation_ids.add(relation["id"])

            invariants = value.get("invariants")
            invariant_fields = {"id", "rule", "failure_or_denial", "trace_refs"}
            if (not isinstance(invariants, list) or not invariants
                    or any(not isinstance(item, dict) or set(item) != invariant_fields
                           or not all(nonempty_string(item.get(field)) for field in ("id", "rule", "failure_or_denial"))
                           or not unique_strings(item.get("trace_refs")) for item in invariants)):
                problems.append("invariants")

            use_cases = value.get("use_cases")
            use_case_fields = {"id", "actor_or_role", "permission_boundary", "preconditions", "success", "failure_or_denial", "first_class_disposition", "trace_refs"}
            if (not isinstance(use_cases, list) or not use_cases
                    or any(not isinstance(item, dict) or set(item) != use_case_fields
                           or not all(nonempty_string(item.get(field)) for field in use_case_fields - {"trace_refs"})
                           or not unique_strings(item.get("trace_refs")) for item in use_cases)):
                problems.append("use_cases")
            context_id = value.get("context_id")
            if nonempty_string(context_id):
                if context_id in domain_contexts: problems.append("duplicate Context model")
                else: domain_contexts[context_id] = (relative, value)
        elif kind == "adoption":
            fields = {"schema_version", "adoption_id", "harness_version", "activation", "root_routing_authority", "entry_chain_evidence", "contexts", "no_overwrite_evidence", "rollback_evidence"}
            if set(value) != fields or value.get("schema_version") != "1" or not SEMVER.fullmatch(str(value.get("harness_version", ""))): problems.append("fields/schema/version")
            if not nonempty_string(value.get("adoption_id")) or value.get("activation") not in {"inactive_staged", "active"}: problems.append("identity/activation")
            contexts = value.get("contexts")
            context_ids: list[str] = []
            if not isinstance(contexts, list) or not contexts: problems.append("contexts")
            else:
                for index, context in enumerate(contexts):
                    if not isinstance(context, dict) or set(context) != {"id", "coverage", "foundation_or_exception"} or not nonempty_string(context.get("id")) or context.get("coverage") not in DOMAIN_COVERAGE or not nonempty_string(context.get("foundation_or_exception")):
                        problems.append(f"contexts[{index}]"); continue
                    context_ids.append(context["id"])
                    if context.get("coverage") == "domain_model_effective" and context.get("foundation_or_exception") == "none":
                        problems.append(f"contexts[{index}].effective reference")
                if len(context_ids) != len(set(context_ids)): problems.append("duplicate context IDs")
            if value.get("activation") == "active" and (value.get("root_routing_authority") == "pending" or value.get("entry_chain_evidence") == "pending"):
                problems.append("active adoption lacks routing authority/evidence")
            if not nonempty_string(value.get("no_overwrite_evidence")) or not nonempty_string(value.get("rollback_evidence")):
                problems.append("transaction evidence")
        elif kind == "legacy_exception":
            problems.extend(legacy_domain_exception_problems(value))
        elif kind == "binding":
            if "not_applicable_reason" in value:
                for problem in domain_free_binding_problems(value):
                    add("AHV-DOMAIN-005", "error", relative, problem, "correct only the named Domain Binding field")
                continue
            if set(value) != {"schema_version", "contexts"} or value.get("schema_version") != "1": problems.append("fields/schema")
            contexts = value.get("contexts")
            ids: list[str] = []
            if not isinstance(contexts, list) or not contexts: problems.append("contexts")
            else:
                for index, context in enumerate(contexts):
                    if not isinstance(context, dict) or set(context) != {"id", "foundation_ref", "legacy_exception_ref"} or not nonempty_string(context.get("id")):
                        problems.append(f"contexts[{index}].fields"); continue
                    ids.append(context["id"])
                    foundation_ref = context.get("foundation_ref")
                    legacy_ref = context.get("legacy_exception_ref")
                    if (foundation_ref == "none") == (legacy_ref == "none"):
                        problems.append(f"contexts[{index}] must bind exactly one source")
                    elif foundation_ref != "none" and revision_reference(foundation_ref) is None:
                        problems.append(f"contexts[{index}].foundation_ref")
                    elif legacy_ref != "none":
                        try: safe_relative(str(legacy_ref))
                        except ValueError: problems.append(f"contexts[{index}].legacy_exception_ref")
                if len(ids) != len(set(ids)): problems.append("duplicate context IDs")
        for problem in problems:
            add(f"AHV-DOMAIN-{ {'foundation':'001','review':'002','context':'003','adoption':'004','binding':'005','legacy_exception':'005'}[kind] }", "error", relative, problem, "correct only the named Domain artifact field or exact reference")

    for review_id, (relative, review) in reviews.items():
        foundation = foundations.get(str(review.get("foundation_id")))
        if foundation and foundation[1].get("revision") != review.get("foundation_revision"):
            add("AHV-DOMAIN-002", "error", relative, "review Foundation revision mismatch", "bind the exact reviewed Foundation revision")
    for foundation_id, (relative, foundation) in foundations.items():
        if foundation.get("effectiveness") != "domain_model_effective":
            continue
        review = reviews.get(str(foundation.get("review_ref")))
        valid = bool(
            review
            and not domain_review_approval_problems(root, relative, foundation, review[1])
        )
        if not valid:
            add("AHV-DOMAIN-001", "error", relative, "effective Foundation lacks its exact approved Review/Human Decision", "bind the version-appropriate independent Review and exact Human decision for this revision")
        for context in foundation.get("contexts", []):
            if not isinstance(context, dict):
                continue
            context_id = context.get("id")
            domain_context = domain_contexts.get(str(context_id))
            expected_path = context.get("domain_spec")
            if not domain_context or domain_context[0] != expected_path:
                add("AHV-DOMAIN-003", "error", relative, f"effective Context {context_id!r} lacks its exact structured Domain Spec", "bind the named Domain Spec path and one complete domain-context block")
                continue
            model = domain_context[1]
            if (model.get("foundation_id") != foundation_id or model.get("foundation_revision") != foundation.get("revision")
                    or model.get("status") != "approved"):
                add("AHV-DOMAIN-003", "error", domain_context[0], f"Context {context_id!r} does not bind the active Foundation revision", "approve the exact Context model under this Foundation revision")


def direct_run_version(text: str) -> str | None:
    blocks = DIRECT_RUN_BLOCK.findall(text)
    if len(blocks) != 1:
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError:
        return None
    version = value.get("harness_version") if isinstance(value, dict) else None
    return version if isinstance(version, str) and SEMVER.fullmatch(version) else None


def uses_lease_free_contract(version: str) -> bool:
    # Withdrawn2.0.0 was the original1.5.0 release, not a later contract generation.
    return SEMVER.fullmatch(version) is not None and version != "2.0.0" and semver_tuple(version) >= LEASE_FREE_MIN_VERSION


def task_control_problems(
    text: str, contract: dict[str, Any], target_documents: dict[str, str] | None = None,
    identifier: str | None = None, start_recovered: bool = False,
) -> list[str]:
    """Check current declarations, not timing, semantic truth or runtime tool authority."""
    blocks = TASK_CONTROLS_BLOCK.findall(text)
    if len(blocks) != 1 or text.count("<!-- task-controls:start -->") != 1 or text.count("<!-- task-controls:end -->") != 1:
        return ["task-controls requires exactly one complete JSON evidence block"]

    def distinct_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    try:
        control = json.loads(blocks[0], object_pairs_hook=distinct_keys)
    except ValueError as error:
        return [f"task-controls JSON is invalid: {error}"]
    fields = {"checked_revision", "progress", "updates", "drift_checks", "obligations"}
    if not isinstance(control, dict) or set(control) != fields:
        return ["task-controls fields differ from the compact evidence schema"]

    problems: list[str] = []
    revision = control["checked_revision"]
    if type(revision) is not int or revision < 1 or revision != contract["revision"]:
        problems.append("task-controls.checked_revision must equal the positive current Run revision")
    progress = control["progress"]
    if type(progress) is not int or not 0 <= progress <= 100:
        problems.append("task-controls.progress must be an integer from 0 to 100")
        progress = None

    def origin_assignment(entry: dict[str, Any]) -> dict[str, Any]:
        """Resolve a carried observation from an already named source, without recursive admission."""
        reference = entry["origin_run"]
        if (not isinstance(reference, dict) or set(reference) != {"id", "revision"}
                or not nonempty_string(reference["id"]) or reference["id"] == identifier
                or type(reference["revision"]) is not int or reference["revision"] < 1):
            raise ValueError("origin_run requires another exact Run ID and positive revision")
        sources = [source for source in (target_documents or {}).values()
                   if (match := ARTIFACT_ID.search(source)) and match.group(1) == reference["id"]]
        if len(sources) != 1:
            raise ValueError("origin_run must resolve to one already named target")
        source = sources[0]
        source_class = ARTIFACT_CLASS.search(source)
        source_blocks = DIRECT_RUN_BLOCK.findall(source)
        if (not source_class or source_class.group(1).strip().strip("`") != "Work contract"
                or len(source_blocks) != 1 or source.count("<!-- run-contract:start -->") != 1
                or source.count("<!-- run-contract:end -->") != 1):
            raise ValueError("origin_run is not one direct Work contract")
        original = json.loads(source_blocks[0], object_pairs_hook=distinct_keys)
        if (not isinstance(original, dict) or set(original) != set(contract) or original.get("schema_version") != "1"
                or type(original.get("revision")) is not int or original["revision"] != reference["revision"]):
            raise ValueError("origin_run revision/schema is invalid or stale")
        version = original.get("harness_version")
        if not isinstance(version, str) or not SEMVER.fullmatch(version) or semver_tuple(version) < DIRECT_RUN_MIN_VERSION:
            raise ValueError("origin_run requires a pinned direct Run version")
        assignment, clearance = original.get("decision"), original.get("agent_start")
        if (not isinstance(original.get("decision_class"), str) or original["decision_class"] not in EFFORT_PROFILES
                or not isinstance(assignment, dict) or not isinstance(clearance, dict)
                or not all(nonempty_string(assignment.get(key)) for key in ("authority", "approval_ref", "lead"))
                or not unique_strings(assignment.get("agents"))
                or not unique_strings(assignment.get("reviewers"), allow_empty=True)
                or assignment["lead"] not in assignment["agents"]
                or not set(assignment["reviewers"]).issubset(assignment["agents"])):
            raise ValueError("origin_run assignment is invalid")
        if original["decision_class"] == "D0":
            if (assignment["agents"] != [assignment["lead"]] or assignment["reviewers"] != []
                    or clearance != {"applicability": "not_applicable_d0", "spawn_reviewer": "not_applicable",
                                     "clearance": "not_applicable", "cleared_agents": []}):
                raise ValueError("origin_run D0 assignment/clearance is invalid")
        elif (clearance.get("applicability") != "required" or clearance.get("clearance") != "pass"
                or not nonempty_string(clearance.get("spawn_reviewer")) or clearance["spawn_reviewer"] == "not_applicable"
                or not unique_strings(clearance.get("cleared_agents"))
                or assignment["lead"] not in clearance["cleared_agents"]):
            raise ValueError("origin_run assignment lacks Agent-start clearance")
        if semver_tuple(version) >= TASK_CONTROLS_MIN_VERSION:
            observations = TASK_CONTROLS_BLOCK.findall(source)
            if (len(observations) != 1 or source.count("<!-- task-controls:start -->") != 1
                    or source.count("<!-- task-controls:end -->") != 1):
                raise ValueError("origin_run lacks one original task-controls block")
            observation = json.loads(observations[0], object_pairs_hook=distinct_keys)
            core = {key: entry[key] for key in ("percent", "reviewer", "decision", "evidence")}
            if (not isinstance(observation, dict) or set(observation) != fields or type(observation.get("checked_revision")) is not int
                    or observation["checked_revision"] != original["revision"]
                    or type(observation.get("progress")) is not int or type(entry["percent"]) is not int
                    or not entry["percent"] <= observation["progress"] <= 100
                    or not isinstance(observation.get("drift_checks"), list)):
                raise ValueError("origin_run observation binding is invalid")
            matches = [item for item in observation["drift_checks"]
                       if isinstance(item, dict) and item.get("percent") == entry["percent"]]
            if len(matches) != 1 or type(matches[0].get("percent")) is not int or matches[0] != core:
                raise ValueError("origin_run must contain the exact non-carried original observation")
        return original

    decision = contract.get("decision")
    decision = decision if isinstance(decision, dict) else {}
    lead = decision.get("lead")
    reviewers = decision.get("reviewers")
    reviewers = reviewers if unique_strings(reviewers, allow_empty=True) else []
    start = contract.get("agent_start")
    start = start if isinstance(start, dict) else {}
    cleared = start.get("cleared_agents")
    cleared = cleared if unique_strings(cleared, allow_empty=True) else []
    # A verified terminal disposition covers missing clearance, not missing participation
    # or independence. Never write these validation-only identities into the old contract.
    if start_recovered:
        cleared = decision.get("agents", [])
    is_d0 = contract.get("decision_class") == "D0"
    if contract["status"] == "completed" and not is_d0:
        agents = decision.get("agents")
        if not unique_strings(agents) or not set(agents).issubset(cleared):
            problems.append("completed Run lacks clearance for every claimed participating Agent")

    for field, step in (("updates", 10), ("drift_checks", 20)):
        entries = control[field]
        if not isinstance(entries, list):
            problems.append(f"task-controls.{field} must be a list")
            continue
        percentages = []
        for index, entry in enumerate(entries):
            required = {"percent", "evidence"} if step == 10 else {"percent", "evidence", "reviewer", "decision"}
            label = f"task-controls.{field}[{index}]"
            if not isinstance(entry, dict) or (set(entry) != required and not (step == 20 and set(entry) == required | {"origin_run"})):
                problems.append(f"{label} fields are invalid")
                continue
            percent = entry["percent"]
            if type(percent) is not int or percent not in range(step, 101, step):
                problems.append(f"{label}.percent is invalid")
            else:
                percentages.append(percent)
            if not nonempty_string(entry["evidence"]):
                problems.append(f"{label}.evidence must name actual evidence or explicit missed-duty resolution")
            if step == 20:
                if not isinstance(entry["decision"], str) or entry["decision"] not in DRIFT_DECISIONS:
                    problems.append(f"{label}.decision is invalid")
                reviewer = entry["reviewer"]
                check_lead, check_reviewers, check_cleared, check_start, check_d0 = lead, reviewers, cleared, start, is_d0
                if "origin_run" in entry:
                    try:
                        original = origin_assignment(entry)
                    except ValueError as error:
                        problems.append(f"{label}: {error}")
                        continue
                    check_lead = original["decision"]["lead"]
                    check_reviewers = original["decision"]["reviewers"]
                    check_start = original["agent_start"]
                    check_cleared = check_start["cleared_agents"]
                    check_d0 = original["decision_class"] == "D0"
                if type(percent) is int and percent in (40, 80):
                    valid = reviewer == "not_applicable_d0" if check_d0 else (
                        nonempty_string(reviewer) and reviewer in check_reviewers and reviewer in check_cleared
                        and reviewer != check_lead and reviewer != check_start.get("spawn_reviewer")
                    )
                else:
                    valid = nonempty_string(reviewer) and reviewer == check_lead
                if not valid:
                    problems.append(f"{label}.reviewer must be the Lead, or a cleared assigned non-author at 40/80 (D0: not_applicable_d0)")
        if progress is not None and percentages != list(range(step, progress + 1, step)):
            problems.append(f"task-controls.{field} must retain the complete ordered {step}-percent prefix through progress")

    obligations = control["obligations"]
    lease_free = uses_lease_free_contract(contract["harness_version"])
    obligation_keys = (TASK_OBLIGATIONS - {"capability_lease"}) | {"capability"} if lease_free else TASK_OBLIGATIONS
    conditional_keys = (TASK_CONDITIONAL_OBLIGATIONS - {"capability_lease"}) | {"capability"} if lease_free else TASK_CONDITIONAL_OBLIGATIONS
    if not isinstance(obligations, dict) or set(obligations) != obligation_keys:
        problems.append("task-controls.obligations must cover exactly all eight canonical duty families")
    else:
        for name, entry in obligations.items():
            label = f"task-controls.obligations.{name}"
            if not isinstance(entry, dict) or set(entry) != {"state", "evidence"}:
                problems.append(f"{label} requires state and evidence")
                continue
            state = entry["state"]
            if not isinstance(state, str) or state not in {"satisfied", "not_applicable", "blocked"}:
                problems.append(f"{label}.state is invalid")
            if state == "not_applicable" and name not in conditional_keys:
                problems.append(f"{label} is always due; preparation is not an exemption")
            if state == "blocked" and contract["status"] not in ("blocked", "cancelled"):
                problems.append(f"{label} is blocked; stop affected continuation before admission or completion")
            if not nonempty_string(entry["evidence"]):
                problems.append(f"{label}.evidence must bind the current action, trigger and observation/reason")
    return problems


START_RECOVERY_BLOCK = re.compile(r"<!-- agent-start-recovery:start -->\s*```json\s*(\{.*?\})\s*```\s*<!-- agent-start-recovery:end -->", re.DOTALL)


def start_recovery_problems(root: Path, relative: str, text: str, contract: dict[str, Any], identifier: str | None) -> list[str] | None:
    """None means absent; [] means a structurally valid historical disposition, not a start pass."""
    if "<!-- agent-start-recovery:" not in text:
        return None
    blocks = START_RECOVERY_BLOCK.findall(text)
    if len(blocks) != 1 or text.count("<!-- agent-start-recovery:start -->") != 1 or text.count("<!-- agent-start-recovery:end -->") != 1:
        return ["start recovery requires exactly one complete block"]

    def distinct_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key}")
            result[key] = value
        return result

    try:
        recovery = json.loads(blocks[0], object_pairs_hook=distinct_keys)
    except ValueError as error:
        return [f"start recovery JSON is invalid: {error}"]
    fields = {"schema_version", "run_id", "run_revision", "contract_sha256", "reviewer", "reviewed_at", "assessment", "evidence", "unresolved_findings", "human_decision"}
    if not isinstance(recovery, dict) or set(recovery) != fields:
        return ["start recovery fields differ from the disposition schema"]
    problems = []
    start = contract.get("agent_start")
    decision = contract.get("decision")
    if not isinstance(start, dict) or not isinstance(decision, dict):
        return ["start recovery requires the original start and decision objects"]
    if contract.get("status") != "completed" or start.get("applicability") != "required" or start.get("clearance") != "not_applicable":
        problems.append("start recovery is only for completed Runs with an honestly missing start pass")
    if recovery["schema_version"] != "1" or recovery["run_id"] != identifier or type(recovery["run_revision"]) is not int or recovery["run_revision"] < 1 or recovery["run_revision"] != contract.get("revision"):
        problems.append("start recovery subject/revision is invalid")
    bound = hashlib.sha256(json.dumps(contract, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if recovery["contract_sha256"] != bound:
        problems.append("start recovery contract binding is stale")
    reviewer = recovery["reviewer"]
    reviewers = decision.get("reviewers")
    if not nonempty_string(reviewer) or not isinstance(reviewers, list) or reviewer not in reviewers or reviewer in (decision.get("lead"), start.get("spawn_reviewer")):
        problems.append("start recovery requires an assigned independent non-author reviewer")
    try:
        stamp = recovery["reviewed_at"]
        if not isinstance(stamp, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", stamp):
            raise ValueError("not UTC ISO8601")
        if datetime.fromisoformat(stamp.replace("Z", "+00:00")) > datetime.now(timezone.utc):
            raise ValueError("future review")
    except ValueError:
        problems.append("start recovery review timestamp is invalid or future")
    if not nonempty_string(recovery["assessment"]) or recovery["unresolved_findings"] != []:
        problems.append("start recovery needs actual assessment and no unresolved findings")
    human = recovery["human_decision"]
    if not isinstance(human, dict) or set(human) != {"authority", "approval_ref", "accepted_risk"} or human.get("authority") != decision.get("authority") or not isinstance(human.get("approval_ref"), str) or not re.fullmatch(r"human-approved:[A-Za-z0-9._-]+", human["approval_ref"]) or not nonempty_string(human.get("accepted_risk")):
        problems.append("start recovery lacks exact Human risk disposition")
    evidence = recovery["evidence"]
    if not isinstance(evidence, list) or not evidence:
        problems.append("start recovery needs exact reviewed evidence")
    else:
        seen = set()
        for item in evidence:
            try:
                if not isinstance(item, dict) or set(item) != {"path", "sha256"} or not isinstance(item["path"], str):
                    raise ValueError("invalid evidence fields")
                path = safe_relative(item["path"])
                if path.as_posix() == relative or path in seen:
                    raise ValueError("self or duplicate evidence")
                seen.add(path)
                if any((root.joinpath(*path.parts[:i])).is_symlink() for i in range(1, len(path.parts) + 1)) or not (root / path).is_file():
                    raise ValueError("missing or symlink evidence")
                if item["sha256"] != digest(root / path):
                    raise ValueError("changed evidence")
            except (OSError, ValueError) as error:
                problems.append(f"start recovery evidence is invalid: {error}")
    return problems


def working_team_problems(contract: dict[str, Any]) -> list[str]:
    """1.4.0+ ordinary topology: two workers, distinct Spawn, one bounded escalation."""
    decision, start = contract.get("decision"), contract.get("agent_start")
    if not isinstance(decision, dict) or not isinstance(start, dict):
        return []  # The common schema checks report malformed blocks.
    agents, reviewers = decision.get("agents"), decision.get("reviewers")
    lead, spawn = decision.get("lead"), start.get("spawn_reviewer")
    if (not unique_strings(agents) or not unique_strings(reviewers, allow_empty=True)
            or not nonempty_string(lead) or not nonempty_string(spawn)):
        return []  # Avoid set operations before common field/type validation.
    problems: list[str] = []
    escalation = decision.get("review_escalation")
    version = contract.get("harness_version", "")
    proportionate = bool(isinstance(version, str) and SEMVER.fullmatch(version)
                         and semver_tuple(version) >= PROPORTIONATE_EXECUTION_MIN_VERSION)
    if contract.get("decision_class") == "D0":
        if proportionate:
            return ["1.5 D0 routine needs task, diff and focused evidence, not a Run Contract"]
        if (agents != [lead] or reviewers or decision.get("max_corrections") != 0
                or "review_escalation" in decision or start.get("applicability") != "not_applicable_d0"):
            problems.append("D0 requires one Lead, no reviewer/escalation, zero corrections and N/A start")
        return problems
    if start.get("applicability") != "required" or lead == spawn or lead in reviewers or spawn in reviewers:
        problems.append("working reviewers, Creator/Lead and start-only Spawn must be distinct")
    if set(agents) != {lead, spawn, *reviewers}:
        problems.append("decision.agents must allocate exactly Lead, working reviewers and separate Spawn")
    cleared = start.get("cleared_agents")
    if unique_strings(cleared, allow_empty=True) and not set(cleared).issubset(agents):
        problems.append("agent_start.cleared_agents contains an unallocated Agent")
    if "review_escalation" not in decision:
        if len(reviewers) != 1:
            problems.append("default team requires one independent working reviewer; extra reviewer needs bounded review_escalation")
    else:
        fields = {"trigger", "question", "reviewer", "max_reviews"}
        if (not isinstance(escalation, dict) or set(escalation) != fields
                or not isinstance(escalation.get("trigger"), str)
                or escalation["trigger"] not in {"critical_competence_gap", "unresolved_material_dissent"}
                or not nonempty_string(escalation.get("question"))
                or not nonempty_string(escalation.get("reviewer"))
                or escalation["reviewer"] not in reviewers
                or len(reviewers) != 2
                or type(escalation.get("max_reviews")) is not int or escalation["max_reviews"] != 1
                or not re.fullmatch(r"human-approved:[A-Za-z0-9._-]+", str(decision.get("effort_override", "")))):
            problems.append("review_escalation requires one additional independent reviewer, concrete trigger/question, one review and exact Human allocation")
    corrections = decision.get("max_corrections")
    ceiling = 3 if proportionate else 1
    if type(corrections) is int and corrections > ceiling and decision.get("effort_override") == "none":
        problems.append(f"correction limit exceeds {ceiling} without exact Human amendment")
    return problems


def validate_direct_run_contract(
    root: Path,
    relative: str,
    text: str,
    identifier: str | None,
    mode: str,
    add,
) -> dict[str, Any] | None:
    """Validate one 1.2.7+ Run and only the exact target files it names."""
    blocks = DIRECT_RUN_BLOCK.findall(text)
    if len(blocks) != 1:
        add("AHV-RUN-CHECK-001", "error", relative, f"direct Run Contract blocks={len(blocks)}", "retain one run-contract JSON block in this Contract")
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-RUN-CHECK-001", "error", relative, f"Run Contract JSON is invalid: {error.msg}", "correct this Contract's JSON")
        return None
    required = {
        "schema_version", "revision", "status", "harness_version", "run_kind",
        "decision_class", "targets", "outcome", "allowed_paths", "non_goals",
        "decision", "external_actions", "completion_evidence", "agent_start",
    }
    problems: list[str] = []
    if not isinstance(value, dict) or set(value) != required:
        add("AHV-RUN-CHECK-001", "error", relative, "Run Contract fields differ from the compact schema", "use exactly the released execution-run template fields")
        return None
    if value.get("schema_version") != "1":
        problems.append("schema_version must be 1")
    if not identifier or not re.fullmatch(r"[A-Z0-9][A-Z0-9._-]+", identifier):
        problems.append("Artifact ID is missing or invalid")
    artifact_class = ARTIFACT_CLASS.search(text)
    if not artifact_class or artifact_class.group(1).strip().strip("`") != "Work contract":
        problems.append("Artifact class must be Work contract")
    if isinstance(value.get("revision"), bool) or not isinstance(value.get("revision"), int) or value["revision"] < 1:
        problems.append("revision must be a positive integer")
    if value.get("status") not in DIRECT_RUN_STATUSES:
        problems.append("status must be approved, active, verification, blocked, completed, or cancelled")
    version = value.get("harness_version")
    current_team = bool(isinstance(version, str) and SEMVER.fullmatch(version)
                        and semver_tuple(version) >= LEAN_WORKING_TEAM_MIN_VERSION)
    if not isinstance(version, str) or not SEMVER.fullmatch(version) or semver_tuple(version) < DIRECT_RUN_MIN_VERSION:
        problems.append("harness_version must be 1.2.7 or newer")
    if value.get("run_kind") not in {"product_delivery", "technical_risk_experiment", "domain_foundation", "bootstrap_initialization", "governance"}:
        problems.append("run_kind is invalid")
    decision_class = value.get("decision_class")
    if decision_class not in EFFORT_PROFILES:
        problems.append("decision_class is invalid")
    if value.get("run_kind") in {"domain_foundation", "bootstrap_initialization"} and decision_class != "D3":
        problems.append(f"{value.get('run_kind')} must use D3")

    targets = value.get("targets")
    target_documents: dict[str, str] = {}
    if not isinstance(targets, list) or not targets:
        problems.append("targets must name at least one exact source")
    else:
        seen_ids: set[str] = set()
        seen_paths: set[str] = set()
        for index, target in enumerate(targets):
            if not isinstance(target, dict) or set(target) != {"id", "path"} or not nonempty_string(target.get("id")) or not nonempty_string(target.get("path")):
                problems.append(f"targets[{index}] must contain exact id and path")
                continue
            target_id, target_relative = target["id"], target["path"]
            if target_id in seen_ids or target_relative in seen_paths:
                problems.append(f"targets[{index}] duplicates an id or path")
                continue
            seen_ids.add(target_id); seen_paths.add(target_relative)
            try:
                safe_relative(target_relative)
            except ValueError:
                problems.append(f"targets[{index}].path is unsafe")
                continue
            target_path = root / target_relative
            if not target_path.is_file() or target_path.is_symlink():
                problems.append(f"target {target_id} is missing at {target_relative}")
                continue
            try:
                target_text = target_path.read_text(encoding="utf-8")
            except UnicodeError:
                problems.append(f"target {target_id} is not UTF-8 Markdown")
                continue
            target_documents[target_relative] = target_text
            observed_id = ARTIFACT_ID.search(target_text)
            if not observed_id or observed_id.group(1) != target_id:
                problems.append(f"target {target_relative} does not declare {target_id}")

    if isinstance(version, str) and SEMVER.fullmatch(version) and semver_tuple(version) >= DOMAIN_FOUNDATION_MIN_VERSION:
        run_kind = value.get("run_kind")
        target_paths = set(target_documents)

        def target_blocks(pattern: re.Pattern[str], label: str) -> list[tuple[str, dict[str, Any]]]:
            result: list[tuple[str, dict[str, Any]]] = []
            for target_relative, target_text in target_documents.items():
                blocks = pattern.findall(target_text)
                if len(blocks) > 1:
                    problems.append(f"target {target_relative} has multiple {label} blocks")
                for block in blocks:
                    try: parsed = json.loads(block)
                    except json.JSONDecodeError:
                        problems.append(f"target {target_relative} has invalid {label} JSON"); continue
                    if not isinstance(parsed, dict):
                        problems.append(f"target {target_relative} has non-object {label} JSON"); continue
                    result.append((target_relative, parsed))
            return result

        foundations = target_blocks(DOMAIN_FOUNDATION_BLOCK, "Domain Foundation")
        reviews = target_blocks(DOMAIN_REVIEW_BLOCK, "Domain Review")

        def targeted_approval_problems(
            foundation_path: str,
            foundation: dict[str, Any],
        ) -> list[str]:
            matches = [
                review for _review_path, review in reviews
                if review.get("review_id") == foundation.get("review_ref")
            ]
            if len(matches) != 1:
                return ["exact approved Human Domain Review is not an exact Run target"]
            return domain_review_approval_problems(root, foundation_path, foundation, matches[0])

        if run_kind == "domain_foundation":
            if foundations or reviews:
                problems.append("domain_foundation targets must be pre-existing authority/input, not its future Foundation or Review outputs")
            bootstrap_inputs = [
                target_text for target_text in target_documents.values()
                if re.search(r"^> Bootstrap lifecycle state:\s*`?(?:intake_ready|modeling_domain)`?\s*$", target_text, re.MULTILINE)
                and re.search(r"^- Human initialization instruction:\s*(?!`?(?:not_available|pending)`?\s*$)\S.+$", target_text, re.MULTILINE)
                and re.search(r"^- PRD(?: and optional-input safe snapshot/digests|/input snapshot digests):.*\b[0-9a-f]{64}\b", target_text, re.MULTILINE)
            ]
            if len(bootstrap_inputs) != 1:
                problems.append("domain_foundation must target one active Bootstrap State with exact Human instruction and safe input digest")
        elif run_kind == "bootstrap_initialization":
            effective = [
                item for item in foundations
                if item[1].get("effectiveness") == "domain_model_effective"
                and item[1].get("revision_status") == "active"
            ]
            if len(effective) != 1 or len(reviews) != 1:
                problems.append("bootstrap_initialization must target one effective Foundation and its approved Human Domain Review")
            elif targeted_approval_problems(effective[0][0], effective[0][1]):
                problems.append("bootstrap_initialization Domain Review does not bind the exact targeted Foundation bytes and Human Decision")
        elif run_kind == "product_delivery":
            bindings = target_blocks(DOMAIN_BINDING_BLOCK, "Domain Binding")
            if not bindings:
                problems.append("product_delivery must target a Work Package with a Domain Binding")
            for binding_path, binding in bindings:
                if semver_tuple(version) >= DOMAIN_FREE_DELIVERY_MIN_VERSION and "not_applicable_reason" in binding:
                    problems.extend(f"target {binding_path}: {problem}" for problem in domain_free_binding_problems(binding))
                    continue
                contexts = binding.get("contexts")
                if binding.get("schema_version") != "1" or not isinstance(contexts, list) or not contexts:
                    problems.append(f"target {binding_path} has an invalid Domain Binding")
                    continue
                for context in contexts:
                    if not isinstance(context, dict):
                        problems.append(f"target {binding_path} has an invalid Context binding"); continue
                    context_id = context.get("id")
                    foundation_ref = context.get("foundation_ref")
                    exception_ref = context.get("legacy_exception_ref")
                    if foundation_ref != "none":
                        parsed_ref = revision_reference(foundation_ref)
                        if parsed_ref is None:
                            problems.append(f"Context {context_id} has an invalid Foundation reference"); continue
                        foundation_path, foundation_revision = parsed_ref
                        if foundation_path not in target_paths:
                            problems.append(f"Context {context_id} Foundation is not an exact Run target"); continue
                        candidate = next((item for path, item in foundations if path == foundation_path), None)
                        covered = candidate.get("contexts", []) if isinstance(candidate, dict) else []
                        if (
                            candidate is None
                            or candidate.get("revision") != foundation_revision
                            or candidate.get("revision_status") != "active"
                            or candidate.get("effectiveness") != "domain_model_effective"
                            or not any(
                                isinstance(item, dict) and item.get("id") == context_id
                                and item.get("coverage") == "domain_model_effective"
                                for item in covered
                            )
                        ):
                            problems.append(f"Context {context_id} lacks the targeted effective Foundation revision")
                        elif targeted_approval_problems(foundation_path, candidate):
                            problems.append(f"Context {context_id} lacks the exact approved Human Domain Review for the targeted Foundation bytes")
                    elif exception_ref != "none":
                        try: exception_path = safe_relative(str(exception_ref)).as_posix()
                        except ValueError:
                            problems.append(f"Context {context_id} has an invalid Legacy Exception reference"); continue
                        if exception_path not in target_paths:
                            problems.append(f"Context {context_id} Legacy Exception is not an exact Run target"); continue
                        exception_blocks = LEGACY_DOMAIN_EXCEPTION_BLOCK.findall(target_documents[exception_path])
                        try: exception = json.loads(exception_blocks[0]) if len(exception_blocks) == 1 else None
                        except json.JSONDecodeError: exception = None
                        exception_problems = legacy_domain_exception_problems(exception) if isinstance(exception, dict) else ["invalid block"]
                        affected_runs = exception.get("affected_runs") if isinstance(exception, dict) else None
                        if (
                            not isinstance(exception, dict)
                            or exception.get("context_id") != context_id
                            or not isinstance(affected_runs, list)
                            or identifier not in affected_runs
                            or exception_problems
                        ):
                            problems.append(f"Context {context_id} lacks an exact approved Legacy Exception")
                    else:
                        problems.append(f"Context {context_id} has no Foundation or Legacy Exception binding")

    if not nonempty_string(value.get("outcome")):
        problems.append("outcome is missing")
    if not unique_strings(value.get("allowed_paths")):
        problems.append("allowed_paths must be a non-empty unique list")
    else:
        for allowed in value["allowed_paths"]:
            try:
                safe_relative(allowed)
            except ValueError:
                problems.append(f"allowed_paths contains unsafe path {allowed!r}")
    if not unique_strings(value.get("non_goals")):
        problems.append("non_goals must be a non-empty unique list")

    decision = value.get("decision")
    decision_fields = {"authority", "approval_ref", "lead", "reasoning", "agents", "reviewers", "max_corrections", "effort_override"}
    valid_decision_fields = (decision_fields, decision_fields | {"review_escalation"}) if current_team else (decision_fields,)
    if not isinstance(decision, dict) or set(decision) not in valid_decision_fields:
        problems.append("decision fields are incomplete")
        decision = {}
    else:
        for field in ("authority", "approval_ref", "lead"):
            if not nonempty_string(decision.get(field)):
                problems.append(f"decision.{field} is missing")
        if decision.get("reasoning") not in {"high", "xhigh", "max", "ultra"}:
            problems.append("decision.reasoning is below high or invalid")
        if not unique_strings(decision.get("agents")):
            problems.append("decision.agents must be a non-empty unique list")
        if not unique_strings(decision.get("reviewers"), allow_empty=True):
            problems.append("decision.reviewers must be a unique list")
        elif isinstance(decision.get("agents"), list) and not set(decision["reviewers"]).issubset(set(decision["agents"])):
            problems.append("decision.reviewers must be listed Agents")
        if isinstance(decision.get("max_corrections"), bool) or not isinstance(decision.get("max_corrections"), int) or decision["max_corrections"] < 0:
            problems.append("decision.max_corrections must be a non-negative integer")
        effort_override = decision.get("effort_override")
        if effort_override != "none" and (not isinstance(effort_override, str) or re.fullmatch(r"human-approved:[A-Za-z0-9._-]+", effort_override) is None):
            problems.append("decision.effort_override must be none or an exact human-approved reference")
    if current_team:
        problems.extend(working_team_problems(value))
    elif decision_class in EFFORT_PROFILES and decision:
        profile = EFFORT_PROFILES[decision_class]
        profile_matches = bool(
            isinstance(decision.get("agents"), list)
            and len(decision["agents"]) == profile["implementers"] + profile["reviewers"]
            and isinstance(decision.get("reviewers"), list)
            and len(decision["reviewers"]) == profile["reviewers"]
            and decision.get("max_corrections") == profile["corrections"]
        )
        if not profile_matches and decision.get("effort_override") == "none":
            problems.append("team or correction limit differs from the decision-class profile without Human override")

    external = value.get("external_actions")
    if not isinstance(external, dict) or set(external) != {"allowed", "prohibited"} or not unique_strings(external.get("allowed"), allow_empty=True) or not unique_strings(external.get("prohibited")):
        problems.append("external_actions must contain unique allowed and non-empty prohibited lists")

    if not unique_strings(value.get("completion_evidence")):
        problems.append("completion_evidence must be a non-empty unique list")

    agent_start = value.get("agent_start")
    recovery_problems = start_recovery_problems(root, relative, text, value, identifier)
    start_recovered = recovery_problems == []
    if recovery_problems:
        problems.extend(recovery_problems)
    if not isinstance(agent_start, dict) or set(agent_start) != {"applicability", "spawn_reviewer", "clearance", "cleared_agents"}:
        problems.append("agent_start fields are incomplete")
    elif agent_start.get("applicability") == "required":
        if start_recovered:
            if not nonempty_string(agent_start.get("spawn_reviewer")) or not unique_strings(agent_start.get("cleared_agents"), allow_empty=True):
                problems.append("recovered Agent Start must retain well-formed original fields")
        elif not nonempty_string(agent_start.get("spawn_reviewer")) or agent_start.get("spawn_reviewer") == "not_applicable" or agent_start.get("clearance") != "pass" or not unique_strings(agent_start.get("cleared_agents")) or decision.get("lead") not in agent_start.get("cleared_agents", []):
            problems.append("required Agent Start lacks Spawn Reviewer pass for the Lead")
    elif agent_start.get("applicability") == "not_applicable_d0":
        if decision_class != "D0" or agent_start.get("spawn_reviewer") != "not_applicable" or agent_start.get("clearance") != "not_applicable" or agent_start.get("cleared_agents") != []:
            problems.append("Agent Start non-applicability is valid only for D0")
    else:
        problems.append("agent_start.applicability is invalid")

    if isinstance(version, str) and SEMVER.fullmatch(version) and semver_tuple(version) >= TASK_CONTROLS_MIN_VERSION:
        problems.extend(task_control_problems(text, value, target_documents, identifier, start_recovered))

    for problem in problems:
        add("AHV-RUN-CHECK-001", "error", relative, problem, "correct only the named Run Contract field or exact target")
    return value if not problems else None


def validate_ordinary_admission(
    root: Path,
    records: dict[str, tuple[Path, str, bool]],
    events: list[dict[str, Any]],
    id_paths: dict[str, Path],
    mode: str,
    add,
) -> None:
    contracts: dict[str, tuple[Path, dict[str, Any]]] = {}
    event_subjects = {event["subject_id"] for event in events}
    for relative, (path, text, is_template) in records.items():
        identifier = ARTIFACT_ID.search(text)
        run_id = identifier.group(1) if identifier else None
        is_run_contract = bool(
            run_id
            and "/run-events/" not in f"/{relative}"
            and "-EVENT-" not in run_id
            and (
                run_id in event_subjects
                or run_id.startswith("AH-RUN-")
                or re.search(r"^# (?:Execution )?Run(?: Contract)?\b", text, re.MULTILINE)
            )
        )
        if is_template or not is_run_contract:
            continue
        if DIRECT_RUN_BLOCK.search(text):
            validate_direct_run_contract(root, relative, text, run_id, mode, add)
            continue
        version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
        visible_applicable = bool(version and SEMVER.fullmatch(version.group(1)) and semver_tuple(version.group(1)) >= ADMISSION_MIN_VERSION)
        if version and SEMVER.fullmatch(version.group(1)) and not visible_applicable:
            if ADMISSION_PROJECTION_BLOCK.search(text):
                add("AHV-ADMISSION-001", "error", relative, "an Admission Projection cannot be hidden by lowering the visible Harness version", "restore the authorized current Harness binding or migrate through a Contract revision")
            continue
        # A repository upgrade cannot project the installed ruleset onto an older
        # Contract that never declared those rules. Current Runs declare their
        # Harness version; activation of an old pin is rejected by the report
        # builder until an authorized schema-migration revision exists.
        if not visible_applicable and ADMISSION_PROJECTION_BLOCK.search(text):
            add("AHV-ADMISSION-001", "error", relative, "an Admission Projection lacks its visible current Harness version", "restore the Contract's explicit Harness version or migrate through an authorized revision")
            continue
        if not visible_applicable:
            continue
        mission = re.search(r"^- Mission ID or `none`:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
        if not mission:
            add("AHV-ADMISSION-001", "error", relative, "Harness >=1.0.10 Run lacks explicit Mission applicability", "record Mission ID or exact none before admission")
            continue
        if mission.group(1).strip().lower() not in {"none", "not_applicable"}:
            continue
        if not version or not SEMVER.fullmatch(version.group(1)) or semver_tuple(version.group(1)) < ADMISSION_MIN_VERSION:
            add("AHV-ADMISSION-001", "error", relative, "prospective ordinary Run lacks the visible canonical Harness >=1.0.10 binding", "restore the exact installed Harness version before admission")
        projection = parse_admission_projection(relative, text, run_id, add, set(id_paths))
        visible_version = version.group(1) if version and SEMVER.fullmatch(version.group(1)) else None
        if projection and projection["harness_version"] != visible_version:
            add("AHV-ADMISSION-002", "error", relative, f"Admission Projection Harness version {projection['harness_version']!r} differs from visible Contract version {visible_version!r}", "bind the Projection to the exact Contract revision's Harness release")
            projection = None
        if identifier and projection:
            contracts[run_id] = (path, projection)

    events_by_run: dict[str, list[dict[str, Any]]] = {}
    for event in events:
        events_by_run.setdefault(event["subject_id"], []).append(event)
    for run_id, (contract_path, projection) in contracts.items():
        current_digest = digest(contract_path)
        chain = sorted(
            (event for event in events_by_run.get(run_id, []) if event["contract_digest"] == current_digest),
            key=lambda item: item["sequence"],
        )
        current_report_digest: str | None = None
        current_report: dict[str, Any] | None = None
        active_seen = False
        correction_reentries = 0
        for event in chain:
            transition = (event["from"], event["to"])
            if transition in ADMISSION_ACTIVE_TRANSITIONS:
                if transition == ("changes_requested", "active") and semver_tuple(projection["harness_version"]) >= CORRECTION_AUTHORITY_MIN_VERSION:
                    correction_reentries += 1
                    if correction_reentries > projection["authority"]["correction_budget"]:
                        add("AHV-CORRECTION-002", "error", event["path"].as_posix(), f"ordinary correction re-entry {correction_reentries} exceeds declared ceiling {projection['authority']['correction_budget']}", "checkpoint and use remaining Mission authority or obtain one exact Human amendment before another correction Run")
                validated = validate_admission_report(root, event, contract_path, projection, mode, add)
                current_report_digest, current_report = validated if validated else (None, None)
                active_seen = True
                continue
            if not active_seen:
                continue
            binding = re.search(r"^- Admission report SHA-256:\s*`([0-9a-f]{64})`\s*$", event["text"], re.MULTILINE)
            report_lease = current_report.get("lease", {}).get("evidence") if current_report else None
            report_authority = current_report.get("authority_ref") if current_report else None
            repository_binding = re.search(r"^- Admission repository state:\s*(\{[^\n]+\})\s*$", event["text"], re.MULTILINE)
            repository_valid = False
            if repository_binding:
                try:
                    observed_repository = json.loads(repository_binding.group(1))
                except json.JSONDecodeError:
                    observed_repository = None
                expected_repository = projection["repository"]
                if expected_repository["git_mutation"]:
                    repository_valid = bool(
                        isinstance(observed_repository, dict)
                        and set(observed_repository) == {"remote", "current_branch", "head_commit"}
                        and isinstance(observed_repository.get("remote"), str)
                        and same_git_remote(observed_repository["remote"], expected_repository["remote"])
                        and observed_repository.get("current_branch") == expected_repository["current_branch"]
                        and re.fullmatch(r"[0-9a-f]{40,64}", str(observed_repository.get("head_commit", "")))
                    )
                    if repository_valid and (root / ".git").exists():
                        head_commit = observed_repository["head_commit"]
                        exists = subprocess.run(["git", "cat-file", "-e", f"{head_commit}^{{commit}}"], cwd=root, capture_output=True, check=False)
                        ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", expected_repository["start_commit"], head_commit], cwd=root, capture_output=True, check=False)
                        repository_valid = exists.returncode == 0 and ancestor.returncode == 0
                else:
                    repository_valid = observed_repository == {"remote":"not_applicable","current_branch":"not_applicable","head_commit":"not_applicable"}
            if (
                not current_report_digest
                or not binding
                or binding.group(1) != current_report_digest
                or event["authority"] != report_authority
                or event["lease"] != report_lease
                or not repository_valid
            ):
                add("AHV-ADMISSION-005", "error", event["path"].as_posix(), "post-activation event lacks the latest exact report, authority, lease, or transition-time repository state", "bind the latest active-transition report and exact observed repository state before continuation or completion")
        latest_state = chain[-1]["to"] if chain else None
        repository = projection["repository"]
        if latest_state in NON_TERMINAL and repository["git_mutation"] and (root / ".git").exists():
            try:
                actual_remote = git_output(root, ["remote", "get-url", "origin"]).strip()
                actual_branch = git_output(root, ["branch", "--show-current"]).strip()
                actual_head = git_output(root, ["rev-parse", "HEAD"]).strip()
                git_output(root, ["merge-base", "--is-ancestor", repository["start_commit"], actual_head])
            except ValueError as error:
                add("AHV-ADMISSION-004", "error", contract_path.relative_to(root).as_posix(), f"current repository state cannot satisfy the admitted baseline: {error}", "restore the admitted repository lineage or pause and re-authorize")
            else:
                if not same_git_remote(actual_remote, repository["remote"]) or actual_branch != repository["current_branch"]:
                    add("AHV-ADMISSION-004", "error", contract_path.relative_to(root).as_posix(), "current repository remote/branch drifted from the green Admission Report", "restore the admitted repository identity or pause and re-authorize")


def parse_visual_assurance(relative: str, text: str, run_id: str, projection: dict[str, Any], artifact_digests: dict[str, str], add) -> dict[str, Any] | None:
    blocks = VISUAL_ASSURANCE_BLOCK.findall(text)
    if len(blocks) != 1:
        add("AHV-VISUAL-001", "error", relative, f"Harness 1.0.13+ Run requires exactly one visual-assurance projection; found {len(blocks)}", "select material_ui, minor_ui, or non_visual once in the immutable Run")
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-VISUAL-001", "error", relative, f"visual-assurance JSON is invalid: {error}", "restore the compact typed projection")
        return None
    fields = {"schema_version", "run_id", "applicability", "rationale", "design_prerequisite", "critical_surfaces", "representative_coverage"}
    design_fields = {"disposition", "reference_id", "sha256"}
    problems: list[str] = []
    if not isinstance(value, dict) or set(value) != fields:
        problems.append("fields")
        value = value if isinstance(value, dict) else {}
    if value.get("schema_version") != "1" or value.get("run_id") != run_id:
        problems.append("schema/run_id")
    applicability = value.get("applicability")
    if applicability not in {"material_ui", "minor_ui", "non_visual"}:
        problems.append("applicability")
    if not nonempty_string(value.get("rationale")):
        problems.append("rationale")
    design = value.get("design_prerequisite")
    if not isinstance(design, dict) or set(design) != design_fields:
        problems.append("design_prerequisite")
        design = {}
    surfaces = value.get("critical_surfaces")
    if not unique_strings(surfaces, allow_empty=True):
        problems.append("critical_surfaces")
        surfaces = []
    coverage = value.get("representative_coverage")
    if not nonempty_string(coverage):
        problems.append("representative_coverage")
    if applicability == "material_ui":
        reviewed_reference = (
            design.get("disposition") == "reviewed_reference"
            and nonempty_string(design.get("reference_id"))
            and HEX64.fullmatch(str(design.get("sha256", ""))) is not None
            and artifact_digests.get(design.get("reference_id")) == design.get("sha256")
        )
        standalone = design.get("disposition") == "owner_approved_standalone" and design.get("reference_id") == projection.get("authority", {}).get("decision_authority_ref") and design.get("sha256") == "not_applicable"
        if not (reviewed_reference or standalone):
            problems.append("material design reference")
        if not surfaces or coverage == "not_applicable":
            problems.append("material representative coverage")
    elif applicability == "minor_ui":
        if design.get("disposition") != "owner_approved_direct" or design.get("reference_id") != projection.get("authority", {}).get("decision_authority_ref") or design.get("sha256") != "not_applicable":
            problems.append("minor direct authority")
        if surfaces or coverage != "not_applicable":
            problems.append("minor proportionality")
    elif applicability == "non_visual":
        if design != {"disposition":"not_applicable", "reference_id":"not_applicable", "sha256":"not_applicable"} or surfaces or coverage != "not_applicable":
            problems.append("non-visual proportionality")
    classification = re.search(r"^> Decision class / classification trigger ID:\s*`?(D[0-3])`?\s*/\s*`?([a-z0-9_]+)`?\s*$", text, re.MULTILINE)
    decision_class, trigger = classification.groups() if classification else (None, None)
    if trigger == "significant_ui" and applicability != "material_ui":
        problems.append("material trigger downgraded")
    if applicability == "material_ui" and (decision_class != "D2" or trigger not in {"significant_ui", "material_user_flow"}):
        problems.append("material classification binding")
    if applicability == "minor_ui" and (decision_class != "D1" or trigger != "bounded_reversible"):
        problems.append("minor classification binding")
    if problems:
        add("AHV-VISUAL-001", "error", relative, f"visual-assurance prerequisite is incomplete or disproportionate: {sorted(set(problems))}", "bind the smallest applicable design prerequisite before mutation")
        return None
    return value


def parse_visual_review(root: Path, relative: str, payload: str, assurance: dict[str, Any], projection: dict[str, Any], expected_commit: str | None, add) -> dict[str, Any] | None:
    try:
        value = json.loads(payload)
    except json.JSONDecodeError as error:
        add("AHV-VISUAL-002", "error", relative, f"visual-review evidence JSON is invalid: {error}", "restore the exact candidate-bound Review projection")
        return None
    fields = {"schema_version", "run_id", "candidate", "design_reference", "representative_coverage", "images", "comparisons", "review", "creator_material_contributor_ids", "final_approver_id"}
    candidate_fields = {"id", "source_commit"}; reference_fields = {"id", "sha256"}
    image_fields = {"id", "role", "artifact_ref", "sha256", "surface", "state", "viewport"}
    comparison_fields = {"candidate_image_id", "baseline_image_id"}
    review_fields = {"reviewer_id", "capability", "inspected_image_ids", "axes", "outcome"}
    problems: list[str] = []
    if not isinstance(value, dict) or set(value) != fields:
        problems.append("fields")
        value = value if isinstance(value, dict) else {}
    if value.get("schema_version") != "1" or value.get("run_id") != assurance["run_id"]:
        problems.append("schema/run_id")
    candidate = value.get("candidate")
    if not isinstance(candidate, dict) or set(candidate) != candidate_fields or not nonempty_string(candidate.get("id")) or re.fullmatch(r"[0-9a-f]{40,64}", str(candidate.get("source_commit", ""))) is None:
        problems.append("candidate")
        candidate = {}
    elif expected_commit and candidate.get("source_commit") != expected_commit:
        problems.append("stale/wrong candidate commit")
    reference = value.get("design_reference")
    expected_reference = assurance["design_prerequisite"]
    if not isinstance(reference, dict) or set(reference) != reference_fields or reference.get("id") != expected_reference["reference_id"] or reference.get("sha256") != expected_reference["sha256"]:
        problems.append("design reference binding")
    if value.get("representative_coverage") != assurance["representative_coverage"]:
        problems.append("representative coverage binding")
    images = value.get("images")
    image_ids: set[str] = set(); candidate_ids: set[str] = set(); baseline_ids: set[str] = set(); candidate_surfaces: set[str] = set()
    if not isinstance(images, list) or not images:
        problems.append("images")
        images = []
    for image in images:
        valid = isinstance(image, dict) and set(image) == image_fields
        if not valid:
            problems.append("image fields")
            continue
        image_id = image.get("id"); role = image.get("role")
        artifact_ref = image.get("artifact_ref")
        artifact_valid = False
        try:
            evidence_relative = safe_relative(str(artifact_ref), f"docs/reviews/evidence/{assurance['run_id']}")
            evidence_path = root
            path_has_symlink = False
            for part in evidence_relative.parts:
                evidence_path = evidence_path / part
                path_has_symlink = path_has_symlink or evidence_path.is_symlink()
        except ValueError:
            evidence_path = root / "invalid"
            path_has_symlink = True
        if evidence_path.is_file() and not path_has_symlink:
            evidence_bytes = evidence_path.read_bytes()
            raster_valid = (
                (len(evidence_bytes) >= 24 and evidence_bytes.startswith(b"\x89PNG\r\n\x1a\n") and evidence_bytes[12:16] == b"IHDR" and int.from_bytes(evidence_bytes[16:20], "big") > 0 and int.from_bytes(evidence_bytes[20:24], "big") > 0)
                or (len(evidence_bytes) >= 4 and evidence_bytes.startswith(b"\xff\xd8\xff") and evidence_bytes.endswith(b"\xff\xd9"))
                or (len(evidence_bytes) >= 16 and evidence_bytes.startswith(b"RIFF") and evidence_bytes[8:12] == b"WEBP")
            )
            artifact_valid = raster_valid and hashlib.sha256(evidence_bytes).hexdigest() == image.get("sha256")
        if not nonempty_string(image_id) or image_id in image_ids or role not in {"candidate", "baseline"} or not artifact_valid or not nonempty_string(image.get("surface")) or not nonempty_string(image.get("state")) or re.fullmatch(r"[1-9][0-9]*x[1-9][0-9]*", str(image.get("viewport", ""))) is None:
            problems.append("image identity/context")
            continue
        image_ids.add(image_id)
        (candidate_ids if role == "candidate" else baseline_ids).add(image_id)
        if role == "candidate":
            candidate_surfaces.add(f"{image['surface']}#{image['state']}")
    baseline_required = assurance["design_prerequisite"]["disposition"] == "reviewed_reference"
    if not candidate_ids or not set(assurance["critical_surfaces"]).issubset(candidate_surfaces) or (baseline_required and not baseline_ids) or (not baseline_required and baseline_ids):
        problems.append("candidate/baseline representative images")
    comparisons = value.get("comparisons")
    compared_candidates: set[str] = set()
    if not isinstance(comparisons, list) or (baseline_required and not comparisons):
        problems.append("comparisons")
        comparisons = []
    for comparison in comparisons:
        if not isinstance(comparison, dict) or set(comparison) != comparison_fields or comparison.get("candidate_image_id") not in candidate_ids or comparison.get("baseline_image_id") not in baseline_ids:
            problems.append("comparison binding")
        else:
            compared_candidates.add(comparison["candidate_image_id"])
    if (baseline_required and compared_candidates != candidate_ids) or (not baseline_required and comparisons):
        problems.append("uncompared candidate image")
    review = value.get("review")
    if not isinstance(review, dict) or set(review) != review_fields:
        problems.append("review fields")
        review = {}
    reviewer_id = review.get("reviewer_id")
    inspected = review.get("inspected_image_ids")
    axes = review.get("axes")
    authority = projection.get("authority")
    projected_reviewers = authority.get("reviewers") if isinstance(authority, dict) else None
    reviewer_ids = set(projected_reviewers) if unique_strings(projected_reviewers) else set()
    inspected_ids = set(inspected) if unique_strings(inspected) else set()
    review_axes = set(axes) if unique_strings(axes) else set()
    if reviewer_id not in reviewer_ids or review.get("capability") not in {"browser", "image_tool"} or inspected_ids != image_ids or review_axes != VISUAL_REVIEW_AXES or review.get("outcome") not in {"approved", "changes_requested"}:
        problems.append("reviewer capability/inspection/axes/outcome")
    creators = value.get("creator_material_contributor_ids")
    final_approver = value.get("final_approver_id")
    creator_set = set(creators) if unique_strings(creators) else set()
    lead = authority.get("lead") if isinstance(authority, dict) else None
    decision_authority = authority.get("decision_authority_ref") if isinstance(authority, dict) else None
    if not creator_set or lead not in creator_set or final_approver != decision_authority or reviewer_id in creator_set or final_approver in creator_set:
        problems.append("non-author review/approval")
    if problems:
        add("AHV-VISUAL-002", "error", relative, f"visual-review evidence is incomplete, stale, or unsupported: {sorted(set(problems))}", "bind exact representative images actually inspected by the independent Product/UX reviewer")
        return None
    return value


def validate_visual_assurance(root: Path, records: dict[str, tuple[Path, str, bool]], events: list[dict[str, Any]], add) -> None:
    event_subjects = {event["subject_id"] for event in events}
    artifact_digests: dict[str, str] = {}
    evidence_blocks: list[tuple[str, str]] = []
    for relative, (_path, text, is_template) in records.items():
        if is_template:
            continue
        identifier = ARTIFACT_ID.search(text)
        if identifier:
            artifact_digests[identifier.group(1)] = hashlib.sha256(_path.read_bytes()).hexdigest()
        for payload in VISUAL_REVIEW_BLOCK.findall(text):
            evidence_blocks.append((relative, payload))
    for relative, (_path, text, is_template) in records.items():
        identifier = ARTIFACT_ID.search(text); version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
        run_id = identifier.group(1) if identifier else None
        if is_template or not run_id or run_id not in event_subjects or "/run-events/" in f"/{relative}" or not version or not SEMVER.fullmatch(version.group(1)) or semver_tuple(version.group(1)) < VISUAL_ASSURANCE_MIN_VERSION:
            continue
        projection_blocks = ADMISSION_PROJECTION_BLOCK.findall(text)
        try:
            projection = json.loads(projection_blocks[0]) if len(projection_blocks) == 1 else {}
        except json.JSONDecodeError:
            projection = {}
        if not isinstance(projection, dict) or not isinstance(projection.get("authority"), dict):
            add("AHV-VISUAL-001", "error", relative, "visual assurance cannot bind missing ordinary Admission authority", "restore Package-1 admission before selecting visual applicability")
            continue
        assurance = parse_visual_assurance(relative, text, run_id, projection, artifact_digests, add)
        if not assurance:
            continue
        if assurance["applicability"] != "material_ui":
            continue
        run_events = sorted((event for event in events if event["subject_id"] == run_id), key=lambda item: item["sequence"])
        if not run_events or run_events[-1]["to"] not in {"verification", "changes_requested", "completed"}:
            continue
        verification_events = [event for event in run_events if event["to"] == "verification"]
        expected_commit: str | None = None
        if verification_events:
            repository_binding = re.search(r"^- Admission repository state:\s*(\{[^\n]+\})\s*$", verification_events[-1]["text"], re.MULTILINE)
            try:
                repository_state = json.loads(repository_binding.group(1)) if repository_binding else {}
            except json.JSONDecodeError:
                repository_state = {}
            candidate_commit = repository_state.get("head_commit") if isinstance(repository_state, dict) else None
            expected_commit = candidate_commit if isinstance(candidate_commit, str) else None
        matching: list[tuple[str, str]] = []
        for evidence_relative, payload in evidence_blocks:
            try:
                value = json.loads(payload)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict) and value.get("run_id") == run_id:
                matching.append((evidence_relative, payload))
        if len(matching) != 1:
            add("AHV-VISUAL-002", "error", relative, f"material UI verification requires exactly one matching visual-review evidence projection; found {len(matching)}", "add one exact Review-record projection before visual verification/acceptance")
            continue
        evidence_relative, payload = matching[0]
        if not evidence_relative.startswith("docs/reviews/") or "/evidence/" in f"/{evidence_relative}":
            add("AHV-VISUAL-002", "error", evidence_relative, "visual-review evidence must live in the existing top-level Review record", "move the projection into the exact candidate Review record")
            continue
        review = parse_visual_review(root, evidence_relative, payload, assurance, projection, expected_commit, add)
        if review and run_events[-1]["to"] == "completed" and review["review"]["outcome"] != "approved":
            add("AHV-VISUAL-003", "error", evidence_relative, "completed material UI Run lacks approved visual-review outcome", "retain changes_requested or close the exact candidate visual finding before completion")


def build_admission_report(
    root: Path,
    contract_relative: str,
    transition_from: str,
    authority_ref: str,
    lease_evidence: str,
    evaluated_at: str | None,
    mode: str,
    expected_manifest: str | None,
) -> dict[str, Any]:
    safe_relative(contract_relative)
    contract_path = root / contract_relative
    if not contract_path.is_file() or contract_path.is_symlink():
        raise ValueError("admission Contract path is missing, non-regular, or a symlink")
    text = contract_path.read_text(encoding="utf-8")
    installed_version = current_harness_version(root, mode)
    raw_blocks = ADMISSION_PROJECTION_BLOCK.findall(text)
    if len(raw_blocks) == 1:
        try:
            raw_projection = json.loads(raw_blocks[0])
        except json.JSONDecodeError:
            raw_projection = {}
        raw_version = raw_projection.get("harness_version") if isinstance(raw_projection, dict) else None
        if isinstance(raw_version, str) and SEMVER.fullmatch(raw_version) and raw_version != installed_version:
            raise ValueError(
                f"current activation requires Contract migration to installed Harness {installed_version}; "
                f"observed Contract revision pinned to {raw_version}"
            )
    identifier = ARTIFACT_ID.search(text)
    known_ids = {
        match.group(1)
        for path in markdown_files(repository_files(root, mode, lambda *_args: None))
        if (match := ARTIFACT_ID.search(path.read_text(encoding="utf-8")))
        and not any(marker in match.group(1) for marker in ("{{", "<<"))
    }
    local_findings: list[str] = []
    projection = parse_admission_projection(contract_relative, text, identifier.group(1) if identifier else None, lambda rule, severity, path, evidence, remediation: local_findings.append(f"{rule} {evidence}"), known_ids)
    if not projection or local_findings:
        raise ValueError(local_findings[0] if local_findings else "Admission Projection is invalid")
    if projection["harness_version"] != installed_version:
        raise ValueError(
            f"current activation requires Contract migration to installed Harness {installed_version}; "
            f"observed Contract revision pinned to {projection['harness_version']}"
        )
    findings = validate(root, mode, expected_manifest)
    errors = [item for item in findings if item.severity == "error"]
    if errors:
        first = errors[0]
        raise ValueError(f"Harness validation is not green: {first.rule_id} {first.path}: {first.evidence}")
    if (transition_from, "active") not in ADMISSION_ACTIVE_TRANSITIONS:
        raise ValueError("admission transition must be authorized|paused|blocked|changes_requested -> active")
    if authority_ref != projection["authority"]["decision_authority_ref"]:
        raise ValueError("admission authority reference differs from the Contract projection")
    if not nonempty_string(lease_evidence):
        raise ValueError("admission lease evidence is required")

    parsed: list[dict[str, Any]] = []
    no_op = lambda *_args: None
    for path in sorted((root / "docs/work/run-events").glob("*.md")) if (root / "docs/work/run-events").is_dir() else []:
        event = parse_event(path.relative_to(root), path.read_text(encoding="utf-8"), mode, no_op)
        if event and event["subject_id"] == projection["run_id"]:
            parsed.append(event)
    parsed.sort(key=lambda item: item["sequence"])
    if not parsed or parsed[-1]["to"] != transition_from:
        raise ValueError(f"latest valid Run event must end in {transition_from!r} before admission")
    if transition_from == "changes_requested" and semver_tuple(projection["harness_version"]) >= CORRECTION_AUTHORITY_MIN_VERSION:
        correction_reentries = sum(1 for item in parsed if (item["from"], item["to"]) == ("changes_requested", "active"))
        ceiling = projection["authority"]["correction_budget"]
        if correction_reentries >= ceiling:
            raise ValueError(f"ordinary correction-pass ceiling exhausted: consumed={correction_reentries}, ceiling={ceiling}")

    control: dict[str, Any] | None = None
    required_activation_records: list[tuple[Path, dict[str, Any]]] = []
    if semver_tuple(projection["harness_version"]) >= AGENT_START_MIN_VERSION:
        control = parse_agent_start_control(
            root, contract_relative, text,
            identifier.group(1) if identifier else projection["run_id"],
            projection, mode, lambda *_args: None,
        )
        if control is None:
            raise ValueError("Agent-start control is invalid")
        if control.get("schema_version") == "2" and control.get("applicability") == "required":
            required_now = {
                item["agent_id"] for item in control.get("planned_agents", [])
                if item.get("activation_stage") == "implementation"
            }
            for path in markdown_files(repository_files(root, mode, lambda *_args: None)):
                activation_text = path.read_text(encoding="utf-8")
                blocks = AGENT_ACTIVATION_BLOCK.findall(activation_text)
                if len(blocks) != 1:
                    continue
                try: raw = json.loads(blocks[0])
                except json.JSONDecodeError: continue
                if not isinstance(raw, dict) or raw.get("run_id") != projection["run_id"] or raw.get("agent_id") not in required_now:
                    continue
                local: list[str] = []
                parsed_activation = parse_agent_activation_record(
                    root, normalized_relative(path, root), activation_text, control, projection, mode,
                    lambda rule, severity, path_value, evidence, remediation: local.append(f"{rule} {evidence}"),
                )
                if not parsed_activation or local:
                    raise ValueError(local[0] if local else "Agent activation record is invalid")
                required_activation_records.append((path, parsed_activation))
            activated_ids = {item["agent_id"] for _path, item in required_activation_records}
            if not required_now or not required_now.issubset(activated_ids):
                raise ValueError(f"initial admission lacks implementation activation records: {sorted(required_now - activated_ids)}")
            if len(required_activation_records) != len(activated_ids):
                raise ValueError("initial admission has duplicate implementation activation records")

    repository = dict(projection["repository"])
    lease = projection["lease"]
    lease_relative: str | None = None
    if lease["disposition"] == "required":
        try:
            lease_relative, lease_data = evidence_reference(root, lease_evidence)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            raise ValueError(f"admission lease evidence is invalid: {error}") from error
        required_lease = {
            "schema_version": "1", "key": lease["key"], "target": lease["target"],
            "owner": lease["owner"], "run_id": projection["run_id"], "state": "claimed",
        }
        if any(lease_data.get(field) != expected for field, expected in required_lease.items()):
            raise ValueError("admission lease evidence content differs from the projected claim")
    elif not lease_evidence.startswith("not_applicable:"):
        raise ValueError("non-applicable lease evidence must start with 'not_applicable:' and state the owner rationale")
    if repository["git_mutation"]:
        actual_remote = git_output(root, ["remote", "get-url", "origin"]).strip()
        actual_branch = git_output(root, ["branch", "--show-current"]).strip()
        actual_head = git_output(root, ["rev-parse", "HEAD"]).strip()
        git_output(root, ["cat-file", "-e", f"{repository['start_commit']}^{{commit}}"])
        git_output(root, ["merge-base", "--is-ancestor", repository["start_commit"], actual_head])
        if not same_git_remote(actual_remote, repository["remote"]) or actual_branch != repository["current_branch"]:
            raise ValueError("current repository remote/branch differs from the Admission Projection")
        if transition_from == "authorized" and actual_head != repository["start_commit"]:
            raise ValueError("initial activation HEAD differs from the projected starting commit")
        dirty_paths, dirty_sha256 = git_dirty_paths(root)
        allowed_dirty = {contract_relative}
        for event in parsed:
            allowed_dirty.add(event["path"].as_posix())
        allowed_dirty.update(normalized_relative(path, root) for path, _item in required_activation_records)
        if lease_relative:
            allowed_dirty.add(lease_relative)
        unexpected_dirty = sorted(dirty_paths - allowed_dirty)
        if unexpected_dirty:
            raise ValueError(f"uncommitted paths outside the exact pre-active Run boundary: {unexpected_dirty}")
        repository["observed_head_commit"] = actual_head
        repository["observed_dirty_sha256"] = dirty_sha256
    else:
        repository["observed_head_commit"] = "not_applicable"
        repository["observed_dirty_sha256"] = "not_applicable"
    timestamp = evaluated_at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        if datetime.fromisoformat(timestamp.replace("Z", "+00:00")).tzinfo is None:
            raise ValueError
    except ValueError as error:
        raise ValueError("evaluation time must be RFC3339 with timezone") from error
    report = {
        "schema_version": "1",
        "report_id": f"{projection['run_id']}-ADMISSION-{parsed[-1]['sequence'] + 1:03d}",
        "subject_run_id": projection["run_id"],
        "contract_sha256": digest(contract_path),
        "ruleset_id": projection["ruleset_id"],
        "harness_version": projection["harness_version"],
        "intended_transition": {"from": transition_from, "to": "active"},
        "repository": repository,
        "authority_ref": authority_ref,
        "environment_disposition": admission_environment(projection),
        "lease": {"key": lease["key"], "owner": lease["owner"], "evidence": lease_evidence},
        "evaluated_at": timestamp,
        "tool_id": f"validate_harness.py@{projection['harness_version']}",
        "rule_results": expected_admission_rule_results(projection),
        "claims": {"contract_admission": "pass", "event_chain_integrity": "not_observed", "semantic_review": "not_observed"},
    }
    if control is not None:
        report["agent_start_control_sha256"] = canonical_json_sha256(control)
        if control.get("schema_version") == "2" and control.get("applicability") == "required":
            activation_digests = [digest(path) for path, _item in required_activation_records]
            activated_ids = {item["agent_id"] for _path, item in required_activation_records}
            planned_ids = {item["agent_id"] for item in control.get("planned_agents", [])}
            report["agent_activation_record_sha256s"] = sorted(activation_digests)
            report["pending_agent_ids"] = sorted(planned_ids - activated_ids)
    return report


def validate_delivery_artifact(relative: str, text: str, is_template: bool, identifier: str | None, add) -> None:
    if relative.endswith("/.agentic-harness/templates/product-release-policy.template.md") or relative == ".agentic-harness/templates/product-release-policy.template.md":
        required = (
            "## Release Unit And Version Source", "## Compatibility And Increment Policy",
            "## Product Tags, Candidates, And Publication", "## Components, Migrations, And Recovery",
            "## Operational Discovery And Evidence", "## Examples And Anti-Criteria",
        )
        if any(heading not in text for heading in required):
            add("AHV-PRODUCT-RELEASE-001", "error", relative, "Product Release Policy template lacks required owned sections", "restore the complete governed Product Release Policy template")
    if relative.endswith("/.agentic-harness/templates/product-release-identity-event.template.md") or relative == ".agentic-harness/templates/product-release-identity-event.template.md":
        required = ("## Transition", "Product Release Policy ID / revision SHA-256", "Owning final RC ID / SHA-256", "Production mutation observation")
        if any(item not in text for item in required):
            add("AHV-PRODUCT-RELEASE-002", "error", relative, "Product Release Identity Event template lacks required chain/state/owner/evidence fields", "restore the complete governed identity-event template")
    if is_template:
        return
    if re.search(r"^> Slice status:", text, re.MULTILINE):
        required = (
            r"^> Artifact class:\s*Work contract",
            r"^> Milestone / Feature-Capability outcomes:",
            r"^## Vertical Outcome$",
            r"^## Ordered Work Packages And Boundaries$",
            r"^## Sizing And Delivery Policy$",
            r"^## Acceptance And Anti-Criteria$",
            r"^## Post-Slice Revalidation$",
            r"Product Delivery Release Candidate Manifest path/ID:",
            r"Early Verification Candidate triggers:",
        )
        missing = [pattern for pattern in required if not re.search(pattern, text, re.MULTILINE)]
        if missing:
            add("AHV-SLICE-001", "error", relative, f"Delivery Slice contract is incomplete: {missing}", "instantiate the complete governed Slice contract")
    candidate = re.search(r"^> Candidate classification:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
    is_delivery_rc = bool(
        (identifier and "-DELIVERY-RC-" in identifier)
        or re.search(r"^# Product Delivery Release Candidate\b", text, re.MULTILINE)
    )
    if is_delivery_rc:
        version = re.search(r"^> Harness version:\s*`([^`]+)`\s*$", text, re.MULTILINE)
        proportionate = bool(version and SEMVER.fullmatch(version.group(1))
                             and semver_tuple(version.group(1)) >= PROPORTIONATE_EXECUTION_MIN_VERSION)
        work_identity = re.search(r"^> Work identity:\s*`([^`]+)`\s*$", text, re.MULTILINE)
        routine = bool(work_identity and work_identity.group(1) == "routine")
        if (routine and not proportionate) or (work_identity and work_identity.group(1) not in {"slice", "routine"}):
            add("AHV-SLICE-002", "error", relative, "routine RC requires Harness1.5+ and a valid work identity", "bind the actual released contract version and slice or routine identity")
        if routine:
            for field in ("Task reference", "D0 rationale", "Delivery authority"):
                if not re.search(rf"^> {re.escape(field)}:\s*(?!`?(?:none|not_applicable|pending)`?\s*$)\S.+$", text, re.MULTILINE):
                    add("AHV-SLICE-002", "error", relative, f"routine RC lacks {field}", "bind the actual task, eligibility and target/action authority; local edit permission alone is insufficient")
        if proportionate and not uses_lease_free_contract(version.group(1)) and not re.search(r"^> Shared-resource coordination evidence:\s*(?!`?(?:none|pending)`?\s*$)\S.+$", text, re.MULTILINE):
            add("AHV-SLICE-002", "error", relative, "RC lacks shared-resource coordination evidence", "reference existing executor/provider serialization and safe release; do not manufacture a branch lease")
        classification = candidate.group(1).strip() if candidate else "missing"
        promotion = re.search(r"^> Promotion state:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
        version_state = re.search(r"^> Product release version state:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
        intended_version = re.search(r"^> Intended Product version:\s*`([^`\s]+)`\s*$", text, re.MULTILINE)
        product_tag = re.search(r"^> Proposed Product release tag:\s*`([^`\s]+)`\s*$", text, re.MULTILINE)
        release_policy = re.search(r"^> Product Release Policy ID / revision SHA-256:\s*`([^`\s]+)`\s*/\s*`([^`\s]+)`\s*$", text, re.MULTILINE)
        required_headings = (
            "## Product And Work Identity", "## Source And Specification Identity",
            "## Application And Toolchain Artifacts", "## Environment-Specific IaC",
            "## Provenance, Validity, And Recovery",
        )
        if not candidate or classification not in {"final", "verification_candidate"} or not promotion or any(heading not in text for heading in required_headings):
            add("AHV-SLICE-002", "error", relative, "Product Delivery RC classification, promotion state, or required identity sections are invalid", "use the complete RC manifest contract")
        else:
            expected_promotion = "eligible_after_technical_and_human_gates" if classification == "final" else "non_promotable"
            if promotion.group(1).strip() != expected_promotion:
                add("AHV-SLICE-003", "error", relative, f"invalid classification/promotion pair: {classification}/{promotion.group(1).strip()}", f"use {classification}/{expected_promotion}")
            if classification == "final":
                unresolved = re.compile(r"\{\{|<<|\b(?:tbd|todo|pending|unresolved)\b", re.IGNORECASE)
                release_identity_valid = bool(
                    version_state and version_state.group(1).strip() == "reserved_unpublished"
                    and intended_version and intended_version.group(1) != "not_applicable" and not unresolved.search(intended_version.group(1))
                    and product_tag and product_tag.group(1) != "not_applicable" and not unresolved.search(product_tag.group(1))
                    and release_policy and release_policy.group(1) != "not_applicable" and not unresolved.search(release_policy.group(1)) and HEX64.fullmatch(release_policy.group(2))
                )
            else:
                release_identity_valid = bool(
                    version_state and version_state.group(1).strip() == "not_applicable"
                    and intended_version and intended_version.group(1) == "not_applicable"
                    and product_tag and product_tag.group(1) == "not_applicable"
                    and release_policy and release_policy.groups() == ("not_applicable", "not_applicable")
                )
            if not release_identity_valid:
                add("AHV-SLICE-006", "error", relative, f"invalid Product release identity for {classification} candidate", "bind reserved unpublished version/tag/Policy for final or exact not_applicable values for verification candidate")
        digest_fields = (
            "Included Package Set SHA-256", "Feature-Capability Mapping SHA-256", "Source tree SHA-256",
            "Specification Set SHA-256", "Application Artifact Set SHA-256", "Migration Set SHA-256",
            "Lockfile Set SHA-256", "SBOM SHA-256", "Toolchain Identity SHA-256",
            "Staging Assembly Tree SHA-256", "Staging Diff SHA-256", "Production Assembly Tree SHA-256",
            "Production Diff SHA-256", "Build Provenance SHA-256", "Staging Environment Lease Evidence SHA-256",
        )
        if proportionate:
            digest_fields = tuple(field for field in digest_fields if field != "Staging Environment Lease Evidence SHA-256")
        if routine:
            digest_fields = tuple(field for field in digest_fields if field not in {"Included Package Set SHA-256", "Feature-Capability Mapping SHA-256"})
        observed_digests: dict[str, str] = {}
        for field in digest_fields:
            match = re.search(rf"^> {re.escape(field)}:\s*`([0-9a-f]{{64}})`\s*$", text, re.MULTILINE)
            if match: observed_digests[field] = match.group(1)
        slice_binding = re.search(r"^> Slice ID / Contract SHA-256:\s*`([^`\s]+)`\s*/\s*`([0-9a-f]{64})`\s*$", text, re.MULTILINE)
        milestone_binding = re.search(r"^> Milestone ID / revision SHA-256:\s*`([^`\s]+)`\s*/\s*`([0-9a-f]{64})`\s*$", text, re.MULTILINE)
        source_commit = re.search(r"^> Source commit:\s*`([0-9a-f]{40,64})`\s*$", text, re.MULTILINE)
        package_rows = re.findall(r"^\|\s*`([^`\s]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|\s*`([0-9a-f]{40,64})`\s*\|\s*$", text, re.MULTILINE)
        if routine and (slice_binding or milestone_binding or package_rows or re.search(r"^> (?:Included Package Set|Feature-Capability Mapping) SHA-256:", text, re.MULTILINE)):
            add("AHV-SLICE-002", "error", relative, "routine RC mixes synthetic material work bindings", "retain only task identity; material work uses the complete slice variant")
        if len(observed_digests) != len(digest_fields) or not source_commit or (not routine and (not slice_binding or not milestone_binding or not package_rows)):
            add("AHV-SLICE-002", "error", relative, "Product Delivery RC lacks format-valid Slice/Milestone/Package/source/spec/artifact/toolchain/CDK/diff/provenance/lease bindings", "populate every required immutable identity and digest")
        elif not routine and len({row[0] for row in package_rows}) != len(package_rows):
            add("AHV-SLICE-005", "error", relative, "Product Delivery RC contains duplicate Package IDs", "bind every included Package exactly once")
        elif not routine:
            rows = sorted((f"{package}\t{contract}\t{commit}\n".encode("utf-8") for package, contract, commit in package_rows))
            package_set = hashlib.sha256(b"".join(rows)).hexdigest()
            if package_set != observed_digests["Included Package Set SHA-256"]:
                add("AHV-SLICE-005", "error", relative, "Included Package Set digest does not match exact Package revision/commit rows", "recompute the canonical Package Set digest")
    if identifier and "-WP-" in identifier and re.search(r"^> Work status:", text, re.MULTILINE):
        if not re.search(r"^> Milestone / Delivery Slice / Feature-Capability outcome:", text, re.MULTILINE):
            add("AHV-SLICE-004", "error", relative, "Work Package lacks parent Delivery Slice and Feature/Capability outcome", "bind the Package to one Slice and mapped outcome")


def validate_product_release_identity_events(root: Path, records: dict[str, tuple[Path, str, bool]], add) -> None:
    allowed = {
        ("none", "reserved_unpublished"): "reserve",
        ("reserved_unpublished", "reserved_unpublished"): "reservation_transfer",
        ("reserved_unpublished", "consumed_for_promotion"): "consume",
        ("consumed_for_promotion", "reserved_unpublished"): "reconcile_no_mutation",
        ("consumed_for_promotion", "consumed_partial"): "partial",
        ("consumed_for_promotion", "published"): "publish",
        ("consumed_partial", "published"): "publish",
        ("consumed_partial", "skipped"): "skip",
    }
    mutation_by_transition = {
        ("none", "reserved_unpublished"): {"none_proven"},
        ("reserved_unpublished", "reserved_unpublished"): {"none_proven"},
        ("reserved_unpublished", "consumed_for_promotion"): {"none_proven"},
        ("consumed_for_promotion", "reserved_unpublished"): {"none_proven"},
        ("consumed_for_promotion", "consumed_partial"): {"occurred", "may_have_occurred"},
        ("consumed_for_promotion", "published"): {"occurred"},
        ("consumed_partial", "published"): {"occurred"},
        ("consumed_partial", "skipped"): {"occurred", "may_have_occurred"},
    }
    rc_records: dict[str, tuple[Path, str]] = {}
    for path, text, is_template in records.values():
        identifier = ARTIFACT_ID.search(text)
        if not is_template and identifier and "-DELIVERY-RC-" in identifier.group(1):
            rc_records[identifier.group(1)] = (path, text)
    events: list[dict[str, Any]] = []
    for relative, (path, text, is_template) in records.items():
        identifier = ARTIFACT_ID.search(text)
        if is_template or not identifier or "-RELEASE-IDENTITY-EVENT-" not in identifier.group(1):
            continue
        subject = re.search(r"^> Immutable subject:\s*Product version\s*`([^`\s]+)`\s*/\s*tag\s*`([^`\s]+)`", text, re.MULTILINE)
        policy = re.search(r"^> Product Release Policy ID / revision SHA-256:\s*`([^`\s]+)`\s*/\s*`([0-9a-f]{64})`", text, re.MULTILINE)
        rc = re.search(r"^> Owning final RC ID / SHA-256:\s*`([^`\s]+)`\s*/\s*`([0-9a-f]{64})`", text, re.MULTILINE)
        sequence = re.search(r"^- Sequence:\s*`([0-9]+)`", text, re.MULTILINE)
        previous = re.search(r"^- Previous-event SHA-256:\s*`([^`]+)`", text, re.MULTILINE)
        transition = re.search(r"^- From / to:\s*`([^`]+)`\s*/\s*`([^`]+)`", text, re.MULTILINE)
        kind = re.search(r"^- Event kind:\s*`([^`]+)`", text, re.MULTILINE)
        actor = re.search(r"^- Actor / Decision Authority:\s*(\S.+)$", text, re.MULTILINE)
        guard = re.search(r"^- Guard evidence:\s*(\S.+)$", text, re.MULTILINE)
        mutation = re.search(r"^- Production mutation observation:\s*`(none_proven|occurred|may_have_occurred|not_applicable)`", text, re.MULTILINE)
        lease = re.search(r"^- Product release identity lease evidence:\s*(\S.+)$", text, re.MULTILINE)
        recovery = re.search(r"^- Recovery Owner / next action:\s*(\S.+)$", text, re.MULTILINE)
        bound_rc = rc_records.get(rc.group(1)) if rc else None
        bound_version = re.search(r"^> Harness version:\s*`([^`]+)`\s*$", bound_rc[1], re.MULTILINE) if bound_rc else None
        lease_free = bool(bound_version and SEMVER.fullmatch(bound_version.group(1))
                          and uses_lease_free_contract(bound_version.group(1)))
        if not all((subject, policy, rc, sequence, previous, transition, kind, actor, guard, mutation, recovery)) or (not lease_free and not lease):
            add("AHV-PRODUCT-RELEASE-003", "error", relative, "incomplete Product Release Identity Event", "bind exact version/tag/Policy/RC, chain transition, authority, mutation, recovery and version-appropriate historical evidence")
            continue
        from_state, to_state = transition.groups()
        if allowed.get((from_state, to_state)) != kind.group(1):
            add("AHV-PRODUCT-RELEASE-004", "error", relative, f"invalid Product release identity transition/kind {from_state}->{to_state}/{kind.group(1)}", "use the canonical append-only Product release state machine")
        if mutation.group(1) not in mutation_by_transition.get((from_state, to_state), set()):
            add("AHV-PRODUCT-RELEASE-007", "error", relative, f"Production mutation observation {mutation.group(1)} contradicts transition {from_state}->{to_state}", "bind transition-specific observed provider/deployment evidence")
        unresolved = re.compile(r"\{\{|<<|\b(?:tbd|todo|pending|unresolved)\b", re.IGNORECASE)
        if any(unresolved.search(value) for value in (*subject.groups(), policy.group(1), rc.group(1), actor.group(1), guard.group(1), lease.group(1) if lease else "historical_field_not_required", recovery.group(1))):
            add("AHV-PRODUCT-RELEASE-003", "error", relative, "unresolved Product release identity field", "resolve every identity/authority/evidence field")
        rc_record = rc_records.get(rc.group(1))
        rc_valid = False
        if rc_record:
            rc_path, rc_text = rc_record
            rc_classification = re.search(r"^> Candidate classification:\s*`final`\s*$", rc_text, re.MULTILINE)
            rc_state = re.search(r"^> Product release version state:\s*`reserved_unpublished`\s*$", rc_text, re.MULTILINE)
            rc_version = re.search(r"^> Intended Product version:\s*`([^`\s]+)`\s*$", rc_text, re.MULTILINE)
            rc_tag = re.search(r"^> Proposed Product release tag:\s*`([^`\s]+)`\s*$", rc_text, re.MULTILINE)
            rc_policy = re.search(r"^> Product Release Policy ID / revision SHA-256:\s*`([^`\s]+)`\s*/\s*`([0-9a-f]{64})`\s*$", rc_text, re.MULTILINE)
            rc_valid = bool(
                digest(rc_path) == rc.group(2) and rc_classification and rc_state
                and rc_version and rc_version.group(1) == subject.group(1)
                and rc_tag and rc_tag.group(1) == subject.group(2)
                and rc_policy and rc_policy.groups() == policy.groups()
            )
        if not rc_valid:
            add("AHV-PRODUCT-RELEASE-007", "error", relative, "identity event does not bind the exact existing frozen final RC bytes and matching version/tag/Policy", "persist the complete final RC and atomically bind its exact ID/digest")
        events.append({"path":path, "relative":relative, "version":subject.group(1), "tag":subject.group(2), "policy":policy.groups(), "rc":rc.groups(), "sequence":int(sequence.group(1)), "previous":previous.group(1), "from":from_state, "to":to_state})

    version_tags: dict[str, str] = {}
    tag_versions: dict[str, str] = {}
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for event in events:
        if event["version"] in version_tags and version_tags[event["version"]] != event["tag"]:
            add("AHV-PRODUCT-RELEASE-005", "error", event["relative"], "one Product version maps to multiple release tags", "retain one immutable version/tag identity chain")
        if event["tag"] in tag_versions and tag_versions[event["tag"]] != event["version"]:
            add("AHV-PRODUCT-RELEASE-005", "error", event["relative"], "one Product release tag maps to multiple versions", "retain one immutable version/tag identity chain")
        version_tags[event["version"]] = event["tag"]; tag_versions[event["tag"]] = event["version"]
        groups.setdefault((event["version"], event["tag"]), []).append(event)
    for identity, chain in groups.items():
        chain.sort(key=lambda item: item["sequence"])
        if chain[0]["sequence"] != 1 or chain[0]["previous"] != "genesis" or chain[0]["from"] != "none":
            add("AHV-PRODUCT-RELEASE-006", "error", chain[0]["relative"], f"Product release identity {identity} lacks one valid genesis reservation", "start one sequence-1 genesis reservation per version/tag")
        terminal_seen = False
        for index, current in enumerate(chain):
            if terminal_seen:
                add("AHV-PRODUCT-RELEASE-006", "error", current["relative"], "event follows terminal published/skipped state", "retain terminal identity state")
            if index:
                prior = chain[index - 1]
                if current["sequence"] != prior["sequence"] + 1 or current["previous"] != digest(prior["path"]) or current["from"] != prior["to"]:
                    add("AHV-PRODUCT-RELEASE-006", "error", current["relative"], "Product release identity event chain is forked, non-contiguous, or state-inconsistent", "bind the exact immediate predecessor and contiguous state")
                if current["policy"] != prior["policy"]:
                    add("AHV-PRODUCT-RELEASE-005", "error", current["relative"], "Product Release Policy identity changed inside one version chain", "retain the reservation's exact Policy revision")
                if current["from"] != "reserved_unpublished" or current["to"] != "reserved_unpublished":
                    if current["rc"] != prior["rc"]:
                        add("AHV-PRODUCT-RELEASE-005", "error", current["relative"], "RC ownership changed outside reservation_transfer", "transfer ownership only while reserved and before Production mutation")
            terminal_seen = current["to"] in {"published", "skipped"}


def validate_effort_profile(relative: str, text: str, is_template: bool, identifier: str | None, add) -> None:
    if is_template:
        return
    if DIRECT_RUN_BLOCK.search(text):
        return
    # Run identity must not depend on one removable metadata line: otherwise a
    # malformed or adversarial Run could evade every effort-budget check by
    # deleting `Run kind`.  Event records are evidence, not mutable Run contracts.
    run_identity = bool(identifier and "-RUN-" in identifier and "-EVENT-" not in identifier)
    run_heading = bool(re.search(r"^# Execution Run\s*$", text, re.MULTILINE))
    is_run = bool(re.search(r"^> Run kind:", text, re.MULTILINE) or run_heading or run_identity)
    is_package = bool(identifier and "-WP-" in identifier and re.search(r"^> Work status:", text, re.MULTILINE))
    if not (is_run or is_package):
        return
    version_match = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
    scope_applicable = not version_match or not SEMVER.fullmatch(version_match.group(1)) or semver_tuple(version_match.group(1)) >= ADMISSION_MIN_VERSION
    if is_run and scope_applicable:
        scope_fields = ("Required outcomes", "Minimum sufficient change", "Allowed path families", "Prohibited outcomes", "Scope expansion authority/reference or `none`")
        missing_scope = [field for field in scope_fields if not re.search(rf"^- {re.escape(field)}:\s*\S.+$", text, re.MULTILINE)]
        if missing_scope:
            add("AHV-SCOPE-001", "error", relative, f"Execution Run lacks machine-readable Scope Lock fields: {missing_scope}", "bind requested outcomes, minimum change, allowed paths, non-goals, and expansion authority before activation")
        exact_scope = {
            "Change-to-outcome evidence": "required_at_verification",
            "Adjacent findings disposition": "follow_up_only",
            "Scope expansion rule": "stop_and_amend_before_mutation",
        }
        invalid_scope = [field for field, value in exact_scope.items() if not re.search(rf"^- {re.escape(field)}:\s*`?{re.escape(value)}`?\s*$", text, re.MULTILINE)]
        if invalid_scope:
            add("AHV-SCOPE-002", "error", relative, f"Execution Run permits implicit breadth or lacks verification mapping: {invalid_scope}", "require path-to-outcome evidence, follow-up-only adjacency, and stop-before-expansion semantics")
    classification = re.search(r"^> Decision class / classification trigger ID:\s*`?(D[0-3])`?\s*/\s*`?([a-z0-9_]+)`?\s*$", text, re.MULTILINE)
    evidence = re.search(r"^> Classification evidence:\s*(\S.+)$", text, re.MULTILINE)
    if not classification or not evidence:
        add("AHV-BUDGET-001", "error", relative, "Work/Run lacks exact decision class, trigger ID, or classification evidence", "bind the lowest class and concrete evidence before authorization")
        return
    decision_class, trigger = classification.groups()
    if trigger not in CLASS_TRIGGERS[decision_class]:
        add("AHV-BUDGET-002", "error", relative, f"trigger {trigger} is not valid for {decision_class}", "use a recognized concrete trigger or lower the class")
    if not is_run:
        return
    fields = {
        "implementers": "Creator/implementer count",
        "reviewers": "Independent reviewer count",
        "active": "Max active Agents total",
        "initial_reviews": "Initial full-review count",
        "corrections": "Consolidated correction-pass ceiling",
        "closures": "Targeted closure-review ceiling",
    }
    values: dict[str, int] = {}
    for key, label in fields.items():
        match = re.search(rf"^- {re.escape(label)}:\s*`?([0-9]+)`?\s*$", text, re.MULTILINE)
        if match:
            values[key] = int(match.group(1))
    escalation = re.search(r"^- Escalation authority/reference or `none`:\s*(\S.+)$", text, re.MULTILINE)
    override = re.search(r"^- Effort-profile override or `none`:\s*(\S.+)$", text, re.MULTILINE)
    if set(values) != set(fields) or not escalation or not override:
        add("AHV-BUDGET-003", "error", relative, "Execution Run lacks complete machine-readable Agent/review/correction ceilings or escalation authority", "populate every class-bound budget field")
        return
    profile = EFFORT_PROFILES[decision_class]
    if (version_match and SEMVER.fullmatch(version_match.group(1))
            and semver_tuple(version_match.group(1)) >= LEAN_WORKING_TEAM_MIN_VERSION
            and decision_class != "D0"):
        # Current Mission/narrative controls keep their format, but not an obsolete team count.
        profile = {**EFFORT_PROFILES["D1"], "active": 3}
    proportionate = bool(version_match and SEMVER.fullmatch(version_match.group(1))
                         and semver_tuple(version_match.group(1)) >= PROPORTIONATE_EXECUTION_MIN_VERSION)
    if proportionate:
        # Mission total is validated in its owner block; no extra local correction/review ceiling.
        profile = {**profile, "corrections": values["corrections"], "closures": values["closures"]}
    invalid_profile = values["implementers"] != profile["implementers"] or values["reviewers"] != profile["reviewers"] or values["initial_reviews"] != profile["initial_reviews"] or any(values[key] > profile[key] for key in ("active", "corrections", "closures"))
    override_value = override.group(1).strip().strip("`")
    if invalid_profile and not re.fullmatch(r"human-approved:[A-Za-z0-9._-]+", override_value):
        add("AHV-BUDGET-004", "error", relative, f"{decision_class} budget {values} exceeds or changes mandatory topology {profile}", "use the class profile or record a separate Human-approved override contract")
    reserve_patterns = {
        "reserve": r"^- Autonomous Mission correction reserve or `none`:\s*`?(none|[0-9]+)`?\s*$",
        "authority": r"^- Reserve allocation authority or `none`:\s*`?([^`\n]+)`?\s*$",
        "activation": r"^- Reserve activation rule or `none`:\s*`?([^`\n]+)`?\s*$",
        "exhaustion": r"^- Reserve exhaustion rule or `none`:\s*`?([^`\n]+)`?\s*$",
    }
    reserve_occurrences = {
        key: list(re.finditer(pattern, text, re.MULTILINE))
        for key, pattern in reserve_patterns.items()
    }
    reserve_fields = {
        key: matches[0] if matches else None
        for key, matches in reserve_occurrences.items()
    }
    if any(reserve_fields.values()):
        reserve_valid = all(reserve_fields.values()) and all(len(matches) == 1 for matches in reserve_occurrences.values())
        if reserve_valid:
            reserve = reserve_fields["reserve"].group(1)
            authority = reserve_fields["authority"].group(1).strip()
            activation = reserve_fields["activation"].group(1).strip()
            exhaustion = reserve_fields["exhaustion"].group(1).strip()
            reserve_valid = (
                (reserve == "none" and authority == activation == exhaustion == "none")
                or (
                    reserve != "none" and int(reserve) > 0
                    and authority == "mission_lead_same_scope"
                    and activation == "new_evidence_hypothesis_and_remaining_total_budget"
                    and exhaustion == "checkpoint_and_escalate"
                    and re.fullmatch(r"human-approved:[A-Za-z0-9._-]+", override_value) is not None
                )
            )
        if not reserve_valid:
            add("AHV-BUDGET-005", "error", relative, "Mission correction reserve is incomplete or can reset authority/budget", "bind a finite Human-approved reserve to same-scope Lead allocation, new evidence, cumulative total budget, and checkpoint/escalation on exhaustion")
    version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
    mission = re.search(r"^- Mission ID or `none`:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
    prospective_non_mission = bool(
        version
        and SEMVER.fullmatch(version.group(1))
        and semver_tuple(version.group(1)) >= CORRECTION_AUTHORITY_MIN_VERSION
        and mission
        and mission.group(1).strip().lower() in {"none", "not_applicable"}
    )
    if prospective_non_mission and (
        any(len(matches) != 1 for matches in reserve_occurrences.values())
        or reserve_fields["reserve"].group(1) != "none"
        or any(reserve_fields[field].group(1).strip() != "none" for field in ("authority", "activation", "exhaustion"))
    ):
        add("AHV-CORRECTION-003", "error", relative, "prospective non-Mission Run omits or declares Mission correction-reserve authority", "retain all four reserve fields and set each exactly to none, or use a complete Human-approved Mission envelope")


def parse_correction_amendment(relative: str, text: str, identifier: str | None, add) -> dict[str, Any] | None:
    blocks = CORRECTION_AMENDMENT_BLOCK.findall(text)
    if not blocks:
        return None
    if len(blocks) != 1:
        add("AHV-CORRECTION-001", "error", relative, f"Run contains {len(blocks)} correction-amendment projections", "retain one exact exceptional Human amendment or omit the block")
        return None
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as error:
        add("AHV-CORRECTION-001", "error", relative, f"correction-amendment JSON is invalid: {error}", "use one valid compact amendment projection")
        return None

    required = {
        "schema_version", "amendment_id", "authority_ref", "parent_run_id",
        "parent_run_sha256", "budget_lineage_id", "additional_allocation",
        "purpose_ids", "outcomes", "path_prefixes", "environments",
        "external_actions", "terminal_condition",
    }
    problems: list[str] = []
    if not isinstance(value, dict) or set(value) != required:
        problems.append("fields")
        value = value if isinstance(value, dict) else {}
    version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
    if not version or not SEMVER.fullmatch(version.group(1)) or semver_tuple(version.group(1)) < CORRECTION_AUTHORITY_MIN_VERSION:
        problems.append("Harness version")
    for field in ("amendment_id", "parent_run_id", "budget_lineage_id"):
        if not isinstance(value.get(field), str) or re.fullmatch(r"[A-Z0-9][A-Z0-9._-]+", value[field]) is None:
            problems.append(field)
    authority_ref = value.get("authority_ref")
    if not isinstance(authority_ref, str) or re.fullmatch(r"human-approved:[A-Za-z0-9._-]+", authority_ref) is None:
        problems.append("authority_ref")
    if HEX64.fullmatch(str(value.get("parent_run_sha256", ""))) is None:
        problems.append("parent_run_sha256")
    allocation = value.get("additional_allocation")
    if not isinstance(allocation, dict) or set(allocation) != CONVERGENCE_COUNTERS or any(isinstance(item, bool) or not isinstance(item, int) or item <= 0 for item in allocation.values()):
        problems.append("additional_allocation")
    amendment_sets: dict[str, set[str]] = {}
    for field in ("purpose_ids", "outcomes", "path_prefixes", "environments", "external_actions"):
        if not unique_strings(value.get(field)):
            problems.append(field)
            amendment_sets[field] = set()
        else:
            amendment_sets[field] = set(value[field])
    if unique_strings(value.get("path_prefixes")):
        try:
            for prefix in value["path_prefixes"]:
                safe_relative(prefix)
        except ValueError:
            problems.append("path_prefixes")
    if value.get("terminal_condition") != "exhaustion_or_purpose_closure":
        problems.append("terminal_condition")

    authority_line = re.search(r"^> Decision Authority / Final Approver / Human Gate Owner:\s*(\S.+)$", text, re.MULTILINE)
    if not authority_line or not isinstance(authority_ref, str) or authority_ref not in authority_line.group(1):
        problems.append("visible authority binding")

    projections = ADMISSION_PROJECTION_BLOCK.findall(text)
    if len(projections) != 1:
        problems.append("ordinary Admission Projection")
    else:
        try:
            projection = json.loads(projections[0])
        except json.JSONDecodeError:
            projection = {}
            problems.append("Admission Projection JSON")
        raw_scope = projection.get("scope_lock", {}) if isinstance(projection, dict) else {}
        raw_external = projection.get("external_actions", {}) if isinstance(projection, dict) else {}
        raw_context = projection.get("context", {}) if isinstance(projection, dict) else {}
        raw_authority = projection.get("authority", {}) if isinstance(projection, dict) else {}
        scope = raw_scope if isinstance(raw_scope, dict) else {}
        external = raw_external if isinstance(raw_external, dict) else {}
        context = raw_context if isinstance(raw_context, dict) else {}
        authority = raw_authority if isinstance(raw_authority, dict) else {}
        if not all(isinstance(item, dict) for item in (raw_scope, raw_external, raw_context, raw_authority)):
            problems.append("Admission containment object shape")
        if authority.get("decision_authority_ref") != authority_ref:
            problems.append("Admission authority containment")
        required_outcomes = scope.get("required_outcomes")
        if not unique_strings(required_outcomes):
            problems.append("Admission required-outcome shape")
            required_outcomes = []
        if not set(required_outcomes).issubset(amendment_sets["outcomes"]):
            problems.append("outcome containment")
        allowed_paths = scope.get("allowed_paths")
        if not unique_strings(allowed_paths):
            problems.append("Admission allowed-path shape")
            allowed_paths = []
        for path in allowed_paths:
            if not any(path == prefix or path.startswith(prefix.rstrip("/") + "/") for prefix in amendment_sets["path_prefixes"]):
                problems.append("path containment")
                break
        environment = context.get("environment_disposition")
        if not isinstance(environment, str) or not environment:
            problems.append("Admission environment shape")
        elif environment not in amendment_sets["environments"]:
            problems.append("environment containment")
        allowed_actions = external.get("allowed")
        if not unique_strings(allowed_actions):
            problems.append("Admission external-action shape")
            allowed_actions = []
        if not set(allowed_actions).issubset(amendment_sets["external_actions"]):
            problems.append("external-action containment")

    if problems:
        add("AHV-CORRECTION-001", "error", relative, f"exceptional Human amendment is incomplete or mismatched: {sorted(set(problems))}", "bind one finite parent/digest/lineage/purpose/scope-contained amendment to the exact Human-authorized Run Contract")
        return None
    return value


def validate_convergence_budgets(markdown_records: dict[str, tuple[Path, str, bool]], ids: dict[str, str], add) -> None:
    parsed: dict[str, dict[str, Any]] = {}
    required = {
        "schema_version", "budget_lineage_id", "predecessor_run_id", "progress_step_percent",
        "drift_checkpoints_percent", "independent_drift_checkpoints_percent", "critical_quorum",
        "critical_chain_remediation_limit", "third_critical_action", "post_convergence_recurrence",
        "prior_consumption", "current_run_allocation", "lineage_total_ceiling",
    }
    exact = {
        "schema_version": "1",
        "progress_step_percent": 10,
        "drift_checkpoints_percent": [20, 40, 60, 80, 100],
        "independent_drift_checkpoints_percent": [40, 80],
        "critical_quorum": {"D0": "reclassify", "D1": "2_of_2", "D2": "2_of_3", "D3": "2_of_3"},
        "critical_chain_remediation_limit": 3,
        "third_critical_action": "drift_check_and_convergence_quorum",
        "post_convergence_recurrence": "checkpoint_and_escalate",
    }

    for relative, (_path, text, is_template) in markdown_records.items():
        if is_template:
            continue
        identifier_match = ARTIFACT_ID.search(text)
        identifier = identifier_match.group(1) if identifier_match else None
        is_run = bool(identifier and "-RUN-" in identifier and "-EVENT-" not in identifier) or bool(re.search(r"^> Run kind:", text, re.MULTILINE)) or bool(re.search(r"^# Execution Run\s*$", text, re.MULTILINE))
        if not is_run:
            continue
        amendment = parse_correction_amendment(relative, text, identifier, add)
        version_match = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
        if not version_match or not SEMVER.fullmatch(version_match.group(1)):
            continue  # legacy contracts retain their pinned release behavior
        version = tuple(int(part) for part in version_match.group(1).split("+", 1)[0].split("-", 1)[0].split("."))
        if version < (1, 0, 9) or version >= PROPORTIONATE_EXECUTION_MIN_VERSION:
            continue  #1.5 uses the existing Mission reserve/checkpoint, not parallel convergence counters.
        blocks = CONVERGENCE_BUDGET_BLOCK.findall(text)
        if len(blocks) != 1:
            add("AHV-BUDGET-006", "error", relative, f"Harness >=1.0.9 Run requires exactly one convergence-budget projection; observed {len(blocks)}", "instantiate one exact cumulative budget-lineage block")
            continue
        try:
            value = json.loads(blocks[0])
        except json.JSONDecodeError:
            add("AHV-BUDGET-006", "error", relative, "convergence-budget JSON is invalid", "use valid exact JSON")
            continue
        expected_fields = exact
        if version >= LEAN_WORKING_TEAM_MIN_VERSION:
            expected_fields = {**exact, "critical_quorum": {
                "D0": "reclassify", **{level: "2_of_2_or_authorized_2_of_3" for level in ("D1", "D2", "D3")},
            }}
        if not isinstance(value, dict) or set(value) != required or any(value.get(key) != expected for key, expected in expected_fields.items()):
            add("AHV-BUDGET-006", "error", relative, "convergence cadence, quorum, causal-chain limit, or schema is incomplete/weakened", "use the exact released convergence-budget schema and constants")
            continue
        lineage = value.get("budget_lineage_id")
        predecessor = value.get("predecessor_run_id")
        counters_ok = True
        for field in ("prior_consumption", "current_run_allocation", "lineage_total_ceiling"):
            counters = value.get(field)
            if not isinstance(counters, dict) or set(counters) != CONVERGENCE_COUNTERS or any(isinstance(item, bool) or not isinstance(item, int) or item < 0 for item in counters.values()):
                counters_ok = False
        identity_ok = isinstance(lineage, str) and re.fullmatch(r"[A-Z0-9][A-Z0-9._-]+", lineage) is not None and isinstance(predecessor, str) and (predecessor == "none" or re.fullmatch(r"[A-Z0-9][A-Z0-9._-]+", predecessor) is not None)
        if not counters_ok or not identity_ok:
            add("AHV-BUDGET-006", "error", relative, "budget lineage identity or typed nonnegative counters are invalid", "use stable uppercase IDs and exact nonnegative integer counters")
            continue
        prior = value["prior_consumption"]; current = value["current_run_allocation"]; total = value["lineage_total_ceiling"]
        arithmetic_ok = current["agent_activations"] > 0 and all(prior[key] + current[key] <= total[key] for key in CONVERGENCE_COUNTERS)
        if predecessor == "none":
            arithmetic_ok = arithmetic_ok and all(prior[key] == 0 for key in CONVERGENCE_COUNTERS)
        if not arithmetic_ok:
            add("AHV-BUDGET-006", "error", relative, "prior plus current allocation exceeds lineage total or a genesis Run has nonzero prior consumption", "reduce allocation or obtain an explicit Human-approved total-budget amendment")
            continue
        if identifier:
            parsed[identifier] = {"relative": relative, "value": value, "amendment": amendment}

    amendment_ids: dict[tuple[str, str], list[dict[str, Any]]] = {}
    amendment_parent_edges: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in parsed.values():
        amendment = record["amendment"]
        if amendment is None:
            continue
        amendment_ids.setdefault(
            (amendment["budget_lineage_id"], amendment["amendment_id"]), []
        ).append(record)
        amendment_parent_edges.setdefault(
            (amendment["budget_lineage_id"], amendment["parent_run_id"]), []
        ).append(record)
    for records in amendment_ids.values():
        if len(records) > 1:
            for record in records:
                add("AHV-CORRECTION-001", "error", record["relative"], "Human amendment ID adds allocation more than once in one budget lineage", "use each Human amendment ID on exactly one expansion edge")
    for records in amendment_parent_edges.values():
        if len(records) > 1:
            for record in records:
                add("AHV-CORRECTION-001", "error", record["relative"], "multiple Human amendments branch from the same parent budget edge", "serialize amendments from the then-current successor so cumulative authority remains unambiguous")

    for identifier, record in parsed.items():
        amendment = record["amendment"]
        if amendment is None:
            continue
        parent_id = amendment["parent_run_id"]
        parent = parsed.get(parent_id)
        parent_relative = ids.get(parent_id)
        if (
            not parent
            or parent_relative != parent["relative"]
            or record["value"]["predecessor_run_id"] != parent_id
            or amendment["parent_run_sha256"] != digest(markdown_records[parent_relative][0])
            or amendment["budget_lineage_id"] != record["value"]["budget_lineage_id"]
        ):
            add("AHV-CORRECTION-001", "error", record["relative"], "Human amendment parent digest or budget lineage is missing/mismatched", "bind the exact existing parent Run Contract and unchanged cumulative lineage")

    for identifier, record in parsed.items():
        value = record["value"]; predecessor = value["predecessor_run_id"]
        if predecessor == "none":
            continue
        prior_record = parsed.get(predecessor)
        if not prior_record or ids.get(predecessor) != prior_record["relative"] or predecessor == identifier:
            add("AHV-BUDGET-006", "error", record["relative"], f"budget predecessor {predecessor!r} is missing, legacy, or self-referential", "reference the immediate governed predecessor Run")
            continue
        prior_value = prior_record["value"]
        carried = {key: prior_value["prior_consumption"][key] + prior_value["current_run_allocation"][key] for key in CONVERGENCE_COUNTERS}
        same_lineage = value["budget_lineage_id"] == prior_value["budget_lineage_id"]
        carried_ok = value["prior_consumption"] == carried
        totals_equal = value["lineage_total_ceiling"] == prior_value["lineage_total_ceiling"]
        amendment = record["amendment"]
        amended_total_ok = False
        if amendment is not None and amendment["parent_run_id"] == predecessor:
            delta = {
                key: value["lineage_total_ceiling"][key] - prior_value["lineage_total_ceiling"][key]
                for key in CONVERGENCE_COUNTERS
            }
            amended_total_ok = (
                delta == amendment["additional_allocation"]
                and all(amount > 0 for amount in delta.values())
            )
        total_authority_ok = totals_equal if amendment is None else amended_total_ok
        if not same_lineage or not carried_ok or not total_authority_ok:
            add("AHV-BUDGET-006", "error", record["relative"], "successor Run resets or disagrees with predecessor lineage, cumulative consumption, or total ceilings", "carry predecessor consumption and totals, or bind one exact Human amendment whose allocation equals the finite ceiling increase")


def validate_mission_runtime(relative: str, text: str, is_template: bool, add, run_version: str | None = None) -> None:
    if is_template:
        return
    mission = re.search(r"^- Mission ID or `none`:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
    if not mission:
        return  # legacy/pinned contracts do not adopt Mission policy retroactively
    mission_id = mission.group(1).strip()
    if mission_id.lower() in {"none", "not_applicable"}:
        return
    if not re.fullmatch(r"[A-Z0-9][A-Z0-9._-]+", mission_id):
        add("AHV-MISSION-001", "error", relative, f"invalid Mission ID {mission_id!r}", "use one stable uppercase Mission ID or explicit none")
    if re.search(r"^> Run kind:", text, re.MULTILINE):
        labels = (
            "Human Mission decision / Decision Authority",
            "Required outcomes and observable completion evidence",
            "Invariants", "Non-goals / prohibited outcomes",
            "Exact ordered item IDs or bounded instantiation rules (outcome IDs, semantic owners, path families, environments/actions, dependencies, class ceiling, maximum item count)",
            "Lead-delegated decisions / non-Human Package Decision Authority / reserved Decision or Human Authority",
            "Per-item and total Agent/review/correction/working-window/external-action/observable-cost budgets",
            "Integration boundary / final Mission stop",
            "Package-boundary checkpoint, continuation evidence, next-item selection, and stop/escalation guard",
        )
        missing = [label for label in labels if not re.search(rf"^- {re.escape(label)}:\s*(?!none\s*$|not_applicable\s*$|\{{\{{)\S.+$", text, re.MULTILINE | re.IGNORECASE)]
        if missing:
            add("AHV-MISSION-002", "error", relative, f"Mission Run lacks complete authority/budget/continuation fields: {missing}", "bind every canonical Mission field before authorization")
    if "## Mission Continuation Guard" in text:
        readable = bool(run_version and SEMVER.fullmatch(run_version) and semver_tuple(run_version) >= (1, 5, 1))
        intent_label = "Pre-mutation intent reference and permitted outcome/owner/path/environment/action set" if readable else "Pre-mutation intent digest and permitted outcome/owner/path/environment/action set"
        mapping_label = "Actual changed-path to Package-and-Mission outcome mapping reference" if readable else "Actual changed-path to Package-and-Mission outcome mapping digest"
        labels = (
            "Mission / Run / current Package revisions and digests",
            intent_label,
            mapping_label,
            "Current acceptance/regression/integration evidence and invariant result",
            "Reversible assumptions, evidence, validation triggers, fallbacks, and authority boundaries or `none`",
            "Findings/dispositions and adjacent follow-ups with owner/trigger or `none`",
            "Attempts and remaining Package/Mission Agent/review/correction/time/external-action/cost budgets",
            "Dependency/baseline drift and next eligible item", "Decision guard evidence / exact escalation need",
        )
        missing = [label for label in labels if not re.search(rf"^- {re.escape(label)}:\s*(?!\{{\{{)\S.+$", text, re.MULTILINE)]
        decision = re.search(r"^- Continuation decision `continue \| stop \| escalate \| complete`:\s*`?(continue|stop|escalate|complete)`?\s*$", text, re.MULTILINE)
        bindings = re.findall(rf"^- (?:{re.escape(intent_label)}|{re.escape(mapping_label)}):\s*([^\n]+)$", text, re.MULTILINE)
        invalid_binding = len(bindings) != 2 or any(
            not value.strip() or value.strip().lower() in {"none", "not_applicable", "unknown"}
            or (not readable and not re.search(r"[0-9a-f]{64}", value))
            for value in bindings
        )
        if missing or not decision or invalid_binding:
            kind = "readable intent/path references" if readable else "intent/path digests"
            add("AHV-MISSION-003", "error", relative, f"Mission checkpoint is incomplete; missing={missing}, decision={bool(decision)}, binding_fields={len(bindings)}", f"bind exact revisions, {kind}, evidence, assumptions, findings, budgets, dependency, next item, and one allowed decision")


def validate_mission_bindings(root: Path, records: dict[str, tuple[Path, str, bool]], id_paths: dict[str, Path], add) -> None:
    contracts: dict[str, dict[str, Any]] = {}
    proportionate_runs: set[str] = set()
    correction_observations: dict[str, list[tuple[int, int, str]]] = {}
    common_contract = {"schema_version", "mission_id", "mode", "total_budget"}
    exact_fields = common_contract | {"ordered_items"}
    bounded_fields = common_contract | {"bounded_instantiation"}
    item_fields = {"id", "contract_sha256", "outcomes", "semantic_owners", "path_prefixes", "environments", "external_actions", "decision_class", "max_agents", "max_corrections"}
    bounded_rule_fields = {"package_id_prefix", "outcomes", "semantic_owners", "path_prefixes", "environments", "external_actions", "dependency_rule", "package_decision_authority", "class_ceiling", "max_items", "max_agents_per_item", "max_corrections_per_item"}
    package_fields = {"schema_version", "mission_id", "run_id", "instantiation_index", "depends_on", "outcomes", "semantic_owners", "path_prefixes", "environments", "external_actions", "decision_class", "decision_authority", "max_agents", "max_corrections"}
    checkpoint_fields = {"schema_version", "mission_id", "run_id", "run_sha256", "package_id", "package_sha256", "instantiation_index", "decision_class", "outcomes", "semantic_owners", "changed_paths", "environments", "external_actions", "agent_activations_used", "corrections_used", "mission_agent_activations_remaining", "mission_corrections_remaining", "next_item", "next_item_sha256", "decision"}
    class_rank = {"D0": 0, "D1": 1, "D2": 2, "D3": 3}

    def string_set(value: Any) -> bool:
        return isinstance(value, list) and bool(value) and all(isinstance(item, str) and item for item in value) and len(value) == len(set(value))

    def safe_prefixes(value: Any) -> bool:
        if not string_set(value): return False
        try:
            for prefix in value: safe_relative(prefix)
        except ValueError:
            return False
        return True

    for relative, (path, text, is_template) in records.items():
        if is_template or not re.search(r"^> Run kind:", text, re.MULTILINE): continue
        visible = re.search(r"^- Mission ID or `none`:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
        if not visible or visible.group(1).strip().lower() in {"none", "not_applicable"}: continue
        blocks = MISSION_CONTRACT_BLOCK.findall(text)
        if len(blocks) != 1:
            add("AHV-MISSION-004", "error", relative, f"non-none Mission Run requires exactly one contract projection; observed {len(blocks)}", "retain one matching exact or bounded mission-contract JSON block"); continue
        try: data = json.loads(blocks[0])
        except json.JSONDecodeError:
            add("AHV-MISSION-004", "error", relative, "Mission contract JSON is invalid", "use valid exact mission-contract JSON"); continue
        artifact = ARTIFACT_ID.search(text); run_id = artifact.group(1) if artifact else ""
        budget = data.get("total_budget", {}) if isinstance(data, dict) else {}
        common_valid = isinstance(data, dict) and data.get("schema_version") == "1" and isinstance(data.get("mission_id"), str) and data.get("mission_id") == visible.group(1).strip() and isinstance(data.get("mode"), str) and data.get("mode") in {"exact_ordered_items", "bounded_instantiation"} and isinstance(budget, dict) and set(budget) == {"max_agent_activations", "max_corrections"} and all(isinstance(value, int) and not isinstance(value, bool) and value >= 0 for value in budget.values())
        valid = common_valid and run_id != ""
        if valid and data["mode"] == "exact_ordered_items":
            ordered_items = data.get("ordered_items")
            valid = set(data) == exact_fields and isinstance(ordered_items, list) and bool(ordered_items)
            ids: list[str] = []
            for item in ordered_items if isinstance(ordered_items, list) else []:
                item_valid = isinstance(item, dict) and set(item) == item_fields and isinstance(item.get("id"), str) and item["id"] and HEX64.fullmatch(str(item.get("contract_sha256", ""))) is not None and all(string_set(item.get(field)) for field in ("outcomes", "semantic_owners", "environments", "external_actions")) and safe_prefixes(item.get("path_prefixes")) and isinstance(item.get("decision_class"), str) and item.get("decision_class") in class_rank and all(isinstance(item.get(field), int) and not isinstance(item[field], bool) and item[field] >= 0 for field in ("max_agents", "max_corrections"))
                valid = valid and item_valid
                if isinstance(item, dict) and isinstance(item.get("id"), str): ids.append(item["id"])
            valid = valid and len(ids) == len(set(ids))
        elif valid:
            rule = data.get("bounded_instantiation")
            valid = set(data) == bounded_fields and isinstance(rule, dict) and set(rule) == bounded_rule_fields and isinstance(rule.get("package_id_prefix"), str) and bool(rule["package_id_prefix"]) and all(string_set(rule.get(field)) for field in ("outcomes", "semantic_owners", "environments", "external_actions")) and safe_prefixes(rule.get("path_prefixes")) and rule.get("dependency_rule") == "sequential" and isinstance(rule.get("package_decision_authority"), str) and bool(rule["package_decision_authority"]) and isinstance(rule.get("class_ceiling"), str) and rule.get("class_ceiling") in class_rank and all(isinstance(rule.get(field), int) and not isinstance(rule[field], bool) and rule[field] >= 1 for field in ("max_items", "max_agents_per_item", "max_corrections_per_item"))
        if not valid:
            add("AHV-MISSION-004", "error", relative, "Mission contract must select one valid exact_ordered_items or bounded_instantiation schema", "bind typed safe sets, exact digests or bounded rules, class/item/Agent/correction ceilings, and finite totals"); continue
        version = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", text, re.MULTILINE)
        if version and SEMVER.fullmatch(version.group(1)) and semver_tuple(version.group(1)) >= PROPORTIONATE_EXECUTION_MIN_VERSION:
            proportionate_runs.add(run_id)
            mirrors = ([item["max_corrections"] for item in data["ordered_items"]]
                       if data["mode"] == "exact_ordered_items" else [data["bounded_instantiation"]["max_corrections_per_item"]])
            if any(value != budget["max_corrections"] for value in mirrors):
                add("AHV-MISSION-004", "error", relative, "1.5 item correction fields must reference the one Mission total", "use the existing Mission total, not an additional local ceiling or new reserve")
                continue
        contracts[run_id] = data

    package_projections: dict[str, list[tuple[str, Path, dict[str, Any]]]] = {}
    for relative, (path, text, is_template) in records.items():
        if is_template: continue
        blocks = MISSION_PACKAGE_BLOCK.findall(text)
        if not blocks: continue
        artifact = ARTIFACT_ID.search(text); package_id = artifact.group(1) if artifact else ""
        if len(blocks) != 1:
            add("AHV-MISSION-007", "error", relative, f"bounded Package requires exactly one projection; observed {len(blocks)}", "retain one typed mission-package projection"); continue
        try: projection = json.loads(blocks[0])
        except json.JSONDecodeError:
            add("AHV-MISSION-007", "error", relative, "Mission Package JSON is invalid", "use valid typed mission-package JSON"); continue
        scalar_valid = isinstance(projection, dict) and set(projection) == package_fields and projection.get("schema_version") == "1" and all(isinstance(projection.get(field), str) and projection[field] for field in ("mission_id", "run_id", "depends_on", "decision_class", "decision_authority")) and isinstance(projection.get("instantiation_index"), int) and not isinstance(projection["instantiation_index"], bool) and projection["instantiation_index"] >= 0 and all(isinstance(projection.get(field), int) and not isinstance(projection[field], bool) and projection[field] >= 0 for field in ("max_agents", "max_corrections"))
        valid = scalar_valid and projection.get("decision_class") in class_rank and all(string_set(projection.get(field)) for field in ("outcomes", "semantic_owners", "environments", "external_actions")) and safe_prefixes(projection.get("path_prefixes")) and bool(package_id)
        if not valid:
            add("AHV-MISSION-007", "error", relative, "Mission Package projection has malformed scalar/list/path/class fields", "bind typed authority, dependency, index, sets, class, and budgets"); continue
        package_projections.setdefault(projection["run_id"], []).append((package_id, path, projection))

    for relative, (path, text, is_template) in records.items():
        if is_template or "## Mission Continuation Guard" not in text: continue
        visible = re.search(r"^- Mission ID or `none`:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
        if not visible or visible.group(1).strip().lower() in {"none", "not_applicable"}: continue
        blocks = MISSION_CHECKPOINT_BLOCK.findall(text)
        if len(blocks) != 1:
            add("AHV-MISSION-005", "error", relative, f"non-none Mission checkpoint requires exactly one projection; observed {len(blocks)}", "retain one matching mission-checkpoint JSON block"); continue
        try: data = json.loads(blocks[0])
        except json.JSONDecodeError:
            add("AHV-MISSION-005", "error", relative, "Mission checkpoint JSON is invalid", "use valid exact mission-checkpoint JSON"); continue
        basic = isinstance(data, dict) and set(data) == checkpoint_fields and data.get("schema_version") == "1" and all(isinstance(data.get(field), str) and data[field] for field in ("mission_id", "run_id", "run_sha256", "package_id", "package_sha256", "decision_class", "next_item", "next_item_sha256", "decision")) and data.get("mission_id") == visible.group(1).strip() and data.get("decision") in {"continue", "stop", "escalate", "complete"} and data.get("decision_class") in class_rank and isinstance(data.get("instantiation_index"), int) and not isinstance(data["instantiation_index"], bool) and data["instantiation_index"] >= 0 and (HEX64.fullmatch(data["run_sha256"]) is not None) and (HEX64.fullmatch(data["package_sha256"]) is not None) and (data["next_item_sha256"] == "none" or HEX64.fullmatch(data["next_item_sha256"]) is not None)
        if not basic:
            add("AHV-MISSION-005", "error", relative, "Mission checkpoint schema, visible ID, index, class, or decision is invalid", "use the exact typed checkpoint schema and one allowed decision"); continue
        run_id = str(data["run_id"]); package_id = str(data["package_id"])
        if run_id not in contracts or run_id not in id_paths or package_id not in id_paths:
            add("AHV-MISSION-006", "error", relative, "Mission checkpoint references unknown Run or Package", "bind existing exact Run and Package artifacts"); continue
        contract = contracts[run_id]; run_path = id_paths[run_id]; package_path = id_paths[package_id]
        identity_valid = data["run_sha256"] == digest(run_path) and data["package_sha256"] == digest(package_path) and data["mission_id"] == contract["mission_id"]
        if not identity_valid:
            add("AHV-MISSION-006", "error", relative, "Mission/Run/Package identity or digest binding mismatch", "bind exact existing artifact digests and the Run Mission ID"); continue
        allowed: dict[str, Any]; expected_next = "none"; expected_next_sha = "none"; package_budget: tuple[int, int]
        if contract["mode"] == "exact_ordered_items":
            items = contract["ordered_items"]; by_id = {item["id"]: item for item in items}
            if package_id not in by_id or by_id[package_id]["contract_sha256"] != data["package_sha256"]:
                add("AHV-MISSION-006", "error", relative, "Package is not the exact digest-bound ordered Mission item", "use the predeclared exact Package ID/digest"); continue
            index = [item["id"] for item in items].index(package_id); allowed = by_id[package_id]
            expected_next = items[index + 1]["id"] if index + 1 < len(items) else "none"
            expected_next_sha = items[index + 1]["contract_sha256"] if index + 1 < len(items) else "none"
            mode_valid = data["instantiation_index"] == index and data["decision_class"] == allowed["decision_class"]
            package_budget = (allowed["max_agents"], allowed["max_corrections"])
        else:
            rule = contract["bounded_instantiation"]
            projections = package_projections.get(run_id, [])
            current = [entry for entry in projections if entry[0] == package_id]
            projection = current[0][2] if len(current) == 1 else {}
            mode_valid = len(current) == 1 and len(projections) <= rule["max_items"]
            indices: list[int] = []
            ordered: list[tuple[str, Path, dict[str, Any]]] = []
            for projected_id, projected_path, projected in projections:
                index_value = projected["instantiation_index"]
                indices.append(index_value)
                entry_valid = (
                    projected["mission_id"] == data["mission_id"]
                    and projected_id.startswith(rule["package_id_prefix"])
                    and index_value < rule["max_items"]
                    and projected["decision_authority"] == rule["package_decision_authority"]
                    and class_rank[projected["decision_class"]] <= class_rank[rule["class_ceiling"]]
                    and projected["max_agents"] <= rule["max_agents_per_item"]
                    and (projected["max_corrections"] == contract["total_budget"]["max_corrections"]
                         if run_id in proportionate_runs else projected["max_corrections"] <= rule["max_corrections_per_item"])
                )
                for field in ("outcomes", "semantic_owners", "environments", "external_actions"):
                    entry_valid = entry_valid and set(projected[field]).issubset(set(rule[field]))
                entry_valid = entry_valid and all(
                    any(prefix == allowed_prefix or prefix.startswith(allowed_prefix.rstrip("/") + "/") for allowed_prefix in rule["path_prefixes"])
                    for prefix in projected["path_prefixes"]
                )
                mode_valid = mode_valid and entry_valid
                ordered.append((projected_id, projected_path, projected))
            mode_valid = mode_valid and len(indices) == len(set(indices)) and sorted(indices) == list(range(len(indices)))
            ordered.sort(key=lambda entry: entry[2]["instantiation_index"])
            for position, (projected_id, _, projected) in enumerate(ordered):
                expected_dependency = "none" if position == 0 else ordered[position - 1][0]
                mode_valid = mode_valid and projected["depends_on"] == expected_dependency
            mode_valid = mode_valid and bool(projection) and projection.get("instantiation_index") == data["instantiation_index"] and projection.get("decision_class") == data["decision_class"]
            allowed = projection
            package_budget = (projection.get("max_agents", -1), projection.get("max_corrections", -1))
            next_entries = [entry for entry in ordered if entry[2]["instantiation_index"] == data["instantiation_index"] + 1]
            if len(next_entries) == 1:
                expected_next = next_entries[0][0]
                expected_next_sha = digest(next_entries[0][1])
        set_valid = mode_valid and all(string_set(data.get(field)) and set(data[field]).issubset(set(allowed.get(field, []))) for field in ("outcomes", "semantic_owners", "environments", "external_actions"))
        paths_valid = string_set(data.get("changed_paths"))
        if paths_valid:
            for changed in data["changed_paths"]:
                try: safe_relative(changed)
                except ValueError: paths_valid = False; continue
                if not any(changed == prefix or changed.startswith(prefix.rstrip("/") + "/") for prefix in allowed.get("path_prefixes", [])): paths_valid = False
        integer_fields = ("agent_activations_used", "corrections_used", "mission_agent_activations_remaining", "mission_corrections_remaining")
        budget_valid = all(isinstance(data.get(field), int) and not isinstance(data[field], bool) and data[field] >= 0 for field in integer_fields)
        if budget_valid:
            total = contract["total_budget"]
            budget_valid = data["agent_activations_used"] <= package_budget[0] and data["agent_activations_used"] + data["mission_agent_activations_remaining"] <= total["max_agent_activations"]
            if run_id in proportionate_runs:
                #1.5 corrections_used is cumulative Mission consumption, not this Package's usage.
                budget_valid = budget_valid and data["corrections_used"] + data["mission_corrections_remaining"] == total["max_corrections"]
                correction_observations.setdefault(run_id, []).append((data["instantiation_index"], data["corrections_used"], relative))
            else:
                budget_valid = budget_valid and data["corrections_used"] <= package_budget[1] and data["corrections_used"] + data["mission_corrections_remaining"] <= total["max_corrections"]
        next_valid = (
            (data["decision"] == "continue" and data["next_item"] == expected_next and data["next_item_sha256"] == expected_next_sha and expected_next != "none")
            or (data["decision"] == "complete" and data["next_item"] == "none" and data["next_item_sha256"] == "none" and expected_next == "none")
            or (data["decision"] in {"stop", "escalate"} and data["next_item"] == "none" and data["next_item_sha256"] == "none")
        )
        if not set_valid or not paths_valid or not budget_valid or not next_valid:
            add("AHV-MISSION-007", "error", relative, f"unauthorized Mission continuation mapping; mode={mode_valid}, sets={set_valid}, paths={paths_valid}, budget={budget_valid}, next={next_valid}", "keep digest-bound exact/bounded outcome/owner/path/environment/action/class/item/budget/dependency limits and next item")

    for observations in correction_observations.values():
        for index, used, relative in observations:
            if any(prior_index < index and prior_used > used for prior_index, prior_used, _ in observations):
                add("AHV-MISSION-007", "error", relative, "Mission correction consumption resets across items", "carry the cumulative observed consumption and remaining total; a new Package is not new authority")


def git_output(root: Path, arguments: list[str]) -> str:
    result = subprocess.run(
        ["git", *arguments], cwd=root, text=True, capture_output=True, check=False,
    )
    if result.returncode:
        raise ValueError(result.stderr.strip() or result.stdout.strip() or f"git {' '.join(arguments)} failed")
    return result.stdout


def changed_paths(output: str) -> set[str]:
    paths: set[str] = set()
    for line in output.splitlines():
        cells = line.split("\t")
        if len(cells) < 2:
            raise ValueError(f"invalid Git name-status row: {line!r}")
        for value in cells[1:]:
            safe_relative(value)
            paths.add(value)
    return paths


def validate_scope_path_maps(root: Path, add) -> None:
    for path in (sorted((root / "docs/reviews").glob("*.md")) if (root / "docs/reviews").is_dir() else []):
        relative = normalized_relative(path, root)
        match = SCOPE_PATH_MAP.search(path.read_text(encoding="utf-8"))
        if not match:
            continue
        try:
            payload = json.loads(match.group(1))
            base_commit = payload["base_commit"]
            head_commit = payload.get("head_commit")
            semantic = payload["semantic_paths"]
            evidence = payload["evidence_navigation_paths"]
            expected_semantic = payload["expected_semantic_count"]
            expected_evidence = payload["expected_evidence_navigation_count"]
            if not isinstance(base_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", base_commit):
                raise ValueError("base_commit must be one full Git commit")
            if head_commit is not None and (not isinstance(head_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", head_commit)):
                raise ValueError("head_commit must be one full Git commit when supplied")
            if not isinstance(semantic, dict) or not isinstance(evidence, dict):
                raise ValueError("semantic/evidence mappings must be objects")
            if len(semantic) != expected_semantic or len(evidence) != expected_evidence:
                raise ValueError("declared path counts do not match mapping sizes")
            overlap = set(semantic) & set(evidence)
            if overlap:
                raise ValueError(f"paths classified twice: {sorted(overlap)}")
            declared = set(semantic) | set(evidence)
            for mapped_path, outcome in {**semantic, **evidence}.items():
                safe_relative(mapped_path)
                if not isinstance(outcome, str) or not outcome.strip():
                    raise ValueError(f"empty outcome/classification for {mapped_path}")
            target = head_commit or "--"
            observed = {line for line in git_output(root, ["diff", "--name-only", base_commit, target]).splitlines() if line}
            if head_commit is None:
                observed.update(line for line in git_output(root, ["ls-files", "--others", "--exclude-standard"]).splitlines() if line)
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
            add("AHV-SCOPE-003", "error", relative, f"invalid Scope path mapping: {error}", "bind one exact base and classify every changed path exactly once")
            continue
        if observed != declared:
            add("AHV-SCOPE-003", "error", relative, f"Scope path mapping drift; missing={sorted(observed - declared)}, stale={sorted(declared - observed)}", "map every actual changed path to one required outcome or evidence/navigation class")


def validate_review_filenames(root: Path, add) -> None:
    review_root = root / "docs/reviews"
    if not review_root.is_dir():
        return
    for path in sorted(review_root.glob("*.md")):
        match = REVIEW_FILENAME.fullmatch(path.name)
        date_valid = False
        if match:
            try:
                datetime.strptime(match.group("date"), "%Y%m%d")
                date_valid = True
            except ValueError:
                pass
        if not match or not date_valid:
            relative = normalized_relative(path, root)
            add("AHV-REVIEW-001", "error", relative, "top-level Review filename does not match a real YYYYMMDD-<harness-semver>-<stable-logical-name>-review.md date", "rename the Review record; keep docs/reviews/evidence paths unchanged")


def validate_hip_schema(relative: str, text: str, add) -> None:
    if not HIP_FILENAME.fullmatch(relative):
        add("AHV-HIP-002", "error", relative, "HIP filename is not YYYY-MM-DD-<stable-logical-slug>.md", "rename the one proposal through the governed HIP path")
    if not re.search(r"^> (?:Artifact|Instantiated artifact) class:\s*Decision record\s*$", text, re.MULTILINE):
        add("AHV-HIP-003", "error", relative, "HIP is not identified as a Decision record", "instantiate the governed narrative HIP template")
    metadata = {
        field: match.group(1).strip().strip("`") if (match := re.search(rf"^> {re.escape(field)}:\s*(\S.+)$", text, re.MULTILINE)) else ""
        for field in HIP_REQUIRED_METADATA
    }
    missing_metadata = [field for field, value in metadata.items() if not value]
    heading_matches = [re.search(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE) for heading in HIP_REQUIRED_HEADINGS]
    missing_headings = [heading for heading, match in zip(HIP_REQUIRED_HEADINGS, heading_matches) if not match]
    empty_headings: list[str] = []
    for heading, match in zip(HIP_REQUIRED_HEADINGS, heading_matches):
        if not match:
            continue
        next_heading = re.search(r"^##\s+", text[match.end():], re.MULTILINE)
        body = text[match.end():match.end() + next_heading.start()] if next_heading else text[match.end():]
        meaningful = [line.strip() for line in body.splitlines() if line.strip() and not line.lstrip().startswith("#")]
        if not meaningful:
            empty_headings.append(heading)
    identifier = ARTIFACT_ID.search(text)
    manifest = re.search(r"^> Installed Harness manifest SHA-256:\s*`?([0-9a-f]{64})`?\s*$", text, re.MULTILINE)
    submitted = re.search(r"^> Submitted at:\s*`?([0-9]{4}-[0-9]{2}-[0-9]{2})`?\s*$", text, re.MULTILINE)
    filename_date = relative.rsplit("/", 1)[-1][:10]
    unresolved = re.compile(r"\b(?:pending|tbd|todo|unresolved)\b", re.IGNORECASE)
    status_valid = metadata.get("Status") == "approved_for_upstream"
    authority_valid = bool(metadata.get("Human Proposal Authority")) and not unresolved.search(metadata["Human Proposal Authority"])
    reviewers_valid = bool(metadata.get("Independent reviewers")) and not unresolved.search(metadata["Independent reviewers"])
    decision_valid = metadata.get("Decision class") == "D3 human-gated"
    placeholders = bool(re.search(r"\{\{[^{}\n]*\}\}|<<[^<>\n]*>>", text))
    identity_valid = bool(identifier and "-HIP-" in identifier.group(1) and manifest and submitted and submitted.group(1) == filename_date)
    if missing_metadata or missing_headings or empty_headings or not identity_valid or not status_valid or not authority_valid or not reviewers_valid or not decision_valid or placeholders:
        add("AHV-HIP-003", "error", relative, f"narrative HIP submission unresolved/incomplete; metadata={missing_metadata}, headings={missing_headings}, empty={empty_headings}, status={metadata.get('Status', '')!r}, placeholders={placeholders}", "submit only an exact approved_for_upstream HIP with resolved Human authority, reviewers, identity, narrative sections, and no template markers")


def validate_proposal_submission(root: Path, base_ref: str, head_ref: str, add) -> None:
    try:
        final_output = git_output(root, ["diff", "--name-status", "--find-renames", base_ref, head_ref])
        final_paths = changed_paths(final_output)
        commits = [line for line in git_output(root, ["rev-list", "--reverse", f"{base_ref}..{head_ref}"]).splitlines() if line]
        history_paths: set[str] = set()
        for commit in commits:
            parents = git_output(root, ["show", "-s", "--format=%P", commit]).split()
            if len(parents) != 1:
                add("AHV-HIP-004", "error", "docs/harness-proposals", f"proposal history contains non-linear commit {commit}", "use a clean linear proposal-only branch")
            history_paths.update(changed_paths(git_output(root, ["diff-tree", "--no-commit-id", "--name-status", "-r", "-M", commit])))
    except ValueError as error:
        add("AHV-HIP-001", "error", "docs/harness-proposals", f"proposal Git evidence unavailable or invalid: {error}", "supply exact locally resolvable proposal base/head refs")
        return

    signal = any(path.startswith(("docs/harness-proposals/", "docs/change-requests/")) for path in final_paths | history_paths)
    if not signal:
        return
    final_hips = sorted(path for path in final_paths if path.startswith("docs/harness-proposals/"))
    if len(final_hips) != 1 or final_paths != set(final_hips):
        add("AHV-HIP-004", "error", "docs/harness-proposals", f"proposal final diff must contain exactly one HIP; observed {sorted(final_paths)}", "separate proposal intake from Core, workflow, release, Product, or competing-intake changes")
        return
    candidate = final_hips[0]
    if history_paths != {candidate}:
        add("AHV-HIP-004", "error", candidate, f"proposal commit history touched prohibited paths: {sorted(history_paths - {candidate})}", "rebuild a clean branch whose every commit touches only the one HIP")
    try:
        text = git_output(root, ["show", f"{head_ref}:{candidate}"])
    except ValueError as error:
        add("AHV-HIP-001", "error", candidate, f"cannot read exact proposal head: {error}", "bind an existing exact head revision")
        return
    validate_hip_schema(candidate, text, add)


def validate(root: Path, mode: str, expected_manifest: str | None, proposal_base_ref: str | None = None, proposal_head_ref: str | None = None) -> list[Finding]:
    findings: list[Finding] = []
    def add(rule: str, severity: str, path: str, evidence: str, remediation: str) -> None:
        findings.append(Finding(rule, severity, severity == "error", path, evidence, remediation))

    files = repository_files(root, mode, add)
    required = ("AGENTS.md", "README.md", "docs/handover.md", "docs/specs/spec-routing.md")
    for relative in required:
        path = root / relative
        if not path.is_file() or path.is_symlink(): add("AHV-ENTRY-001", "error", relative, "required entry file missing, non-regular, or symlink", "restore a regular governed entry file")
    allowed_agents = {root / "AGENTS.md"}
    if mode == "master": allowed_agents.add(root / "harness/product-repo-overlay/AGENTS.md")
    for path in files:
        if path.name == "AGENTS.md" and path not in allowed_agents: add("AHV-ANCHOR-001", "error", normalized_relative(path, root), "unauthorized nested Agent-instruction file", "remove and route guidance through docs/agent-extensions.md")

    protected_root = root / ("harness/product-repo-overlay/.agentic-harness" if mode == "master" else ".agentic-harness")
    if protected_root.exists():
        for path in protected_root.rglob("*"):
            if path.is_symlink(): add("AHV-INTEGRITY-002", "error", normalized_relative(path, root), "symlink inside protected payload", "replace with a regular inventoried file")

    terminal_history = terminal_historical_contracts(root, files, mode)
    ids: dict[str, str] = {}; id_paths: dict[str, Path] = {}; run_events: list[tuple[Path, str]] = []; markdown_records: dict[str, tuple[Path, str, bool]] = {}
    source_token_allowlist = {"harness/product-repo-overlay/.agentic-harness/manifest.md", "harness/product-repo-overlay/.agentic-harness/release-metadata.json", "harness/product-repo-overlay/docs/harness-state/bootstrap-and-installation.md"}
    for path in markdown_files(files):
        relative = normalized_relative(path, root); text = path.read_text(encoding="utf-8"); is_template = ".agentic-harness/templates/" in f"{relative}/"
        markdown_records[relative] = (path, text, is_template)
        identifier = ARTIFACT_ID.search(text)
        if identifier and not any(mark in identifier.group(1) for mark in ("{{", "<<")):
            value = identifier.group(1)
            if value in ids: add("AHV-ARTIFACT-001", "error", relative, f"duplicate Artifact ID {value}; first {ids[value]}", "assign one stable owner ID")
            else: ids[value] = relative; id_paths[value] = path
        class_match = ARTIFACT_CLASS.search(text)
        if class_match and class_match.group(1).strip().strip("`") not in KNOWN_CLASSES: add("AHV-ARTIFACT-002", "error", relative, f"unknown primary class {class_match.group(1).strip()}", "use one allowed class")
        if not is_template and ("/run-events/" in f"/{relative}" or (identifier and "RUN-EVENT" in identifier.group(1))): run_events.append((path, text))
        historical_terminal = bool(identifier and identifier.group(1) in terminal_history)
        if not historical_terminal:
            validate_delivery_artifact(relative, text, is_template, identifier.group(1) if identifier else None, add)
            validate_effort_profile(relative, text, is_template, identifier.group(1) if identifier else None, add)
        tokens = list(RELEASE_INSTALL_TOKEN.finditer(text))
        if tokens:
            allowed = mode == "master" and relative in source_token_allowlist
            if mode == "release" and relative == "docs/harness-state/bootstrap-and-installation.md": allowed = all("AH_INSTALL:" in item.group(0) for item in tokens)
            if not allowed: add("AHV-TOKEN-001", "error", relative, "unresolved release/install token", "resolve in the governed stage")
        status = STATUS.search(text); is_draft = bool(status and status.group(1).strip().lower() == "draft")
        if identifier and INSTANCE_MARKER.search(text) and not is_template and not is_draft: add("AHV-TOKEN-002", "error", relative, "unresolved instantiation marker outside template/draft", "resolve field or return to draft")
        if relative.startswith("docs/specs/") and relative.endswith(".spec.md"):
            for field in SPEC_REQUIRED:
                if not re.search(rf"^> {re.escape(field)}:", text, re.MULTILINE): add("AHV-SPEC-001", "error", relative, f"missing spec metadata: {field}", "add required metadata")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")) or "{{" in target or "<<" in target: continue
            if target.startswith("/"):
                add("AHV-LINK-003", "error", relative, f"absolute repository link is non-portable: {target}", "use a repository-relative link"); continue
            target = target.split("#", 1)[0]
            if not target: continue
            linked = (path.parent / target).resolve()
            try: linked.relative_to(root.resolve())
            except ValueError: add("AHV-LINK-001", "error", relative, f"link escapes repository: {target}", "use repository-relative target"); continue
            if not linked.exists(): add("AHV-LINK-002", "warning" if mode == "master" and "product-repo-overlay" in relative else "error", relative, f"missing link target: {target}", "correct or create target")

    # Select checkpoint semantics from its bound Run, never the currently installed release or
    # a self-declared checkpoint version. Existing Mission binding checks verify that Run's digest.
    for relative, (_path, text, is_template) in markdown_records.items():
        identifier = ARTIFACT_ID.search(text)
        if identifier and identifier.group(1) in terminal_history:
            continue
        run_version = None
        blocks = MISSION_CHECKPOINT_BLOCK.findall(text)
        if len(blocks) == 1:
            try:
                checkpoint = json.loads(blocks[0])
                run_id = checkpoint.get("run_id") if isinstance(checkpoint, dict) else None
                record = markdown_records.get(ids.get(run_id, "")) if isinstance(run_id, str) else None
                if record:
                    run_version = direct_run_version(record[1])
                    declared = re.search(r"^> Harness version:\s*`?([^`\s]+)`?\s*$", record[1], re.MULTILINE)
                    if run_version is None and declared and SEMVER.fullmatch(declared.group(1)):
                        run_version = declared.group(1)
            except json.JSONDecodeError:
                pass  # The binding validator reports malformed checkpoint JSON below.
        validate_mission_runtime(relative, text, is_template, add, run_version)

    validate_convergence_budgets(markdown_records, ids, add)
    validate_domain_artifacts(root, markdown_records, add)

    for path in files:
        if path.is_symlink():
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".txt", ".py", ".js", ".ts", ".tsx", ".jsx", ".env"}: continue
        relative = normalized_relative(path, root); text = path.read_text(encoding="utf-8", errors="ignore")
        if path.suffix.lower() != ".md" and RELEASE_INSTALL_TOKEN.search(text):
            allowed = mode == "master" and relative in source_token_allowlist
            if not allowed: add("AHV-TOKEN-001", "error", relative, "unresolved release/install token", "resolve in the governed stage")
        for rule, pattern in SECRET_PATTERNS.items():
            if pattern.search(text): add("AHV-SECRET-001", "error", relative, f"high-confidence {rule} pattern detected; value suppressed", "remove/rotate and use an authorized reference")

    parsed_events = validate_event_chains(root, run_events, id_paths, mode, add)
    validate_agent_start_controls(root, markdown_records, parsed_events, mode, add)
    validate_ordinary_admission(root, markdown_records, parsed_events, id_paths, mode, add)
    validate_visual_assurance(root, markdown_records, parsed_events, add)
    validate_product_release_identity_events(root, markdown_records, add)
    validate_mission_bindings(root, markdown_records, id_paths, add)
    if mode == "master":
        validate_review_filenames(root, add)
        validate_source_lock(root, add)
        validate_master_release_controls(root, id_paths, add)
        validate_scope_path_maps(root, add)
        if bool(proposal_base_ref) != bool(proposal_head_ref):
            add("AHV-HIP-001", "error", "docs/harness-proposals", "proposal validation requires both base and head refs", "supply exact base/head refs together")
        elif proposal_base_ref and proposal_head_ref:
            validate_proposal_submission(root, proposal_base_ref, proposal_head_ref, add)
    if mode in {"product", "release"}:
        manifest = root / ".agentic-harness/manifest.md"
        if not manifest.is_file() or manifest.is_symlink(): add("AHV-MANIFEST-001", "error", ".agentic-harness/manifest.md", "manifest missing/non-regular", "restore authenticated release")
        elif not expected_manifest or not HEX64.fullmatch(expected_manifest.lower()): add("AHV-MANIFEST-002", "error", ".agentic-harness/manifest.md", "valid external expected manifest digest not supplied", "supply trusted digest")
        else:
            manifest_text = manifest.read_text(encoding="utf-8")
            actual_manifest = digest(manifest)
            if actual_manifest != expected_manifest.lower(): add("AHV-MANIFEST-003", "error", ".agentic-harness/manifest.md", f"manifest digest {actual_manifest} differs", "use authenticated release/pin")
            inventory, expected_tree = parse_manifest_inventory(manifest_text); actual_paths = protected_inventory(root); actual = {normalized_relative(path, root): digest(path) for path in actual_paths}
            if inventory != actual: add("AHV-MANIFEST-004", "error", ".agentic-harness/manifest.md", "protected inventory/path/digest mismatch", "reinstall or authorized upgrade")
            observed_tree = tree_digest(actual_paths, root)
            if not expected_tree or expected_tree != observed_tree: add("AHV-MANIFEST-005", "error", ".agentic-harness/manifest.md", f"tree digest mismatch: {observed_tree}", "restore exact protected payload")
        validate_release_metadata(root, add)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", default="."); parser.add_argument("--mode", choices=("auto", "master", "release", "product"), default="auto"); parser.add_argument("--expected-manifest-sha256"); parser.add_argument("--proposal-base-ref"); parser.add_argument("--proposal-head-ref"); parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--check-run", help="check only this repository-relative 1.2.7+ Run Contract and its exact named targets")
    args = parser.parse_args(); root = Path(args.root).resolve()
    if not root.is_dir(): print(f"validator error: root is not a directory: {root}", file=sys.stderr); return 2
    mode = args.mode if args.mode != "auto" else "master" if (root / "harness/product-repo-overlay").is_dir() else "product"
    if args.check_run:
        try:
            relative = safe_relative(args.check_run).as_posix()
            path = root / relative
            if not path.is_file() or path.is_symlink():
                raise ValueError("Run Contract path is missing, non-regular, or a symlink")
            text = path.read_text(encoding="utf-8")
            identifier = ARTIFACT_ID.search(text)
            findings: list[Finding] = []
            def add(rule: str, severity: str, finding_path: str, evidence: str, remediation: str) -> None:
                findings.append(Finding(rule, severity, severity == "error", finding_path, evidence, remediation))
            contract = validate_direct_run_contract(root, relative, text, identifier.group(1) if identifier else None, mode, add)
            installed_version = current_harness_version(root, mode)
            if contract and semver_tuple(contract["harness_version"]) >= TASK_CONTROLS_MIN_VERSION and contract["status"] in ("blocked", "cancelled"):
                add("AHV-RUN-CHECK-001", "error", relative, f"Run status {contract['status']} forbids start/continuation", "resolve the blocker under its owning authority before rechecking an authorized revision")
            if contract and installed_version and contract["harness_version"] != installed_version:
                add("AHV-RUN-CHECK-001", "error", relative, f"harness_version {contract['harness_version']!r} differs from installed {installed_version!r}", "create or revise the Run under the installed Harness before starting it")
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as error:
            print(f"validator error: {error}", file=sys.stderr)
            return 1
        if args.format == "json":
            result = {"run_contract": relative, "findings": [asdict(item) for item in findings]}
            if not findings and START_RECOVERY_BLOCK.search(text):
                result["historical_recovery"] = {"status": "accepted", "authorizes_start_or_continuation": False}
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            for item in findings: print(f"{item.severity.upper()} {item.rule_id} {item.path}: {item.evidence} — {item.remediation}")
            if not findings and START_RECOVERY_BLOCK.search(text):
                print("Historical start-omission recovery accepted; this is not start/continuation authorization.")
            print(f"Run check: {'fail' if findings else 'pass'} — {relative}")
        return 1 if findings else 0
    try: findings = validate(root, mode, args.expected_manifest_sha256, args.proposal_base_ref, args.proposal_head_ref)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as error: print(f"validator error: {error}", file=sys.stderr); return 2
    if args.format == "json": print(json.dumps({"mode": mode, "findings": [asdict(item) for item in findings]}, indent=2, sort_keys=True))
    else:
        for item in findings: print(f"{item.severity.upper()} {item.rule_id} {item.path}: {item.evidence} — {item.remediation}")
        print(f"Harness validation: {sum(item.severity == 'error' for item in findings)} error(s), {sum(item.severity == 'warning' for item in findings)} warning(s), mode={mode}")
    return 1 if any(item.severity == "error" for item in findings) else 0


if __name__ == "__main__": raise SystemExit(main())
