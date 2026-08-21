# CS PhD SOP Evaluator

## 中文

一个用于评估、比较和排名研究型 CS PhD Statement of Purpose（SOP）的 Codex Skill。

### 功能

- 使用 100 分、7 维度的证据型评分标准
- 支持单篇审核、版本比较和多篇 SOP 排名
- 支持匿名、多评委评分与分歧检测
- 跨学校比较时，将学校匹配度（D6）单独报告

本工具只评价 **SOP 文本质量**，不评价申请者，也不预测录取概率。

### 使用

通过 Codex Skill Installer 安装此仓库，或将仓库复制到本地 Skills 目录。安装后调用：

```text
$evaluate-cs-phd-sops
```

批量分数聚合：

```bash
python3 scripts/aggregate_scores.py scores.json --strict-privacy
```

聚合文件应只包含匿名 ID 和评分，不要加入姓名、联系方式、SOP 正文或 CV 内容。

## English

A Codex skill for evaluating, comparing, and ranking research-oriented Computer Science PhD Statements of Purpose.

### Features

- Evidence-based 100-point rubric with seven dimensions
- Single-SOP review, version comparison, and batch ranking
- Anonymous multi-judge aggregation and disagreement detection
- Separate program-fit reporting (D6) for cross-program comparisons

This tool evaluates **SOP document quality only**. It does not evaluate applicants or predict admission outcomes.

### Usage

Install this repository with the Codex Skill Installer, or copy it into your local skills directory. Then invoke:

```text
$evaluate-cs-phd-sops
```

Aggregate batch scores with:

```bash
python3 scripts/aggregate_scores.py scores.json --strict-privacy
```

Aggregation files should contain anonymous IDs and scores only—never names, contact details, SOP text, or CV content.

[Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)

## Reference materials / 参考材料

The private repository includes the 11 local sources used to build the rubric: **10 PDFs and 1 XLSX** (about 11.4 MB). They are organized under `source_materials/` and are not loaded during normal skill execution.

本私有仓库收录了构建 rubric 时实际采用的 11 个本地来源：**10 个 PDF 和 1 个 XLSX**（约 11.4 MB）。文件整理在 `source_materials/` 中，Skill 正常运行时不会自动加载它们。

<details>
<summary>File list and introductions / 文件清单与介绍</summary>

| File / 文件 | Type | Introduction / 介绍 |
|---|---|---|
| [Berkeley Comprehensive Review](source_materials/admissions_rubrics/04_Berkeley_Comprehensive_Review_Graduate_Admissions.pdf) | PDF | Holistic and context-aware graduate review; supports the rule against treating one SOP score as an admission prediction. / 研究生整体与情境化审核，支持“不把 SOP 分数等同录取结果”的原则。 |
| [Colorado State Rubric Template](source_materials/admissions_rubrics/10_Colorado_State_Comprehensive_Review_Rubric_Template.xlsx) | XLSX | Example of behavioral anchors and comprehensive-review structure; not a CS-specific rubric. / 行为锚点与综合审核结构示例，并非 CS 专用 rubric。 |
| [Caltech GPS Admissions Rubric](source_materials/admissions_rubrics/Caltech_GPS_Admissions_Rubric.pdf) | PDF | Covers motivation, research goals, prior experience, writing, perseverance, and program alignment. / 涵盖动机、研究目标、既往经历、写作、坚持性和项目匹配。 |
| [Cornell Communication PhD Rubric](source_materials/admissions_rubrics/Cornell_Communication_PhD_Admissions_Rubric.pdf) | PDF | Provides criteria for academic potential, originality, research experience, writing, and fit; requires CS calibration. / 提供学术潜力、原创性、研究经历、写作和匹配标准，使用时需按 CS 校准。 |
| [Harvard GSAS Perspectives Guide](source_materials/sop_guides/06_Harvard_GSAS_Perspectives_SOP_Guide.pdf) | PDF | Emphasizes research questions, intellectual turning points, and the SOP/personal-statement distinction. / 强调研究问题、学术转折点，以及 SOP 与 Personal Statement 的区别。 |
| [Harchol-Balter: Applying to PhD Programs in CS](source_materials/sop_guides/09_Harchol_Balter_Applying_to_PhD_Programs_in_CS.pdf) | PDF | CS-specific guidance on research readiness, findings, failures, why PhD, and program fit; administrative advice is dated. / CS 专向指导，涉及研究准备度、发现、失败经验、为何读博和项目匹配；行政建议较旧。 |
| [Cornell Academic SOP Guide](source_materials/sop_guides/Cornell_Writing_Academic_Statement_of_Purpose.pdf) | PDF | Focuses on preparation, concrete examples, informed program choice, faculty fit, and active writing. / 强调学术准备、具体证据、知情选校、导师匹配和主动语态。 |
| [Stanford CS PhD Applicant Advice](source_materials/sop_guides/Stanford_General_Advice_for_CS_PhD_Applicants.pdf) | PDF | Research-story structure, personal contribution, project motivation, lessons learned, fit, and compression. / 涵盖研究故事结构、个人贡献、项目动机、经验反思、匹配和信息压缩。 |
| [MIT EECS Annotated SOP Example 1](source_materials/annotated_examples/MIT_EECS_Annotated_SOP_Example_1_CS.pdf) | PDF | Annotated CS example illustrating problem, contribution, outcome, and fit. / 展示研究问题、个人贡献、结果和项目匹配的 CS 标注样例。 |
| [MIT EECS Annotated SOP Example 3](source_materials/annotated_examples/MIT_EECS_Annotated_SOP_Example_3_CS.pdf) | PDF | Annotated CS example illustrating concrete evidence, future work, and fit. / 展示具体证据、未来研究和项目匹配的 CS 标注样例。 |
| [How to Avoid the Kisses of Death](source_materials/admissions_research/How_to_Avoid_the_Kisses_of_Death.pdf) | PDF | Negative-control research on common application-writing failures; psychology-specific and dated, so it is used cautiously. / 关于常见申请写作失败的负面控制研究；领域为心理学且年代较早，因此谨慎使用。 |

</details>

These documents remain the property of their original authors and institutions. They are included for private reference; verify current official guidance before reuse or evaluation.

以上材料的权利仍归原作者和机构所有，仅供私有参考；复用或审核前请核对最新官方要求。
