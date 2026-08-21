# CS PhD Statement of Purpose Review Rubric

**Version:** 2.0

**Date:** 2026-08-20

**Primary use:** Research-oriented Computer Science PhD Statements of Purpose

**Compatible with:** `evaluate-phd-sop` evidence-first workflow
**Scoring scale:** Seven dimensions, each scored 0-4, weighted to 100 points

**Integration note:** This is the normative scoring reference for the `evaluate-cs-phd-sops` skill.

---

## 0. Purpose and boundaries

This rubric evaluates how effectively an SOP communicates a credible research identity, research readiness, intellectual development, future agenda, and authentic program fit.

It evaluates the **current document**, not the applicant's intrinsic ability and not the full admissions file.

### Main changes from v1

- separates `Future Research Agenda and Why PhD` from faculty fit;
- reduces the risk that school-specific fit overwhelms research readiness;
- adds confidence labels and explicit counter-evidence;
- adds score caps for common evidence failures;
- separates whole-application context from the 100-point SOP score;
- expands ownership, publication-status, and SOP/personal-statement gates;
- adds project-level and paragraph-level audit schemas;
- adds a direct source-to-rubric provenance map.

A score of `86/100` means:

> The current SOP satisfies most of this rubric's research-communication criteria.

It does **not** mean:

> The applicant has an 86% probability of admission.

Admission decisions also depend on recommendation letters, transcripts, publications, faculty capacity, funding, institutional priorities, applicant-pool strength, and year-specific circumstances. Berkeley's comprehensive-review guidance is especially important here: an SOP is one part of a contextual, holistic review and should not be used as a proxy for the whole application.

### What this rubric rewards

- a specific and stable research identity;
- evidence that the applicant understands open-ended research;
- clear ownership of collaborative work;
- causal intellectual development across projects;
- interpretation of evidence, including limitations or failed approaches;
- a reachable future research agenda and a credible reason for pursuing a PhD;
- problem-level faculty and program fit;
- compressed, accessible, applicant-specific writing.

### What this rubric does not reward by itself

- prestige;
- publication count;
- benchmark density;
- sophisticated vocabulary;
- long method lists;
- faculty names;
- personal hardship;
- childhood stories;
- confident tone unsupported by evidence.

---

# 1. Evidence authority

When sources conflict, use this order:

1. **Current program ground truth**
   - official prompt;
   - word or page limit;
   - current department instructions;
   - current faculty and lab information;
   - official program-specific rubric.
2. **Official university or faculty guidance**
   - department or graduate-school advice;
   - public admissions rubrics;
   - faculty-authored applicant guidance.
3. **Empirical admissions and genre research**
   - research on doctoral statements, gatekeeper judgments, disciplinary variation, and writer identity.
4. **Annotated examples and practitioner guidance**
   - useful for rhetorical patterns, never universal templates.
5. **Implementation references**
   - LLM evaluators, public scorecards, and generic websites.

Current official requirements always override this rubric.

---

# 2. Required inputs and uncertainty labels

## 2.1 Preferred inputs

```yaml
required:
  sop_text: true

strongly_preferred:
  official_program_prompt: true
  word_or_page_limit: true

preferred:
  target_program: true
  target_faculty: true
  current_faculty_or_lab_evidence: true
  cv_or_research_record: true
  applicant_evidence_bank: true
  master_sop: true
  comparison_versions: true
```

## 2.2 Confidence labels

Every dimension receives a score and a confidence label.

| Confidence | Meaning |
|---|---|
| `HIGH` | The SOP evidence is clear and relevant external claims were verified where needed. |
| `MEDIUM` | The SOP evidence is clear, but some program, faculty, or cross-document facts remain unverified. |
| `LOW` | Important inputs are missing or the score depends heavily on inference. |
| `UNSCORABLE` | The supplied material is insufficient to judge the dimension responsibly. |

Confidence describes the reliability of the rubric judgment, not confidence in admission.

---

# 3. Evaluation workflow

Use this order. Do not assign scores before identifying evidence.

1. Parse the official prompt and constraints.
2. Run all submission gates.
3. Map each paragraph to its dominant rhetorical function.
4. Audit each major research project using the project-evidence schema.
5. Write the applicant's one-sentence research identity.
6. Score D1-D7 using the smallest sufficient evidence spans.
7. Apply score caps and report counter-evidence.
8. Apply the non-scored holistic-context lens.
9. Report red flags separately.
10. Run the 30-second adversarial faculty read.
11. Identify the single highest-leverage bottleneck.
12. Recommend no more than three prioritized revisions by default.

---

# 4. Submission gates

Submission gates are non-compensatory. A high numerical score cannot erase a failed gate.

Use four statuses:

