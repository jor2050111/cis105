# Chapter 10 Data Pack: From CSV to Connected Base

Starter files for Skills Lab 10A. Work at the extracted `cis105` root
and import the two CSV files into Airtable from
`assets/code/chapter-10/`.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `saguaro-bookings.csv` | CSV, 60 data rows by 13 columns | Skills Lab 10A, all parts, plus the Section 10.2 examples |
| `saguaro-customers.csv` | CSV, 24 data rows by 6 columns | Skills Lab 10A, Parts 2 and 3 (the table the bookings link to) |

`saguaro-bookings.csv` is the primary tabular dataset and clears the
50-by-5 floor on its own. `saguaro-customers.csv` is its companion
dimension table (the same pattern as the Chapter 8 audit checklist), so
it is deliberately smaller: one row per organization, contact details
stored once.

## The scenario

Saguaro Hall is the downtown Phoenix event venue run by Darnell Brooks
(Chapter 4). Its booking system is a web app, and this export is the
flat table it produced. The lab turns that flat export into a
**connected base**: two linked tables that store each fact once.

## Data dictionary

**saguaro-bookings.csv:** one row per event booking. The customer's
email and phone are COPIED onto every row (the denormalization the lab
fixes by linking a Customers table).

| Column | Header | Type in Airtable | Notes |
| ------ | ------ | ---------------- | ----- |
| A | Booking ID | Single line text | `SH-1001` through `SH-1060`, unique (the primary key) |
| B | Event Date | Date | ISO dates across 2026 |
| C | Space | Single select | Main Hall, Courtyard, or Meeting Room |
| D | Organization | Link to Customers (starts as text) | Matches a row in `saguaro-customers.csv` exactly |
| E | Contact Email | Email | The organization's email, copied onto every booking |
| F | Contact Phone | Phone number | The organization's phone, copied onto every booking |
| G | Event Type | Single select | Wedding, Conference, Fundraiser, Workshop, and so on |
| H | Guest Count | Number | Expected attendance |
| I | Hours | Number | Length of the booking |
| J | Package | Single select | Bronze, Silver, or Gold |
| K | Add-Ons | Multiple select | Comma-separated. `None` means no add-ons |
| L | Status | Single select | Confirmed, Pending, Completed, or Cancelled |
| M | Quoted Price | Currency | Computed (see pricing model) |

**saguaro-customers.csv:** one row per organization, the clean
dimension. Set the first column (Organization) as the primary field on
import, so the bookings link matches on it.

| Column | Header | Type in Airtable | Notes |
| ------ | ------ | ---------------- | ----- |
| A | Organization | Single line text | Primary field, unique |
| B | Contact Name | Single line text | The person who books |
| C | Email | Email | The one correct email |
| D | Phone | Phone number | The one correct phone |
| E | Member Since | Number | Year the organization first booked |
| F | Notes | Long text | Free-text account notes |

## Pricing model (so every Quoted Price is explainable)

`Quoted Price = space rate x Hours + package fee + add-on fees`

* Space rate per hour: Main Hall $200, Courtyard $150, Meeting Room $60
* Package fee: Bronze $0, Silver $350, Gold $750
* Add-on fee each: AV Package $150, Catering $500, Decor $300,
  Extra Staff $200, Parking $100

## Engineered properties the chapter and lab rely on

* 60 bookings across 24 organizations. Every booking's Organization
  exists in the Customers table, so the Airtable link matches cleanly
  with no phantom records.
* Repeat business: 17 of the 24 organizations book more than once. The
  City of Phoenix Parks and Rec books the most (6 times), then Phoenix
  Camera Club (5). This is what the link makes visible.
* Contact Email always matches the Customers table. Contact Phone
  matches too, except **one** booking, `SH-1005`, whose phone drifted
  one digit (the hazard of copying data instead of pointing at it). The
  Customers table holds the one correct number.
* Every Quoted Price equals the formula above, so the total is
  reproducible: $81,060 quoted across all 60 bookings, $73,780 once the
  6 cancellations drop out.
* Status mix: 27 Completed, 15 Confirmed, 12 Pending, 6 Cancelled.
* Space mix: Courtyard 24, Main Hall 19, Meeting Room 17.
* Exactly two bookings exceed their space's capacity, `SH-1009`
  (175 guests in the 150-seat Courtyard) and `SH-1052` (52 guests in the
  40-seat Meeting Room): a feasibility flag students can spot.

## Reproducibility

Seeded synthetic data, base seed 105. The generator is
`assets/code/_generators/generate_chapter10_data.py`, and rerunning it
rebuilds both files byte-identically:

```bash
python3 assets/code/_generators/generate_chapter10_data.py
```

The script's asserts verify every engineered property above before
writing. The generator needs only the Python standard library.

## Source and license

Original content authored for this course. Saguaro Hall, the 24
organizations, and every booking are fictional. Any resemblance to real
organizations is coincidental. Copyright 2026 Jorge Vega, Phoenix
College. Provided for CIS105 coursework.
