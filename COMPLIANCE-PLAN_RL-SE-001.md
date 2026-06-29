# Compliance-Plan Sichere Entwicklungs-Sandbox / CL_12 — `absdd-image-sandbox`

## Zweck dieses Dokuments

Der fachliche Bezugspunkt dieses Plans ist die generische Secure-Development-Basis in `docs/secure-development/`. Sie enthält die Richtlinie Sichere Entwicklung, die zugehörigen Checklisten und den Checklistensammelband als organisationsneutrale Ausbildungs- und Prüfgrundlage. Die in diesem Dokument genannten Richtlinien- und CL-Kürzel beziehen sich auf diese lokale, generische Dokumentationsbasis.

Diese Datei ist die Arbeits- und Auftragsdatei für die agentische Behebung der
Befunde aus der Sandbox-Governance-Prüfung dieses Repositories gegen die Richtlinie Sichere Entwicklung und die Checkliste `CL_12` ("Agentische KI in Sandbox-Umgebungen"). Frühere Planfassungen wurden aus einem organisationsspezifischen Auditkontext in diese generische Ausbildungs- und Prüfgrundlage überführt.

Sie ist nicht das Audit-Protokoll selbst. Das Audit-Protokoll bleibt in der
separaten Managementsystem- oder Audit-Ablage. Dieses Dokument beschreibt, **was zu tun ist**, **wie es zu tun
ist**, **wie es abzunehmen ist**, in einer Form, die ein ausführender
KI-Agent direkt umsetzen kann.

## Auftragnehmer

- **Ausführender Agent:** Codex CLI mit Modell **gpt-5.5**, Reasoning-Stufe
  **high**.
- **Sandbox:** Diese absdd-image-sandbox selbst, gestartet über
  `podman compose up -d`.
- **Schreibrechte des Agenten:** ausschließlich innerhalb der gemounteten
  Host-Verzeichnisse, primär das Repository-Wurzelverzeichnis dieses
  Sandbox-Repos und gegebenenfalls Spec-Kit-Pilotprojekt unter
  `/rider-projects/<projektname>`.
- **Menschliche Aufsicht:** Pflicht. Jede Änderung wird vor `git commit` und
  vor `git push` von einer Person geprüft. Sicherheitskritische Änderungen
  unterliegen dem Vier-Augen-Prinzip.

## Geltungsbereich

**Eingeschlossen:**

- Inhalt und Struktur dieses Repositories `absdd-image-sandbox`.
- Image-Build, Compose-Konfiguration, Werkzeugkonfiguration für OpenCode und
  Codex, Spec-Kit-Initialisierung.
- Dokumentations-Artefakte unter `docs/security/` (neu anzulegen).

**Ausgeschlossen** (gehört in ein externes Managementsystem oder in die Plattform-Administration):

- Rotation von API-Keys auf Anbieter- oder Plattformseite.
- Aktivierung von Branch-Protection-Regeln in GitLab oder GitHub.
- Eintragung von Freigabe-Entscheidungen in externe Dokumentenmanagement- oder Audit-Systeme.
- Aufnahme eines Werkzeugs in eine externe Liste genehmigter Software.
- Anlage von Risiko-Register-Einträgen oder SoA-Einträgen.

Wo der Agent an eine dieser Grenzen stößt, **bricht er ab und meldet
Eskalation**.

## Normative Bezüge

- `docs/secure-development/Richtlinie_Sichere-Entwicklung.md`, Abschnitt "Agentische KI in
  Sandbox-Umgebungen" und Abschnitt "KI-gestützte Codeerzeugung".
- `docs/secure-development/checklisten/CL_12_Agentische-KI-Sandbox.md` (CL_12 v1.2, Prüfpunkte 1
  bis 11). CL_12 v1.1 ergänzte gegenüber v1.0 drei Prüfpunkte: §9
  Sandbox-Typologie und Isolationsnachweis (Aufgabe P1-5), §10
  Netzwerkrestriktion (Aufgabe P3-2) und §11 Re-Validierungsstand und
  Lebenszyklus (Aufgabe P1-4). CL_12 v1.2 erweiterte §1: Die
  Initialfreigabe der Sandbox kann von der oder dem CISO/ISB oder von der
  oder dem KI-Beauftragten (KIB) erteilt werden (Aufgabe P1-4). CL_12 v1.3
  erweiterte §5 um einen Querverweis auf die KI-Lieferkettentransparenz.
- `docs/secure-development/checklisten/CL_09_KI-Codeerzeugung.md` (CL_09 v1.3, Prüfpunkte 1, 11,
  13, 15). CL_09 v1.3 ergänzte Prüfpunkt 15 „KI-Lieferkettentransparenz"
  (Aufgabe P1-6).
- `docs/secure-development/checklisten/CL_10_Sichere-Entwicklungsumgebung.md` (CL_10, Prüfpunkte 4,
  5, 6, 9).
- `docs/secure-development/checklisten/CL_05_Lieferkette-Build-Integritaet.md` (CL_05, Pinning,
  SBOM, Malware-Scan).

Diese Dokumente liegen lokal unter `docs/secure-development/` und werden als mitgeltende Ausbildungs- und Prüfgrundlage behandelt. Der Agent nutzt diese lokale Fassung als Quelle und ändert sie nur, wenn ein ausdrücklicher Auftrag zur Richtlinienpflege vorliegt.

## Arbeitsweise

1. **Eine Aufgabe = ein Commit = ein Pull Request.** Keine Sammel-Commits
   über mehrere Aufgaben hinweg.
2. **Commit-Stil:** kurz, imperativ, mit Präfix `docs:`, `chore:`, `build:`
   oder `ci:`. Beispiel: `build: pin codex sandbox defaults`.
3. **Vor jedem Commit:**
   - `podman-compose config` muss als Standardpruefung fuer die statische
     Compose-Konfiguration ohne Fehler durchlaufen.
   - `podman compose config` ist eine zusaetzliche lokale Plausibilitaets-
     pruefung, wenn die Podman-Machine beziehungsweise der Podman-Socket
     funktioniert; Socket- oder Machine-Fehler gelten nicht als Repo-Fehler,
     solange `podman-compose config` erfolgreich ist.
   - Wenn das `Dockerfile` geändert wurde: `podman compose build --pull`
     muss erfolgreich durchlaufen.
4. **Keine Secrets im Klartext.** Wenn Codex auf einen API-Key, ein Token
   oder einen Endpoint stößt, wird der Wert über eine Umgebungsvariable aus
   einer gitignored Datei (`opencode.env`, `codex.env`) gelesen.
5. **Keine destruktiven Git-Aktionen ohne Freigabe.** Kein `git push
   --force`, kein `git reset --hard`, kein `git clean -fd` außerhalb des
   Workspace.
6. **Bei Unklarheit lieber eskalieren.** Codex erstellt am Ende seiner
   Sitzung ein Protokoll der ausgeführten Aufgaben und der eskalierten
   Punkte.

## Priorisierung

| Stufe | Bedeutung | Maximaler Termin |
|---|---|---|
| **P0** | Build-blockierend | sofort |
| **P1** | Audit-Evidenz fehlt; CL_12-Akzeptanzkriterium nicht erfüllbar | binnen 2 Wochen |
| **P2** | Härtung gegen RL-Anforderungen | binnen 6 Wochen |
| **P3** | Optimierung, Konsistenz, Defense-in-Depth | bei Gelegenheit |

