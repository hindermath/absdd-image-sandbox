# Human-only-Uebergaben / Human-Only Handoffs

## Status und Leseregel / Status and Reading Rule

**DE:** Diese Uebergabe enthaelt exakt die 49 Human-only-Gaps der akzeptierten
Baseline. Fakten und Vorlagen sind Vorbereitung, keine Freigabe. Ohne datierten
Rollenbeleg bleiben Status `Open`, Umsetzung `Not Assessed` und Restrisiko
`Unassessed`. `Repository Maintainer` pflegt repositorylokale Fakten nach;
`Security Review` prueft den spaeteren Nachweis.

**EN:** This handoff contains exactly the 49 human-only gaps from the accepted
baseline. Facts and templates are preparation, not approval. Without dated
role evidence, status remains `Open`, implementation `Not Assessed`, and
residual risk `Unassessed`. Repository Maintainer maintains repository-local
facts and Security Review reviews later evidence.

## Privacy/Legal Review

Exakte IDs (30): `GAP-011`, `GAP-012`, `GAP-070`, `GAP-075` bis `GAP-086`,
`GAP-105`, `GAP-106`, `GAP-115` und `GAP-134` bis `GAP-145`. / Exact IDs (30):
the listed gap IDs and inclusive ranges.

- Fakten / Facts: Die Baseline ordnet diese Punkte Standards-/Rechtsstatus,
  Offenlegungsprozess, CRA, Provider-/Trainingsdatenfragen und DPIA zu. Das
  Repository ist eine lokale Lern- und Entwicklungs-Sandbox ohne Registry-,
  Cloud- oder Marktbereitstellungsauftrag. / The baseline maps these items to
  standards/legal status, disclosure, CRA, provider/training-data questions,
  and DPIA. The repository is a local learning/development sandbox with no
  registry, cloud, or market-placement mandate.
- Fehlende Entscheidung / Missing decision: datierte Anwendbarkeits-, Rechts-,
  Datenschutz-, CRA-, DPIA- oder Offenlegungsentscheidung durch
  `Privacy/Legal Review`. / Dated decision by Privacy/Legal Review.
- Folgeaktion / Follow-up: aktuelle repositorylokale Datenfluss-, Produkt-,
  Distributions- und Lebenszyklusfakten pruefen und nur bei bestehender
  Autoritaet den Rollenbeleg anhaengen. / Review current local facts and attach
  role evidence only with authority.
- Faktenpakete / Fact packages: `work-packages/wp07-cra-facts.md` und
  `work-packages/wp11-dpia-facts.md`.
- Trigger: Rechtsaenderung, Marktbereitstellung, Kundenuebergabe, geaenderter
  Datenfluss, Provider-/Trainingsdatenscope oder neue Offenlegung. / Legal
  change, market placement, customer handover, changed data flow,
  provider/training-data scope, or new disclosure.
- Agentengrenze / Agent boundary: keine Rechts-, Datenschutz-, CRA-, DPIA-
  oder externe Registerentscheidung; keine externe Meldung. / No legal,
  privacy, CRA, DPIA, external-register, or external-notification action.

## Platform Owner/Admin

Exakte IDs (10): `GAP-034`, `GAP-035`, `GAP-120`, `GAP-121`, `GAP-124`,
`GAP-128` bis `GAP-131` und `GAP-155`. / Exact IDs (10): the listed gap IDs
and inclusive range.

- Fakten / Facts: Diese Punkte betreffen Schluesselverwaltung, Hosting-Regeln,
  zentrale Secret-/Audit-/Backup-/Netzwerkmechanismen und Branchschutz. Das
  Repository kann lokale Konfiguration und Anleitungen belegen, aber keine
  Plattformdurchsetzung. / These items concern key management, hosting rules,
  central secret/audit/backup/network controls, and branch protection. The
  repository can evidence local configuration but not platform enforcement.
