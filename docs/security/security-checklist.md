# Projektspezifische Sicherheitspruefliste / Project Security Checklist

Status ist textorientiert: `Pass` verlangt aktuelle Evidenz, `Open` benennt
fehlenden Nachweis, `N/A` besitzt Sachgrund und Trigger. / Status is text-first:
Pass requires current evidence, Open names missing proof, and N/A includes a
rationale and trigger.

| Bereich / Area | Aktueller Zustand / Current state | Evidenz oder Folgeaktion / Evidence or follow-up |
|---|---|---|
| NIST SSDF und CWE Top 25 | Applicable, FollowUp | Gap-Matrix, Sprachregeln und Work-Package-Reviews; erneut nach Scriptaenderung. |
| OWASP ASVS | N/A | Kein eigener Web/API/Auth-Dienst; erneut, wenn ein solcher Dienst in Scope kommt. |
| Rootless und geringste Rechte | Applicable | `Dockerfile`, `compose.yml`; Runtimebeleg folgt am finalen Image. |
| Mounts, State und Secrets | Applicable | Compose-/Agentenkonfiguration; finaler Runtime- und Secret-Scan folgt. |
| Lieferkette, SBOM und VEX | Applicable, FollowUp | Bewegliche Fallbacks werden in WP05 behoben; finale Kette folgt nach Build. |
| Threat Model und Architektur | Applicable | Projektbezogene Dokumente und S-ADRs; erneut bei Boundary-Aenderung. |
| STRIDE, CIA und CAPEC | Applicable | `docs/security/threat-model.md`, S-ADR 004; Restrisiko bleibt unakzeptiert. |
| Schwachstellenoffenlegung | Applicable, FollowUp | `SECURITY.md`, `security.txt`, CVD-Ablauf; erste moderierte Uebung fehlt. |
| Sichere Skriptlogik | Applicable, FollowUp | Sprachregeln und WP08-Review; Analyzer-Evidenz folgt im statischen Gate. |
| Human-only-Freigaben | Open | Exakt 49 Uebergaben; keine Agentenfreigabe oder Risikoakzeptanz. |

**EN summary:** NIST SSDF, CWE causes, least privilege, boundaries, supply
chain, and threat modelling are applicable. ASVS is not triggered because the
repository has no first-party web/API/auth service. Human-only decisions stay
open. Owner is Repository Maintainer; reviewer is Security Review.

Mapping: `GAP-001`–`GAP-012`, `GAP-041`–`GAP-074`,
`GAP-087`–`GAP-099`, FR-001–FR-021.