---

# P0 — Sofortmaßnahmen

## P0-1 Codex-Konfigurationsverzeichnis anlegen

### Befund

Der `Dockerfile` enthält in den Zeilen 71 bis 73:

```dockerfile
COPY ./codex/config.toml /etc/codex/config.toml
COPY ./codex/config.toml /etc/codex/managed_config.toml
COPY ./codex/requirements.toml /etc/codex/requirements.toml
```

Das Verzeichnis `codex/` existiert im Repository nicht. Im Verzeichnis-Root
liegt nur `codex.config.toml.example` als loses Vorlagen-Schnipsel.

**Folgen:**

- `podman compose build --pull` und `podman compose build --pull` schlagen
  reproduzierbar fehl. Die Sandbox ist in der jetzigen Form nicht baubar.
- Die in `README.md` Zeilen 1300 bis 1307 dokumentierten Codex-Sicherheits-
  Defaults sind nicht durchgesetzt, sondern nur beschrieben.
- CL_12 Prüfpunkt 5 ("Genehmigte Werkzeuge und Modelle") und Prüfpunkt 2
  ("Begrenzte Host-Mounts" — Codex-Schreibgrenze) sind nicht prüfbar.

### Aufgabe

Lege das Verzeichnis `codex/` mit zwei Dateien an: `config.toml` und
`requirements.toml`. Inhalt entspricht den dokumentierten Sicherheits-
Defaults aus `README.md` Zeilen 1300 bis 1307 plus dem Provider-Block aus
`codex.config.toml.example`.

### Vorlage `codex/config.toml`

```toml
# Codex CLI Standardkonfiguration (User Config Layer).
# Wird im Image-Build nach /etc/codex/config.toml kopiert.
# Diese Werte sind die ergonomischen Defaults, die ein Endnutzer
# innerhalb der zulässigen Grenzen anpassen darf.

model = "gpt-5.4"
model_provider = "azure"
model_reasoning_effort = "medium"

# Sandbox-Modus: Codex darf in den deklarierten Wurzeln schreiben,
# aber nicht beliebig auf das Host-Dateisystem zugreifen.
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
# Kein direkter Netzwerkzugriff aus Shell-Kommandos der Sandbox heraus.
# Modell-Calls laufen separat über die Codex-CLI-Provider-Schicht.
network_access = false
# /tmp ist nicht automatisch beschreibbar; jede Schreiboperation muss
# auf einem expliziten Mount landen.
exclude_slash_tmp = true
# Schreibrechte beschraenken sich auf die vom Compose-Stack
# gemounteten Arbeitsverzeichnisse. Aenderungen an dieser Liste
# erfordern ein neues Container-Image, nicht nur einen Restart.
writable_roots = [
  "/absdd-image-sandbox",
  "/home/adedev/home-baseline-tmp",
  "/workspace",
  "/rider-projects",
  "/java-projects",
  "/go-projects",
  "/rust-projects",
  "/python-projects",
]

[model_providers.azure]
name = "Azure OpenAI"
# Der Platzhalter <changeme> wird beim Betrieb ueber den Endpoint des
# zustaendigen Provider- oder Ausbildungs-Subscriptions ersetzt.
# Der konkrete Endpoint gehoert in die Betriebsdokumentation,
# nicht in dieses Image.
base_url = "https://<changeme>.openai.azure.com/openai/v1"
env_key = "AZURE_OPENAI_API_KEY"
wire_api = "responses"
```

### Vorlage `codex/requirements.toml`

Der Zweck dieser Datei ist die **administrative Erzwingung** der Sicherheits-
Defaults. Wo der User Config Layer noch nachgeben kann, soll der
Requirements Layer harte Untergrenzen ziehen.

**Schema-Recherche:** Das genaue Schema von `requirements.toml` der Codex
CLI ist projektspezifisch. Bevor du diese Datei schreibst, prüfe:

1. Aktuelle Dokumentation der Codex CLI im npm-Paket `@openai/codex`. Im
   Container: `podman compose exec ade sh -lc 'codex --help'` und
   `podman compose exec ade sh -lc 'find $(npm root -g)/@openai/codex
   -name "*.md" -o -name "schema*.json"'`.
2. Wenn das Schema dort nicht eindeutig dokumentiert ist, **erzeuge nur eine
   minimale, syntaktisch valide Datei** mit denselben Sicherheits-Schlüsseln
   wie in `config.toml`, deklarativ kommentiert als "harte Untergrenze". Es
   ist besser, die Datei vorerst klein zu halten als ungültige Direktiven
   einzubauen.

**Minimaler vertretbarer Inhalt** (falls Schema unklar):

```toml
# Codex CLI Requirements Layer.
# Wird im Image-Build nach /etc/codex/requirements.toml kopiert.
# Inhalt: harte, vom Administrator erzwungene Untergrenzen.
# Werte, die der User Config Layer (/etc/codex/config.toml und
# ~/.codex/config.toml) nicht unterschreiten darf.

sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false
exclude_slash_tmp = true
writable_roots = [
  "/absdd-image-sandbox",
  "/home/adedev/home-baseline-tmp",
  "/workspace",
  "/rider-projects",
  "/java-projects",
  "/go-projects",
  "/rust-projects",
  "/python-projects",
]
```

Wenn nach der Schema-Recherche klar wird, dass `requirements.toml` ein
abweichendes Format hat, **passe den Inhalt an und dokumentiere die Quelle
deiner Anpassung im Commit-Body**.

### Akzeptanzkriterien

- [x] Verzeichnis `codex/` existiert.
- [x] `codex/config.toml` existiert und enthält `sandbox_mode =
      "workspace-write"`, `network_access = false`,
      `exclude_slash_tmp = true` und die definierten `writable_roots`.
- [x] `codex/requirements.toml` existiert und ist gültiges TOML.
- [x] `podman compose build --pull` läuft ohne Fehler durch.
- [x] `podman compose exec ade cat /etc/codex/config.toml` zeigt die
      erwarteten Defaults.
- [x] `podman compose exec ade cat /etc/codex/requirements.toml` zeigt die
      erwarteten Defaults.

### Verifikation (Skript)

```bash
podman-compose config >/dev/null
podman compose build --pull
podman compose up -d
podman compose exec ade cat /etc/codex/config.toml | grep -E 'sandbox_mode|network_access|exclude_slash_tmp|writable_roots'
podman compose exec ade cat /etc/codex/requirements.toml
podman compose exec ade codex --version
podman compose down
```

### Commit-Vorschlag

```
build: add codex sandbox defaults

Adds codex/config.toml and codex/requirements.toml so the Dockerfile
COPY steps no longer fail. The files lock the Codex sandbox to
workspace-write with no shell network access and writable roots
limited to /workspace, /rider-projects, /java-projects.

Refs: RL-SE-001 "Agentische KI in Sandbox-Umgebungen" bullet 1, CL_12
checklist items 2 and 5.
```

### Eskalationspunkte

