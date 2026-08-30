# WP04 Bedrohungsmodellierung / Threat Modelling

## RED-Inspektion / RED inspection

Am 30.08.2026 waren weder ein projektspezifisches Bedrohungsmodell noch eine
Entscheidung zu den Container-Vertrauensgrenzen vorhanden. Damit fehlten die
Nachweise fuer `GAP-041` bis `GAP-050`. / On 2026-08-30 the repository had no
project threat model or container-boundary decision, so evidence for the ten
gaps was missing.

## Ergebnis / Result

`docs/security/threat-model.md` beschreibt Assets, CIA-Schutzziele
(Vertraulichkeit, Integritaet, Verfuegbarkeit), Datenfluesse, STRIDE,
Missbrauchsfaelle, CAPEC-Bezuege und Massnahmen. S-ADR 004 bindet die
Vertrauensgrenzen. Offene Egress-, Plattform- und Freigaberisiken bleiben
ausdruecklich unakzeptiert. / The threat model and S-ADR 004 now provide the
text-first evidence; open egress, platform, and approval risks remain
unaccepted.

Owner: Repository Maintainer. Reviewer: Security Review. Trigger: Mount-,
Netzwerk-, Tool-, State- oder Laufzeitgrenze aendert sich. Mapping:
FR-006–FR-009, FR-018, AR-002–AR-005, `GAP-041`–`GAP-050`.
