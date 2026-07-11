# Data Pack Generators

Scripts in this folder rebuild every derived file in the course data
pack. Follow the pattern the existing textbooks use:

## Current inventory

One script, one generated file. Base seed for this course: 105.

| Script | Rebuilds | Properties |
| ------ | -------- | ---------- |
| `generate_chapter06_data.py` | `assets/code/chapter-06/device-comparison.xlsx` | 54 rows x 8 columns, 7 engineered blank battery cells, unique MIN/MAX prices, Chapter 5 cast devices included, byte-identical on rerun |
| `generate_chapter07_data.py` | `assets/code/chapter-07/internet-plans.xlsx` | 54 rows x 10 columns, hand-designed plan market: sticker-versus-true-cost flip, 13 venue qualifiers with a unique winner, cap-only failure plan, GEO/LEO latency contrast, byte-identical on rerun |
| `generate_chapter08_data.py` | `assets/code/chapter-08/security-audit.xlsx` | Two sheets: 25-item audit checklist plus 54 x 7 anonymized class results with engineered category ordering (Devices strongest, Backups weakest), byte-identical on rerun |
| `generate_chapter09_data.py` | `assets/code/chapter-09/coffee-sales.xlsx` | 571 rows x 12 columns of June line items: Campus weekend dip hidden by the chain average, app revenue share rising every week, app orders outspending counter orders, Cold Drinks leading, byte-identical on rerun |

The Word and RTF starter files in chapters 1-5 are committed artifacts
authored via pandoc, not generated. Each chapter folder's README is the
data dictionary.

## Conventions

* **Dependencies.** Generators run with system `python3` and need
  `openpyxl` (`python3 -m pip install openpyxl`). The repo's `.venv`
  holds Zensical only, so do not run generators with `.venv/bin/python3`.
* **Seeded and reproducible.** Synthetic datasets use a fixed base seed
  (pick the course number) so reruns are byte-identical. Add asserts
  that verify the engineered properties each chapter depends on.
* **Document provenance.** Real datasets record their source, license,
  and retrieval date here and in the chapter folder's README.
* **One-time captures are not rebuilt.** Files captured from live APIs
  are committed as-is and documented, not regenerated.
* **Each chapter folder gets a README** describing every file, its
  schema, and which sections or labs load it.

## Rebuilding the student data pack zip

From the parent of the repo root (the zip's internal root is
`cis105`, the folder name the published chapters tell
students to work in):

```bash
cd /Users/vega/Documents/code/textbooks && \
zip -r cis105/build/cis105-data-pack.zip \
    cis105/assets/code \
    -x '*.DS_Store' -x '*__pycache__*'
```

The zip lands in `build/` (gitignored) and uploads to Canvas.
