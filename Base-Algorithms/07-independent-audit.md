# Algorithm 7 — Independent multi-agent audit

## Aim

Provide a disciplined audit process for any future multi-agent prototype. Multiple models can share data, assumptions, or failure modes; consensus is not proof, independence, or legitimacy.

## Audit stages

1. **Mandate check:** Confirm a narrow, publicly authorized purpose, accountable human owner, affected-party participation, legal basis, and explicit prohibited uses. Otherwise return `NO-GO`.
2. **Data and privacy review:** Record provenance, consent/lawful basis, minimization, access controls, retention, deletion, security, and known gaps. Do not ingest sensitive personal data just because it is available.
3. **Role separation:** Define each agent's limited task, permissions, and conflicts. Keep recommendation, audit, and human decision roles distinct. No agent can grant authority to itself or another agent.
4. **Independent challenge:** Use genuinely independent reviewers, evidence sources, or methods where feasible. Ask reviewers to identify counterexamples, rights conflicts, correlated errors, proxy discrimination, and uncertainty. Do not treat agent voting as proof.
5. **Scenario testing:** Test missing/incorrect data, distribution shifts, manipulation, adversarial inputs, model disagreement, correlated failures, outage, unsafe tool use, and rollback. Use synthetic or de-identified data where suitable; do not test coercive actions on real people.
6. **Impact and rights review:** Evaluate disaggregated outcomes, worst cases, accessibility, privacy, freedom of expression, due process, consent, and potential concentration of power. Involve affected communities and independent human experts.
7. **Human authorization gate:** An accountable human institution reviews evidence, dissent, safeguards, and alternatives. A model cannot authorize launch or override a human stop decision.
8. **Limited pilot only if legitimate:** If approved, use a voluntary, bounded, monitored pilot that cannot affect essential needs or rights. Establish informed participation, a human fallback, independent monitoring, incident response, and a stop mechanism.
9. **Post-deployment review:** Publish appropriate aggregate findings, report incidents, handle complaints, correct records, reevaluate at a set interval, and sunset/rollback if safeguards or performance fail.

## Go/no-go logic

`NO-GO` if purpose or authority is unclear; privacy/security is inadequate; there is no appeal or human fallback; independent audit is missing; a rights-affecting decision is automated; the system can deny essentials, suppress dissent, or coerce; or safe shutdown and continuity are untested. Do not convert unresolved concerns into a numerical pass score.

## Audit record

Store model/version identifiers, scope, tests, evidence, known limitations, agent dependencies, reviewer independence, dissent, incidents, approvals, complaints, and rollback status. Retain personal data only as necessary and lawful; publish no sensitive records.