- Wenn das `requirements.toml`-Schema nicht eindeutig recherchierbar ist:
  stoppe und melde dies. Liefere die `config.toml` separat, ohne
  `requirements.toml` zu erfinden.
- Der Azure-Endpoint-Platzhalter `<changeme>` bleibt im Image-Build
  beabsichtigt unausgefüllt. Den echten Endpoint setzt der Betrieb über
  Umgebungsvariablen.

---

## P0-2 Basisimage auf Digest pinnen

### Befund

Zeile 1 des `Dockerfile` muss ein digest-gepinntes Basisimage enthalten. Der
aktuelle Zielzustand ist das Microsoft-.NET-SDK-Basisimage aus MCR:

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:10.0@sha256:<DIGEST>
```

Der `latest`-Tag ist nicht reproduzierbar. Zwei Builds an unterschiedlichen
Tagen liefern unterschiedliche Images. Das verletzt RL-SE-001 §"Agentische
KI" Bullet 4 ("freigegebene Versionen") und CL_05 ("Lock-Dateien werden
eingecheckt").

### Aufgabe

Ersetze den `:latest`-Tag durch eine Pinning-Form mit Image-Digest
(`@sha256:...`). Halte den lesbaren Tag als Kommentar daneben, damit ein
menschlicher Reviewer die ungefähre Generation erkennt.

### Vorgehen

1. Aktuellen MCR-Digest abfragen:
   ```bash
   podman pull mcr.microsoft.com/dotnet/sdk:10.0
   podman image inspect mcr.microsoft.com/dotnet/sdk:10.0 --format '{{index .RepoDigests 0}}'
   ```
2. Im `Dockerfile` ersetzen:
   ```dockerfile
   # Tag 10.0 beobachtet am YYYY-MM-DD, hier auf Digest gepinnt.
   FROM mcr.microsoft.com/dotnet/sdk:10.0@sha256:<HIER_DIGEST>
   ```
3. Image neu bauen und prüfen, dass alle nachfolgenden Schritte des
   Dockerfiles wie zuvor laufen.

### Akzeptanzkriterien

- [x] `Dockerfile` Zeile 1 enthält `@sha256:` und keinen `:latest`-Tag.
- [x] Kommentar mit Beobachtungsdatum direkt darüber.
- [x] `podman compose build --pull` läuft erfolgreich.
- [x] `README.md` Abschnitt "Konfiguration" enthält einen Hinweis, dass das
      Basisimage gepinnt ist und über `Dockerfile`-Änderung plus Commit
      aktualisiert wird.

### Eskalationspunkte

- Wenn das Basisimage nicht erreichbar ist (Registry- oder Netzwerkproblem): melden,
  nicht raten.
- Wenn die Registry keine Digests ausliefert: ältere Tag-Variante mit
  Datums-Suffix als Zwischenlösung dokumentieren, dann eskalieren.

---

## P0-3 OpenCode- und Codex-NPM-Pakete pinnen

### Befund

Zeile 61 des `Dockerfile`:

```dockerfile
RUN npm i -g opencode-ai@latest @openai/codex@latest
```

`@latest` widerspricht der gleichen Anforderung wie P0-2. Bereits ein
Update der NPM-Pakete kann das Verhalten der Sandbox verändern, ohne dass
ein Commit dokumentiert ist.

### Aufgabe

Pinne beide Pakete auf konkrete Versionen. Halte sie nicht im Code-Body
hartcodiert verstreut, sondern als `ARG` am Kopf des `Dockerfiles` analog zu
`GO_VERSION` und `RUST_TOOLCHAIN`.

### Vorgehen

1. Aktuell installierte Versionen im laufenden Container ermitteln:
   ```bash
   podman compose exec ade sh -lc 'opencode --version; codex --version'
   ```
2. Diese Versionen als ARGs am Dockerfile-Kopf ergänzen:
   ```dockerfile
   ARG OPENCODE_VERSION=<HIER_VERSION>
   ARG CODEX_VERSION=<HIER_VERSION>
   ```
3. Den NPM-Befehl umstellen:
   ```dockerfile
   RUN npm i -g "opencode-ai@${OPENCODE_VERSION}" "@openai/codex@${CODEX_VERSION}" \
       && ln -sf "$(npm root -g)/@openai/codex/bin/codex.js" /usr/local/bin/codex
   ```
4. Build verifizieren.

### Akzeptanzkriterien

- [x] Keine Vorkommen von `@latest` mehr im `Dockerfile`.
- [x] Pinning per `ARG` am Kopf des Dockerfiles deklariert.
- [x] `podman compose build --pull` läuft erfolgreich.
- [x] `podman compose exec ade sh -lc 'opencode --version; codex --version'`
      gibt genau die im `ARG` gesetzten Versionen aus.
- [x] `README.md` Abschnitt "Konfiguration" nennt diese ARGs als
      Update-Hebel.

---

# P1 — Audit-Evidenz aufbauen

## P1-1 Audit-Log-Konzept für Agentennutzung

### Befund

CL_12 Prüfpunkt 8 verlangt: Werkzeug, Sandbox-Typ, Projektpfad, Zeitraum,
verantwortliche Person, Review-Ergebnis und relevante Spec-Kit-Artefakte
müssen je Agentennutzung nachvollziehbar sein.

OpenCode- und Codex-Sitzungen liegen heute in den flüchtigen Podman-Volumes
`opencode_data` und `codex_data`. Beim `podman compose down -v` sind sie
weg. Es gibt keinen periodischen Export, kein zentrales Log.

### Aufgabe

Lege ein Audit-Log-Skript und eine begleitende Dokumentation an, die
mindestens einmal pro Arbeitstag oder bei Container-Stopp die Session-
Metadaten aus beiden Volumes in ein versionsfreundliches Audit-Verzeichnis
außerhalb des Repositories exportiert.

Wichtig: **Inhalte der Sitzungen können personenbezogene Daten oder
Geheimnisse enthalten**. Es werden **nur Metadaten** exportiert (Werkzeug,
Sitzungs-ID, Startzeit, Endzeit, Projektpfad innerhalb der Sandbox,
verantwortliche Linux-Person `whoami` oder Git-Identity-Hinweis), keine
vollständigen Prompt- oder Antwort-Texte.

### Vorgehen

1. Datei `scripts/audit-export.sh` anlegen mit folgendem Verhalten:
   - Liest aus `/home/adedev/.local/share/opencode` die vorhandenen
     Sitzungs-Verzeichnisse oder -Dateien.
   - Liest aus `/home/adedev/.codex` die vorhandenen Sitzungen.
   - Schreibt **eine** Zeile pro Sitzung in eine CSV oder JSONL nach
     `/audit/<datum>.jsonl` (Pfad ist Bind-Mount, siehe Compose-Anpassung
     unten). Mindestfelder: `tool`, `session_id`, `started_at`, `ended_at`,
     `project_path`, `actor`.
2. In `compose.yml` einen neuen Bind-Mount ergänzen:
   ```yaml
       - type: bind
         source: ${AUDIT_DIR:-./audit-logs}
         target: /audit
   ```
   Verzeichnis `audit-logs/` mit `.gitkeep` und einer `audit-logs/README.md`
   anlegen, die die Inhalts-, Zugriffs- und Aufbewahrungsregeln beschreibt.
3. `.gitignore` erweitern, sodass nur die Strukturdatei (`README.md`,
   `.gitkeep`) im Repo bleibt, die echten Audit-Daten nicht.
4. In `AGENTS.md` Abschnitt "Security & Configuration Tips" einen Hinweis
   ergänzen: "Audit-Log-Export per `scripts/audit-export.sh` mindestens
   einmal pro Arbeitstag und zwingend vor `podman compose down -v`."

### Akzeptanzkriterien

- [x] `scripts/audit-export.sh` ist ausführbar (`chmod +x`).
- [x] Lauf im Container erzeugt eine JSONL-Datei im `audit-logs/`-Mount mit
      mindestens einer Beispielzeile aus einer Test-Sitzung.
- [x] CSV/JSONL enthält **keine** Prompt- oder Antworttexte.
- [x] Anweisung in `AGENTS.md` und `README.md` Abschnitt "Konfiguration"
      ergänzt.
- [x] `audit-logs/README.md` beschreibt: was gespeichert wird, wer Zugriff
      hat, Aufbewahrungsdauer, Lösch-Vorgang.

### Eskalationspunkte

- Wenn OpenCode oder Codex die Sitzungsdaten in einem Binärformat
  speichern, das nicht trivial parsbar ist: minimale Variante implementieren
  (Verzeichnis-Listing mit `ls -la`-Metadaten plus Tool-Name) und im Commit-
  Body dokumentieren.
- Wenn die zentrale Ablage (z. B. SIEM oder DMS) noch nicht geklärt ist:
  lokaler `audit-logs/`-Ordner als Zwischenschritt; dauerhafte Ablage als
  Folge-Ticket markieren.

---

## P1-2 KI-Werkzeug-Inventar `docs/security/ai-tools-inventory.md`

### Befund

CL_09 Prüfpunkt 1 verlangt ein dokumentiertes KI-Werkzeug-Inventar mit
Vendor, Lizenztyp, Datenresidenz, ZDR-Status, DPA-Datum, vierteljährlicher
Re-Evaluation.

Heute existiert nur die `opencode.jsonc` mit Modell-Liste, keine
Inventarsicht.

### Aufgabe

Lege `docs/security/ai-tools-inventory.md` an. Sprache: Deutsch zuerst,
Englisch danach (Konvention dieses Repos für Sicherheitsdokumente).

### Mindestinhalt

Tabelle mit Spalten:

| Werkzeug | Variante | Vendor | Endpoint | EU-Datenresidenz | ZDR-Status | DPA-Datum | Trainings-Opt-out | OpenSSF-Scorecard | freigegeben bis | Owner |

Einträge initial:

1. **OpenCode** (CLI im Container) — kein vorkonfigurierter Modellanbieter.
   DPA-Datum, ZDR-Status, freigegeben-bis-Datum und etwaige lokal
   genehmigte Provider vom Owner einzutragen.
2. **Codex CLI** (im Container) — Provider Azure OpenAI, Region einzutragen
   (EU bevorzugt). DPA-Datum, ZDR-Status, freigegeben-bis-Datum vom Owner
   einzutragen.
3. **Spec Kit** — Version `v0.8.3`, Bezug aus GitHub
   `github.com/github/spec-kit.git`, Lizenz beachten.

Felder, die der Agent nicht selbst kennt (DPA-Datum, ZDR-Status,
Owner-Name), bleiben als `_TODO_` mit Begründung "vom Owner einzutragen"
stehen. Der Agent erfindet sie nicht.

### Akzeptanzkriterien

- [x] Datei `docs/security/ai-tools-inventory.md` existiert.
- [x] Tabelle mit allen oben genannten Werkzeugen.
- [x] Keine erfundenen Felder; offene Felder als `_TODO_` markiert.
- [x] Hinweis am Ende der Datei: "Re-Evaluation: jedes Quartal, nächste
      Prüfung YYYY-MM-DD".

---

## P1-3 Pre-Commit-Hook gegen Klartext-Geheimnisse

### Befund

CL_10 Prüfpunkt 6 verlangt Secret-Scanning, das einen versehentlichen
Klartext-Commit blockiert. Aktuell schützt nur `.gitignore`. Ein
versehentliches Umbenennen oder ein neuer Pfad würden nicht aufgehalten.

### Aufgabe

Konfiguriere `pre-commit` mit `gitleaks` als Mindestabsicherung.

### Vorgehen

1. Datei `.pre-commit-config.yaml` anlegen:
   ```yaml
   repos:
     - repo: https://github.com/gitleaks/gitleaks
       rev: v8.21.2  # konkrete Tag-Version pruefen und einsetzen
       hooks:
         - id: gitleaks
   ```
   Hinweis: Die exakte Tag-Version vor Übernahme prüfen
   (`gitleaks --version` der aktuellen stabilen Release), nicht `main`
   verwenden.
2. Datei `.gitleaks.toml` mit Custom-Allowlist nur für die `*.example`-
   Dateien anlegen, damit neutrale Beispielwerte wie `changeme` keinen
   Treffer erzeugen.
3. In `AGENTS.md` und `README.md` einen Installations-Hinweis ergänzen:
   ```bash
   pre-commit install
   pre-commit run --all-files
   ```
4. Ersten Vollscan ausführen. Wenn Treffer auftauchen, **nicht
   unterdrücken**, sondern als Befund anhängen und an Mensch eskalieren.

### Akzeptanzkriterien

- [x] `.pre-commit-config.yaml` mit konkret gepinnter Gitleaks-Version.
- [x] `.gitleaks.toml` mit knapper Allowlist nur für Beispieldateien.
- [x] `pre-commit run --all-files` läuft ohne unerwartete Funde.
- [x] Installations-Hinweis in `AGENTS.md` und `README.md` ergänzt.

---

## P1-4 Formelle Sandbox-Freigabe — Eskalation an Mensch

### Befund

CL_12 Prüfpunkt 1 verlangt: Sandbox-Typ, verantwortliche Person und
Freigabestatus dokumentiert. CL_12 selbst bezeichnet `absdd-image-sandbox` als
"in Feinabstimmung". Es gibt keine formelle Freigabe-Notiz.

Nach CL_12 v1.2 kann die Initialfreigabe der Sandbox von der oder dem
CISO/ISB oder von der oder dem KI-Beauftragten (KIB) erteilt werden. Die
Freigabe-Notiz muss daher beide Rollen als mögliche Freigabeinstanz vorsehen.

### Aufgabe

**Diese Aufgabe übernimmt Codex nicht.** Codex bereitet aber den
Dokumentenrumpf vor und legt ihn als Entwurf ab.

### Vorgehen

1. Datei `docs/security/sandbox-freigabe.md` anlegen mit folgenden Pflicht-
   Feldern als Vorlage:
   - Sandbox-Typ: Container (Podman)
   - Sandbox-Identifikator: Image-Digest aus P0-2
   - Verantwortliche Person: `_TODO_`
   - Freigabestatus: `_Entwurf, Freigabe ausstehend_`
   - Freigabedatum: `_TODO_`
   - Ablaufdatum / Re-Review: `_TODO_ (Empfehlung: 12 Monate nach Freigabe)`
   - Genehmigte Modelle (Verweis auf `ai-tools-inventory.md`)
   - Genehmigte Mount-Liste (Verweis auf `compose.yml`)
   - Genehmigte Tool-Versionen (Verweis auf `Dockerfile` ARGs)
   - Unterschriftsblock mit getrennten Zeilen für verantwortliche Person,
     CISO/ISB und KI-Beauftragte:n (KIB)
2. In `README.md` Abschnitt "Konfiguration" auf diese Datei verlinken.

Codex füllt die `_TODO_`-Felder nicht selbst. Codex erstellt nur den Rumpf
und reicht die Datei in einem PR ein.

### Akzeptanzkriterien

- [x] `docs/security/sandbox-freigabe.md` als Entwurf existiert.
- [x] Alle Pflichtfelder vorhanden, offene Felder als `_TODO_` markiert.
- [x] Verweis in `README.md` ergänzt.
- [ ] Pull Request enthält Hinweis "Freigabe durch CISO/ISB oder KI-Beauftragte:n (KIB) ausstehend".

---

## P1-5 Isolations-/Architekturdokument der Sandbox

### Befund

CL_12 v1.1 ergänzte den Prüfpunkt 9 ("Sandbox-Typologie und
Isolationsnachweis"). Er verlangt ein Sicherheits- oder Architekturdokument
der Sandbox, das an einer Stelle nennt: den Sandbox-Typ gemäß RL-Typologie,
den technischen Isolationsmechanismus und eine Begründung des erreichten
Schutzniveaus.

Diese Angaben existieren heute, sind aber über mehrere Dateien verstreut:
Sandbox-Typ in `docs/security/sandbox-freigabe.md`, nicht-privilegierte
Ausführung implizit im `Dockerfile` (`useradd adedev`, `USER adedev`),
Egress-Entscheidung in `docs/security/network-decision.md`, Agenten-Grenzen
in `codex/config.toml`, `codex/requirements.toml` und `opencode.jsonc`. Es
gibt kein konsolidiertes Dokument, das Prüfpunkt 9 erwartet.

### Aufgabe

Lege `docs/security/sandbox-isolation.md` an. Sprache: Deutsch zuerst,
Englisch danach (Konvention dieses Repos für Sicherheitsdokumente). Das
Dokument fasst vorhandene Fakten zusammen; es ändert keine Konfiguration.

### Mindestinhalt

- **Sandbox-Typ:** Container-Sandbox (Podman) gemäß der
  Sandbox-Typologie der RL-SE-001, Abschnitt "Agentische KI in
  Sandbox-Umgebungen".
- **Isolationsmechanismen, je mit konkreter Evidenzquelle (Datei und Stelle):**
  - Nicht-privilegierte Ausführung: `Dockerfile` (`useradd adedev`,
    `USER adedev`); der Container läuft nicht als `root`.
  - Dateisystem-Grenzen: nur explizite Bind-Mounts laut `compose.yml` und
    Mount-Liste in `sandbox-freigabe.md`; `ContainerBuild.props` ist
    read-only gemountet.
  - Agenten-Schreibgrenzen: Codex `sandbox_mode = "workspace-write"` mit
    `writable_roots`, abgesichert durch `codex/requirements.toml` als harte
    Untergrenze; OpenCode `permission`-Block in `opencode.jsonc`.
  - Netzwerk: Verweis auf `network-decision.md`; Codex
    `network_access = false` im Workspace-Write-Modus.
  - Trennung Agentendaten/Host: benannte Volumes `codex_data` und
    `opencode_data` statt Bind-Mounts; `history.persistence = "none"`.
  - Geheimnis-Trennung: `deny_read`/`permission`-Regeln auf `*.env`,
    `.gitignore`, Einbringung per `env_file`.
- **Schutzniveau-Begründung:** ehrliche Einordnung, dass die Isolation
  derzeit auf Podman-Standardkonfiguration plus non-root-Benutzer beruht;
  Verweis auf die optionale Härtung P3-4 als Verstärkung; Aussage, für
  welche Datenklassifikation das Schutzniveau als ausreichend bewertet wird.
- **Verweise** auf die übrigen `docs/security/`-Dokumente, `compose.yml`,
  `Dockerfile` und die Agentenkonfigurationen.

Die abschließende Bewertung "Schutzniveau ausreichend für
Datenklassifikation X" ist eine Owner-, CISO/ISB- oder KIB-Entscheidung. Codex bereitet die
Faktenlage auf und markiert das Urteil als `_TODO_`; es wird nicht erfunden.

### Akzeptanzkriterien

- [x] `docs/security/sandbox-isolation.md` existiert, Deutsch und Englisch.
- [x] Sandbox-Typ als Container-Sandbox gemäß RL-Typologie benannt.
- [x] Jeder Isolationsmechanismus mit konkreter Evidenzquelle belegt.
- [x] Schutzniveau-Begründung vorhanden; offene Owner-Bewertung als `_TODO_`
      markiert, nicht erfunden.
- [x] Verweis in `README.md` und in `sandbox-freigabe.md` ergänzt.

### Eskalationspunkte

- Die endgültige Schutzniveau-Bewertung gegenüber einer Datenklassifikation
  trifft der Owner, die/der CISO/ISB oder die/der KI-Beauftragte (KIB),
  nicht Codex.
- Wenn ein Isolationsmechanismus nicht eindeutig belegbar ist: als offenen
  Punkt kennzeichnen statt eine Annahme als Tatsache zu schreiben.

### Commit-Vorschlag

```
docs: add sandbox isolation evidence document