- `PASS`
- `REVISE`
- `BLOCKED`
- `UNVERIFIED`

## G1. Prompt and format compliance

Check:

- answers the actual prompt;
- covers every required topic;
- respects the word or page limit;
- follows naming, formatting, and faculty-reference instructions;
- does not include content assigned to a separate required essay.

`BLOCKED` if the draft materially violates explicit instructions.

## G2. Factual and publication integrity

Check:

- project facts;
- methods and datasets;
- numerical results;
- publication status;
- awards and affiliations;
- degree and employment facts.

Any substantive fabrication or knowingly misleading status claim is `BLOCKED`.

Use calibrated publication language:

- published;
- accepted;
- under review;
- submitted;
- in preparation;
- workshop paper;
- preprint.

Do not collapse these categories.

## G3. Ownership and claim calibration

Check whether the reader can distinguish:

```text
team objective
vs.
applicant contribution
vs.
team result
```

Flag vague collective claims such as "we developed" or "our system achieved" when the applicant's role is unclear.

- `REVISE` for ordinary ambiguity.
- `BLOCKED` when wording materially exaggerates ownership or leadership.

## G4. Faculty and program freshness

Verify:

- faculty member is currently at the institution;
- faculty can plausibly supervise in the target program;
- lab, center, or track still exists;
- cited paper or project is accurate;
- claimed research connection is current.

Use `UNVERIFIED` when verification was not possible. Use `BLOCKED` for a confirmed wrong institution, departed faculty member presented as current, or similarly material error.

## G5. Cross-document consistency

When a CV, evidence bank, or other application documents are available, compare:

- dates;
- roles;
- project names;
- metrics;
- publication status;
- contribution scope;
- chronology.

Minor wording differences are acceptable. Material contradiction or role inflation requires `REVISE` or `BLOCKED` depending on severity.

## G6. Template and document integrity

Check for:

- wrong school, professor, lab, or program;
- unresolved placeholders;
- copied comments or prompt text;
- duplicated paragraphs;
- corrupted extraction;
- severe grammar breakdown.

A wrong-school or wrong-faculty leak is normally `BLOCKED`.

## G7. SOP versus personal-statement boundary

When a program separates the academic SOP from a personal or diversity statement, verify that the SOP remains primarily academic and intellectual.

- Personal context may appear when it explains research direction, preparation, access to opportunity, or a required prompt.
- The SOP should not duplicate the separate personal statement.
- No applicant should be expected to disclose sensitive personal information to appear credible.

Ordinary boundary problems are `REVISE`; use `BLOCKED` only when they cause direct prompt noncompliance.

---

# 5. Scoring overview

Each dimension receives an integer raw score from 0 to 4.

```text
weighted_points = raw_score / 4 * dimension_weight
```

| Dimension | Weight |
|---|---:|
| D1. Research Identity and Question | 15 |
| D2. Research Readiness, Ownership, and Credibility | 20 |
| D3. Intellectual Trajectory | 15 |
| D4. Evidence to Insight and Research Judgment | 15 |
| D5. Future Research Agenda and Why PhD | 10 |
| D6. Faculty and Program Fit | 15 |
| D7. Writing, Structure, and Distinctiveness | 10 |
| **Total** | **100** |

## 5.1 Global anchor meaning

| Raw | Meaning |
|---:|---|
| `0` | Missing, contradictory, or actively harmful. |
| `1` | Superficial, generic, or weakly supported. |
| `2` | Competent and understandable, but incomplete or not yet persuasive. |
| `3` | Strong, specific, and evidence-grounded. |
| `4` | Exceptional and integrated across the essay. |

A `4` should be rare. Absence of an obvious flaw is not enough.

## 5.2 Dimension-separation rules

Avoid double counting:

| Question | Score primarily under |
|---|---|
| What problem defines this applicant? | D1 |
| What did the applicant personally do, and was the work credible? | D2 |
| Why did one project or question lead to the next? | D3 |
| What do the results, failures, or limitations mean? | D4 |
| What should be studied next, and why does it require PhD training? | D5 |
| Why is this specific environment the right next setting? | D6 |
| How effectively is all of this communicated? | D7 |

One sentence may support several dimensions, but the evaluator must explain the distinct inference made for each.

---

# 6. D1 - Research Identity and Question

**Weight: 15**

## Core question

> Can a faculty reader describe the applicant's research problem in one specific sentence without relying only on field labels?

## Evaluate

- central research problem or family of questions;
- why the problem matters scientifically or technically;
- conceptual coherence across projects;
- specificity without artificial over-narrowing;
- stability after faculty names and trendy keywords are removed.

## Positive signals

