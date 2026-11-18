"""Rights-preserving prevention, support, and repair options."""

from typing import Any, Mapping

from models import Result, DecisionState, require_mapping


def prevention_support_repair(payload: Mapping[str, Any]) -> Result:
    payload = require_mapping(payload, "payload")
    known_facts = payload.get("known_facts", [])
    allegations = payload.get("allegations", [])
    affected_needs = payload.get("affected_needs", [])

    if not isinstance(known_facts, (list, tuple)):
        raise ValueError("known_facts must be a list or tuple")
    if not isinstance(allegations, (list, tuple)):
        raise ValueError("allegations must be a list or tuple")
    if not isinstance(affected_needs, (list, tuple)):
        raise ValueError("affected_needs must be a list or tuple")

    if not known_facts:
        return Result(
            module="prevention_support_repair",
            state=DecisionState.INCOMPLETE,
            summary="No verified or clearly bounded factual record is available for case support.",
            findings=[{"allegations": list(allegations)}],
            questions_for_human_review=[
                "What facts have been lawfully and reliably established?",
                "What support does each affected person need?",
                "Which accountable institution has lawful authority?",
            ],
            safeguards=[
                "An allegation is not a finding of guilt.",
                "No coercive disposition or person-risk score may be produced.",
            ],
        )

    return Result(
        module="prevention_support_repair",
        state=DecisionState.REVIEW,
        summary="Generate case-support options for an accountable human process; no guilt or restriction is inferred.",
        findings=[
            {"known_facts": list(known_facts)},
            {"allegations": list(allegations)},
            {"affected_needs": list(affected_needs)},
        ],
        questions_for_human_review=[
            "Which prevention, support, voluntary repair, or safeguarding options are appropriate?",
            "If a restriction is legally proposed, is it necessary, proportionate, time-limited, and independently reviewable?",
            "What representation, notice, appeal, and remedy are available?",
        ],
        safeguards=[
            "No AI determination of guilt or dangerousness.",
            "No surveillance, detention, movement restriction, or essential-service denial.",
            "No contribution, poverty, identity, or group membership as guilt evidence.",
            "Use the least-restrictive effective option.",
            "Affected people choose voluntary support or repair whenever appropriate.",
        ],
    )