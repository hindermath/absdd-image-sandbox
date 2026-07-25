<!-- intake-authoring:begin -->
# Forkbare Selbstbau-Sandbox fuer Lernende / Forkable Self-Build Sandbox for Learners

**Status:** ReadyForReview
**Audience:** Fachinformatiker*innen, Kaufleute fuer IT-System-Management,
Kaufleute fuer Digitalisierungsmanagement ab dem ersten Ausbildungsjahr sowie
weitere Nutzende der Sandbox / IT specialist apprentices, IT system management
apprentices, digitalization management apprentices from the first training
year, and other sandbox users
**Assumed prior knowledge:** Grundlegende Bedienung eines Computers und eines
Terminals; keine Erfahrung mit Containern, Podman, Forks, Spec Kit oder
Software Bills of Materials wird vorausgesetzt. / Basic computer and terminal
use; no prior experience with containers, Podman, forks, Spec Kit, or software
bills of materials is assumed.
**Profile:** learner-a11y-bilingual

## Purpose

Das Repository soll als lernorientierte Ausgangsbasis genutzt werden koennen.
Lernende und andere Nutzende holen sich eine eigene, beschreibbare Kopie,
lesen die Dokumentation und bauen das Container-Image selbst. Ein **Fork** ist
eine serverseitige Kopie eines Git-Repositorys, die auf vielen Plattformen die
Beziehung zur gepflegten Referenz beibehaelt.

*The repository should work as a learner-oriented starting point. Learners and
other users obtain their own writable copy, read the documentation, and build
the container image themselves. A **fork** is a server-side copy of a Git
repository that, on many platforms, keeps a relationship to the maintained
reference.*

Der Selbstbau ist ein Lernziel. Deshalb wird kein fertiges Sandbox-Image in der
GitHub Container Registry (GHCR) oder einer anderen Projekt-Registry als
normaler Bezugsweg bereitgestellt. GHCR ist die Container-Registry von GitHub.

*Building the image is a learning objective. Therefore, no ready-made sandbox
image in GitHub Container Registry (GHCR) or another project registry is
provided as the normal distribution path. GHCR is GitHub's container
registry.*

## Current State

- `compose.yml` baut das Image bereits lokal aus dem `Dockerfile`; es
  referenziert kein vorgebautes Projekt-Image.
- Die Einstiegsdokumentation beschreibt Installation, Build, Start,
  Tool-Pruefung, VS-Code-Zugriff und sauberes Stoppen.
- Das Level-0-Muster nutzt eine eigene Lernenden-Kopie als `origin` und die
  gepflegte Referenz als `upstream`. `origin` ist das Repository, in das die
  lernende Person schreibt; `upstream` liefert spaetere Aktualisierungen.
- GitHub ist nur ein moegliches Profil. Institutionelle Git-Systeme, GitLab,
  Codeberg und Forgejo muessen weiter unterstuetzt werden.
- Es gibt derzeit keinen Workflow, der das Sandbox-Image nach GHCR
  veroeffentlicht.

*Compose already builds locally, learner documentation exists, and the Level-0
model distinguishes a writable `origin` from the maintained `upstream`.
GitHub is one supported profile among several Git-capable platforms. No
current workflow publishes the sandbox image to GHCR.*

## Target State

Ein neuer Nutzer kann die gepflegte Referenz forken oder eine von der
Institution bereitgestellte Kopie verwenden, den Checkout ohne private
Voreinstellungen konfigurieren und das Image anhand eines geordneten
Lernpfads selbst bauen. Die Dokumentation erklaert den Unterschied zwischen
Fork und GitHubs optionaler Funktion **Use this template**: Ein
Template-Repository erzeugt ein unabhaengiges neues Repository und besitzt
nicht automatisch die fuer Aktualisierungen wichtige Fork-Beziehung.

*A new user can fork the maintained reference or use an
institution-provided copy, configure the checkout without private defaults,
and build the image through an ordered learning path. The documentation
explains the difference between a fork and GitHub's optional **Use this
template** feature: a template creates an independent repository and does not
automatically keep the fork relationship needed for updates.*

