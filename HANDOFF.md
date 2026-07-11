# CIS105 Textbook: Session Handoff

**Last updated:** 2026-07-11 (Chapter 12 capstone session: THE BOOK IS COMPLETE)
**Repo:** https://github.com/jor2050111/cis105
**Live site:** https://jor2050111.github.io/cis105/
**Task list:** CLAUDE_CODE_TASK_LIST_ID=cis105 (pinned in
`/Users/vega/Documents/code/textbooks/cis105/.claude/settings.json`)

## What Was Done (2026-07-11 Chapter 12 capstone session)

* Drafted, adversarially reviewed, QA-gated, and committed Chapter 12,
  the Part IV closer and course capstone:
    * Chapter 12: Automate Your Work: Macros, VBA, and AI Coding
      Assistants (`book/chapters/chapter-12.md`, 7,7xx words). All 12
      chapters now exist: the book is content-complete.
* **Codex-in-the-loop protocol (new this session, via the
  codex@openai-codex plugin):** the chapter DESIGN went to a Codex
  adversarial task (xhigh, 9 minutes) BEFORE drafting and came back
  with 33 findings. About 20 were adopted at outline cost instead of
  rewrite cost: click-level lab precision (active-sheet recovery after
  sheet duplication, This Workbook, blank shortcut key, whole-column
  Currency selection), cross-platform macro-security wording (Windows
  Mark-of-the-Web hard block versus Mac ask-first), accuracy hedges
  (recorder-output variance, assembly mapping, compiler/interpreter
  blend, JavaScript beyond the browser, survivorship framing instead
  of "quiet errors cost more"), MLO single-verb discipline, CLO XIII
  inclusion, a student-designed IMPROVEMENT step to earn the Create
  tag, TIY 12.1 branch coverage, and the four-number evidence block.
  Declined with reasons: dropping the language-history or design-tools
  sections (district outline section V mandates both) and removing the
  September-label breadcrumb (intentional scaffold). A second Codex
  read-only review ran on the final working-tree diff before commit.
