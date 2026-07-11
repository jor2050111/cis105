# Chapter 9 Data Pack: Sort, Filter, Pivot: Answers from Sales Data

Starter file for Skills Lab 9A. Work at the extracted `cis105` root and load the file at `assets/code/chapter-09/coffee-sales.xlsx`.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `coffee-sales.xlsx` | Excel workbook, one worksheet (`SalesData`) | Skills Lab 9A, all parts, plus the Section 9.4 examples |

## Data dictionary

**coffee-sales.xlsx:** Desert Bloom Coffee's June 2026 sales export: 571 line items (rows 2-572) by 12 columns, covering three locations, four full Monday-to-Sunday weeks (June 1-28), two channels, and five product categories. The file is a teaching-sized sample: a real month at three locations runs thousands of line items, and the pivots you build on this sample work the same way at any size.

| Column | Header | Type | Notes |
| ------ | ------ | ---- | ----- |
| A | Order ID | Text | `DB-1001` through `DB-1571`, unique, chronological |
| B | Date | Date | June 1-28, 2026 |
| C | Week | Number | 1 through 4 (Monday-to-Sunday weeks) |
| D | Day Type | Text | Weekday or Weekend |
| E | Location | Text | 7th Street, Roosevelt Row, or Campus |
| F | Daypart | Text | Morning, Afternoon, or Evening |
| G | Channel | Text | Counter or Bloom Ahead (the mobile app) |
| H | Category | Text | Hot Coffee, Cold Drinks, Tea, Bakery, or Merch |
| I | Item | Text | Menu item names |
| J | Qty | Number | Units on the line |
| K | Unit Price ($) | Number | Menu price. Unformatted: students apply the currency format |
| L | Line Total ($) | Number | Qty times Unit Price, exactly |

Engineered properties the chapter and lab rely on: total revenue $4,994.75. The Campus location's weekend days average $23.41 against $60.17 on weekdays (a dip below half), while 7th Street holds its weekends ($79.94 versus $72.44), so the chain-wide daily average ($165.94 weekend versus $183.36 weekday) hides the Campus story until a pivot splits location by day type. Bloom Ahead's share of revenue rises every week: 26.4%, 41.7%, 51.5%, 60.4%. App line items average $11.36 against the counter's $7.34. Cold Drinks is the top category of a Phoenix June ($1,765.75) and Merch the smallest ($256.00).

## Reproducibility

Seeded synthetic data, base seed 105. The generator is `assets/code/_generators/generate_chapter09_data.py`, and rerunning it rebuilds this file byte-identically:

```bash
python3 assets/code/_generators/generate_chapter09_data.py
```

The script's asserts verify every engineered property above before writing.

## Source and license

Original content authored for this course. Desert Bloom Coffee, its locations, menu, and every transaction are fictional. Copyright 2026 Jorge Vega, Phoenix College. Provided for CIS105 coursework.
