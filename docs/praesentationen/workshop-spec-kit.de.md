---
lang: de-DE
title: absdd-image-sandbox - Spec Kit Workshop
date: 2026-10-25
---

<!-- slide: W01 -->
# absdd-image-sandbox

Spec-Kit-Workshop mit KI-Agenten
Für Ausbildung ab Lehrjahr 1 und Entwicklung ohne Spezialkenntnisse
Deutsch · Stand 25.10.2026

::: notes
KI bedeutet künstliche Intelligenz. Ein Container ist eine begrenzte Arbeitsumgebung, keine vollständige Sicherheitsgarantie. Dieser Workshop setzt eine durch die Lernbegleitung vorbereitete Umgebung voraus. Die vier IT-Ausbildungsberufe und alle vier Fachrichtungen der Fachinformatik können denselben Einstieg nutzen. Die praktischen Aufgaben dürfen nur innerhalb der jeweils genehmigten Grenzen ausgeführt werden.
:::

---

<!-- slide: W02 -->
# Unser Arbeitsweg

- Umgebung und eigenen Projektordner verstehen
- Git, Agenten-Kontext und Spec Kit vorbereiten
- Anforderungen, Plan und Aufgaben prüfen
- Begrenzte Umsetzung und Ergebnisse reviewen

::: notes
Spec Kit gliedert einen Arbeitsauftrag in Anforderungen, Planung und Aufgaben. Ein Review ist eine bewusste Prüfung durch eine andere Person oder einen dafür beauftragten Agenten. Heute werden diese Schritte erklärt, nicht automatisch genehmigt. Nach jeder Phase darf die Gruppe pausieren. Details stehen im Lernendenindex und in der FAQ dieses Repositories.
:::

---

<!-- slide: W03 -->
# Host, Image und Container

- Host: dein echter Rechner
- Image: vorbereiteter Werkzeugbestand
- Container: laufende Umgebung aus einem Image
- Mount: Verbindung zu echten Host-Dateien

::: notes
Ein beschreibbarer Mount erlaubt Änderungen und Löschungen auch auf dem Host. Ein Volume ist dagegen ein von Podman verwalteter dauerhafter Datenspeicher. Beides ist keine Datensicherung. Desktop-IDE und Desktop-Agenten sind nicht automatisch mit der CLI im Container verbunden. Textalternative zum Schaubild: Der Host stellt einen ausgewählten Projektordner bereit; der Container greift über den Mount darauf zu; Agentenzustände liegen in getrennten Volumes.
:::

---

<!-- slide: W04 -->
# Den richtigen Plattformweg wählen

- Apple Silicon: linux/arm64, nativ ohne Rosetta-Fallback
- Windows Intel/AMD: PowerShell 7 und Podman-Machine
- Ubuntu/WSL2: eigener rootless Podman unter Linux
- Gleiche Hardware ersetzt keine getrennten Nachweise

```text
podman info
podman-compose config
```

::: notes
Ort: Host im Sandbox-Checkout, Bash oder PowerShell 7. podman info soll antworten; config prüft die Compose-Datei ohne Build oder Start. Rootless bedeutet Betrieb ohne Root-Rechte auf dem jeweiligen Linux-System. Windows und Ubuntu/WSL2 verwenden getrennte Podman-Laufzeiten. Ein ARM64-Erfolg beweist keine AMD64-Abnahme; WSL2 ist kein Nachweis nativer Linux-Hardware. Fehlerhilfe: docs/fuer-lernende/installation.md und troubleshooting.md.
:::

---

<!-- slide: W05 -->
# Ein eigenes Repository verwenden

- Fork als Standard; Template später optional
- origin ist dein beschreibbarer Ursprung
- upstream braucht einen passenden Referenzbezug
- GitHub ist ein Weg, keine allgemeine Voraussetzung

```text
git status --short --branch
git remote -v
```

::: notes
Ort: Host im eigenen Projekt-Checkout. Ein Fork erhält die Beziehung und Historie der Referenz und bleibt Standard. Ein Template erzeugt eine unabhängige Historie; das zusätzliche Profil ist vorbereitet, noch nicht aktiviert. Ein Remote-Name erzeugt keine gemeinsame Historie: keine pauschalen Upstream- oder Unrelated-History-Merges. Kopierte Freigaben, Statistiken und Run-States sind nur Referenzkontext. Für SysInfo/Web weiterhin ein leeres Produktrepo und genau ein Lernpaket nutzen, nicht die gesamte Sandbox. Die Home-Baseline bleibt separat. Die Befehle ändern nichts, können aber private URLs zeigen; Ausgaben vor Weitergabe bereinigen. GitLab, Codeberg, Forgejo und institutionelle Systeme bleiben möglich. Commit/Push bleiben getrennte Entscheidungen. Details: docs/fuer-lernende/template-profil.md.
:::