- Fehlende Entscheidung / Missing decision: datierter Plattformnachweis mit
  Scope und verantwortlicher Instanz. / Dated platform evidence with scope and
  accountable owner.
- Folgeaktion / Follow-up: Platform Owner/Admin prueft die vorbereiteten
  lokalen Fakten, fuehrt erforderliche externe Schritte selbst aus und liefert
  einen nicht sensiblen Statusbeleg. / Platform Owner/Admin reviews facts,
  performs any authorized external action, and supplies non-sensitive status
  evidence.
- Trigger: Schluessel-/Secret-Lebenszyklus, Hosting- oder Branch-Regelaenderung,
  zentraler Audit-/Backup-/Endpoint-/Netzwerkentscheid oder neue Plattform. /
  Key/secret lifecycle, hosting or branch-rule change, central audit/backup/
  endpoint/network decision, or new platform.
- Agentengrenze / Agent boundary: keine Schluesselaktion, Branch-Regel,
  Plattformkonfiguration, zentrale Audit-, Endpoint-, Backup- oder
  Netzwerkfreigabe. / No key, branch-rule, platform, central audit, endpoint,
  backup, or network action.

## CISO/ISB/KIB

Exakte IDs (8): `GAP-100` bis `GAP-102`, `GAP-109`, `GAP-110`, `GAP-146`,
`GAP-150` und `GAP-152`. / Exact IDs (8): the listed IDs and inclusive range.

- Fakten / Facts: Repositorylokale Inventare und Konfigurationen beschreiben
  Agenten, Versionspins, Telemetrie-, Zustands- und Sandboxgrenzen. Sie
  enthalten keinen vorkonfigurierten Provider und keine Modellfreigabe. /
  Repository-local inventory and configuration describe agents, pins,
  telemetry, state, and sandbox boundaries. They contain no preconfigured
  provider or model approval.
- Fehlende Entscheidung / Missing decision: datierte Werkzeug-, Modell-,
  Telemetrie-, Sandbox- oder Review-Freigabe durch `CISO/ISB/KIB`. / Dated
  approval by CISO/ISB/KIB.
- Folgeaktion / Follow-up: technische Evidenz und offene Provider-/Modellfelder
  pruefen; Entscheidung getrennt und ohne Secrets dokumentieren. / Review
  technical evidence and open provider/model fields; record the decision
  separately and without secrets.
- Trigger: neue Agenten-/Modellversion, Provider-, Telemetrie-, Mount-,
  Netzwerk- oder Sandboxgrenze sowie Ablauf eines Rollenbelegs. / New agent or
  model version, provider, telemetry, mount, network, sandbox boundary, or
  expired role evidence.
- Agentengrenze / Agent boundary: keine Werkzeug-, Modell-, Telemetrie-,
  Sandbox- oder Review-Freigabe und keine Provideraktion. / No tool, model,
  telemetry, sandbox, or review approval and no provider action.

## Project Owner

Exakte ID (1): `GAP-113`. / Exact ID (1): `GAP-113`.

- Fakten / Facts: Der Punkt betrifft eine Ausnahme und ihr Restrisiko. Der
  Agent darf die technische Ausgangslage und moegliche Folgeaktionen
  beschreiben. / The item concerns an exception and residual risk; the agent
  may document technical facts and possible follow-up.
- Fehlende Entscheidung / Missing decision: datierte Ausnahme- und
  Risikoentscheidung durch `Project Owner`. / Dated exception and risk
  decision by Project Owner.
- Folgeaktion / Follow-up: Project Owner prueft Scope, technische Evidenz,
  Alternativen und Ablaufdatum. / Project Owner reviews scope, evidence,
  alternatives, and expiry.
- Trigger: neue Ausnahme, geaenderter Scope, Kontrollausfall oder Ablaufdatum.
  / New exception, scope change, control failure, or expiry.
- Agentengrenze / Agent boundary: keine stellvertretende Risikoakzeptanz. /
  No proxy risk acceptance.

