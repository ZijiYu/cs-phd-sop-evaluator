---
name: evaluate-cs-phd-sops
description: Evaluate, compare, score, and rank research-oriented CS PhD Statements of Purpose with evidence-grounded behavioral anchors. Use for a single SOP critique, targeted dimension review, before/after or school-version comparison, same-program batch ranking, cross-program document-quality comparison, red-flag checks, faculty-fit analysis, or machine-readable scoring. Rank SOP documents, not applicants, and never interpret scores as admission probabilities.
---

# Evaluate CS PhD SOPs

Evaluate research-oriented CS PhD SOPs using evidence spans, non-compensatory submission gates, seven 0-4 dimensions, and calibrated comparison rules.

## Select the mode

- **Single evaluation:** one SOP, full diagnosis and 100-point score.
- **Targeted evaluation:** one or more named dimensions; run directly relevant gates.
- **Version comparison:** drafts from the same applicant; report score deltas and identity, contribution, agenda, and faculty-fit drift.
- **Same-program batch ranking:** SOPs answering the same prompt for the same program; compare the full 100-point score.
- **Cross-program comparison:** SOPs written for different prompts or schools; rank only the normalized core document score and report local fit separately.
- **Pipeline output:** return the machine-readable schema.

## Load references

- For any scored review, read [references/sop-evaluation-rubric.md](references/sop-evaluation-rubric.md). For a targeted review, read the purpose, gates, evidence protocol, requested dimensions, and output sections.
- For version or batch comparison, also read [references/batch-ranking-protocol.md](references/batch-ranking-protocol.md).
- For JSON, multi-SOP tables, or deterministic aggregation, read [references/output-schemas.md](references/output-schemas.md).
- Use [scripts/aggregate_scores.py](scripts/aggregate_scores.py) to aggregate judge scores, normalize cross-program core scores, detect near-score pairs, and create rank tiers. Do not calculate these mechanically by hand when the script is available.

## Gather and qualify inputs

Require SOP text. Use the following when supplied:

- current official program prompt and limit;
- target program and faculty;
- current official faculty or lab evidence;
- CV, evidence bank, or research record;
- master SOP and comparison versions;
- anonymous `sop_id` values for batch work.

Continue when optional inputs are missing, but mark the affected gates or dimensions `UNVERIFIED`, `LOW`, or `UNSCORABLE`. Never invent applicant, faculty, or program facts.

## Evaluate one SOP

1. Parse prompt constraints.
2. Run G1-G7 before scoring.
3. Map paragraph functions and audit major research projects.
4. Identify the smallest sufficient evidence spans before assigning scores.
5. Write the one-sentence research identity.
6. Score D1-D7 with integer raw scores from 0 to 4 and apply score caps.
7. Report confidence, counter-evidence, and red flags explicitly.
8. Compute the weighted total out of 100.
9. Apply holistic context separately with no score bonus.
10. Run the adversarial 30-second faculty read.
11. Identify one main bottleneck and at most three prioritized revisions.

Do not rewrite unless explicitly requested. If rewriting is requested, complete the evidence-based diagnosis first and preserve verified facts and ownership boundaries.

## Compare or rank multiple SOPs

Follow the batch protocol exactly.

Core invariants:

- blind or randomize document order when practical;
- score each SOP independently before viewing the leaderboard;
- use anonymous IDs in aggregation files;
- compare full scores only under the same program and prompt;
- for cross-program comparison, exclude D6 from the ranking score and report D6 separately;
- use at least two independent judge passes when the ranking is consequential;
- adjudicate a raw-score disagreement of 2 or more;
- run pairwise review for close documents instead of forcing precision;
- return tiers when evidence does not support a strict order;
- keep blocked documents outside the ranked set until corrected.

The output ranks **SOP communication quality**, not applicant worth, research potential outside the text, or likelihood of admission.

## Calibrate judgments

- Evidence before score; never choose a score and search for support afterward.
- A raw 4 is rare and requires integrated, multi-span evidence.
- Publications, metrics, polished prose, jargon, faculty names, and prestige do not earn high scores by themselves.
- Negative or null results can strengthen research-readiness and insight scores when interpreted well.
- Penalize contradictions and claim inflation more heavily than ordinary style weakness.
- Do not reward or require sensitive disclosure, hardship, or adversity.
- Treat current official program requirements as higher authority than the rubric.
- Never present a score, tier, or ranking as admission probability or an admit/reject decision.

## Privacy

- Use anonymous `sop_id` values in ranking inputs and outputs.
- Do not copy names, email addresses, phone numbers, student IDs, or other identifiers into aggregation files.
- Quote only the smallest evidence span required for a judgment.
- Do not persist SOP text or CV content in scripts; the aggregation script accepts scores and anonymous IDs only.

## Default output

For one SOP, return:

- evaluation scope and provisional judgments;
- G1-G7 table;
- one-sentence research identity;
- D1-D7 score table with evidence and confidence;
- project and paragraph audits when useful;
- holistic-context note;
- strongest feature and main bottleneck;
- red flags;
- top three revisions;
- faculty-overfitting check;
- adversarial faculty read.

For a batch, return:

- comparison universe and ranking mode;
- gate summary;
- full or normalized core score as appropriate;
- local fit score separately for cross-program work;
- judge disagreement and confidence;
- near-score pairs and pairwise outcomes;
- rank tiers, not unsupported exact positions;
- one distinguishing strength and bottleneck per SOP.
