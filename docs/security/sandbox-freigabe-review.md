# Sandbox-Freigabe per MR/PR

Status: Review-Anleitung fuer P1-4

Dieses Dokument beschreibt, wie die formelle Freigabe der `ade-dev-sandbox`
durch CISO/ISB oder eine:n KI-Beauftragte:n (KIB) vorbereitet, geprueft und
per Merge Request beziehungsweise Pull Request dokumentiert wird.

## Deutsch

### Zweck

Die Freigabe bestaetigt nicht, dass jede Restrisikoquelle beseitigt ist. Sie
bestaetigt, dass der dokumentierte Sandbox-Stand fuer den genannten Zweck,
die genannte Datenklassifikation und den genannten Zeitraum bewusst bewertet
und akzeptiert wurde.

Codex darf die Faktenlage vorbereiten. Die Freigabeentscheidung selbst trifft
eine verantwortliche Person, CISO/ISB oder KIB.

### Rollen

| Rolle | Aufgabe |
|---|---|
| Owner / verantwortliche Person | Freigabe-MR vorbereiten, offene `_TODO_`-Felder ausfuellen, Evidenz verlinken. |
| CISO / ISB | Sicherheitsbewertung pruefen, Auflagen oder Freigabe dokumentieren. |
| KI-Beauftragte:r (KIB) | KI-bezogene Bewertung pruefen, insbesondere Modelle, Datenfluesse und Nutzungsgrenzen. |
| Betrieb / Plattform | Laufzeitumgebung, Registry-Zugriff, Image-Build und Compose-Betrieb bestaetigen. |
| Codex / Agent | Darf Entwuerfe und Nachweise vorbereiten, aber keine Freigabe erteilen. |

### Pruefumfang

Der MR/PR fuer die formelle Freigabe soll mindestens diese Punkte referenzieren
oder aktualisieren:

| Pruefpunkt | Evidenz / Datei |
|---|---|
| Freigabegegenstand, Status, Verantwortliche, Ablaufdatum | `docs/security/sandbox-freigabe.md` |
| Sandbox-Typ und Isolationsnachweis | `docs/security/sandbox-isolation.md` sobald vorhanden; bis dahin `Dockerfile`, `compose.yml`, `codex/`, `opencode.jsonc` |
| Basisimage und Tool-Versionen | `Dockerfile`, insbesondere Digest und `ARG`-Versionen |
| Genehmigte Host-Mounts | `compose.yml`, Mount-Liste in `docs/security/sandbox-freigabe.md` |
| KI-Werkzeuge, Dienste und Modelle | `docs/security/ai-tools-inventory.md`, `opencode.jsonc`, `codex/config.toml` |
| Netzwerkentscheidung | `docs/security/network-decision.md` |
| Audit-Export fuer Agentensitzungen | `scripts/audit-export.sh`, `scripts/compose-down-with-audit.*`, `audit-logs/README.md` |
| Secret-Scanning und Secret-Umgang | `.pre-commit-config.yaml`, `.gitleaks.toml`, `docs/security/secret-scanning.md` |
| Branch-Protection und MR-Prozess | `docs/security/branch-protection.md`, `.gitlab/CODEOWNERS`, `.gitlab/merge_request_templates/Default.md` |
| Offene Restrisiken und Folgeaufgaben | `COMPLIANCE-PLAN_RL-SE-001.md` |

### Entscheidung festhalten

Der MR/PR muss eine eindeutige Entscheidung enthalten:

- `Freigabe ausstehend`
- `Freigegeben`
- `Freigegeben mit Auflagen`
- `Nicht freigegeben`

Bei einer Freigabe oder Freigabe mit Auflagen muessen mindestens genannt
werden:

- freigebende Rolle: CISO/ISB oder KIB
- Name der freigebenden Person
- Datum der Entscheidung
- Gueltigkeitsbereich, zum Beispiel Lern- und Ausbildungsumgebung
- zulaessige Datenklassifikation oder ausdrueckliches `_TODO_`
- Ablaufdatum oder Re-Review-Datum
- Auflagen, falls vorhanden

