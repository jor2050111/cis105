# Data Pack Generators

Scripts in this folder rebuild every derived file in the course data
pack. Follow the pattern the existing textbooks use:

## Current inventory

One script, one generated file. Base seed for this course: 105.

| Script | Rebuilds | Properties |
| ------ | -------- | ---------- |
| `generate_chapter06_data.py` | `assets/code/chapter-06/device-comparison.xlsx` | 54 rows x 8 columns, 7 engineered blank battery cells, unique MIN/MAX prices, Chapter 5 cast devices included, byte-identical on rerun |

The Word and RTF starter files in chapters 1-5 are committed artifacts
authored via pandoc, not generated. Each chapter folder's README is the
data dictionary.

## Conventions

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
