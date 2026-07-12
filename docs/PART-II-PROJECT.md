Draft and publish Part II of the CIS105 textbook (chapters 4, 5, and 6) at
publication-ready quality. A chapter ships only after an adversarial
self-scoring against the family quality instrument lands at 90+ and nothing
you can fix remains below Exemplary. You are running with extended thinking:
spend it on planning, misconception inventories, and hostile self-review,
not on drafting speed.

Working directory: /Users/vega/Documents/code/textbooks/cis105/

Read first, in this order: CLAUDE.md, HANDOFF.md, docs/part-structure.md,
docs/legacy-title-blocklist.md, docs/style-guide-core.md,
docs/style-guide.md, docs/CIS105_CLOs.md, every file in templates/,
book/glossary.md, and the three published chapters in book/chapters/ (they
carry the recurring cast and conventions you must continue). Those files
are the law and they outrank anything in this prompt. The repo is
self-contained and needs no outside notes. The old-reference-docs
folder was archived off-repo on 2026-07-11 to the co-professor Drive at
`/Users/vega/Library/CloudStorage/GoogleDrive-jor2050111@phoenixcollege.edu/My Drive/co-professor/01-teaching/03-cis105-survey-cis/cis105-old-reference-docs/`.

Then calibrate before writing a word:

* Read ../TEXTBOOK-QUALITY-RUBRIC.md, the 15-criterion instrument (C1-C15)
  every book in this family is scored against, including the Exemplary
  anchors and category weights.
* Read the reports in ../evaluations/ for cis360 (98.4, the family's best)
  and cis133 (91.6). The improvement plans list exactly what evaluators
  dock: inline MLO section bindings, Predict-step integrity, canonical
  rubric labels, data-pack reproducibility, alt text. Treat them as a map
  of failure modes to pre-empt.
* Read two chapters of ../cis360/book/chapters/ end to end and note what
  Exemplary craft looks like at the paragraph level.
* Chapters 1-3 of this book scored 6/10 in Mr. Vega's review. Match their
  structure, recurring cast (Desert Bloom Coffee, Maya Reyes, Elena
  Fuentes), and conventions, but do not treat them as the quality bar.
  Their known gaps: length tapering below the ~600-line target (515, 446,
  378), zero diagrams, and sections that survive the gates without always
  teaching a decision. Exceed them.

Deliver the three chapters strictly in order, each fully finished,
committed, and pushed before the next begins:

1. What Makes Your Device Run: Operating Systems and Utilities
   (Skills Lab 4, PowerPoint: Pitch Deck Foundations: An Outline Becomes
   Slides)
2. Processors, Memory, and the AI PC
   (Skills Lab 5, PowerPoint: Show, Don't Tell: Hardware Specs as Visuals)
3. From Touchscreens to the Cloud: Devices and Storage
   (Skills Lab 6, Excel: Side by Side: A Device Comparison Workbook)

Titles, subtitles, content bullets, CLO alignment, and lab titles are
locked in docs/part-structure.md. Track the work in the Tasks API (list
cis105), one task per chapter.

Per chapter, run this workflow:

1. Plan before prose: a section outline with each of the three MLOs bound
   to a section, a misconception inventory for the topic (what first-time
   students wrongly believe about OSes, chips, and storage, and which
   section corrects each), a continuity map (what this chapter calls back
   to and what it must set up), and the lab's skill progression from the
   previous lab.
2. Draft at full depth: ~600 lines of substance. When a section runs thin,
   the fix is a better teaching idea (a worked decision, a failure story,
   a comparison table, a mermaid diagram, which zensical renders), never
   filler. Every main section must teach at least one decision a student
   could defend afterward, not just facts.
3. Adversarial self-review before any commit: score the full draft against
   all 15 criteria as a hostile evaluator would, citing evidence line by
   line. Revise until nothing scores below 4 and C2 (explanation quality),
   C5 (active-learning scaffolding), and C7 (authentic assessment) score
   5. Then reread the chapter once straight through as a first-time
   student and fix every place you stumble.
4. Only then run the mechanical gates: the blocklist grep in
   docs/legacy-title-blocklist.md, zero em dashes, zero banned vocabulary,
   zero semicolons, python3 tools/check_sentence_length.py on the chapter,
   and .venv/bin/zensical build --clean with no issues. One commit per
   chapter, pushed.

Quality bars the instrument rewards, honored from the first draft:

* MLOs carry inline section bindings: **MLO-N.Y (Level):** verb, outcome,
  (Section N.X). C4 anchors on this.
* At least four Try It Yourself exercises and four Quick Checks per
  chapter. Every Predict step forces a specific committed choice (a
  number, a selection, a written guess), never "what do you think will
  happen."
* Labs: three progressive parts on one dataset, two weighted Questions &
  Analysis, the transferable half as strong as the technical half, parts
  explicitly aligned to MLOs, short rubric reference block (chapters 2-12
  pattern).
* Exactly one Tech in Your Field admonition covering at least three
  enrolled majors, roles changing, never disappearing.
* Hardware and OS claims must be current for 2026 (NPUs, unified memory,
  storage tiers, current Windows and macOS behavior). Verify anything
  uncertain with a web search before asserting it. Live, durable Further
  Reading links only.
* App steps target Microsoft 365 desktop current channel on Windows 11 and
  macOS, giving both platforms' paths where they differ, with Excel for
  the web limits noted where relevant.
* Chapter 6 starts the generator convention: a seeded script in
  assets/code/_generators/ that rebuilds device-comparison.xlsx
  byte-identically (50+ rows, 5+ columns, asserts verifying the engineered
  properties), with the seed and rebuild command documented in HANDOFF.md.
  Run every formula the chapter prints against the real file before
  writing its output into the text. Never hardcode an output the pack
  cannot reproduce.
* PowerPoint labs (4-5): the pack ships the outline and spec content, so
  students never hand-type body text. Name the event venue business and
  the repair shop contact, and add them to the recurring cast in
  HANDOFF.md.
* Glossary integrity both directions: every bolded term resolves in
  book/glossary.md, and every Key Terms entry is bolded somewhere in its
  chapter.
* Mermaid diagrams where a picture teaches better than prose (boot
  sequence, memory hierarchy, storage decision tree), each introduced by
  prose that stands alone if the diagram fails to render, with descriptive
  text for accessibility. Tables always carry header rows.

Uncomment each chapter's nav line in zensical.toml as it lands. When all
three chapters are live: update HANDOFF.md (session record, key decisions,
answer keys for anything planted, generator seed, next steps pointing at
Part III), commit, push, and confirm the deployed site renders all three
chapters and their nav entries. Flesch target is 60-70, leaning toward the
top. Make pedagogical decisions within the law yourself and record them in
HANDOFF.md rather than stopping to ask.
