# CIS105 Textbook: Session Handoff

**Last updated:** 2026-07-11 (Part III session: chapters 7-9)
**Repo:** https://github.com/jor2050111/cis105
**Live site:** https://jor2050111.github.io/cis105/
**Task list:** CLAUDE_CODE_TASK_LIST_ID=cis105 (pinned in
`/Users/vega/Documents/code/textbooks/cis105/.claude/settings.json`)

## What Was Done (2026-07-11 Part III drafting session)

* Drafted, adversarially reviewed, QA-gated, committed, and pushed
  chapters 7-9 (all of Part III plus Part IV's opener), one commit per
  chapter:
    * Chapter 7: Networks Everywhere: From Wi-Fi to Satellite Internet
      (`book/chapters/chapter-07.md`, 379 lines, 7,166 words)
    * Chapter 8: Digital Self-Defense: Security, Privacy, and Ethics
      in the AI Era (`book/chapters/chapter-08.md`, 360 lines, 7,452
      words)
    * Chapter 9: How Organizations Turn Data into Decisions
      (`book/chapters/chapter-09.md`, 322 lines, 6,365 words)
* Built three seeded data packs with README data dictionaries, all
  byte-identical on rerun (base seed 105):
    * `assets/code/chapter-07/internet-plans.xlsx`: 54 hand-designed
      plans, 9 fictional providers, 6 technologies
    * `assets/code/chapter-08/security-audit.xlsx`: 25-item audit
      checklist plus 54 anonymized class results
    * `assets/code/chapter-09/coffee-sales.xlsx`: 571 June line items,
      3 locations, 4 weeks, 2 channels
* **Adversarial review protocol (new this session):** each chapter got
  a dedicated reviewer agent instructed to refute its claims: re-run
  the generator, independently recompute every cited number, walk each
  lab step in real Excel semantics, check every law and continuity
  debt. All findings fixed before each commit. Every number in prose
  now traces to an executed value.
* **Generator determinism fix (family-relevant):** openpyxl restamps
  `dcterms:modified` at save time, so the pinned workbook property
  never survived and rebuilds were NOT byte-identical (the Chapter 6
  claim was false as shipped). All generators (6-9) now pin
  `docProps/core.xml` inside the zip-normalization pass. Chapter 6's
  workbook restamped: md5 df9cd5be75e7e7c8d03462cb8aa9e932. Sibling
  books using this pattern should adopt the same fix.
* Glossary grew from 162 to 256 terms (42 in Ch 7, 40 in Ch 8, 12 in
  Ch 9). All Key Terms resolve, verified by script.
* Every chapter passed all QA gates before its commit: blocklist grep,
  zero em dashes, zero banned vocabulary, zero prose semicolons,
  `check_sentence_length.py` zero flags, Flesch in the family band
  (63.2 / 60.6 / 58.1 on the session estimator, which reads 2-4 points
  below the tool used for the Part I/II numbers: shipped chapters
  measure 58.7-63.8 on the same estimator), `zensical build --clean`,
  and a green Pages deploy.
* Uncommented the Part III nav block and the Chapter 9 line of Part IV.
* Further Reading links verified live at draft time (fcc.gov, cisa.gov,
  consumer.ftc.gov, and bls.gov block fetch tools and were verified in
  a browser). Watch item: GCFGlobal now 308-redirects to learnfree.org
  and some paths 404; all five links shipped in chapters 1-6 still
  resolve.

## Key Design Decisions (Part III session)

* **Excel thread progression:** Ch 7 adds relative/absolute references,
  the fill handle, IF, AND, COUNTIF, and the shared-assumption-cell
  pattern. Ch 8 adds charts (column/bar/line/pie, honest axes) and
  cross-sheet references. Ch 9 adds multi-level sort and pivot tables
  (rows/columns/values/filters, Show Values As % of Row Total,
  drill-down double-click, Refresh). Ready for Ch 12's macros.
* **Recurring cast additions:** Rosa (Desert Bloom's roastery contact,
  voice-clone scam target in Ch 8's opening). Desert Bloom is now
  three locations (7th Street original, Roosevelt Row opened spring
  2026, Campus by the college): established in Ch 9.
* **CLO alignment blocks:** Ch 7 = III, VI, XIII. Ch 8 = VI, XI, XIII.
  Ch 9 = XII, IX, XIII.
* **Excel lab submission convention (from Ch 6):** one `.xlsx` with a
  `Questions & Analysis` worksheet, `skills-lab-Na-lastname.xlsx`.
* **Honest-denominators thread:** planted in Ch 7 (cost per Mbps),
  paid again in Ch 9 (weekday/weekend daily averages). The truncated
  axis is taught in Ch 8 by building the lie and labeling it.

## Instructor Answer Keys (Part III)

* **Ch 7 lab (internet-plans):** venue requirements are download 300+,
  upload 30+, latency <= 100 ms, Unlimited. Exactly 13 qualifiers,
  winner IP-103 Sonoran Fiber Home 300 at $65 true cost (runner-up
  Office 500, $75). Sticker minimum IP-138 Basic 25 ($30 advertised,
  $45 true) versus true minimum IP-131 Essential 100 ($40): the flip.
  Essential 100 fails the venue test on download, upload, and cap.
  IP-135 Surge 500 fails on the cap alone. Venue's current plan is
  IP-120 Grand Canal Basic 100 (100/10, $54 true). Cost per Mbps:
  best Pro 2000 ($0.055), worst Rural 10 ($4.70). IF counts: 28 of 54
  uploads >= 20, 44 of 54 in budget at $100 (22 at $60). Q&A 2's
  headroom judgment: either answer defensible with reasoning.
* **Ch 8 lab (security-audit):** class category averages Accounts
  6.39, Devices 7.04 (strongest), Network 5.67, Backups 3.46
  (weakest), Privacy 4.43. Class average total 26.98 of 50. Eight
  students scored 0 in Backups. Honest chart ratio Devices:Backups is
  about 2x, distorted (axis floor 3) about 9x. Student scores vary:
  the rubric grades formulas, charts, and analysis, never the audit
  score itself.
* **Ch 9 lab (coffee-sales):** June total $4,994.75 (7th Street
  $2,088.25, Roosevelt Row $1,515.75, Campus $1,390.75). Campus daily
  averages: $60.17 weekday versus $23.41 weekend (the dip). The other
  two hold or grow their weekends (7th Street $79.94 versus $72.44,
  Roosevelt Row $62.59 versus $50.75), so Q&A 1's "which locations did
  the concealing" has two correct answers. Chain-wide daily averages
  ($183.36 versus $165.94) hide the Campus story. The iced-latte TPS
  example is order DB-1041. The refresh demo edits a Line Total (the
  column ships as static values, not formulas, so a Qty or price edit
  would not reach the pivot). App (Bloom Ahead) revenue share by week: 26.4%,
  41.7%, 51.5%, 60.4%. App average line $11.36 versus counter $7.34.
  Category revenue: Cold Drinks $1,765.75 > Hot Coffee $1,451.75 >
  Bakery $995.75 > Tea $525.50 > Merch $256.00. TIY 9.4 pivot on the
  Ch 6 device file: Laptop 22 (avg $608.09), Desktop 7 ($813.29),
  Tablet 13 ($319.00), Phone 12 ($320.67).

## What Was Done (2026-07-11 Part II drafting session)

* Drafted, QA-gated, committed, and pushed all three Part II chapters,
  one commit per chapter:
    * Chapter 4: What Makes Your Device Run: Operating Systems and
      Utilities (`book/chapters/chapter-04.md`, 538 lines, Flesch 66.4)
    * Chapter 5: Processors, Memory, and the AI PC
      (`book/chapters/chapter-05.md`, 488 lines, Flesch 64.8)
    * Chapter 6: From Touchscreens to the Cloud: Devices and Storage
      (`book/chapters/chapter-06.md`, 440 lines, Flesch 64.9)
* Built the three data packs with README data dictionaries:
    * `assets/code/chapter-04/`: `pitch-outline.docx` and
      `pitch-outline.rtf` (Saguaro Hall pitch outline, Heading 1/2
      styled, three planted flaws; the RTF exists because PowerPoint
      for Mac imports outlines only from RTF)
    * `assets/code/chapter-05/`: `spec-sheets.docx` (source of truth),
      `spec-outline.docx`, `spec-outline.rtf` (three planted flaws)
    * `assets/code/chapter-06/`: `device-comparison.xlsx`, built by
      the course's FIRST seeded generator (see Data Pack Conventions)
* Fixed a latent repo defect: the blanket `*.docx` gitignore rule had
  silently excluded every Part I starter file from the repo. Added an
  `!assets/code/**/*.docx` exception and committed all pack sources.
* Adopted the family rubric rename (Mr. Vega, 2026-07-11): criterion 1
  is now Technical Accuracy and Efficiency, criterion 3 is
  Documentation Quality. Re-synced `book/skills-lab-rubric.md`,
  updated the link block in chapters 2-6 (digest matches the sibling
  books), CLAUDE.md, and the rubric template.
* Glossary grew from 82 to 160 terms (24 in Ch 4, 22 in Ch 5, 32 in
  Ch 6). Inline "(Section N.X)" MLO bindings used in chapters 4-6.
* Every chapter passed all QA gates before its commit: blocklist grep,
  zero em dashes, zero banned vocabulary, zero semicolons,
  `check_sentence_length.py` zero flags, and `zensical build --clean`.
* Uncommented the Part II nav block in `zensical.toml`.

## Key Design Decisions (Part II session)

* **Recurring cast additions (reuse in later chapters):**
    * Saguaro Hall: community event venue, downtown Phoenix, general
      manager Darnell Brooks, events@saguarohall.com, 602-555-0148.
      Bookings return in the Chapter 10 Airtable lab.
    * Cactus Wren Repair: device repair shop two blocks from Saguaro
      Hall, owner Amir Haddad, 1120 E Roosevelt Street,
      hello@cactuswrenrepair.com, 602-555-0173, tech help night first
      Thursday monthly. Its refurb inventory is the Ch 5 deck and the
      Ch 6 workbook, and its devices (Desert Falcon 15, Stone Tower,
      Bloom Pad 11) recur across both labs.
* **CLO alignment blocks:** Ch 4 = II, XIII. Ch 5 = I, VIII, XIII.
  Ch 6 = I, XIII.
* **PowerPoint lab submission convention (Ch 4-5):** two files,
  `skills-lab-Na-lastname.pptx` and `.pdf`. Q&A answers go in the
  NOTES pane of a final Section Header slide, added after the PDF
  export, so the PDF stays a clean deliverable and the notes-pane
  skill gets exercised.
* **Excel lab submission convention (Ch 6, carries to 7-9):** one
  `.xlsx` with a separate `Questions & Analysis` worksheet.
* **Outline imports ship dual-format** (.docx for Windows, .rtf for
  Mac) because Mac PowerPoint imports outlines only from RTF, and
  PowerPoint for the web cannot import outlines at all (noted in labs).
* **Inline MLO bindings:** chapters 4-6 carry "(Section N.X)" on every
  MLO line per the family standard. Chapters 1-3 do not yet (pending
  decision below).

## Instructor Answer Keys (Part II)

* **Ch 4 pitch outline planted flaws:** (1) "Why Saguaro Hall Works"
  carries 9 bullets (students split it into two slides), (2) one
  37-word spoken-sentence bullet on "What a Booking Includes" (the
  audio-visual setup sentence, belongs in speaker notes), (3) "The
  Numbers" sits before "What a Booking Includes" (price before value,
  students reorder). A clean import produces 9 slides from 32 bullets.
* **Ch 5 spec outline planted flaws:** (1) Desert Falcon 15 bullet
  says "512 GB of memory" (truth per spec-sheets.docx: 512 GB storage,
  16 GB RAM), (2) "BIOS version 2.31" is the customer-useless bullet
  (moves to notes), (3) "Side by Side" is the wall-of-numbers slide.
  Import produces 9 slides from 36 bullets. Intended profile matches:
  Note-Taker = Desert Falcon 15 (battery, NPU), Creator = Stone Tower
  (cores, GPU, and the "add memory next year" plan WORKS on it: four
  slots, upgradeable to 64 GB), Kitchen Browser = Bloom Pad 11.
* **Ch 6 workbook summary values:** COUNTA(A2:A55)=54,
  SUM(H2:H55)=27066 ($27,066), AVERAGE(H2:H55)=$501.22,
  MIN=89 (Cactus Call Mini, CW-1044), MAX=1299 (Saguaro Workstation,
  CW-1001), COUNT(G2:G55)=47, AVERAGE(G2:G55)=86.11 rounded (7 desktop
  battery cells are blank by design). Laptop filter count: 22 of 54.
  Maya's tablet filter (Tablet, price under $400, battery 85+) leaves
  7 devices: CW-1011, CW-1018, CW-1021 (Bloom Pad 11), CW-1023,
  CW-1030, CW-1040, CW-1049. Cast rows: CW-1019 Desert Falcon 15,
  CW-1029 Stone Tower.

## What Was Done (2026-07-11 Part I drafting session)

* Drafted, QA-gated, committed, and pushed all three Part I chapters,
  one commit per chapter:
    * Chapter 1: People, Data, and Intelligent Machines
      (`book/chapters/chapter-01.md`, 515 lines)
    * Chapter 2: The Web at Work: Search, Communication, and
      E-commerce (`book/chapters/chapter-02.md`, 446 lines)
    * Chapter 3: Apps and AI Copilots: Choosing the Right Tool
      (`book/chapters/chapter-03.md`, 378 lines)
* Built the three data packs with README data dictionaries:
    * `assets/code/chapter-01/`: `letter-content.docx` (draft letter
      with planted errors), `app-fact-sheet.docx` (12 facts)
    * `assets/code/chapter-02/`: `ai-briefing.docx` (8-claim AI-style
      briefing authored for the course)
    * `assets/code/chapter-03/`: `bookstore-report.docx` (unstyled
      report for the styles/TOC lab)
* Populated `book/glossary.md`: 82 terms across Chapters 1-3.
* Uncommented the Part I nav block in `zensical.toml` (all three
  chapters live) and the Getting Started link in `book/index.md`.
* Every chapter passed all QA gates before its commit: blocklist grep
  (clean), zero em dashes, zero banned vocabulary, zero semicolons,
  `check_sentence_length.py` (zero flagged), and
  `zensical build --clean` (no issues).

## Key Design Decisions (Part I session)

* **Recurring cast (reuse in later chapters):** Desert Bloom Coffee,
  the Phoenix-area coffee shop. Owner Maya Reyes. Mobile ordering app
  "Bloom Ahead" (launched October 5, Petal Points loyalty, address
  4210 N 7th Street). The campus bookstore is managed by Elena
  Fuentes. Chapters 1-3 cross-reference these continuously.
* **CLO alignment blocks** quote the elevated CLO wording with RBT
  tags: Ch 1 = X, II, XIII. Ch 2 = IV, V, VI. Ch 3 = II, IX, XIII.
* **Chapter length:** the ~600-line target was treated as a ceiling,
  not a quota. Part I lands at 378-515 dense lines, inside the family
  band (published CIS133 chapters run 425-543). No padding was added
  to chase the number.
* **Word lab thread progression:** Ch 1 letter from a blank page
  (format, edit, deliver as PDF). Ch 2 memo (header block, findings
  table, footer, bottom line up front). Ch 3 styles, self-updating
  table of contents, Navigation Pane, and comments. Each lab reuses
  the previous chapter's habits (pre-send inspection, Editor plus
  read-aloud, descriptive file names).
