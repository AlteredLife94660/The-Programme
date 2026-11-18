#!/usr/bin/env python3
"""Demonstration entry point for the Base-Algorithms package."""

import json

from coordinator import coordinate


def main() -> None:
    payload = {
        "modules": ["harm_fairness", "needs_support", "power", "audit"],
        "harm_fairness": {
            "question": "Could a proposed service restriction worsen basic needs?",
            "action": "temporary pilot of a proposed access policy",
            "affected_parties": ["service users", "caregivers", "small providers"],
            "impacts": [{
                "domain": "basic_needs",
                "description": "Possible interruption of essential service access",
                "severity": "high",
                "likelihood": "possible",
                "duration": "temporary",
                "reversibility": "partly_reversible",
            }],
            "distribution": {
                "subgroup_impacts": ["access may differ by disability, location, or income"],
                "missing_or_excluded_groups": ["people not represented in the service data"],
            },
        },
        "needs_support": {
            "stated_needs": {
                "healthcare": {"description": "Person requests accessible health support"},
                "communication": {"description": "Person requests an accessible communication channel"},
            },
            "preferences": ["in-person support"],
        },
        "power": {
            "unit": "Example service institution",
            "public_purpose": "Independent accountability review",
            "channels": ["information", "decision_authority"],
            "evidence": ["public governance record", "documented conflict-of-interest finding"],
        },
        "audit": {
            "purpose": "research-only advisory analysis",
            "accountable_owner": "Independent human review board",
            "independent_audit": True,
            "human_fallback": True,
            "appeal_route": True,
            "privacy_review": True,
            "safe_shutdown": True,
            "affected_party_participation": True,
            "prohibited_features": [],
        },
    }

    print(json.dumps(coordinate(payload), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()