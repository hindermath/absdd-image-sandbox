# Optionales Template-Profil / Optional Template Profile

## Deutsch

**Stand 25.10.2026: vorbereitet, nicht aktiviert.** Das Referenzrepo ist
öffentlich, aber derzeit kein GitHub-Template. Die folgende Anleitung beschreibt
einen späteren, gesondert freizugebenden Weg. Lizenzklärung, Vorlagenprüfung
und erforderliche Vorgängerabnahmen der Selbstbau-Reihe bleiben Gates.

Ein **Fork** erhält die Git-Historie und die Beziehung zur Referenz. Ein
**Template** erzeugt ein unabhängiges Repository mit neuer Historie. Ein
**Clone** ist der lokale Checkout eines entfernten Repos. Das sind keine
austauschbaren Begriffe.

| Bedarf | Bezugsweg | Aktualisierung |
|---|---|---|
| Sandbox pflegen, Referenzänderungen übernehmen, Beiträge vorschlagen | Fork oder institutionelle Kopie mit gemeinsamer Historie, Standard | Referenz prüfen und Änderungen über den passenden Git-/Review-Weg übernehmen |
| Bewusst unabhängige Sandbox mit eigener Geschichte | Template, später optional | Getrennten Referenzstand vergleichen und ausgewählte Änderungen reviewen; kein normaler Upstream-Merge |
| SysInfo-/Web-Produkt neu entwickeln | Leeres persönliches Produktrepo und genau ein Lernpaket | Eigene Produktentwicklung; nicht die ganze Sandbox zum Produktstarter erklären |

GitHub ist nur für seinen direkten Template-Weg erforderlich. GitLab,
Codeberg, Forgejo und institutionelle Git-Systeme bleiben gleichwertige
Bezugsprofile; dort gelten die bereitgestellten Kopier-/Importverfahren und
die tatsächliche Historie. Home-Baseline bleibt eine getrennte, gepinnte
Level-0-Referenz und wird durch diesen Weg nicht automatisch geforkt oder geändert.

### Späterer GitHub-Weg

1. Erst die Aktivierungsentscheidung und [Lizenzgrenzen](../licensing.md)
   prüfen. Ist der Template-Button noch nicht verfügbar, den Fork-Standardweg
   nutzen; die Anleitung ist keine Aktivierungsbestätigung.
2. Auf der Referenz **Use this template → Create a new repository** wählen.
   Eigenen Namen setzen, Privat als Ausgangswahl verwenden und **nur `main`**
   übernehmen, nicht alle Branches. Die Sichtbarkeit bewusst selbst bestätigen.
3. Die URL des neu erzeugten persönlichen Repos klonen. `origin` ist dieses
   Repo, nicht die Referenz. Keine URL mit eingebettetem Token verwenden.
4. `.env` und gegebenenfalls `opencode.env` gemäß Installation ohne Überschreiben
   anlegen; persönliche Host-Mounts bewusst auswählen. Keine gesamte Home-Freigabe.
5. Vor Agentenautomation die kopierten Governance-Zustände anhand der
   [Erstübernahme-Checkliste](../betrieb/template-erstuebernahme.md) einordnen.
   Alte `Completed`, `Ready` und Prüfberichte sind Referenzkontext. Nicht löschen
   oder als eigene Abnahme ausgeben; keine kopierten Läufe fortsetzen.
6. Eigene Zuständigkeiten und Hosting-Einstellungen prüfen. CODEOWNERS nennt
   zunächst Referenzzuständige, nicht automatisch deine Reviewer. Neue
   Rulesets, Required Checks und Zugriffsrechte müssen eigenständig eingerichtet
   und beobachtet werden. Secrets werden weder kopiert noch automatisch angelegt.
7. Das Image nach gesonderter Ausführungsentscheidung mit Podman selbst bauen,
   prüfen und SBOM erzeugen. Keine fertigen Projekt-Images als Ersatz verwenden.
   Eine neue Repo-Historie ist keine frische Image-/Plattformabnahme.

### Updates und Beiträge

Eine zusätzliche Remote namens `upstream` oder `template-upstream` erzeugt
keine gemeinsame Historie. In der Template-Kopie **kein** pauschales
`git merge --ff-only upstream/main` und kein
`git merge --allow-unrelated-histories` ausführen.

Für ein Update einen gewünschten Referenzstand getrennt lesend auschecken,
Herkunfts-Commit dokumentieren und Änderungen gezielt vergleichen. Nur bewusst
ausgewählte Dateien in einem eigenen Branch übernehmen, lokale Konfiguration
und Daten erhalten, Konflikte reviewen und eigene Tests durchführen. Git
veröffentlicht nichts automatisch. Für Beiträge zur Referenz einen separaten
Fork mit gemeinsamer Historie verwenden. Im eigenen Repo gehen persönliche
Pull/Merge Requests gegen dessen eigenen Zielbranch.

## English

**25 October 2026: prepared, not enabled.** The public reference is not currently
a GitHub template. This is a later separately authorized route; license review,
template validation and predecessor acceptance remain gates.

A fork preserves history/reference relationship; a template creates independent
history; a clone is a local checkout. Prefer a fork or shared-history institutional
copy for maintenance and contributions. Use a template only for a deliberate
independent sandbox. SysInfo/web products still start in empty personal product
repos with one learning package. Home Baseline remains a separate pinned source.
GitHub is required only for its direct route, not for all learners.

Later: verify approval/licenses, choose Use this template/Create repository,
prefer private and default `main` only; clone the new personal origin without
credentials in URLs. Prepare local files without overwrites, choose limited
mounts, classify copied governance as source context and use the handover
checklist before automation. Configure personal owners, hosting protections
and any separately approved secrets; do not assume they are inherited.
Self-build/test/SBOM still need explicit authority and current evidence.

Adding a reference remote does not join histories. Do not blindly fast-forward
or merge unrelated histories. Compare a separate pinned reference checkout,
review selected file changes on a personal branch and preserve local data.
Personal PRs target the personal repo; reference contributions use a separate
fork. Never resume copied source runs or claim source acceptance as your own.

[GitHub: Unterschiede zwischen Fork und Template / Fork and template differences](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
