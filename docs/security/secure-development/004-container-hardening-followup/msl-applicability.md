# Sprachwahl und MSL / Language choice and memory safety

## Deutsch

**Status 2026-10-31: Applicable; technische Begründung, keine Freigabe.** Der Registry-Eintrag für `container-images/absdd-image-sandbox` beschreibt dieses Container- und Skriptrepository. Feature 004 erzeugt keine neue C#-Anwendung. Neue gemeinsame Datei- und Datumslogik gehört in einen kleinen Python-3-Kern mit Standardbibliothek. Python ist hier eine speichersichere Sprache (MSL): übliche rohe Speicherzugriffe wie in C/C++ werden vermieden. Das verhindert weder Pfadwechsel, Symlink-Rennen, unsichere Prozessaufrufe, Datenabfluss noch fehlerhafte Rechte.

Bash bleibt die vorhandene portable Prozess- und Compose-Grenze; PowerShell 7 ist der verwaltete Gegenpart auf den unterstützten Hosts. Diese begrenzte Ausnahme vermeidet eine neue Laufzeit und erhält die dokumentierten Einstiegspunkte. Beide Wrapper müssen Eingaben als Argumente übergeben, nicht als zusammengesetzte Shell-Befehle. Prüfungen erfolgen mit echten Bash-/PowerShell-Prozessen in eigenen temporären Bereichen. Native Dateisystem- und Containergrenzen brauchen zusätzlich Plattformbelege.

| Sprache/Dateiart | Einsatz | Sicherheitsregel und Prüfbeleg |
| --- | --- | --- |
| Python 3 (`scripts/lib/*.py`) | Datums-/Pfad-/JSON-Entscheidungen, Retention, Validierung | Eingabeform und Wurzelbindung vor Wirkung prüfen; `subprocess` mit argv und Timeout; keine `shell=True`-Interpolation; `coverage.py --branch` je namentlichem Modul plus negative Fälle. |
| Bash (`scripts/*.sh`, `scripts/lib/*.sh`) | Host-/Container-Einstieg, Compose und Prozess-Glue | Arrays und quotierte Variablen; `--` wo unterstützt; `set -e` allein ist kein Fehlervertrag; `trap` räumt nur eigene Ressourcen; synthetische Zweig-Outcomes. |
| PowerShell 7 (`scripts/*.ps1`, `.psm1`) | Parität und verwaltete Host-Einstiege | Advanced Functions/`ShouldProcess` bei Änderungen, gebundene Parameter, argv statt `Invoke-Expression`, `-LiteralPath` und Fehlerterminierung; AST-/Outcome-Review zusätzlich zu Pester-Zeilenwerten. |
| Dockerfile/YAML/JSON | Lieferkette und Containerrechte | Gepinnte Artefakte/Hashes, minimale Rechte, explizite Mounts; Konfiguration und echte Runtime getrennt prüfen. |

Die Sprachwahl folgt CR-001/005 und dem generischen Secure-Development-Referenzrahmen. Ein MSL-Label ist kein Testergebnis. Owner: Repository Maintainer; Reviewer: Security Review. Trigger: neue Sprache, native Erweiterung, neue Prozess-/Dateisystemgrenze oder geänderter Laufzeit-Pin. Offene Coverage und native Prüfungen stehen in `coverage-modules.json` und `checkpoints.md`.

## English

**Status 2026-10-31: Applicable; technical rationale, not an approval.** This is a container and script repository, not a new C# application. A small Python 3 standard-library core handles shared file and date rules. Python avoids common raw-memory errors but does not prevent path races, unsafe subprocess calls, data leakage or privilege mistakes. Existing Bash and PowerShell 7 entrypoints remain bounded process glue. Pass argument vectors, validate roots and types before effects, and test actual processes with synthetic temporary resources. Review each language with the rules above; memory safety alone is never accepted as a passing security test. Native filesystem and container claims require separate platform evidence.
