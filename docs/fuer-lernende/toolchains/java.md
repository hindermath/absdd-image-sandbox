# Java und Maven / Java and Maven

## Einordnung / Context

**DE:** Java-Projekte liegen standardmäßig unter `/java-projects`. Das Image
enthält ein JDK 21 und Maven. Eine projektspezifische Maven- oder Gradle-
Wrapperdatei hat Vorrang, wenn das Repository sie mitliefert.

**EN:** Java projects normally live under `/java-projects`. The image contains
JDK 21 and Maven. A project-specific Maven or Gradle wrapper takes precedence
when the repository provides one.

## Werkzeuge prüfen / Check the Tools

```bash
cd /java-projects
java --version
javac --version
mvn --version
```

## Kleines Programm / Small Program

**DE:** Lege in einem neuen Übungsordner eine Datei `Main.java` an:

**EN:** In a new exercise directory, create a file named `Main.java`:

```java
public final class Main {
  public static void main(String[] args) {
    System.out.println("Hallo aus der Sandbox");
  }
}
```

```bash
javac Main.java
java Main
```

## Maven-Projekt / Maven Project

**DE:** In einem vorhandenen Maven-Projekt sind `pom.xml` und gegebenenfalls
`mvnw` die verbindlichen Quellen. Prüfe zuerst die Projektanleitung:

**EN:** In an existing Maven project, `pom.xml` and, when present, `mvnw` are
the authoritative sources. Read the project guide first:

```bash
test -x ./mvnw && ./mvnw test || mvn test
test -x ./mvnw && ./mvnw verify || mvn verify
```

**DE:** `mvn dependency:analyze` hilft bei ungenutzten oder nicht deklarierten
Abhängigkeiten. Es ersetzt keine Schwachstellenprüfung und kann je nach Projekt
zusätzliche Plugin-Downloads benötigen.

**EN:** `mvn dependency:analyze` helps find unused or undeclared dependencies.
It does not replace vulnerability scanning and may download additional plugins
depending on the project.

## Grenzen / Limits

- **DE:** Gradle und Spring Boot CLI sind nicht global installiert. Nutze den
  Projekt-Wrapper oder dokumentiere eine bewusste Image-Erweiterung. **EN:**
  Gradle and the Spring Boot CLI are not globally installed. Use the project
  wrapper or document a deliberate image extension.
- **DE:** Frameworks und Bibliotheken gehören in `pom.xml` oder die
  projektspezifische Builddatei, nicht global ins Image. **EN:** Frameworks and
  libraries belong in `pom.xml` or the project build file, not globally in the
  image.
- **DE:** Lösche generierte Dateien nur innerhalb des eindeutig gewählten
  Projekts. **EN:** Delete generated files only inside the explicitly selected
  project.

Zurück zum [Toolchain-Index](README.md). / Return to the
[toolchain index](README.md).