Wenn die Entscheidung noch nicht getroffen wurde, muss der MR/PR den folgenden
Hinweis enthalten:

```text
Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend.
```

### MR/PR erstellen

Der Standardweg in diesem GitLab-Repo ist ein Feature-Branch mit Merge Request
gegen `main`:

```bash
git switch -c sandbox-freigabe-YYYY-MM-DD
git add docs/security/sandbox-freigabe.md docs/security/sandbox-freigabe-review.md
git commit -m "docs: prepare sandbox approval review"
git push -u origin sandbox-freigabe-YYYY-MM-DD
glab mr create \
  --source-branch sandbox-freigabe-YYYY-MM-DD \
  --target-branch main \
  --title "Sandbox-Freigabe vorbereiten" \
  --description "Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend."
```

Falls GitHub statt GitLab verwendet wird, gilt derselbe fachliche Ablauf mit
Pull Request statt Merge Request.

### Inhalt der MR/PR-Beschreibung

Die Beschreibung soll knapp, aber pruefbar sein:

```text
Summary:
- Aktualisiert docs/security/sandbox-freigabe.md fuer die formelle Freigabe.
- Verlinkt relevante Evidenzdokumente.

Freigabestatus:
Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend.

Pruefgrundlage:
- docs/security/sandbox-freigabe.md
- docs/security/ai-tools-inventory.md
- docs/security/network-decision.md
- docs/security/branch-protection.md
- COMPLIANCE-PLAN_RL-SE-001.md

Offene Punkte / Auflagen:
- _TODO_
```

### Review und Merge

Die freigebende Person kann die Entscheidung als MR/PR-Kommentar, Review oder
als Aenderung in `docs/security/sandbox-freigabe.md` dokumentieren. Vor dem
Merge muss klar sein, ob der MR/PR nur die Freigabe vorbereitet oder eine
erteilte Freigabe dokumentiert.

Nach dem Merge ist `docs/security/sandbox-freigabe.md` der gueltige
Repository-Nachweis. Formale DMS-, QISMS- oder Registereintraege bleiben
ausserhalb dieses Repositories.

## English

### Purpose

This document describes how formal approval of `ade-dev-sandbox` is prepared,
reviewed, and documented through a merge request or pull request by CISO/ISB
or an AI officer (KIB).

Approval means that the documented sandbox state has been reviewed and accepted
for the stated purpose, data classification, and review period. Codex may
prepare facts and drafts, but it must not grant approval.

### Review Scope

The approval MR/PR should reference or update:

- `docs/security/sandbox-freigabe.md` for approval status, owner, dates, and
  scope.
- `docs/security/sandbox-isolation.md` once available; until then `Dockerfile`,
  `compose.yml`, `codex/`, and `opencode.jsonc`.
- `docs/security/ai-tools-inventory.md` for AI tools, services, and models.
- `docs/security/network-decision.md` for egress rationale.
- Audit-export scripts and `audit-logs/README.md` for agent-session metadata
  evidence.
- Secret-scanning configuration and `docs/security/secret-scanning.md`.
- `docs/security/branch-protection.md`, `.gitlab/CODEOWNERS`, and the MR
  template for repository governance.
- `COMPLIANCE-PLAN_RL-SE-001.md` for open residual work.

### Required MR/PR Note

If approval has not yet been granted, the MR/PR must include:

```text
Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend.
```

If approval is granted, the decision must name the approving role and person,
approval date, scope, allowed data classification or explicit `_TODO_`,
expiration or re-review date, and any conditions.

### GitLab Flow

```bash
git switch -c sandbox-freigabe-YYYY-MM-DD
git add docs/security/sandbox-freigabe.md docs/security/sandbox-freigabe-review.md
git commit -m "docs: prepare sandbox approval review"
git push -u origin sandbox-freigabe-YYYY-MM-DD
glab mr create \
  --source-branch sandbox-freigabe-YYYY-MM-DD \
  --target-branch main \
  --title "Sandbox-Freigabe vorbereiten" \
  --description "Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend."
```

For GitHub, use the same content and review criteria in a pull request.
