#!/usr/bin/env python3
"""Compare Chat AI /v1/models with opencode.jsonc.

The script is intentionally read-only by default. It never prints the API key.
Use --write with an explicit --stage to change opencode.jsonc.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
import json
import os
from pathlib import Path
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_API_URL = "https://chat-ai.academiccloud.de/v1/models"
DEFAULT_CONFIG_CANDIDATES = (
    Path("/ade-dev-sandbox/opencode.jsonc"),
    Path("opencode.jsonc"),
)


@dataclass(frozen=True)
class ModelEntry:
    key: str
    key_start: int
    key_end: int
    value_start: int
    value_end: int


def strip_jsonc_comments(text: str) -> str:
    """Remove // and /* */ comments while preserving string content."""
    result: list[str] = []
    i = 0
    in_string = False
    escaped = False

    while i < len(text):
        char = text[i]
        next_char = text[i + 1] if i + 1 < len(text) else ""

        if in_string:
            result.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            i += 1
            continue

        if char == '"':
            in_string = True
            result.append(char)
            i += 1
            continue

        if char == "/" and next_char == "/":
            while i < len(text) and text[i] not in "\r\n":
                i += 1
            continue

        if char == "/" and next_char == "*":
            i += 2
            while i + 1 < len(text) and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue

        result.append(char)
        i += 1

    return "".join(result)


def scan_string_end(text: str, start: int) -> int:
    if start >= len(text) or text[start] != '"':
        raise ValueError(f"expected string at offset {start}")

    i = start + 1
    escaped = False
    while i < len(text):
        char = text[i]
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == '"':
            return i + 1
        i += 1

    raise ValueError(f"unterminated string at offset {start}")


def skip_ws_comments(text: str, start: int, limit: int | None = None) -> int:
    if limit is None:
        limit = len(text)

    i = start
    while i < limit:
        if text[i].isspace():
            i += 1
            continue

        if text.startswith("//", i):
            i += 2
            while i < limit and text[i] not in "\r\n":
                i += 1
            continue

        if text.startswith("/*", i):
            end = text.find("*/", i + 2)
            if end == -1 or end + 2 > limit:
                raise ValueError(f"unterminated block comment at offset {i}")
            i = end + 2
            continue

        break

    return i


def find_matching_bracket(text: str, open_pos: int) -> int:
    opening = text[open_pos]
    closing = {"{": "}", "[": "]"}.get(opening)
    if closing is None:
        raise ValueError(f"expected object or array at offset {open_pos}")

    depth = 0
    i = open_pos
    while i < len(text):
        if text[i] == '"':
            i = scan_string_end(text, i)
            continue

        if text.startswith("//", i):
            i += 2
            while i < len(text) and text[i] not in "\r\n":
                i += 1
            continue

        if text.startswith("/*", i):
            end = text.find("*/", i + 2)
            if end == -1:
                raise ValueError(f"unterminated block comment at offset {i}")
            i = end + 2
            continue

        if text[i] == opening:
            depth += 1
        elif text[i] == closing:
            depth -= 1
            if depth == 0:
                return i
        i += 1

    raise ValueError(f"unterminated bracket at offset {open_pos}")


def find_value_end(text: str, start: int) -> int:
    start = skip_ws_comments(text, start)
    if start >= len(text):
        raise ValueError("expected JSON value at end of file")

    if text[start] in "{[":
        return find_matching_bracket(text, start) + 1

    if text[start] == '"':
        return scan_string_end(text, start)

    i = start
    while i < len(text) and text[i] not in ",}]":
        if text[i] == '"':
            i = scan_string_end(text, i)
            continue
        if text.startswith("//", i):
            break
        if text.startswith("/*", i):
            break
        i += 1
    return i


def find_models_object_span(text: str) -> tuple[int, int]:
    search_pos = 0
    while True:
        key_start = text.find('"models"', search_pos)
        if key_start == -1:
            raise SystemExit('opencode config has no "models" object')

        key_end = scan_string_end(text, key_start)
        colon_pos = skip_ws_comments(text, key_end)
        if colon_pos < len(text) and text[colon_pos] == ":":
            value_start = skip_ws_comments(text, colon_pos + 1)
            if value_start < len(text) and text[value_start] == "{":
                return value_start, find_matching_bracket(text, value_start)

        search_pos = key_end


