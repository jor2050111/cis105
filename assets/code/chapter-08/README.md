# Chapter 8 Data Pack: Score Your Own Security: An Audit in Charts

Starter file for Skills Lab 8A. Work at the extracted `cis105` root and load the file at `assets/code/chapter-08/security-audit.xlsx`.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `security-audit.xlsx` | Excel workbook, two worksheets (`AuditChecklist`, `ClassResults`) | Skills Lab 8A, all parts, plus the Section 8.4 chart examples |

## Data dictionary

**AuditChecklist** (rows 2-26): the 25-item personal security audit, five categories with five items each. Students score each item 0, 1, or 2, for 10 points per category and 50 total.

| Column | Header | Type | Notes |
| ------ | ------ | ---- | ----- |
| A | Item ID | Text | `SA-01` through `SA-25` |
| B | Category | Text | Accounts, Devices, Network, Backups, or Privacy (five consecutive rows each) |
| C | Audit Item | Text | The habit being scored |
| D | Score 0 when | Text | The failing anchor |
| E | Score 2 when | Text | The passing anchor (1 = partly true) |
| F | Where to look | Text | Where to verify the honest answer |
| G | Your Score | Empty | Students enter 0, 1, or 2 |

**ClassResults** (rows 2-55): 54 anonymized category scores from a class-sized set of the same audit, the comparison series for every chart. 54 data rows by 7 columns.

| Column | Header | Type | Notes |
| ------ | ------ | ---- | ----- |
| A | Student ID | Text | `ST-01` through `ST-54`, anonymized on purpose (no names ship in the file) |
| B-F | Accounts, Devices, Network, Backups, Privacy | Number | Category scores, 0-10 |
| G | Total | Number | Sum of the five categories, 0-50 |

Engineered properties the chapter and lab rely on: category averages are strictly ordered Devices (7.04) > Accounts (6.39) > Network (5.67) > Privacy (4.43) > Backups (3.46), with each gap at least 0.5. Backups is the weakest class category and holds 8 zeros, the overall average total is 26.98 of 50, and no row is implausibly perfect or empty (the generator bounds totals to 8-46, and this draw runs 18-39).

## Reproducibility

Seeded synthetic data, base seed 105. The generator is `assets/code/_generators/generate_chapter08_data.py`, and rerunning it rebuilds this file byte-identically:

```bash
python3 assets/code/_generators/generate_chapter08_data.py
```

The script's asserts verify every engineered property above before writing.

## Source and license

Original content authored for this course. The class results are seeded synthetic data, not real student records: the anonymization the lab points out is also a design choice you can copy. Copyright 2026 Jorge Vega, Phoenix College. Provided for CIS105 coursework.
