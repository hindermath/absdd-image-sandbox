#!/usr/bin/env python3
"""Validate installed Spec Kit command surfaces and preset profiles."""

from __future__ import annotations

from collections import Counter
import json
import hashlib
import re
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit


REPOSITORY = Path(__file__).resolve().parents[2]
PRESETS = REPOSITORY / ".specify" / "presets"
CONFIG = REPOSITORY / "scripts" / "config"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalized_hash(path: Path) -> str:
    raw = path.read_bytes()
    try:
        raw = raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    except UnicodeDecodeError:
        pass  # Binary evidence remains byte-exact; text permits only newline/BOM parity.
    return hashlib.sha256(raw).hexdigest()


def payload_binding(root: Path) -> dict:
    if root.is_symlink() or not root.is_dir():
        raise ValueError("installed preset must be a regular directory")
    entries = []
    # POSIX string ordering is stable across hosts; Windows Path ordering folds case.
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        if path.is_symlink():
            raise ValueError("symlink in installed preset")
        if path.is_file():
            entries.append([path.relative_to(root).as_posix(), normalized_hash(path)])
    data = json.dumps(entries, separators=(",", ":")).encode("utf-8")
    return {"fileCount": len(entries), "contentSha256": hashlib.sha256(data).hexdigest()}


def validate_installed_lock(root: Path, lock: dict) -> None:
    if lock.get("schemaVersion") != 1 or lock.get("hashContract") != "sha256-utf8-lf-bom-or-raw-v1":
        raise ValueError("unsupported installed-state contract")
    if not re.fullmatch(r"[0-9a-f]{40}", lock.get("baselineCommit", "")):
        raise ValueError("missing immutable installation baseline")
    registry_path = root / ".registry"
    if registry_path.is_symlink():
        raise ValueError("installed registry must not be a symlink")
    if normalized_hash(registry_path) != lock["registrySha256"]:
        raise ValueError("installed registry hash drift")
    registry = read_json(registry_path)["presets"]
    entries = lock["presets"]
    expected = {entry["id"]: entry for entry in entries}
    if len(expected) != len(entries) or set(expected) != set(registry):
        raise ValueError("installed preset coverage drift")
    actual_directories = {path.name for path in root.iterdir() if path.is_dir() and path.name != ".cache"}
    if actual_directories != set(expected):
        raise ValueError("installed directory coverage drift")
    for preset_id, entry in expected.items():
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", preset_id):
            raise ValueError("unsafe installed preset ID")
        installed = registry[preset_id]
        for field in ("version", "priority", "enabled", "manifest_hash"):
            if installed[field] != entry[field]:
                raise ValueError(f"installed {field} drift: {preset_id}")
        manifest = root / preset_id / "preset.yml"
        digest = "sha256:" + normalized_hash(manifest)
        if digest != entry["manifest_hash"]:
            raise ValueError(f"installed manifest hash drift: {preset_id}")
        version = re.search(r'^\s+version:\s*"([^"\s]+)"\s*$', manifest.read_text(encoding="utf-8-sig"), re.M)
        if not version or version[1] != entry["version"]:
            raise ValueError(f"installed manifest version drift: {preset_id}")
        if payload_binding(root / preset_id) != {key: entry[key] for key in ("fileCount", "contentSha256")}:
            raise ValueError(f"installed payload drift: {preset_id}")


def validate_release_sources(config: Path, lock: dict) -> None:
    entries = lock["presets"]
    sources = {entry["id"]: entry for entry in entries}
    if len(sources) != len(entries):
        raise ValueError("duplicate release source ID")
    for path in config.glob("*governance-presets.json"):
        profile = read_json(path)["presets"]
        if len({entry["id"] for entry in profile}) != len(profile):
            raise ValueError("duplicate profile preset ID")
        for entry in profile:
            if entry["id"] not in sources:
                raise ValueError(f"missing release source: {entry['id']}")
            source = sources[entry["id"]]
            if (entry["version"] != source["tag"] or entry["archiveUrl"] != source["archiveUrl"]
                    or entry["repository"] != source["repository"]):
                raise ValueError(f"release source drift: {entry['id']}")


def strip_frontmatter(text: str) -> str:
    normalized = text.replace("\r\n", "\n")
    if normalized.startswith("---\n"):
        end = normalized.find("\n---\n", 4)
        if end >= 0:
            normalized = normalized[end + 5 :]
    return normalized.strip()


def command_path(surface: str, command: str) -> Path:
    skill = command.replace(".", "-")
    layouts = {
        "agy": REPOSITORY / ".agents" / "skills" / skill / "SKILL.md",
        "codex": REPOSITORY / ".agents" / "skills" / skill / "SKILL.md",
        "claude": REPOSITORY / ".claude" / "skills" / skill / "SKILL.md",
        "copilot": REPOSITORY / ".github" / "agents" / f"{command}.agent.md",
        # The tracked OpenCode contract uses the singular ``command`` path.
        # A machine-local ``commands`` cache must never redirect parity checks.
        "opencode": REPOSITORY / ".opencode" / "command" / f"{command}.md",
    }
    return layouts[surface]


