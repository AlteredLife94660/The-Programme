"""Voluntary needs-support option generation.

This module does not determine entitlement, deservingness, or eligibility.
"""

from typing import Any, Mapping

from models import Result, DecisionState, require_mapping, require_text


NEED_CATEGORIES = {
    "food", "shelter", "healthcare", "water_sanitation", "energy",
    "safety", "communication", "mobility", "education", "participation",
}


def support_options(payload: Mapping[str, Any]) -> Result:
    payload = require_mapping(payload, "payload")
    stated_needs = payload.get("stated_needs", {})
    stated_needs = require_mapping(stated_needs, "stated_needs")
    preferences = payload.get("preferences", [])

    unknown_categories = set(stated_needs) - NEED_CATEGORIES
    if unknown_categories:
        return Result(
            module="needs_support",
            state=DecisionState.INCOMPLETE,
            summary="Unknown need categories require a human-defined, accessible review.",
            questions_for_human_review=[
                f"Define or replace the category: {category}" for category in sorted(unknown_categories)
            ],
            safeguards=[
                "Ask the person about their needs rather than inferring them.",
                "No contribution or labor condition may determine basic support.",
            ],
        )

    findings: list[dict[str, Any]] = []
    for category, details in stated_needs.items():
        if isinstance(details, Mapping):
            summary = str(details.get("description", "Person-stated need"))
        else:
            summary = str(details)
        findings.append({"category": category, "person_description": summary})

    urgent = bool(payload.get("urgent_safety_or_health_risk", False))
    questions: list[str] = []

    if urgent:
        questions.append("Refer immediately to the appropriate accountable emergency or safeguarding service under applicable procedure.")

    if not preferences:
        questions.append("Which voluntary support options are acceptable to the person?")

    return Result(
        module="needs_support",
        state=DecisionState.REVIEW,
        summary="Provide a person-controlled list of voluntary support options; eligibility and service decisions remain with legitimate human institutions.",
        findings=findings,
        questions_for_human_review=questions,
        safeguards=[
            "No deservingness score or automated eligibility rule.",
            "No contribution, labor, or compliance test for basic needs.",
            "No inference from social media or unrelated proxies.",
            "Provide appeal and non-digital support routes.",
            "Retain only minimum necessary data with consent or lawful basis.",
        ],
    )