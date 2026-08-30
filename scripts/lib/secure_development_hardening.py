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
) -> int:
    gaps_path = repo / "docs/security/secure-development/2026-08-30-container-hardening/gap-dispositions.json"
    requirements_path = repo / GATE_REQUIREMENTS_PATH
    errors: list[str] = []
    try:
        gaps = load_json(gaps_path)
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
            requirements = load_json(requirements_path)
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
            learner_errors = validate_learner_result(repo)
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
        if not command_plan(repo, selected) or not dry_run:
            print(f"GREEN [{selected}]: declared checks completed.")
    return EXIT_OK


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
    mode_parser.add_argument("--dry-run", action="store_true")
    fixture_parser = subparsers.add_parser(
        "validate-fixture",
        help="Apply one declared negative fixture to the canonical gap register.",
    )
    fixture_parser.add_argument("--repo", required=True)
    fixture_parser.add_argument("--fixture", required=True)
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
        if arguments.command == "run-mode":
            return execute_mode(repo, arguments.mode, arguments.evidence, arguments.dry_run)
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
