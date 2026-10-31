# Feature 004: Bedrohungsmodell / Threat model

## Deutsch

**Stand:** 2026-10-31, Ausgangsrevision `51757c98f6a872419be6b9ae4d33685fe0782b67`. Dies ist ein Quellcode- und Konfigurationsmodell vor der Feature-004-Implementierung. Der Codex-Security-Scan `4af7bffe-c319-4f8a-86b1-3a3623e50c5e` lieferte einen partiellen Ausgangsbefund, keine Runtime-Freigabe. Die Projektgrenze und Entscheidungen stehen in [context-and-decisions.md](../../../architecture/004-container-hardening-followup/context-and-decisions.md).

### Schutzgüter, Akteure und Datenklassen

Schutzgüter sind Host-Projekte und Repositorys, persistente Agentenzustände und Zugangsdaten, auditierbare Metadaten, das lokale Image mit seinen Toolchains, Build-/Download-Herkunft sowie verlässliche technische Nachweise. Datenklassen: öffentliche Quellen; künstliche Testdaten; möglicherweise vertrauliche Projekt- und Agentendaten; besonders schützenswerte Credentials. Lernende und Maintainer wählen Projektpfade und Kommandos. Ein weniger vertrauenswürdiger Checkout, Makefile, Paket-/Release-Artefakt, Registry-Eintrag oder Agenten-Prompt kann Eingaben beeinflussen. Daraus folgt keine Host-Admin- oder Providerfreigabe.

Die Sicherheitsziele sind **C** (Vertraulichkeit: keine Secrets/Prompts an unberechtigte Prozesse oder Artefakte), **I** (Integrität: nur geprüfte Quellen, kontrollierte Host-/Audit-Schreibpfade) und **A** (Verfügbarkeit: reproduzierbarer Build, begrenzte Wartung und sicherer Wiederanlauf). CIA-Werte unten sind relative Schwerpunkte, keine gemessene Risikozahl.

### Textlicher Datenfluss und Trust Boundaries

1. **TB1 Host → Podman-VM → Container:** Hostpfade aus Compose-Variablen werden als Bind-Mounts in `ade` sichtbar. `adedev`, `cap_drop: ALL`, `no-new-privileges` und Loopback-Ports begrenzen den Container, aber Host-Dateirechte und rootless Podman müssen auf der jeweiligen Plattform beobachtet werden. C/I hoch, A mittel.
2. **TB2 Quellen → Root-Build → Image:** Der digest-gepinnte MCR-Start, Paketmanager und direkte Downloads führen externe Bytes in Buildschritte. Ein Download-Hash aus derselben Quelle schützt nicht vor gemeinsamer Manipulation; Swift-Signaturprüfung muss den akzeptierten Signierer an den Pin binden. I hoch, A hoch, C mittel.
3. **TB3 Nutzer/Projekt → Agenten-CLI und Wartung:** Der Prompt-Dispatcher, Agentenregeln, registrierte Checkouts, Makefiles und alternative Registry-Kommandos laufen teils mit Host-, teils mit Containerrechten. Stdin-Datei als Eingabe schützt nicht, wenn der letzte CLI-Aufruf den Prompt in argv setzt. Eine Vorschau darf keine Checkout-Kommandos ausführen. C/I hoch, A mittel.
4. **TB4 Agentenzustand → Audit-Metadaten → Host-Ablage:** Getrennte benannte Volumes bleiben persistent; Export darf nur Metadaten schreiben. Vor `down` sind tatsächlicher regulärer Tagesexport, Mountidentität und sichere 30-Tage-Retention zu verifizieren. OpenCode-2-`session_coverage=not-exported` bleibt eine Nachweisgrenze. C/I hoch, A hoch.
5. **TB5 Container/Wartung → Paketquellen und optionale Provider:** Default-Egress ist frei, um das Lernprofil zu erhalten. Der Netzwerkpfad allein begründet kein Vertrauen in Ziel, Konto oder Modell. Paketmanager können dynamische Endpunkte erreichen; Providerwahl und Anmeldung bleiben explizit beim Menschen. C/I hoch, A mittel.
6. **TB6 Quellcode/Evidenz → Review/Übergabe:** Hashes und Exitcodes binden Versionen, ersetzen aber keine inhaltliche Prüfung. T063-SBOM, T068-unabhängiger Review, Human-only-Freigaben und Plattformbelege sind getrennte Gates. I hoch, C mittel, A mittel.

