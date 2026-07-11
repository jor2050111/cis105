# CIS105 Textbook: 12-Chapter Structure (Authoritative)

**Course:** CIS105: Survey of Computer Information Systems
**Structure:** 12 chapters organized into 4 thematic Parts
**Schedule:** 12 content weeks + 1 review/exam week + 1 finals week
= 14-week term (a 16-week section adds a project week after Part III
and a buffer week before finals)
**Prerequisite:** None. Chapters teach from zero.
**Last revised:** 2026-07-11

This document is the single authoritative plan for chapter order,
scope, and outcome coverage.

---

## Design Rationale

This plan synthesizes three sources:

1. **Official district CLOs and course outline**
   (docs/CIS105_CLOs.md): every outcome and outline section maps to a
   chapter
2. **The previous Canvas build:** 13 modules following O'Leary's
   *Computing Essentials 2023* (29e) with SIMnet labs for Word, Excel,
   PowerPoint, and Access
3. **The textbook family structure:** 12 chapters in 4 Parts, the
   pattern proven by the sibling textbooks

**Key design decisions:**

* Merged old modules 6 (Input/Output) and 7 (Secondary Storage) into
  Chapter 6 (Input, Output, and Storage). Both cover peripheral
  hardware, and the merge fits the family's 12-chapter frame while
  keeping every other proven module in its taught order.
* Moved application-skills instruction out of SIMnet and into chapter
  Skills Labs. The lab thread runs Word (Ch 1-3), PowerPoint (Ch 4-5),
  Excel (Ch 6-9), Airtable (Ch 10-11), and Excel macros with VBA
  (Ch 12), covering CLO XIII with authentic tasks instead of
  simulations.
* Replaced Microsoft Access with Airtable per Mr. Vega's standing
  decision (recorded twice in the source outline). Chapters teach the
  same database concepts in Airtable's current web app.
* Gave macros and VBA a conceptual home in Chapter 12 (Programming and
  Languages), aligned with CLO VII and outline section V. The old
  build parked the Excel macros unit in module 9 with no programming
  context around it.
* Kept privacy, security, and ethics as one chapter (Ch 8) and paired
  it with networks in Part III, so risk always follows connectivity.

**Bloom's rule for every MLO (course-configured, mirrors CLAUDE.md):**
the full RBT range is available. Early chapters lean on Remember
through Apply verbs. Analyze through Create verbs appear in Skills
Labs, later chapters, and the VBA work in Chapter 12. Every MLO uses a
measurable action verb. Never write "understand," "know," or "learn"
as the verb.

---

## Part I: Digital Foundations (Chapters 1-3)

**Theme:** what an information system is, and how you already live inside one
**Learning arc:** Describe the system -> Use the web well -> Choose the right application
**Outcome alignment:** CLO II, IV, V, X (CLO XIII lab thread: Word)
**Bloom's focus:** Remember, Understand, Apply

### Chapter 1: Information Technology, the Internet, and You

**Subtitle:** DESCRIBE the parts of an information system
**Outcome(s):** CLO X (primary), CLO I, II, V (introduced)
**Outline section(s):** VIII (uses of technology), survey of I-IV

**Content:**

* The five parts of an information system: people, procedures,
  software, hardware, data (plus connectivity)
* System software vs application software at a glance
* Types of computers and personal devices
* Document, worksheet, database, and presentation files
* Connectivity, cloud computing, and IoT as the course roadmap

**Prior-course parallel:** old module 1 (I.T., the Internet, and You)
**Prerequisite bridge:** new content. Bridges from students' daily
phone and app experience.
**Skills Lab app:** Word (create and edit a document)

### Chapter 2: The Internet, the Web, and E-commerce

**Subtitle:** USE the web to communicate, research, and buy safely
**Outcome(s):** CLO IV, V (primary), CLO VI, XI (introduced)
**Outline section(s):** IV (Internet)

**Content:**

* Origins of the Internet and the web
* Providers, browsers, and how a web page reaches you
* Website technology: HTML, links, and web servers
* Communication tools: email, messaging, social networks, podcasts
* Search engines and evaluating online information
* E-commerce types (B2C, C2C, B2B) and safe transactions

**Prior-course parallel:** old module 2 (Internet, Web, and Electronic
Commerce)
**Prerequisite bridge:** extends Chapter 1's connectivity roadmap.
**Skills Lab app:** Word (format and customize a research document)

### Chapter 3: Application Software

**Subtitle:** CHOOSE the right application for the task
**Outcome(s):** CLO II (primary), CLO IX (introduced), CLO XIII
**Outline section(s):** II.B-D (application software), IX (business
application tools, concepts)

**Content:**

* General-purpose applications: word processors, spreadsheets,
  presentation software, database management systems