---

<!-- slide: W06 -->
# Projekt-Mounts bewusst einrichten

- .env enthält lokale Compose-Werte
- opencode.env bleibt ohne Provider unverändert
- Vorhandene Dateien niemals durch Vorlagen ersetzen
- Nur benötigte Ordner, nicht das ganze Home mounten

```text
if [ ! -e .env ]; then cp .env.example .env; fi
if [ ! -e opencode.env ]; then
  cp opencode.env.example opencode.env
fi
chmod 600 .env opencode.env
```

::: notes
Ort: Host im Sandbox-Checkout, Bash. PowerShell-Alternative: if (-not (Test-Path -LiteralPath .env)) { Copy-Item .env.example .env }; entsprechend für opencode.env. Unter Windows lokale Dateirechte über die Dateisystem-Berechtigungen schützen; chmod ist dort keine allgemeine ACL-Anweisung. Erwartung: vorhandene Dateien bleiben unverändert. .env wird nicht in das Image eingebaut. Neue Mounts brauchen eine kontrollierte Container-Neuerstellung, nicht zwingend einen Image-Neubau. Details: installation.md und faq.md.
:::

---

<!-- slide: W07 -->
# Ein erster Test ohne KI-Konto

- Host öffnet die Container-Shell
- Benutzer und Arbeitsort prüfen
- Ein kleines Programm im Projekt-Mount ausführen
- Gleiche Ausgabe ist keine vollständige Plattformabnahme

```text
podman compose exec ade bash
# Danach im Container / then inside the container:
id
pwd
python -c 'print("Hello from the sandbox")'
```

::: notes
Der erste Befehl läuft auf dem Host, die folgenden in der geöffneten Container-Shell. Erwartung: adedev, UID ungleich 0 und die Hello-Ausgabe. Für C#, Java, Go, Rust oder Swift die jeweilige Toolchain-Anleitung verwenden. Eine IDE auf dem Host darf Dateien bearbeiten; Compiler müssen nicht zusätzlich auf dem Host installiert sein. Die Anleitung behauptet weder perfekte Isolation noch einen bestandenen Windows-/Linux-Test. Fehlerhilfe: erste-schritte.md.
:::

---

<!-- slide: W08 -->
# Agenten-Kontext vor dem Auftrag

- Projekt-README und vorhandene Agent-Regeln lesen
- AGENTS.md hält dauerhafte Projektkonventionen fest
- Gemeinsame Regeln für alle gepflegten Agenten erhalten
- Anmeldung und Berechtigungen nicht automatisieren

::: notes
Eine Agent-CLI ist ein Kommandozeilenprogramm, das einen KI-Agenten ausführt. Ihre Installation ist keine Provider-, Modell- oder Datenfreigabe. OpenCode 2 hat in dieser Sandbox ausdrücklich offene Kontroll- und Audit-Nachprüfungen. Für praktische Aufgaben nur einen projektspezifisch freigegebenen Agenten verwenden. Der Prompt-Dispatcher unterstützt Einzelaufträge, umgeht aber weder Anmeldung noch Freigaben. Siehe agenten-und-spec-kit.md und agent-prompt.md.
:::

---

<!-- slide: W09 -->
# Ein begrenzter AGENTS.md-Auftrag

- Erst belegbare Repo-Signale lesen
- Nur dauerhafte, projektspezifische Regeln ergänzen
- Keine Kommandos oder Freigaben erfinden
- Diff und offene Annahmen zeigen lassen

```text
Lies README, Projektdateien, Skripte und Agent-Regeln.
Ergänze nur belegbare Projektkonventionen in AGENTS.md.
Erhalte Sicherheitsgrenzen und vorhandene Hinweise.
Zeige Diff und offene Annahmen. Kein Commit oder Push.
```

::: notes
Ort: Chat eines freigegebenen Agenten im Anwendungsprojekt, nicht in der Shell. /init ist kein universeller Agentenbefehl. Vor einer Änderung die bestehenden Dateien lesen; in einem bestehenden Projekt keine Regeln pauschal ersetzen. In dieser Sandbox werden gemeinsame Agent-Regeln auf fünf Flächen synchron gepflegt. Ein Anwendungsprojekt bestimmt seine eigenen gepflegten Flächen.
:::

---

<!-- slide: W10 -->
# Spec Kit kontrolliert initialisieren

- Das Image pinnt Spec Kit 1.2.3
- Vorhandene .specify-Struktur zuerst prüfen
- Eine passende Agenten-Integration auswählen
- Keine globale Installation und kein ungeprüftes --force

```text
specify --version
specify check
# Nur im vorbereiteten neuen Projekt / new project only:
specify init . --integration codex
```

