# CIS105 Textbook: Session Handoff

**Last updated:** 2026-07-11
**Repo:** https://github.com/jor2050111/cis105
**Live site:** https://jor2050111.github.io/cis105/
**Task list:** CLAUDE_CODE_TASK_LIST_ID=cis105 (pinned in
`/Users/vega/Documents/code/textbooks/cis105/.claude/settings.json`)

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

## Next Steps (Part II: Under the Hood, Chapters 4-6)

1. Draft Chapter 4 (What Makes Your Device Run: Operating Systems and
   Utilities) from the Chapter 4 block in `docs/part-structure.md`.
   The lab thread moves to PowerPoint: Skills Lab 4 builds the event
   venue's pitch deck from a provided outline, so the chapter-04 data
   pack needs that outline file (the event venue business gets named
   here; keep the recurring-cast pattern).
2. Chapter 5 (Processors, Memory, and the AI PC) continues PowerPoint
   with the device repair shop's spec-sheet visuals.
3. Chapter 6 (From Touchscreens to the Cloud: Devices and Storage)
   starts the Excel thread with `device-comparison.xlsx` and likely
   the first `_generators/` script (seeded tabular data, 50+ rows).
4. Per chapter, follow the Part I pattern: template structure, data
   pack with README, glossary additions, nav uncomment, all QA gates,
   one commit, push.
5. Ch 1 Looking Ahead promises Ch 4 previews OS-level AI assistants
   and privacy (part-structure lists it). Keep the cross-references
   honest when drafting.

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
  `assets/code/chapter-NN/`, authored via pandoc. Every folder has a
  README data dictionary (contents, types, source, license).
* Generators live in `assets/code/_generators/` (none yet). Base
  seed: not yet assigned. Document the seed and rebuild command here
  when the first generator lands (expected with Chapter 6's Excel
  data).
* Mr. Vega uploads data pack zips to Canvas manually. Keep sources
  committed and local zips current.

## Build

```bash
.venv/bin/zensical build --clean   # local check
.venv/bin/zensical serve           # preview at http://localhost:8000
```

Push to `main` deploys via `.github/workflows/docs.yml`.
