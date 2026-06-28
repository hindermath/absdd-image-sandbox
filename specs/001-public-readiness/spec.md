# Feature Specification: Sandbox Public Readiness

**Feature Branch**: `001-public-readiness`
**Created**: 2026-06-26
**Status**: Draft
**Input**: User description: "Nutze Lastenheft_Sandbox-Public-Readiness.md als verbindliche Eingabedatei. Erstelle die Feature-Spezifikation fuer die Public-Readiness von absdd-image-sandbox als Ausbildungs-Sandbox. Ziel: Interne oder organisationsspezifische Formulierungen in generische Sprache ueberfuehren, ohne Sicherheitsanforderungen zu verwaessern. Das Repo soll perspektivisch fuer Fachinformatik-Auszubildende oeffentlich nutzbar werden. Beruecksichtige README, AGENTS.md, CLAUDE.md, GEMINI.md, .github/copilot-instructions.md, COMPLIANCE-PLAN_RL-SE-001.md, docs/security/ und bestehende Lastenhefte. Starte keinen Container-Build und schalte das Repo nicht auf Public."

## Clarifications

### Session 2026-06-28

- Q: How should organization-specific audit references be handled across
  public-readiness surfaces? → A: User-facing and agent-guidance surfaces use
  generic wording; security and audit evidence may retain organization-specific
  origin when it is explicitly marked as context, example, or not
  public-release-relevant evidence.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Public Training Reader Understands the Sandbox (Priority: P1)

A Fachinformatik apprentice or trainer reviews the repository and can understand
what the sandbox is for, how it is bounded, and which security statements are
examples, open items, or active rules without needing private organizational
context.

**Why this priority**: Public readiness fails if the primary audience cannot
distinguish reusable training guidance from internal assumptions.

**Independent Test**: Review the user-facing documentation from a clean-reader
perspective and confirm that the sandbox purpose, non-goals, optional
home-baseline relationship, and security evidence status are understandable
without private access.

**Acceptance Scenarios**:

1. **Given** a reader who has no internal organizational context, **When** they
   read the public-facing documentation, **Then** they can identify the sandbox
   purpose, supported training audience, and setup boundaries.
2. **Given** a reader sees a security or compliance document, **When** it
   contains an approval, provider, or legal status, **Then** the status is
   marked as active evidence, `Open`, `N/A`, or `_TODO_` with a rationale.

---

### User Story 2 - Maintainer Neutralizes Private Assumptions (Priority: P2)

A maintainer can inspect repository guidance and identify language that assumes
private host paths, private URLs, organization-specific roles, non-public
services, or account-specific defaults, then replace it with generic wording
that preserves the original security intent.

**Why this priority**: The repository can only become public-ready if reusable
guidance is separated from private or organization-bound assumptions.

**Independent Test**: Scan the public-readiness surfaces and verify that any
remaining private or organization-specific references are either removed,
generalized, or explicitly documented as examples or open decisions.

**Acceptance Scenarios**:

1. **Given** a repository document mentions a private path, private service, or
   organization-specific approval role, **When** the public-readiness review is
   applied, **Then** user-facing and agent-guidance text is generalized, while
   security or audit evidence either generalizes the wording or marks the
   organization-specific origin as context, example, or not public-release-
   relevant evidence.
2. **Given** a security requirement is organization-specific in origin, **When**
   it is rewritten, **Then** the resulting text still preserves the control
   objective and does not weaken the requirement.

---

### User Story 3 - Reviewer Verifies Evidence and Boundaries (Priority: P3)

A reviewer can verify that public-readiness changes did not claim a stronger
security, legal, provider, or release status than the repository can prove.

**Why this priority**: Public documentation must avoid both oversharing and
overclaiming; unresolved decisions must remain visible.

**Independent Test**: Review acceptance evidence and confirm that no document
claims public release, formal sandbox approval, provider readiness, or completed
legal review unless an evidence path exists.

**Acceptance Scenarios**:

1. **Given** the repository remains private or unreleased, **When** public
   readiness documentation is complete, **Then** it states readiness work
   without switching the repository to public or implying release completion.
2. **Given** a compliance field depends on an owner, reviewer, or platform
   decision, **When** the documentation is reviewed, **Then** the field remains
   `Open`, `N/A`, or `_TODO_` rather than being invented.

### Edge Cases

- A document contains a real private URL or host path that is still needed as
  historical evidence; it must be converted to a generic example or marked as
  non-public evidence rather than copied into public-facing instructions.
- A security control is tied to an internal guideline; the control objective
  must remain, but the wording must not require readers to know or access that
  internal source.
- An evidence document contains an unresolved approval, provider, or legal
  question; the unresolved state must stay explicit and must not be presented
  as completed public readiness.
- A file is maintained across multiple agent surfaces; public-readiness wording
  must remain consistent across all maintained surfaces or document the
  intentional deviation.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The repository MUST define the sandbox as a public-ready training
  and work environment for secure development without presenting it as a
  production system.
- **FR-002**: User-facing documentation MUST use generic language for public
  readers and MUST remove or neutralize private host paths, private URLs,
  organization-bound assumptions, and account-specific defaults.
