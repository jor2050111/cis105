# Chapter 12 Data Pack: Record It, Read It, Rewrite It

Starter files for Skills Lab 12A. Work at the extracted `cis105` root
and open the workbook from `assets/code/chapter-12/` in desktop Excel
(Windows or macOS). Excel for the web cannot record or run the macros
this lab teaches.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `booking-export.xlsx` | Excel workbook, 63 data rows by 10 columns | Skills Lab 12A, all parts, plus the Section 12.1 and 12.4 examples |
| `ai-macro-draft.txt` | Plain text: a prompt and the VBA it produced | Skills Lab 12A, Part 3, and Try It Yourself 12.4 |

The AI draft ships as plain text on purpose. Nothing in this pack
contains a runnable macro, so nothing here triggers Excel's macro
security, and students paste and run only code they have read.

## The scenario

Saguaro Hall's booking base (built in Chapter 10, rolled out in
Chapter 11) went live after its parallel run, and October 2026 was its
first full month. On the first business day of November, Renee Salazar
downloads the month's bookings from an Airtable export view and formats
the same revenue readout for Darnell Brooks she formats every month.
The export view does two jobs before she ever clicks Download: it
filters out cancellations and leaves the customer contact columns
behind (the least-privilege habit from Chapters 8 and 10), and it sorts
by event date.

Back in September, Renee asked an AI assistant to draft a macro that
appends the month's booking count and total to the export. Her prompt
described September's file, which held 60 bookings. October holds 63.
The draft still runs without a single error message. Its numbers are
wrong. Finding out why is Part 3 of the lab.

## Data dictionary

**booking-export.xlsx**, one worksheet named `OctoberExport`, one row
per booking, headers in row 1, data in rows 2-64:

| Column | Header | Type | Notes |
| ------ | ------ | ---- | ----- |
| A | Booking ID | Text | `SH-` plus four digits, unique |
| B | Event Date | Date | October 2026, sorted ascending |
| C | Space | Text | Main Hall, Courtyard, or Meeting Room |
| D | Organization | Text | The client, from the Chapter 10 customer list |
| E | Event Type | Text | Fundraiser, Concert, Workshop, and so on |
| F | Guest Count | Number | Never exceeds the space's capacity |
| G | Hours | Number | Booked hours |
| H | Package | Text | Bronze, Silver, or Gold |
| I | Add-Ons | Text | Comma-separated add-ons, or None |
| J | Quoted Price | Number | Unformatted dollars (the lab formats it) |

Pricing follows the Chapter 10 model exactly: space hourly rate times
hours, plus the package fee, plus add-on fees (Main Hall $200/hr,
Courtyard $150/hr, Meeting Room $60/hr; Bronze $0, Silver $350, Gold
$750; AV Package $150, Catering $500, Decor $300, Extra Staff $200,
Parking $100).

**ai-macro-draft.txt:** Renee's September prompt, word for word, and
the assistant's drafted `Sub SummarizeExport()`, unchanged. Every range
in the draft is hardcoded to rows 2-61 because her prompt said the data
runs to row 61, and the summary label still says September.

## Engineered properties the chapter and lab rely on

* 63 bookings, all in October 2026, dates ascending, no cancellations,
  no contact columns.
* The four October bookings that already existed in the Chapter 10 base
  (`SH-1016`, `SH-1017`, `SH-1040`, `SH-1041`) appear verbatim, same
  fields and same prices. The other 59 were booked after that July
  snapshot and continue the ID series from `SH-1061`. That growth is the
  normal shape of a venue calendar: in July only four October dates were
  reserved, and the weeks before and during October filled in the rest.
* No space is booked twice on the same date, and every guest count fits
  its space.
* Correct October totals: **63 bookings, $83,910** quoted revenue.
* What the AI draft reports on this file: **60 bookings, $78,510**. Its
  hardcoded rows 2-61 cover only the first 60 bookings, so it silently
  drops the last three (the Oct 30-31 finale: `SH-1071` at $2,750,
  `SH-1081` at $1,500, `SH-1085` at $1,150). The miss is **$5,400**,
  about 6 percent of the month: material, not a rounding slip.
* The draft contains no syntax error. It runs clean and reports wrong
  numbers, which is the chapter's point.

## Reproducibility

Seeded synthetic data, base seed 105. The generator imports the
Chapter 10 generator so the shared pricing model, organization list,
and inherited October rows can never drift, and it pins workbook
metadata and zip timestamps so rebuilds are byte-identical:

```bash
python3 assets/code/_generators/generate_chapter12_data.py
```

The script's asserts verify every engineered property above before
writing. It needs `openpyxl` (`python3 -m pip install openpyxl`).

## Source and license

Original content authored for this course. Saguaro Hall, its clients,
and the AI-drafted macro are fictional teaching artifacts. Copyright
2026 Jorge Vega, Phoenix College. Provided for CIS105 coursework.
