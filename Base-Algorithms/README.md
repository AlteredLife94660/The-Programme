# Base Algorithms — Implementation

The algorithm documents in this directory are currently conceptual specifications. The implementation in this repository will be ordinary, auditable decision-support code: it may evaluate data, classify options, or produce recommendations, but it must not exercise authority over people or institutions.

## Language

Python 3.11 or newer.

## Scope

The implementation deliberately separates measurement from action:

- Harm and fairness review produces evidence records and uncertainty.
- Needs support produces voluntary options and never determines worth or entitlement.
- Contribution recognition produces a temporary, scoped description and is never used for rights or essentials.
- Power review produces evidence for independent human review, not enforcement.
- Prevention and repair proposes least-restrictive options, never guilt or coercive disposition.
- An independent audit validator checks whether a proposal has the minimum governance safeguards.
- The multi-algorithm coordinator may combine independent analyses only for review and cannot issue authority-bearing decisions.

Every public function validates its inputs, preserves unknown values instead of guessing, and returns an auditable result record. The module uses only the Python standard library so it can be reviewed, tested, and run without external services.

## Not included

No person-risk model, guilt classifier, coercive disposition, surveillance system, citizen score, forced redistribution mechanism, social-credit ranking, or content-suppression feature is implemented. No training dataset, model weights, biometric collection, or automatic eligibility decision is included.

## Status

These are research-grade Python modules. They do not confer legal authority and are not production-ready for decisions affecting rights or basic needs. Real deployment requires legitimate human governance, independent impact assessment, affected-community participation, security/privacy controls, audit, appeal, and applicable law.

## Files

- `models.py`: bounded data structures and evidence record types.
- `evidence.py`: evidence-quality and uncertainty helpers.
- `harm_fairness.py`: harm and distribution assessment.
- `needs_support.py`: voluntary needs-support option review.
- `contribution.py`: scoped, temporary contribution recognition.
- `power.py`: power-concentration review for human institutions.
- `prevention_repair.py`: rights-preserving prevention/support/repair options.
- `audit.py`: independent-governance and deployment gate.
- `coordinator.py`: combines analyses while preserving stop conditions and human fallback.
- `cli.py`: demonstration interface.
- `tests/test_base_algorithms.py`: unit tests for boundaries and core behavior.

Run the demonstration with:

```bash
python3 Base-Algorithms/cli.py
```

Run tests with:

```bash
python3 -m unittest discover -s Base-Algorithms/tests -v
```