from __future__ import annotations

import sys
import unittest

sys.path.insert(0, ".")
sys.path.insert(0, "./Base-Algorithms")

from audit import audit_proposal
from contribution import recognize_contribution
from harm_fairness import assess_harm_and_fairness
from needs_support import support_options
from coordinator import coordinate
from power import review_power
from prevention_repair import prevention_support_repair


class BaseAlgorithmsTests(unittest.TestCase):
    def test_harm_assessment_never_emits_person_score(self):
        result = assess_harm_and_fairness({
            "question": "What are the likely effects?",
            "action": "Change an information service",
            "affected_parties": ["users"],
            "impacts": [{
                "domain": "privacy",
                "description": "Data collection could expose information",
                "severity": "high",
                "likelihood": "possible",
                "duration": "ongoing",
                "reversibility": "partly_reversible",
            }],
            "distribution": {
                "subgroup_impacts": ["marginalized users may be affected"],
                "missing_or_excluded_groups": ["people without data access"],
            },
        })
        rendered = str(result.to_dict()).lower()
        self.assertIn("person", rendered)
        self.assertNotIn("person_score", rendered)

    def test_needs_support_rejects_unknown_categories(self):
        result = support_options({
            "stated_needs": {"unknown_category": "The person needs help"},
            "preferences": [],
        })
        self.assertEqual(result.state.value, "INCOMPLETE")

    def test_contribution_stops_rank_or_score_purpose(self):
        result = recognize_contribution({
            "purpose": "rank people for a public leaderboard",
            "activity": "community work",
        })
        self.assertEqual(result.state.value, "STOP")

    def test_power_review_requires_evidence(self):
        result = review_power({
            "unit": "Institution",
            "public_purpose": "Accountability",
            "channels": [],
            "evidence": [],
        })
        self.assertEqual(result.state.value, "INCOMPLETE")

    def test_prevention_repair_never_accepts_allegation_alone(self):
        result = prevention_support_repair({
            "known_facts": [],
            "allegations": ["an allegation without evidence"],
            "affected_needs": ["safety information"],
        })
        self.assertEqual(result.state.value, "INCOMPLETE")
        rendered = str(result.to_dict()).lower()
        self.assertIn("no coercive", rendered)

    def test_audit_gate_blocks_forbidden_features(self):
        result = audit_proposal({
            "purpose": "decision support",
            "accountable_owner": "Human review board",
            "independent_audit": True,
            "human_fallback": True,
            "appeal_route": True,
            "privacy_review": True,
            "safe_shutdown": True,
            "affected_party_participation": True,
            "prohibited_features": ["coercive_disposition"],
        })
        self.assertEqual(result.state.value, "NO_GO")

    def test_audit_gate_requires_safeguards(self):
        result = audit_proposal({
            "purpose": "research",
            "accountable_owner": "",
        })
        self.assertEqual(result.state.value, "NO_GO")

    def test_coordinator_stop_overrides_review(self):
        result = coordinate({
            "modules": ["audit", "harm_fairness"],
            "audit": {
                "purpose": "test",
                "accountable_owner": "board",
                "prohibited_features": ["coercive_disposition"],
            },
            "harm_fairness": {
                "question": "Potential effect",
                "action": "pilot",
                "affected_parties": ["people"],
                "impacts": [],
                "distribution": {},
            },
        })
        self.assertEqual(result["overall_state"], "STOP")
        self.assertTrue(result["human_authority_required"])


if __name__ == "__main__":
    unittest.main()