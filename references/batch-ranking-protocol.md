# Batch Ranking Protocol for CS PhD SOPs

Use this protocol for comparing versions or ranking multiple SOP documents. It supplements the core rubric and does not replace its evidence requirements.

## 1. Define the comparison universe

Choose exactly one mode.

### Same-program batch

Use when every SOP answers the same prompt, limit, degree, and program context.

- Rank on the complete D1-D7 weighted total out of 100.
- D6 faculty/program fit is directly comparable only after current facts are verified consistently.

### Cross-program comparison

Use when prompts, institutions, or faculty contexts differ.

- Do not rank on the complete total.
- Rank on the normalized core document score:

```text
core dimensions = D1 + D2 + D3 + D4 + D5 + D7
core maximum = 85
normalized core score = core weighted points / 85 * 100
```

- Report D6 as a separate local-fit score:

```text
local fit score = D6 raw / 4 * 100
```

- Report prompt compliance separately. A difficult or unusual prompt is not evidence of weaker document quality.

### Version comparison

Use for drafts from the same applicant.

- Compare score deltas and evidence changes.
- Do not treat the versions as independent applicants.
- Check factual, contribution, identity, narrative-origin, future-agenda, and faculty-vocabulary drift.

## 2. Prepare documents

1. Assign anonymous IDs such as `SOP-A01`.
2. Remove names and direct contact information from batch score files.
3. Preserve the actual SOP text for the qualitative judges, but do not send it to the aggregation script.
4. Record each prompt and limit.
5. Randomize or rotate review order when practical.
6. Apply the same extraction and formatting process to every document.

Do not remove information that is substantively required to evaluate research ownership, chronology, or program fit.

## 3. Independent first-pass scoring

Each judge must evaluate one SOP at a time before seeing batch totals.

Required per-SOP record:

```yaml
sop_id:
judge_id:
mode: same_program_or_cross_program
gates:
  G1: PASS_REVISE_BLOCKED_UNVERIFIED
  G2: PASS_REVISE_BLOCKED_UNVERIFIED
  G3: PASS_REVISE_BLOCKED_UNVERIFIED
  G4: PASS_REVISE_BLOCKED_UNVERIFIED
  G5: PASS_REVISE_BLOCKED_UNVERIFIED
  G6: PASS_REVISE_BLOCKED_UNVERIFIED
  G7: PASS_REVISE_BLOCKED_UNVERIFIED
scores:
  D1: 0_to_4_integer
  D2: 0_to_4_integer
  D3: 0_to_4_integer
  D4: 0_to_4_integer
  D5: 0_to_4_integer
  D6: 0_to_4_integer
  D7: 0_to_4_integer
confidence:
  D1: HIGH_MEDIUM_LOW_UNSCORABLE
  D2: HIGH_MEDIUM_LOW_UNSCORABLE
  D3: HIGH_MEDIUM_LOW_UNSCORABLE
  D4: HIGH_MEDIUM_LOW_UNSCORABLE
  D5: HIGH_MEDIUM_LOW_UNSCORABLE
  D6: HIGH_MEDIUM_LOW_UNSCORABLE
  D7: HIGH_MEDIUM_LOW_UNSCORABLE
evidence_spans:
counter_evidence:
red_flags:
main_bottleneck:
```

## 4. Minimum judge design

For consequential ranking, use at least two independent passes.

Recommended roles:

- research-content judge: D1-D5;
- fit judge: G4 and D6 with current program evidence;
- writing judge: D7 with the SOP only where practical;
- consistency judge: G2-G5 and version drift when supporting records exist.

One evaluator may fill more than one role, but scores should still be produced independently before aggregation.

## 5. Judge disagreement

For each dimension:

- difference 0-1: ordinarily aggregate;
- difference 2 or more: adjudication required;
- `UNSCORABLE` versus a numeric score: resolve missing-input assumptions before aggregation;
- disagreement caused by unverified faculty facts: mark D6 provisional rather than averaging.

Adjudication must answer:

1. Which evidence spans did each judge use?
2. Which behavioral anchor is directly supported?
3. Is a score cap applicable?
4. Is the disagreement caused by missing external information?
5. Should the result remain a range or tie rather than a single score?

## 6. Deterministic aggregation

Use `scripts/aggregate_scores.py`.

For each SOP, the script calculates:

- each judge's weighted total;
- median full score;
- median normalized core score;
- median local-fit score;
- judge range and maximum raw-dimension disagreement;
- gate-derived rankability;
- near-score pairs requiring pairwise review;
- rank tiers.

Use the median because a small panel is sensitive to one unusually generous or strict judge. Do not hide the full range.

## 7. Pairwise adjudication for close SOPs

Default trigger:

- score difference at or below 5 points; or
- overlapping judge score ranges; or
- a high-leverage dimension differs by 2 or more; or
- the documents appear qualitatively different despite nearly identical totals.

Pairwise reviewers should not ask "Which applicant is better?"

Ask one focused question at a time:

- Which SOP more clearly demonstrates research readiness, and what evidence changes the judgment?
- Which SOP presents the more causal intellectual trajectory?
- Which SOP turns evidence into stronger research insight?
- Which SOP gives the more earned future agenda and PhD rationale?
- In a same-program batch, which SOP demonstrates more specific and authentic program fit?

Allowed outcomes:

- `A`
- `B`
- `TIE`
- `INSUFFICIENT_EVIDENCE`

Each outcome requires evidence from both documents. A tie is valid and should not be broken for cosmetic reasons.

## 8. Rank tiers

Prefer tiers over unsupported exact positions.

Recommended tier logic:

- documents within the near-score threshold begin in the same provisional cluster;
- pairwise evidence may separate documents within that cluster;
- unresolved or contradictory pairwise results remain tied;
- blocked documents receive `BLOCKED`, not a numeric rank;
- documents with material unverified inputs receive `PROVISIONAL` status.

Do not label tiers with admissions language such as `admit`, `waitlist`, or `reject`.

Suggested neutral labels:

- `Tier 1`
- `Tier 2`
- `Tier 3`
- `Provisional`
- `Blocked`

## 9. Fairness and scope controls

- Rank SOP communication quality, not applicant worth.
- Do not score institutional prestige.
- Do not turn publication count into research-readiness points without textual evidence of reasoning.
- Do not add adversity points or require sensitive disclosure.
- Use holistic context only to interpret opportunity and evidence, never as a mechanical bonus.
- Do not compare complete scores across materially different prompts.
- Do not infer missing research ownership, results, or faculty facts.
- Do not convert ranks or scores into admission probabilities.

## 10. Required batch output

Report:

1. comparison mode and universe;
2. prompt and verification differences;
3. gate summary;
4. score table with medians, ranges, and confidence;
5. normalized core and local-fit scores when cross-program;
6. dimensions requiring adjudication;
7. near-score pairs and pairwise outcomes;
8. rank tiers;
9. one distinguishing strength and one bottleneck per SOP;
10. limitations of the ranking.

Never return only a sorted list of names or IDs without the evidence and uncertainty that produced it.
