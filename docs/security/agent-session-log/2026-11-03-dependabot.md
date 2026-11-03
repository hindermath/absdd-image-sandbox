# Dependabot-Konfiguration / Dependabot Configuration

DE: Expliziter Ownerauftrag vom 2026-11-03: Dependabot fuer die benannten
Herzensprojekte konfigurieren und ueber gepruefte PRs regulär ausliefern.
GitHub Actions und externe pre-commit-Hooks erhalten Versions- und getrennte
Sicherheitsgruppen. Renovate behaelt Dockerfile und Toolchain-ARGs.
Kopierte Wartungsworkflows bleiben bei Level 0. Dokumentationsentscheidung:
UpdateRequired; die Betriebsanleitung verlinkt den zweisprachigen Wartungspfad.
YAML/Schema, Manifestabdeckung, Liefermenge, Dokumentation und Secret-Scan
werden vor Commit geprueft; genaue Hosted-Ergebnisse stehen am PR.
Keine Compliance-Plan-ID geschlossen. P0/P1/P2/P3-Arbeit wurde nicht gestartet,
weil dieser Auftrag die Dependabot-Einrichtung betrifft. Formale Freigaben,
Branch-Schutz und externe Register bleiben unveraendert. Naechste Sitzung:
Dependabot-Laeufe pruefen; neue Abhaengigkeits-PRs getrennt reviewen.

EN: Explicit owner instruction dated 2026-11-03 authorizes configuring
Dependabot and regular delivery through checked PRs. Actions and external
pre-commit hooks receive version and separate security groups. Renovate keeps
Dockerfile and toolchain ARG ownership; copied maintenance workflows stay
with level 0. Documentation Impact: UpdateRequired, with an operations-guide
link to the bilingual maintenance guide. YAML/schema, manifest coverage,
delivery scope, documentation and secret scanning precede commit; hosted
results are recorded on the PR. No compliance task is closed or started,
because this instruction concerns Dependabot setup. Formal approvals,
branch protection and external registers remain unchanged. Next session:
inspect Dependabot runs and review dependency proposals separately.