def list_model_entries(text: str, open_pos: int, close_pos: int) -> list[ModelEntry]:
    entries: list[ModelEntry] = []
    i = open_pos + 1
    while True:
        i = skip_ws_comments(text, i, close_pos)
        if i >= close_pos:
            break
        if text[i] == ",":
            i += 1
            continue
        if text[i] != '"':
            raise SystemExit(f"unexpected token in models object at offset {i}")

        key_start = i
        key_end = scan_string_end(text, key_start)
        key = json.loads(text[key_start:key_end])
        colon_pos = skip_ws_comments(text, key_end, close_pos)
        if colon_pos >= close_pos or text[colon_pos] != ":":
            raise SystemExit(f"model entry {key!r} has no ':' separator")

        value_start = skip_ws_comments(text, colon_pos + 1, close_pos)
        value_end = find_value_end(text, value_start)
        entries.append(ModelEntry(key, key_start, key_end, value_start, value_end))
        i = value_end

    return entries


def previous_non_ws(text: str, pos: int) -> int:
    i = pos - 1
    while i >= 0 and text[i].isspace():
        i -= 1
    return i


def model_candidate_snippet(model_id: str) -> str:
    encoded = json.dumps(model_id, ensure_ascii=False)
    return (
        "        // DE: Automatisch als Chat-AI-Review-Kandidat aus /v1/models ergaenzt.\n"
        "        // EN: Automatically added as Chat AI review candidate from /v1/models.\n"
        "        // DE: Tool-Call, Agent-Zuordnung und Default-Eignung manuell pruefen.\n"
        "        // EN: Review tool-call capability, agent mapping, and default suitability manually.\n"
        f"        {encoded}: {{\n"
        f"          \"name\": {encoded},\n"
        "          \"temperature\": true,\n"
        "          \"tool_call\": false\n"
        "        }"
    )


def add_candidate_models(text: str, model_ids: list[str]) -> tuple[str, list[str]]:
    if not model_ids:
        return text, []

    open_pos, close_pos = find_models_object_span(text)
    entries = list_model_entries(text, open_pos, close_pos)
    existing = {entry.key for entry in entries}
    candidates = [model_id for model_id in model_ids if model_id not in existing]
    if not candidates:
        return text, []

    snippets = [model_candidate_snippet(model_id) for model_id in candidates]
    previous = previous_non_ws(text, close_pos)
    if entries:
        insert_pos = previous + 1
        insertion = ",\n\n" + ",\n\n".join(snippets)
    else:
        insert_pos = open_pos + 1
        insertion = "\n" + ",\n\n".join(snippets)

    return text[:insert_pos] + insertion + text[insert_pos:], candidates


def mark_unavailable_models(text: str, model_ids: list[str], report_date: str) -> tuple[str, list[str]]:
    if not model_ids:
        return text, []

    marked: list[str] = []
    open_pos, close_pos = find_models_object_span(text)
    entries = list_model_entries(text, open_pos, close_pos)
    missing = set(model_ids)

    for entry in reversed(entries):
        if entry.key not in missing:
            continue

        prefix_start = max(open_pos + 1, entry.key_start - 500)
        prefix = text[prefix_start:entry.key_start]
        if "Chat-AI-Report:" in prefix:
            continue

        marker = (
            f"        // DE: Chat-AI-Report: Am {report_date} nicht in /v1/models gesehen.\n"
            f"        // EN: Chat AI report: Not seen in /v1/models on {report_date}.\n"
            "        // DE: Nicht automatisch loeschen; Referenzen und Provider-ID pruefen.\n"
            "        // EN: Do not remove automatically; check references and provider ID.\n"
        )
        text = text[: entry.key_start] + marker + text[entry.key_start :]
        marked.append(entry.key)

    marked.reverse()
    return text, marked


def remove_model_entry(text: str, model_id: str) -> tuple[str, bool]:
    open_pos, close_pos = find_models_object_span(text)
    entries = list_model_entries(text, open_pos, close_pos)
    index_by_key = {entry.key: index for index, entry in enumerate(entries)}
    index = index_by_key.get(model_id)
    if index is None:
        return text, False

    entry = entries[index]
    if index > 0:
        start = entries[index - 1].value_end
        end = entry.value_end
    elif len(entries) > 1:
        start = open_pos + 1
        end = skip_ws_comments(text, entry.value_end, close_pos)
        if end < close_pos and text[end] == ",":
            end += 1
    else:
        start = open_pos + 1
        end = close_pos

    return text[:start] + text[end:], True


