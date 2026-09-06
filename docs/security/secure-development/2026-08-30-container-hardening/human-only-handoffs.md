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

**DE:** Der Repository Owner hat am 06.09.2026 ausdruecklich entschieden, dass
dieses Feature zunaechst als allein durchgefuehrte Machbarkeitsstudie endet.
Reale Teilnehmende und eine unabhaengige Learning-/A11Y-Review werden in diesem
Studienlauf nicht verfuegbar sein. Deshalb bleibt
`learner-first-use-results.json` absichtlich abwesend und
`feasibility-study-decision.json` dokumentiert stattdessen `NotPerformed`.
`GATE-LEARNER-01` ist nur fuer den bis 31.12.2026 befristeten,
source-repository-only Studienabschluss `N/A`. Dies ist keine positive
Lernendenevidenz und keine Behauptung einer unabhaengigen Pruefung.

Vor einem Lernenden-Rollout, einer Verteilung eines vorgebauten Images,
produktiver Nutzung oder bei Ablauf wird das Gate wieder `Applicable`. Dann
darf ausschliesslich `Learning/A11Y Review` den realen 30-Minuten-Test
ausfuehren und aggregierte, nicht-sensible Ergebnisse mit mindestens 90
Prozent Erfolg liefern.

**EN:** On 2026-09-06, the Repository Owner explicitly limited this closeout
to a single-person feasibility study. Real participants and independent
Learning/A11Y review will not be available in this study run. The learner
result therefore remains absent and the feasibility decision records
NotPerformed. GATE-LEARNER-01 is N/A only for the source-repository-only study
through 2026-12-31. It becomes Applicable again before learner rollout,
prebuilt image distribution, production use, or at expiry.

## Projektspezifische Review-Abweichung / Project-specific Review Deviation

**DE:** Der Repository Owner ist zugleich alleiniger Ersteller, Ausfuehrender
und menschlicher Pruefer dieses Feature-Patches. Am 06.09.2026 wurde dieser
Umstand als bindende Eigenschaft der Machbarkeitsstudie bestaetigt und die
autonome Fortsetzung des bestehenden Runs ausdruecklich angeordnet. Eine zweite
unabhaengige Person fuer das Vier-Augen-Prinzip steht nicht zur Verfuegung.
Diese Begrenzung bleibt sichtbar und ist weder ein echtes Vier-Augen-Testat
noch eine produktive oder organisationsweite Freigabe.

**EN:** The Repository Owner is also the sole creator, operator, and human
reviewer of this feature patch. On 2026-09-06, this was confirmed as a binding
property of the feasibility study and autonomous continuation of the existing
run was explicitly ordered. No second independent person is available. The
limitation remains visible and is neither a genuine four-eyes attestation nor
a production or organization-wide approval.

Exakter Trigger / Exact trigger: Before learner rollout, prebuilt image
distribution, production use, or at or after 2026-12-31.
