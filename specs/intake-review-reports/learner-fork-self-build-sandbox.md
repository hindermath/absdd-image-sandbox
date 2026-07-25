# Intake Review: Forkbare Selbstbau-Sandbox / Forkable Self-Build Sandbox

## Identity

- **Review ID:** `cfbc8af4-48be-40e2-9a4b-5381d60d3dd5`
- **Mode:** `Single`
- **Policy:** `learner-a11y-bilingual`
- **Outcome:** `Ready`
- **Target:** `intakes/learner-fork-self-build-sandbox.md`
- **Normalized SHA-256:**
  `6e17c637283212954857e82b53b2eeb11fd44a3c3d9996bb677ad991064d8293`

**DE:** Der Intake ist inhaltlich konsistent und bereit fuer den getrennten
Specify-Schritt. `Ready` ist eine Review-Entscheidung, aber noch keine
Implementierungs-, Commit-, Push-, Merge- oder Plattformaenderungsfreigabe.

**EN:** The intake is internally consistent and ready for the separate Specify
step. `Ready` is a review outcome, not implementation, commit, push, merge, or
platform-change authority.

## Findings

Es wurden keine Findings festgestellt.

*No findings were identified.*

| Severity | Count |
|---|---:|
| Critical | 0 |
| High | 0 |
| Medium | 0 |
| Low | 0 |

## Questions And Decisions

Es bestehen keine offenen Review-Fragen. Die drei im Intake dokumentierten
Entscheidungen sind eindeutig:

1. Fork oder institutionelles Repository ist `origin`; die gepflegte Referenz
   ist `upstream`.
2. Es wird kein fertiges Projekt-Image ueber GHCR oder eine andere
   Projekt-Registry bereitgestellt.
3. Der Intake erteilt nur lokale Authoring-Berechtigung; weitere
   Lebenszyklus-Schritte starten getrennt.

*There are no open review questions. The intake clearly defines the
origin/upstream model, excludes a ready-made project image, and keeps later
lifecycle authority separate.*

## Coverage

| Review dimension | Status | Evidence |
|---|---|---|
| Identity, audience, purpose | Pass | Title, audience, purpose, current and target state are explicit |
| Assumed prior knowledge | Pass | No container, Podman, fork, Spec Kit, or SBOM experience is assumed |
| First-use terminology | Pass | Fork, GHCR, origin, upstream, template repository, and SBOM are explained |
| Scope and non-goals | Pass | Local self-build and fork onboarding are included; registry publication and platform changes are excluded |
| Atomic requirements | Pass | `FR-001` through `FR-015` state individual normative expectations |
| Measurable acceptance | Pass | `AC-001` through `AC-012` bind checkout, build, smoke test, registry absence, SBOM, A11Y, and validation evidence |
| Dependencies and risks | Pass | Build resources, platform differences, human-owned settings, and skipped-platform evidence are explicit |
| Security and privacy | Pass | Secrets, private paths, personal defaults, and weakened controls are excluded |
| Accessibility and language | Pass | German-first, English-second, CEFR B2, WCAG 2.2 AA, and text-first evidence are required |
| Platform and supply chain | Pass | Git-hosting neutrality, local Podman build, pinned supply-chain controls, and local CycloneDX evidence are preserved |
| Prompt alignment | Pass | Specify forbids implementation and remote writes; Autonomous is bound to `LocalImplementation` |
| Personal or secret data | Pass | No credentials, secrets, private endpoints, or unnecessary personal data are present |

## Delivery Authority

**DE:** Fuer diesen Review ist `MergeAndSync` nicht erforderlich. Das
Intake-Receipt und der Autonomous-Prompt bleiben bei `LocalImplementation`.
Die bedingte Nutzerangabe "falls notwendig" erteilt keine pauschale
Remote-Berechtigung und wird durch den Review nicht verbraucht. Eine spaetere
Auslieferung mit `MergeAndSync` benoetigt eine ausdrueckliche, zum konkreten
Lauf passende Autorisierung und die dort vorgesehenen Gates.

**EN:** `MergeAndSync` is not required for this review. The intake receipt and
Autonomous prompt remain bound to `LocalImplementation`. The user's
conditional "if necessary" statement is not treated as general remote
authority. A later `MergeAndSync` delivery requires explicit authority for
that concrete run and its required gates.

## Residual Risk

Es wurden keine Rest-Risiken akzeptiert. Ein Agent hat keine
Risikoakzeptanz erklaert.

*No residual risk was accepted. The agent did not claim risk-acceptance
authority.*

## Next Action

```text
$speckit-specify Erstelle eine Spezifikation ausschliesslich auf Grundlage von intakes/learner-fork-self-build-sandbox.md. Bewahre den Fork-/upstream-Standard, den bewussten Ausschluss eines fertigen Projekt-Images aus GHCR oder anderen Projekt-Registries, die DE-first/EN-second-Lernendenbasis, WCAG 2.2 AA, Plattformneutralitaet und alle menschlichen Stop-Grenzen. Klaere materielle Luecken, aber beginne keine Implementierung und fuehre keine Commits, Pushes, Pull Requests, Merges oder Plattformaenderungen aus.
```