::: notes
Ort: Container-Bash im vorbereiteten Anwendungsprojekt. Erwartung: CLI-Version und verfügbare Werkzeuge werden angezeigt. Initialisierung schreibt Projektartefakte und ist deshalb ein gesondert genehmigter Schritt. Bei vorhandenen Dateien zuerst Diff, Sicherung und Zweck klären. Linux-Skripte passen zum Container; PowerShell ist zusätzlich installiert, aber nicht mit dem Windows-Host zu verwechseln. Die gepinnte Version steht im Dockerfile. Kein Initialisierungsbefehl wird durch das bloße Lesen der Folie ausgeführt.
:::

---

<!-- slide: W11 -->
# Shell-Befehl oder Agenten-Aufruf?

- specify init gehört in die Shell
- $speckit-analyze ist ein Codex-Skill-Aufruf
- Andere Integrationen haben andere Schreibweisen
- Vorhandene Skills prüfen, nicht Schreibweisen erraten

::: notes
Beispiele im Agenten-Chat: Codex $speckit-analyze; OpenCode /speckit.analyze; Claude Code, Antigravity und Copilot je nach installierter Skill-Integration /speckit-analyze. Dies sind Integrationsbeispiele, keine aktuelle Freigabe aller Agenten. Die folgenden Prompts verwenden Codex-Schreibweise. In einer anderen Integration nur den Aufruf anpassen; Auftrag und Sicherheitsgrenzen erhalten. Unterstützte CLI-Schlüssel und tatsächlich erzeugte Dateien vor einer Live-Demo prüfen.
:::

---

<!-- slide: W12 -->
# Governance-Presets zuerst verstehen

- Ein Preset ergänzt Regeln für den Arbeitsablauf
- Kleine Prioritätszahlen haben Vorrang
- Installation ist keine Kontrolle-Erfüllung
- Bestehende Versionen und lokale Änderungen prüfen

```text
specify preset list
git status --short
```

::: notes
Ort: Container-Bash im initialisierten Anwendungsprojekt. Erwartung: Liste installierter Presets und bestehender Änderungen. Die Repository-Matrizen sind geprüfte Quellen für Versionen, Prioritäten und Archive. Nicht still auf latest wechseln. Eine neue Version kann Nachweise und Quellenbindungen ändern. Die Lernbegleitung entscheidet über anwendbare Profile und Installationsrechte.
:::

---

<!-- slide: W13 -->
# Sechs fachliche Basis-Presets

- Security und Architecture
- iSAQB Architecture und A11Y
- Cross-Platform und Agent Parity
- Das verwaltete Standardprofil enthält zusätzlich zwei Lauf-Presets

::: notes
Die sechs Bereiche sind der fachliche Einstieg. Das hiesige Standardprofil enthält acht Pakete: zusätzlich Autonomous Run und Parallel Autonomous Run. Ihre Installation erteilt keine autonome Ausführungsbefugnis. Für den Workshop vorhandene, genehmigte Profile bevorzugen. Die vollständige lokale Pilotmatrix enthält 14 Pakete; sie ist nicht pauschal für jedes Lernendenprojekt vorgeschrieben.
:::

---

<!-- slide: W14 -->
# Security und Architecture

- Security: Schutzbedarf, Secrets und Lieferketten
- Architecture: Grenzen, Entscheidungen und Risiken
- Annahmen und Nachweise sichtbar trennen
- Menschliche Freigaben bleiben menschlich

::: notes
Ein Secret ist eine vertrauliche Zugangsinformation. Eine Lieferkette umfasst Quellen, Pakete und Buildschritte. Ein Architekturentscheid erklärt eine bewusste technische Wahl mit Alternativen und Folgen. Beispiel: Projektordner wird gemountet, das gesamte Host-Home nicht. Eine SBOM ist ein Komponentenverzeichnis; sie beweist nicht, dass ein Image frei von Schwachstellen oder genehmigt ist.
:::

---

<!-- slide: W15 -->
# iSAQB und Barrierefreiheit

- iSAQB: nachvollziehbare Architektur und Qualitätsziele
- A11Y: verständliche Inhalte und zugängliche Bedienung
- Deutsch zuerst, gleichwertiges Englisch
- Automatische Checks ersetzen keine menschliche Prüfung

::: notes
iSAQB bezeichnet eine Architektur-Prüfbasis; für den Einstieg genügt eine nachvollziehbare Beschreibung von Bausteinen und Entscheidungen. A11Y ist eine Kurzform für Accessibility, also Barrierefreiheit. WCAG 2.2 AA ist ein Prüfziel für anwendbare Kriterien, keine automatische Eigenschaft dieser Präsentation. Tastatur, Screenreader, Lesereihenfolge und Verständlichkeit mit Menschen prüfen. CEFR B2 beschreibt unser Sprachziel.
:::

---

<!-- slide: W16 -->
# Cross-Platform und Agent Parity