* Specialized applications: graphics, web authoring, video, gaming
* Mobile apps and app stores
* Software suites: office, cloud, specialized, utility
* Choosing between installed, web, and mobile versions

**Prior-course parallel:** old module 3 (Application Software)
**Prerequisite bridge:** names the categories behind the tools used in
Chapters 1-2 labs.
**Skills Lab app:** Word (styles, table of contents, collaboration
features)

**Part I milestone:** students can explain how an information system
works, research and evaluate sources on the web, and produce polished
Word documents.

---

## Part II: Inside the System (Chapters 4-6)

**Theme:** what makes the machine run, from the OS down to every port and drive
**Learning arc:** Explain the software layer -> Identify the components -> Select devices and storage
**Outcome alignment:** CLO I, II (CLO XIII lab thread: PowerPoint, Excel)
**Bloom's focus:** Understand, Apply, Analyze

### Chapter 4: System Software

**Subtitle:** EXPLAIN what the operating system does for you
**Outcome(s):** CLO II (primary)
**Outline section(s):** II.A (system software)

**Content:**

* System software vs application software (deepens Chapter 1)
* Operating system functions, features, and categories
* Mobile operating systems: iOS and Android
* Desktop operating systems: Windows, macOS, UNIX, Linux,
  virtualization
* Utilities and device drivers

**Prior-course parallel:** old module 4 (System Software)
**Prerequisite bridge:** builds on the software split introduced in
Chapters 1 and 3.
**Skills Lab app:** PowerPoint (create and edit a presentation)

### Chapter 5: The System Unit

**Subtitle:** IDENTIFY the components on the system board
**Outcome(s):** CLO I (primary), CLO VIII (purchasing decisions)
**Outline section(s):** I.A, I.E (processing, expansion), VI.B
(purchasing and upgrading)

**Content:**

* Types of system units, from desktops to wearables
* System boards, sockets, slots, and bus lines
* Microprocessors and specialty processors
* Memory: RAM, ROM, and flash
* Expansion cards, ports, and power
* Reading a spec sheet: purchasing and upgrading decisions

**Prior-course parallel:** old module 5 (The System Unit)
**Prerequisite bridge:** hardware overview from Chapter 1 becomes
component-level detail.
**Skills Lab app:** PowerPoint (pictures and information graphics:
build a spec-sheet deck)

### Chapter 6: Input, Output, and Storage

**Subtitle:** SELECT the devices that move and keep your data
**Outcome(s):** CLO I (primary)
**Outline section(s):** I.B-D (storage, input, output devices), VII.D
(ergonomics)

**Content:**

* Input: keyboards, pointing devices, scanners, image and audio capture
* Output: monitors, printers, audio devices, combination devices
* Ergonomics and healthy setup
* Primary vs secondary storage
* Solid-state, hard-disk, optical, and cloud storage
* Choosing storage: capacity, speed, and backup habits

**Prior-course parallel:** old modules 6 (Input/Output) and 7
(Secondary Storage), merged
**Prerequisite bridge:** extends Chapter 5's memory discussion into
persistent storage.
**Skills Lab app:** Excel (create and edit a workbook: device
comparison sheet)

**Part II milestone:** students can trace what happens inside the
machine, compare hardware options against a task, and build both a
presentation and a working Excel workbook.

---

## Part III: Networks and Security (Chapters 7-8)

**Theme:** how data travels, and what can go wrong on the way
**Learning arc:** Explain connectivity -> Examine the risks -> Judge safe and ethical practice
**Outcome alignment:** CLO III, VI, XI (CLO XIII lab thread: Excel)
**Bloom's focus:** Understand, Analyze, Evaluate

### Chapter 7: Communications and Networks

**Subtitle:** EXPLAIN how networks connect people and resources
**Outcome(s):** CLO III (primary), CLO VI (network security intro)
**Outline section(s):** III (networks)

**Content:**

* Connectivity, the wireless revolution, and communication systems
* Wireless and physical channels
* Connection services: cellular, DSL, cable, satellite
* Bandwidth and protocols
* Network types: LAN, home, wireless, PAN, MAN, WAN
* Topologies, strategies, and shared resources

**Prior-course parallel:** old module 8 (Communications and Networks)
**Prerequisite bridge:** the connectivity thread from Chapters 1-2
becomes technical.
**Skills Lab app:** Excel (formulas and functions: internet plan
comparison)

### Chapter 8: Privacy, Security, and Ethics

**Subtitle:** JUDGE the risks and responsibilities of a connected life
**Outcome(s):** CLO VI, XI (primary)
**Outline section(s):** VII (social and ethical issues), III.C, IV.H
(security)

**Content:**

