# Vertikaler RED-GREEN-Slice / Vertical RED-GREEN Slice

## Scope und Zuordnung / Scope and Mapping

Der Slice verbindet `GAP-013`, `GAP-015`, `GAP-020`, `GAP-051`, `GAP-122`,
`GAP-147`, `GAP-148`, `GAP-149` und `GAP-154` mit FR-005 bis FR-018,
AR-002 bis AR-005 sowie `GATE-GAP-01` und `GATE-STATIC-01`. Owner ist
`Repository Maintainer`, Reviewer ist `Security Review`; dies ist keine
Risikoakzeptanz. / The slice links the nine named gaps to the stated
requirements and gates. Ownership does not grant risk acceptance.

## RED

**DE:** Der Befehl
`python3 scripts/lib/secure_development_hardening.py validate-fixture --repo "$PWD" --fixture scripts/tests/fixtures/secure-development-container-hardening/gap-147-missing-mount-evidence.json`
wurde am 2026-08-30 ausgefuehrt. Beobachtet: Exit 1 und die Regel
`AlreadySatisfied requires current evidence`. Es wurden keine Mount-Quellen,
Umgebungswerte oder Secrets ausgegeben.

**EN:** The command was executed on 2026-08-30. It returned exit 1 with the
expected current-evidence rule and printed no mount source, environment value,
or secret.

## Aktuelle Inspektion / Current Inspection

- `Dockerfile` nutzt ein digest-gepinntes MCR-Basisimage und endet fuer die
  Laufzeit mit `USER adedev`. / It pins the base image by digest and ends with
  non-root runtime user `adedev`.
- `compose.yml` setzt `no-new-privileges:true`, `cap_drop: ALL` und bindet den
  Projekt-Portbereich nur an `127.0.0.1`. / Compose applies the stated
  least-privilege and localhost controls.
- `podman-compose config` bestand am 2026-08-30T13:18:46Z. Die statische,
  nicht sensible Mount-Zaehlung ergab 20 Mounts: 14 Bind-Mounts, sechs
  benannte Volumes und einen read-only-Mount. / The canonical config check
  passed with the stated non-sensitive mount counts.
- Die fuenf Agenten-Zustandsverzeichnisse fuer OpenCode, Codex, Claude,
  Gemini und Copilot liegen in getrennten benannten Volumes. / Five named
  volumes separate agent state from project code.
- `.gitignore`, `.dockerignore`, `codex/requirements.toml` und
  `opencode.jsonc` sperren reale Env-/Credentialpfade; keine Secret-Datei
  wurde gelesen. / The listed controls deny environment and credential paths;
  no secret file was read.
- Beide Codex-TOML-Dateien wurden mit Python `tomllib` erfolgreich geparst. /
  Both Codex TOML files parsed successfully.
- `scripts/build-and-sbom.sh` und `.ps1` enthalten jeweils noch einen
  `SyftImage`-Fallback auf `docker.io/anchore/syft:latest`; dies ist RED fuer
  die reproduzierbare Lieferkette. / Both SBOM entry points retain the movable
  fallback, which is a supply-chain RED finding.

## GREEN und offene Folgearbeit / GREEN and Open Follow-Up

`GAP-147` ist fuer den aktuellen statischen Compose-Scope GREEN: die Fixture
scheitert ohne Evidenz, der echte Config-Check besteht, und der Gap verweist
reziprok auf `EVD-SLICE-STATIC-001`. Die bestaetigten Produktkontrollen wurden
nicht unnoetig geaendert. `GAP-020`, `GAP-051`, `GAP-122` und `GAP-154`
bleiben teilweise erfuellt oder bis zu ihren spaeteren Runtime-/Secret-/
Supply-Chain-Gates offen. / GAP-147 is GREEN for current static Compose scope.
Confirmed controls were not changed unnecessarily. The named supply-chain,
secret-scan, and runtime-isolation items remain follow-up work for their later
gates.