- Befehle mit Ort und Shell kennzeichnen
- ARM64 und AMD64 getrennt prüfen
- Windows und Ubuntu/WSL2 getrennt belegen
- Gemeinsame Agent-Regeln synchron pflegen

::: notes
Parity bedeutet hier inhaltliche Übereinstimmung, nicht identische Software auf allen Plattformen. Bash- und PowerShell-Varianten können auf demselben Host getestet werden; das ist kein nativer Windows-Nachweis. Fehlende Tests bleiben Open mit Owner, nächstem Schritt und Anlass zur Neubewertung. Der Container bleibt Linux, auch wenn PowerShell darin läuft.
:::

---

<!-- slide: W17 -->
# Vor Installation eine Vorschau

- Im vorbereiteten Anwendungsprojekt arbeiten
- Verwaltete Matrix ausdrücklich auswählen
- Erst --dry-run, dann menschlich prüfen
- Ohne Installationsauftrag nichts anwenden

```text
repo=/ade-dev-sandbox
matrix="$repo/scripts/config/spec-kit-governance-presets.json"
bash "$repo/scripts/install-spec-kit-governance-presets.sh" \
  --repo "$PWD" --preset-config "$matrix" --dry-run
```

::: notes
Ort: Container-Bash im Anwendungsprojekt; /ade-dev-sandbox ist der vorhandene Repository-Mount. Erwartung: Vorschau, keine Installation. Vorhandene lokale Ergänzungen und Versionen sichern. Das Weglassen von --dry-run ist ein schreibender Schritt und braucht einen eigenen Auftrag. Skriptoptionen nicht mit Werkzeugen anderer Sandbox-Repositories vermischen. Bei fehlendem Mount die Lernbegleitung fragen, keinen fremden Installer herunterladen.
:::

---

<!-- slide: W18 -->
# Zusatzprofile nach Bedarf wählen

- Intake: Anforderungen erfassen, prüfen und ordnen
- Model Routing: Aufgabenrollen operativ zuordnen
- Assurance: projektspezifische Kontrollnachweise
- Statistics: optionale Pilot-Auswertung

::: notes
Die Matrixnamen stehen unter scripts/config/. Das 14er-Profil ist ausdrücklich ein optionales Statistics-Pilotprofil. Keine Modelle in Feature-Specs festschreiben und keine Provider- oder Plattformfreigabe aus einer Preset-Installation ableiten. Vor Auswahl Zweck, Voraussetzungen und Auswirkungen mit der Lernbegleitung prüfen. Assurance-Paketversion und Evidence-Schema sind verschiedene Versionsangaben.
:::

---

<!-- slide: W19 -->
# Versionen und Prioritäten belegen

- Matrix und tatsächlich installierten Stand vergleichen
- Quellen und lokale Änderungen nachvollziehen
- Profile nicht unbeabsichtigt erweitern
- Abweichungen als Open behandeln

```text
repo=/ade-dev-sandbox
bash "$repo/scripts/install-spec-kit-governance-presets.sh" \
  --repo "$PWD" --check-only
specify preset list
```

::: notes
Ort: Container-Bash im Projekt. --check-only prüft die ausgewählte Matrix ohne Schreibabsicht. Das Beispiel verwendet das Standardprofil mit acht Paketen; für ein anderes genehmigtes Profil --preset-config ausdrücklich angeben. Ein Fehler wird nicht durch --force beseitigt. Prüfung, technische Erfüllung und menschliche Freigabe sind getrennte Zustände.
:::

---

<!-- slide: W20 -->
# Intake: einen Auftrag festhalten

- Zielgruppe, Problem und Ergebnis benennen
- Scope und Nicht-Ziele ausdrücklich festhalten
- Quellen geordnet und nachvollziehbar binden
- Offene Entscheidungen nicht erraten

::: notes
Ein Intake ist eine Anforderungsdatei vor dem eigentlichen Feature-Lauf. Ein Receipt hält ihre Herkunft und Quellenbindungen fest; ein Hash ist eine Prüfsumme für den Inhalt. Eine Änderung gebundener Quellen kann ein neues Update und Review erfordern. Bestehende Intake-IDs erhalten, Vorzustände archivieren und Quellen nicht nur zum Bestehen eines Validators austauschen. Im Workshop ein neues, ausdrücklich abgegrenztes Beispiel verwenden, nicht die aktiven Sandbox-Intakes ausführen.
:::

---

<!-- slide: W21 -->
# Review und Reihenfolge vor dem Start

- Anforderungen vollständig und unabhängig prüfen
- Abhängigkeiten und Übergaben ausdrücklich nennen
- Ready und Eligible sind keine Startbefugnis
- Einen blockierten Nachfolger nicht überspringen

