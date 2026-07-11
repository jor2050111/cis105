# CIS105 Textbook Style Guide

This file holds the course-specific layer only. The canonical shared
writing law lives at `../shared/style-guide-core.md` in the textbooks
workspace. The sync script copies it into this repo as
`docs/style-guide-core.md`. Read the core first. Never edit the synced
copy, and never restate core rules here. When this file and the core
disagree, this file wins for CIS105 only.

## Audience and Tone Calibration

Calibrate the core's tone invariants for community college students in
their first computing course.

* **Assumed background:** no prior experience. CIS105 has no
  prerequisite courses. Chapters teach from zero and assume only
  earlier chapters of this book.
* **Register:** friendly but authoritative. Many readers are testing
  whether technology is for them, so explain plainly and never talk
  down. Treat students as emerging professionals who already use
  phones, apps, and the web every day.
* **Reading level:** Flesch Reading Ease 60-70, leaning toward the top
  of the band (course default, confirmed by Mr. Vega at setup,
  2026-07-11).
* **Bridging rule:** bridge from everyday technology experience
  (phones, streaming, social apps), then name the formal concept.
  Reference earlier chapters with one sentence, never reteach.

## Bloom's-Level Emphasis for CIS105

The shared framework lives in `docs/blooms-taxonomy-reference.md`
(synced). Record here how this course weights the six levels.

* **Primary levels:** Remember, Understand, and Apply carry most MLOs.
* **Occasional levels:** Analyze for comparison sections (hardware
  choices, software categories, security risks). Evaluate for
  tool-selection and ethics work. Create for the VBA macro work in
  Chapter 12 and stretch parts of Skills Labs.
* **Avoided levels:** none banned, but Evaluate and Create MLOs need a
  concrete, gradable product. Never tag an MLO above the level its
  assessment reaches.
* **Distribution across the term:** Parts I and II lean Remember
  through Apply. Part III adds Analyze and Evaluate (security and
  ethics judgments). Part IV finishes Apply through Create (databases,
  systems thinking, macros).

## Tech-Stack Conventions for Microsoft 365, Airtable, and VBA

Language and tool rules the core delegates to the course guide.

* **Code fence identifiers:** `vba` for macro code, `html` for markup
  snippets, `text` for Excel formulas and Airtable formula expressions,
  `bash` only in instructor tooling docs (never student-facing).
* **Language style standard:** VBA procedures in PascalCase with one
  comment line stating WHY. Excel formulas written with named ranges or
  structured references where the lesson allows. HTML snippets follow
  current HTML Living Standard (no deprecated tags).
* **Naming scheme:** semantic names everywhere. Worksheet tabs, Excel
  tables, Airtable bases, tables, and fields all describe their
  content. Generic names (`Sheet2`, `Table 1`, `data`) are banned
  except in deliberately broken teaching examples.
* **Version targets:** Microsoft 365 desktop apps (current channel) on
  Windows 11 or macOS. Airtable current web app, free plan features
  only. VBA labs require desktop Excel (Excel for the web cannot run
  macros). Evergreen browsers.
* **Capitalization table:**

| Term | Correct | Incorrect |
| ---- | ------- | --------- |
| Microsoft 365 | Microsoft 365 | MS365, Office 365 (retired name) |
| Excel | Excel | EXCEL, excel |
| PowerPoint | PowerPoint | Powerpoint, Power Point |
| Airtable | Airtable | AirTable, Air Table |
| VBA | VBA (Visual Basic for Applications on first mention) | Vba, vba |
| macro | macro (lowercase) | Macro (mid-sentence) |
| email | email | e-mail, E-mail |
| e-commerce | e-commerce | eCommerce, E-Commerce (mid-sentence) |
| the web | the web | the Web (mid-sentence) |
| Wi-Fi | Wi-Fi | wifi, WiFi |
| Internet | the Internet | the internet |

## Dataset and Example-Domain Conventions

* **Example domains:** small-business scenarios students recognize:
  a Phoenix-area coffee shop, a campus bookstore, a mobile device
  repair shop, and a community event venue. Reuse these businesses
  across chapters so context carries forward.
* **Provided files:** every lab file ships in the course data pack
  under `assets/code/chapter-NN/`. Students download one zip from
  Canvas, extract it, and work at the `cis105` root. Excel and Word
  labs open pack files directly. Airtable labs import pack CSVs.
* **Rules for new datasets or fixtures:** tabular files carry at least
  50 rows and 5 columns. Use real public data where it fits (cite
  source and license in the folder README). Use seeded synthetic data
  when the lab needs engineered properties. Generators live in
  `assets/code/_generators/` and rebuild byte-identical.
* **What students never hand-type:** datasets, record sets, body text,
  and slide content. The exceptions where typing is itself the lesson:
  short Excel formulas, VBA edits in the Visual Basic Editor, small
  HTML snippets, and Airtable formula fields.
