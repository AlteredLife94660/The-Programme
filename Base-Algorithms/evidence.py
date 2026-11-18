"""Evidence quality and uncertainty helpers.

These functions support evidence review. They do not infer probability,
character, intent, or an individual's future behavior.
"""

from typing import Iterable

from models import Evidence, EvidenceKind


VALID_KINDS = {item.value for item in EvidenceKind}


def validate_evidence(item: Evidence) -> list[str]:
    problems: list[str] = []
    if item.kind not in EvidenceKind:
        problems.append("The evidence kind is not recognized.")
    if not item.claim.strip():
        problems.append("The evidence claim is empty.")
    if not item.source.strip():
        problems.append("The evidence source is missing.")
    if not item.uncertainty.strip():
        problems.append("The uncertainty description is missing.")
    if item.kind in (EvidenceKind.ESTIMATE, EvidenceKind.HYPOTHESIS):
        if "unknown" in item.uncertainty.lower():
            problems.append("Estimates and hypotheses require specific uncertainty limits.")
    return problems


def evidence_summary(items: Iterable[Evidence]) -> dict[str, int]:
    counts = {kind.value: 0 for kind in EvidenceKind}
    for item in items:
        counts[item.kind.value] += 1
    return counts


def confidence_is_sufficient_for_research(items: Iterable[Evidence]) -> bool:
    evidence = list(items)
    if not evidence:
        return False
    if any(validate_evidence(item) for item in evidence):
        return False
    return not any(
        item.kind in (EvidenceKind.HYPOTHESIS, EvidenceKind.UNKNOWN)
        for item in evidence
    )