class SpecKitAgentSurfaceParityTests(unittest.TestCase):
    def test_composed_governance_commands_retain_all_wrappers_on_every_surface(self) -> None:
        # DE: Einzelbesitzer-Paritaet erkennt verlorene Wrapper nicht.
        # EN: Single-owner parity cannot detect lost wrappers on shared commands.
        wrappers = ("Security", "Architecture", "iSAQB Architecture", "A11Y", "Cross-Platform", "Agent Parity")
        for command in ("speckit.specify", "speckit.plan", "speckit.tasks"):
            for surface in ("agy", "codex", "claude", "copilot", "opencode"):
                body = strip_frontmatter(command_path(surface, command).read_text(encoding="utf-8"))
                self.assertNotIn("{CORE_TEMPLATE}", body, f"unexpanded core: {surface}/{command}")
                for wrapper in wrappers:
                    self.assertIn(f"apply the {wrapper} Governance preset:", body,
                                  f"missing wrapper: {wrapper}/{surface}/{command}")
                self.assertIn("C3A-/C5-Evidence-Vertrag", body, f"missing architecture contract: {surface}/{command}")

    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = read_json(PRESETS / ".registry")["presets"]

    def test_registered_commands_have_all_maintained_surfaces(self) -> None:
        checked: set[tuple[str, str]] = set()
        for preset in self.registry.values():
            for surface in ("agy", "codex", "claude", "copilot", "opencode"):
                for command in preset.get("registered_commands", {}).get(surface, []):
                    key = (surface, command)
                    if key in checked:
                        continue
                    checked.add(key)
                    path = command_path(surface, command)
                    self.assertTrue(path.is_file(), f"missing {surface} surface: {path}")

                    if surface == "copilot":
                        prompt = (
                            REPOSITORY
                            / ".github"
                            / "prompts"
                            / f"{command}.prompt.md"
                        )
                        self.assertTrue(prompt.is_file(), f"missing Copilot prompt: {prompt}")
                        self.assertIn(
                            f"agent: {command}",
                            prompt.read_text(encoding="utf-8"),
                        )

    def test_single_owner_commands_preserve_the_canonical_body(self) -> None:
        owners = Counter()
        commands_by_preset: dict[str, set[str]] = {}
        for preset_id, preset in self.registry.items():
            commands = set(preset.get("registered_commands", {}).get("codex", []))
            commands_by_preset[preset_id] = commands
            owners.update(commands)

        for preset_id, commands in commands_by_preset.items():
            for command in sorted(commands):
                if owners[command] != 1:
                    continue
                source = PRESETS / preset_id / "commands" / f"{command}.md"
                self.assertTrue(source.is_file(), f"missing canonical command: {source}")
                body = strip_frontmatter(source.read_text(encoding="utf-8"))
                for surface in ("codex", "claude", "copilot", "opencode"):
                    target = command_path(surface, command)
                    if not target.is_file():
                        continue
                    rendered = strip_frontmatter(target.read_text(encoding="utf-8"))
                    self.assertIn(
                        body,
                        rendered,
                        f"canonical body drift: {surface} {command}",
                    )

    def test_preset_profiles_preserve_the_canonical_entries(self) -> None:
        canonical_items = read_json(
            CONFIG / "spec-kit-governance-presets.json"
        )["presets"]
        canonical = {item["id"]: item for item in canonical_items}

        for config in sorted(CONFIG.glob("spec-kit-*-governance-presets.json")):
            profile = {item["id"]: item for item in read_json(config)["presets"]}
            for preset_id, expected in canonical.items():
                if preset_id in profile:
                    self.assertEqual(
                        profile[preset_id],
                        expected,
                        f"canonical preset drift in {config.name}: {preset_id}",
                    )

        for preset_id, expected in canonical.items():
            installed = self.registry[preset_id]
            self.assertEqual(installed["version"], expected["version"].removeprefix("v"))
            self.assertEqual(installed["priority"], expected["priority"])


    def test_gsdb_rollout_installed_payload_and_release_bindings(self) -> None:
        # Preserve the distinction between release provenance and observed installation.
        validate_installed_lock(PRESETS, read_json(REPOSITORY / "docs/maintenance/gsdb-344-preset-installed-lock.json"))
        validate_release_sources(CONFIG, read_json(REPOSITORY / "docs/maintenance/gsdb-344-preset-source-lock.json"))


    def test_gsdb_source_navigation_and_level0_scope(self) -> None:
        register = read_json(REPOSITORY / "docs/maintenance/gsdb-344-external-references.json")
        commit = register["sourceCommit"]
        self.assertRegex(commit, r"^[0-9a-f]{40}$")
        paths = [entry["path"] for entry in register["references"]]
        self.assertEqual(len(paths), len(set(paths)))
        for entry in register["references"]:
            path = entry["path"]
            self.assertTrue(path.startswith("docs/maintenance/"))
            self.assertNotIn("..", Path(path).parts)
            self.assertEqual(entry["sourceCommit"], commit)
            self.assertRegex(entry["sourceNormalizedSha256"], r"^[0-9a-f]{64}$")
            self.assertEqual(entry["url"], f"https://github.com/hindermath/home-baseline/blob/{commit}/{path}")
            pointer = REPOSITORY / path
            text = pointer.read_text(encoding="utf-8")
            for token in ("Level0SourceReference", commit, entry["url"], entry["sourceNormalizedSha256"]):
                self.assertIn(token, text)
            if pointer.suffix == ".json":
                data = read_json(pointer)
                self.assertEqual(data["documentType"], "Level0SourceReference")
                self.assertNotIn("overallOutcome", data)
                self.assertNotIn("humanDecisions", data)
        for document in (REPOSITORY / "docs/secure-development").rglob("*.md"):
            for link in re.findall(r"\]\(([^)\s]+)\)", document.read_text(encoding="utf-8")):
                parsed = urlsplit(link)
                if not parsed.scheme and not parsed.netloc and parsed.path:
                    self.assertTrue((document.parent / unquote(parsed.path)).exists(), f"Missing source link: {document}: {link}")


if __name__ == "__main__":
    unittest.main()