* Privacy: large databases, online identity, major privacy laws
* Cybercrime: identity theft, scams, ransomware, denial of service
* Social engineering and malware
* Protecting yourself: access control, encryption, backups
* Ethics: copyright, DRM, plagiarism, cyberbullying
* Green computing

**Prior-course parallel:** old module 9 (Privacy, Security, and Ethics)
**Prerequisite bridge:** every threat maps to a network path from
Chapter 7.
**Skills Lab app:** Excel (charts: visualize a personal security
audit)

**Part III milestone:** students can map how their data travels, name
the threats along the way, and defend their choices with evidence and
ethical reasoning.

---

## Part IV: Technology at Work (Chapters 9-12)

**Theme:** how organizations turn data into decisions, systems, and software
**Learning arc:** Describe business systems -> Build a database -> Outline a solution -> Automate with code
**Outcome alignment:** CLO VII, VIII, IX, XII (CLO XIII lab thread: Excel, Airtable, VBA)
**Bloom's focus:** Apply, Analyze, Evaluate, Create

### Chapter 9: Information Systems

**Subtitle:** DESCRIBE how information flows through a business
**Outcome(s):** CLO XII (primary), CLO VIII, IX
**Outline section(s):** VI.A (IS role in business), VIII (uses of
technology)

**Content:**

* Functional view of an organization
* Management levels and their information needs
* TPS, MIS, DSS, and executive support systems
* Office automation and knowledge work systems
* Expert systems
* Careers in information technology

**Prior-course parallel:** old module 10 (Information Systems)
**Prerequisite bridge:** the coffee-shop and bookstore scenarios from
earlier labs scale up to whole organizations.
**Skills Lab app:** Excel (tables, sort, filter, pivot tables:
business data analysis)

### Chapter 10: Databases

**Subtitle:** BUILD a database that answers business questions
**Outcome(s):** CLO XIII (primary for databases), CLO VI (data
security)
**Outline section(s):** II.B.3 (databases), IX.D (database tools,
taught in Airtable)

**Content:**

* Physical vs logical views of data
* Data organization: characters, fields, records, tables, databases
* Key fields and relationships
* Batch vs real-time processing
* Database models and DBMS types
* Database security and strategic use
* Airtable: bases, tables, fields, and views

**Prior-course parallel:** old module 11 (Databases)
**Prerequisite bridge:** the pivot-table questions from Chapter 9
become database queries.
**Skills Lab app:** Airtable (create a base and tables by importing
pack CSVs)

### Chapter 11: Systems Analysis and Design

**Subtitle:** OUTLINE a technology solution phase by phase
**Outcome(s):** CLO VIII, IX (primary)
**Outline section(s):** VI (planning and implementing solutions)

**Content:**

* The six phases of the systems life cycle
* Identifying needs and formulating solutions
* Feasibility and alternatives
* Acquiring and testing hardware and software
* Conversion strategies and minimizing risk
* Audits, evaluation, prototyping, and RAD

**Prior-course parallel:** old module 12 (Systems Analysis and Design)
**Prerequisite bridge:** applies the business context from Chapter 9
and the database from Chapter 10 to a full project.
**Skills Lab app:** Airtable (views, filters, and reports: a project
tracker for a systems proposal)

### Chapter 12: Programming and Languages

**Subtitle:** CREATE your first macros with VBA
**Outcome(s):** CLO VII (primary), CLO IV, IX
**Outline section(s):** V (VBA), IX.C.5 (Excel automation)

**Content:**