::: notes
Eine Intake-Reihe ordnet mehrere Aufträge durch Abhängigkeiten. Das maschinenlesbare Manifest ist maßgeblich; Text und Diagramm erklären denselben Zustand. Ein unabhängiges Review prüft Inhalte, nicht nur Hashes. Ein erfolgreiches Anforderungen-Review ist keine technische Sandbox-, Rechts-, Datenschutz-, Provider- oder Release-Freigabe. Die aktive Sandbox-Reihe bleibt von diesem Workshop unberührt.
:::

---

<!-- slide: W22 -->
# Autonomie braucht klare Grenzen

- Ziel, Dateien und erlaubte Aktionen festlegen
- Stop-Regeln und menschliche Entscheidungen nennen
- Commit, Push und Merge getrennt genehmigen
- Modellwahl bleibt operative Agenten-Guidance

::: notes
Autonomous Run steuert einen ausdrücklich beauftragten Lauf; Parallel Autonomous Run koordiniert getrennte Läufe. Beides ist keine pauschale Erlaubnis. Secrets, formelle Freigaben und Plattformregeln bleiben menschliche Aufgaben. Ein Abbruchgrund muss verständlich gemeldet werden. Modellnamen gehören nicht in reproduzierbare spec.md-, plan.md- oder tasks.md-Artefakte.
:::

---

<!-- slide: W23 -->
# Nachweise statt grüne Behauptungen

- Datum, Version, Plattform und Ergebnis festhalten
- Open: Owner, Follow-up und Trigger nennen
- N/A braucht eine nachvollziehbare Begründung
- Statistiken messen keine Personenleistung

::: notes
Ein Follow-up ist der nächste geplante Schritt; ein Trigger ist der Anlass für erneute Prüfung. Erfolgreiche PDF-Erzeugung beweist keine PDF-Barrierefreiheit. Eine SBOM beweist keine Schwachstellenfreiheit. Projektstatistiken beschreiben dokumentierte Lieferaktivität, keine Arbeitszeit oder persönliche Produktivität. Das optionale Pilotprofil nicht ohne Projektentscheidung installieren.
:::

---

<!-- slide: W24 -->
# Bestehende Projekte nicht überschreiben

- Vor jeder Einrichtung git status lesen
- Lokale Regeln und Presets erhalten
- Änderungen klein und überprüfbar halten
- Keine Reparatur durch pauschales --force

```text
git status --short
git diff
specify preset list
```

::: notes
Ort: Container-Bash im Anwendungsprojekt. git diff zeigt keine ungetrackten Dateien; deshalb zusätzlich git status und neue Dateien lesen. Vor Updates Sicherung und Auswirkungen klären. Der eingebettete Home-Baseline-Stand ist schreibgeschützt; er ist kein Ziel für Workshop-Änderungen. Kein Home-Sync läuft automatisch. Außerhalb dieser Sandbox unterscheiden sich Installer und Host-Berechtigungen; hierfür gibt es keinen stillen Fallback.
:::

---

<!-- slide: W25 -->
# Unser Beispiel: SysInfoTool

- Kleines Konsolenprogramm mit erfundenen Daten
- Eine der sechs Sprachtoolchains wählen
- Keine echten Benutzer-, Host- oder Netzwerkdaten sammeln
- Noch keine Umsetzung starten

::: notes
Möglicher Auftrag: Ein Konsolenprogramm zeigt drei festgelegte Beispielwerte und unterstützt deutsche sowie englische Beschriftungen. Fehlerfälle und Erfolgskriterien werden vor der Implementierung beschrieben. C#/.NET, Java, Go, Rust, Python und Swift sind alternative Toolchains, nicht alle gleichzeitig verpflichtend. Python und PowerShell ergänzen die Skriptgrundlagen. Keine echten API-Schlüssel oder Provideraufrufe für dieses Beispiel nötig.
:::

---

<!-- slide: W26 -->
# Constitution: Projektprinzipien

- Langlebige Regeln des Anwendungsprojekts
- Sicherheit, Qualität und Zuständigkeiten benennen
- MUST, SHOULD und MAY bewusst unterscheiden
- Bestehende Verfassung zuerst lesen

```text
$speckit-constitution
Prüfe die vorhandenen Projektprinzipien für SysInfoTool.
Nutze nur erfundene Daten; keine Secrets oder Provider.
Zeige Auswirkungen auf abhängige Artefakte.
Keine Implementierung, kein Commit oder Push.
```

::: notes
Ort: Agenten-Chat im separat genehmigten Anwendungsprojekt. MUST bedeutet verbindlich, SHOULD begründete Empfehlung und MAY erlaubte Option. Eine geänderte Verfassung kann abhängige Artefakte betreffen; diese Auswirkungen müssen sichtbar werden. Der Aufruf startet keine Änderung an der Verfassung des Sandbox-Repositories. Jede konkrete Änderung anschließend menschlich lesen und entscheiden.
:::

