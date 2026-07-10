# Container-Grundlagen / Container Basics

**Stand / Date:** 2026-07-10
**Ausrichtung / Orientation:** DE-first, EN-second, CEFR B2, WCAG 2.2 AA

**DE:** Dieses Dokument erklärt die Grundbegriffe der Containerisierung für den
Einstieg — ganz ohne Vorkenntnisse. Wenn du noch nie mit Containern gearbeitet
hast, lies dieses Dokument zuerst. Danach verstehst du, warum eine Sandbox
sinnvoll ist ([warum-sandbox.md](warum-sandbox.md)) und kannst die Umgebung
installieren ([installation.md](installation.md)).

**EN:** This document explains the basics of containerization for getting
started — with no prior knowledge required. If you have never worked with
containers, read this first. Afterwards you understand why a sandbox is useful
([warum-sandbox.md](warum-sandbox.md)) and can install the environment
([installation.md](installation.md)).

---

## Was ist ein Container? / What Is a Container?

**DE:** Stell dir einen Umzugscontainer vor: eine standardisierte Kiste, die
überall gleich aussieht und die man auf jedes Schiff, jeden Zug und jeden LKW
laden kann. Ein Software-Container ist dasselbe Prinzip für Programme. Er packt
ein Programm **zusammen mit allen Werkzeugen und Bibliotheken**, die es zum
Laufen braucht, in eine abgeschlossene Kiste. Diese Kiste läuft auf jedem
Computer gleich — egal ob macOS, Windows oder Linux.

**EN:** Picture a shipping container: a standardized box that looks the same
everywhere and can be loaded onto any ship, train, or truck. A software
container follows the same principle for programs. It packs a program
**together with all the tools and libraries** it needs to run into one enclosed
box. This box runs the same on every computer — whether macOS, Windows, or
Linux.

**DE:** Der große Vorteil: Auf deinem Rechner muss nicht C#, Go, Java, Python,
Rust und Swift einzeln installiert und richtig eingestellt sein. All das steckt
schon fertig im Container dieser Sandbox.

**EN:** The big advantage: you do not need to install and correctly configure
C#, Go, Java, Python, Rust, and Swift one by one on your machine. All of that is
already prepared inside this sandbox container.

---

## Die wichtigsten Begriffe / The Most Important Terms

**DE:** Diese Begriffe begegnen dir immer wieder. Jede Erklärung ist bewusst
kurz gehalten. Eine ausführlichere Liste steht im [GLOSSAR.md](GLOSSAR.md).

**EN:** You will meet these terms again and again. Each explanation is kept
deliberately short. A fuller list is in the [GLOSSAR.md](GLOSSAR.md).

| Begriff / Term | Erklärung / Explanation |
|---|---|
| **Image** | Die Bauvorlage für einen Container — wie ein Kuchenrezept. Aus einem Image entstehen beliebig viele gleiche Container. / The build template for a container — like a cake recipe. From one image you can create any number of identical containers. |
| **Container** | Ein laufendes, abgeschlossenes Programm-Paket, gestartet aus einem Image. / A running, self-contained program package, started from an image. |
| **Volume** | Ein von Podman verwalteter Speicherbereich, der Daten behält, auch wenn der Container neu startet. / A storage area managed by Podman that keeps data even when the container restarts. |
| **Bind-Mount** | Ein Ordner **von deinem Rechner**, der in den Container eingehängt wird, damit beide auf dieselben Dateien zugreifen. / A folder **from your machine** mounted into the container so both access the same files. |
| **Registry** | Ein Online-Lager für Images, aus dem sie heruntergeladen werden (hier: `mcr.microsoft.com` für das .NET-Basis-Image). / An online store for images from which they are downloaded (here: `mcr.microsoft.com` for the .NET base image). |
| **Podman-Machine** | Eine kleine, versteckte Linux-VM, die Podman auf macOS und Windows braucht, weil Container Linux voraussetzen. / A small, hidden Linux VM that Podman needs on macOS and Windows because containers require Linux. |
| **Host** | Dein eigener Rechner (Laptop/PC), auf dem der Container läuft. / Your own machine (laptop/PC) on which the container runs. |
| **Egress** | Ausgehender Netzwerkverkehr aus dem Container ins Internet. / Outbound network traffic from the container to the internet. |

---

## Container oder virtuelle Maschine? / Container or Virtual Machine?

**DE:** Eine **virtuelle Maschine (VM)** ist ein kompletter, simulierter
Computer mit eigenem Betriebssystem — schwer und langsam beim Start. Ein
**Container** teilt sich den Kern (Kernel) mit dem Host und startet daher in
Sekunden. Für Lernen und Entwicklung ist der Container schlanker und schneller.

