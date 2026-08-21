# CS PhD SOP Evaluator

**English** | [简体中文](README.zh-CN.md)

An installable Codex skill for evidence-based evaluation, comparison, and ranking of research-oriented Computer Science PhD Statements of Purpose.

> This skill evaluates SOP document quality. It does not rank applicants, predict admission probability, or make admit/reject decisions.

## Features

- A 100-point rubric with seven behaviorally anchored dimensions
- Submission gates for prompt compliance, factual integrity, research ownership, faculty freshness, consistency, and template leakage
- Single-SOP review, targeted review, version comparison, same-program ranking, and cross-program comparison
- Anonymous multi-judge aggregation, disagreement detection, close-score review, and provisional tiers
- Separate reporting of program fit (D6) in cross-program comparisons

## Install and use

Install this repository with the Codex Skill Installer, or copy it into your local skills directory. Then invoke:

```text
$evaluate-cs-phd-sops
```

Aggregate anonymous batch scores with:

```bash
python3 scripts/aggregate_scores.py scores.json --strict-privacy
```

Aggregation files should contain anonymous IDs and scores only; never names, contact details, SOP text, or CV content.

## Evidence base and provenance

The rubric synthesizes official university guidance, CS faculty advice, annotated MIT EECS examples, public admissions rubrics, and peer-reviewed negative-control research. The repository includes **10 PDFs and 1 XLSX** under [`source_materials/`](source_materials/), totaling about 11.4 MB.

Source pages below were checked on **August 21, 2026**. Current program prompts, limits, faculty availability, and official admissions instructions always take precedence.

### SOP guides and CS faculty guidance

