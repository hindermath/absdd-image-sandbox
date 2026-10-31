#!/usr/bin/env python3
"""Validate secure-development hardening evidence without third-party modules.

The shared core keeps Bash and PowerShell semantics identical.  It validates
repository-relative paths before reading, never follows a path outside the
declared repository, and prints only validation rules—not file contents.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
from typing import Any, Iterable


EXIT_OK = 0
EXIT_VALIDATION = 1
EXIT_USAGE = 2
EXIT_PLATFORM = 3

FEATURE_DIR = "specs/003-secure-development-container-hardening"
ASSESSMENT_PATH = "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/assessment-results.json"
GATE_REQUIREMENTS_PATH = f"{FEATURE_DIR}/autonomous-run-gate-requirements.json"
FEASIBILITY_DECISION_PATH = (
    "docs/security/secure-development/2026-08-30-container-hardening/"
    "feasibility-study-decision.json"
)

EXPECTED_FEASIBILITY_DECISION_FIELDS = {
    "schemaVersion",
    "decisionId",
    "status",
    "effectiveAt",
    "expiresOn",
    "ownerRole",
    "studyType",
    "deliveryScope",
    "independentReview",
    "moderatedLearnerTest",
    "supplyChainDisposition",
    "prohibitedClaims",
    "reevaluationTriggers",
    "containsSensitiveContent",
}

EXPECTED_PROHIBITED_FEASIBILITY_CLAIMS = {
    "IndependentSecurityApproval",
    "LearnerValidationCompleted",
    "PrebuiltImageApprovedForDistribution",
    "ProductionUseApproved",
}

EXPECTED_FEASIBILITY_REEVALUATION_TRIGGERS = {
    "BeforeLearnerRollout",
    "BeforePrebuiltImageDistribution",
    "BeforeProductionUse",
    "AtOrAfterExpiry",
}

EXPECTED_BINDINGS = (
    (
        "Lastenheft_Secure-Development-Container-Hardening.md",
        "72c263db933ea5a10ca60f3a7cc41231b43e1aec5d0dd641129e1a523b3432dc",
        "FeatureIntake",
    ),
    (
        "specs/intake-review-results/sandbox-development-lifecycle.json",
        "0d08a1e90e25965c4b529d66be6996394b963abef4ddb3c3b75dd678f464004b",
        "IntakeReview",
    ),
    (
        "specs/intake-series/sandbox-development-lifecycle/manifest.json",
        "8813d2135a092671ccb373cd9273f44fe8ec3ceabab3eaa35f44e617cf2d15c4",
        "SeriesManifest",
    ),
    (
        ASSESSMENT_PATH,
        "81a7ab5c5d8c6de449289de1dbf143e14933a3678a1160a25ed8ba5d671c8b39",
        "AssessmentResults",
    ),
    (
        "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/prioritized-gap-list.md",
        "b7e631e9df5e37686ab1ff2c0a07552c5d59c23af28621c917e36d2a42f55542",
        "PrioritisedGapList",
    ),
    (
        "docs/security/secure-development/2026-08-30-gsdb-baseline-assessment/acceptance-decision.md",
        "12fbac3263f31646e83e4d9b841a73c41d96dcc8ca259be68b40f356bd0354c7",
        "AcceptanceDecision",
    ),
)

EXPECTED_GAP_FIELDS = {
    "gapId",
    "affectedClIds",
    "priority",
    "humanOnly",
    "humanOnlyRole",
    "applicability",
    "implementationStatus",
    "consolidatedState",
    "rationaleDe",
    "rationaleEn",
    "requirementIds",
    "evidenceIds",
    "owner",
    "reviewer",
    "residualRisk",
    "missingEvidence",
    "followUp",
    "reevaluationTrigger",
    "lastEvaluatedAt",
}

EXPECTED_EVIDENCE_FIELDS = {
    "evidenceId",
    "gateId",
    "applicability",
    "subjectPaths",
    "command",
    "runnerOrPlatform",
    "startedAt",
    "finishedAt",
    "exitCode",
    "expectedResult",
    "observedResult",
    "result",
    "freshness",
    "limitations",
    "artifactSha256",
    "containsSensitiveContent",
    "rationale",
    "reevaluationTrigger",
}

TEXT_FIELDS_GAP = {
    "gapId",
    "humanOnlyRole",
    "applicability",
    "implementationStatus",
    "consolidatedState",
    "rationaleDe",
    "rationaleEn",
    "owner",
    "reviewer",
    "residualRisk",
    "missingEvidence",
    "followUp",
    "reevaluationTrigger",
    "lastEvaluatedAt",
}

ROLE_VALUES = {
    "Repository Maintainer",
    "Security Review",
    "Privacy/Legal Review",
    "Platform Owner/Admin",
    "CISO/ISB/KIB",
    "Project Owner",
    "Learning/A11Y Review",
}


def normalized_bytes(path: Path) -> bytes:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    text = raw.decode("utf-8", errors="strict")
    if "\x00" in text:
        raise ValueError(f"binary NUL is not supported: {path.name}")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def normalized_sha256(path: Path) -> str:
    return hashlib.sha256(normalized_bytes(path)).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(normalized_bytes(path).decode("utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path.name}")
    return value


def safe_repo_path(repo_root: Path, candidate: str, *, must_exist: bool = True) -> Path:
    """Resolve a repository-relative path without allowing traversal."""
    if not isinstance(candidate, str) or not candidate.strip():
        raise ValueError("repository path must be a non-empty string")
    pure = PurePosixPath(candidate.replace("\\", "/"))
    if pure.is_absolute() or ".." in pure.parts or re.match(r"^[A-Za-z]:", candidate):
        raise ValueError(f"path is outside the repository boundary: {candidate}")
    root = repo_root.resolve()
    resolved = (root / Path(*pure.parts)).resolve(strict=False)
    if resolved != root and root not in resolved.parents:
        raise ValueError(f"path is outside the repository boundary: {candidate}")
    if must_exist and not resolved.exists():
        raise ValueError(f"required path does not exist: {candidate}")
    return resolved


def is_nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_utc(value: Any, label: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        errors.append(f"{label} must be a UTC date-time ending in Z")
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        errors.append(f"{label} must be a valid UTC date-time")
        return None


def duplicates(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    repeated: set[str] = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        seen.add(value)
    return sorted(repeated)


def status_is_valid(item: dict[str, Any]) -> bool:
    key = (
        item.get("consolidatedState"),
        item.get("applicability"),
        item.get("implementationStatus"),
    )
    return key in {
        ("N/A", "N/A", "Not Assessed"),
        ("Open", "Open", "Not Assessed"),
        ("AlreadySatisfied", "Applicable", "Fulfilled"),
        ("FollowUp", "Applicable", "Partly Fulfilled"),
        ("FollowUp", "Applicable", "Not Fulfilled"),
        ("Applicable", "Applicable", "Not Assessed"),
    }


# The completed Feature 003 retains accepted input hashes after lifecycle repair.
# These fixed snapshots prove historical inputs, never current intake readiness.
HISTORICAL_BINDING_PATHS = {
    "FeatureIntake": "specs/intake-authoring-archive/a92a7ced-bbf3-4408-9754-7b739be19a41/8524075f-f913-41da-a68b-a0f5c5aef582/target.md",
    "IntakeReview": "specs/intake-review-archive/6403c657-e508-4029-bfe8-319436f3fa7a/9d9fce68-15cc-490c-afe0-16b98eda8a54/result.json",
    "SeriesManifest": "specs/intake-series-archive/65371068-4b1d-4465-9ce7-120e6b15b926/9d9fce68-15cc-490c-afe0-16b98eda8a54/manifest.json",
}


def validate_gap_document(
    document: dict[str, Any],
    repo_root: Path,
    *,
    known_evidence_ids: set[str] | None = None,
) -> list[str]:
    errors: list[str] = []
    expected_root = {
        "schemaVersion",
        "acceptedInputBindings",
        "sourceAssessmentSha256",
        "dispositions",
        "summary",
    }
    unexpected_root = set(document) - expected_root
    missing_root = expected_root - set(document)
    if unexpected_root:
        errors.append(f"gap document has unexpected fields: {sorted(unexpected_root)}")
    if missing_root:
        errors.append(f"gap document is missing fields: {sorted(missing_root)}")
    if document.get("schemaVersion") != "1.0":
        errors.append("gap document schemaVersion must be 1.0")

    bindings = document.get("acceptedInputBindings")
    if not isinstance(bindings, list) or len(bindings) != 6:
        errors.append("acceptedInputBindings must contain exactly six entries")
        bindings = []
    expected_roles = {entry[2] for entry in EXPECTED_BINDINGS}
    actual_roles = {entry.get("role") for entry in bindings if isinstance(entry, dict)}
    if actual_roles != expected_roles or len(actual_roles) != len(bindings):
        errors.append("accepted input binding roles must be exactly the six declared roles")
    expected_by_role = {role: (path, sha) for path, sha, role in EXPECTED_BINDINGS}
    for index, binding in enumerate(bindings):
        label = f"acceptedInputBindings[{index}]"
        if not isinstance(binding, dict):
            errors.append(f"{label} must be an object")
            continue
        if set(binding) != {"path", "sha256", "role"}:
            errors.append(f"{label} has unexpected or missing fields")
            continue
        role = binding.get("role")
        if role not in expected_by_role:
            continue
        expected_path, expected_hash = expected_by_role[role]
        if binding.get("path") != expected_path:
            errors.append(f"{label} path mismatch for role {role}")
            continue
        if binding.get("sha256") != expected_hash:
            errors.append(f"{label} accepted hash mismatch for {expected_path}")
            continue
        try:
            current_hash = normalized_sha256(safe_repo_path(repo_root, expected_path))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{label} cannot verify accepted path: {exc}")
            continue
        if current_hash != expected_hash:
            historical_path = HISTORICAL_BINDING_PATHS.get(role)
            try:
                completed = load_json(safe_repo_path(
                    repo_root, f"{FEATURE_DIR}/autonomous-run-state.json"
                )).get("status") == "Completed"
                historical_hash = (
                    normalized_sha256(safe_repo_path(repo_root, historical_path))
                    if historical_path and completed else None
                )
            except (OSError, UnicodeError, ValueError):
                historical_hash = None
            if historical_hash != expected_hash:
                errors.append(f"{label} current hash mismatch for {expected_path}")

    if document.get("sourceAssessmentSha256") != expected_by_role["AssessmentResults"][1]:
        errors.append("sourceAssessmentSha256 does not match the accepted assessment")

    dispositions = document.get("dispositions")
    if not isinstance(dispositions, list) or len(dispositions) != 157:
        errors.append("dispositions must contain exactly 157 entries")
        dispositions = dispositions if isinstance(dispositions, list) else []
    gap_ids = [item.get("gapId") for item in dispositions if isinstance(item, dict)]
    repeated = duplicates([value for value in gap_ids if isinstance(value, str)])
    if repeated:
        errors.append(f"duplicate gap IDs: {repeated}")
    expected_ids = [f"GAP-{number:03d}" for number in range(1, 158)]
    if gap_ids != expected_ids:
        missing = sorted(set(expected_ids) - set(gap_ids))
        extra = sorted(set(gap_ids) - set(expected_ids), key=str)
        errors.append(f"gap IDs must be ordered GAP-001 through GAP-157; missing={missing}, extra={extra}")

    try:
        baseline = load_json(safe_repo_path(repo_root, ASSESSMENT_PATH))
        baseline_gaps = baseline.get("gaps", [])
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read accepted baseline projection: {exc}")
        baseline_gaps = []
    baseline_by_id = {
        item.get("gapId"): item for item in baseline_gaps if isinstance(item, dict)
    }

    evidence_ids_seen: list[str] = []
    for index, item in enumerate(dispositions):
        label = f"dispositions[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object")
            continue
        unexpected = set(item) - EXPECTED_GAP_FIELDS
        missing = EXPECTED_GAP_FIELDS - set(item)
        if unexpected:
            errors.append(f"{label} has unexpected fields: {sorted(unexpected)}")
        if missing:
            errors.append(f"{label} is missing fields: {sorted(missing)}")
        for field in TEXT_FIELDS_GAP:
            if not is_nonempty_text(item.get(field)):
                errors.append(f"{label}.{field} must be non-empty")
        parse_utc(item.get("lastEvaluatedAt"), f"{label}.lastEvaluatedAt", errors)
        if item.get("priority") != "P1":
            errors.append(f"{label}.priority must be P1")
        if item.get("owner") not in ROLE_VALUES or item.get("reviewer") not in ROLE_VALUES:
            errors.append(f"{label} has an unknown owner or reviewer role")
        baseline_item = baseline_by_id.get(item.get("gapId"))
        if not baseline_item:
            errors.append(f"{label} has no reciprocal baseline gap")
        else:
            projection = ("gapId", "affectedClIds", "priority", "humanOnly", "humanOnlyRole")
            if any(item.get(field) != baseline_item.get(field) for field in projection):
                errors.append(f"{label} baseline projection mismatch")
        if not status_is_valid(item):
            errors.append(f"{label} has an invalid status combination")
        if item.get("humanOnly"):
            if (
                item.get("consolidatedState") != "Open"
                or item.get("implementationStatus") != "Not Assessed"
                or item.get("residualRisk") != "Unassessed"
            ):
                errors.append(f"{label} human-only status must remain Open/Not Assessed/Unassessed")
        requirements = item.get("requirementIds")
        if not isinstance(requirements, list) or not requirements or len(requirements) != len(set(requirements)):
            errors.append(f"{label}.requirementIds must be a non-empty unique list")
        elif any(not isinstance(value, str) or not re.match(r"^(FR|GR|AR|CP|AP|AU|GATE)-[A-Za-z0-9-]+$", value) for value in requirements):
            errors.append(f"{label}.requirementIds contains an invalid ID")
        evidence_ids = item.get("evidenceIds")
        if not isinstance(evidence_ids, list) or len(evidence_ids) != len(set(evidence_ids)):
            errors.append(f"{label}.evidenceIds must be a unique list")
        else:
            evidence_ids_seen.extend(value for value in evidence_ids if isinstance(value, str))
            if known_evidence_ids is not None:
                unknown = sorted(set(evidence_ids) - known_evidence_ids)
                if unknown:
                    errors.append(f"{label} references unknown evidence IDs: {unknown}")
        if item.get("consolidatedState") == "AlreadySatisfied" and not evidence_ids:
            errors.append(f"{label} AlreadySatisfied requires current evidence")
        if item.get("consolidatedState") == "N/A" and item.get("missingEvidence") != "N/A":
            errors.append(f"{label} N/A requires missingEvidence=N/A")

    if known_evidence_ids is not None:
        orphaned = sorted(known_evidence_ids - set(evidence_ids_seen))
        # Gate-only evidence need not map to a gap; only explicit EVD-GAP records do.
        orphaned_gap_records = [value for value in orphaned if value.startswith("EVD-GAP-")]
        if orphaned_gap_records:
            errors.append(f"non-reciprocal gap evidence IDs: {orphaned_gap_records}")

    summary = document.get("summary")
    if not isinstance(summary, dict):
        errors.append("summary must be an object")
    else:
        expected_summary_fields = {
            "gapCount",
            "agentActionableCount",
            "humanOnlyCount",
            "missingGapIds",
            "duplicateGapIds",
            "extraGapIds",
            "unmappedChangedPaths",
        }
        if set(summary) != expected_summary_fields:
            errors.append("summary has unexpected or missing fields")
        if summary.get("gapCount") != 157:
            errors.append("summary.gapCount must be 157")
        if summary.get("agentActionableCount") != 108:
            errors.append("summary.agentActionableCount must be 108")
        if summary.get("humanOnlyCount") != 49:
            errors.append("summary.humanOnlyCount must be 49")
        for field in ("missingGapIds", "duplicateGapIds", "extraGapIds", "unmappedChangedPaths"):
            if summary.get(field) != []:
                errors.append(f"summary.{field} must be empty")
    if sum(1 for item in dispositions if isinstance(item, dict) and item.get("humanOnly")) != 49:
        errors.append("human-only partition must contain exactly 49 entries")
    if sum(1 for item in dispositions if isinstance(item, dict) and item.get("humanOnly") is False) != 108:
        errors.append("agent-actionable partition must contain exactly 108 entries")
    return errors


def validate_evidence_document(
    document: dict[str, Any],
    gate_requirements: dict[str, Any],
    repo_root: Path,
    *,
    require_all_gates: bool = False,
) -> list[str]:
    errors: list[str] = []
    expected_root = {"schemaVersion", "sourceRevision", "imageIdentity", "gateResults", "overallResult"}
    if set(document) != expected_root:
        errors.append("evidence document has unexpected or missing fields")
    if document.get("schemaVersion") != "1.0":
        errors.append("evidence schemaVersion must be 1.0")
    source_revision = document.get("sourceRevision")
    if source_revision != "WORKTREE" and not (
        isinstance(source_revision, str) and re.fullmatch(r"[a-f0-9]{40}", source_revision)
    ):
        errors.append("sourceRevision must be WORKTREE or a lowercase 40-character commit")
    if not is_nonempty_text(document.get("imageIdentity")):
        errors.append("imageIdentity must be non-empty")
    if document.get("overallResult") not in {"Pass", "Fail", "Blocked"}:
        errors.append("overallResult must be Pass, Fail, or Blocked")

    requirements = gate_requirements.get("gates")
    if not isinstance(requirements, list):
        errors.append("gate requirements must contain a gates array")
        requirements = []
    requirement_by_id = {
        item.get("gateId"): item for item in requirements if isinstance(item, dict)
    }
    records = document.get("gateResults")
    if not isinstance(records, list) or not records:
        errors.append("gateResults must be a non-empty array")
        records = []
    record_gate_ids = [record.get("gateId") for record in records if isinstance(record, dict)]
    record_evidence_ids = [record.get("evidenceId") for record in records if isinstance(record, dict)]
    if duplicates([value for value in record_gate_ids if isinstance(value, str)]):
        errors.append("gateResults contains duplicate gate IDs")
    if duplicates([value for value in record_evidence_ids if isinstance(value, str)]):
        errors.append("gateResults contains duplicate evidence IDs")
    if require_all_gates and set(record_gate_ids) != set(requirement_by_id):
        errors.append("gateResults must contain every declared gate exactly once")

    for index, record in enumerate(records):
        label = f"gateResults[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{label} must be an object")
            continue
        unexpected = set(record) - EXPECTED_EVIDENCE_FIELDS
        missing = EXPECTED_EVIDENCE_FIELDS - set(record)
        if unexpected:
            errors.append(f"{label} has unexpected fields: {sorted(unexpected)}")
        if missing:
            errors.append(f"{label} is missing fields: {sorted(missing)}")
        gate = requirement_by_id.get(record.get("gateId"))
        if not gate:
            errors.append(f"{label} references an unknown gate")
            continue
        if record.get("applicability") != gate.get("applicability"):
            errors.append(f"{label} applicability differs from gate requirements")
        if not isinstance(record.get("subjectPaths"), list) or not record.get("subjectPaths"):
            errors.append(f"{label}.subjectPaths must be non-empty")
        else:
            for subject in record["subjectPaths"]:
                if not is_nonempty_text(subject):
                    errors.append(f"{label}.subjectPaths contains an empty value")
                    continue
                if not subject.startswith("local-image:") and subject != "N/A":
                    try:
                        safe_repo_path(repo_root, subject, must_exist=False)
                    except ValueError as exc:
                        errors.append(f"{label}.subjectPaths is invalid: {exc}")
        started = parse_utc(record.get("startedAt"), f"{label}.startedAt", errors)
        finished = parse_utc(record.get("finishedAt"), f"{label}.finishedAt", errors)
        if started and finished and finished < started:
            errors.append(f"{label} finishedAt precedes startedAt")
        for field in (
            "evidenceId",
            "gateId",
            "expectedResult",
            "observedResult",
            "limitations",
            "rationale",
            "reevaluationTrigger",
        ):
            if not is_nonempty_text(record.get(field)):
                errors.append(f"{label}.{field} must be non-empty")
        if record.get("containsSensitiveContent") is not False:
            errors.append(f"{label}.containsSensitiveContent must be false")
        if record.get("applicability") == "N/A":
            expected_na = {
                "command": "N/A",
                "runnerOrPlatform": "N/A",
                "exitCode": None,
                "result": "N/A",
                "freshness": "N/A",
                "artifactSha256": "N/A",
            }
            if any(record.get(field) != value for field, value in expected_na.items()):
                errors.append(f"{label} N/A execution fields must not contain invented run data")
            if record.get("rationale") != gate.get("rationale"):
                errors.append(f"{label} N/A rationale must equal the declared gate rationale")
            if record.get("reevaluationTrigger") != gate.get("reevaluationTrigger"):
                errors.append(f"{label} N/A trigger must equal the declared gate trigger")
        else:
            if not is_nonempty_text(record.get("command")) or record.get("command") == "N/A":
                errors.append(f"{label}.command must describe actual execution")
            if not is_nonempty_text(record.get("runnerOrPlatform")) or record.get("runnerOrPlatform") == "N/A":
                errors.append(f"{label}.runnerOrPlatform must describe actual execution")
            if not isinstance(record.get("exitCode"), int) or not 0 <= record["exitCode"] <= 255:
                errors.append(f"{label}.exitCode must be an integer from 0 to 255")
            if record.get("result") not in {"Pass", "Fail", "Blocked"}:
                errors.append(f"{label}.result must be Pass, Fail, or Blocked")
            if record.get("freshness") not in {"Current", "Stale"}:
                errors.append(f"{label}.freshness must be Current or Stale")
            artifact = record.get("artifactSha256")
            if artifact != "N/A" and not (
                isinstance(artifact, str) and re.fullmatch(r"[a-f0-9]{64}", artifact)
            ):
                errors.append(f"{label}.artifactSha256 must be lowercase SHA-256 or N/A")
            if record.get("result") == "Pass" and record.get("exitCode") != 0:
                errors.append(f"{label} Pass requires exitCode 0")
            if record.get("result") == "Pass" and record.get("freshness") == "Stale":
                errors.append(f"{label} stale evidence cannot pass")
            for token in gate.get("requiredCommandTokens", []):
                if token not in record.get("command", ""):
                    errors.append(f"{label}.command is missing required token: {token}")
            for token in gate.get("requiredRunnerOrPlatformTokens", []):
                if token not in record.get("runnerOrPlatform", ""):
                    errors.append(f"{label}.runnerOrPlatform is missing required token: {token}")
    return errors


def print_result(errors: list[str], label: str) -> int:
    if errors:
        print(f"RED: {label} rejected with {len(errors)} rule violation(s).", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return EXIT_VALIDATION
    print(f"GREEN: {label} is valid.")
    return EXIT_OK


def command_plan(repo: Path, mode: str) -> list[list[str]]:
    python = sys.executable
    plans: dict[str, list[list[str]]] = {
        "Input": [],
        "Static": [
            [python, "-m", "unittest", "scripts.tests.test_secure_development_container_hardening"],
            [python, "scripts/check-dockerfile-arg-renovate.py"],
            [python, "scripts/check-home-baseline-lock.py"],
            [python, "scripts/tests/test_agent_prompt_dispatchers.py"],
            [python, "scripts/tests/test_spec_kit_agent_surface_parity.py"],
            ["bash", "scripts/test-documentation-impact.sh"],
            ["git", "diff", "--check"],
        ],
        "Runtime": [
            ["podman", "compose", "ps"],
            ["podman", "compose", "exec", "-T", "ade", "sh", "-lc", "test \"$(id -u)\" -ne 0 && test \"$(id -un)\" = adedev"],
            ["podman", "compose", "exec", "-T", "ade", "sh", "-lc", "grep -q '^NoNewPrivs:[[:space:]]*1' /proc/1/status"],
        ],
        "SupplyChain": [],
        "Documentation": [["bash", "scripts/test-documentation-impact.sh"]],
        "Accessibility": [],
    }
    return plans[mode]


def validate_feasibility_study_decision_document(
    value: dict[str, Any], *, today: datetime | None = None
) -> list[str]:
    errors: list[str] = []
    if set(value) != EXPECTED_FEASIBILITY_DECISION_FIELDS:
        errors.append("feasibility study decision has unexpected or missing fields")
    expected_values = {
        "schemaVersion": "1.0",
        "decisionId": "DEC-FEASIBILITY-SINGLE-PERSON-2026-09-06",
        "status": "AcceptedScopeLimitation",
        "ownerRole": "Repository Owner",
        "studyType": "SinglePersonFeasibilityStudy",
        "deliveryScope": "SourceRepositoryOnly",
        "independentReview": "NotPerformed",
        "moderatedLearnerTest": "NotPerformed",
        "supplyChainDisposition": "TransparentOpenTriage",
        "containsSensitiveContent": False,
    }
    for field, expected in expected_values.items():
        if value.get(field) != expected:
            errors.append(f"feasibility study decision {field} must be {expected!r}")
    if set(value.get("prohibitedClaims", [])) != EXPECTED_PROHIBITED_FEASIBILITY_CLAIMS:
        errors.append("feasibility study decision must prohibit every unsupported approval claim")
    if set(value.get("reevaluationTriggers", [])) != EXPECTED_FEASIBILITY_REEVALUATION_TRIGGERS:
        errors.append("feasibility study decision must retain every re-evaluation trigger")
    parse_utc(value.get("effectiveAt"), "feasibilityStudyDecision.effectiveAt", errors)
    try:
        expires_on = datetime.strptime(value.get("expiresOn", ""), "%Y-%m-%d").date()
        current_date = (today or datetime.now(timezone.utc)).date()
        if expires_on < current_date:
            errors.append("feasibility study decision has expired")
    except (TypeError, ValueError):
        errors.append("feasibilityStudyDecision.expiresOn must use YYYY-MM-DD")
    return errors


def validate_feasibility_study_decision(repo: Path) -> list[str]:
    path = repo / FEASIBILITY_DECISION_PATH
    if not path.is_file():
        return ["single-person feasibility study decision is missing"]
    try:
        value = load_json(path)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        return [f"feasibility study decision is invalid: {exc}"]
    learner_result = repo / (
        "docs/security/secure-development/2026-08-30-container-hardening/"
        "learner-first-use-results.json"
    )
    errors = validate_feasibility_study_decision_document(value)
    if learner_result.exists():
        errors.append(
            "learner evidence exists and requires GATE-LEARNER-01 applicability re-evaluation"
        )
    return errors


def validate_learner_result(repo: Path) -> list[str]:
    path = repo / "docs/security/secure-development/2026-08-30-container-hardening/learner-first-use-results.json"
    if not path.is_file():
        return [
            "GATE-LEARNER-01 is Blocked: dated Learning/A11Y Review evidence is missing; "
            "the agent must not create substitute observations"
        ]
    try:
        value = load_json(path)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        return [f"learner-first-use-results.json is invalid: {exc}"]
    errors: list[str] = []
    if value.get("owner") != "Learning/A11Y Review":
        errors.append("learner result owner must be Learning/A11Y Review")
    if value.get("priorSpecKitExperience") is not False:
        errors.append("learner result must cover participants without prior Spec Kit experience")
    if value.get("timeLimitMinutes") != 30:
        errors.append("learner result timeLimitMinutes must be 30")
    rate = value.get("successRatePercent")
    if not isinstance(rate, (int, float)) or rate < 90:
        errors.append("learner result successRatePercent must be at least 90")
    expected_audiences = {
        "Fachinformatiker*innen",
        "IT-System-Elektroniker*innen",
        "Kaufleute fuer IT-System-Management",
        "Kaufleute fuer Digitalisierungsmanagement",
    }
    if set(value.get("audienceCoverage", [])) != expected_audiences:
        errors.append("learner result must cover all four binding occupations")
    if value.get("containsSensitiveContent") is not False:
        errors.append("learner result containsSensitiveContent must be false")
    return errors


def execute_mode(
    repo: Path,
    mode: str,
    evidence_path: str | None,
    dry_run: bool,
    feature_directory: str | None = None,
) -> int:
    if feature_directory is not None:
        return execute_feature_004_mode(repo, mode, evidence_path, dry_run, feature_directory)
    gaps_path = repo / "docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json"
    requirements_path = repo / GATE_REQUIREMENTS_PATH
    errors: list[str] = []
    try:
        gaps = load_json(gaps_path)
        requirements = load_json(requirements_path)
        evidence = None
        known = None
        if evidence_path:
            candidate = safe_repo_path(repo, evidence_path, must_exist=False)
            if candidate.is_file():
                evidence = load_json(candidate)
                known = {
                    item.get("evidenceId")
                    for item in evidence.get("gateResults", [])
                    if isinstance(item, dict) and isinstance(item.get("evidenceId"), str)
                }
        errors.extend(validate_gap_document(gaps, repo, known_evidence_ids=known))
        if evidence is not None:
            errors.extend(
                validate_evidence_document(
                    evidence,
                    requirements,
                    repo,
                    require_all_gates=(mode == "All"),
                )
            )
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Contract or path error: {exc}", file=sys.stderr)
        return EXIT_USAGE
    if errors:
        return print_result(errors, f"{mode} evidence contract")

    selected_modes = (
        ["Input", "Static", "Runtime", "SupplyChain", "Documentation", "Accessibility"]
        if mode == "All"
        else [mode]
    )
    for selected in selected_modes:
        if selected == "SupplyChain":
            required = [
                "docs/security/secure-development/2026-08-30-container-hardening/build-provenance.json",
                "docs/security/secure-development/2026-08-30-container-hardening/vulnerability-findings.json",
                "docs/security/secure-development/2026-08-30-container-hardening/vex.cdx.json",
            ]
            missing = [path for path in required if not (repo / path).is_file()]
            if missing:
                print(f"RED: SupplyChain evidence is missing: {', '.join(missing)}", file=sys.stderr)
                return EXIT_VALIDATION
        if selected == "Documentation":
            required_docs = [
                "README.md",
                "docs/betrieb/README.md",
                "docs/fuer-lernende/README.md",
                "docs/security/secure-development/2026-08-30-container-hardening/README.md",
            ]
            missing = [path for path in required_docs if not (repo / path).is_file()]
            if missing:
                print(f"RED: documentation paths are missing: {', '.join(missing)}", file=sys.stderr)
                return EXIT_VALIDATION
        if selected == "Accessibility":
            learner_gate = next(
                item
                for item in requirements.get("gates", [])
                if item.get("gateId") == "GATE-LEARNER-01"
            )
            learner_errors = (
                validate_feasibility_study_decision(repo)
                if learner_gate.get("applicability") == "N/A"
                else validate_learner_result(repo)
            )
            if learner_errors:
                for error in learner_errors:
                    print(f"- {error}", file=sys.stderr)
                return EXIT_PLATFORM
        for command in command_plan(repo, selected):
            display = " ".join(command)
            if dry_run:
                print(f"DRY-RUN / WHATIF [{selected}]: {display}")
                continue
            if not shutil.which(command[0]):
                print(f"BLOCKED: required executable is unavailable: {command[0]}", file=sys.stderr)
                return EXIT_PLATFORM
            result = subprocess.run(command, cwd=repo, text=True, check=False)
            if result.returncode != 0:
                print(f"RED [{selected}] exit {result.returncode}: {display}", file=sys.stderr)
                return EXIT_VALIDATION
        if dry_run and not command_plan(repo, selected):
            print(f"DRY-RUN / WHATIF [{selected}]: no executable checks in this mode")
        elif not dry_run:
            print(f"GREEN [{selected}]: declared checks completed.")
    return EXIT_OK


FEATURE_004_ID = "004-container-hardening-followup"
FEATURE_004_GATES = {f"G004-{number:02d}" for number in range(1, 19)}
FEATURE_004_APPLICABILITY = {"Applicable", "N/A", "Open"}
FEATURE_004_IMPLEMENTATION = {
    "Fulfilled", "Partly Fulfilled", "Not Fulfilled", "Not Assessed"
}


def validate_feature_004_assurance_profile(repo: Path) -> list[str]:
    """Bind the fourteen local manifests to the pinned project registry."""
    errors: list[str] = []
    registry = load_json(safe_repo_path(
        repo, "scripts/config/spec-kit-project-statistics-governance-presets.json"
    ))
    presets = registry.get("presets")
    if not isinstance(presets, list) or len(presets) != 14:
        return ["Feature 004 requires the fourteen-preset registry"]
    seen_ids: set[str] = set()
    seen_priorities: set[int] = set()
    for preset in presets:
        if not isinstance(preset, dict):
            errors.append("invalid preset registry entry")
            continue
        preset_id = preset.get("id")
        version = preset.get("version")
        priority = preset.get("priority")
        if (not isinstance(preset_id, str)
                or not re.fullmatch(r"[a-z0-9-]+", preset_id)
                or preset_id in seen_ids
                or not isinstance(version, str)
                or not re.fullmatch(r"v\d+\.\d+\.\d+", version)
                or isinstance(priority, bool) or not isinstance(priority, int)
                or priority in seen_priorities):
            errors.append(f"invalid or duplicate preset metadata: {preset_id}")
            continue
        seen_ids.add(preset_id)
        seen_priorities.add(priority)
        path = safe_repo_path(repo, f".specify/presets/{preset_id}/preset.yml")
        text = path.read_text(encoding="utf-8")
        ids = re.findall(r'^  id: "([^"]+)"$', text, re.MULTILINE)
        versions = re.findall(r'^  version: "([^"]+)"$', text, re.MULTILINE)
        if ids != [preset_id] or versions != [version[1:]]:
            errors.append(f"installed preset manifest differs from registry: {preset_id}")
    if "secure-development-assurance-governance" not in seen_ids:
        errors.append("Assurance preset is absent")
    else:
        assurance = next(
            item for item in presets
            if item.get("id") == "secure-development-assurance-governance"
        )
        if assurance.get("version") != "v0.1.8" or assurance.get("priority") != 15:
            errors.append("Assurance preset must be v0.1.8 at priority 15")
    preset_root = safe_repo_path(repo, ".specify/presets")
    installed_ids = {item.name for item in preset_root.iterdir() if item.is_dir()}
    if installed_ids != seen_ids:
        errors.append("installed preset directory set differs from fourteen-preset registry")
    return errors


def execute_feature_004_mode(
    repo: Path,
    mode: str,
    evidence_path: str | None,
    dry_run: bool,
    feature_directory: str,
) -> int:
    """Select Feature 004 explicitly; never reuse Feature 003 evidence paths."""
    selected = safe_repo_path(repo, feature_directory)
    if selected != safe_repo_path(repo, f"specs/{FEATURE_004_ID}") or not selected.is_dir():
        raise ValueError("--feature-directory must select specs/004-container-hardening-followup")
    requirements_path = safe_repo_path(
        repo, f"specs/{FEATURE_004_ID}/gate-requirements.json"
    )
    requirements = load_json(requirements_path)
    if dry_run:
        print(f"DRY-RUN / WHATIF [{mode}]: validate Feature 004 gate contract and evidence; no checks executed")
        return EXIT_OK
    profile_errors = validate_feature_004_assurance_profile(repo)
    if profile_errors:
        return print_result(profile_errors, "Feature 004 preset profile")
    if not evidence_path:
        raise ValueError("Feature 004 requires --evidence; no historical evidence fallback")
    document = load_json(safe_repo_path(repo, evidence_path))
    errors = validate_feature_004_evidence(
        document, requirements, repo, _sha256_raw(requirements_path)
    )
    if errors:
        return print_result(errors, f"Feature 004 {mode} evidence contract")
    mode_checks = {
        "Input": {"Q1"}, "Static": {"Q2", "Q3", "Q4"},
        "Runtime": {"Q5"}, "SupplyChain": {"Q6"},
        "Documentation": {"Q8"}, "Accessibility": {"Q8"},
        "All": {f"Q{number}" for number in range(1, 9)},
    }[mode]
    gate_checks = {
        item["gateId"]: set(item.get("quickstartChecks", []))
        for item in requirements["gates"]
    }
    relevant = [
        item for item in document["checkpoints"]
        if gate_checks.get(item["gateId"], set()) & mode_checks
    ]
    failed = [item["gateId"] for item in relevant if item["implementation"] == "Not Fulfilled"]
    if failed:
        print(f"RED [{mode}]: Not Fulfilled gates: {', '.join(failed)}", file=sys.stderr)
        return EXIT_VALIDATION
    open_gates = [
        item["gateId"] for item in relevant
        if item["implementation"] != "Fulfilled" and item["applicability"] != "N/A"
    ]
    if open_gates:
        print(f"BLOCKED [{mode}]: required Feature 004 evidence is Open: {', '.join(open_gates)}", file=sys.stderr)
        return EXIT_PLATFORM
    print(f"GREEN [{mode}]: selected Feature 004 gates have current evidence.")
    return EXIT_OK


def _sha256_raw(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _valid_digest(value: Any) -> bool:
    return isinstance(value, str) and bool(re.fullmatch(r"[0-9a-f]{64}", value))


def validate_feature_004_evidence(
    document: dict[str, Any],
    requirements: dict[str, Any],
    repo: Path,
    requirements_hash: str,
) -> list[str]:
    """Validate current project evidence without changing Feature 003 contracts."""
    errors: list[str] = []
    if requirements.get("feature") != FEATURE_004_ID or requirements.get("schemaVersion") != "1.0":
        errors.append("feature 004 requirements context is invalid")
    gates = requirements.get("gates")
    if (not isinstance(gates, list) or len(gates) != 18
            or any(not isinstance(item, dict)
                   or not isinstance(item.get("gateId"), str) for item in gates)
            or {item["gateId"] for item in gates} != FEATURE_004_GATES):
        errors.append("feature 004 requires exactly G004-01 through G004-18")
        gates = []
    if requirements.get("gateCount") != 18:
        errors.append("feature 004 gate count is invalid")
    quickstart_ids = requirements.get("quickstartCheckIds")
    if (not isinstance(quickstart_ids, list)
            or any(not isinstance(item, str) for item in quickstart_ids)
            or set(quickstart_ids) != {
        f"Q{number}" for number in range(1, 9)
    }):
        errors.append("feature 004 Q1-Q8 binding is incomplete")

    bindings = requirements.get("sourceBindings")
    if not isinstance(bindings, list) or not bindings:
        errors.append("feature 004 source bindings are missing")
        bindings = []
    seen_paths: set[str] = set()
    for index, binding in enumerate(bindings):
        if not isinstance(binding, dict):
            errors.append(f"source binding {index} must be an object")
            continue
        path_text = binding.get("path")
        if not isinstance(path_text, str) or path_text in seen_paths:
            errors.append(f"source binding {index} has missing or duplicate path")
            continue
        seen_paths.add(path_text)
        try:
            source = safe_repo_path(repo, path_text)
            if binding.get("hashKind") != "text/raw-and-utf8-lf":
                errors.append(f"source binding {path_text} hash kind is invalid")
            if binding.get("rawSha256") != _sha256_raw(source):
                errors.append(f"source binding {path_text} raw hash is stale")
            if binding.get("normalizedSha256") != normalized_sha256(source):
                errors.append(f"source binding {path_text} normalized hash is stale")
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"source binding {path_text}: {exc}")

    if document.get("schemaVersion") != "1.0" or document.get("feature") != FEATURE_004_ID:
        errors.append("feature 004 evidence context is invalid")
    if document.get("gateRequirementsSha256") != requirements_hash:
        errors.append("feature 004 gate requirements hash is stale")
    if document.get("gitHead") != requirements.get("gitHead"):
        errors.append("feature 004 Git context is stale")

    records = document.get("evidenceRecords")
    if not isinstance(records, list):
        errors.append("evidenceRecords must be an array")
        records = []
    by_id: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"evidence record {index} must be an object")
            continue
        evidence_id = record.get("evidenceId")
        if not is_nonempty_text(evidence_id) or evidence_id in by_id:
            errors.append(f"evidence record {index} has missing or duplicate ID")
            continue
        by_id[evidence_id] = record
        if record.get("gateId") not in FEATURE_004_GATES:
            errors.append(f"{evidence_id} has unknown gate")
        if record.get("gitHead") != requirements.get("gitHead"):
            errors.append(f"{evidence_id} has stale Git context")
        outcome = record.get("outcome")
        if outcome == "NotRun":
            if "exitCode" in record or "imageId" in record:
                errors.append(f"{evidence_id} invents execution data for NotRun")
            for field in ("owner", "nextAction", "trigger", "limitations"):
                if not is_nonempty_text(record.get(field)):
                    errors.append(f"{evidence_id} missing {field}")
        elif outcome in {"Passed", "Failed"}:
            for field in requirements.get("executedEvidenceRequiredFields", []):
                value = record.get(field)
                if field == "exitCode":
                    if isinstance(value, bool) or not isinstance(value, int):
                        errors.append(f"{evidence_id} missing integer exitCode")
                elif field == "commandArgv":
                    if not isinstance(value, list) or not value or not all(
                        is_nonempty_text(part) for part in value
                    ):
                        errors.append(f"{evidence_id} missing commandArgv")
                elif field == "inputHashes":
                    if not isinstance(value, dict):
                        errors.append(f"{evidence_id} missing inputHashes")
                    else:
                        for path_text, hash_record in value.items():
                            if not isinstance(hash_record, dict):
                                errors.append(f"{evidence_id} invalid hash record")
                                continue
                            try:
                                source = safe_repo_path(repo, path_text)
                                kind = hash_record.get("kind")
                                expected = (
                                    _sha256_raw(source) if kind == "rawSha256"
                                    else normalized_sha256(source)
                                    if kind == "normalizedSha256" else None
                                )
                                if expected is None or hash_record.get("digest") != expected:
                                    errors.append(
                                        f"{evidence_id} stale or wrong-kind input hash: {path_text}"
                                    )
                            except (OSError, UnicodeError, ValueError) as exc:
                                errors.append(f"{evidence_id} input hash {path_text}: {exc}")
                elif field in {"payloadSha256", "decisionSha256"}:
                    if not _valid_digest(value):
                        errors.append(f"{evidence_id} missing {field}")
                elif not is_nonempty_text(value):
                    errors.append(f"{evidence_id} missing {field}")
            parse_utc(record.get("observedAt"), f"{evidence_id}.observedAt", errors)
        else:
            errors.append(f"{evidence_id} has invalid outcome")

    checkpoints = document.get("checkpoints")
    if not isinstance(checkpoints, list):
        errors.append("checkpoints must be an array")
        checkpoints = []
    seen_gates: set[str] = set()
    for index, checkpoint in enumerate(checkpoints):
        if not isinstance(checkpoint, dict):
            errors.append(f"checkpoint {index} must be an object")
            continue
        gate_id = checkpoint.get("gateId")
        if gate_id not in FEATURE_004_GATES or gate_id in seen_gates:
            errors.append(f"checkpoint {index} has unknown or duplicate gate")
            continue
        seen_gates.add(gate_id)
        applicability = checkpoint.get("applicability")
        implementation = checkpoint.get("implementation")
        if applicability not in FEATURE_004_APPLICABILITY or implementation not in FEATURE_004_IMPLEMENTATION:
            errors.append(f"{gate_id} has invalid status enum")
        if applicability in {"N/A", "Open"} and implementation != "Not Assessed":
            errors.append(f"{gate_id} has invalid applicability/implementation pair")
        for field in ("reason", "owner", "reviewer", "residualRisk",
                      "nextAction", "dueAt", "reevaluationTrigger"):
            if not is_nonempty_text(checkpoint.get(field)):
                errors.append(f"{gate_id} missing {field}")
        evidence_ids = checkpoint.get("evidenceIds")
        if not isinstance(evidence_ids, list) or not all(
            is_nonempty_text(value) for value in evidence_ids
        ) or len(evidence_ids) != len(set(evidence_ids)):
            errors.append(f"{gate_id} evidenceIds are invalid")
            evidence_ids = []
        for evidence_id in evidence_ids:
            record = by_id.get(evidence_id)
            if record is None or record.get("gateId") != gate_id:
                errors.append(f"{gate_id} references missing or foreign evidence {evidence_id}")
        if implementation == "Fulfilled":
            if not evidence_ids or any(
                by_id.get(value, {}).get("outcome") != "Passed"
                for value in evidence_ids
            ):
                errors.append(f"{gate_id} Fulfilled lacks passed evidence")
            if gate_id in {"G004-09", "G004-12", "G004-14", "G004-16",
                           "G004-17", "G004-18"}:
                authority_path = checkpoint.get("authorityEvidence")
                if not is_nonempty_text(authority_path):
                    errors.append(f"{gate_id} requires separate human or independent review")
                else:
                    try:
                        safe_repo_path(repo, authority_path)
                    except (OSError, ValueError) as exc:
                        errors.append(f"{gate_id} authority evidence: {exc}")
    if seen_gates != FEATURE_004_GATES:
        errors.append("feature 004 checkpoint set is incomplete")
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate ADE sandbox hardening evidence.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    gaps = subparsers.add_parser("validate-gaps", help="Validate canonical gap dispositions.")
    gaps.add_argument("--repo", required=True)
    gaps.add_argument("--gaps", required=True)
    gaps.add_argument("--evidence")
    evidence = subparsers.add_parser("validate-evidence", help="Validate gate evidence.")
    evidence.add_argument("--repo", required=True)
    evidence.add_argument("--evidence", required=True)
    evidence.add_argument("--requirements", default=GATE_REQUIREMENTS_PATH)
    evidence.add_argument("--require-all-gates", action="store_true")
    both = subparsers.add_parser("validate-all", help="Validate gaps and gate evidence together.")
    both.add_argument("--repo", required=True)
    both.add_argument("--gaps", required=True)
    both.add_argument("--evidence", required=True)
    both.add_argument("--requirements", default=GATE_REQUIREMENTS_PATH)
    both.add_argument("--require-all-gates", action="store_true")
    hash_parser = subparsers.add_parser("hash", help="Print a normalized SHA-256.")
    hash_parser.add_argument("--repo", required=True)
    hash_parser.add_argument("--path", required=True)
    mode_parser = subparsers.add_parser("run-mode", help="Run one shared hardening mode.")
    mode_parser.add_argument("--repo", required=True)
    mode_parser.add_argument(
        "--mode",
        required=True,
        choices=["Input", "Static", "Runtime", "SupplyChain", "Documentation", "Accessibility", "All"],
    )
    mode_parser.add_argument("--evidence")
    mode_parser.add_argument("--feature-directory")
    mode_parser.add_argument("--dry-run", action="store_true")
    fixture_parser = subparsers.add_parser(
        "validate-fixture",
        help="Apply one declared negative fixture to the canonical gap register.",
    )
    fixture_parser.add_argument("--repo", required=True)
    fixture_parser.add_argument("--fixture", required=True)
    feature_004 = subparsers.add_parser(
        "validate-feature-004", help="Validate current Feature 004 gate evidence."
    )
    feature_004.add_argument("--repo", required=True)
    feature_004.add_argument("--evidence", required=True)
    feature_004.add_argument(
        "--requirements",
        default="specs/004-container-hardening-followup/gate-requirements.json",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    try:
        arguments = parser.parse_args(argv)
        repo = Path(arguments.repo).resolve()
        if not repo.is_dir():
            raise ValueError("--repo must name an existing directory")
        if arguments.command == "hash":
            print(normalized_sha256(safe_repo_path(repo, arguments.path)))
            return EXIT_OK
        if arguments.command == "validate-feature-004":
            requirements_path = safe_repo_path(repo, arguments.requirements)
            requirements = load_json(requirements_path)
            evidence_document = load_json(safe_repo_path(repo, arguments.evidence))
            feature_errors = validate_feature_004_evidence(
                    evidence_document, requirements, repo,
                    _sha256_raw(requirements_path),
                )
            feature_errors.extend(validate_feature_004_assurance_profile(repo))
            return print_result(feature_errors, "feature 004 evidence")
        if arguments.command == "run-mode":
            return execute_mode(
                repo, arguments.mode, arguments.evidence, arguments.dry_run,
                arguments.feature_directory,
            )
        if arguments.command == "validate-fixture":
            fixture = load_json(safe_repo_path(repo, arguments.fixture))
            if fixture.get("mutation") != "GAP-147 AlreadySatisfied without mount evidence":
                raise ValueError("unsupported negative fixture mutation")
            canonical_path = repo / "docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json"
            candidate = load_json(canonical_path)
            target = next(
                item for item in candidate["dispositions"] if item.get("gapId") == "GAP-147"
            )
            target["applicability"] = "Applicable"
            target["implementationStatus"] = "Fulfilled"
            target["consolidatedState"] = "AlreadySatisfied"
            target["evidenceIds"] = []
            target["missingEvidence"] = "Mount evidence deliberately omitted by negative fixture."
            errors = validate_gap_document(candidate, repo)
            return print_result(errors, "GAP-147 missing-mount-evidence fixture")
        gaps_document: dict[str, Any] | None = None
        evidence_document: dict[str, Any] | None = None
        requirements: dict[str, Any] | None = None
        if arguments.command in {"validate-gaps", "validate-all"}:
            gaps_document = load_json(safe_repo_path(repo, arguments.gaps))
        if arguments.command in {"validate-evidence", "validate-all"}:
            evidence_document = load_json(safe_repo_path(repo, arguments.evidence))
            requirements = load_json(safe_repo_path(repo, arguments.requirements))
        if arguments.command == "validate-gaps":
            known = None
            if arguments.evidence:
                evidence_document = load_json(safe_repo_path(repo, arguments.evidence))
                known = {
                    item.get("evidenceId")
                    for item in evidence_document.get("gateResults", [])
                    if isinstance(item, dict) and isinstance(item.get("evidenceId"), str)
                }
            return print_result(validate_gap_document(gaps_document or {}, repo, known_evidence_ids=known), "gap dispositions")
        if arguments.command == "validate-evidence":
            return print_result(
                validate_evidence_document(
                    evidence_document or {}, requirements or {}, repo, require_all_gates=arguments.require_all_gates
                ),
                "verification evidence",
            )
        if arguments.command == "validate-all":
            known = {
                item.get("evidenceId")
                for item in (evidence_document or {}).get("gateResults", [])
                if isinstance(item, dict) and isinstance(item.get("evidenceId"), str)
            }
            errors = validate_evidence_document(
                evidence_document or {}, requirements or {}, repo, require_all_gates=arguments.require_all_gates
            )
            errors.extend(validate_gap_document(gaps_document or {}, repo, known_evidence_ids=known))
            return print_result(errors, "gap dispositions and verification evidence")
        parser.error("unknown command")
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Contract or path error: {exc}", file=sys.stderr)
        return EXIT_USAGE
    return EXIT_USAGE


if __name__ == "__main__":
    raise SystemExit(main())
