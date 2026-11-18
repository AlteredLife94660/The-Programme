"""Governance gate for proposed multi-agent implementations."""

from typing import Any, Iterable, Mapping

from models import Result, DecisionState, require_mapping


PROHIBITED_FEATURES = {
    "autonomous_person_ranking",
    "coercive_disposition",
    "surveillance_without_lawful_basis",
    "essential_needs_denial",
    "speech_suppression",
    "self_granted_authority",
    "guilt_from_risk_score",
}


def audit_proposal(payload: Mapping[str, Any]) -> Result:
    payload = require_mapping(payload, "payload")
    purpose = str(payload.get("purpose", "")).strip()
    accountable_owner = str(payload.get("accountable_owner", "")).strip()
    proposed_features = payload.get("prohibited_features", [])

    if not isinstance(proposed_features, (list, tuple, set)):
        raise ValueError("prohibited_features must be a collection")

    detected = set(proposed_features) & PROHIBITED_FEATURES
    missing: list[str] = []

    if not purpose:
        missing.append("Define a narrow purpose.")
    if not accountable_owner:
        missing.append("Identify an accountable human owner.")

    required_fields = (
        "independent_audit", "human_fallback", "appeal_route",
        "privacy_review", "safe_shutdown", "affected_party_participation",
    )
    absent_safeguards = [
        field for field in required_fields
        if not bool(payload.get(field, False))
    ]

    if detected:
        state = DecisionState.NO_GO
        summary = "The proposal includes prohibited authority-bearing or coercive features."
    elif missing or absent_safeguards:
        state = DecisionState.NO_GO
        summary = "The governance gate is incomplete; deployment must not proceed."
    else:
        state = DecisionState.REVIEW
        summary = "Minimum documented governance requirements are present; independent review and limited pilot approval are still required."

    questions = missing + [
        f"Document and provide: {field}" for field in absent_safeguards
    ]
    if detected:
        questions.append("Remove prohibited features or terminate the proposal: " + ", ".join(sorted(detected)))

    return Result(
        module="independent_governance_audit",
        state=state,
        summary=summary,
        findings=[{
            "purpose": purpose,
            "accountable_owner": accountable_owner,
            "detected_prohibited_features": sorted(detected),
            "missing_safeguards": absent_safeguards,
        }],
        questions_for_human_review=questions,
        safeguards=[
            "No model or agent may grant itself authority.",
            "No rights-affecting decision may be automated.",
            "Independent review must include affected parties.",
            "Safe rollback and continuity must be tested.",
        ],
    )