- identifies a concrete problem, mechanism, tension, or failure mode;
- distinguishes an application domain from the underlying research question;
- gives a reason the problem matters beyond generic impact;
- maintains a recognizable intellectual center across experiences;
- allows multiple plausible future questions without becoming topic soup.

## Behavioral anchors

### 0 - No research identity

The SOP is mainly biography, coursework, grades, achievements, or generic ambition. A meaningful research question cannot be stated.

### 1 - Topic labels

The SOP names areas such as AI, systems, HCI, security, agents, or multimodal learning but does not define the underlying problem.

### 2 - Identifiable direction

The direction is understandable, but the central question remains broad, unstable, or weakly connected to prior evidence.

### 3 - Clear problem-centered identity

A reader can state the applicant's research identity in one specific sentence, and the identity is supported by more than one part of the SOP.

### 4 - Generative intellectual identity

The central problem explains why multiple prior experiences belong together, supports a coherent future agenda, and remains recognizable across reasonable school-specific adaptations.

## Required tests

### One-sentence identity test

Complete:

> This applicant studies ______ because ______.

If the blank can only be filled with broad field names, score at most 2.

### Keyword-removal test

Remove fashionable terms such as `AI`, `LLM`, `agents`, `multimodal`, or `trustworthy`.

If the underlying question disappears, score at most 2.

### Faculty-deletion test

Remove the fit paragraph. If the applicant no longer has a coherent identity, score at most 2.

---

# 7. D2 - Research Readiness, Ownership, and Credibility

**Weight: 20**

## Core question

> Does the SOP show that the applicant can participate credibly in open-ended research, rather than merely execute assigned technical work?

## Evaluate

- understanding of the research problem and why it is difficult;
- applicant-specific role and ownership;
- methodological or design decisions;
- alternatives, tradeoffs, or diagnostic reasoning;
- validation strategy;
- calibrated claims;
- evidence of independence, initiative, or increasing responsibility.

Research readiness is not equivalent to publication count.

## Behavioral anchors

### 0 - No assessable research evidence

Little relevant work is described, or claims are too vague or contradictory to evaluate.

### 1 - CV prose or tool execution

The SOP lists projects, methods, datasets, publications, or metrics without showing the applicant's reasoning or role.

### 2 - Competent execution

The applicant explains the problem, method, and outcome, but ownership, design reasoning, validation, or independence remains incomplete.

### 3 - Strong developing researcher

The SOP clearly communicates the problem, applicant role, at least one meaningful design choice, evaluation, and what the applicant learned.

### 4 - Research maturity

The SOP additionally demonstrates tradeoff analysis, competing explanations, diagnostic experiments, failed approaches, limitation awareness, or independent question formation. Multiple spans make the reader trust the applicant in open-ended research.

## Score caps

- If the applicant's personal role is unclear across major projects, score at most 2.
- If validation or evidence is absent across major projects, score at most 2.
- A publication alone cannot raise the score above 2.
- A negative result can support a 3 or 4 when the reasoning is strong.

---

# 8. D3 - Intellectual Trajectory

**Weight: 15**

## Core question

> Do the applicant's experiences form a causal intellectual development, or merely a chronological sequence?

## Evaluate

- why one experience led to the next;
- how questions became more precise, difficult, or general;
- how failures or limitations changed the applicant's thinking;
- whether interdisciplinary movement has an explicit bridge;
- whether the future agenda feels earned.

## Behavioral anchors

### 0 - Fragmented

Projects appear unrelated, and no meaningful relationship is established.

### 1 - Chronological only

The essay says what happened next but not why the applicant's thinking changed.

### 2 - Thematic continuity

Projects share a field, method, or application, but transitions are mainly associative.

### 3 - Causal continuity

At least two important transitions show that an observation, limitation, or open question from one experience motivated the next.

### 4 - Compelling research evolution

The essay forms an integrated progression:

```text
observation -> investigation -> limitation -> deeper question -> future agenda
```

The trajectory explains both past choices and the proposed next stage.

## Transition test

For each major paragraph transition, ask:

> Why does paragraph N+1 logically follow paragraph N?

If the only answer is "because it happened later," score at most 1. If the answer is only "because it is in the same field," score at most 2.

---

# 9. D4 - Evidence to Insight and Research Judgment

**Weight: 15**

## Core question

> Does the applicant turn results into scientific or technical insight, or merely report achievements?

## Evaluate

- claim-evidence alignment;
- whether metrics have a clear inferential purpose;
- interpretation of positive, negative, or ambiguous results;
- recognition of limitations and alternative explanations;
- whether evidence generates better questions;
- claim calibration.

## Evidence chain

```text
claim
-> evidence
-> interpretation
-> limitation or implication
-> next question
```

An SOP does not need this full chain for every project, but repeated absence of interpretation lowers the score.