Der primaere Lernweg ist deshalb Fork oder institutionelle Kopie mit
`origin`/`upstream`. Eine GitHub-Template-Einstellung darf nur als optionales
Profil bewertet werden. Ihre Aktivierung bleibt eine menschliche
Plattformentscheidung.

*The primary learning path is therefore a fork or institutional copy with
`origin` and `upstream`. A GitHub template setting may only be evaluated as an
optional profile. Enabling it remains a human platform decision.*

## Scope

- Eignung des Repositorys als forkbare, lernorientierte Ausgangsbasis pruefen
  und verbleibende Luecken dokumentieren.
- Einen DE-first/EN-second Einstieg fuer Fork, Klonen, `origin`, `upstream`,
  lokale Konfiguration, Build, Start, Smoke-Test und Aktualisierung schaffen.
- Den lokalen Selbstbau mit Podman als verbindlichen Standardweg festhalten.
- Den bewussten Ausschluss eines fertig bereitgestellten Projekt-Images
  dokumentieren und technisch gegen unbeabsichtigte Registry-Publikation
  absichern.
- GitHub, GitLab, Codeberg, Forgejo und institutionelle Git-Systeme als
  unterschiedliche Bezugsprofile beruecksichtigen.
- Die bestehende Sicherheits-, Lieferketten-, A11Y- und
  Agenten-Paritaets-Governance erhalten.

*Scope includes readiness assessment, bilingual fork and build onboarding,
local Podman self-build as the standard path, safeguards against accidental
image publication, multiple Git-hosting profiles, and preservation of existing
governance.*

## Non-Goals

- Kein Build und keine Veroeffentlichung eines fertigen Projekt-Images in
  GHCR, Docker Hub oder einer anderen Projekt-Registry.
- Keine automatische Erstellung persoenlicher oder institutioneller
  Repositories.
- Keine automatische Aktivierung der GitHub-Einstellung `Template repository`.
- Keine Aenderung von Plattform-Rulesets, Branch Protection, Accounts,
  Berechtigungen oder Providerfreigaben.
- Keine Aufnahme echter Zugangsdaten, Tokens, privater Hostpfade oder
  personenspezifischer Standardwerte.
- Keine Vereinfachung durch Entfernen von Sicherheitspruefungen,
  Versions-Pinnings, SBOM-Erzeugung oder Agenten-Isolation.

*Non-goals include publishing a ready-made image, creating remote
repositories, changing GitHub settings or governance, storing personal data or
secrets, and weakening existing security controls.*

## Requirements

- **FR-001:** Die Dokumentation MUSS den primaeren Bezugsweg als persoenlichen
  Fork oder institutionell bereitgestelltes Repository beschreiben.
- **FR-002:** Die Dokumentation MUSS `origin` als beschreibbare Lernenden-Kopie
  und `upstream` als gepflegte Referenz erklaeren und die Befehle zum
  Einrichten, Pruefen und spaeteren Aktualisieren zeigen.
- **FR-003:** GitHub DARF nicht als allgemeine Voraussetzung dargestellt
  werden. Ein GitHub-Konto ist nur fuer den direkten GitHub-Fork oder die
  optionale Anmeldung bei GitHub Copilot erforderlich.
- **FR-004:** Die Begriffe Fork und GitHub-Template MUESSEN beim ersten
  Auftreten erklaert und hinsichtlich Aktualisierbarkeit deutlich
  unterschieden werden.
- **FR-005:** Der normale Startweg MUSS das Image lokal mit
  `podman compose build --pull` bauen und danach mit Compose starten.
- **FR-006:** `compose.yml`, CI-Konfiguration und Einstiegsdokumentation DUERFEN
  kein vorgebautes Projekt-Image aus GHCR oder einer anderen Projekt-Registry
  als Ersatz fuer den Selbstbau referenzieren.
