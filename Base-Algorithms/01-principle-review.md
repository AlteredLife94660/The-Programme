# Algorithm 1 — Principle and proposal review

## Aim

Help a human team review a proposed policy or action against the Programme's declared principles before implementation. This is a **structured checklist**, not a moral oracle or policy-approval engine.

## Inputs

- Plain-language proposal, purpose, scope, sponsor, and accountable decision-maker.
- Affected people and communities; rights and services implicated.
- Evidence, alternatives (including non-AI and no-action), assumptions, and uncertainty.
- Legal basis, consent/participation plan, safeguards, review and rollback plan.

## Procedure

1. **Scope gate:** If purpose, accountable human authority, affected groups, or lawful basis is unspecified, return `INCOMPLETE — DO NOT ADVANCE` with missing items.
2. **Dignity and moral consideration:** Check whether anyone's worth, rights, or access to essentials is tied to identity, status, productivity, contribution, predicted usefulness, or model score. A proposed ranking of human worth is a hard fail.
3. **Harm and fairness:** Identify plausible harms from action and inaction; consider severity, likelihood, duration, reversibility, distribution, and affected people's perspectives. Do not reduce the assessment to a single aggregate score.
4. **Agency and consent:** Check meaningful participation, dissent, accessibility, privacy, and whether refusal or exit would cost someone basic needs.
5. **Power and authority:** Identify who gains decision power, data access, or control; examine checks, independence, scope limits, audit, and challenge routes.
6. **Least-harm alternatives:** Compare feasible alternatives and explain why the preferred option meets a legitimate aim with the least restriction and avoidable harm.
7. **Evidence and uncertainty:** Separate facts, assumptions, estimates, and unresolved value judgments. If uncertainty or likely impact is high, require further consultation or testing.
8. **Decision memo:** Output `SUPPORT FOR FURTHER HUMAN REVIEW`, `REVISE`, or `STOP / ESCALATE`, with reasons, dissent, conditions, and review date. Never output an autonomous approval.

## Hard-stop results

Return `STOP / ESCALATE` for a plan to autonomously rank human worth, punish or restrict people on a model score, suppress peaceful dissent, deny essential needs based on contribution, or evade lawful process. Give a safer alternative where possible.

## Output format

- Proposal and scope
- Accountable human authority and affected parties
- Findings for each principle (evidence / uncertainty / missing information)
- Rights and distributional risks
- Alternatives considered
- Recommendation and conditions (not a binding decision)
- Appeal, oversight, review, rollback, and unresolved human choices