Adds docs/security/sandbox-isolation.md consolidating sandbox type,
technical isolation mechanisms, and a protection-level rationale in one
place. Sources existing facts from Dockerfile, compose.yml, codex/ and
opencode.jsonc; owner-side protection-level judgement left as _TODO_.

Refs: RL-SE-001 "Agentische KI in Sandbox-Umgebungen", CL_12 checklist
item 9.
```

---

## P1-6 AI-SBOM-Lieferantentransparenz im KI-Werkzeug-Inventar

### Befund

RL-SE-001 v2.4.0 und CL_09 v1.3 führten den Prüfpunkt 15
"KI-Lieferkettentransparenz" ein. Er verlangt, dass für jedes eingesetzte
KI-Werkzeug, jeden KI-Dienst und jedes Modell die vom Anbieter verfügbaren
Transparenzangaben im KI-Werkzeug-Inventar erfasst oder verlinkt werden:
Modell-Identität und -Version, Verweis auf Model Card oder AI-SBOM des
Anbieters, Trainings- und Feinabstimmungsverfahren, Herkunft und
Sensitivität der Trainingsdaten sowie KI-spezifische Sicherheitseigen-
schaften. Bezugsrahmen ist die G7-Leitlinie "Software Bill of Materials
for AI – Minimum Elements" (2026).

Das mit Aufgabe P1-2 angelegte `docs/security/ai-tools-inventory.md` führt
Vendor, Endpoint, EU-Datenresidenz, ZDR-Status, DPA-Datum,
Trainings-Opt-out und OpenSSF-Scorecard. Es deckt jedoch den
Model-Card-/AI-SBOM-Verweis, das Trainings- und Feinabstimmungsverfahren
sowie Herkunft und Sensitivität der Trainingsdaten noch nicht ab.

### Aufgabe

Erweitere `docs/security/ai-tools-inventory.md` um die fehlenden Felder aus
CL_09 Prüfpunkt 15. Die Organisation nutzt die Modelle nur und erzeugt keine eigene
AI-SBOM; die Angaben werden, soweit der Anbieter sie veröffentlicht,
erfasst oder verlinkt. Fehlt eine Angabe, wird das ausdrücklich vermerkt.

### Vorgehen

1. Inventar-Tabelle je Werkzeug, Dienst und Modell um folgende Felder
   ergänzen:
   - Verweis auf Model Card oder AI-SBOM des Anbieters (URL oder Ablageort).
   - Trainings- und Feinabstimmungsverfahren, soweit veröffentlicht.
   - Herkunft und Sensitivität der Trainingsdaten, soweit veröffentlicht.
   - KI-spezifische Sicherheitseigenschaften (zum Beispiel Eingabe-/
     Ausgabefilter, Robustheitsmaßnahmen), soweit veröffentlicht.
2. Für vorkonfigurierte Modellanbieter je Modell die Model Card bzw. den
   AI-SBOM-Verweis eintragen. OpenCode hat in diesem Image keinen
   vorkonfigurierten Modellanbieter; dort ist nur die CLI als Werkzeug zu
   bewerten. Wo eine Quelle fehlt, "vom Anbieter nicht veröffentlicht" mit
   Datum vermerken.
3. Felder, die nur der Owner kennt, als `_TODO_` belassen; nichts erfinden.
4. Den Hinweisblock am Dateiende um einen Verweis auf die G7-Leitlinie und
   auf CL_09 Prüfpunkt 15 ergänzen.

### Akzeptanzkriterien

- [x] `ai-tools-inventory.md` enthält je Werkzeug, Dienst und vorkonfiguriertem Modell die
      vier neuen Felder oder einen begründeten Fehlt-Vermerk.
- [x] Für jedes vorkonfigurierte Modell ist eine Anbieter-Transparenzquelle (Model Card oder
      AI-SBOM) verlinkt oder ihr Fehlen dokumentiert.
- [x] Keine erfundenen Trainings- oder Datenherkunfts-Angaben; offene
      Punkte sind als `_TODO_` oder "nicht veröffentlicht" markiert.
- [x] Verweis auf die G7-Leitlinie "Software Bill of Materials for AI –
      Minimum Elements" (2026) und auf CL_09 Prüfpunkt 15 ergänzt.

### Eskalationspunkte

- Die Organisation erzeugt für fremdbezogene Modelle keine eigene AI-SBOM. Diese
  Aufgabe beschränkt sich auf das Erfassen und Verlinken von
  Anbieterangaben; eine eigene Modell- oder Trainingsdaten-Erhebung ist
  nicht Gegenstand des Plans.
- Stellt ein Anbieter keine Model Card oder AI-SBOM bereit, ist das ein
  dokumentierter Lieferketten-Befund. Die Bewertung der Auswirkung trifft
  der Owner bzw. die/der CISO/ISB oder KIB, nicht Codex.

### Commit-Vorschlag

```
docs: extend ai-tools-inventory with AI-SBOM supplier fields

