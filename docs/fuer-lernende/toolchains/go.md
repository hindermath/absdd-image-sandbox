# Go

## Einordnung / Context

**DE:** Go-Projekte liegen standardmäßig unter `/go-projects`. Neben dem
Compiler enthält das Image `gopls`, `staticcheck`, `govulncheck` und `dlv`.
Abhängigkeiten bleiben im jeweiligen `go.mod` und `go.sum` nachvollziehbar.

**EN:** Go projects normally live under `/go-projects`. In addition to the
compiler, the image contains `gopls`, `staticcheck`, `govulncheck`, and `dlv`.
Dependencies remain traceable in each project's `go.mod` and `go.sum`.

## Projekt anlegen / Create a Project

```bash
cd /go-projects
mkdir hello-sandbox
cd hello-sandbox
go mod init example.invalid/hello-sandbox
```

Datei `main.go` / File `main.go`:

```go
package main

import "fmt"

func main() {
	fmt.Println("Hallo aus der Sandbox")
}
```

```bash
gofmt -w main.go
go run .
go test ./...
go vet ./...
staticcheck ./...
govulncheck ./...
```

## Abhängigkeiten / Dependencies

**DE:** Füge Webframeworks wie Gin, Fiber oder Chi nur dem konkreten Projekt
hinzu. Prüfe danach `go.mod`, `go.sum` und den vollständigen Diff. Nutze
`go mod tidy` bewusst, weil der Befehl beide Dateien ändern kann.

**EN:** Add web frameworks such as Gin, Fiber, or Chi only to the specific
project. Then review `go.mod`, `go.sum`, and the full diff. Use `go mod tidy`
deliberately because it can change both files.

## Debugging und Grenzen / Debugging and Limits

- `gopls version` prüft den Language Server. / checks the language server.
- `dlv version` prüft den Debugger. / checks the debugger.
- **DE:** Netzwerkzugriff kann beim ersten Download von Modulen erforderlich
  sein. Verwende nur freigegebene Quellen. **EN:** Network access may be needed
  for the first module download. Use approved sources only.
- **DE:** Ein grüner `go test`-Lauf ersetzt weder `staticcheck` noch
  `govulncheck`. **EN:** A green `go test` run replaces neither `staticcheck`
  nor `govulncheck`.

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