* **Submission convention (all labs):** two files,
  `skills-lab-Na-lastname.docx` and `.pdf`. Questions & Analysis
  answers go on a final page of the docx. The PDF is exported before
  that page is added, so it stays a clean deliverable.
* **AI-tool convention honored:** the Ch 2 briefing ships in the data
  pack (authored for the course in AI-output style), no lab step
  requires an AI account or paid tool, and Try It Yourself AI
  exercises use free search-engine answer boxes.
* **Ch 2 briefing answer key (instructor reference):** claims 2, 3,
  5, and 7 are true. Claims 1, 4, 6, and 8 are false. Students verify
  five of the eight.
* **Ch 1 letter planted errors (instructor reference):** three
  misspellings (recieve, convienience, apreciate), one wrong word
  Editor may miss (exited for excited), and "Desert Bloom Cafe" twice
  so Replace All reports 2 replacements.
* **Word starter files are committed artifacts**, authored via pandoc
  from markdown drafts. No generator scripts yet (the `_generators/`
  convention starts when a lab needs seeded tabular data, likely
  Chapter 6).

## Earlier Sessions (2026-07-11 scaffold and retitle)

* Repo instantiated from the family template, shared files synced,
  `docs/CIS105_CLOs.md` built from the district outline.
* Title freshness rule executed: `docs/legacy-title-blocklist.md`
  bans every heading from the old Computing Essentials build, with a
  grep check run before every chapter commit.
