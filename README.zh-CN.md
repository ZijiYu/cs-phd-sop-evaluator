# CS PhD SOP 评估器

[English](README.md) | **简体中文**

一个可安装的 Codex Skill，用于基于证据评估、比较和排名研究型计算机科学博士申请的 Statement of Purpose（SOP）。

> 本 Skill 只评价 SOP 文本质量，不排名申请者、不预测录取概率，也不作出录取或拒绝判断。

## 核心功能

- 100 分、7 个行为锚定维度的评分体系
- 对题目合规、事实诚信、研究所有权、导师信息时效、跨文档一致性和模板泄漏设置非补偿性门槛
- 支持单篇审核、定向审核、版本比较、同项目排名和跨项目比较
- 支持匿名多评委聚合、分歧检测、近分复核和暂定分层
- 跨项目比较时单独报告项目匹配度（D6）

## 安装与使用

通过 Codex Skill Installer 安装本仓库，或将其复制到本地 Skills 目录。安装后调用：

```text
$evaluate-cs-phd-sops
```

匿名批量分数聚合：

```bash
python3 scripts/aggregate_scores.py scores.json --strict-privacy
```

聚合文件只应包含匿名 ID 和评分，不应包含姓名、联系方式、SOP 正文或 CV 内容。

## 证据基础与来源说明

本 rubric 综合了大学官方指南、CS 教授建议、MIT EECS 标注样例、公开招生 rubric 和同行评议的负面控制研究。仓库在 [`source_materials/`](source_materials/) 中收录了 **10 个 PDF 和 1 个 XLSX**，总计约 11.4 MB。

以下来源页面核验于 **2026 年 8 月 21 日**。当前项目的官方题目、篇幅限制、导师状态和招生要求始终具有最高优先级。

### SOP 指南与 CS 教授建议