## Behavioral anchors

### 0 - Unsupported or misleading

Important claims lack evidence, contradict the record, or misrepresent what results establish.

### 1 - Achievement reporting

Metrics and outcomes appear, but the essay rarely explains what they mean.

### 2 - Evidence supports claims

The main claims are supported by appropriate evidence, but interpretation remains local or conventional.

### 3 - Evidence produces insight

The applicant explains what results imply, including meaningful limitations, unexpected behavior, or distinctions that affect the research question.

### 4 - Evidence generates research questions

Across multiple spans, evidence, controls, failures, or limitations lead to deeper questions and visibly shape the applicant's research trajectory.

## Required tests

### Metric-necessity test

For each number, ask:

> If this number disappeared, would the reader lose an important inference?

If no, compress or remove it.

### Alternative-explanation test

Ask whether the SOP distinguishes what the evidence shows from other plausible interpretations.

### Negative-result test

Negative results are not mandatory. When genuine and well interpreted, they are positive evidence of research judgment rather than a weakness.

---

# 10. D5 - Future Research Agenda and Why PhD

**Weight: 10**

## Core question

> Does the SOP present a reachable research agenda and explain why PhD training is the appropriate next step?

This dimension is separate from faculty fit. `What I want to study next` should be clear before `where I want to study it`.

## Evaluate

- future questions emerge from prior work;
- agenda is specific enough to be meaningful but open enough for doctoral exploration;
- explains why the next problems require sustained research training;
- distinguishes a PhD goal from another engineering role, coursework degree, or prestige goal;
- longer-term goals are coherent when included or required;
- acknowledges that research direction may evolve.

## Behavioral anchors

### 0 - Missing or contradictory purpose

No future agenda is given, or the stated agenda contradicts the applicant's evidence and goals.

### 1 - Generic PhD aspiration

The SOP says the applicant wants to advance knowledge, make impact, become an expert, or pursue a PhD without defining the research need.

### 2 - Plausible next direction

A future area or question is identifiable, but the bridge from prior work or the reason for PhD training remains underdeveloped.

### 3 - Earned agenda and credible PhD rationale

The future agenda grows naturally from prior evidence, and the SOP explains why sustained research mentorship, inquiry, or methodological development is needed.

### 4 - Generative and disciplined agenda

The SOP presents a focused family of questions that is both ambitious and reachable, identifies meaningful uncertainty rather than pretending to know the dissertation in advance, and makes the need for PhD training intellectually compelling.

## Score caps

- If there is no explicit or strongly inferable reason for pursuing a PhD, score at most 2.
- If the future direction is a sudden faculty-driven pivot, score at most 2.
- Career prestige, title, or university reputation cannot support a score above 1 by itself.

---

# 11. D6 - Faculty and Program Fit

**Weight: 15**

## Core question

> Why is this specific faculty and program environment a natural next setting for the applicant's existing trajectory?

## Fit ladder

### 0 - No fit or factual mismatch

Wrong, absent, or unrelated faculty/program information.

### 1 - Name-dropping or prestige fit

The SOP lists professors, labs, rankings, location, or reputation without an intellectual connection.

### 2 - Topic overlap

The applicant and faculty share a real area, but the relationship remains broad or interchangeable.

### 3 - Problem-level fit

The SOP connects the applicant's existing question to a specific faculty problem, method, or line of work and explains what the environment would enable.

### 4 - Bidirectional and non-performative fit

The SOP makes clear:

```text
what the applicant already brings
+
what the faculty or program uniquely enables
+
what new question becomes possible
```

The fit is specific without reconstructing the applicant's identity around the professor.

## Required tests

### Specificity test

Why this faculty member rather than any researcher in the same broad area?

### Substitution test

Replace the professor with another person in the subfield. If the paragraph still works almost unchanged, score at most 2.

### Bidirectionality test

Does the paragraph explain both what the applicant brings and what the environment enables?

### Overfitting test

Remove the faculty paragraph. If the rest of the SOP describes a different or incoherent researcher, score at most 2.

### Research-distance check

| Distance | Relationship | Interpretation |
|---:|---|---|
| 0 | nearly identical problem | direct fit |
| 1 | direct extension | strong bridge |
| 2 | adjacent question or method | explain bridge explicitly |
| 3 | substantial pivot | narrow claims and preserve identity |
| 4 | unrelated | do not force fit |

Distance 3 requires a warning. Distance 4 normally caps D6 at 1.

## Score caps

- If faculty facts are unverified, mark confidence `LOW` or `UNSCORABLE`; do not award 4.
- Names and paper titles without problem-level reasoning cap the score at 2.
- Program resources mentioned without explaining their research use cap the score at 2.

---

# 12. D7 - Writing, Structure, and Distinctiveness

