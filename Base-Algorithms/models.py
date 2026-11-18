"""Core bounded data structures for the Programme's base algorithms.

This module contains no person-scoring or enforcement primitives.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Mapping, Sequence


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class DecisionState(str, Enum):
    INCOMPLETE = "INCOMPLETE"
    REVIEW = "REVIEW"
    STOP = "STOP"
    NO_GO = "NO_GO"


class EvidenceKind(str, Enum):
    VERIFIED = "verified"
    ACCOUNT = "affected_person_account"
    ESTIMATE = "estimate"
    HYPOTHESIS = "hypothesis"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Evidence:
    """A claim with provenance and an honest evidence classification."""

    claim: str
    kind: EvidenceKind
    source: str
    uncertainty: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "claim": self.claim,
            "kind": self.kind.value,
            "source": self.source,
            "uncertainty": self.uncertainty,
        }


@dataclass(frozen=True)
class Impact:
    domain: str
    description: str
    severity: str
    likelihood: str
    duration: str
    reversibility: str
    evidence: tuple[Evidence, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "domain": self.domain,
            "description": self.description,
            "severity": self.severity,
            "likelihood": self.likelihood,
            "duration": self.duration,
            "reversibility": self.reversibility,
            "evidence": [item.to_dict() for item in self.evidence],
        }


@dataclass
class Result:
    module: str
    state: DecisionState
    summary: str
    findings: list[dict[str, Any]] = field(default_factory=list)
    questions_for_human_review: list[str] = field(default_factory=list)
    safeguards: list[str] = field(default_factory=list)
    timestamp: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "module": self.module,
            "state": self.state.value,
            "summary": self.summary,
            "findings": self.findings,
            "questions_for_human_review": self.questions_for_human_review,
            "safeguards": self.safeguards,
            "timestamp": self.timestamp,
        }


def require_text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()


def require_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be a mapping")
    return value


def require_sequence(value: Any, name: str) -> Sequence[Any]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise ValueError(f"{name} must be a sequence")
    return value


def evidence_or_unknown(
    claim: str,
    source: str = "No source supplied",
    uncertainty: str = "Unknown",
) -> Evidence:
    return Evidence(
        claim=require_text(claim, "claim"),
        kind=EvidenceKind.UNKNOWN,
        source=require_text(source, "source"),
        uncertainty=require_text(uncertainty, "uncertainty"),
    )