* Programs and the six steps of programming
* Design tools: pseudocode, flowcharts, logic structures
* Testing and debugging
* Five generations of programming languages
* Macros: recording, running, and when to use them
* The Visual Basic Editor: procedures and variables
* Where web scripting fits (connects back to Chapter 2's HTML)

**Prior-course parallel:** old module 13 (Programming and Languages)
plus the Excel macros unit the old build placed in module 9
**Prerequisite bridge:** automates the Excel skills built in
Chapters 6-9.
**Skills Lab app:** Excel with VBA (record a macro, then edit it in
the Visual Basic Editor)

**Part IV milestone:** students can follow data from a transaction to
a decision, build and query an Airtable base, outline a systems
project, and automate a repetitive Excel task with a macro.

---

## Course Schedule (14-Week Term)

| Weeks | Content | Assessment |
| ----- | ------- | ---------- |
| 1-3 | Part I: Digital Foundations (Ch 1-3) | Skills Labs 1-3 (Word), Quick Checks, discussions |
| 4-6 | Part II: Inside the System (Ch 4-6) | Skills Labs 4-6 (PowerPoint, Excel), Unit Exam 1 (Ch 1-6) |
| 7-8 | Part III: Networks and Security (Ch 7-8) | Skills Labs 7-8 (Excel), discussions |
| 9-12 | Part IV: Technology at Work (Ch 9-12) | Skills Labs 9-12 (Excel, Airtable, VBA), Unit Exam 2 (Ch 7-12) |
| 13 | Review and integration | Unit Exam 3 or capstone review |
| 14 | Finals | Comprehensive final exam (Ch 1-12) |

A 16-week section adds a project week after Part III and a buffer week
before finals. Exam count and placement stay course-configured in
Canvas: the old build ran three summative exams plus a comprehensive
final, and that pattern still fits.

**Assessment structure (adapted from the Spring 2026 syllabus):**

* Orientation activities: 2%
* Discussions: 17%
* Chapter reading and Quick Checks: 20%
* Skills Labs (12): 30%
* Unit exams: 21%
* Comprehensive final: 10%

Weights carry forward from the previous build's proportions and may
shift when the Canvas shell is rebuilt.

---

## Outcome Coverage Matrix

Every course outcome needs at least one primary chapter. Flag weak
rows before writing begins.

| Outcome | Primary chapters | Supporting chapters | Coverage assessment |
| ------- | ---------------- | ------------------- | ------------------- |
| I. Hardware components | Ch 5, Ch 6 | Ch 1 | Strong: two dedicated chapters |
| II. Software types | Ch 3, Ch 4 | Ch 1 | Strong: dedicated application and system chapters |
| III. Network uses | Ch 7 | Ch 2 | Strong: dedicated chapter |
| IV. Website technology | Ch 2 | Ch 12 | Strong: web structure in Ch 2, scripting tie-in Ch 12 |
| V. Internet use | Ch 2 | Ch 1, every lab's research tasks | Strong: taught then practiced all term |
| VI. Security and privacy | Ch 8 | Ch 2, Ch 7, Ch 10 | Strong: dedicated chapter plus threads |
| VII. Macros and VBA | Ch 12 | Excel labs Ch 6-9 | Strong: dedicated sections and lab |
| VIII. Planning solutions | Ch 11 | Ch 5, Ch 9 | Strong: dedicated chapter |
| IX. Select tools | Ch 9, Ch 11 | Every Skills Lab | Strong: decision framing throughout |
| X. Terminology and limits | Ch 1 | Every chapter (glossary thread) | Strong: roadmap chapter plus glossary |
| XI. Ethics | Ch 8 | Ch 2 | Strong: dedicated coverage in Ch 8 |
| XII. Business and careers | Ch 9 | Ch 1, Ch 12 | Strong: dedicated chapter |
| XIII. Productivity software | Skills Lab thread Ch 1-12 | Ch 3 (concepts) | Strong: every chapter has an app lab |

---

## District Outline Coverage Map

Confirm every section of the official course outline lands somewhere.

| District outline section | Chapter(s) |
| ------------------------ | ---------- |
| I. Hardware | Ch 5 (processing, expansion), Ch 6 (storage, input, output) |
| II. Software | Ch 4 (system), Ch 3 (application, specialized, web authoring) |
| III. Networks | Ch 7 (types, uses), Ch 8 (security and data integrity) |
| IV. Internet | Ch 2 (all subsections), Ch 8 (security) |
| V. Visual Basic Application (VBA) | Ch 12 (editor, procedures, variables, macros) |
| VI. Planning and Implementing Technology Solutions | Ch 11 (primary), Ch 9 (IS role), Ch 5 (purchasing/upgrading) |
| VII. Social and Ethical Issues | Ch 8 (primary), Ch 6 (ergonomics) |
| VIII. Uses of Technology | Ch 9 (business, careers), Ch 1 (survey) |
| IX. Business Application Tools | Skills Lab thread: Word Ch 1-3, PowerPoint Ch 4-5, Excel Ch 6-9, Airtable (for Access) Ch 10-11, Excel macros Ch 12 |

---

## Cross-Chapter Dependencies

**Strict prerequisites:**

* Chapter 6 requires Chapter 5 (storage extends the memory discussion)
* Chapter 8 requires Chapter 7 (threats map onto network paths)
* Chapter 10 requires Chapter 9 (database questions come from business
  information needs)
* Chapter 12 requires Chapters 6-9 (VBA automates the Excel skills the
  lab thread built)

**Lab thread order (strict):**

* Word (Ch 1-3) -> PowerPoint (Ch 4-5) -> Excel (Ch 6-9) ->
  Airtable (Ch 10-11) -> Excel macros with VBA (Ch 12)

**Knowledge assumed across all chapters:**

* Everyday phone, app, and web experience (nothing more)
* Earlier chapters of this book only

---

## Prerequisite-to-CIS105 Bridge Map

CIS105 has no prerequisite course. This section intentionally records
none. Chapters bridge from everyday technology experience instead
(see docs/style-guide.md, Bridging rule).
