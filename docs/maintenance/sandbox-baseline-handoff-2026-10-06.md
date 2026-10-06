# Technische SandboxBaseline-Uebergabe / Technical SandboxBaseline Handoff

## Identitaet und Autoritaet / Identity and Authority

DE: `SBH-2026-10-06` ist die vom Owner beauftragte repositorylokale technische
Uebergabe fuer den Governance-Abgleich. Sie bindet den historischen Abschluss
von Feature 003 und nachfolgende dokumentierte Aenderungen an die aktuelle
Quellbaseline. Sie ist keine menschliche Abnahme, Risikoakzeptanz oder
Ausfuehrungsautoritaet. Die Intake-Reihe wird hier nicht weitergeschaltet.

EN: SBH-2026-10-06 is the owner-requested repository-local technical handoff.
It binds historical Feature 003 completion and subsequently documented changes
to the current source baseline. It is not human acceptance, risk acceptance
or execution authority. This handoff does not advance the intake series.

- Source baseline: `5deacc910227bb19684c335030c26ac5a075f9a0` plus the
  hash-bound local lifecycle repair; no uncommitted product/runtime changes.
- Feature 003 study run: `8330f54b-97d1-424c-ad1a-842a3fad7be3`, Completed,
  85/85 tasks, PR #53 merge `1c67b226d5a2c7c565c8b9630376710100798894`.
- Documentation toolchain delivery: PR #88 merge
  `941bf442d06fe3f5069305ccd2c9e4b150e8ac8d`.
- CI migration: PR #90 merge `5deacc910227bb19684c335030c26ac5a075f9a0`;
  nine successful checks on `4521c9623a12b54ca984a0b7c47ad42bcc69148e`.
- Local image: `localhost/absdd-image-sandbox_ade:latest`, `linux/arm64`;
  ID `1ed9ce9a1a143431d6ddc8bde6183cdf549dee8a602cc98b06c5c59298e12e88`.
  Binding is the image ID, not the mutable latest tag.

## Quellbindungen / Source Bindings

| Pfad / Path | SHA-256 |
|---|---|
| `Dockerfile` | `4d094a538371d049d641e6651930772fdb75a9302273549aa12bc7f6b1d94feb` |
| `compose.yml` | `e54d5335d21b23fd8628ff9a6c184b17e8b9e70b47110c27ce2c75c74b878d3a` |
| `compose.home-baseline.yml` | `854989226683bde0a72e164c5bff590119a69cdc2dd0e2455f7d10494d27ee3e` |
| `scripts/smoke-test-toolchains.sh` | `693668879c601c2f3662c82e0409387ff43240e66d5430abaf74801942e8e04a` |
| Feature 003 `feasibility-study-decision.json` | `eea6c42eaaaa0a34fddb8e1c3d18cb60560d3d1192c6f53b0bb32bb7e2bc804c` |

DE: Die vier Image-/Compose-/Smoke-Quellen unterscheiden sich nicht zwischen
Toolchain-Commit `89a400f` und der genannten Quellbaseline. Dieser Vergleich
bindet die dokumentierte Build-Evidenz, ersetzt aber keinen neuen Build.

EN: The four image/Compose/smoke sources do not differ between toolchain
commit 89a400f and the stated source baseline. This comparison binds the
documented build evidence; it does not replace a new build.

## Nachweise und Grenzen / Evidence and Limits

- [Toolchain session](../security/agent-session-log/2026-10-04-0037.md): ARM64
  cached build, full toolchain smoke, documentation PDF smoke and SBOM passed.
- Local, ignored SBOM: `sboms/2026-10-04-localhost-absdd-image-sandbox_ade-latest.cdx.json`;
  SHA-256 `3fbf85c3b03a8dc60875e9306717c38d2ac8e299dd49ca514c8265614c58b299`.
  It was present and hash-checked locally; it is not a published artifact.
- [Start evidence](../security/agent-session-log/2026-10-05-1236.md) binds the
  same image ID. The container is now stopped; no current running-state claim.
- [CI reconciliation](github-actions-governance-reconciliation.md) records
  macOS 15 check names and unchanged Linux-only conditional maintenance jobs.
- Historical Feature 003 evidence stays historical; its recorded Current
  fields are not refreshed or asserted to cover later changes.

DE: `DEC-FEASIBILITY-SINGLE-PERSON-2026-09-06` begrenzt den Studienabschluss
bis 2026-12-31 auf SourceRepositoryOnly. Unabhaengiges menschliches Review und
moderierter Lernendentest bleiben NotPerformed; 49 Human-only-Punkte offen.
Die damalige N/A-Entscheidung darf nicht automatisch in einen neuen Lauf
uebernommen werden. Der Reviewer darf diese technische Uebergabe nicht mit
einer eigenstaendigen Security-Freigabe verwechseln.

EN: The feasibility decision limits the study to SourceRepositoryOnly through
2026-12-31. Independent human review and moderated learner testing remain
NotPerformed; 49 human-only items remain open. The historical N/A decision
must not be automatically transferred into a new run. This technical handoff
is not an independent security approval.

| Offener Nachweis / Open Evidence | Owner | Follow-up | Trigger |
|---|---|---|---|
| AMD64 documentation toolchain runtime | Repository Maintainer | Separate Windows and Ubuntu/WSL2 image build/smokes on the same source revision | Available platform or next acceptance run |
| Independent human Security Review | Security Review | Review current source/image and outstanding controls | Before acceptance or learner rollout |
| Real learner/A11Y acceptance and PDF accessibility | Learning/A11Y Review | Re-evaluate applicability and perform real checks | Before learner rollout or study expiry |
| 49 human-only dispositions and supply-chain triage | Respective roles in Feature 003 handoffs | Review dated role evidence; do not infer closure from CI or SBOM generation | Changed scope/image/provider or next acceptance run |

## Naechste Aktion / Next Action

DE: Nach erfolgreichem unabhaengigem Reparatur-Review die Reihe ueber einen
ausdruecklich autorisierten Series-Update fortschreiben. Dabei den historischen
Studienabschluss von einer aktuellen Abnahme trennen. Ein neuer Abnahmelauf
benoetigt eigene Autoritaet und neu bewertete Gates.

EN: After independent repair review passes, advance through an explicitly
authorized series update, keeping historical study completion distinct from
current acceptance. A new acceptance run needs separate authority and
re-evaluated gates.