1. **[Stanford - CS PhD 申请者通用建议](source_materials/sop_guides/Stanford_General_Advice_for_CS_PhD_Applicants.pdf)**
   - **来源：** [Stanford Computer Science 官方站点 PDF](https://www.cs.stanford.edu/sites/g/files/sbiybj28076/files/media/file/general-advice-for-cs-phd-applicants.pdf)。
   - **对 rubric 的贡献：** 研究故事结构、清晰的个人贡献、项目动机、从困难中学到什么、学校匹配和信息压缩。
   - **适用限制：** 这是学生撰写的指导材料，不是官方招生评分规则。

2. **[Cornell - 如何撰写 Academic Statement of Purpose](source_materials/sop_guides/Cornell_Writing_Academic_Statement_of_Purpose.pdf)**
   - **来源：** [Cornell Graduate School 官方指南](https://gradschool.cornell.edu/inclusion/recruitment/prospective-students/writing-your-statement-of-purpose/)；PDF 元数据署名 Anitra M. Douglas-McCarthy，并显示 2026 年修订。
   - **对 rubric 的贡献：** 学术准备、具体例子、知情选校、导师匹配、主动写作和终稿检查清单。
   - **适用限制：** 属于通用研究生申请指导；本 Skill 另行增加了 CS 所需的研究所有权和技术证据标准。

3. **[Harvard Griffin GSAS - Perspectives 指南](source_materials/sop_guides/06_Harvard_GSAS_Perspectives_SOP_Guide.pdf)**
   - **来源：** Harvard Griffin Graduate School of Arts and Sciences 的 *Perspectives: Application and Student Life Resources*；PDF 元数据显示该手册制作于 2024 年。另见[当前官方申请入口](https://gsas.harvard.edu/apply)。
   - **对 rubric 的贡献：** 研究问题、学术转折点、学术画像，以及 SOP 与 Personal Statement 的边界。
   - **适用限制：** 与 SOP 直接相关的指导主要集中在综合申请手册的第 6 页。

4. **[Mor Harchol-Balter - 申请计算机科学博士项目](source_materials/sop_guides/09_Harchol_Balter_Applying_to_PhD_Programs_in_CS.pdf)**
   - **来源：** Carnegie Mellon University School of Computer Science 的 Mor Harchol-Balter，[教授主页托管的官方 PDF](https://www.cs.cmu.edu/~harchol/gradschooltalk.pdf)，最后更新于 2003 年。
   - **对 rubric 的贡献：** 研究准备度、发现与学习、失败方法作为有效证据、为何读博，以及导师和项目匹配。
   - **适用限制：** 研究与 SOP 原则仍有价值，但 GRE、排名、联系教授和行政流程建议已经过时。

### CS SOP 标注样例

5. **[MIT EECS 标注 SOP 样例 1](source_materials/annotated_examples/MIT_EECS_Annotated_SOP_Example_1_CS.pdf)**
   - **来源：** MIT EECS Communication Lab 的[官方标注样例 1](https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2016/09/CS-grad-school-personal-statement-annotated-example.pdf)，由 [MIT CommKit SOP 指南](https://mitcommlab.mit.edu/eecs/commkit/graduate-school-statement-of-purpose/)公开链接。
   - **对 rubric 的贡献：** 问题-贡献-结果结构、技术具体性、申请者所有权、量化证据、未来研究和项目匹配。
   - **适用限制：** 成功样例只具有说明作用，不是导致录取的因果证据，也不应被当作仿写模板。

6. **[MIT EECS 标注 SOP 样例 3](source_materials/annotated_examples/MIT_EECS_Annotated_SOP_Example_3_CS.pdf)**
   - **来源：** MIT EECS Communication Lab 的[官方标注样例 3](https://mitcommlab.mit.edu/eecs/wp-content/uploads/sites/6/2016/09/CS-grad-school-personal-statement-annotated-example-2.pdf)，由 [MIT CommKit SOP 指南](https://mitcommlab.mit.edu/eecs/commkit/graduate-school-statement-of-purpose/)公开链接。
   - **对 rubric 的贡献：** 学术轨迹、从广度到聚焦的转折、经解释的研究证据、教学或 outreach 证据、未来议程和项目匹配。
   - **适用限制：** 成功样例只具有说明作用，不是导致录取的因果证据，也不是普适写作模型。

### 招生 Rubric 与整体审核来源

7. **[Caltech GPS 研究生招生 Rubric](source_materials/admissions_rubrics/Caltech_GPS_Admissions_Rubric.pdf)**
   - **来源：** Caltech Division of Geological and Planetary Sciences，[2021 年秋季官方招生 rubric](https://www.gps.caltech.edu/documents/4355/GPS_AdmissionsRubric_Fall2021_Final.pdf)。
   - **对 rubric 的贡献：** 为动机、研究目标、既往经历、写作、坚持性和导师或项目匹配提供明确行为锚点。
   - **适用限制：** 这是官方 STEM 整体申请 rubric，但不是 CS 专用或 SOP 专用；本 Skill 没有复制其权重。

8. **[Cornell Communication PhD 招生 Rubric](source_materials/admissions_rubrics/Cornell_Communication_PhD_Admissions_Rubric.pdf)**
   - **来源：** Cornell Department of Communication；PDF 元数据署名 Drew Margolin，制作于 2021 年。另见 [Cornell Communication 官方研究生项目页面](https://cals.cornell.edu/communication/graduate)。
   - **对 rubric 的贡献：** 学术潜力、原创性、研究经历、写作、动机、坚持性、学术轨迹和导师或项目匹配。
   - **适用限制：** 属于传播学领域和整体申请标准，必须经过明确校准后才能用于 CS SOP。

9. **[UC Berkeley - 研究生申请综合审核备忘录](source_materials/admissions_rubrics/04_Berkeley_Comprehensive_Review_Graduate_Admissions.pdf)**
   - **来源：** Lisa García Bedolla 与 Oscar Dubón，UC Berkeley，2019 年 12 月 6 日；[Graduate Division 官方备忘录](https://grad.berkeley.edu/wp-content/uploads/archive/Comprehensive-Review-of-Applicants-for-Graduate-Admission-and-Fellowship-Nominations_2019-June-6-2.pdf)。
   - **对 rubric 的贡献：** 整体审核、成就背景，以及不能过度依赖单一申请指标的明确边界。
   - **适用限制：** 这是整体申请政策指南，不是 SOP rubric，也不能作为机械增加背景分的依据。

10. **[Colorado State - 综合审核 Rubric 模板](source_materials/admissions_rubrics/10_Colorado_State_Comprehensive_Review_Rubric_Template.xlsx)**
    - **来源：** Colorado State University Graduate School 的[官方综合审核标准与模板页面](https://graduateschool.colostate.edu/comprehensive-admissions-review-criteria/)；仓库内工作簿最后修改于 2025 年 9 月 22 日。
    - **对 rubric 的贡献：** 为学术准备、研究潜力、匹配、长期目标、坚持性和自我评估提供行为锚点设计参考。
    - **适用限制：** 不是 CS 专用且面向整体申请；本 rubric 没有移植其分类、权重、奖励分或总分。

### 负面控制研究

11. **[Appleby & Appleby - 如何避免申请中的 Kisses of Death](source_materials/admissions_research/How_to_Avoid_the_Kisses_of_Death.pdf)**
    - **来源：** Drew C. Appleby 与 Karen M. Appleby（2006），*Teaching of Psychology*, 33(1), 19-24；[DOI: 10.1207/s15328023top3301_5](https://doi.org/10.1207/s15328023top3301_5)。
    - **对 rubric 的贡献：** 为低质量写作、缺乏项目了解、不恰当表达以及缺乏证据或有害主张提供负面控制。
    - **适用限制：** 研究领域为心理学且年代较早；本 Skill 不会机械惩罚敏感信息披露，也不会不加批判地推广到 CS。

## 其他网页来源

- [MIT EECS Communication Lab - Graduate School Statement of Purpose](https://mitcommlab.mit.edu/eecs/commkit/graduate-school-statement-of-purpose/)：具体证据、研究叙事、经验含义和项目匹配
- [MIT EECS 教授 - 申请文书中关注什么](https://www.eecs.mit.edu/academics/graduate-programs/admission-process/what-faculty-members-are-looking-for-in-a-grad-school-application-essay/)：教授阅读视角
- [CMU Jonathan Aldrich - PhD SOP 建议](https://www.cs.cmu.edu/~aldrich/essay-advice.html)：研究聚焦与导师匹配
- [CMU Andy Pavlo - 如何写一篇糟糕的 CS PhD SOP](https://www.cs.cmu.edu/~pavlo/blog/2015/10/how-to-write-a-bad-statement-for-a-computer-science-phd-admissions-application.html)：CS 专向负面控制
- [Cornell Adrian Sampson - PhD 申请文书批评](https://www.cs.cornell.edu/~asampson/blog/gradstatement.html)：段落级批评示例
- [UC Berkeley Graduate Division - Writing Your Statements](https://grad.berkeley.edu/admissions/application-process/writing-your-statements/)：当前 SOP 与 Personal Statement 边界
- [UPenn Career Services - 在 SOP 中介绍 STEM 研究](https://careerservices.upenn.edu/blog/2021/10/21/talking-about-your-stem-research-in-your-statement-of-purpose/)：STEM 研究表达
- [Jason Eisner, Johns Hopkins CS - Prospective Graduate Students](https://www.cs.jhu.edu/~jason/advice/prospective-students.html)：导师与研究匹配视角

## 负责任使用

- 分数与层级描述的是文档，不是申请者或录取结果。
- 论文、学校声望、指标、导师姓名和流畅文笔，若缺乏研究推理与个人所有权证据，不能自动获得高分。
- 跨项目排名时，D6 不进入排名分数，项目匹配度单独报告。
- 当前官方项目要求覆盖所有随附指南和 rubric。

仓库内材料的权利仍归原作者和机构所有。这些材料收录在私有仓库中供参考；收录行为不转移版权，也不表示所有文件采用相同许可证。再次分发前请核对原始来源及当前使用条款。

[Codex Skill 官方文档](https://learn.chatgpt.com/docs/build-skills)