- **FR-007:** Das Repository DARF keinen automatischen Workflow enthalten, der
  das fertige Sandbox-Image in eine Registry pusht. Ein spaeterer
  Registry-Workflow erfordert eine neue, ausdrueckliche Anforderung.
- **FR-008:** Der Einstieg MUSS erklaeren, welche lokalen Dateien aus Vorlagen
  erzeugt werden, warum sie ignoriert bleiben und wo Secrets niemals
  eingetragen werden duerfen.
- **FR-009:** Der Lernpfad MUSS Voraussetzungen, erwarteten Speicher- und
  Zeitbedarf, Build-Fortschritt, typische Fehler und einen erfolgreichen
  Abschluss in geordneter Textform beschreiben.
- **FR-010:** Nach dem Build MUSS eine dokumentierte Pruefung mindestens
  OpenCode, Codex, Claude Code, Antigravity CLI, GitHub Copilot CLI, Syft und
  die sechs Sprach-Toolchains abdecken.
- **FR-011:** Die lokale CycloneDX-SBOM-Erzeugung MUSS als Lern- und
  Lieferkettennachweis erhalten bleiben. Eine SBOM ist eine strukturierte Liste
  der Softwarebestandteile eines Images.
- **FR-012:** Der Aktualisierungsweg MUSS zeigen, wie Lernende Aenderungen aus
  `upstream` pruefen und in ihre eigene Kopie uebernehmen, ohne eigene lokale
  Konfiguration oder Projektarbeit zu ueberschreiben.
- **FR-013:** Eine optionale GitHub-Template-Nutzung MUSS, falls sie empfohlen
  wird, als separates Profil dokumentiert werden und darf den
  Fork-/Upstream-Standard nicht verdraengen.
- **FR-014:** Plattformseitige Einstellungen wie `Template repository` oder
  Branch Protection MUESSEN als menschlich auszufuehrende Schritte markiert
  werden; Agenten duerfen deren Aktivierung nicht als erledigt behaupten.
- **FR-015:** Neue Hilfsskripte MUESSEN bei Bedarf als Bash- und
  PowerShell-7-Variante mit gleichwertigem Verhalten, Hilfe und den im
  Repository verlangten Nachweisen erstellt werden.

*The requirements establish a fork-first, platform-neutral onboarding flow,
local Podman builds, no prebuilt project image or publishing workflow,
safe local configuration, toolchain verification, local SBOM evidence,
upstream updates, optional GitHub-template separation, human-owned platform
settings, and cross-platform parity for any new helper scripts.*

## Quality And Governance

- Lern-, Bedien- und Governance-Inhalte stehen auf Deutsch zuerst und Englisch
  danach, verwenden ungefaehr CEFR B2 und erklaeren Fachbegriffe beim ersten
  Auftreten.
- Spec-Kit-Erfahrung wird nicht vorausgesetzt. Abhaengigkeiten, Status,
  Entscheidungen und naechste Schritte bleiben als geordneter Text
  verstaendlich.
- WCAG 2.2 Level AA und `Programmierung #include<everyone>` bilden die
  anwendbare Pruefbasis.
- Getrackte Dateien muessen frei von Secrets, privaten Endpunkten und
  personenspezifischen Hostpfaden bleiben.
- Das digest-gepinnte Basisimage, verifizierte Downloads, Dockerfile-ARG-
  Metadaten, Renovate-Regeln, Agenten-Isolation und lokale SBOM-Erzeugung
  bleiben erhalten.
- Ein erfolgreicher Test auf nur einer Plattform ist lokale Evidenz, keine
  unbelegte Aussage ueber vollstaendige Plattformparitaet.

*Learner and governance content is German-first and English-second at about
CEFR B2, explains terms on first use, assumes no Spec Kit experience, and
keeps all essential relationships in text. WCAG 2.2 AA, secret safety,
supply-chain controls, agent isolation, and honest platform evidence remain
binding.*

## Dependencies And Risks

