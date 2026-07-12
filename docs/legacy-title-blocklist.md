# Legacy Title Blocklist (Authoritative)

**Purpose:** No part name, chapter title, section heading (H1-H3),
Skills Lab title, or assignment title in this textbook may exactly
reproduce a title or heading from the previous Computing Essentials
build. This file lists every banned string, extracted from the bold
headings in `chapter-NN-old-notes.docx` (2026-07-11) and the old SIMnet
assignment titles in `cis105-old-assignment-calendar.md`. Both source
files were archived off-repo on 2026-07-11 to the co-professor Drive at
`/Users/vega/Library/CloudStorage/GoogleDrive-jor2050111@phoenixcollege.edu/My Drive/co-professor/01-teaching/03-cis105-survey-cis/cis105-old-reference-docs/`.
The banned strings below are already fully materialized here, so this
check does not need those files.

**Rule (from Mr. Vega, 2026-07-11):** cover the district outline
concepts, but never under the old names. New titles MAY share common
words (software, hardware, networks, storage) with old headings. They
may NOT match an old heading exactly.

**Exemptions:**

* Family-template structural headings mandated by CLAUDE.md
  (Learning Objectives 🎯, Module Overview 🧭, Summary and Retrieval,
  Review Questions, Further Reading, Looking Ahead). The template's
  icon suffix and decimal numbering already differentiate them.
* Internal authoring docs (docs/, HANDOFF.md) may quote old titles as
  provenance, for example the Prior-course parallel lines in
  docs/part-structure.md.

## How to check a chapter before commit

From the repo root, with the draft at `book/chapters/chapter-NN.md`:

```bash
grep -E '^#{1,3} ' book/chapters/chapter-NN.md \
  | sed -E 's/^#+ //; s/ *(🎯|🧭|🛠️|✅|💡|🤔|🔄️|📖|⏩)$//; s/^[0-9]+\.[0-9]+ //; s/^Chapter [0-9]+: //' \
  | grep -Fx -f <(grep -E '^\* ' docs/legacy-title-blocklist.md | sed 's/^\* //') \
  && echo 'BLOCKED TITLE FOUND' || echo 'clean'
```

The command strips heading marks, icons, and numbering, then compares
each heading against the list below as a full-line match.

## Banned chapter titles (old modules 1-13)

* Information Technology, the Internet, and You
* The Internet, the Web, and Electronic Commerce
* Application Software
* System Software
* The System Unit
* Input and Output
* Secondary Storage
* Communications and Networks
* Privacy, Security, and Ethics
* Information Systems
* Databases
* Systems Analysis and Design
* Programming and Languages

## Banned section headings (old module 1)

* People
* Procedures
* Software
* Hardware
* Data
* Connectivity and the Mobile Internet
* Careers in IT
* A Look to the Future

## Banned section headings (old module 2)

* The Internet and the Web
* Internet Access
* Web Utilities
* Communication
* Blogs, Microblogs, Podcasts, and Wikis
* Messaging
* Search Tools
* Search Engines
* Content evaluation
* Electronic Commerce
* Cloud Computing
* The Internet of Things (IoT)

## Banned section headings (old module 3)

* Two kinds of software:
* Mobile Apps
* General-Purpose Applications
* Word Processors
* Presentation software
* Spreadsheets
* Database Management Systems
* Specialized Applications
* Graphics
* Video Game Design Software
* Web Authoring Programs
* Other Specialized Applications
* Software Suites

## Banned section headings (old module 4)

* Operating Systems
* Features
* Categories
* Mobile Operating Systems
* Desktop Operating Systems
* Microsoft's Windows
* macOS
* Unix and Linux
* Linux
* Virtualization
* Utilities
* Operating System Utilities
* Utility Suites:

## Banned section headings (old module 5)

* System Unit
* Wearable computers, wearable devices
* System Board
* Microprocessor
* Microprocessor chips
* Specialty processors
* Memory
* RAM
* ROM
* Flash Memory
* Expansion Cards and Slots
* Bus Line
* Expansion Buses
* Ports
* Power Supply
* Electronic Data and Instructions
* Careers In IT
* A Look to the Future-Brian-Computer Interfaces

