# Architektur verlinkter Intake-Evidence / Linked Intake Evidence Architecture

## Kontext und Datenfluss / Context and data flow

```text
Kanonisches sandbox-development-lifecycle-Manifest
  + manifestgebundene Intake-Dateien
  + explizite Spec-/Run-State-/archivierte Closeout-Evidence
  -> UTF-8-, Schema-, Pfad-, Hash-, Graph- und Proof-Validierung
  -> eine typisierte Fünf-Felder-Projektion
  -> Root-Ansicht + Series-Ansicht mit relativem Linkkontext
  -> Check oder atomare Mehrdateien-Publikation mit Recheck/Rollback
```

Das Manifest bleibt die fachliche Quelle für Reihenfolge, Status, Rollen,
Wurzeln und Kanten. Beide Ansichten besitzen dieselben vier Zeilen und drei
direkten Kanten; nur die relativen Linkziele unterscheiden sich aufgrund des
Dateistandorts. Fehlendes Feature-Evidence wird ausdrücklich angezeigt und
nicht aus Nummer oder Slug geraten.

*The manifest remains the functional source for order, status, roles, roots,
and edges. Both views contain the same four rows and three direct edges; only
their relative link targets differ by file location. Missing feature evidence
is shown explicitly and is never inferred from a number or slug.*

## Qualitätsziele / Quality goals

| Ziel | Szenario | Messbares Ergebnis |
|---|---|---|
| Integrität | Quelle, Pfad, Hash, Kante oder Proof ist ungültig. | Stabiler `LIE001`–`LIE012`-Blocker; kein Output wird verändert. |
| Determinismus | Unveränderte Eingaben werden erneut verarbeitet. | Beide Dateien bleiben bytegleich; `writes=0`. |
| Semantische Parität | Root- und Series-Datei haben verschiedene Linkbasen. | Fünf Felder sind identisch; nur das sichere relative Ziel ist kontextabhängig. |
| Wiederherstellbarkeit | Publication scheitert oder wird unterbrochen. | In-Prozess-Fehler rollen vollständig zurück; Generationshash deckt externe Teilstände auf. |
| Produktisolation | Governance-Automation wird ergänzt. | Kein Dockerfile-, Image-, Compose-, Runtime-, Paket-, Lockfile- oder SBOM-Diff. |
| Portabilität | Dieselben Oberflächen laufen unter Linux und Windows. | Exact-head-Proofs binden Commands, Runner, Exitcodes, Hashes und Write-Zähler. |

## Architekturentscheidung und Kommentarbedarf

Die Änderung fügt repositorynative Standardwerkzeug-Skripte hinzu und berührt
keine Container- oder Laufzeitkomponente. ADR/S-ADR sowie Podman-
Compose-Build/Up sind `N/A / Not Assessed`, solange Dockerfile, Compose, Image,
Runtime und Abhängigkeiten unverändert bleiben. Trigger sind eine neue
Komponente, Runtime, Dependency, Deployment- oder Trust Boundary. Kommentare
erklären nur nicht offensichtliche Grenzen: Diagnoseredaktion, historisches
Rename-Evidence und atomare Publication.

*The change adds repository-native standard-tool scripts and touches no
container or runtime component. ADR/S-ADR and Podman Compose build/up are `N/A
/ Not Assessed` while Dockerfile, Compose, image, runtime, and dependencies stay
unchanged. Triggers are a new component, runtime, dependency, deployment, or
trust boundary. Comments explain only non-obvious diagnostic, historic
rename-proof, and atomic-publication boundaries.*

## Documentation Impact: `GeneratedUpdate`

| Feld | Entscheidung |
|---|---|
| Kanonische Quelle | `specs/intake-series/sandbox-development-lifecycle/manifest.json` plus explizite terminale Feature-Evidence |
| Owner / Reviewer | absdd-image-sandbox Repository Owner / Feature-032 Documentation Reviewer |
| Zielgruppen und Leserpfad | Lernende, Maintainer, Reviewer: Repository-Root → Reihenfolge → vollständiger Intake oder Feature-Nachweis |
| Navigation und Dokumentklasse | Zwei verlinkte Markdown-Referenzansichten; Security-, Architektur- und A11Y-Nachweise unter `docs/` |
| Sprachpartner | Deutsch zuerst, direkt gefolgt von Englisch; technische Literale bleiben identisch |
| Plattform-/Beispielnachweis | Lokale macOS-Fixtures; exact-head Linux-/Windows-Proofs folgen im Delivery-Checkpoint |
| Distribution / Home Sync | Repositorylokale Source- und Dokumentationsänderung; kein Home Sync und kein Runtime-only Sync |
| Evidence | Positive/negative Fixtures, `LIE001`–`LIE012`, Check/Write/Check und Null-Diff-Write |
| Re-Evaluation | Manifest-, Feld-, Link-, Sprach-, Zielgruppen-, Plattform-, Renderer-, Container- oder Distributionsänderung |