1. Die Umsetzung haengt von einer erreichbaren Git-Referenz, Podman,
   Compose-Unterstuetzung, Netzverbindung fuer Abhaengigkeiten und
   ausreichenden Host-Ressourcen ab.
2. Der vollstaendige Selbstbau dauert laenger und benoetigt mehr Bandbreite als
   das Herunterladen eines fertigen Images. Diese Mehrbelastung ist akzeptiert,
   muss aber vor dem Build transparent erklaert werden.
3. Lernende koennen Fork und GitHub-Template verwechseln. Die Dokumentation
   muss beide Begriffe direkt vergleichen und einen klaren Standardweg nennen.
4. Git-Plattformen unterscheiden sich bei Forks und Template-Funktionen. Die
   Kernanleitung muss Git-neutral bleiben; plattformspezifische Schritte
   duerfen als Profile folgen.
5. Die Aktivierung einer GitHub-Template-Einstellung oder von
   Plattformregeln benoetigt Owner-/Admin-Rechte und bleibt ausserhalb
   agentischer Abschlussbehauptungen.
6. Nicht verfuegbare macOS-, Windows-/WSL2- oder Linux-Testsysteme muessen als
   ausgelassene Plattformpruefung mit Grund dokumentiert werden.

*Dependencies include Git hosting, Podman, network access, and sufficient host
resources. Risks include longer builds, platform differences, terminology
confusion, and unavailable cross-platform test systems. Human-owned platform
settings remain explicit stop boundaries.*

## Expected Artifacts And Evidence

- Eine dokumentierte Entscheidung zum Bezugsmodell: Fork/`upstream` als
  Standard, GitHub `Use this template` hoechstens als optionales Profil.
- Aktualisierte Einstiegs- und Lernenden-Dokumentation mit einem vollstaendigen
  Selbstbau- und Aktualisierungspfad.
- Falls erforderlich, paarige Bash-/PowerShell-Hilfen fuer
  Readiness-Pruefung oder Onboarding samt Dokumentation.
- Repository-seitige Pruefung, dass keine Projekt-Registry als normaler
  Image-Bezugsweg oder Push-Ziel konfiguriert ist.
- Nachweise fuer `podman-compose config`, lokalen Image-Build,
  Toolchain-Smoke-Test, Pre-Commit-/Secret-Scan und lokale
  CycloneDX-SBOM-Erzeugung.
- Plattformmatrix mit `Pass`, `Skipped` oder `Open` und nachvollziehbarer
  Begruendung.
- Aktualisiertes Sitzungsprotokoll und, falls die Umsetzung die
  Statistik-Trigger erfuellt, reproduzierbar aktualisierte Projektstatistik.

*Expected evidence covers the distribution decision, learner onboarding,
optional cross-platform helpers, absence of a project-registry delivery path,
Compose/build/toolchain/secret/SBOM checks, an honest platform matrix, and
required governance records.*

## Acceptance Criteria

- **AC-001:** Ein frischer persoenlicher Fork oder institutioneller Checkout
  kann ohne private Pfade oder Zugangsdaten konfiguriert werden; alle lokalen
  Dateien bleiben korrekt ignoriert.
- **AC-002:** Eine lernende Person kann anhand der Dokumentation `origin` und
  `upstream` einrichten, deren Rollen erklaeren und den Aktualisierungsweg
  ausfuehren oder im sicheren Vorschau-/Pruefmodus nachvollziehen.
- **AC-003:** `podman-compose config` laeuft in einem frischen Checkout ohne
  Fehler, nachdem die dokumentierten lokalen Vorlagendateien angelegt wurden.
- **AC-004:** `podman compose build --pull` baut das Image lokal erfolgreich;
  Start, Shell-Zugriff und sauberer Stopp funktionieren wie dokumentiert.
- **AC-005:** Der dokumentierte Smoke-Test bestaetigt die sechs
  Sprach-Toolchains, OpenCode, vier Required-Agenten und Syft.
- **AC-006:** Eine Repository-Suche und CI-Pruefung bestaetigen, dass kein
  vorgebautes `absdd-image-sandbox`-Projekt-Image aus einer Registry bezogen
  oder automatisch dorthin gepusht wird.