---

<!-- slide: W27 -->
# Specify: Anforderungen beschreiben

- Zielgruppe, Nutzen und Grenzen beschreiben
- Prüfbarkeit statt Lösungsdetails verlangen
- Nicht-Ziele ausdrücklich festhalten
- spec.md anschließend lesen und verstehen

```text
$speckit-specify
Spezifiziere SysInfoTool mit drei erfundenen Beispielwerten.
Definiere DE/EN-Ausgaben, Fehlerfälle und Erfolgskriterien.
Keine echte Systemdatenerhebung oder Netzverbindung.
Keine Implementierung und keine Git-Lieferung.
```

::: notes
Ein funktionales Requirement beschreibt gewünschtes Verhalten; ein Akzeptanzkriterium zeigt, woran es überprüfbar erfüllt wäre. Eine User Story erklärt Bedarf aus Sicht einer Person. Diese Begriffe vorlesen und an einem kleinen Beispiel erläutern. Vorgegebene Lastenhefte als verbindliche Eingabe benennen, nicht durch spontan erfundene Anforderungen ersetzen. Aktive Sandbox-Spezifikationen bleiben unberührt.
:::

---

<!-- slide: W28 -->
# Clarify: wichtige Entscheidungen klären

- Nur Unklarheiten mit echten Auswirkungen fragen
- Genau eine Frage nach der anderen
- Höchstens fünf Fragen pro Durchgang
- Entscheidung und Begründung nachvollziehbar festhalten

```text
$speckit-clarify
Prüfe die aktive SysInfoTool-Spec auf wichtige Unklarheiten.
Maximal fünf Fragen, einzeln, mit Empfehlung.
Keine Umsetzung; bereits entschiedene Punkte erhalten.
```

::: notes
Beispiele für wichtige Entscheidungen: Welche Daten dürfen angezeigt werden? Was passiert bei einer unbekannten Sprache? Keine Rückfrage nur zur persönlichen Wortwahl stellen. Technische Details können in die Planung gehören. Ein weiterer Durchgang ist nur nötig, wenn neue entscheidungsrelevante Fragen sichtbar sind; keine Wiederholung bis zu einer beliebigen grünen Behauptung.
:::

---

<!-- slide: W29 -->
# Klären oder bewusst zurückstellen?

- Anforderungen und Sicherheitsgrenzen jetzt entscheiden
- Implementierungsdetails später im Plan behandeln
- Zurückstellung mit Owner und Anlass festhalten
- Bei Blockern stoppen statt eine Freigabe zu erfinden

::: notes
Deferred heißt bewusst zurückgestellt. Das ist kein erledigter Punkt. Beispiel: konkrete interne Dateiaufteilung später planen; erlaubte Daten bereits vor der Planung entscheiden. Für Open-Punkte Owner, Follow-up und Re-Evaluation-Trigger nennen. Eine Person ohne Spezialkenntnisse muss verstehen können, was bis zur Entscheidung nicht ausgeführt werden darf.
:::

---

<!-- slide: W30 -->
# Plan: technische Umsetzung vorbereiten

- Anforderungen in einen passenden technischen Weg übersetzen
- Sicherheits- und Architekturgrenzen erhalten
- Relevante Nachweise und Tests planen
- Noch keine Implementierung ausführen

```text
$speckit-plan
Plane nur die aktive SysInfoTool-Spec.
Nutze vorhandene Projektkonventionen und Testwerkzeuge.
Begründe N/A und dokumentiere offene Nachweise.
Keine Tasks erzeugen oder Implementierung starten.
```

::: notes
Ein Plan beschreibt das Wie: Bausteine, Schnittstellen, Datenfluss, Fehlerfälle und Nachweise. Keine Datenbank oder API erfinden, wenn das Beispiel keine braucht. N/A heißt nicht anwendbar und braucht eine kurze Begründung. Geplante Tests sind noch keine bestandenen Tests. Security-, Architecture-, iSAQB-, A11Y-, Cross-Platform- und Agent-Parity-Punkte nach Anwendbarkeit prüfen.
:::

---

<!-- slide: W31 -->
# Checklist: Qualität der Anforderungen

- Sind Aussagen klar und vollständig?
- Sind Kriterien messbar und widerspruchsfrei?
- Hat jeder Prüfpunkt einen Durchführungshinweis?
- Das ist noch kein Implementierungs- oder Funktionstest

```text
$speckit-checklist
Prüfe die Qualität der aktiven Anforderungen.
Jeder Prüfpunkt braucht Referenz und Durchführungshinweis.
Keine Builds, Laufzeittests oder Implementierungsprüfung.
```

