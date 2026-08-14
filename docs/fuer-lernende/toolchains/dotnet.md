# .NET und C# / .NET and C#

## Einordnung / Context

**DE:** Das Image basiert auf einem per SHA256-Digest festgelegten Microsoft
.NET-SDK-Image. Der kanonische Projektpfad ist `/rider-projects`. Das
eingebundene `ContainerBuild.props` leitet `bin`, `obj` und AppHost-Ausgaben
nach `/dotnet-build` um, damit diese Artefakte nicht auf einem Windows- oder
Host-Bind-Mount landen.

**EN:** The image is based on a Microsoft .NET SDK image pinned by SHA256
digest. The canonical project path is `/rider-projects`. The mounted
`ContainerBuild.props` redirects `bin`, `obj`, and AppHost output to
`/dotnet-build` so these artifacts do not land on a Windows or host bind mount.

## Konsole erstellen und prüfen / Create and Check a Console App

```bash
cd /rider-projects
dotnet new console --framework net10.0 -n HelloSandbox
cd HelloSandbox
dotnet restore
dotnet build
dotnet run
```

**DE:** Verwende bei einem vorhandenen Repository dessen Solution, Projektdatei
und dokumentierte Testbefehle. Für ein Testprojekt gilt zum Beispiel:

**EN:** For an existing repository, use its solution, project file, and
documented test commands. For example, a test project can be checked with:

```bash
dotnet test
dotnet list package --vulnerable --include-transitive
```

## ASP.NET vom Host erreichen / Reach ASP.NET from the Host

**DE:** Compose veröffentlicht ausschließlich die Hostadresse `127.0.0.1` und
die Ports `5100` bis `5199`. Die Anwendung muss im Container an `0.0.0.0`
binden. Dieses Beispiel verwendet Port `5100`:

**EN:** Compose publishes only host address `127.0.0.1` and ports `5100`
through `5199`. The application must bind to `0.0.0.0` inside the container.
This example uses port `5100`:

```bash
cd /rider-projects
dotnet new web -n SandboxWeb --framework net10.0
cd SandboxWeb
ASPNETCORE_URLS=http://0.0.0.0:5100 dotnet run --no-launch-profile
```

In einem zweiten Host-Terminal / In a second host terminal:

```bash
curl --fail http://127.0.0.1:5100/
```

**DE:** Beende die Anwendung anschließend mit `Ctrl+C`. Ein Testserver bleibt
nicht unbeaufsichtigt im Hintergrund aktiv.

**EN:** Stop the application with `Ctrl+C` afterwards. Do not leave a test
server running unattended in the background.

## Grenzen / Limits

- **DE:** Der Workload-Resolver ist deaktiviert. MAUI, WebAssembly oder andere
  SDK-Workloads müssen bewusst im Image ergänzt und neu validiert werden.
  **EN:** The workload resolver is disabled. MAUI, WebAssembly, or other SDK
  workloads must be added to the image deliberately and revalidated.
- **DE:** Der `dotnet`-Wrapper filtert nur eine bekannte Workload-Prüfzeile.
  Andere Warnungen und Fehler bleiben sichtbar. **EN:** The `dotnet` wrapper
  filters only one known workload-verification line. Other warnings and errors
  remain visible.
- **DE:** Rider oder Visual Studio läuft auf dem Host; Build und Agentenlauf
  finden im Container statt. **EN:** Rider or Visual Studio runs on the host;
  build and agent execution happen inside the container.

## Abschluss / Completion

```bash
dotnet --info
git status --short
```

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