## Banned section headings (old module 6)

* What is Input?
* Keyboard Entry
* Virtual keyboards
* Laptop keyboards
* Traditional keyboards
* Pointing Devices
* Touch Screen
* Mouse
* Game Controllers
* Scanning Devices
* Card Readers
* Bar Code Readers
* RFID Readers
* Character and Mark Recognition Devices
* Image Capturing Devices
* Audio-Input devices
* What is Output?
* Monitors
* E-book Readers
* Printers
* Ink-jet printers
* Laser printers
* Other Printers
* Multifunctional devices (MFD)

## Banned section headings (old module 7)

* Storage
* Solid State Storage
* Solid-State Drives (SSDs)
* Flash Memory Cards
* USB Flash Drives
* Hard Disks
* Internal hard disk
* External hard disk
* Network Drive
* Performance Enhancements
* Optical Discs
* Cloud Storage
* Mass Storage Devices
* Storage Area Network (SAN)

## Banned section headings (old module 8)

* Communications
* Communication channel
* Communication Channels
* Wireless Connections
* Connection Devices
* Connection Service
* Making IT Work for You-The Mobile Office
* Mobile Hotspot Device
* Personal Hotspot
* Public Wi-Fi
* Video Conferencing
* Data transmission
* Networks
* Network Types
* Network Architecture
* Strategies
* Organizational Networks
* Intranet
* Extranet
* Network Security
* Firewalls
* Intrusion detection systems (IDS)
* Virtual private networks (VPN)
* A Look to the Future-Telepresence Lets You Be There without Actually Being There

## Banned section headings (old module 9)

* Privacy
* Collecting public, but personally identifying information
* Spreading information without personal consent
* Spreading inaccurate information
* Private networks
* The Internet and the web
* Major Laws on Privacy
* Security
* Cyber Crime
* Social Engineering
* Malicious Software
* Malicious Hardware
* Rogue Wi-Fi Hotspots
* Infected USB flash drives
* Measures to Protect Computer Security
* Preventing Data Loss
* Cyberbullying
* Copyright and Digital Rights Management
* Plagiarism
* IT security analysts

## Banned section headings (old module 10)

* Organizational Information Flow
* Transaction Processing System
* Management Information Systems (MIS)
* Decision Support System (DSS)
* Executive Support Systems
* Other Information System

## Banned section headings (old module 11)

* Key Field
* Batch vs. Real-time Processing
* Database Management
* DBMS Structure
* Multidimensional database
* Types of Databases
* Database Uses and Issues
* Strategic uses

## Banned section headings (old module 12)

* Phase 1: Preliminary Investigation
* Defining the Problem
* Suggesting Alternative Solutions
* Prepare a Short Report
* Gathering Data
* Analyzing Data
* Documenting System Analysis
* Designing Alternative Systems
* Writing the System Design Report
* Acquiring Software
* Acquiring Hardware
* Testing the New System
* Types of Conversion
* Training
* Phase 6: System Maintenance
* Prototyping and Rapid Applications Development
* Prototyping
* The Challenge of Keeping Pace

## Banned section headings (old module 13)

* Step 2: Program Design
* Top-down program design
* Step 3: Program Code
* Step 4: Program Test
* Syntax error
* Logic error
* Step 5: Program Documentation
* Step 6: Program Maintenance
* CASE and OOP
* Generations of Programming Languages

## Banned assignment titles (old SIMnet units)

* Creating and Editing Documents
* Formatting and Customizing Documents
* Collaborating with Others and Working Reports
* Creating and Editing Presentations
* Illustrating with Pictures & Information Graphics
* Preparing for Delivery & Using a Slide Presentation
* Creating and Editing Workbooks
* Working with Formulas and Functions
* Creating and Editing Charts
* Formatting, Organizing, and Getting Data
* Working with Macros
* Creating a Database and Tables
* Using Design View, Data Validation, Relationships
* Creating and Using Queries