- **AC-007:** Die lokale SBOM-Erzeugung liefert eine valide CycloneDX-JSON-
  Datei; das generierte Artefakt bleibt standardmaessig ungetrackt.
- **AC-008:** Die Dokumentation vergleicht Fork und GitHub-Template direkt und
  nennt Fork/`upstream` eindeutig als Standard fuer den wartbaren Lernweg.
- **AC-009:** GitHub-unabhaengige Nutzende koennen die Kernanleitung mit einer
  institutionellen Git-URL befolgen; GitHub-spezifische Schritte sind als
  eigenes Profil erkennbar.
- **AC-010:** Deutsch steht vor Englisch, Fachbegriffe werden beim ersten
  Auftreten erklaert, und alle Abhaengigkeiten, Entscheidungen, Zustaende und
  naechsten Schritte sind ohne visuelle Darstellung verstaendlich.
- **AC-011:** `pre-commit run --all-files`, `git diff --check` und die
  einschlaegigen Repo-Validatoren laufen ohne unerwartete Funde.
- **AC-012:** Eine eventuelle Aktivierung von `Template repository`, Branch
  Protection oder anderen Plattformregeln bleibt als menschlicher Schritt
  `Open`, bis ein Owner oder Admin sie tatsaechlich ausfuehrt und prueft.

*Acceptance requires a clean fresh checkout, working origin/upstream workflow,
successful local Compose build and smoke checks, no project-registry delivery
path, a local valid SBOM, platform-neutral and accessible documentation,
passing repository checks, and truthful human-only platform status.*

## Assumptions And Open Questions

- **IAD001 - Answered:** Der primaere Bezugsweg ist ein persoenlicher Fork oder
  ein institutionell bereitgestelltes Repository mit `origin`/`upstream`.
  Evidence: ausdruecklicher Wunsch nach dem Level-0-aehnlichen Fork-Muster und
  bestehende Repository-Guidance.
- **IAD002 - Answered:** Ein fertiges Projekt-Image in GHCR oder einer anderen
  Projekt-Registry ist kein Ziel. Lernende und Nutzende sollen das Image selbst
  bauen und dabei die Dokumentation lesen.
- **IAD003 - Answered:** Die Intake-Erstellung erteilt nur lokale
  Authoring-Berechtigung. Review, Implementierung, Commit, Push,
  Pull-Request, Merge und Plattformaenderungen starten nicht automatisch.
- Es bestehen keine offenen materiellen Entscheidungen fuer die
  Intake-Erstellung. Das spaetere Intake Review darf neue fachliche Fragen
  markieren.

*The primary path, self-build-only decision, and local authoring authority are
resolved. No material authoring questions remain; Intake Review may identify
new feature questions.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify Erstelle eine Spezifikation ausschliesslich auf Grundlage von intakes/learner-fork-self-build-sandbox.md. Bewahre den Fork-/upstream-Standard, den bewussten Ausschluss eines fertigen Projekt-Images aus GHCR oder anderen Projekt-Registries, die DE-first/EN-second-Lernendenbasis, WCAG 2.2 AA, Plattformneutralitaet und alle menschlichen Stop-Grenzen. Klaere materielle Luecken, aber beginne keine Implementierung und fuehre keine Commits, Pushes, Pull Requests, Merges oder Plattformaenderungen aus.
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous Fuehre den vollstaendigen Spec-Kit-Lauf fuer intakes/learner-fork-self-build-sandbox.md mit Delivery Authority LocalImplementation aus. Implementiere nur lokal, erhalte den Fork-/upstream-Standard und den Ausschluss eines fertig bereitgestellten Projekt-Images, pruefe die Lernenden-, A11Y-, Sicherheits-, Lieferketten- und Plattformanforderungen und stoppe vor Commit, Push, Pull Request, Merge oder GitHub-/Hosting-Einstellungen.
```

<!-- intake-authoring:end -->