**Weight: 10**

## Core question

> Is the SOP clear, compressed, technically accessible, applicant-specific, and easy for a faculty reader to navigate?

## Evaluate

- paragraph-level organization;
- active and calibrated wording;
- readable technical detail for adjacent-field faculty;
- sentence economy;
- transitions;
- applicant-specific intellectual voice;
- professional tone;
- balance between research detail and narrative purpose.

Do not reward ornate prose, vocabulary complexity, or metaphors by themselves.

## Behavioral anchors

### 0 - Comprehension obstructed

Grammar, structure, formatting, or technical opacity prevents reliable understanding.

### 1 - Generic or structurally weak

Readable in places, but dominated by clichés, repetition, disconnected paragraphs, template language, or uncontrolled detail.

### 2 - Clear but interchangeable

The essay is organized and understandable, yet overly CV-like, generic, repetitive, or lacking a recognizable intellectual fingerprint.

### 3 - Clear and applicant-specific

The writing is concise, technically credible, logically organized, and specific to this applicant's reasoning and trajectory.

### 4 - Memorable without theatrics

The prose is unusually efficient and coherent. A reader remembers the applicant through a precise intellectual pattern, not through decoration, gimmicks, or exaggerated claims.

## Required tests

### Paragraph-function test

Each paragraph should have one dominant intellectual job.

### Adjacent-field test

An informed CS faculty member outside the exact subfield should understand the problem, contribution, and importance.

### Distinctiveness test

Replace the main domain with another plausible domain. If most sentences still work with trivial substitutions, score at most 2.

### Compression test

Classify every sentence:

```yaml
sentence_function:
  - establishes_problem
  - provides_evidence
  - explains_role
  - explains_design_choice
  - interprets_result
  - creates_transition
  - defines_future_question
  - establishes_fit
  - required_context
  - redundant
```

Repeated `redundant` sentences lower the score.

---

# 13. Project-evidence audit

For every major research experience, complete:

```yaml
project:
  problem:
  why_it_matters:
  why_it_is_hard:
  team_goal:
  applicant_role:
  applicant_decisions:
  approach:
  alternatives_or_tradeoffs:
  validation:
  result:
  limitation_or_failure:
  interpretation:
  next_question:
```

Not every field must appear for every project. Across the SOP, repeated absence of `applicant_role`, `validation`, `interpretation`, or `next_question` should lower D2-D4.

### Mini-abstract rule

Stanford, MIT EECS examples, Harchol-Balter, and STEM-oriented writing guidance converge on a useful research-paragraph pattern:

```text
motivation/problem
-> applicant contribution
-> enough technical detail to establish credibility
-> outcome or evidence
-> learning, limitation, or next question
```

This is a diagnostic pattern, not a mandatory paragraph template.

---

# 14. Paragraph-function audit

Assign one dominant function to each paragraph:

```yaml
allowed_primary_functions:
  - research_identity_or_motivating_observation
  - research_experience
  - failure_limitation_or_diagnostic_reasoning
  - intellectual_transition
  - future_research_agenda
  - why_phd
  - faculty_program_fit
  - career_goal
  - required_context
```

Flag:

- paragraphs with several unrelated functions;
- a long opening that delays research identity;
- repeated project summaries with no transitions;
- fit content scattered before the applicant's own agenda is clear;
- a closing that adds no inference.

One effective research-heavy architecture is:

```text
P1  research identity and motivating problem
P2  first research experience and unresolved question
P3  deeper investigation, design choice, or limitation
P4  intellectual transition and broader research question
P5  future agenda and why PhD
P6  faculty/program fit and concise close
```

Do not penalize a strong alternative architecture.

---

# 15. Non-scored holistic-context lens

This lens is informed by Berkeley comprehensive review and the context-sensitive portions of Caltech, Cornell, and Colorado State rubrics.

It is **not** an adversity bonus and does not add points to the SOP score.

Use context to interpret opportunity and evidence responsibly:

- access to research opportunities;
- institution or lab resources;
- first-generation status when voluntarily supplied;
- employment or family responsibilities;
- international or educational transitions;
- nontraditional learning;
- disability or health context when voluntarily and relevantly supplied;
- leadership, outreach, teaching, and community contribution;
- persistence through research or educational constraints.

## Rules

1. Do not penalize applicants for omitting personal hardship or sensitive information.
2. Do not rank types of adversity.
3. Do not treat hardship as proof of research readiness.
4. Do not treat unequal access to publications or prestigious labs as lack of potential.
5. Research-specific persistence may support D2-D4 when the SOP shows concrete reasoning or action.
6. Leadership or outreach may support a required program prompt but cannot substitute for research evidence.
7. Report contextual interpretation separately from the 100-point SOP score.

