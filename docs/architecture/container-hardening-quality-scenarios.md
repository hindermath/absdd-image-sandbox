# Qualitaetsszenarien / Quality Scenarios

Ein Szenario nennt Ausloeser, erwartete Reaktion und messbaren Nachweis. / A
scenario states trigger, expected response, and measurable evidence.

1. **Unzulaessiger Schreibzugriff / Denied write:** Ein Schreibversuch
   ausserhalb deklarierter Roots wird abgelehnt; Exit ist ungleich null und
   keine Zieldatei entsteht. Runtime-Gate T053.
2. **Reproduzierbarer Build / Reproducible build:** Gleiche Revision und Pins
   verwenden dieselben deklarierten Quellen; genau ein finaler Build endet mit
   Exit 0 und bindet Image-ID. Build-Gate T053.
3. **Toolchain-Smoke:** Sechs MSL-Familien, zwei Skriptgrundlagen, vier
   Pflichtagenten und zwei Zusatzoberflaechen liefern Identitaet plus minimale
   Funktion ohne Provideraufruf. Smoke-Gate T053.
4. **Egress-Entscheidung:** Jeder benoetigte Paket-/Agentenfluss ist textlich
   begruendet; freie Erreichbarkeit bleibt Open bis Platform Owner/Admin.
5. **Build-Fehler:** Ein fehlender Pin oder Download stoppt sicher; es gibt
   keinen Wechsel auf `latest`. Repair invalidates only affected gates.

**EN summary:** The scenarios cover denied writes, reproducible build, complete
tool/agent smoke, reviewable egress, and fail-closed build recovery. They are
re-run when their subject changes.