**EN:** A **virtual machine (VM)** is a complete, simulated computer with its
own operating system — heavy and slow to start. A **container** shares the
kernel with the host and therefore starts in seconds. For learning and
development, the container is leaner and faster.

**DE:** Kleine Ausnahme: Auf macOS und Windows läuft im Hintergrund trotzdem
eine schlanke Linux-VM (die **Podman-Machine**), weil Container Linux brauchen.
Auf Linux entfällt dieser Schritt.

**EN:** Small exception: on macOS and Windows a lean Linux VM runs in the
background anyway (the **Podman machine**), because containers need Linux. On
Linux this step is not needed.

---

## Warum Podman und nicht Docker? / Why Podman and Not Docker?

**DE:** Docker ist ein bekanntes Container-Werkzeug, aber diese freigegebene
Lernumgebung nutzt verbindlich **Podman**. Podman kann Container ohne einen
privilegierten Hintergrunddienst und ohne Root starten („rootless"). Die
Anleitungen, Tests und Audit-Wrapper werden nur fuer Podman gepflegt.

**EN:** Docker is a well-known container tool, but this approved learning
environment uses **Podman** as its binding runtime. Podman can start containers
without a privileged background service and without root ("rootless"). The
guides, tests, and audit wrappers are maintained for Podman only.

---

## So sieht diese Sandbox aus / What This Sandbox Looks Like

**DE:** Das folgende Diagramm zeigt die Schichten: dein Rechner (Host), die
Podman-Machine (nur auf macOS/Windows) und der Container mit seinen
eingehängten Ordnern. Nur die gezeigten Ordner sind aus dem Container
erreichbar — alles andere auf deinem Rechner bleibt unsichtbar und geschützt.

**EN:** The diagram below shows the layers: your machine (host), the Podman
machine (only on macOS/Windows), and the container with its mounted folders.
Only the folders shown are reachable from the container — everything else on
your machine stays invisible and protected.

```text
+---------------------------------------------------------------+
|  HOST (dein Rechner / your machine: macOS, Windows, Linux)     |
|                                                               |
|   Ordner auf dem Host / folders on the host:                  |
|     ./workspace          ./secure-case-tracker-projects       |
|     ./java-projects      ./go-projects   ./rust-projects       |
|     ./python-projects     ./swift-projects   ./audit-logs      |
|                                                               |
|   +-------------------------------------------------------+   |
|   |  PODMAN-MACHINE (nur macOS/Windows / only macOS/Win)  |   |
|   |  kleine Linux-VM / small Linux VM                     |   |
|   |                                                       |   |
|   |   +-----------------------------------------------+   |   |
|   |   |  CONTAINER  "ade"  (Benutzer / user: adedev)  |   |   |
|   |   |  Ubuntu + .NET, Go, Java, Python, Rust, Swift |   |   |
|   |   |                                               |   |   |
|   |   |   Eingehängt / mounted:                       |   |   |
|   |   |     /workspace        /go-projects            |   |   |
|   |   |     /rider-projects   /rust-projects          |   |   |
|   |   |     /java-projects    /python-projects        |   |   |
|   |   |     /swift-projects   /audit                  |   |   |
|   |   |                                               |   |   |
|   |   |   Härtung / hardening:                        |   |   |
|   |   |     kein Root / no root   cap_drop: ALL       |   |   |
|   |   |     no-new-privileges                         |   |   |
|   |   +-----------------------------------------------+   |   |
|   +-------------------------------------------------------+   |
|                                                               |
|   Ports: 127.0.0.1:5100-5199  (nur Web-App-Tests / web only)  |
+---------------------------------------------------------------+
        |
        v  Egress (ausgehend / outbound): Paketregister, GitHub, MCR ...
      Internet
```

**DE:** Die genauen Ordner, Schreibrechte und Sicherheitsmaßnahmen stehen im
[sandbox-profil.md](sandbox-profil.md). Die Faktenquelle ist `compose.yml`.

**EN:** The exact folders, write permissions, and security measures are in the
[sandbox-profil.md](sandbox-profil.md). The source of truth is `compose.yml`.

---

## Nächster Schritt / Next Step

**DE:** Jetzt weißt du, *was* ein Container ist. Als Nächstes lernst du, *warum*
diese Umgebung eine abgeschottete Sandbox ist und warum das für KI-gestützte
Arbeit Pflicht ist: [warum-sandbox.md](warum-sandbox.md).

**EN:** Now you know *what* a container is. Next you learn *why* this
environment is a walled-off sandbox and why that is mandatory for AI-assisted
work: [warum-sandbox.md](warum-sandbox.md).