Recommended output:

```yaml
holistic_context:
  supplied_by_applicant: true_or_false
  relevant_factors: []
  effect_on_interpretation: ""
  score_effect: none
```

---

# 16. Red-flag checker

Red flags are reported separately. Do not hide them inside unexplained point deductions.

## Critical red flags

- fabricated or materially misleading claim;
- wrong university, program, professor, or lab;
- false publication status;
- material ownership inflation;
- direct contradiction with supporting documents.

Critical red flags normally trigger a gate `BLOCKED`.

## Major red flags

| Code | Red flag | Main dimensions affected |
|---|---|---|
| R1 | CV prose without reasoning | D2, D4, D7 |
| R2 | Topic soup or keyword identity | D1, D7 |
| R3 | Method shopping list | D2, D7 |
| R4 | Metric overload without inference | D4, D7 |
| R5 | Applicant role hidden behind `we` | D2, G3 |
| R6 | Unsupported future leap | D3, D5 |
| R7 | Professor name-dropping or flattery | D6 |
| R8 | Faculty mimicry or identity reconstruction | D1, D5, D6 |
| R9 | Excessive technical density | D7 |
| R10 | Research-proposal cosplay: ambitious future claims without prior bridge | D1, D5 |
| R11 | Generic passion or impact claims | D1, D5, D7 |
| R12 | Grade, award, or resume regurgitation | D2, D7 |
| R13 | Excessive autobiography or childhood origin | D1, D7, G7 |
| R14 | Defensive excuse without relevant context or agency | D7, context lens |
| R15 | SOP duplicates a separate personal statement | G7, D7 |
| R16 | Claim inflation: `solved`, `proved`, `led`, `developed` beyond evidence | D2, D4, G2-G3 |
| R17 | Generic closing based on prestige or enthusiasm | D6, D7 |
| R18 | Outdated faculty or program claim | G4, D6 |

Red flags do not have universal fixed deductions. Severity depends on extent, location, and whether the problem changes the reader's core inference.

---

# 17. Evidence-span scoring protocol

For each dimension, record:

```yaml
dimension:
raw_score: 0_to_4_integer
weight:
weighted_score:
confidence: HIGH_MEDIUM_LOW_UNSCORABLE
evidence_spans:
  - exact_smallest_sufficient_quote
counter_evidence:
  - exact_quote_or_missing_pattern
strength:
missing_for_next_level:
score_cap_applied:
```

## Evidence rules

1. Quote the smallest sufficient span.
2. Separate quoted evidence from evaluator interpretation.
3. Whole-essay scores of 3 or 4 normally require evidence from multiple locations.
4. Do not infer applicant ownership beyond the SOP and supporting records.
5. Do not infer research maturity from sophisticated wording.
6. Record counter-evidence before finalizing a high score.
7. Apply score caps before computing the total.
8. Do not use fractional raw scores for one judge.
9. Fractional raw scores are allowed only after aggregating independent judges.

---

# 18. Scoring and internal status

## 18.1 Calculation example

```text
D1 = 3/4 * 15 = 11.25
D2 = 4/4 * 20 = 20.00
D3 = 3/4 * 15 = 11.25
D4 = 3/4 * 15 = 11.25
D5 = 2/4 * 10 = 5.00
D6 = 3/4 * 15 = 11.25
D7 = 3/4 * 10 = 7.50

Total = 77.50/100
```

## 18.2 Internal quality bands

These labels are revision states, not admission probabilities.

| Score | Internal status |
|---:|---|
| 0-59 | `REBUILD` |
| 60-69 | `MAJOR_REVISION` |
| 70-81 | `REVISION_REQUIRED` |
| 82-89 | `STRONG_DRAFT` |
| 90-100 | `FINAL_REVIEW_CANDIDATE` |

Overrides:

- Any `BLOCKED` gate prevents `STRONG_DRAFT` or `FINAL_REVIEW_CANDIDATE` status.
- Any `UNVERIFIED` faculty gate makes D6 provisional.
- A total above 90 should be rare and requires no major score cap.

---

# 19. Adversarial 30-second faculty read

After scoring, answer without rereading the CV:

1. What do I remember about this applicant after 30 seconds?
2. What research problem do they appear to care about?
3. What is the strongest evidence that they can conduct research?
4. What did they personally contribute?
5. Why do their projects belong in one trajectory?
6. What result, failure, or limitation changed their thinking?
7. What do they want to study next?
8. Why does that next step require PhD training?
9. Why this faculty or program specifically?
10. What is the largest unresolved concern?
11. Would I continue reading, discuss the file, or advocate for the applicant based on the SOP's communication quality? Why?

The last answer is a diagnostic judgment about the SOP, not an admissions recommendation.