* **Adversarial reviewer agent (the Part III/IV protocol):** a
  dedicated agent instructed to REFUTE the chapter across five attacks
  (numbers vs the shipped workbook, desktop Excel + VBA realism on
  Windows and macOS, domain accuracy, style law + pedagogy, continuity
  + links). Attack 1 recomputed every cited figure independently from
  the shipped xlsx with zero mismatches. Findings: 2 REQUIRED (a
  self-contradicting "below the data (try L10)" ground-truth
  instruction that could poison the lastRow repair if a student put
  the scratch SUM in column A, and "the owner's desk" contradicting
  Darnell's established general-manager title), plus 5 adopted
  JUDGMENT items (Move or Copy rename gap, Trusted-Documents reopen
  nuance, "most laptops" -> "most common laptop processor family",
  VBA-in-all-desktop-apps overbreadth softened in chapter AND
  glossary, live/solo wording wobble). All fixed before scoring.
* **Data pack (`assets/code/chapter-12/`):** `booking-export.xlsx`
  (October 2026, 63 bookings x 10 columns, sheet `OctoberExport`,
  date-sorted, no cancellations, no contact columns) plus
  `ai-macro-draft.txt` (Renee's September prompt and the assistant's
  drafted `SummarizeExport`, hardcoded to rows 2-61 because HER PROMPT
  said so: the stale assumption is earned, not a strawman). Generator
  `generate_chapter12_data.py` (seed 105) IMPORTS the Chapter 10
  generator so the pricing model, org cast, and the four inherited
  October bookings (SH-1016/1017/1040/1041, verbatim to the base) can
  never drift. Byte-identical on rerun, asserts pin every cited
  number, and the draft's exact expressions were also executed in real
  desktop Excel against the shipped workbook via the Excel MCP
  (=SUM(J2:J64)=83,910; =SUM(J2:J61)=78,510; =COUNTA(A2:A61)=60;
  =COUNTA(A2:A64)=63), with the file closed unsaved (md5 unchanged).
* **Retro-edit to Chapter 11 (one sentence, line ~223):** "Chapter 12
  will have you do exactly that" promised drafting an Airtable formula
  or reminder script; the shipped Chapter 12 has students VERIFY an
  AI-drafted Excel macro instead. The sentence now reads "Chapter 12
  hands you code drafted exactly this way, then asks whether to trust
  it," which the Codex design review flagged and the chapter pays
  exactly.
* Glossary grew 300 to 324 headwords (+24, including a new `## J`
  section for JavaScript). Every Key Terms entry resolves (all 24,
  verified by script). CLO block carries four CLOs (VII primary + IV,
  IX, XIII): part-structure lists VII/IV/IX and the CLO mapping
  threads XIII through the Chapter 12 lab, so the block is the
  superset, matching how chapters 10-11 added their thread CLO.
* QA gates all passed: zero em dashes, zero prose semicolons, zero
  banned vocabulary (the sweeps caught "very" and a "rather than"
  during drafting), asterisk bullets, `check_sentence_length.py` zero
  flags (446 sentences, avg 16.0, longest 34; 18 overlong sentences
  split during drafting), Flesch 66.3 on the session estimator
  (calibrated band 62.0-67.1, leaning top), title blocklist clean (the
  old module 13 "Step N: Program..." / "Syntax error" / "Logic error"
  headings all avoided: those concepts are taught inline), `zensical
  build --clean` clean, chapter in nav and search.
* Further Reading verified live in a browser at draft time (Microsoft
  quick-start macro page, Microsoft Learn getting-started-with-VBA and
  internet-macros-blocked, BLS Software Developers OOH, MDN What is
  JavaScript). Two labels corrected after loading: the macro-block
  page is Microsoft Learn (not Support), and the BLS page's real title
  is "Software Developers, Quality Assurance Analysts, and Testers."
* Try It Yourself 12.2 claims the course site itself ships JavaScript:
  verified against the built page (6 `<script>` tags in
  `site/chapters/chapter-12/index.html`).
* Data-pack zip rebuilt (52 files) with chapter 12. Chapter 12 nav
  line uncommented in `zensical.toml`. Generator inventory table
  updated.
* **Whole-book evaluation:**
  `evaluations/cis105-2026-07-11-ch12-and-whole-book-scored-rubric.md`
  (workspace root) scores Chapter 12 and stamps the completed book.

## Instructor Answer Key (Chapter 12)

* **Ground truth on `booking-export.xlsx`:** 63 bookings, total quoted
  revenue $83,910. Status-bar count of column A reads 64 (header + 63).
  Data occupies A2:J64.
* **What the shipped AI draft reports when run on October:** 60
  bookings and $78,510, labeled "September Summary," written to L1:M3.
  It runs with no error message. The miss is $5,400 (6.4 percent of
  the month): the last three rows, which the hardcoded J2:J61 range
  cannot see.
* **The three missed bookings (sheet rows 62-64):** SH-1071 (Oct 30,
  Main Hall, Central Library Friends fundraiser, $2,750), SH-1081
  (Oct 31, Main Hall, Las Artes Folklórico concert, $1,500), SH-1085
  (Oct 31, Courtyard, Phoenix Pride Alliance fundraiser, $1,150).
* **Root cause students should state:** Renee's September prompt said
  "the data runs from row 2 to row 61," true for September's 60
  bookings, false for October's 63. The draft did what it was told,
  and what it was told went stale. Logic error (nothing crashed).
* **The durable repair:** `lastRow = Cells(Rows.Count,
  "A").End(xlUp).Row` with both ranges rebuilt via `& lastRow` and a
  month-free label. The full repaired skeleton is printed in lab step
  Part 3.5. After repair: 63 and $83,910, matching ground truth, and
  a second run leaves one summary (fixed cells L1:M3).
* **TIY 12.1 answers:** zero of October's 63 rows flag (the venue
  books within capacity after Chapter 10's overflows); the hypothetical
  175-in-Courtyard flags (capacity 150). "Nothing flagged" is the
  program succeeding, echoing Chapter 11's audit line.
* **TIY 12.2:** the built course pages carry `<script>` tags (search,
  instant navigation, the palette toggle are script behaviors).
* **Part 2 deliberate break:** removing the closing quote raises a
  loud compile/syntax complaint (possibly the moment the student
  leaves the line, if Auto Syntax Check is on) and NOTHING runs.
  Contrast with Part 3's silent wrong number is the point of Q&A 1.
* **Q&A 2 has no single right answer:** grade the application of the
  three-part automation test, the named verifier, and the cost of a
  quiet wrong answer in the student's own field.
* **Grading note:** students submit `.xlsm`. Canvas downloads carry
  Mark of the Web on Windows, so expect the security banner when
  opening submissions; the VBA project is still readable in the VBE
  without enabling anything, which is all grading needs.

## Key Design Decisions (Chapter 12 session)

* **The capstone integrates the term instead of adding a new domain:**
  the lab automates the exact ritual the Part IV story produced (the
  monthly export of the Chapter 10 base, whose rollout Chapter 11
  tracked), with ground-truth habits from Chapters 6 and 9 (status-bar
  count, SUM check) as the verification tools, and the Chapter 1
  "tools draft, you decide" loop closed explicitly in 12.4 and the lab.
* **Two-defect pedagogy, one artifact:** students BUILD the loud error
  themselves (Part 2's deliberate broken quote) and DISCOVER the quiet
  one in code they did not write (Part 3). Syntax versus logic errors
  are taught by survivorship (a crash interrupts you; a wrong answer
  interrupts nobody), never as a universal cost ranking.
* **The AI draft ships as plain text** so nothing in the pack is a
  runnable macro, no student enables foreign code, and every student
  verifies the same artifact (course AI-tool convention: no AI account
  required).
* **Summary block lives in L1:M3** (fixed cells, columns L:M) so the
  buggy and repaired macros are both idempotent and the column-A
  lastRow pattern can never be contaminated by the macro's own output.
* **Looking Ahead is the course send-off** (the cis360/cis133 capstone
  pattern): no next chapter to preview, so it closes the Chapter 1
  loop and hands students the habit ("your field is full of
  twenty-minute rituals nobody has questioned yet").
* **Timeline:** the base went live after the parallel run Chapter 11's
  lab recommended; October 2026 is its first full month solo; Renee's
  September export (60 bookings) existed inside the parallel period.
  The Chapter 10 base's four October advance bookings appear in the
  export verbatim, and the other 59 IDs continue from SH-1061.

## What Was Done (2026-07-11 Part IV drafting session: chapters 10-11)

* Drafted, adversarially reviewed, QA-gated, and committed chapters 10-11
  (Part IV's database and systems-planning chapters):
    * Chapter 10: Where Data Lives: Tables, Records, and Relationships
      (`book/chapters/chapter-10.md`, 6,338 words)
    * Chapter 11: From Idea to Rollout: Planning Technology Solutions
      (`book/chapters/chapter-11.md`, 6,210 words)
* Lab thread turned to Airtable (free-plan features only, CLO XIII).
  Ch 10 lab "From CSV to Connected Base" imports two CSVs, builds the
  linked relationship, typed views, and a least-privilege form. Ch 11
  lab "Track the Project" runs a systems tracker: group by phase,
  Kanban by status, calendar, find the overdue and the at-risk task,
  write a go/no-go readout.
* Built two seeded CSV data packs (base seed 105, stdlib only, no
  openpyxl), byte-identical on rerun, each with a README data
  dictionary:
    * `assets/code/chapter-10/`: `saguaro-bookings.csv` (60x13,
      denormalized "before") and `saguaro-customers.csv` (24x6
      dimension). Referential integrity for a clean Airtable link, 17
      repeat organizations, one planted phone drift (SH-1005), a
      reproducible pricing model, two capacity overflows.
    * `assets/code/chapter-11/`: `project-tasks.csv` (54x11), Saguaro
      Hall's rollout across the six life-cycle phases (9 each), one
      at-risk task (T-140 In Progress ahead of the unstarted T-136),
      11 overdue on the 2026-07-11 status date.
* **Adversarial review protocol (per chapter):** a dedicated reviewer
  agent instructed to REFUTE the chapter across five attacks (numbers
  vs CSV, Airtable free-plan lab realism, domain accuracy, style law
  plus pedagogy, continuity plus links). Ch 10: 4 REQUIRED + 6 JUDGMENT.
  Ch 11: 2 REQUIRED + 7 JUDGMENT. All REQUIRED fixed and sound JUDGMENT
  adopted before scoring (see the Part IV evaluation). The Ch 10 review
  is the exemplar of why the protocol exists: it caught the chapter
  teaching that an Airtable email field rejects a phone number (it does
  not) and an opening scenario that contradicted the shipped drift row.
* **Airtable accuracy guardrails (family-relevant, from the Ch 10
  review):** Airtable does NOT strictly validate typed fields or enforce
  primary-key uniqueness, and a linked field on a Form lets a submitter
  search the linked table. Chapters now teach validation and keys as
  database CONCEPTS and credit the DESIGN (normalization) as the real
  safeguard, and the intake form uses a plain text field for the
  organization. Sibling Airtable labs should inherit these caveats.
* Glossary grew 255 to 299 terms (44 new across the two chapters), with
  a new `## Q` section. Every Key Terms entry resolves (Ch 10 all 25,
  Ch 11 all 16), verified by script.
* Every chapter passed all QA gates: zero em dashes, zero prose
  semicolons, zero banned vocabulary, asterisk bullets,
  `check_sentence_length.py` zero flags, Flesch in band (66.7 / 65.8 on
  the session estimator, which reads ~3.3 above the recorded house
  estimator, so the band is ~62.0-67.1), title blocklist clean,
  `zensical build --clean` clean, both chapters in nav and search.
* Further Reading verified live in a browser at draft time (Airtable
  getting-started, linking-records, and views; FTC; both BLS OOH pages;
  Wikipedia SDLC). Two dead URLs were caught and replaced: Ch 10's
  `creating-different-views` (404) became `getting-started-with-airtable-views`,
  and Ch 11's GCF `beginning-a-project` (404 via the learnfree redirect)
  became the Wikipedia SDLC overview.
* Uncommented the Part IV nav block for chapters 10-11 in
  `zensical.toml` (Chapter 12 stays commented until drafted).
* Data-pack zip rebuilt (47 files) with chapters 10-11.
* **Part IV evaluation:** `evaluations/cis105-2026-07-11-part4-scored-rubric.md`
  (workspace-root repo) scores chapters 10-11 at **97.6/100,
  Publication-ready**, every fixable axis at 5, C10 capped at 3 (no
  images shipped anywhere in the book).
* **Commit note:** chapters 10-11 were committed together in one Part IV
  commit, because the glossary merge interleaved both chapters' terms
  alphabetically and the shared nav references both files, so a clean
  per-chapter split would leave an intermediate commit whose nav points
  at a missing file. The Airtable lab thread spans both chapters.

## Key Design Decisions (Part IV session)

* **Airtable submission convention (Ch 10-11):** the base lives in the
  cloud, so the deliverable is a read-only shared VIEW LINK plus a PDF
  (`skills-lab-NNa-lastname.pdf`) holding the link, three screenshots,
  the written plan or readout, and the two Q&A answers. This makes
  Chapter 1's "cloud trades the file for a login" concrete.
* **Recurring cast additions:** the Ch 11 project team is Renee Salazar
  (Saguaro Hall's office manager) and Sam Ortiz (a hired IT consultant),
  alongside Darnell Brooks (GM, the project sponsor). Ch 10's customer
  list seeds cross-cast cameos: Desert Bloom Coffee, Cactus Wren Repair,
  and the college bookstore all book the venue.
* **CLO alignment blocks:** Ch 10 = XIII, VI, X. Ch 11 = VIII, IX, XIII.
* **Bloom escalation across Part IV:** Ch 10 tops at Analyze (MLO-10.3),
  Ch 11 reaches Evaluate (MLO-11.3), and Ch 12 will reach Create (the
  macro work). This matches the part plan's Apply-through-Create arc.
* **Data-quality-by-design thread:** Ch 10 plants a copied-then-drifted
  phone (SH-1005) and pays it in the lab (link once, drift gone). Ch 11
  plants an at-risk task (parallel run started before data is loaded)
  that students find by comparing a task's status to its dependency's.

## Instructor Answer Keys (Part IV)

* **Ch 10 lab (saguaro bookings + customers):** 60 bookings, 24 orgs.
  City of Phoenix Parks books most (6), then Phoenix Camera Club (5). 17
  of 24 booked more than once. SH-1005 is the sole phone drift (booking
  says 602-555-0117, the Customers table holds the correct
  602-555-0110). Status: Completed 27, Confirmed 15, Pending 12,
  Cancelled 6. Space: Courtyard 24, Main Hall 19, Meeting Room 17.
  Quoted total $81,060, realized (non-cancelled) $73,780. Over-capacity:
  SH-1009 (175 in the 150-seat Courtyard, Cancelled) and SH-1052 (52 in
  the 40-seat Meeting Room, Completed). Pricing = space rate x hours +
  package fee + add-on fees (rates: Main Hall $200, Courtyard $150,
  Meeting Room $60 per hour; Bronze $0, Silver $350, Gold $750; add-ons
  AV $150, Catering $500, Decor $300, Extra Staff $200, Parking $100).
* **Ch 11 lab (project-tasks):** 54 tasks, 9 per phase across the six
  phases. Status: Done 28, In Progress 5, Blocked 2, Not Started 19.
  Priority: High 27, Medium 23, Low 4. Total 246 hours (by phase:
  Investigation 43, Analysis 45, Design 42, Development 42,
  Implementation 40, Maintenance 34). At-risk task: T-140 (Run the old
  and new systems in parallel, In Progress) depends on T-136 (Load the
  historical bookings, Not Started). Overdue on 2026-07-11: 11 tasks, 6
  High priority. The plan chose parallel conversion (T-137 Done). The
  Q&A go/no-go answer: not ready to cut over (finish Development, run
  parallel), defended from the overdue and at-risk signals.

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

## Next Steps (Part IV finale: Chapter 12, the capstone)

1. Draft Chapter 12 (Automate Your Work: Macros, VBA, and AI Coding
   Assistants) from its block in `docs/part-structure.md`. The lab
   thread returns to Excel and requires desktop Excel (Excel for the
   web cannot record or run macros, noted since Ch 3 and Ch 6). Skills
   Lab 12: Record It, Read It, Rewrite It (record a macro, then edit
   and explain it in the Visual Basic Editor).
2. Cross-references Chapter 12 must pay: Ch 11's Looking Ahead (record
   a macro, read the generated code, put an AI coding assistant to
   work, verify code you did not write), Ch 2's HTML/web-scripting tie,
   Ch 3's "Excel for the web cannot run the macros Chapter 12 teaches,"
   and the Excel skills built across Ch 6-9. Grep chapters 1-11 for
   every literal "Chapter 12" promise before drafting.
3. Chapter 12 is the capstone: it must reach Create-level Bloom work
   (the macro students write and defend) and carry an integrated
   deliverable that ties the term together (check the C9
   integrated-capstone expectation in the quality instrument).
4. Keep the Part III/IV pattern: plan (MLO bindings, misconception
   inventory, continuity ledger), seeded data pack with README (VBA
   labs need desktop-Excel starter workbooks, not CSVs), glossary
   additions, nav uncomment, a dedicated adversarial reviewer agent
   instructed to refute, all QA gates, commit, push.
5. After Chapter 12, run the whole-book stamp against the quality
   instrument (the Part IV taper watch is clear through Ch 11; the
   capstone's integrated deliverable is the remaining C9 risk), and
   consider shipping the first annotated screenshots (Airtable and VBA
   labs are the strongest candidates), which would lift the book-wide
   C10 alt-text cap from 3.

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