* `docs/part-structure.md` is authoritative for part names, chapter
  titles, subtitles, content bullets, CLO alignment, and Skills Lab
  titles.

## Pending Decisions

* Canvas assessment weights: part-structure.md carries the Spring
  2026 proportions as a starting point. Confirm when the Canvas shell
  is rebuilt.
* Exam placement (2 vs 3 unit exams) across the 14-week schedule.
* License for the published book (README has a TODO; siblings can
  guide, for example CC BY-NC-SA 4.0).
* Retrofit inline "(Section N.X)" MLO bindings to chapters 1-3 so all
  chapters match the family standard (chapters 4-6 already carry
  them). Nine mechanical edits, held for Mr. Vega's approval because
  MLO lines feed Canvas alignment.

## Next Steps (Part IV remainder: Chapters 10-12)

1. Draft Chapter 10 (Where Data Lives: Tables, Records, and
   Relationships) from its block in `docs/part-structure.md`. Skills
   Lab 10 (Airtable): From CSV to Connected Base. Needs pack CSVs
   (customer orders and Saguaro Hall bookings). The lab thread turns
   to Airtable (free plan features only).
2. Cross-references Chapter 10 must pay: Ch 9's Looking Ahead (pivot
   questions become queries, Saguaro Hall's bookings get a base,
   Bloom Ahead sits on a database), Ch 1's Airtable cloud-login
   difference ("Chapter 10 examines up close"), Ch 6's filter-view
   line ("the first taste of the database questions Chapter 10 asks
   properly"), and Ch 8's CLO VI support (data security in databases
   per the coverage matrix).