---

# 20. Revision prioritization

Identify one main bottleneck based on leverage, not merely the lowest score.

Example:

> D3 may be the bottleneck even if D5 is numerically lower, because clarifying trajectory would also strengthen research identity, evidence interpretation, and the future agenda.

Give no more than three revisions by default. Each revision must contain:

```yaml
priority:
problem:
why_it_matters:
target_location:
revision_goal:
evidence_of_success:
do_not_change:
```

Do not rewrite the SOP unless explicitly requested. Diagnosis should precede rewriting.

---

# 21. Human-readable evaluation template

```markdown
# CS PhD SOP Evaluation

## Evaluation Scope

- Program:
- Degree:
- Prompt:
- Limit:
- Faculty named:
- External materials supplied:
- Provisional judgments:

## Submission Gates

| Gate | Status | Evidence / Reason |
|---|---|---|
| G1 Prompt and format | PASS | |
| G2 Factual integrity | PASS | |
| G3 Ownership and claims | PASS | |
| G4 Faculty freshness | UNVERIFIED | |
| G5 Cross-document consistency | UNVERIFIED | |
| G6 Template integrity | PASS | |
| G7 SOP/PS boundary | PASS | |

## One-Sentence Research Identity

> This applicant studies ... because ...

## Score

| Dimension | Raw | Weighted | Confidence | Key evidence | Missing for next level |
|---|---:|---:|---|---|---|
| D1 Research Identity | /4 | /15 | | | |
| D2 Research Readiness | /4 | /20 | | | |
| D3 Intellectual Trajectory | /4 | /15 | | | |
| D4 Evidence to Insight | /4 | /15 | | | |
| D5 Future Agenda and Why PhD | /4 | /10 | | | |
| D6 Faculty and Program Fit | /4 | /15 | | | |
| D7 Writing and Structure | /4 | /10 | | | |
| **Total** | | **/100** | | | |

**Internal status:**

## Project-Evidence Audit

| Project | Problem | Applicant role | Choice/reasoning | Validation | Insight/limitation | Next question |
|---|---|---|---|---|---|---|

## Paragraph-Function Audit

| Paragraph | Dominant function | Works? | Main issue |
|---:|---|---|---|

## Holistic Context Lens

- Context voluntarily supplied:
- Effect on interpretation:
- Score effect: none

## Strongest Feature

## Main Bottleneck

## Red Flags

## Top 3 Revisions

### 1.
- Problem:
- Why it matters:
- Target location:
- Revision goal:
- Evidence of success:
- Do not change:

## Faculty Overfitting Check

## Adversarial 30-Second Read
```

---

# 22. Version comparison and faculty adaptation

When comparing a master SOP with school-specific versions, preserve:

```text
core research identity       highly stable
completed project facts      immutable
applicant contributions      immutable
metrics/publication status   immutable
intellectual origin          highly stable
```

Allow controlled change in:

```text
project emphasis             flexible
future subquestion           moderately flexible
faculty and program bridge   flexible
```

Track:

- factual drift;
- contribution inflation;
- research-identity drift;
- narrative-origin drift;
- future-agenda drift;
- faculty-vocabulary mimicry;
- school-name or faculty leakage.

Recommended research-identity drift scale:

| Drift | Meaning |
|---:|---|
| 0 | Same meaning and emphasis. |
| 1 | Same identity, different emphasis. |
| 2 | Adjacent reframing; explain bridge. |
| 3 | Substantial pivot; warning required. |
| 4 | Different researcher identity. |

Target: 0-1. A score of 2 requires explanation. Scores of 3-4 normally indicate overfitting.

---

# 23. Multi-judge reliability

For high-stakes use, run at least two independent evidence-first passes.

Recommended roles:

- **Research judge:** D1-D5, SOP plus applicant evidence.
- **Fit judge:** G4 and D6, SOP plus current official faculty evidence.
- **Writing judge:** D7, SOP only where possible.
- **Consistency judge:** G2-G5 and version drift, all supplied documents.

Adjudicate any dimension where independent raw scores differ by 2 or more.

The adjudicator must answer:

1. What evidence did each judge use?
2. Which behavioral anchor is actually supported?
3. Did missing information cause the disagreement?
4. Is a score cap applicable?
5. Is the rubric wording ambiguous?

Do not average away a major disagreement without explanation.

---

# 24. Calibration and validation plan

Treat this rubric as a working diagnostic instrument, not a validated admissions model.

## Stage 1 - Internal calibration

Score:

- weak synthetic SOPs;
- competent SOPs;
- strong anonymized SOPs;
- multiple revisions of the same SOP.

Check whether ordering matches expert judgment and whether revision direction is sensible.

## Stage 2 - Faculty and mentor annotation