def model_references(config: dict[str, Any], model_ids: set[str]) -> dict[str, list[str]]:
    references: dict[str, list[str]] = {model_id: [] for model_id in model_ids}

    def add_reference(model_ref: Any, where: str) -> None:
        if not isinstance(model_ref, str) or not model_ref.startswith("chat-ai/"):
            return
        model_key = model_ref.removeprefix("chat-ai/")
        if model_key in references:
            references[model_key].append(where)

    add_reference(config.get("model"), "model")
    add_reference(config.get("small_model"), "small_model")

    agents = config.get("agent", {})
    if isinstance(agents, dict):
        for agent_name, metadata in agents.items():
            if isinstance(metadata, dict):
                add_reference(metadata.get("model"), f"agent.{agent_name}.model")

    return {model_id: refs for model_id, refs in references.items() if refs}


def validate_jsonc(text: str) -> None:
    try:
        json.loads(strip_jsonc_comments(text))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"updated opencode config would be invalid JSONC: {exc}") from exc


def default_config_path() -> Path:
    for candidate in DEFAULT_CONFIG_CANDIDATES:
        if candidate.exists():
            return candidate
    return DEFAULT_CONFIG_CANDIDATES[-1]


def load_opencode(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise SystemExit(f"opencode config not found: {path}") from exc

    try:
        return json.loads(strip_jsonc_comments(text))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"opencode config is not valid JSONC after comment stripping: {exc}") from exc


