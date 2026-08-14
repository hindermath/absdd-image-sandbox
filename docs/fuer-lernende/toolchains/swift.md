# Swift und SwiftPM / Swift and SwiftPM

## Einordnung / Context

**DE:** Swift-Projekte liegen standardmäßig unter `/swift-projects`. Das Image
enthält die native Swift-Toolchain für Ubuntu 24.04, Swift Package Manager
(SwiftPM) und SourceKit-LSP. Damit lassen sich plattformunabhängige Swift-
Pakete und Kommandozeilenprogramme bauen.

**EN:** Swift projects normally live under `/swift-projects`. The image
contains the native Swift toolchain for Ubuntu 24.04, Swift Package Manager
(SwiftPM), and SourceKit-LSP. It can build platform-independent Swift packages
and command-line programs.

## Projekt anlegen / Create a Project

```bash
cd /swift-projects
mkdir HelloSandbox
cd HelloSandbox
swift package init --name HelloSandbox --type executable
swift build
swift test
swift run HelloSandbox
```

**DE:** `swift test` ist auch dann zulässig, wenn das neue Paket noch keine
Tests enthält; füge für reale Projekte Tests unter `Tests/` hinzu. Prüfe vor
dem Commit mindestens:

**EN:** `swift test` is valid even when the new package has no tests yet; add
tests under `Tests/` for real projects. Before committing, check at least:

```bash
swift build
swift test
command -v sourcekit-lsp
git status --short
```

## Editor / Editor

**DE:** Für VS Code ist `swiftlang.swift-vscode` die vorgesehene Extension.
Öffne das Verzeichnis mit der `Package.swift` als Projektwurzel, damit
SourceKit-LSP das Paket erkennt.

**EN:** For VS Code, `swiftlang.swift-vscode` is the intended extension. Open
the directory containing `Package.swift` as the project root so SourceKit-LSP
can recognize the package.

## Grenzen / Limits

- **DE:** Das Linux-Image enthält weder Xcode noch iOS-, macOS- oder andere
  Apple-SDKs. Apple-Plattformanwendungen können hier nicht vollständig gebaut
  oder signiert werden. **EN:** The Linux image contains neither Xcode nor iOS,
  macOS, or other Apple SDKs. Apple-platform applications cannot be fully built
  or signed here.
- **DE:** Ein globales Swift-Schwachstellenwerkzeug wird nicht behauptet.
  Prüfe Paketquellen und `Package.resolved` im Projekt. **EN:** No global Swift
  vulnerability tool is claimed. Review package sources and `Package.resolved`
  in the project.
- **DE:** Binärartefakte unter `.build/` sind nicht die Quelle. **EN:** Binary
  artifacts under `.build/` are not source files.

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
