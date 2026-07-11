# Chapter 7 Data Pack: Let Formulas Do the Math: Choosing an Internet Plan

Starter file for Skills Lab 7A. Work at the extracted `cis105` root and load the file at `assets/code/chapter-07/internet-plans.xlsx`.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `internet-plans.xlsx` | Excel workbook, one worksheet (`InternetPlans`) | Skills Lab 7A, all parts, plus the Section 7.4 examples |

## Data dictionary

**internet-plans.xlsx:** the Phoenix-area Internet plan comparison sheet Saguaro Hall shops from: 54 data rows (rows 2-55) by 10 columns, covering nine fictional providers across six connection technologies (Fiber, Cable, 5G Home, DSL, GEO satellite, LEO satellite).

| Column | Header | Type | Notes |
| ------ | ------ | ---- | ----- |
| A | Plan ID | Text | `IP-101` through `IP-154`, unique |
| B | Provider | Text | Nine fictional providers |
| C | Technology | Text | Fiber, Cable, 5G Home, DSL, Satellite (GEO), or Satellite (LEO) |
| D | Plan Name | Text | Provider tier names |
| E | Download (Mbps) | Number | Advertised download speed |
| F | Upload (Mbps) | Number | Advertised upload speed; fiber is symmetric, everything else is not |
| G | Latency (ms) | Number | Typical round-trip delay |
| H | Advertised Price ($/mo) | Number | The sticker price. Unformatted: students apply the currency format |
| I | Equipment Fee ($/mo) | Number | Monthly modem, router, or dish rental. Zero where the fee is included |
| J | Data Cap | Text | `Unlimited` or a monthly cap such as `300 GB` |

Engineered properties the chapter and lab rely on: the cheapest advertised plan (Copper Basin DSL Basic 25, $30) is not the cheapest true-cost plan (Roadrunner Wireless Essential 100, $40 with no equipment fee), and both minimums are unique. Exactly 13 plans meet Saguaro Hall's requirements (download 300+, upload 30+, latency 100 ms or less, Unlimited data), with a unique cheapest qualifier (Sonoran Fiber Home 300, $65 true cost). Roadrunner Surge 500 fails the venue test on its data cap alone. Every GEO satellite plan fails on latency and every LEO plan passes it. Cost per Mbps has a unique best (Sonoran Fiber Pro 2000, about $0.06) and worst (Copper Basin DSL Rural 10, $4.70).

## Reproducibility

Hand-designed rows rebuilt deterministically. The generator is `assets/code/_generators/generate_chapter07_data.py`, and rerunning it rebuilds this file byte-identically:

```bash
python3 assets/code/_generators/generate_chapter07_data.py
```

The script's asserts verify every engineered property above before writing.

## Source and license

Original content authored for this course. All providers, plans, prices, and speeds are fictional, designed to mirror 2026 market shapes without naming any company. Copyright 2026 Jorge Vega, Phoenix College. Provided for CIS105 coursework.