::: notes
Beispiel: Ist die Sprache bei unbekannter Auswahl eindeutig festgelegt? Der Durchführungshinweis nennt die zu lesende Textstelle und erkennbare Qualitätsmerkmale. Die Frage lautet nicht: Funktioniert die Sprachumschaltung? Das wäre ein späterer Funktionstest. Fehlende Anforderungen als Lücke benennen und Änderungen ausdrücklich beauftragen, nicht als automatische Remediation verstecken.
:::

---

<!-- slide: W32 -->
# Tasks: kleine ausführbare Aufgaben

- Jede Anforderung durch Aufgaben abdecken
- Abhängigkeiten und konkrete Dateien nennen
- [P] nur bei wirklich unabhängigen Arbeiten
- Aufgaben erst nach Erledigung mit [X] markieren

```text
$speckit-tasks
Erzeuge tasks.md aus aktiver spec.md und plan.md.
Nenne Abhängigkeiten, Dateien und Validierung.
Keine Implementierung, kein Commit oder Push.
```

::: notes
MVP bezeichnet die kleinste sinnvoll prüfbare erste Ausbaustufe. User-Story-Aufgaben erhalten die vereinbarten Story-IDs. Ein [P] ist kein Auftrag, weitere Agenten ohne Erlaubnis zu starten. TDD-Testaufgaben nur dort planen, wo passende Produktlogik und ein tatsächlicher Testweg existieren; Dokumentationsarbeit nicht mit erfundenen Runtime-Tests aufblähen.
:::

---

<!-- slide: W33 -->
# Analyze: Artefakte lesend abgleichen

- Spec, Plan und Tasks auf Konsistenz prüfen
- Anforderungen und Erfolgskriterien zu Aufgaben zuordnen
- Findings mit stabilen IDs und Schweregrad melden
- Keine Dateien während Analyze verändern

```text
$speckit-analyze
Prüfe aktive Spec, Plan und Tasks strikt read-only.
Melde Lücken, Widersprüche und fehlende Task-Abdeckung.
Keine Remediation, Builds, Commits oder Pushes.
```

::: notes
Traceability bedeutet nachvollziehbare Zuordnung zwischen Anforderung, Aufgabe und späterem Nachweis. Eine Analyse darf keine Freigaben behaupten und keine vorhandenen Findings ohne Begründung verschwinden lassen. Eine aktuelle Analyse ist keine technische Plattformabnahme. Für einen neuen Stand dieselben Prüfziele verwenden; einen historischen Vergleich nur mit belegbarer Voranalyse behaupten.
:::

---

<!-- slide: W34 -->
# Findings gezielt beheben

- Zuerst konkrete Findings und betroffene Dateien nennen
- Korrekturen gesondert beauftragen
- Danach nur den relevanten Stand erneut prüfen
- Bei unklaren Entscheidungen stoppen

```text
Behebe nur die bestätigten Findings C1 und C2.
Erhalte Sicherheitsgrenzen und bereits entschiedenen Scope.
Keine Umsetzung des Features, kein Commit oder Push.
Berichte die Änderungen; Analyze erfolgt danach lesend.
```

::: notes
Es gibt keine feste Zahl von Analyze-Wiederholungen und keinen Auftrag, sich zu Tode zu prüfen. Ein fokussierter Lauf, konkrete Korrektur und gezielte Nachprüfung reichen, wenn keine relevanten Blocker übrig bleiben. Verfassungs-MUST-Verstöße und bestätigte schwere Findings nicht durch geschönte Statuswerte umgehen. Menschliche Risikofreigaben nicht ersetzen.
:::

---

<!-- slide: W35 -->
# Implement: nur mit aktuellem Auftrag

- Aktuelle Spec, Plan und Tasks erneut lesen
- Checklisten und Voraussetzungen prüfen
- Aufgaben in ihrer Abhängigkeit umsetzen
- Tatsächliche Tests und Stop-Gründe dokumentieren

```text
$speckit-implement
Implementiere nur die freigegebenen SysInfoTool-Tasks.
Markiere Aufgaben erst nach prüfbarer Erledigung.
Stoppe bei Secrets oder fehlender menschlicher Entscheidung.
Kein Commit, Push, Container-Neubau oder Hosting-Eingriff.
```

::: notes
Der Beispielauftrag muss zum tatsächlichen Projekt passen. Projekttests und ein Sandbox-Image-Build sind verschiedene Aktionen. Eine frische Agentensitzung kann helfen, muss aber Repo-Regeln, aktuelle Artefakte und nachweisbare Entscheidungen erneut lesen; nicht blind einen komplett leeren Kontext verlangen. Für lange Läufe Fortschritt und Stop-Regeln festlegen. Nicht unbeaufsichtigt sensible Aufgaben laufen lassen.
:::

---

<!-- slide: W36 -->
# Review, Tests und sichere Daten