## Vollstaendigkeitspruefung / Completeness Check

Die vier disjunkten Gruppen ergeben `30 + 10 + 8 + 1 = 49`. Jede spaetere
Rollenentscheidung wird erst nach erneuter Scope-, Hash-, Evidence- und
Authority-Pruefung uebernommen. Der moderierte SC-009-Erstnutzungstest durch
`Learning/A11Y Review` ist ein separates Feature-Gate und aendert diese
Partition nicht. / The four disjoint groups total 49. Any later role decision
requires renewed scope, hash, evidence, and authority checks. The SC-009 human
learner test is a separate feature gate and does not change this partition.

## Separates Learner-Gate / Separate Learner Gate

**DE:** `GATE-LEARNER-01` bleibt `Blocked`. Owner ist `Learning/A11Y Review`.
Es liegt keine datierte, moderierte Beobachtung fuer alle vier Berufe ohne
Spec-Kit-Vorerfahrung vor; deshalb wurde
`learner-first-use-results.json` nicht erzeugt. Der Repository Owner hat am
04.09.2026 bestaetigt, dass im vorhandenen Ein-Personen-Setup weder reale
Teilnehmende aus allen vier Ausbildungsberufen noch die geforderten
Beobachtungen mit assistiven Technologien bereitgestellt werden koennen. Dies
ist eine begruendete offene Abweichung, keine positive Testevidenz und keine
Umklassifizierung zu `N/A`. Folgeaktion: Das Gate bleibt `Blocked`; erst wenn
geeignete Teilnehmende und assistive Technologien tatsaechlich verfuegbar
werden, darf `Learning/A11Y Review` den 30-Minuten-Test ausfuehren und nur
aggregierte, nicht-sensible Ergebnisse mit mindestens 90 Prozent Erfolg
liefern.

**EN:** GATE-LEARNER-01 remains Blocked and is owned by Learning/A11Y Review.
No dated moderated observation exists for all four occupations without prior
Spec Kit experience, so learner-first-use-results.json was not created. On
2026-09-04, the Repository Owner confirmed that the available one-person setup
cannot provide real participants from all four occupations or the required
assistive-technology observations. This is a justified open deviation, not
positive test evidence and not a reclassification to N/A. The gate remains
Blocked. Learning/A11Y Review may run the 30-minute test and provide only
aggregated non-sensitive results with at least 90 percent success if suitable
participants and assistive technologies become available later.

## Projektspezifische Review-Abweichung / Project-specific Review Deviation

**DE:** Der Repository Owner ist zugleich alleiniger Ersteller, Ausfuehrender
und menschlicher Pruefer dieses Feature-Patches. Die ausdrueckliche
Patch-Pruefung vor Commit und Push bleibt moeglich und wurde fuer den bisherigen
Evidenzstand am 04.09.2026 bestaetigt. Eine zweite unabhaengige Person fuer das
Vier-Augen-Prinzip steht jedoch nicht zur Verfuegung. Diese Begrenzung bleibt
als offene, nicht personell unabhaengige Review-Abweichung dokumentiert. Sie ist
weder ein echtes Vier-Augen-Testat noch eine formale Risikoakzeptanz und darf
kein fehlgeschlagenes oder blockiertes technisches, Security-, Plattform- oder
Learner-Gate uebergehen.

**EN:** The Repository Owner is also the sole creator, operator, and human
reviewer of this feature patch. Explicit human patch review before commit and
push remains possible and was confirmed for the previous evidence state on
2026-09-04. No second independent person is available for a four-eyes review.
This limitation remains documented as an open, non-person-independent review
deviation. It is neither a genuine four-eyes attestation nor formal risk
acceptance, and it cannot override a failed or blocked technical, security,
platform, or learner gate.

Exakter Trigger / Exact trigger: Any startup path, verification-status
presentation, Human-only handoff, audience policy, test protocol, participant
coverage, or learner-facing documentation change.