def fetch_model_ids(api_url: str, api_key: str, timeout: int) -> set[str]:
    request = Request(
        api_url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise SystemExit(f"Chat AI API returned HTTP {exc.code}") from exc
    except URLError as exc:
        raise SystemExit(f"Chat AI API request failed: {exc.reason}") from exc
    except TimeoutError as exc:
        raise SystemExit("Chat AI API request timed out") from exc

    data = payload.get("data")
    if not isinstance(data, list):
        raise SystemExit("Chat AI API response has no data array")

    model_ids = {item.get("id") for item in data if isinstance(item, dict)}
    return {model_id for model_id in model_ids if isinstance(model_id, str)}


def configured_models(config: dict[str, Any]) -> tuple[dict[str, str | None], dict[str, str]]:
    provider = config.get("provider", {}).get("chat-ai", {})
    models = provider.get("models", {})
    if not isinstance(models, dict):
        raise SystemExit("opencode config has no provider.chat-ai.models object")

    configured: dict[str, str | None] = {}
    for model_key, metadata in models.items():
        provider_name = metadata.get("name") if isinstance(metadata, dict) else None
        configured[model_key] = provider_name if isinstance(provider_name, str) else None

    agents = config.get("agent", {})
    agent_models: dict[str, str] = {}
    if isinstance(agents, dict):
        for agent_name, metadata in agents.items():
            if not isinstance(metadata, dict):
                continue
            model_ref = metadata.get("model")
            if isinstance(model_ref, str) and model_ref.startswith("chat-ai/"):
                agent_models[agent_name] = model_ref.removeprefix("chat-ai/")

    return configured, agent_models


def build_report(api_ids: set[str], configured: dict[str, str | None], agent_models: dict[str, str]) -> dict[str, Any]:
    configured_keys = set(configured)
    configured_provider_names = {name for name in configured.values() if name}
    configured_match_values = configured_keys | configured_provider_names

    unavailable_configured = {
        key: provider_name
        for key, provider_name in configured.items()
        if key not in api_ids and (not provider_name or provider_name not in api_ids)
    }
    stale_agent_models = {
        agent: model_key
        for agent, model_key in agent_models.items()
        if model_key not in configured_keys
    }

    return {
        "api_model_count": len(api_ids),
        "configured_model_count": len(configured),
        "configured_agent_model_count": len(agent_models),
        "api_models_not_configured": sorted(api_ids - configured_match_values),
        "configured_models_not_seen_in_api": dict(sorted(unavailable_configured.items())),
        "agent_models_without_provider_entry": dict(sorted(stale_agent_models.items())),
        "configured_models_seen_in_api": sorted(configured_match_values & api_ids),
    }


def print_text_report(report: dict[str, Any]) -> None:
    print("Chat AI model report")
    print("====================")
    print(f"API models: {report['api_model_count']}")
    print(f"Configured provider models: {report['configured_model_count']}")
    print(f"Configured agent model references: {report['configured_agent_model_count']}")
    print()

    sections = [
        ("Models in Chat AI but not configured", "api_models_not_configured"),
        ("Configured models not seen in Chat AI API", "configured_models_not_seen_in_api"),
        ("Agent model references without provider entry", "agent_models_without_provider_entry"),
        ("Configured models seen in Chat AI API", "configured_models_seen_in_api"),
    ]

    for title, key in sections:
        value = report[key]
        print(title)
        print("-" * len(title))
        if isinstance(value, dict):
            if not value:
                print("- none")
            for model_key, provider_name in value.items():
                suffix = f" (provider name: {provider_name})" if provider_name else ""
                print(f"- {model_key}{suffix}")
        else:
            if not value:
                print("- none")
            for item in value:
                print(f"- {item}")
        print()

    print("Note: opencode.jsonc contains reviewed agent, default, tool_call, and")
    print("parameter decisions. Treat this report as a review aid, not as an")
    print("automatic approval to rewrite the configuration.")


def apply_mark_stage(path: Path, report: dict[str, Any]) -> int:
    original = path.read_text(encoding="utf-8")
    updated, added = add_candidate_models(original, report["api_models_not_configured"])
    updated, marked = mark_unavailable_models(
        updated,
        list(report["configured_models_not_seen_in_api"].keys()),
        date.today().isoformat(),
    )

    validate_jsonc(updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="")

    print()
    print("Write stage: mark")
    print("-----------------")
    print(f"Added review candidates: {len(added)}")
    for model_id in added:
        print(f"- {model_id}")
    print(f"Marked unavailable configured models: {len(marked)}")
    for model_id in marked:
        print(f"- {model_id}")
    if updated == original:
        print("No file changes were necessary.")
    else:
        print(f"Updated: {path}")
    return 0


def apply_prune_stage(path: Path, config: dict[str, Any], report: dict[str, Any]) -> int:
    prune_candidates = set(report["configured_models_not_seen_in_api"].keys())
    references = model_references(config, prune_candidates)
    if references:
        print()
        print("Write stage: prune")
        print("------------------")
        print("Refusing to remove models that are still referenced:")
        for model_id, refs in sorted(references.items()):
            print(f"- {model_id}: {', '.join(refs)}")
        print("Review and change those references manually before pruning.")
        return 3

    original = path.read_text(encoding="utf-8")
    updated = original
    removed: list[str] = []
    for model_id in sorted(prune_candidates):
        updated, changed = remove_model_entry(updated, model_id)
        if changed:
            removed.append(model_id)

    validate_jsonc(updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="")

    print()
    print("Write stage: prune")
    print("------------------")
    print(f"Removed unreferenced unavailable models: {len(removed)}")
    for model_id in removed:
        print(f"- {model_id}")
    if updated == original:
        print("No file changes were necessary.")
    else:
        print(f"Updated: {path}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=default_config_path(),
        help="Path to opencode.jsonc. Defaults to /ade-dev-sandbox/opencode.jsonc when mounted, otherwise ./opencode.jsonc.",
    )
    parser.add_argument("--api-url", default=DEFAULT_API_URL, help="Chat AI models endpoint.")
    parser.add_argument("--api-key-env", default="GWDG_API_KEY", help="Environment variable containing the API key.")
    parser.add_argument("--timeout", type=int, default=30, help="API request timeout in seconds.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON instead of text.")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Rewrite opencode.jsonc. Without this flag the script only reports.",
    )
    parser.add_argument(
        "--stage",
        choices=("mark", "prune"),
        default="mark",
        help="Write stage to apply with --write: mark is non-destructive, prune removes unreferenced unavailable models.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api_key = os.environ.get(args.api_key_env)
    if not api_key:
        print(f"Missing API key environment variable: {args.api_key_env}", file=sys.stderr)
        return 2

    config = load_opencode(args.config)
    api_ids = fetch_model_ids(args.api_url, api_key, args.timeout)
    configured, agent_models = configured_models(config)
    report = build_report(api_ids, configured, agent_models)

    if args.write and args.json:
        print("--json cannot be combined with --write", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_text_report(report)

    if args.write:
        if args.stage == "mark":
            return apply_mark_stage(args.config, report)
        if args.stage == "prune":
            return apply_prune_stage(args.config, config, report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
