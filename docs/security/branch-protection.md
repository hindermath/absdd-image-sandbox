# Branch Protection und signierte Commits

Stand: 2026-05-17

## Deutsch

Dieses Dokument erfasst die GitLab-CE-Evidenz aus dem bisherigen Hosting-
Kontext. Wenn `absdd-image-sandbox` auf einer anderen Plattform oder als
oeffentliches Repository betrieben wird, muessen die Plattformregeln dort neu
bewertet und dokumentiert werden. P2-2 wurde in diesem Kontext pragmatisch
umgesetzt:

- `main` ist serverseitig als Protected Branch konfiguriert.
- Direkte Pushes auf `main` sind deaktiviert.
- Merges nach `main` sind fuer Maintainer ueber Merge Requests erlaubt.
- Force Push ist deaktiviert.
- CODEOWNERS und Merge-Request-Template liegen im Repository.
- Signierte Commits werden dokumentiert und koennen in GitLab als verified
  angezeigt werden.
- Serverseitige Erzwingung signierter Commits ist in dieser CE-Instanz aktuell
  nicht per Projekt-Push-Rule verfuegbar.

Aktueller Plattformzustand, geprueft mit `glab`:

```bash
glab api projects/:id/protected_branches
```

Erwarteter Zustand fuer `main`:

```text
Allowed to push: No one
Allowed to merge: Maintainers
Allow force push: false
```

Die Einstellung wurde am 2026-05-17 per `glab api` gesetzt. Die direkte
PATCH-Aktualisierung des bestehenden Access-Level-Eintrags wurde von dieser
Instanz nicht wirksam uebernommen. Deshalb wurde die Protected-Branch-Regel
kurz entfernt und direkt mit strengerer Konfiguration neu angelegt:

```bash
glab api --method DELETE projects/:id/protected_branches/main
glab api --method POST projects/:id/protected_branches \
  --field "name=main" \
  --field "push_access_level=0" \
  --field "merge_access_level=40" \
  --field "allow_force_push=false"
```

Das ist kein regulaerer Arbeitsablauf fuer Entwickler:innen, sondern eine
einmalige Owner-/Admin-Konfiguration. Normaler Aenderungsfluss:

1. Feature-Branch erstellen.
2. Aenderung committen.
3. Branch pushen.
4. Merge Request gegen `main` erstellen.
5. Review, Validierung und Merge ueber GitLab.

Repo-seitige Vorbereitung:

- `.gitlab/CODEOWNERS` weist zunaechst `@thinder` als Owner zu.
- `.gitlab/merge_request_templates/Default.md` enthaelt Sicherheits-,
  Review-, Audit- und KI-Anteil-Fragen.

Hinweis zu CODEOWNERS:

GitLab CE kann die Datei als Code-Ownership-Hinweis verwenden. Ob Code-Owner-
Approval fuer Merge Requests erzwungen werden kann, haengt von der konkreten
GitLab-Edition und Instanzkonfiguration ab. Dedizierte Organisations- oder Ausbildungsteam-Handles sollten
spaeter in `.gitlab/CODEOWNERS` nachgetragen werden.

### Signierte Commits

GitLab kann GPG-, SSH- und X.509-signierte Commits als verified anzeigen, wenn
der oeffentliche Schluessel im GitLab-Profil hinterlegt ist und zur Committer-
Identitaet passt.

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

Der passende Public Key muss im GitLab-Profil hinterlegt werden:

- User Settings > SSH Keys: fuer SSH-Signing mit Usage Type `Signing` oder
  `Authentication & Signing`.
- User Settings > GPG Keys: fuer GPG-Signing.

### Nicht per GitLab CE/API erfuellt

Der API-Aufruf

```bash
glab api projects/:id/push_rule
```

liefert auf dieser Instanz `404 Not Found`. Die serverseitige Push-Rule
`Reject unsigned commits` ist daher aktuell nicht als Projektregel verfuegbar.
Fuer harte Erzwingung signierter Commits braucht es eine der folgenden Optionen:

- GitLab Push Rules mit `Reject unsigned commits`, falls die Instanz/Edition
  diese Funktion bereitstellt.
- Admin-betriebener Git-Server-Hook.
- Upgrade beziehungsweise Freischaltung einer GitLab-Edition/Funktion, die
  diese Regel unterstuetzt.

Quellen:

- GitLab Protected Branches: https://docs.gitlab.com/user/project/repository/branches/protected/
- GitLab Protected Branches API: https://docs.gitlab.com/api/protected_branches/
- GitLab Push Rules: https://docs.gitlab.com/user/project/repository/push_rules/
- GitLab Signed Commits: https://docs.gitlab.com/user/project/repository/signed_commits/
- GitLab Code Owners: https://docs.gitlab.com/user/project/codeowners/

## English

This document records GitLab CE evidence from the previous hosting context. If
`absdd-image-sandbox` is operated on another platform or as a public
repository, the platform rules must be reassessed and documented there. P2-2
was therefore implemented pragmatically in this context:

- `main` is configured as a protected branch on the GitLab server.
- Direct pushes to `main` are disabled.
- Maintainers can merge into `main` through merge requests.
- Force push is disabled.
- CODEOWNERS and a merge request template are stored in the repository.
- Signed commits are documented and can be shown as verified in GitLab.
- Server-side enforcement of signed commits is not currently available through
  a project push rule on this CE instance.

Current platform state, checked with `glab`:

```bash
glab api projects/:id/protected_branches
```

Expected state for `main`:

```text
Allowed to push: No one
Allowed to merge: Maintainers
Allow force push: false
```

The setting was applied with `glab api` on 2026-05-17. A direct PATCH update of
the existing access-level entry was not applied by this instance. The protected
branch rule was therefore briefly removed and immediately recreated with the
stricter configuration:

```bash
glab api --method DELETE projects/:id/protected_branches/main
glab api --method POST projects/:id/protected_branches \
  --field "name=main" \
  --field "push_access_level=0" \
  --field "merge_access_level=40" \
  --field "allow_force_push=false"
```

This is not a regular developer workflow, but a one-time owner/admin
configuration. Normal change flow:

1. Create a feature branch.
2. Commit the change.
3. Push the branch.
4. Create a merge request targeting `main`.
5. Review, validate, and merge through GitLab.

Repository-side preparation:

- `.gitlab/CODEOWNERS` currently assigns `@thinder` as owner.
- `.gitlab/merge_request_templates/Default.md` contains questions for security,
  review, audit, and AI involvement.

Note about CODEOWNERS:

GitLab CE can use the file as a code ownership signal. Whether Code Owner
approval can be enforced for merge requests depends on the concrete GitLab
edition and instance configuration. Dedicated organization or training-team handles should be added
to `.gitlab/CODEOWNERS` later.

### Signed commits

GitLab can display GPG-, SSH-, and X.509-signed commits as verified when the
public key is registered in the GitLab profile and matches the committer
identity.

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

The matching public key must be registered in the GitLab profile:

- User Settings > SSH Keys: for SSH signing with usage type `Signing` or
  `Authentication & Signing`.
- User Settings > GPG Keys: for GPG signing.

### Not fulfilled through GitLab CE/API

The API call

```bash
glab api projects/:id/push_rule
```

returns `404 Not Found` on this instance. The server-side push rule
`Reject unsigned commits` is therefore not currently available as a project
rule. Hard enforcement of signed commits requires one of these options:

- GitLab Push Rules with `Reject unsigned commits`, if the instance/edition
  provides that feature.
- Admin-operated Git server hook.
- Upgrade or enablement of a GitLab edition/feature that supports this rule.