- **FR-003**: Maintained agent guidance surfaces MUST follow the same generic
  wording rule as user-facing documentation.
- **FR-004**: Security and compliance documentation MUST preserve control
  objectives while replacing organization-specific phrasing with reusable
  wording or marking organization-specific audit origin as context, example, or
  not public-release-relevant evidence.
- **FR-005**: Open approval, provider, model, data-residency, licensing, legal,
  or platform decisions MUST be marked as `Open`, `N/A`, or `_TODO_` with a
  short rationale instead of being inferred.
- **FR-006**: Documentation MUST describe `home-baseline` as an optional
  governance and template basis, not as a private mandatory path or account.
- **FR-007**: The public-readiness feature MUST NOT build the container image,
  change the repository visibility, rotate secrets, configure provider access,
  or change model access.
- **FR-008**: Maintained agent guidance surfaces MUST stay consistent when
  shared public-readiness wording changes; intentional deviations MUST be
  documented.
- **FR-009**: Documentation intended for apprentices MUST remain bilingual where
  the surrounding content is bilingual, use clear CEFR-B2-friendly wording, and
  stay friendly to text-oriented assistive technologies.
- **FR-010**: Evidence-style documents MUST distinguish active evidence,
  example evidence, unresolved follow-up, and non-applicable controls.
- **FR-011**: The feature MUST preserve auditability by retaining concrete
  evidence paths or explicit follow-up owners/triggers for open checkpoints.

### Governance Applicability

- **Primary implementation language**: Not applicable. This is a documentation
  and governance specification for a container-training repository, not a
  product runtime implementation. Memory-safe-language assessment remains
  relevant for documented training scope and later sandbox self-checks.
- **NIST SSDF**: Applicable as secure-development guidance for repository
  documentation and evidence classification.
- **CWE Top 25**: `N/A` for this specify run because no application code or
  vulnerability remediation is implemented.
- **OWASP ASVS**: `N/A` for this specify run because no web application,
  authentication flow, or service behavior is implemented.
- **SBOM**: Applicable as an existing evidence topic; public-readiness wording
  must not claim a generated SBOM unless evidence exists.
- **VEX**: Applicable as a planned or evidence-classified topic for later image
  and dependency vulnerability context; unresolved status must remain visible.
- **AI-SBOM**: Applicable for AI-tool inventory wording and provider/model
  transparency; unknown owner fields remain open.
- **SLSA**: Applicable as supply-chain evidence terminology for build integrity;
  this run must classify it without creating new build attestations.
- **BSI C3A / C5**: `N/A` for this specify run unless documentation claims a
  cloud-service deployment or provider-dependent production operation.
- **Threat modeling / Zero Trust**: Limited applicability. Public-readiness
  affects documentation trust boundaries and disclosure risk, but does not add
  runtime behavior.
- **Architecture evidence**: Existing architecture/security evidence may need
  wording updates; new runtime ADRs are not required unless a later plan changes
  deployment or trust boundaries.
- **Cross-platform scripts**: `N/A` for this specify run because no
  script-shaped tool is added, changed, or removed.
- **Accessibility evidence**: Applicable for user-facing documentation; updates
  should preserve readable Markdown structure and bilingual accessibility where
  already established.

### Key Entities

- **Public-Readiness Surface**: A repository file or documentation group that a
  public reader may use to understand setup, security, governance, or training
  workflow.
- **Private Assumption**: A private path, URL, account, organization-specific
  role, non-public service, or context-bound statement that cannot be required
  of public readers.
- **Evidence Classification**: The status assigned to a security or compliance
  statement: active evidence, example evidence, `Open`, `N/A`, or `_TODO_`.
- **Maintained Agent Surface**: Shared guidance files that must remain aligned
  when public-readiness wording changes.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A reviewer can inspect all public-readiness surfaces and find no
  mandatory private host path, private URL, private account, or non-public
  provider requirement in reusable setup instructions.
- **SC-002**: 100% of remaining organization-specific audit references in
  security evidence are explicitly classified as context, example, or not
  public-release-relevant evidence.
- **SC-003**: 100% of unresolved approval, provider, legal, data-residency, or
  platform decisions in reviewed security documents are marked as `Open`,
  `N/A`, or `_TODO_` with a short rationale.
- **SC-004**: A new reader can identify the sandbox purpose, non-goals, and
  public-readiness status from the primary documentation in under 10 minutes.
- **SC-005**: All shared agent guidance surfaces affected by the change either
  contain aligned wording or document an intentional deviation.
- **SC-006**: No acceptance evidence claims that the repository has been made
  public, the container has been rebuilt, or formal approval has been granted
  unless a separate evidence path proves that action.

## Assumptions

- Public readiness means preparing wording, evidence classification, and reader
  guidance; it does not mean changing repository visibility.
- The repository remains a training and development sandbox, not a production
  runtime or product artefact.
- Existing security controls must be preserved in intent even when their
  organization-specific wording is generalized.
- Existing bilingual and accessibility-oriented documentation practices remain
  in force where surrounding files already use them.
- Later planning may decide exact file edits, but this specification treats
  README, agent guidance, compliance/security documents, and existing
  Lastenhefte as the review surface.
