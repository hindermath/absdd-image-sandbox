# MSL-Anwendbarkeit / Memory-Safe Language Applicability

**DE:** Das Repository ist ein Container-, Automations- und Lernprojekt ohne
einzelne Anwendungssprache. **MSL** bedeutet speichersichere Sprache: typische
Speicherzugriffe werden durch Laufzeit oder Typsystem abgesichert. Fuer neue
wiederverwendbare Validatorlogik ist Python 3 die primaere MSL. Bash und
PowerShell 7 bleiben notwendige plattformspezifische Schnittstellen. Das Image
stellt .NET/C#, Java, Go, Rust, Python und Swift als sechs MSL-Familien bereit.

**EN:** This is a container, automation, and learning repository without one
application language. A memory-safe language protects typical memory access
through its runtime or type system. Python 3 is primary for reusable validator
logic; Bash and PowerShell 7 remain necessary platform interfaces. The image
provides .NET/C#, Java, Go, Rust, Python, and Swift as six MSL families.

Neue nicht speichersichere Logik ist nur mit dokumentierter Hardware- oder
Legacy-Begruendung, minimalem Scope und Security Review zulaessig. Aktuell gibt
es keine solche Ausnahme. Neubewertung bei neuer Sprache, Runtime oder nativer
Erweiterung. / New non-memory-safe logic requires a documented hardware or
legacy rationale, minimal scope, and Security Review. Re-evaluate on a new
language, runtime, or native extension.

Mapping: `GAP-001`–`GAP-003`, FR-005, FR-010, GR-005.