- Änderungen und neue Dateien menschlich prüfen
- Geplante und wirklich ausgeführte Tests unterscheiden
- Projektdateien im vorgesehenen Mount speichern
- Commit und Push bewusst getrennt entscheiden

```text
git status --short
git diff
# Im Anwendungsprojekt / in the application project:
# dokumentierte Projekttests / documented project tests
```

::: notes
Ort: Container-Shell im Anwendungsprojekt. Erwartung: nachvollziehbarer Diff und sichtbare neue Dateien. Ein erfolgreicher Smoke-Test ist ein kleiner Funktionstest, keine vollständige Sicherheits- oder Barrierefreiheitsabnahme. Persistente Agentenzustände können Zugangsdaten enthalten; nicht ins Repository kopieren. SBOMs und Auditnachweise nach dem vorgesehenen Prozess behandeln.
:::

---

<!-- slide: W37 -->
# Die Sitzung sauber beenden

- Arbeit im Projekt-Mount speichern
- Container-Shell verlassen
- Audit-Wrapper auf dem Host ausführen
- Keine Volume-Löschung im normalen Alltag

```text
# Host, Bash:
bash scripts/compose-down-with-audit.sh --podman
# Host, PowerShell 7 (Alternative):
.\scripts\compose-down-with-audit.ps1 -Engine podman
```

::: notes
Voraussetzung: Terminal wieder im Sandbox-Checkout auf dem Host. Erwartung: erfolgreicher Metadatenexport vor compose down; Volumes bleiben erhalten. Bei Exportfehler stoppen, nicht direkt down als Umgehung verwenden. Nie -v oder -Volumes als normale Stoppoption hinzufügen: diese Optionen können Agentendaten und Anmeldungen löschen. OpenCode-2-Dateimetadaten beweisen keine vollständige Sitzungsabdeckung. Ein Machine-Stopp ist eine separate Hostaktion. Details: alltag.md.
:::

---

<!-- slide: W38 -->
# Begriffe zum Mitnehmen

- Spec: prüfbare Anforderungen; Plan: technischer Weg
- Tasks: kleine Aufgaben; Evidence: tatsächlicher Nachweis
- Open: offen; N/A: begründet nicht anwendbar
- Ready ist keine Start-, Produkt- oder Release-Freigabe

::: notes
Weitere Begriffe: MSL bezeichnet hier die sechs Sprachpfade; das ist keine Garantie, dass jeder Code sicher ist. STRIDE ist eine Methode zur Bedrohungsanalyse. CIA benennt Vertraulichkeit, Integrität und Verfügbarkeit. SBOM ist ein Komponentenverzeichnis; VEX beschreibt begründete Schwachstellen-Aussagen; SLSA betrachtet Lieferkettennachweise. Nicht alles ist für jedes Projekt anwendbar. Das Glossar der Lernenden-Dokumentation erklärt Details.
:::

---

<!-- slide: W39 -->
# Nächster Schritt und Materialien

- Lernweg und passende Toolchain wählen
- Ein kleines, ausdrücklich genehmigtes Projekt beginnen
- Fragen und offene Nachweise mit der Lernbegleitung klären
- Markdown, Sprecherhinweise und Profilmatrix mitnehmen

::: notes
Materialien: docs/fuer-lernende/README.md, lernwege.md, installation.md, agenten-und-spec-kit.md und alltag.md; aktuelle Sicherheitsgrenzen stehen in docs/security/toolchain-followups-2026-10-25.md. Die folgende Profilmatrix in dieser Markdown-Quelle und den Sprecherhinweisen wird aus der vorhandenen lokalen Konfiguration übernommen. Sie zeigt einen dokumentierten Stand, keine Aufforderung zur Installation aller Pakete. Keine institutionellen Zugänge oder fremden Präsentationsvorlagen nötig.

Lokaler Pilotstand, keine Installationsfreigabe:

| Preset | Version | Priority |
|---|---|---|
| security-governance | v0.7.4 | 10 |
| secure-development-assurance-governance | v0.1.8 | 15 |
| architecture-governance | v0.6.5 | 20 |
| isaqb-architecture-governance | v0.2.5 | 30 |
| a11y-governance | v0.4.6 | 40 |
| cross-platform-governance | v0.2.5 | 50 |
| agent-parity-governance | v0.4.5 | 60 |
| model-routing-governance | v0.1.7 | 61 |
| intake-authoring-governance | v0.3.10 | 64 |
| intake-review-governance | v0.2.7 | 65 |
| intake-sequencing-governance | v0.2.11 | 66 |
| autonomous-run-governance | v0.4.7 | 70 |
| parallel-autonomous-run-governance | v0.2.9 | 80 |
| project-statistics-governance | v0.1.3 | 90 |

https://github.com/hindermath/absdd-image-sandbox
https://github.com/github/spec-kit/tree/v1.2.3

:::

---