Adds model-card / AI-SBOM reference, training and fine-tuning method, and
training-data origin and sensitivity to docs/security/ai-tools-inventory.md
as required by CL_09 item 15 (AI supply-chain transparency). Provider data
is recorded or linked; missing items are marked, not invented.

Refs: RL-SE-001 "KI-gestützte Codeerzeugung", CL_09 checklist item 15.
```

---

# P2 — Härtung

## P2-1 Spec-Kit-Pilotinitialisierung

### Befund

CL_12 Prüfpunkt 6 verlangt: Spec Kit ist im Projekt initialisiert und die
sechs Governance-Presets sind installiert oder eine begründete Ausnahme ist
dokumentiert. `README.md` Zeilen 1085 bis 1090 listet die Befehle. Es gibt
aber kein Projekt, in dem das tatsächlich gelaufen ist.

### Aufgabe

Legen ein **dokumentiertes Pilotprojekt** unter
`/rider-projects/specify-pilot/` an, initialisiere Spec Kit dort und
installiere die sechs Presets. Sichere die Ausgabe von `specify preset
list` als Evidenz.

### Vorgehen

1. Pilotprojekt-Ordner im gemounteten Host-Pfad anlegen (außerhalb dieses
   Repos, also unter `${RIDER_PROJECTS_DIR}`):
   ```bash
   mkdir -p /rider-projects/specify-pilot
   cd /rider-projects/specify-pilot
   specify init . --integration opencode --force
   ```
   Bei der Script-Typ-Abfrage `sh` wählen.
2. Die sechs Presets aus `README.md` Z. 1085–1090 installieren.
3. Evidenz ablegen:
   ```bash
   specify preset list > /workspace/audit-evidence/specify-preset-list.txt
   specify preset info security-governance >> /workspace/audit-evidence/specify-preset-list.txt
   ```
4. In diesem `absdd-image-sandbox`-Repo eine kurze Notiz unter
   `docs/security/spec-kit-pilot.md` ablegen, die das Pilotprojekt referenziert
   und die Evidenz-Datei nennt.

### Akzeptanzkriterien

- [x] Pilotprojekt initialisiert.
- [x] Sechs Presets in der `specify preset list`-Ausgabe sichtbar.
- [x] Evidenz-Datei abgelegt und in `docs/security/spec-kit-pilot.md`
      verlinkt.

### Eskalationspunkte

- Wenn ein Preset nicht erreichbar ist (z. B. GitHub-Ratelimit):
  dokumentieren, retry später.
- Wenn ein Preset-Repository nicht auflösbar ist: in der Notiz als Ausnahme
  dokumentieren und Mensch konsultieren.

---

## P2-2 Branch-Protection und signierte Commits — Eskalation und Vorbereitung

### Befund

CL_10 Prüfpunkte 4 und 5 verlangen Branch-Protection und signierte Commits
für `main`. Im Sandbox-Repo selbst nicht durchgesetzt.

### Aufgabe

**Plattform-seitige Schritte:** Eskalation an Repo-Owner.

**Repo-seitige Vorbereitung durch Codex:**

1. Datei `.github/CODEOWNERS` oder `.gitlab/CODEOWNERS` anlegen mit
   Mindesteinträgen:
   ```
   *               @<organisation-team-handle>
   /Dockerfile     @<security-team-handle>
   /compose.yml    @<security-team-handle>
   /codex/         @<security-team-handle>
   /opencode.jsonc @<security-team-handle>
   /docs/security/ @<security-team-handle>
   ```
   Team-Handles als `_TODO_` markieren, wenn unbekannt.
2. Pull-Request-Template anlegen unter `.github/pull_request_template.md`
   (oder `.gitlab/merge_request_templates/Default.md`) mit Mindestabschnitt:
   - "Sicherheitsrelevante Änderung? Ja/Nein"
   - "Vier-Augen-Review erforderlich? Ja/Nein, falls ja: Name"
   - "Audit-Log-Export vor `podman compose down -v` durchgeführt? Ja/Nein"
   - "KI-Anteil? Werkzeug, Umfang, Reviewer"
3. In `AGENTS.md` Hinweis ergänzen, dass diese Vorlagen im Repo liegen,
   aber **plattformseitige Branch-Protection-Regeln separat von einem
   Admin gesetzt werden**.

### Akzeptanzkriterien

- [x] CODEOWNERS-Datei vorhanden.
- [x] PR-/MR-Template vorhanden.
- [x] `AGENTS.md`-Hinweis ergänzt.
- [x] Eskalations-Item für Branch-Protection an Admin notiert.

---

## P2-3 Image-SBOM beim Build

### Befund

CL_05 verlangt eine maschinenlesbare SBOM je Release-Artefakt. Das Sandbox-
Image ist ein Release-Artefakt.

### Aufgabe

Ergänze einen Build-Skript-Schritt, der nach einem Image-Build automatisch
eine CycloneDX-SBOM erzeugt.

### Vorgehen

1. Werkzeugwahl: `syft` (Anchore) oder `trivy sbom`. Beide sind frei
   nutzbar. Empfehlung: `syft`, weil dedizierter Zweck.
2. Skript `scripts/build-and-sbom.sh` anlegen:
   ```bash
   #!/usr/bin/env bash
   set -euo pipefail
   podman compose build --pull
   IMAGE="${IMAGE_NAME:-localhost/absdd-image-sandbox-ade:latest}"
   mkdir -p sboms
   syft "${IMAGE}" -o cyclonedx-json="sboms/$(date +%Y-%m-%d)-ade-sandbox.cdx.json"
   ```
3. `sboms/` mit `.gitkeep` ins Repo, **aber** SBOM-Dateien selbst per
   `.gitignore` ausschließen, wenn sie groß werden — alternativ als
   Release-Asset ablegen.
4. Hinweis in `AGENTS.md` und `README.md`: SBOM-Generierung Pflicht vor
   Verteilung des Images.

### Akzeptanzkriterien

- [x] `scripts/build-and-sbom.sh` vorhanden und ausführbar.
- [x] Testlauf erzeugt eine CycloneDX-JSON-SBOM.
- [x] Hinweis in Dokumentation ergänzt.

### Eskalationspunkte

- Wenn `syft` lokal nicht installierbar ist: minimaler `dpkg -l`-Export als
  Übergangs-Ersatz, klar gekennzeichnet.

---

# P3 — Optimierung

## P3-1 Curl-Pipe-Bash-Installer durch verifizierte Pfade ersetzen

### Befund

Der Dockerfile installiert per `curl | bash`:

- NodeSource-Setup (Zeile 42)
- Rust per `sh.rustup.rs` (Zeilen 84/85)
- uv per `astral.sh/uv/install.sh` (Zeile 63)

Diese Pfade liefern keine echte Integritätsprüfung. RL §"Lieferketten-
sicherheit" verlangt geprüfte Paketregister.

### Aufgabe

Ersetze stufenweise:

- Node: Debian-Paket aus `nodesource`-Apt-Repo via signiertem Schlüssel
  einbinden (`gpg --import` plus `apt-key`-Nachfolge).
- Rust: festen Rustup-Tarball mit `sha256`-Prüfung herunterladen.
- uv: feste Release-URL aus GitHub-Tag plus `sha256`-Prüfung.

Wegen mittleren Umsetzungsaufwands: in **mehreren** kleinen PRs.

### Umsetzungsschnitt und Abnahme

- MR 1: NodeSource-Setup-Skript ersetzen; TODO-Einträge für uv/uvx und
  Rust/rustup in `docs/security/supply-chain-todo.md` anlegen.
- MR 2: uv/uvx auf ein festes GitHub-Release-Artefakt mit
  `sha256`-Prüfung umstellen.
- MR 3: Rust/rustup auf `rustup-init` mit `sha256`-Prüfung umstellen.

Wenn MR 2 auf dem lokalen macOS-/Podman-System wegen Storage-, Speicherplatz-
oder Podman-VM-Problemen nicht vollständig abgenommen werden kann, darf der
Branch für eine externe Abnahme auf ein stärkeres System gepusht werden. MR 2
gilt dann aber erst als mergefähig, wenn dort mindestens folgende Prüfungen
grün gelaufen sind:

```bash
podman-compose config
podman compose build --pull
uvx pre-commit run --all-files
```

Danach müssen zusätzlich die Tool-Checks im neu gebauten Image laufen. P3-1
darf erst abgehakt werden, wenn MR 1 bis MR 3 gemergt sind und Build- sowie
Tool-Checks sauber durchlaufen.

### Akzeptanzkriterien

- [x] Mindestens einer der drei Punkte umgestellt, dokumentiert, getestet.
- [x] Bei den anderen: TODO-Eintrag in `docs/security/supply-chain-todo.md`.

---

## P3-2 Netzwerk-Restriktion auf Compose-Ebene

### Befund

`compose.yml` hat keinen `networks:`-Block. Der `ade`-Container hängt am
Default-Bridge und kann beliebige Hosts erreichen. `network_access = false`
in Codex bremst nur Shell-Kommandos, nicht die Tools selbst.

### Aufgabe

Lege ein dediziertes Netzwerk mit egress-Allow-List an oder dokumentiere,
warum freier Egress in der Lernumgebung beabsichtigt ist.

### Vorgehen

Variante A — Lernumgebung bleibt offen, aber dokumentiert:

1. In `docs/security/network-decision.md` festhalten: "Default-Bridge mit
   freiem Egress, weil Spec-Kit, Codex, Maven Central, NuGet, crates.io,
   deb.nodesource.com, static.rust-lang.org, go.dev und MCR erreichbar sein
   müssen. Risiko: lateral
   movement gering wegen Container-Isolation. Akzeptiert bis YYYY-MM-DD."
2. In `compose.yml` Kommentar ergänzen, der auf diese Entscheidung
   verweist.

Variante B — Allow-List:

Komplexer; nur sinnvoll, wenn ein Proxy oder ein DNS-Filter im RZ
verfügbar ist. Wenn nicht: Variante A.

### Akzeptanzkriterien

- [x] Entscheidung dokumentiert.
- [x] Kommentar in `compose.yml` vorhanden.

---

## P3-3 Renovate oder Dependabot

### Befund

CL_05 / RL Z. 347 empfiehlt automatisiertes Abhängigkeits-Management.

### Aufgabe

Lege `.github/dependabot.yml` (wenn GitHub) oder `renovate.json` (wenn
Renovate) an, das `Dockerfile`-Pinning-Variablen und npm-Pakete überwacht.

### Akzeptanzkriterien

- [x] Konfigurationsdatei vorhanden.
- [x] Mindestens eine erfolgreiche Auswertung lokal simuliert oder als
      "wird nach Aktivierung serverseitig laufen" notiert.

Umsetzung: `renovate.json` ist vorhanden und wurde lokal mit
`npx --yes --package renovate@latest renovate-config-validator renovate.json`
validiert. Die operative MR-Erzeugung laeuft nach Aktivierung eines
Renovate-Bots, GitLab-Runner-Jobs oder externen Renovate-Services fuer dieses
GitLab-CE-Projekt.

---

## P3-4 compose.yml-Härtung (Defense-in-Depth)

### Befund

`compose.yml` startet den `ade`-Container auf Podman-Standardwerten: alle
Standard-Linux-Capabilities sind vorhanden, `no-new-privileges` ist nicht
gesetzt, das Root-Dateisystem ist schreibbar. Die einzige harte
Isolationskontrolle auf Container-Ebene ist der non-root-Benutzer `adedev`.

CL_12 Prüfpunkt 9 verlangt eine Begründung des Schutzniveaus. Eine
gehärtete `compose.yml` macht dieses Schutzniveau belegbar statt nur
behauptet und stützt damit das Isolationsdokument aus P1-5.

### Aufgabe

Härte den `ade`-Service schrittweise. Wegen des Risikos, Build- oder
Laufzeitschritte zu brechen, wird jede Direktive einzeln gesetzt und
getestet.

### Vorgehen

1. `security_opt: ["no-new-privileges:true"]` ergänzen. Danach
   `podman compose build --pull`, `podman compose up -d` und die
   Tool-Checks (`dotnet --info`, `java --version`, `go version`,
   `rustc --version`, `python --version`, `opencode --version`,
   `codex --version`) durchlaufen.
2. `cap_drop: ["ALL"]` ergänzen. Wenn ein Werkzeug fehlschlägt, einzelne
   Capabilities gezielt über `cap_add` zurückgeben und im Kommentar
   begründen.
3. Optional `pids_limit` sowie Speicher- und CPU-Limits setzen.
4. `read_only: true` nur setzen, wenn alle Schreibpfade über Mounts oder
   `tmpfs` abgedeckt sind. Andernfalls dokumentiert auslassen.
5. Jede Direktive in `compose.yml` kommentieren und das Ergebnis in
   `docs/security/sandbox-isolation.md` (P1-5) nachtragen.

Wenn eine Härtung ein Werkzeug bricht und nicht risikolos über `cap_add`
zu retten ist: Direktive weglassen, im Kommentar und im Isolationsdokument
begründen, nicht erzwingen.

### Akzeptanzkriterien

- [x] Mindestens `no-new-privileges:true` ist gesetzt und getestet.
- [x] `cap_drop`/`cap_add` ist bewusst konfiguriert oder begründet
      ausgelassen.
- [x] `podman-compose config` und
      `podman compose build --pull` laufen fehlerfrei.
- [x] Die Tool-Checks im Container laufen unverändert erfolgreich.
- [x] Änderungen in `compose.yml` sind kommentiert und in
      `sandbox-isolation.md` dokumentiert.

### Eskalationspunkte

- `read_only: true` kann Toolchains brechen. Im Zweifel weglassen und als
  künftige Option im Isolationsdokument vermerken.
- Diese Aufgabe ist als P3 optional. Wenn sie ein stabiles Setup gefährdet,
  hat ein lauffähiger Container Vorrang; der offene Härtungsschritt wird
  dann dokumentiert.

### Commit-Vorschlag

```
chore: harden ade compose service

