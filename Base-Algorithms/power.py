"""Power-concentration review for legitimate human institutions."""

from typing import Any, Mapping

from models import Result, DecisionState, require_mapping, require_text


POWER_CHANNELS = {
    "wealth", "information", "infrastructure", "decision_authority",
    "communication_reach", "essential_resources", "data_control",
}


def review_power(payload: Mapping[str, Any]) -> Result:
    payload = require_mapping(payload, "payload")
    unit = require_text(payload.get("unit"), "unit")
    public_purpose = require_text(payload.get("public_purpose"), "public_purpose")

    channels = payload.get("channels", [])
    if not isinstance(channels, (list, tuple)):
        raise ValueError("channels must be a list or tuple")

    unknown = set(channels) - POWER_CHANNELS
    if unknown:
        return Result(
            module="power_concentration_review",
            state=DecisionState.INCOMPLETE,
            summary="The power channels are incomplete or unrecognized.",
            questions_for_human_review=[f"Define the power channel: {item}" for item in sorted(unknown)],
            safeguards=["No enforcement or compulsory redistribution is authorized."],
        )

    evidence = payload.get("evidence", [])
    if not isinstance(evidence, (list, tuple)):
        raise ValueError("evidence must be a list or tuple")

    if not channels or not evidence:
        return Result(
            module="power_concentration_review",
            state=DecisionState.INCOMPLETE,
            summary="A power-review case requires identified channels and proportionate evidence.",
            questions_for_human_review=[
                "Identify control channels.",
                "Supply lawful, relevant, and sufficient evidence.",
            ],
            safeguards=["No automatic decay or seizure."],
        )

    return Result(
        module="power_concentration_review",
        state=DecisionState.REVIEW,
        summary="Surface potential concentration for independent human review; no enforcement action is produced.",
        findings=[{
            "unit": unit,
            "public_purpose": public_purpose,
            "channels": list(channels),
            "evidence_count": len(evidence),
        }],
        questions_for_human_review=[
            "What practical effect does the concentration have on rights, access, or challenge?",
            "What lawful and least-restrictive safeguards could accountable institutions consider?",
            "What side effects may affect privacy, service continuity, dissent, or smaller institutions?",
        ],
        safeguards=[
            "No universal decay rate or compulsory seizure.",
            "No censorship based solely on a stability or speech label.",
            "No algorithmic or institutional actor may expand its own authority.",
            "Require independent review and appeal.",
        ],
    )