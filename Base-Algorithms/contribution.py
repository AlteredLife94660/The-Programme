"""Scoped, temporary contribution recognition.

No result may affect worth, rights, basic needs, or access to justice.
"""

from typing import Any, Mapping

from models import Result, DecisionState, require_mapping, require_text


def recognize_contribution(payload: Mapping[str, Any]) -> Result:
    payload = require_mapping(payload, "payload")
    purpose = require_text(payload.get("purpose"), "purpose")
    activity = require_text(payload.get("activity"), "activity")

    prohibited_purposes = (
        "rank people", "social credit", "guilt", "punishment",
        "rights", "essential needs", "coercion", "public leaderboard",
    )

    if any(term in purpose.lower() for term in prohibited_purposes):
        return Result(
            module="contribution_recognition",
            state=DecisionState.STOP,
            summary="Contribution recognition cannot rank people or affect coercive or essential-needs decisions.",
            safeguards=[
                "Human worth is independent of contribution.",
                "No universal social score.",
                "No contribution test for survival or rights.",
            ],
        )

    consenting = bool(payload.get("participants_consent", False))
    retention_days = payload.get("retention_days")
    equity_check = payload.get("equity_check_completed", False)

    findings = [{
        "purpose": purpose,
        "activity": activity,
        "participants_consent": consenting,
        "retention_days": retention_days,
        "equity_check_completed": bool(equity_check),
    }]

    questions: list[str] = []
    if not consenting:
        questions.append("Do participants voluntarily consent to this scoped recognition process?")
    if retention_days is None:
        questions.append("Define a time limit and correction/deletion process.")
    if not equity_check:
        questions.append("Complete an independent check for bias, invisibility, gaming, and disparate impact.")

    state = DecisionState.REVIEW if questions else DecisionState.REVIEW
    return Result(
        module="contribution_recognition",
        state=state,
        summary="Produce a scoped, temporary recognition description for human review; it has no status or entitlement effect.",
        findings=findings,
        questions_for_human_review=questions,
        safeguards=[
            "Include care, maintenance, learning, and community activity.",
            "Do not assign exclusive credit for collective or uncertain outcomes.",
            "No permanent status or authority.",
            "No data collection for compliance or surveillance.",
        ],
    )