# Checkliste zur autonomen Laufbereitschaft / Autonomous Run Readiness Checklist

## Zweck / Purpose

**DE:** Diese Checkliste trennt bereits belegte Planungsbereitschaft von noch
offener Implementierungs-, Delivery- und Human-only-Evidenz. Ein offenes
Kaestchen ist ein sichtbarer Stop- oder Folgeschritt, kein stiller Pass. /
**EN:** This checklist separates proven planning readiness from implementation,
delivery, and human-only evidence that is still open. An open box is a visible
stop or follow-up step, never a silent pass.

## Authority und Scope / Authority and Scope

- [x] Die aktuelle Intake-Review ist eindeutig und `Ready`. / The current
      intake review is unambiguous and `Ready`.
- [x] Der Delivery-Modus `MergeAndSync` stammt aus dem aktuellen Auftrag. / The
      `MergeAndSync` delivery mode comes from the current instruction.
- [x] Der Admin-Bypass ist auf den neu erzeugten PR und nichttechnische
      Repository-Policy begrenzt. / The admin bypass is limited to the newly
      created pull request and non-technical repository policy.
- [x] Der Scope bleibt ausschliesslich die GSDB-Bestandspruefung. / Scope
      remains limited to the GSDB baseline assessment.
- [x] Human-only-Entscheidungen bleiben offen. / Human-only decisions remain
      open.
- [x] Der naechste Intake der Serie wird nicht gestartet. / The next intake in
      the series is not started.
- [x] Die Lernenden- und A11Y-Basis ist Deutsch zuerst, Englisch danach, CEFR
      B2, textorientiert und ohne vorausgesetzte Spec-Kit-Erfahrung. / The
      learner and accessibility baseline is German first, English second,
      CEFR B2, text-first, and assumes no Spec Kit experience.

## Artefakt-Konvergenz / Artifact Convergence

- [x] Clarify hat keine materielle Planungsunklarheit. / Clarify has no material
      planning ambiguity.
- [x] Requirements-Checkliste und Plan-Review-Konvergenztabelle sind bestanden.
      / The requirements checklist and plan-review convergence table pass.
- [x] Tasks sind abhaengigkeitsgeordnet und nennen exakte Evidenzpfade. / Tasks
      are dependency ordered and name exact evidence paths.
- [x] Analyze hat keine Critical-/High-Findings; Medium ist behoben oder mit
      Owner und Trigger vollstaendig disponiert. / Analyze has no Critical or
      High findings; each Medium is resolved or fully disposed with owner and
      trigger.
- [x] Alle Implementierungsaufgaben T001 bis T062 sind abgeschlossen oder
      bedingt belegt; T063 bis T068 bleiben ausserhalb dieses Auftrags. /
      All implementation tasks are complete or conditionally evidenced.

## Nachweis und Delivery / Proof and Delivery

- [x] Evidenz existiert vor dem ersten Implementierungs-Edit. / Evidence exists
      before the first implementation edit.
- [x] Gate-Anforderungen sind vor der Implementierung deklariert und reviewt. /
      Gate requirements are declared and reviewed before implementation.
- [ ] Der explizite Delivery-Set-Validator besteht; sein dokumentierter
      `git write-tree`-Metadaten-Write ist in der aktuellen Sandbox erlaubt. /
      The explicit delivery-set validator passes, including its documented Git
      metadata write.
- [x] Ein repraesentativer vertikaler Slice besitzt Rot-/Gruen-Nachweis. / A
      representative vertical slice has red/green proof.
- [x] Alle lokal anwendbaren getriggerten Validatoren bestehen; nicht
      verfuegbare Runtime-/Netzwerkbeobachtungen sind sichtbar `Open`. / All
      locally applicable triggered validators pass; unavailable runtime or
      network observations remain visibly Open.
- [ ] Exakter Review-Head und Schema-2.0-`PreMerge`-Evidenz sind validiert. /
      Exact reviewed head and schema-2.0 PreMerge evidence are validated.
- [ ] Required Checks und Reviews sind aktuell und ohne offene Threads. /
      Required checks and reviews are current with no open threads.
- [ ] Merge, PostMerge-Evidenz und lokaler Default-Branch-Sync sind belegt. /
      Merge, PostMerge evidence, and local default-branch sync are proven.
- [ ] Alle Schema-1.1-Closeout-Felder sind terminal. / All schema-1.1 closeout
      fields are terminal.
