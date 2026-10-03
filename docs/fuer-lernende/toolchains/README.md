# Toolchains und Projektpfade / Toolchains and Project Paths

## Zweck / Purpose

**DE:** Eine **Toolchain** ist die Gruppe von Werkzeugen, mit denen du ein
Programm erstellst, baust, testest und ausführst. Dieses Image stellt mehrere
Toolchains bereit. Arbeite mit Projekten in den vorgesehenen Mounts, damit die
Dateien auf dem Host erhalten bleiben. Temporäre Übungen und Dokumentations-
tests gehören nach `/tmp` oder unter `/home/adedev/smoke-tests`.

**EN:** A **toolchain** is the group of tools used to create, build, test, and
run a program. This image provides several toolchains. Work on projects in the
designated mounts so files persist on the host. Temporary exercises and
documentation tests belong in `/tmp` or `/home/adedev/smoke-tests`.

## Auswahl / Choose a Toolchain

**DE:** Die sechs verbindlichen speichersicheren Sprachpfade (MSL) dieses
Images sind .NET/C#, Java, Go, Rust, Python und Swift. PowerShell 7 ist die
zweite Skriptbasis neben Python. Node.js/npm ist vor allem die unterstuetzende
Laufzeit fuer Agenten- und Projektwerkzeuge; es ist in diesem Image kein
siebter verbindlicher MSL-Lernpfad.

**EN:** The six required memory-safe language (MSL) paths in this image are
.NET/C#, Java, Go, Rust, Python, and Swift. PowerShell 7 is the second scripting
foundation alongside Python. Node.js/npm mainly supports agent and project
tooling; it is not a seventh required MSL learning path in this image.

| Sprache oder Laufzeit / Language or runtime | Projektpfad / Project path | Anleitung / Guide |
|---|---|---|
| C# und .NET / C# and .NET | `/rider-projects` | [.NET](dotnet.md) |
| Java und Maven / Java and Maven | `/java-projects` | [Java](java.md) |
| Go | `/go-projects` | [Go](go.md) |
| Rust | `/rust-projects` | [Rust](rust.md) |
| Python und `uv` / Python and `uv` | `/python-projects` | [Python](python.md) |
| PowerShell 7 | `/powershell-projects` | [PowerShell](powershell.md) |
| Swift und SwiftPM / Swift and SwiftPM | `/swift-projects` | [Swift](swift.md) |
| Node.js und npm / Node.js and npm | `/workspace` oder ein projektspezifischer Mount / or a project-specific mount | [Node.js](nodejs.md) |

**DE:** Die drei Secure-Trader-Lernprojekte besitzen eigene Mounts. Nutze
`/secure-case-tracker-projects`, `/secure-service-harvester-projects` oder
`/secure-order-desk-projects`, wenn die jeweilige Lernreihe diesen Pfad
vorgibt. Die Sprache ändert den vorgegebenen Projektpfad nicht.

**EN:** The three Secure Trader training projects have dedicated mounts. Use
`/secure-case-tracker-projects`, `/secure-service-harvester-projects`, or
`/secure-order-desk-projects` when the corresponding learning series requires
that path. The language does not override the prescribed project path.

## Gemeinsamer Arbeitsablauf / Common Workflow

1. **DE:** Wechsle in den richtigen Mount und prüfe mit `pwd`, wo du bist.
   **EN:** Change to the correct mount and use `pwd` to verify your location.
2. **DE:** Prüfe vorhandene Projektdateien und lies zuerst `README.md` sowie
   `AGENTS.md`. **EN:** Inspect existing project files and read `README.md` and
   `AGENTS.md` first.
3. **DE:** Nutze projektlokale Abhängigkeiten und Lock-Dateien. **EN:** Use
   project-local dependencies and lock files.
4. **DE:** Führe Formatierung, statische Prüfung und Tests vor einem Commit
   aus. **EN:** Run formatting, static checks, and tests before a commit.
5. **DE:** Prüfe `git diff` menschlich. Ein grüner Test ersetzt kein Review.
   **EN:** Review `git diff` yourself. A green test does not replace review.

## Image-weite Prüfung / Image-Wide Check

**DE:** Der vorhandene Smoke-Test legt nur temporäre Projekte an und entfernt
sie nach dem Lauf:

**EN:** The existing smoke test creates temporary projects only and removes
them after the run:

```bash
podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-toolchains.sh
```

**DE:** Er prüft die installierten Versionen und kleine Programme für .NET,
Java, Go, Rust, Python, PowerShell, Node.js und Swift. Er installiert keine
projektfremden Frameworks und führt keinen KI-Provideraufruf aus.

**EN:** It checks installed versions and small programs for .NET, Java, Go,
Rust, Python, PowerShell, Node.js, and Swift. It installs no project-specific
framework and makes no AI-provider call.

## Nächste Schritte / Next Steps

**DE:** Wähle die Anleitung deiner Sprache. Für KI-gestützte Arbeit lies
anschließend [Agenten und Spec Kit](../agenten-und-spec-kit.md).

**EN:** Choose the guide for your language. For AI-assisted work, continue
with [Agents and Spec Kit](../agenten-und-spec-kit.md).
## Dokumentation als PDF / Documentation as PDF

**DE:** Pandoc wandelt Markdown in Typst-Quelltext um. Typst setzt daraus das
PDF. Lychee prueft Links; Tinymist stellt den Typst-Sprachserver fuer Editoren
bereit. Alle vier CLIs sind im Image enthalten. Apple Silicon verwendet
`linux/arm64`; Intel-/AMD-Windows und dessen Ubuntu/WSL2 verwenden
`linux/amd64`. Podman waehlt die native Architektur ohne Rosetta-Voraussetzung.

**EN:** Pandoc converts Markdown to Typst source, and Typst creates the PDF.
Lychee checks links; Tinymist provides the Typst language server for editors.
All four CLIs are included in the image. Apple Silicon uses `linux/arm64`;
Intel/AMD Windows and its Ubuntu/WSL2 use `linux/amd64`. Podman selects the
native architecture without requiring Rosetta.

Im Container / Inside the container:

```bash
pandoc documentation.md --standalone --to=typst -o documentation.typ
typst compile documentation.typ documentation.pdf
```

Separater Funktionstest vom Host / Standalone functional test from the host:

```bash
podman compose exec ade bash /ade-dev-sandbox/scripts/smoke-test-documentation.sh
```

**DE:** Der Test prueft Versionen, lokale Links (auch einen erwarteten Fehler),
Markdown-zu-PDF-Konvertierung, Seitenzahl und extrahierten Text. Er verwendet
temporaere Dateien und keine externen Downloads. Der vollstaendige
Toolchain-Smoke-Test fuehrt ihn ebenfalls aus. Das Ergebnis ist kein Nachweis
der PDF-Barrierefreiheit. Tinymist ist ein CLI-Sprachserver; eine Editor-
Erweiterung wird dadurch nicht automatisch installiert.

**EN:** The test checks versions, local links (including an expected failure),
Markdown-to-PDF conversion, page count, and extracted text. It uses temporary
files and no external downloads. The full toolchain smoke test also runs it.
The result does not prove PDF accessibility. Tinymist is a CLI language
server; installing it does not automatically install an editor extension.
