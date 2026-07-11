# Chapter 6 Data Pack: Side by Side: A Device Comparison Workbook

Starter file for Skills Lab 6A. Work at the extracted `cis105` root and load the file at `assets/code/chapter-06/device-comparison.xlsx`.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `device-comparison.xlsx` | Excel workbook, one worksheet (`DeviceInventory`) | Skills Lab 6A, all parts |

## Data dictionary

**device-comparison.xlsx:** Cactus Wren Repair's refurbished-device inventory: 54 data rows (rows 2-55) by 8 columns.

| Column | Header | Type | Notes |
| ------ | ------ | ---- | ----- |
| A | Device ID | Text | `CW-1001` through `CW-1054`, unique |
| B | Device Name | Text | Shop model names |
| C | Category | Text | Laptop, Desktop, Tablet, or Phone |
| D | Condition Grade | Text | A, B, or C |
| E | RAM (GB) | Number | Working memory |
| F | Storage (GB) | Number | Drive capacity |
| G | Battery Health (%) | Number or blank | Blank for all 7 desktops on purpose: desktops have no battery, and the lab teaches how AVERAGE treats blanks |
| H | Price ($) | Number | Unformatted: students apply the currency format |

Engineered properties the lab relies on: exactly 7 blank battery cells (the desktops), a unique maximum price ($1,299, Saguaro Workstation) and minimum price ($89, Cactus Call Mini), and the three Chapter 5 devices (Desert Falcon 15, Stone Tower, Bloom Pad 11) present with their published specs.

## Reproducibility

Seeded synthetic data, base seed 105. The generator is `assets/code/_generators/generate_chapter06_data.py`, and rerunning it rebuilds this file byte-identically:

```bash
python3 assets/code/_generators/generate_chapter06_data.py
```

The script's asserts verify every engineered property above before writing.

## Source and license

Original content authored for this course. Cactus Wren Repair and all device names, specs, and prices are fictional. Copyright 2026 Jorge Vega, Phoenix College. Provided for CIS105 coursework.
