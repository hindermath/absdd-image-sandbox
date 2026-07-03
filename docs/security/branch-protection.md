# Branch Protection and Signed Commits

Stand: 2026-07-03

## Deutsch

Dieses Dokument beschreibt den GitHub-Zielzustand fuer `absdd-image-sandbox`
als Public-Readiness-Sandbox. Es dokumentiert Repository-seitige Vorbereitung
und Owner-/Admin-Aufgaben. Es schaltet das Repository nicht auf Public und
setzt keine Plattformregel.

### Aktueller Status

- Repository-seitig vorhanden: `.github/CODEOWNERS`.
- Repository-seitig vorhanden: `.github/pull_request_template.md`.
- Repository-seitig vorhanden: `.github/workflows/homogeneity-check.yml` mit
  Agent-Secret-Scan-Jobs fuer Linux, macOS und Windows.
- Plattformseitige GitHub-Rulesets oder Branch-Protection-Regeln sind
  Human-/Admin-only und bleiben `Open`, bis sie auf GitHub gesetzt und erneut
  dokumentiert wurden.
- Auf dem aktuellen privaten Repository kann der Ruleset-API-Zugriff je nach
  GitHub-Plan mit dem Hinweis blockiert sein, dass Repository Rulesets erst mit
  GitHub Pro oder nach Public-Schaltung nutzbar sind. Das ist kein Repo-Fehler.

### Zielzustand fuer `main`

Der empfohlene GitHub-Ruleset fuer `refs/heads/main`:

| Regel | Zielwert |
|---|---|
| Ruleset status | `active` |
| Target | branch `refs/heads/main` |
| Deletion protection | enabled |
| Non-fast-forward protection | enabled |
| Pull request required | enabled |
| Required approving reviews | `1` |
| Code Owner review | required |
| Required status checks | Agent Secret Scan auf Linux, macOS und Windows |
| Allowed merge methods | merge, squash, rebase |
| Admin bypass | allowed only for documented Owner/Admin emergency use |

Der Admin-Bypass ist bewusst vorgesehen, damit ein Owner oder Admin bei
dringenden Governance- oder Infrastrukturkorrekturen handlungsfaehig bleibt.
Jede Nutzung muss in PR-Beschreibung, Review-Kommentar oder Session-/Admin-Log
begruendet werden.

### Normaler Aenderungsfluss

1. Feature-Branch erstellen.
2. Aenderung committen.
3. Branch pushen.
4. Pull Request gegen `main` erstellen.
5. Review, Required Checks und Merge ueber GitHub durchfuehren.

### Signierte Commits

GitHub kann GPG-, SSH- und S/MIME-signierte Commits als verified anzeigen,
wenn der passende oeffentliche Schluessel im GitHub-Profil hinterlegt ist und
zur Committer-Identitaet passt.

SSH-Signing, Beispiel:

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git commit -S -m "docs: update branch protection notes"
```

GPG-Signing, Beispiel:

```bash
gpg --full-generate-key
gpg --list-secret-keys --keyid-format=long
git config --global user.signingkey <KEY-ID>
git config --global commit.gpgsign true
git commit -S -m "docs: update branch protection notes"
```

Der passende Public Key muss im GitHub-Profil hinterlegt werden:

- Settings > SSH and GPG keys: fuer SSH-Signing mit Signing-Key.
- Settings > SSH and GPG keys: fuer GPG-Signing.

Harte serverseitige Erzwingung signierter Commits ist eine
Plattform-/Admin-Entscheidung. Sie darf in diesem Repository erst als erledigt
markiert werden, wenn die Regel auf GitHub aktiv ist und durch Owner/Admin
nachgewiesen wurde.

## English

This document describes the GitHub target state for `absdd-image-sandbox` as a
public-readiness sandbox. It records repository-side preparation and
owner/admin tasks. It does not make the repository public and does not configure
platform rules.

### Current Status

- Repository-side file present: `.github/CODEOWNERS`.
- Repository-side file present: `.github/pull_request_template.md`.
- Repository-side workflow present: `.github/workflows/homogeneity-check.yml`
  with agent secret scan jobs for Linux, macOS, and Windows.
- Platform-side GitHub rulesets or branch-protection rules are human/admin-only
  and remain `Open` until configured on GitHub and documented again.
- On the current private repository, GitHub Rulesets API access may be blocked
  depending on the GitHub plan with a message that rulesets require GitHub Pro
  or public visibility. That is not a repository defect.

### Target State For `main`

Recommended GitHub ruleset for `refs/heads/main`:

| Rule | Target value |
|---|---|
| Ruleset status | `active` |
| Target | branch `refs/heads/main` |
| Deletion protection | enabled |
| Non-fast-forward protection | enabled |
| Pull request required | enabled |
| Required approving reviews | `1` |
| Code Owner review | required |
| Required status checks | Agent Secret Scan on Linux, macOS, and Windows |
| Allowed merge methods | merge, squash, rebase |
| Admin bypass | allowed only for documented owner/admin emergency use |

The admin bypass is intentional so that an owner or admin can still handle
urgent governance or infrastructure fixes. Each use must be justified in the
PR description, a review comment, or a session/admin log.

### Normal Change Flow

1. Create a feature branch.
2. Commit the change.
3. Push the branch.
4. Create a pull request targeting `main`.
5. Review, required checks, and merge through GitHub.

### Signed Commits

GitHub can display GPG-, SSH-, and S/MIME-signed commits as verified when the
matching public key is registered in the GitHub profile and matches the
committer identity.

SSH signing example:

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git commit -S -m "docs: update branch protection notes"
```

GPG signing example:

```bash
gpg --full-generate-key
gpg --list-secret-keys --keyid-format=long
git config --global user.signingkey <KEY-ID>
git config --global commit.gpgsign true
git commit -S -m "docs: update branch protection notes"
```

The matching public key must be registered in the GitHub profile:

- Settings > SSH and GPG keys: for SSH signing with a signing key.
- Settings > SSH and GPG keys: for GPG signing.

Hard server-side enforcement of signed commits is a platform/admin decision.
This repository may only mark it as complete after the rule is active on GitHub
and evidenced by an owner/admin.