3. Chapter 11 (From Idea to Rollout) then Chapter 12 (Automate Your
   Work: macros, VBA, AI coding assistants; requires desktop Excel,
   noted since Ch 6). Chapter 12 is the capstone: check C9's
   integrated-deliverable expectation when drafting its lab.
4. Per chapter, keep the Part III pattern: plan (MLO bindings,
   misconception inventory, continuity ledger), seeded data pack with
   README, glossary additions, nav uncomment, dedicated adversarial
   reviewer agent, all QA gates, one commit, push.
5. Bloom's per part-structure: Part IV finishes Apply through Create
   (Create belongs to Ch 12's macro work).

## How to Continue

Start a session in `/Users/vega/Documents/code/textbooks/cis105/`.
Read `CLAUDE.md`, this file, and `docs/part-structure.md`. The repo is
self-contained: the blocklist and part-structure encode everything
needed from the retired build. Old lecture notes in
`../cis105-old-reference-docs/` are concept reference only, never
title reference (new Chapter 6 merges old modules 6 and 7, and new
Chapters 7-12 map to old 8-13).

## Data Pack Conventions

* Word starter files: committed `.docx` artifacts in
  `assets/code/chapter-NN/`, authored via pandoc (with hand-built
  `.rtf` twins for PowerPoint outline imports on Mac). Every folder
  has a README data dictionary (contents, types, source, license).
  Note the gitignore exception `!assets/code/**/*.docx` that keeps
  them committed past the build-output `*.docx` rule.
* Generators live in `assets/code/_generators/`. **Base seed: 105.**
  First generator: `generate_chapter06_data.py` rebuilds
  `assets/code/chapter-06/device-comparison.xlsx` byte-identically
  (md5 df9cd5be75e7e7c8d03462cb8aa9e932, restamped 2026-07-11 when the
  generators gained pinned core.xml timestamps), with asserts on every
  engineered property. Rebuild command, from the repo root:

  ```bash
  python3 assets/code/_generators/generate_chapter06_data.py
  ```

* Mr. Vega uploads data pack zips to Canvas manually. Keep sources
  committed and local zips current (rebuild command in
  `assets/code/_generators/README.md`).

## Build

```bash
.venv/bin/zensical build --clean   # local check
.venv/bin/zensical serve           # preview at http://localhost:8000
```

Push to `main` deploys via `.github/workflows/docs.yml`.