1. **[Stanford - General Advice for CS PhD Applicants](source_materials/sop_guides/Stanford_General_Advice_for_CS_PhD_Applicants.pdf)**
   - **Origin:** [Stanford Computer Science public PDF](https://www.cs.stanford.edu/sites/g/files/sbiybj28076/files/media/file/general-advice-for-cs-phd-applicants.pdf).
   - **Contribution:** Research-story structure, clear individual contribution, project motivation, lessons from challenges, school-specific fit, and compression.
   - **Limitation:** Student-authored guidance rather than an official admissions scoring rule.

2. **[Cornell - Writing Your Academic Statement of Purpose](source_materials/sop_guides/Cornell_Writing_Academic_Statement_of_Purpose.pdf)**
   - **Origin:** [Cornell Graduate School official guide](https://gradschool.cornell.edu/inclusion/recruitment/prospective-students/writing-your-statement-of-purpose/); PDF metadata credits Anitra M. Douglas-McCarthy and shows a 2026 revision.
   - **Contribution:** Academic preparation, concrete examples, informed program choice, faculty alignment, active writing, and a final quality checklist.
   - **Limitation:** General graduate-school guidance; CS-specific ownership and technical-evidence standards are added by this skill.

3. **[Harvard Griffin GSAS - Perspectives Guide](source_materials/sop_guides/06_Harvard_GSAS_Perspectives_SOP_Guide.pdf)**
   - **Origin:** Harvard Griffin Graduate School of Arts and Sciences, *Perspectives: Application and Student Life Resources*; PDF metadata dates the brochure to 2024. See the [current official application portal](https://gsas.harvard.edu/apply).
   - **Contribution:** Research questions, intellectual turning points, intellectual profile, and the distinction between a statement of purpose and a personal statement.
   - **Limitation:** The relevant SOP guidance is concentrated on page 6 of a broader applicant-resource brochure.

4. **[Mor Harchol-Balter - Applying to Ph.D. Programs in Computer Science](source_materials/sop_guides/09_Harchol_Balter_Applying_to_PhD_Programs_in_CS.pdf)**
   - **Origin:** Mor Harchol-Balter, Carnegie Mellon University School of Computer Science, [official faculty-hosted PDF](https://www.cs.cmu.edu/~harchol/gradschooltalk.pdf), last updated in 2003.
   - **Contribution:** Research readiness, findings and lessons, failed approaches as valid evidence, why a PhD, and faculty/program fit.
   - **Limitation:** Research and SOP principles remain useful, but GRE, ranking, contact, and administrative advice is outdated.

### Annotated CS SOP examples

5. **[MIT EECS Annotated SOP Example 1](source_materials/annotated_examples/MIT_EECS_Annotated_SOP_Example_1_CS.pdf)**
   - **Origin:** MIT EECS Communication Lab, [official Annotated Example 1](https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2016/09/CS-grad-school-personal-statement-annotated-example.pdf), linked from the [MIT CommKit SOP guide](https://mitcommlab.mit.edu/eecs/commkit/graduate-school-statement-of-purpose/).
   - **Contribution:** Problem-contribution-outcome structure, technical specificity, applicant ownership, quantitative evidence, future work, and program fit.
   - **Limitation:** A successful example is illustrative, not causal evidence of admission and not a template to imitate.

6. **[MIT EECS Annotated SOP Example 3](source_materials/annotated_examples/MIT_EECS_Annotated_SOP_Example_3_CS.pdf)**
   - **Origin:** MIT EECS Communication Lab, [official Annotated Example 3](https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2016/09/CS-grad-school-personal-statement-annotated-example-2.pdf), linked from the [MIT CommKit SOP guide](https://mitcommlab.mit.edu/eecs/commkit/graduate-school-statement-of-purpose/).
   - **Contribution:** Intellectual trajectory, breadth-to-focus transitions, interpreted research evidence, teaching/outreach evidence, future agenda, and program fit.
   - **Limitation:** A successful example is illustrative, not causal evidence of admission and not a universal writing model.

### Admissions rubrics and holistic-review sources

7. **[Caltech GPS Graduate Admissions Rubric](source_materials/admissions_rubrics/Caltech_GPS_Admissions_Rubric.pdf)**
   - **Origin:** Caltech Division of Geological and Planetary Sciences, [official Fall 2021 admissions rubric](https://www.gps.caltech.edu/documents/4355/GPS_AdmissionsRubric_Fall2021_Final.pdf).
   - **Contribution:** Explicit anchors for motivation, research goals, prior experience, writing, perseverance, and faculty/program alignment.
   - **Limitation:** An official STEM whole-application rubric, but neither CS-specific nor SOP-only; its weights are not copied.

8. **[Cornell Communication PhD Admissions Rubric](source_materials/admissions_rubrics/Cornell_Communication_PhD_Admissions_Rubric.pdf)**
   - **Origin:** Cornell Department of Communication; PDF metadata credits Drew Margolin and dates the document to 2021. See the [official Cornell Communication graduate-program page](https://cals.cornell.edu/communication/graduate).
   - **Contribution:** Academic potential, originality, research experience, writing, motivation, perseverance, intellectual trajectory, and faculty/program fit.
   - **Limitation:** Communication-field and whole-application criteria require explicit calibration before use in CS SOP evaluation.

9. **[UC Berkeley - Comprehensive Review of Graduate Applicants](source_materials/admissions_rubrics/04_Berkeley_Comprehensive_Review_Graduate_Admissions.pdf)**
   - **Origin:** Lisa García Bedolla and Oscar Dubón, UC Berkeley, December 6, 2019; [official Graduate Division memo](https://grad.berkeley.edu/wp-content/uploads/archive/Comprehensive-Review-of-Applicants-for-Graduate-Admission-and-Fellowship-Nominations_2019-June-6-2.pdf).
   - **Contribution:** Holistic review, context of achievement, and a clear boundary against over-reliance on any single application metric.
   - **Limitation:** Whole-application policy guidance, not an SOP rubric and not a basis for mechanical context bonuses.

10. **[Colorado State - Comprehensive Review Rubric Template](source_materials/admissions_rubrics/10_Colorado_State_Comprehensive_Review_Rubric_Template.xlsx)**
    - **Origin:** Colorado State University Graduate School, [official comprehensive-review criteria and template page](https://graduateschool.colostate.edu/comprehensive-admissions-review-criteria/); the bundled workbook was modified September 22, 2025.
    - **Contribution:** Behavioral-anchor design for preparation, scholarly potential, alignment, long-term goals, perseverance, and self-appraisal.
    - **Limitation:** Non-CS and whole-application; categories, weights, bonus points, and total score are not transplanted into this rubric.

### Negative-control research

11. **[Appleby & Appleby - How to Avoid the Kisses of Death](source_materials/admissions_research/How_to_Avoid_the_Kisses_of_Death.pdf)**
    - **Origin:** Drew C. Appleby and Karen M. Appleby (2006), *Teaching of Psychology*, 33(1), 19-24; [DOI: 10.1207/s15328023top3301_5](https://doi.org/10.1207/s15328023top3301_5).
    - **Contribution:** Negative controls for poor writing, weak program knowledge, inappropriate presentation, and unsupported or damaging claims.
    - **Limitation:** Psychology-specific and dated. It is never used to penalize sensitive disclosure mechanically or generalized uncritically to CS.

## Additional web-only references

- [MIT EECS Communication Lab - Graduate School Statement of Purpose](https://mitcommlab.mit.edu/eecs/commkit/graduate-school-statement-of-purpose/): concrete evidence, research narrative, meaning, and program match
- [MIT EECS faculty - What faculty members look for in an application essay](https://www.eecs.mit.edu/academics/graduate-programs/admission-process/what-faculty-members-are-looking-for-in-a-grad-school-application-essay/): faculty-reader perspective
- [CMU Jonathan Aldrich - PhD statement advice](https://www.cs.cmu.edu/~aldrich/essay-advice.html): research focus and advisor fit
- [CMU Andy Pavlo - How to Write a Bad CS PhD Statement](https://www.cs.cmu.edu/~pavlo/blog/2015/10/how-to-write-a-bad-statement-for-a-computer-science-phd-admissions-application.html): CS-specific negative control
- [Cornell Adrian Sampson - Critiquing a PhD Application Statement](https://www.cs.cornell.edu/~asampson/blog/gradstatement.html): paragraph-level critique
- [UC Berkeley Graduate Division - Writing Your Statements](https://grad.berkeley.edu/admissions/application-process/writing-your-statements/): current SOP/personal-statement boundaries
- [UPenn Career Services - Talking About STEM Research in Your SOP](https://careerservices.upenn.edu/blog/2021/10/21/talking-about-your-stem-research-in-your-statement-of-purpose/): research communication for STEM applicants
- [Jason Eisner, Johns Hopkins CS - Prospective Graduate Students](https://www.cs.jhu.edu/~jason/advice/prospective-students.html): advisor and research-fit perspective

## Responsible use

- Scores and tiers describe the document, not the applicant or an admission outcome.
- Publications, prestige, metrics, faculty names, and polished prose do not earn high scores without evidence of reasoning and ownership.
- Cross-program ranking excludes D6 from the ranking score and reports local fit separately.
- Current official program instructions override every bundled guide or rubric.

The bundled documents remain the property of their original authors and institutions. They are included in this private repository for reference; inclusion does not transfer copyright or imply a common license. Verify the original source and current terms before redistribution.

[Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
