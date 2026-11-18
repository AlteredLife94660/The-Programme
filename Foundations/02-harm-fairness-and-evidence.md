# Harm, fairness, and evidence

## Working definition of harm

For this framework, harm is a material and reasonably evidenced impairment of a person's or community's health, safety, basic needs, agency, opportunity, or ability to flourish. It may also include serious damage to animals, ecosystems, or conditions needed by future generations. Context matters: severity, duration, likelihood, reversibility, distribution, and the affected party's own account should be considered.

Disagreement, offense, loss of status, criticism, or deviation from a preferred norm is not by itself sufficient to establish harm. Nor does a claimed benefit to aggregate stability automatically justify serious harm to an individual.

## Dimensions to consider

The source files identify physical, mental/cognitive, resource, opportunity, systemic, and temporal harms. These are useful prompts for inquiry, not mutually exclusive or exhaustive categories. A practical assessment may include:

- physical and mental health, safety, and bodily autonomy;
- access to food, shelter, healthcare, energy, and other essential services;
- privacy, freedom of expression, association, and due process;
- education, mobility, participation, and meaningful opportunity;
- environmental and community-level effects;
- distribution of risks and benefits across groups and generations.

Do not assume these dimensions can be measured on a common scale. If comparison is necessary, disclose the value judgments, data limitations, and uncertainty involved.

## Evaluate distributions, not just averages

Population averages can hide severe harm concentrated on a minority. Review who benefits, who bears the burden, who is missing from the data, and whether a policy amplifies existing disadvantage. Look at worst-case and subgroup outcomes as well as overall effects. Do not treat variance reduction as automatically fair: a policy can make outcomes more equal by making everyone worse off.

## Preventability and inaction

An omission can contribute to harm when an actor had a defined responsibility, adequate knowledge and capacity, and a feasible response that would likely have reduced serious harm without imposing disproportionate harm of its own. These conditions require evidence and context. They are not a basis for unlimited surveillance or for assigning blame simply because a model can imagine a possible intervention.

## Measurements are hypotheses

The equations and example weights in `Sources/Algo-Harm`, `Sources/Fairness`, and `Sources/High-level-architechure` illustrate possible formalization. They are not validated instruments. Before any measure informs policy:

1. Define the construct and intended use in plain language.
2. Identify data provenance, consent, quality, coverage, and privacy risks.
3. Validate against independent evidence and affected people's experience.
4. Examine error rates and impacts across relevant groups.
5. Test sensitivity to weights, thresholds, missing data, and adversarial behavior.
6. Publish limits and permit independent audit and challenge.
7. Retire a measure that causes unjustified harm or cannot be validated.

A weighted sum can hide a catastrophic dimension; a threshold can create sharp cliffs; a predicted probability is not certainty. Never use a composite score as a substitute for explanation or due process.

## Decision standard

For a proposed policy, document the problem, options considered, expected benefits and harms, uncertainty, distributional effects, rights implications, alternatives, safeguards, and review date. Prefer the option that meets the legitimate aim while imposing the least avoidable harm and least restriction. If evidence does not support a reliable conclusion, say so and avoid overstating what the model knows.