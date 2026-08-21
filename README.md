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
