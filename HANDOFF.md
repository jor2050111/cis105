# CIS105 Textbook: Session Handoff

**Last updated:** 2026-07-11
**Repo:** https://github.com/jor2050111/cis105
**Live site:** https://jor2050111.github.io/cis105/
**Task list:** CLAUDE_CODE_TASK_LIST_ID=cis105 (pinned in
`/Users/vega/Documents/code/textbooks/cis105/.claude/settings.json`)

## What Was Done (2026-07-11 retitle session, later the same day)

* Executed Mr. Vega's directive: no title or heading may match the old
  Computing Essentials build, and the book should teach the district
  outline through a 2026 lens (AI reshaping every major's work).
* Extracted every bold heading from the 13 old-notes docx files and
  the old SIMnet assignment titles into
  `docs/legacy-title-blocklist.md` (banned list + grep check).
* Rewrote `docs/part-structure.md`: new part names (Your Digital
  Toolkit, Under the Hood, Connected and Protected, Data, Decisions,
  and Automation), 12 fresh chapter titles, refreshed content bullets
  with 2026 threads (AI copilots, answer engines, NPUs and AI PCs,
  passkeys, deepfakes, AI agents in business, AI coding assistants),
  and a named Skills Lab title for each chapter. Chapter ORDER and
  all coverage matrices are unchanged.
* Updated `book/index.md`, `zensical.toml` (nav + description),
  `README.md`, and `CLAUDE.md` (purpose, audience note, Tech in Your
  Field admonition, Title Freshness Rule, AI terminology, checklist).
* Added to `docs/style-guide.md`: a neighborhood health clinic example
  domain and the AI-tool convention (no paid AI subscription in labs,
  AI samples ship in the data pack).
* Verified the site build (`zensical build --clean`).

## What Was Done (2026-07-11 scaffold session)

* Instantiated this repo from
  `/Users/vega/Documents/code/textbooks/template/` following
  `NEW-TEXTBOOK-SETUP.md` (interview completed with Mr. Vega, all
  placeholder tokens replaced, acceptance grep clean).
* Ran `../shared/tools/sync-shared.sh .` (all synced files current)
  and seeded `docs/blooms-taxonomy-reference.md`.
* Built `docs/CIS105_CLOs.md` from
  `/Users/vega/Documents/code/textbooks/cis105-old-reference-docs/cis105-course-outline.md`:
  official description, 13 elevated CLOs with Bloom's tags, district
  CLOs verbatim, CLO-to-chapter mapping, full district outline.
* Authored `docs/part-structure.md` (authoritative 12-chapter plan),
  `book/index.md` (home page with CLO listing and Part summaries),
  `docs/style-guide.md` (course layer), and the course-configured
  sections of `CLAUDE.md`.
* Created the GitHub repo, enabled Pages (build_type=workflow),
  verified the local build (`zensical build --clean`, no issues), and
  confirmed the Actions deploy and live site (HTTP 200).

## Key Design Decisions

* **Title freshness rule (2026-07-11):** no part, chapter, section,
  or assignment title reproduces a heading from the old build. Banned
  list and grep check: `docs/legacy-title-blocklist.md`. Concepts
  stay, names change.
* **2026 reframe (2026-07-11):** every chapter carries an AI-era
  thread, and every chapter includes one "Tech in Your Field"
  admonition connecting the topic to the majors enrolled in the course
  (about half Business and Entrepreneurship, a quarter BAS-IT, the
  rest across health, science, arts, and public-service majors).
  Through-line: roles are changing, not disappearing, and judgment
  stays with the student.
* **12 chapters in 4 Parts** (family standard). Old modules 6
  (Input/Output) and 7 (Secondary Storage) merged into Chapter 6.
  Every other module from the previous 13-module Computing Essentials
  build keeps its taught order. Full rationale in
  `docs/part-structure.md`.
* **Airtable replaces Microsoft Access** (Mr. Vega's standing
  decision, recorded twice in the source outline).
* **Skills Lab app thread** covers CLO XIII: Word (Ch 1-3),
  PowerPoint (Ch 4-5), Excel (Ch 6-9), Airtable (Ch 10-11), Excel
  macros with VBA (Ch 12).
* **VBA and macros live in Chapter 12** with programming concepts
  (CLO VII, outline section V).
* **Bloom's focus:** full RBT range, early chapters lean Remember
  through Apply (recorded in CLAUDE.md and docs/part-structure.md).
* **Flesch band:** 60-70, leaning toward the top.
* **Task list ID is plain `cis105`** (no term suffix) per Mr. Vega's
  setup answer: repo name, site subpath, folder, and task list all
  match.
* **Example domains:** recurring small businesses (Phoenix-area
  coffee shop, campus bookstore, device repair shop, event venue).
  See `docs/style-guide.md`.

## Pending Decisions

* Canvas assessment weights: part-structure.md carries the Spring
  2026 proportions as a starting point. Confirm when the Canvas shell
  is rebuilt.
* Exam placement (2 vs 3 unit exams) across the 14-week schedule.
* License for the published book (README has a TODO; siblings can
  guide, for example CC BY-NC-SA 4.0).

## Next Steps

1. Draft Chapter 1 (People, Data, and Intelligent Machines) from
   `templates/chapter-template.md` and the Chapter 1 block in
   `docs/part-structure.md`. Old lecture notes are concept reference
   only, never title reference:
   `/Users/vega/Documents/code/textbooks/cis105-old-reference-docs/chapter-01-old-notes.docx`.
   Before commit, run the heading check in
   `docs/legacy-title-blocklist.md`.
2. Build the Chapter 1 data pack folder (`assets/code/chapter-01/`)
   with the Word starter file and a README data dictionary.
3. Uncomment the Chapter 1 nav line in `zensical.toml` and the
   Getting Started link in `book/index.md` when the chapter lands.
4. Add Chapter 1 key terms to `book/glossary.md`.
5. Repeat per chapter, following the lab thread order.

## How to Continue

Start a session in `/Users/vega/Documents/code/textbooks/cis105/`.
Read `CLAUDE.md`, this file, and `docs/part-structure.md`. The old
lecture notes for every chapter live in
`/Users/vega/Documents/code/textbooks/cis105-old-reference-docs/`
(chapter-NN-old-notes.docx map to old module numbers: new Chapter 6
merges old 6 and 7, and new Chapters 7-12 map to old 8-13).

## Data Pack Conventions

* Generators live in `assets/code/_generators/` (none yet). Base seed:
  not yet assigned. Document the seed and rebuild command here when
  the first generator lands.
* Mr. Vega uploads data pack zips to Canvas manually. Keep generator
  sources committed and local zips current.

## Build

```bash
.venv/bin/zensical build --clean   # local check
.venv/bin/zensical serve           # preview at http://localhost:8000
```

Push to `main` deploys via `.github/workflows/docs.yml`.
