"""Coordinator for bounded base-algorithm analyses.

The coordinator never makes an authority-bearing decision. Any STOP or NO_GO
result overrides REVIEW results and requires a legitimate human process.
"""

from typing import Any, Mapping

from models import Result, DecisionState, require_mapping
from harm_fairness import assess_harm_and_fairness
from needs_support import support_options
from contribution import recognize_contribution
from power import review_power
from prevention_repair import prevention_support_repair
from audit import audit_proposal


def coordinate(payload: Mapping[str, Any]) -> dict[str, Any]:
    payload = require_mapping(payload, "payload")
    modules = payload.get("modules", [])
    if not isinstance(modules, (list, tuple)):
        raise ValueError("modules must be a list or tuple")

    allowed = {
        "harm_fairness": (assess_harm_and_fairness, payload.get("harm_fairness", {})),
        "needs_support": (support_options, payload.get("needs_support", {})),
        "contribution": (recognize_contribution, payload.get("contribution", {})),
        "power": (review_power, payload.get("power", {})),
        "prevention_repair": (prevention_support_repair, payload.get("prevention_repair", {})),
        "audit": (audit_proposal, payload.get("audit", {})),
    }

    unknown = [name for name in modules if name not in allowed]
    if unknown:
        raise ValueError(f"Unknown module names: {', '.join(sorted(unknown))}")

    results: list[dict[str, Any]] = []
    for name in modules:
        function, module_payload = allowed[name]
        try:
            result = function(require_mapping(module_payload, name))
        except (ValueError, KeyError, TypeError) as error:
            result = Result(
                module=name,
                state=DecisionState.INCOMPLETE,
                summary="The module input could not be processed safely.",
                questions_for_human_review=[str(error)],
                safeguards=["No conclusion or authority-bearing action was produced."],
            )
        results.append(result.to_dict())

    states = {result["state"] for result in results}
    if "NO_GO" in states or "STOP" in states:
        overall = "STOP"
    elif "INCOMPLETE" in states:
        overall = "INCOMPLETE"
    else:
        overall = "REVIEW"

    return {
        "overall_state": overall,
        "human_authority_required": True,
        "results": results,
        "notice": "These outputs are advisory research records, not decisions, predictions, or legal authority.",
    }