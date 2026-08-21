# CS PhD SOP Evaluator

An installable Codex skill for evidence-grounded review, comparison, and ranking of research-oriented Computer Science PhD Statements of Purpose.

The skill evaluates SOP communication quality—not applicant worth, research potential outside the submitted text, admission probability, or an admit/reject outcome.

## What it provides

- A 100-point rubric with seven behaviorally anchored dimensions.
- Non-compensatory gates for prompt compliance, factual integrity, ownership, faculty freshness, cross-document consistency, template integrity, and SOP/personal-statement boundaries.
- Single-draft review, targeted review, version comparison, same-program ranking, and cross-program comparison.
- Evidence spans, counter-evidence, score caps, confidence labels, red flags, and prioritized revision guidance.
- A privacy-aware deterministic script for multi-judge aggregation, disagreement detection, near-score review, and provisional tiers.

For cross-program comparison, the ranking score excludes program-specific fit (D6). Local fit remains visible as a separate score.

## Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── batch-ranking-protocol.md
│   ├── output-schemas.md
│   └── sop-evaluation-rubric.md
└── scripts/
    └── aggregate_scores.py
```

`SKILL.md` is the routing layer. Detailed scoring anchors and procedures live in `references/` so they are loaded only when relevant.

## Install

Install from this repository using the Codex skill installer, or copy the repository into your local skills directory. The required skill entry point is `SKILL.md`; optional references, scripts, and agent metadata are bundled alongside it.

Official skill format and installation guidance: [Build skills](https://learn.chatgpt.com/docs/build-skills).

Invoke the installed skill with:

```text
$evaluate-cs-phd-sops
```

Example request:

```text
Use $evaluate-cs-phd-sops to score these three anonymized SOP drafts independently,
then compare them for the same CS PhD program using two judge passes and rank tiers.
```

## Deterministic aggregation

The aggregation script accepts anonymous IDs and rubric scores only. It does not ingest or persist SOP or CV text.

```bash
python3 scripts/aggregate_scores.py scores.json --strict-privacy
```

Input and output formats are documented in `references/output-schemas.md`. Run its built-in checks with:

```bash
python3 scripts/aggregate_scores.py --self-test
```

## Privacy and source note

Use anonymous `sop_id` and `judge_id` values in aggregation files. Do not include names, contact details, student IDs, local paths, SOP text, or CV content.

The rubric synthesizes publicly available university guidance and research literature. Source provenance is listed in the rubric. Local source PDFs and potentially copyrighted guide files are not redistributed in this repository.