Ask experienced reviewers to score independently. Measure:

- dimension agreement;
- recurring disagreements;
- which dimensions drive `continue reading`, `discuss`, or `advocate` judgments;
- whether evaluators use context consistently.

## Stage 3 - Pairwise preference

Ask:

> Which of Draft A and Draft B better demonstrates research readiness, and what evidence changes your judgment?

Pairwise judgments are often more stable than absolute scores.

## Stage 4 - Outcome data, with caution

Admission outcomes are confounded by faculty capacity, funding, letters, record, competition, institution, and year. Do not convert SOP scores into admission probabilities.

---

# 25. Source synthesis

The v2 changes are grounded in the public sources summarized below. Local copies of source PDFs are not distributed with this skill; use the official links and verify current program instructions before evaluation.

| Source | Contribution to this rubric | Caution |
|---|---|---|
| Stanford, *General Advice for CS PhD Applicants* | Research-story structure; personal contribution; project motivation; learning from challenges; school-specific fit; compression. | Student-authored guidance, not a universal program rule. |
| MIT EECS annotated CS examples 1 and 3 | Problem-contribution-outcome pattern; concrete evidence; outreach when relevant; future work; program fit. | Successful examples are not causal proof and should not become templates. |
| Cornell, *Writing Your Academic Statement of Purpose* | Academic preparation; specific examples; informed program decision; faculty fit; active tone; final checklist. | General academic guidance, not CS-specific scoring. |
| Harvard Griffin GSAS perspectives guide | Research questions; intellectual turning points; intellectual profile; separation of SOP and personal statement. | The SOP guidance is concentrated in one section of a broader brochure. |
| Mor Harchol-Balter, *Applying to Ph.D. Programs in Computer Science* | Research statement framing; what was found and learned; failed approaches as valid evidence; why PhD; why program; research readiness. | Archival, last updated 2003; administrative, GRE, ranking, and contact advice is outdated. |
| Caltech GPS admissions rubric | Motivation; research goals; prior experience; writing; faculty/program alignment; perseverance. | STEM but not CS-specific; archival. |
| Cornell Communication PhD admissions rubric | Academic potential; originality; research experience; writing; motivation; perseverance; field and faculty fit. | Communication-field criteria require CS calibration. |
| Berkeley comprehensive-review guidance | Holistic review; context of achievement; no single-metric admissions inference. | Whole-application guidance, not an SOP rubric. |
| Colorado State comprehensive-review template | Explicit behavioral anchors; scholarly potential; alignment; long-term goals; perseverance; self-appraisal. | Whole-application and non-CS; do not transplant categories, weights, bonuses, or total score. |
| Appleby and Appleby, *Kisses of Death* | Negative-control categories: poor writing, weak program knowledge, inappropriate presentation, damaging claims. | Psychology-specific and dated; never generalize uncritically or penalize sensitive disclosure automatically. |

### Important web-based CS/faculty sources retained in the bundle index

- MIT EECS Communication Lab SOP guide;
- MIT EECS faculty perspectives on application essays;
- CMU Jonathan Aldrich SOP advice;
- CMU Andy Pavlo negative-control advice;
- Cornell Adrian Sampson SOP critique;
- UC Berkeley statement guidance;
- UPenn STEM research-in-SOP guidance;
- Jason Eisner's prospective CS graduate-student guidance.

---

# 26. Minimal evaluator prompt

```text
Evaluate this research-oriented CS PhD SOP using
cs_phd_sop_review_rubric_v2.md.

Protocol:
1. Parse the current official prompt and limit.
2. Run G1-G7 before scoring.
3. Identify evidence spans before assigning scores.
4. Map paragraphs and audit major research projects.
5. Write the one-sentence research identity.
6. Score D1-D7 with integer 0-4 anchors and apply score caps.
7. Report confidence and counter-evidence for each dimension.
8. Compute the weighted total out of 100.
9. Do not interpret the total as admission probability.
10. Apply the holistic-context lens separately with no score bonus.
11. Report red flags explicitly.
12. Run the adversarial 30-second faculty read.
13. Identify one main bottleneck and at most three revisions.
14. Do not rewrite unless explicitly requested.
15. Mark faculty fit provisional when current facts are not verified.
16. When multiple versions exist, run the drift check.
```

---

# 27. Final principle

Optimize for:

> credible research identity + demonstrated research reasoning + causal trajectory + evidence-derived insight + an earned future agenda + authentic fit + clear writing

Do not optimize for:

> prestige signaling + keyword matching + benchmark density + professor imitation + ornamental prose + adversity performance

A strong school-specific SOP should feel like:

> the same researcher viewed from the most relevant angle

not:

> a different researcher reconstructed for every professor.