Adds no-new-privileges and capability drops to the ade service so the
container runs with least privilege beyond the non-root user. Each
directive is commented; risky options that break toolchains are omitted
and documented instead.

Refs: RL-SE-001 "Agentische KI in Sandbox-Umgebungen", CL_12 checklist
item 9.
```

---

# Sitzungs-Schluss

Am Ende jeder Codex-Sitzung erstellt der Agent unter
`docs/security/agent-session-log/` eine neue Datei mit Zeitstempel im
Dateinamen. Inhalt:

- ausgeführte Aufgaben aus diesem Plan (mit ID, Status `done` oder
  `partial`)
- übersprungene Aufgaben mit Begründung
- eskalierte Punkte (P1-4, gegebenenfalls weitere)
- Empfehlung für die nächste Sitzung

Diese Datei dient als Audit-Spur der agentischen Arbeit selbst und
unterstützt CL_12 Prüfpunkt 8.

---

# Anhang A — Querverweise zur RL und zu den Checklisten

| Aufgabe | RL-SE-001 Bezug | Checkliste |
|---|---|---|
| P0-1 codex/-Verzeichnis | §"Agentische KI" Bullets 1, 4 | CL_12 §2, §5 |
| P0-2 Image-Pinning | §"Sichere Konfiguration", §"Lieferkettensicherheit" | CL_05, CL_10 §9 |
| P0-3 NPM-Pinning | §"Agentische KI" Bullet 4 | CL_12 §5, CL_05 |
| P1-1 Audit-Log | §"Agentische KI" Bullet 8 | CL_12 §8, CL_09 §13 |
| P1-2 Tool-Inventar | §"KI-gestützte Codeerzeugung" | CL_09 §1 |
| P1-3 pre-commit Secret | §"Sichere Konfiguration" | CL_10 §6, CL_12 §4 |
| P1-4 Sandbox-Freigabe | §"Agentische KI" Satz 2 | CL_12 §1, §11 |
| P1-5 Isolationsdokument | §"Agentische KI" Sandbox-Typen | CL_12 §9 |
| P1-6 AI-SBOM-Inventarfelder | §"KI-gestützte Codeerzeugung" | CL_09 §15, CL_12 §5 |
| P2-1 Spec-Kit-Pilot | §"Agentische KI" Bullets 5, 6 | CL_12 §6 |
| P2-2 Branch-Protection | §"Versionierung und Änderungsmanagement" | CL_10 §4, §5 |
| P2-3 SBOM | §"Lieferkettentransparenz" | CL_05 |
| P3-1 Verifizierte Installer | §"Lieferkettensicherheit" | CL_05 |
| P3-2 Netzwerk | §"Attack Surface Reduction" | CL_12 §10 |
| P3-3 Renovate/Dependabot | §"Lieferkettentransparenz" | CL_05 |
| P3-4 compose.yml-Härtung | §"Attack Surface Reduction" | CL_12 §9 |

# Anhang B — Versionshistorie dieses Plans

| Version | Datum | Änderung |
|---|---|---|
| 1.0.0 | 2026-05-14 | Erstfassung nach Audit RL-SE-001 v2.1.0 / CL_12 v1.0 |
| 1.1.0 | 2026-05-19 | Normbezug auf RL-SE-001 v2.2.0 / CL_12 v1.1 nachgeführt; Geltungsbereich auf CL_12 §§9–11 erweitert; Aufgaben P1-5 (Isolations-/Architekturdokument, CL_12 §9) und P3-4 (compose.yml-Härtung, CL_12 §9) ergänzt; Querverweise P1-4 und P3-2 auf CL_12 §11 bzw. §10 aktualisiert |
| 1.2.0 | 2026-05-19 | Normbezug auf RL-SE-001 v2.3.0 / CL_12 v1.2 nachgeführt; Aufgaben P1-4 und P1-5 um die KI-Beauftragten-Rolle (KIB) als gleichwertige Freigabe- bzw. Bewertungsinstanz neben CISO/ISB ergänzt |
| 1.3.0 | 2026-05-19 | Normbezug auf RL-SE-001 v2.4.0 / CL_12 v1.3 nachgeführt; Aufgabe P1-6 (AI-SBOM-Lieferantentransparenz im KI-Werkzeug-Inventar, CL_09 §15) ergänzt |