### STRIDE, CAPEC und Gegenmaßnahmen

| STRIDE | Konkreter Missbrauch und Grenze | CAPEC-Bezug | Gegenmaßnahme und offener Nachweis |
| --- | --- | --- | --- |
| Spoofing | Austausch von Downloadquelle oder vorgegebener Provideridentität an TB2/TB5 | CAPEC-94, CAPEC-148 | TLS, explizite Herkunft/Version und Signiererbindung; T033–T039 und T047, keine Providerfreigabe aus Konfiguration. |
| Tampering | Symlink oder Registry-/Makefile-Inhalt lenkt Host-Schreib- oder Buildpfad an TB1/TB3/TB4 um | CAPEC-153, CAPEC-242 | Physische Pfadgrenzen, keine ausführbare Vorschau, geprüfte Zielidentität; Security-Scan-Befunde vor Code-Freeze einzeln schließen. |
| Repudiation | Stopp meldet erfolgreichen Export ohne zuordenbare aktuelle Auditdatei an TB4 | CAPEC-93 | Exportidentität und reguläre nichtleere Datei vor Retention/Down, eigener Lock, echter Exit; T014–T021. |
| Information disclosure | Prompt in Prozessargumenten oder Secret-Datei über alternativen Agententoolpfad an TB3/TB5 | CAPEC-118, CAPEC-37 | Endgültiger CLI-Aufruf ohne vertraulichen argv-Inhalt; OpenCode-grep-Pfad versionsgebunden prüfen; keine Prompt-/DB-Inhalte exportieren. |
| Denial of service | Unbegrenzte TUI-Ausgabe oder ausfallende Paket-/Scannerquelle blockiert Wartung an TB2/TB3 | CAPEC-125, CAPEC-130 | Begrenzte Streams, klare Fehler-/Timeoutpfade und ehrliches `Open`; keine stillen Fallbacks oder erhöhten Timeouts zum Bestehen. |
| Elevation of privilege | Container- oder Buildprozess nutzt Host-Mount oder vertrauenswürdigen Wartungseinstieg mit höheren Rechten an TB1/TB2/TB3 | CAPEC-233, CAPEC-22 | Non-root-Runtime, dropped capabilities, no-new-privileges, separate Kandidatenressourcen, keine Host-Wartung aus untrusted Preview. |

Die CAPEC-IDs folgen dem lokalen generischen [CL-04-Modell](../../../secure-development/checklisten/CL_04_Bedrohungsmodellierung.md); ihre Zuordnung beschreibt Angriffsmuster, keine beobachtete Ausnutzung. Für jede Hochrisikogrenze sind mehrere relevante Muster oben bzw. in den konkreten Security-Scan-Befunden zu prüfen. Neue Angreiferpfade erfordern eine Aktualisierung dieses Modells.

### Ausgehende Ziele und Zweck

Die folgende Tabelle ordnet **bekannte Quellen und dynamische Zielklassen** zu. Sie ist keine Firewall-Allowlist und beweist keine vollständige DNS-Liste eines Paketmanagers. `Dockerfile` und Konfigurationsdateien sind die Quellen; die tatsächliche Verbindung wird erst beim autorisierten Build/Runtime-Lauf beobachtet.

