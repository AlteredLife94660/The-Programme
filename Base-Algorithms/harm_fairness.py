"""Harm and fairness assessment for human review.

This module intentionally emits no person score or deployment decision.
"""

from typing import Any, Mapping, Sequence

from models import Evidence, Impact, Result, DecisionState, require_mapping, require_sequence, require_text


HARM_DOMAINS = (
    "physical_health",
    "mental_health",
    "basic_needs",
    "autonomy",
    "privacy",
    "opportunity",
    "community",
    "environment",
    "future_generations",
)


SEVERITY_VALUES = {"negligible", "low", "medium", "high", "critical", "unknown"}
LIKELIHOOD_VALUES = {"remote", "unlikely", "possible", "likely", "expected", "unknown"}
DURATION_VALUES = {"brief", "temporary", "ongoing", "permanent", "unknown"}
REVERSIBILITY_VALUES = {"fully_reversible", "partly_reversible", "irreversible", "unknown"}


def assess_harm_and_fairness(payload: Mapping[str, Any]) -> Result:
    payload = require_mapping(payload, "payload")

    question = require_text(payload.get("question"), "question")
    action = require_text(payload.get("action"), "action")
    affected = require_sequence(payload.get("affected_parties", []), "affected_parties")

    missing: list[str] = []
    if not affected:
        missing.append("Identify affected people and communities.")

    raw_impacts = payload.get("impacts", [])
    impacts = require_sequence(raw_impacts, "impacts")

    findings: list[dict[str, Any]] = []
    questions: list[str] = []

    for index, raw in enumerate(impacts):
        item = require_mapping(raw, f"impacts[{index}]")
        domain = require_text(item.get("domain"), f"impacts[{index}].domain")
        description = require_text(item.get("description"), f"impacts[{index}].description")
        severity = str(item.get("severity", "unknown")).lower()
        likelihood = str(item.get("likelihood", "unknown")).lower()
        duration = str(item.get("duration", "unknown")).lower()
        reversibility = str(item.get("reversibility", "unknown")).lower()

        if domain not in HARM_DOMAINS:
            missing.append(f"impacts[{index}].domain must be one of {', '.join(HARM_DOMAINS)}")
        if severity not in SEVERITY_VALUES:
            missing.append(f"impacts[{index}].severity is not recognized")
        if likelihood not in LIKELIHOOD_VALUES:
            missing.append(f"impacts[{index}].likelihood is not recognized")
        if duration not in DURATION_VALUES:
            missing.append(f"impacts[{index}].duration is not recognized")
        if reversibility not REVERSIBILITY_VALUES:
            missing.append(f"impacts[{index}].reversibility is not recognized")

        findings.append({
            "domain": domain,
            "description": description,
            "severity": severity,
            "likelihood": likelihood,
            "duration": duration,
            "reversibility": reversibility,
            "evidence": [item.to_dict() for item in item.get("evidence", ()) if isinstance(item, Evidence)],
        })

    distribution = require_mapping(payload.get("distribution", {}), "distribution")
    subgroup_impacts = distribution.get("subgroup_impacts", [])
    missing_or_excluded = distribution.get("missing_or_excluded_groups", [])

    if not subgroup_impacts:
        questions.append("Who bears each impact, and are relevant subgroups represented?")
    if not missing_or_excluded:
        questions.append("Which populations or perspectives are missing from the evidence?")

    serious_unknown = any(
        finding["severity"] in {"high", "critical"} and finding["likelihood"] in {"unknown", "possible", "likely", "expected"}
        for finding in findings
    )

    if missing:
        state = DecisionState.INCOMPLETE
        summary = "The harm and fairness assessment cannot advance until incomplete fields are resolved."
    elif serious_unknown:
        state = DecisionState.REVIEW
        summary = "Serious or potentially severe impacts require accountable human review and further evidence."
    else:
        state = DecisionState.REVIEW
        summary = "The assessment organizes evidence and options for human review; it does not decide a policy or person."

    if payload.get("merely_offense_or_disagreement"):
        state = DecisionState.REVIEW
        questions.append("Confirm that a claim of offense is supported by a distinct, material impairment before treating it as harm.")

    return Result(
        module="harm_and_fairness_assessment",
        state=state,
        summary=summary,
        findings=findings,
        questions_for_human_review=questions + missing,
        safeguards=[
            "No aggregate score may override serious or rights-affecting individual impacts.",
            "No person-score or deployment decision is produced.",
            "Include affected-person accounts and missing populations.",
            "Compare feasible alternatives, including no action and non-AI options.",
        ],
    )