# Git und Hosting sicher verwenden / Use Git and Hosting Safely

## Rollen von `origin` und `upstream` / Roles of `origin` and `upstream`

**DE:** Git speichert die Versionsgeschichte lokal. Eine Hosting-Plattform wie
GitLab, GitHub, Codeberg oder Forgejo stellt entfernte Repositories,
Zusammenarbeit und Reviews bereit. Für Lernende gelten zwei klare Rollen:

- `origin` ist dein persönlicher Fork oder das von deiner Institution
  bereitgestellte beschreibbare Repository.
- `upstream` ist die von der Institution oder dem Projekt gepflegte Referenz.

**EN:** Git stores version history locally. A hosting platform such as GitLab,
GitHub, Codeberg, or Forgejo provides remote repositories, collaboration, and
reviews. Learners use two clear roles:

- `origin` is your personal fork or institution-provided writable repository.
- `upstream` is the reference maintained by the institution or project.

**DE:** Ein GitHub-Konto ist nur für den direkten GitHub-Weg oder eine
optionale GitHub-Copilot-Anmeldung erforderlich. Andere institutionelle
Git-Systeme sind gleichwertige Git-Ziele.

**EN:** A GitHub account is required only for the direct GitHub route or an
optional GitHub Copilot sign-in. Other institutional Git systems are equally
valid Git targets.

## Repository einrichten / Set Up the Repository

**DE:** Ersetze die Platzhalter durch die von deiner Institution oder dem
Projekt bereitgestellten HTTPS-Adressen:

**EN:** Replace the placeholders with the HTTPS addresses provided by your
institution or project:

```bash
git clone <URL-DEINES-FORKS-ODER-INSTITUTIONS-REPOS> mein-projekt
cd mein-projekt
git remote add upstream <URL-DER-REFERENZ>
git remote -v
```

**DE:** `git clone` nennt das geklonte Ziel automatisch `origin`. Prüfe mit
`git remote -v`, dass keine geheime URL oder ein Token gespeichert wurde.

**EN:** `git clone` automatically names the cloned target `origin`. Use
`git remote -v` to verify that no secret URL or token was stored.

## Identität lokal setzen / Set Identity Locally

**DE:** Ändere keine globale Identität, wenn nur dieses Lernprojekt betroffen
ist:

**EN:** Do not change global identity when only this training project is
affected:

```bash
git config --local user.name "DEIN NAME"
git config --local user.email "DEINE FREIGEGEBENE ADRESSE"
git config --local --list
```

## Vor der Arbeit aktualisieren / Update Before Work

```bash
git fetch --prune upstream
git switch main
git merge --ff-only upstream/main
git push origin main
```

**DE:** `--ff-only` verhindert einen unbeabsichtigten Merge-Commit. Schlägt der
Befehl fehl, prüfe die Abweichung und frage nach, statt Historie mit Force-
Befehlen umzuschreiben.

**EN:** `--ff-only` prevents an unintended merge commit. If it fails, inspect
the divergence and ask for guidance instead of rewriting history with force
commands.

## Änderung in einem Branch / Change on a Branch

```bash
git switch -c docs/meine-aenderung
git status --short --branch
```

Nach der Bearbeitung / After editing:

```bash
git diff --check
git diff
git add <BEWUSST-GEWAEHLTE-DATEI>
git diff --cached
git commit -m "docs: describe the change"
git push --set-upstream origin docs/meine-aenderung
```

**DE:** `git add .` kann mehr Dateien auswählen als beabsichtigt. Bevorzuge
explizite Pfade und prüfe den gestagten Diff. Ein Commit enthält keine Secrets,
generierten SBOMs, lokalen Auditdaten oder Agenten-Caches.

**EN:** `git add .` can select more files than intended. Prefer explicit paths
and review the staged diff. A commit contains no secrets, generated SBOMs,
local audit data, or agent caches.

## Review auf der Hosting-Plattform / Review on the Hosting Platform

**DE:** Erstelle auf der aktiven Plattform einen Merge Request oder Pull
Request von deinem Branch nach `upstream/main`. Beschreibe Zweck, Tests,
Konfigurations- und Secret-Auswirkungen sowie ausgelassene Plattformprüfungen.
Die Plattformbezeichnung ändert den Review-Grundsatz nicht.

**EN:** On the active platform, create a merge request or pull request from
your branch to `upstream/main`. Describe purpose, tests, configuration and
secret impact, and skipped platform checks. Platform terminology does not
change the review principle.

## Nach dem Merge / After the Merge

```bash
git switch main
git fetch --prune upstream
git merge --ff-only upstream/main
git push origin main
git branch -d docs/meine-aenderung
```

**DE:** Lösche den entfernten Branch über die Hosting-Oberfläche oder ein
freigegebenes CLI nur, wenn der Merge bestätigt ist. Lokales Aufräumen ist
keine Erlaubnis für Änderungen am Referenzrepository.

**EN:** Delete the remote branch through the hosting interface or an approved
CLI only after the merge is confirmed. Local cleanup does not authorize
changes to the reference repository.

## Fehler und Stop-Regeln / Errors and Stop Rules

- **DE:** Bei Konflikten zuerst `git status` und die betroffenen Dateien
  lesen. Kein `reset --hard`, `clean -fd` oder Force-Push ohne ausdrückliche
  Freigabe. **EN:** For conflicts, first read `git status` and affected files.
  Do not use `reset --hard`, `clean -fd`, or force push without explicit
  approval.
- **DE:** Ungetrackte Dateien können wichtige lokale Arbeit enthalten. Vor
  einer Löschung immer prüfen und nachfragen. **EN:** Untracked files may
  contain important local work. Inspect and ask before deletion.
- **DE:** Hosting-Regeln, Code-Owner-Review und Admin-Bypass werden von Ownern
  auf der Plattform eingerichtet. Ein Agent behauptet sie nicht als erledigt.
  **EN:** Owners configure hosting rules, code-owner review, and admin bypass
  on the platform. An agent does not claim them as completed.

## Nächste Schritte / Next Steps

**DE:** Für den ersten kontrollierten Agentenauftrag gehe zu
[KI-Agenten und Spec Kit](agenten-und-spec-kit.md).

**EN:** For the first controlled agent task, continue with
[AI agents and Spec Kit](agenten-und-spec-kit.md).