| Ziel / Zielklasse | Phase und Zweck | Grenze, Kontrolle und offener Punkt |
| --- | --- | --- |
| MCR (`mcr.microsoft.com`) | Build: .NET-Basisimage | Digest-Pin; Registry-/TLS- und Architekturbeleg bei T059. |
| Ubuntu `archive.ubuntu.com`, `security.ubuntu.com`, `ports.ubuntu.com` | Build: OS-Pakete für AMD64/ARM64 | Paketquellen und Signaturen des Paketmanagers; tatsächliche Architektur und Paketstand prüfen. |
| Microsoft `.NET`-Buildquelle `builds.dotnet.microsoft.com` und PowerShell-Azure-Edge | Build: SDK/PowerShell-Artefakte | Version/Hash/Signatur und Umleitungskette prüfen; keine pauschale Vertrauensannahme. |
| `deb.nodesource.com` | Build: Node.js-Quelle | GPG-/Repo-Konfiguration und Pin prüfen. |
| `dlcdn.apache.org`, `archive.apache.org` | Build: Maven und erlaubter Fallback | Gleiche erwartete SHA-512 bei Fallback, keine neue implizite Quelle. |
| `github.com` und Release-Redirects | Build/Setup: Python, Dokumentwerkzeuge, Syft, uv, Spec Kit, Home Baseline und Presets | Exakte Version/Commit/Digest; Redirect-Host und gleiche-Quelle-Prüfsummen als Restrisiko bis T034/T035. |
| `go.dev`, Go-Modul-Proxy und Modulquellen | Build: Go und `go install`-Werkzeuge | Versionen im Dockerfile; dynamische Modulziele in T034 konkret inventarisieren. |
| `static.rust-lang.org` und Rust-Komponentenquelle | Build: rustup und Komponenten | Version/Hash und tatsächlich nachgeladene Komponenten prüfen. |
| `download.swift.org`, `www.swift.org` | Build: Swift-Archiv und Signierschlüssel | Signierer-Pin, Archiv/Signatur-Verbindung und Herkunft prüfen. |
| npm-Registry, Python-/uv-Index und NuGet (`api.nuget.org`) | Build bzw. TUI-Restore: Paketauflösung | Dynamische Paketendpunkte; Lock/Version, Lizenz und tatsächliche Downloadpfade bei T034/T059 prüfen. |
| Brew-, WinGet- und lokale/alternative Tool-Registries | Explizite Host-Wartung | Von Operator/Plattform gewählt; Vergleich/Vorschau darf keine Registry-Kommandos ausführen; T040 und Variantenprüfung. |
| Optionale Agenten-Provider, Telemetrie und Modellendpunkte | Laufzeit nach menschlicher Anmeldung/Wahl | Kein Provider/Modell vorgewählt. Effektive Version, Konto, Region, Datenfluss und Nutzungsentscheidung bleiben Open bis zuständiger Prüfung; keine Endpunkt- oder Null-Telemetriebehauptung. |

**Egress-Entscheidung:** Eine allgemeine Allowlist ist für das Lernprofil nicht aktiviert. Owner für die spätere anlassbezogene Ziel-/Egressbewertung: Repository Owner und Platform/Security Review; Trigger sind neue Paketquelle, Provideranmeldung, Hostingwechsel oder geänderter Datenfluss. Bis dahin ist „freier Egress“ eine benannte Grenze, kein positiver Schutzbeleg. Lokale Loopback-Ports sind eingehende Entwicklungsports und keine der obigen ausgehenden Quellen.

### Revalidierung

Bei Änderung von Mounts, Benutzerrechten, Buildquellen, Agentenversionen, Provider-/Modellwahl, Auditdaten oder öffentlich erreichbaren Ports dieses Modell, [S-ADR-003](../../adr/003-container-isolation.md) und [S-ADR-004](../../adr/004-container-threat-boundaries.md) erneut prüfen. T053 bindet den finalen Code-/Katalogstand; T059–T062 prüfen nur tatsächlich verfügbare Plattformpfade. Ohne T063 oder T068 entsteht keine finale Lieferketten- oder unabhängige Gesamtentscheidung.

## English

This source-bound model separates host/VM/container mounts, root build and downloaded inputs, agent and maintenance commands, persistent state, audit metadata, outbound targets and review evidence. The table gives CIA priorities, realistic STRIDE abuse cases, CAPEC patterns and planned controls. Default egress remains available for learning; the known hosts and dynamic package/provider classes above are an inventory, not a firewall allowlist or proof of every resolved destination. User/provider sign-in, formal approval and legal decisions remain separate. Revalidate the model when mounts, rights, versions, data flows, external targets or ports change. The partial Codex Security scan is an input, not runtime acceptance.
