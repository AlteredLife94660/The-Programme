# Algorithm 2 — Harm and fairness assessment

## Aim

Organize evidence about possible effects of a proposal or event without turning harm into an absolute judgment of an individual or claiming that all dimensions share one measurable scale. It develops `Sources/Algo-Harm` and `Sources/Fairness` under `Foundations/02-harm-fairness-and-evidence.md`.

## Inputs

A clearly scoped action or policy; plausible affected parties; evidence and provenance; baseline and counterfactual options; time horizon; known limits and uncertainty. Use the minimum personal data necessary.

## Procedure

1. **Define the question:** Describe the action and what potential harm is being assessed. Exclude mere disagreement, offense, criticism, or status loss unless there is separate evidence of material impairment.
2. **Map impacts:** Consider physical/mental health, safety, basic needs, autonomy, privacy, opportunity, community and environmental effects, and future impacts. Add context-specific dimensions; do not assume the list is exhaustive.
3. **Assess each impact:** Record affected group/person, severity, likelihood, duration, reversibility, evidence quality, uncertainty, and the affected person's own account where available. Do not convert an uncertain probability into a fact.
4. **Examine distribution:** Identify who benefits, who bears each burden, subgroup and worst-case outcomes, missing populations, accessibility, and existing disadvantage. A good population average cannot cancel a severe individual impact.
5. **Assess preventability carefully:** Count omission only where there is a defined role or responsibility, sufficient knowledge and capacity, a feasible response, and a reasonable expectation that the response would reduce serious harm without disproportionate harm.
6. **Compare options:** Include the status quo, no action, non-AI alternatives, and the least restrictive feasible response. Explain trade-offs; do not hide value judgments in weights.
7. **Report, do not decide:** Produce an evidence table and uncertainty statement. Recommend additional evidence or human deliberation where material uncertainty or rights impact remains.

## No-score rule

Do not emit a single `fairness score`, `person risk score`, or numeric rank as a conclusion. If a limited metric is used for research, specify the construct, scale, validation, data limitations, subgroup error, sensitivity analysis, and intended use. It must not be used alone for eligibility, enforcement, or a rights-affecting decision.

## Output

`Question | Impacts | Evidence | Uncertainty | Distribution | Options | Rights/safeguards | Unresolved human judgments`. Mark any conclusion unsupported by evidence as a hypothesis.