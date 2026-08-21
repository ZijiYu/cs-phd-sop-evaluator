# Output Schemas

## 1. Single-SOP JSON

```json
{
  "rubric_version": "2.0",
  "mode": "single",
  "sop_id": "SOP-A01",
  "scope": {
    "program": "",
    "prompt_verified": false,
    "limit_verified": false,
    "faculty_verified": false
  },
  "gates": {
    "G1": {"status": "PASS", "reason": ""},
    "G2": {"status": "PASS", "reason": ""},
    "G3": {"status": "PASS", "reason": ""},
    "G4": {"status": "UNVERIFIED", "reason": ""},
    "G5": {"status": "UNVERIFIED", "reason": ""},
    "G6": {"status": "PASS", "reason": ""},
    "G7": {"status": "PASS", "reason": ""}
  },
  "dimensions": {
    "D1": {"raw": 0, "weight": 15, "confidence": "LOW", "evidence_spans": [], "counter_evidence": [], "missing_for_next_level": ""},
    "D2": {"raw": 0, "weight": 20, "confidence": "LOW", "evidence_spans": [], "counter_evidence": [], "missing_for_next_level": ""},
    "D3": {"raw": 0, "weight": 15, "confidence": "LOW", "evidence_spans": [], "counter_evidence": [], "missing_for_next_level": ""},
    "D4": {"raw": 0, "weight": 15, "confidence": "LOW", "evidence_spans": [], "counter_evidence": [], "missing_for_next_level": ""},
    "D5": {"raw": 0, "weight": 10, "confidence": "LOW", "evidence_spans": [], "counter_evidence": [], "missing_for_next_level": ""},
    "D6": {"raw": 0, "weight": 15, "confidence": "LOW", "evidence_spans": [], "counter_evidence": [], "missing_for_next_level": ""},
    "D7": {"raw": 0, "weight": 10, "confidence": "LOW", "evidence_spans": [], "counter_evidence": [], "missing_for_next_level": ""}
  },
  "total_score": 0,
  "internal_status": "REBUILD",
  "one_sentence_research_identity": "",
  "strongest_feature": "",
  "main_bottleneck": "",
  "red_flags": [],
  "holistic_context": {"supplied": false, "effect_on_interpretation": "", "score_effect": "none"},
  "top_revisions": [],
  "faculty_overfitting": {"status": "", "reason": ""},
  "adversarial_read": {}
}
```

## 2. Aggregation input JSON

The deterministic script accepts scores and anonymous IDs only. Do not include SOP text or contact information.

```json
{
  "mode": "same_program",
  "near_score_threshold": 5.0,
  "sops": [
    {
      "sop_id": "SOP-A01",
      "gate_status": "PASS",
      "judges": [
        {"judge_id": "J1", "D1": 3, "D2": 3, "D3": 2, "D4": 3, "D5": 2, "D6": 3, "D7": 3},
        {"judge_id": "J2", "D1": 3, "D2": 4, "D3": 3, "D4": 3, "D5": 2, "D6": 3, "D7": 3}
      ]
    },
    {
      "sop_id": "SOP-A02",
      "gate_status": "PASS",
      "judges": [
        {"judge_id": "J1", "D1": 3, "D2": 3, "D3": 3, "D4": 2, "D5": 3, "D6": 3, "D7": 3},
        {"judge_id": "J2", "D1": 3, "D2": 3, "D3": 3, "D4": 3, "D5": 3, "D6": 2, "D7": 3}
      ]
    }
  ],
  "pairwise": [
    {"a": "SOP-A01", "b": "SOP-A02", "winner": "TIE", "judge_id": "P1", "dimension": "overall_document_quality"}
  ]
}
```

Allowed values:

- `mode`: `same_program` or `cross_program`
- `gate_status`: `PASS`, `REVISE`, `BLOCKED`, or `UNVERIFIED`
- dimension scores: integer 0-4
- pairwise winner: one of the two SOP IDs, `TIE`, or `INSUFFICIENT_EVIDENCE`

## 3. Aggregation output JSON

```json
{
  "mode": "same_program",
  "ranking_basis": "full_score",
  "weights": {"D1": 15, "D2": 20, "D3": 15, "D4": 15, "D5": 10, "D6": 15, "D7": 10},
  "near_score_threshold": 5.0,
  "results": [
    {
      "sop_id": "SOP-A01",
      "rankable": true,
      "gate_status": "PASS",
      "median_full_score": 73.12,
      "median_core_score": 72.79,
      "median_local_fit_score": 75.0,
      "judge_full_score_range": [68.75, 77.5],
      "judge_core_score_range": [67.65, 77.94],
      "max_dimension_disagreement": 1,
      "adjudication_dimensions": [],
      "pairwise_points": 0.5,
      "pairwise_comparisons": 1,
      "pairwise_record": {"wins": 0, "ties": 1, "losses": 0, "insufficient": 0},
      "tier": "Tier 1",
      "ranking_score": 73.12,
      "judge_ranking_score_range": [68.75, 77.5]
    }
  ],
  "near_score_pairs": [],
  "privacy_warnings": [],
  "limitations": [
    "Scores and tiers describe SOP document quality, not admission probability."
  ]
}
```

## 4. Batch Markdown table

```markdown
| Tier | SOP ID | Gate | Ranking score | Judge range | Core score | Local fit | Max disagreement | Pairwise | Status |
|---|---|---|---:|---|---:|---:|---:|---|---|
| Tier 1 | SOP-A01 | PASS | 84.4 | 82.5-86.3 | 85.1 | 79.2 | 1 | 1-0-1 | Rankable |
```

For cross-program comparison, label `Ranking score` as `Normalized core score` and never sort on the local-fit column.

## 5. Version comparison table

```markdown
| Dimension | Master | Version A | Delta A | Version B | Delta B | Drift note |
|---|---:|---:|---:|---:|---:|---|
| D1 Research Identity | 3 | 3 | 0 | 2 | -1 | Version B overfits faculty vocabulary. |
```

Also report factual drift, contribution drift, narrative-origin drift, future-agenda drift, and template leakage separately.
