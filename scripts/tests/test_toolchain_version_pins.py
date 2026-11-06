#!/usr/bin/env python3
"""DE: Toolchain-Pins absichern. EN: Protect toolchain version pins."""

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


class VersionPinTests(unittest.TestCase):
    def test_release_archives_are_native_and_bound_to_independent_checks(self):
        text = (ROOT / "Dockerfile").read_text()
        sources = {
            "python": ("github.com/astral-sh/python-build-standalone/releases/download/", "python_sha256"),
            "go": ("go.dev/dl/go${GO_VERSION}.linux-${go_arch}.tar.gz", "go_sha256"),
            "syft": ("github.com/anchore/syft/releases/download/", "syft_sha256"),
            "uv": ("github.com/astral-sh/uv/releases/download/", "uv_sha256"),
            "antigravity": ("github.com/google-antigravity/antigravity-cli/releases/download/", "agy_sha256"),
        }
        for name, (source, digest_name) in sources.items():
            with self.subTest(name=name):
                self.assertIn(source, text)
                self.assertRegex(text, rf'amd64\) [^\n]*{digest_name}="[0-9a-f]{{64}}"')
                self.assertRegex(text, rf'arm64\) [^\n]*{digest_name}="[0-9a-f]{{64}}"')
                self.assertIn(f'"${{{digest_name}}}"', text)
        self.assertIn('gpg --batch --assert-signer "${swift_signing_key}"', text)
        self.assertIn('sha512sum -c -', text)

    def test_linux_swift_registry_matches_image_toolchain(self):
        text = (ROOT / "Dockerfile").read_text()
        tag = re.search(r"(?m)^ARG SWIFT_DOCKER_TAG=(\S+)$", text).group(1)
        registry = json.loads(
            (ROOT / "scripts/config/required-cli-tools-registry.json").read_text()
        )
        swift = next(tool for tool in registry["tools"] if tool["id"] == "swift")
        self.assertEqual(swift["install"]["linux"]["swiftVersion"], tag.removesuffix("-resolute"))

    def test_swift_signature_must_match_pinned_signer(self):
        text = (ROOT / "Dockerfile").read_text()
        fingerprint = "".join(("52BB7E3DE2", "8A71BE22EC", "05FFEF80A8", "66B47A981F"))
        self.assertIn(f'swift_signing_key="{fingerprint}"', text)
        self.assertIn('gpg --batch --assert-signer "${swift_signing_key}" --verify '
                      '"${tmp_dir}/swift.tar.gz.sig" "${tmp_dir}/swift.tar.gz"', text)
        self.assertNotIn('gpg --batch --verify "${tmp_dir}/swift.tar.gz.sig"', text)

    def test_syft_and_uv_archives_use_reviewed_digest_literals(self):
        text = (ROOT / "Dockerfile").read_text()
        expected = {
            "syft": {
                "amd64": "bb65249542db5fedeeb4d3f9b018b75e7264dbfbbb10486f044581a92f90490d",
                "arm64": "929bd163db2d7cd2255d3bcb8967208079813d7b46b0c952f7b794d8e2c7d304",
            },
            "uv": {
                "amd64": "c5221ff41b7892bfc223543883600125f6a47fe845093e0f5bdff4f359196d83",
                "arm64": "71279f8d3c67241e807b9d8db872d1bf541579fb9f08b7d1eb1682196d1e57dc",
            },
        }
        for tool, architectures in expected.items():
            arg = {"syft": "SYFT_VERSION", "uv": "UV_VERSION"}[tool]
            reviewed = {"syft": "1.55.0", "uv": "0.13.7"}[tool]
            version = re.search(r"(?m)^ARG " + arg + r"=(\S+)$", text).group(1)
            if version != reviewed:
                # A later automated update must retain its own version/hash proof.
                # Separate group records survive subsequent unrelated updates.
                record = json.loads((ROOT / "docs/maintenance/toolchain-update-proposals"
                                     / f"{arg.lower()}.json").read_text())
                self.assertEqual(arg, record["proposal"]["group"])
                self.assertEqual(version, record["proposal"]["updates"][arg])
                self.assertEqual("podman", record["proof"]["runtime"])
                self.assertEqual(0, record["proof"]["buildExit"])
                architectures = record["proposal"]["hashes"]
                self.assertEqual({"amd64", "arm64"}, set(architectures))
            for architecture, digest in architectures.items():
                self.assertRegex(digest, r"^[0-9a-f]{64}$")
                self.assertRegex(text, rf'{architecture}\) [^\n]*{tool}_sha256="{digest}"')
            self.assertIn(f'"${{{tool}_sha256}}" "${{tmp_dir}}/', text)
        self.assertNotIn('syft_${SYFT_VERSION}_checksums.txt" -o', text)
        self.assertNotIn('${uv_archive}.sha256" -o', text)

    def test_learner_language_versions_match_image_pins(self):
        text = (ROOT / "Dockerfile").read_text()
        profile = (ROOT / "docs/fuer-lernende/sandbox-profil.md").read_text()
        for language, arg in (("Go", "GO_VERSION"), ("Rust", "RUST_TOOLCHAIN"),
                              ("Swift", "SWIFT_DOCKER_TAG")):
            version = re.search(r"(?m)^ARG " + arg + r"=(\S+)$", text).group(1)
            version = version.removesuffix("-resolute")
            row = re.search(r"(?m)^\| \*\*" + language + r"\*\* \| ([^|]+)\|", profile)
            self.assertIsNotNone(row, language)
            self.assertEqual(row.group(1).strip(), version, language)

    def test_compat_sdk_keeps_the_base_host_and_runtime_patch(self):
        text = (ROOT / "Dockerfile").read_text()
        self.assertIn("AS dotnet-base", text)
        self.assertIn(
            "COPY --from=dotnet-base /usr/share/dotnet/dotnet /usr/share/dotnet/dotnet",
            text,
        )
        self.assertIn('newest="$(find', text)
        self.assertIn('"${path##*/}" != "${newest}"', text)

    def test_native_agent_hooks_are_narrow_and_checked(self):
        text = (ROOT / "Dockerfile").read_text()
        self.assertIn(
            "--allow-scripts=@opencode/cli,@anthropic-ai/claude-code,@github/keytar,node-pty",
            text,
        )
        self.assertNotIn("--allow-scripts=true", text)
        self.assertNotIn("--allow-scripts=*", text)
        self.assertIn("libsecret-1-0", text)
        self.assertIn("&& opencode --version", text)
        self.assertIn("&& claude --version", text)
        self.assertIn("require(p)", text)

    def test_python_is_native_and_keeps_system_interpreter(self):
        text = (ROOT / "Dockerfile").read_text()
        for architecture, target in (("amd64", "x86_64"), ("arm64", "aarch64")):
            self.assertRegex(
                text,
                architecture + r'\) python_target="' + target
                + r'"; python_sha256="[0-9a-f]{64}"',
            )
        self.assertIn('"${python_sha256}" "${tmp_dir}/${archive}" | sha256sum -c -', text)
        self.assertIn("/usr/local/bin/python3", text)
        self.assertNotIn("/opt/cpython/bin/python3 /usr/bin/", text)
        self.assertIn("openjdk-${JAVA_VERSION}-jdk-headless", text)

    def test_maven_uses_verified_upstream_not_apt(self):
        text = (ROOT / "Dockerfile").read_text()
        self.assertRegex(text, r'(?m)^ARG MAVEN_VERSION=[0-9]+\.[0-9]+\.[0-9]+$')
        self.assertRegex(text, r'maven_sha512="[0-9a-f]{128}"')
        self.assertIn('"${maven_sha512}" "${tmp_dir}/${archive}" | sha512sum -c -', text)
        self.assertIn("https://dlcdn.apache.org/maven/", text)
        self.assertIn("https://archive.apache.org/dist/maven/", text)
        self.assertNotRegex(text, r"(?m)^\s+maven \\\s*$")

    def check_maven_download(self, mode, expected_success, expected_sources):
        if os.name == "nt" or not shutil.which("sh"):
            self.skipTest("Dockerfile download fixtures require a POSIX shell")
        text = (ROOT / "Dockerfile").read_text()
        block = re.search(r'(?ms)^RUN set -eux; \\\n    tmp_dir=.*?archive="apache-maven-.*?(?=^RUN )', text).group()
        # Execute the actual download/checksum prefix, never tar or installation.
        prefix = block.split("    tar -xzf", 1)[0].removeprefix("RUN ").replace("\\\n", "\n")
        self.assertNotIn("/opt", prefix)
        version = re.search(r"(?m)^ARG MAVEN_VERSION=(\S+)$", text).group(1)
        with tempfile.TemporaryDirectory(prefix="ade-maven-download-") as directory:
            root = Path(directory)
            payload = root / "verified-archive"
            payload.write_bytes(b"isolated Maven archive fixture\n")
            checksum = hashlib.sha512(payload.read_bytes()).hexdigest()
            prefix, substitutions = re.subn(r'maven_sha512="[0-9a-f]{128}"',
                                            f'maven_sha512="{checksum}"', prefix)
            self.assertEqual(substitutions, 1)
            bin_dir = root / "bin"
            bin_dir.mkdir()
            curl = bin_dir / "curl"
            curl.write_text('''#!/bin/sh
set -eu
url=''
output=''
while [ "$#" -gt 0 ]; do
    case "$1" in
        -o) output="$2"; shift 2 ;;
        https://*) url="$1"; shift ;;
        *) shift ;;
    esac
done
printf '%s\\n' "$url" >> "$MAVEN_TEST_LOG"
case "$url" in
    https://dlcdn.apache.org/*) source=cdn ;;
    https://archive.apache.org/*) source=archive ;;
    *) exit 99 ;;
esac
case "$source:$MAVEN_TEST_MODE" in
    cdn:archive|cdn:archive-bad|cdn:missing|archive:missing)
        printf 'partial failed download' > "$output"; exit 22 ;;
    cdn:cdn-bad|archive:archive-bad)
        printf 'corrupt archive' > "$output" ;;
    *) cp "$MAVEN_TEST_PAYLOAD" "$output" ;;
esac
''')
            curl.chmod(0o755)
            if not shutil.which("sha512sum"):
                shasum = shutil.which("shasum")
                if not shasum:
                    self.skipTest("a real SHA-512 verifier is required")
                verifier = bin_dir / "sha512sum"
                verifier.write_text(f'#!/bin/sh\nexec "{shasum}" -a 512 "$@"\n')
                verifier.chmod(0o755)
            log = root / "downloads"
            environment = dict(os.environ, PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
                               TMPDIR=str(root), MAVEN_VERSION=version, MAVEN_TEST_MODE=mode,
                               MAVEN_TEST_LOG=str(log), MAVEN_TEST_PAYLOAD=str(payload))
            completed = subprocess.run(["/bin/sh", "-c", prefix], cwd=root, env=environment,
                                       capture_output=True, text=True, timeout=5)
            self.assertEqual(completed.returncode == 0, expected_success,
                             completed.stdout + completed.stderr)
            archive = f"apache-maven-{version}-bin.tar.gz"
            urls = {"cdn": f"https://dlcdn.apache.org/maven/maven-3/{version}/binaries/{archive}",
                    "archive": f"https://archive.apache.org/dist/maven/maven-3/{version}/binaries/{archive}"}
            self.assertEqual(log.read_text().splitlines(), [urls[s] for s in expected_sources])

    def test_maven_cdn_success_needs_no_archive(self):
        self.check_maven_download("cdn", True, ["cdn"])

    def test_maven_archive_fallback_keeps_pinned_version(self):
        self.check_maven_download("archive", True, ["cdn", "archive"])

    def test_maven_bad_cdn_checksum_does_not_fall_back(self):
        self.check_maven_download("cdn-bad", False, ["cdn"])

    def test_maven_bad_archive_checksum_fails_closed(self):
        self.check_maven_download("archive-bad", False, ["cdn", "archive"])

    def test_maven_unavailable_sources_fail_closed(self):
        self.check_maven_download("missing", False, ["cdn", "archive"])

    def test_lts_args_remain_major_numbers(self):
        config = json.loads((ROOT / "scripts/config/toolchain-pins.json").read_text())
        text = (ROOT / "Dockerfile").read_text()
        self.assertEqual("podman", config["runtime"])
        self.assertEqual("10.0.403-resolute", config["baseImage"]["tag"])
        self.assertRegex(text, r"(?m)^ARG NPM_VERSION=12\.[0-9]+\.[0-9]+$")
        self.assertIn('"npm@${NPM_VERSION}"', text)
        for arg, channel in (("JAVA_VERSION", "25"), ("NODE_MAJOR", "24")):
            major = re.search(r"(?m)^ARG " + arg + r"=([0-9]+)$", text).group(1)
            pin = next(pin for pin in config["pins"] if pin["arg"] == arg)
            self.assertEqual(channel, major)
            self.assertEqual(channel, pin["channel"])


if __name__ == "__main__":
    unittest.main()
