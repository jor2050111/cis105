# Chapter 11: From Idea to Rollout: Planning Technology Solutions

The booking mess from Chapter 10 had an obvious fix: build a database. Darnell Brooks nearly built it the fast way. On a slow Tuesday he opened Airtable, started dragging fields around, and had half a booking table before lunch. In 2026 that is how a lot of software begins, because the tools finally let anyone build. Then Renee Salazar, his office manager, asked three questions that stopped him cold. What exactly is the problem we are solving? Who has to switch to this, and when? And what happens to the fifty bookings already on the calendar the day we turn it on?

Darnell did not have answers. He had a half-built table and a good feeling. That gap, between a tool you can build and a solution people can trust, is the whole subject of this chapter. Building was the easy part. Everything around the building is the harder part. Naming the real problem, weighing the options, designing before you type, testing against reality, and moving people over without dropping a booking: that is the work that decides whether the project helps or hurts.

That work has a shape professionals have used for decades, and it did not disappear when building got easy. If anything, cheap building made it more valuable, because now the scarce skill is not typing the app. It is knowing what to build, whether it is worth it, and how to roll it out without chaos. This chapter walks the six phases that carry a technology solution from a vague complaint to a running system, using the exact project that produced your Chapter 10 base. Then the Skills Lab hands you that project as a tracker, already behind schedule, and asks the question Darnell has to answer: is this ready to go live?

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero), builds on Chapter 10 (the base you designed and built), Chapter 9 (how businesses use information), and Chapter 3 (subscribe versus buy, and task-first tool choice)
* **Deliverables:** Skills Lab 11A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-11.1 (Understand):** Outline the six phases of the systems life cycle and the purpose of each (Section 11.1)
* **MLO-11.2 (Analyze):** Differentiate build, buy, and subscribe options against a project's feasibility and requirements (Sections 11.2 and 11.3)
* **MLO-11.3 (Evaluate):** Recommend a conversion strategy and defend it against a project's readiness, risks, and people (Sections 11.3 and 11.4 and Skills Lab 11A)

### This chapter aligns with the following Course Learning Outcomes

* **CLO VIII (Understand):** Outline the steps for planning and implementing a technology solution, from needs analysis to rollout
* **CLO IX (Evaluate):** Evaluate tasks and problems to select the technology tools and resources that fit
* **CLO XIII (Apply):** Produce documents, spreadsheets, databases, and presentations with industry-standard productivity software

---

## 11.1 The Systems Life Cycle: Six Phases, One Loop

A **system** is a set of parts working together toward a goal, and Chapter 1 named the six parts of an information system: people, procedures, software, hardware, data, and connectivity. Building one is a project, and projects that skip planning tend to end the same way: the wrong thing gets built, the money runs out, or the people refuse to use it. The **systems life cycle** is the ordered set of phases that keeps a project from those endings. You will also hear it called systems analysis and design, or the systems development life cycle.

### The Six Phases

Every serious build passes through six phases, whether the team names them or not.

* **Investigation.** Spot the problem, define it, and decide whether solving it is worth the effort. This phase ends with a go or no-go.
* **Analysis.** Study the current process and pin down the requirements: what the solution must do, in specifics.
* **Design.** Draw the blueprint before building. The Chapter 10 base, with its tables, keys, and relationships, was a design.
* **Development.** Build, buy, or subscribe to the actual system, then configure it to the design.
* **Implementation.** Move everyone onto the new system: convert the data, train the people, and go live.
* **Maintenance.** Keep it running, fix what breaks, and improve it, until a new need starts the cycle again.

The order matters because each phase feeds the next. Skip analysis and you design for a problem you never confirmed. Skip design and you build a mess you have to rebuild. Chapter 10's phone-number disaster was a design failure, a fact stored in six places, and no amount of careful building would have saved a bad design.

Skipping a phase is not free, it is a bill paid later with interest. A team that skips investigation builds a booking app nobody needed, because the real problem was a training gap at the front desk. A team that skips analysis builds the app the loudest person described, then rebuilds it when the quiet people surface the requirements everyone forgot. A team that skips testing ships a form that accepts a booking with no date, and finds out from an angry client. The phases are not paperwork. Each one catches a specific, expensive mistake before it ships.

### A Loop, Not a Line

The six phases look like a straight line, but the last one bends back to the first. Maintenance is where a running system meets the real world, and the real world keeps asking for more: a new report, a faster form, a feature nobody imagined at launch. Each of those requests is a small new investigation, and the cycle turns again. A system is never finished. It is only current.

Modern teams turn that loop quickly. Instead of one grand year-long march through the phases, they take a small slice, run it through all six in weeks, ship it, and learn. That habit has a name, **agile**, and Section 11.4 returns to it. For now, hold the two ideas together: the six phases name the work that always has to happen, and good teams cycle through them fast instead of once.

### Try It Yourself 11.1: Read the Project's Pulse 🛠️

**Predict:** The data pack file `project-tasks.csv` is the task list for Saguaro Hall's booking-system project, the one that built your Chapter 10 base. Before you open it, predict in writing which phase holds most of the project's active work, given that the base itself already exists in draft.

**Run:** Open the file. Look at the Phase and Status columns together. Which phases are mostly Done, which phase carries the most In Progress work, and which are still untouched?

**Explain:** In 1-2 sentences, name the phase where most of the active work sits, and cite one task's status as your evidence. Notice whether any later-phase task has jumped ahead of its phase.

### Quick Check 11.1 ✅

1. List the six phases of the systems life cycle in order, and give the one-line purpose of each.
2. Explain why the systems life cycle is drawn as a loop instead of a straight line, using the idea of maintenance.
3. A team is eager to start building in Airtable on day one. Name the two phases they are skipping and one specific risk each skip creates.

---

## 11.2 Name the Problem, Then Weigh the Fixes

The first two phases, investigation and analysis, are where projects are quietly won or lost. They produce no software. They produce clarity, and clarity is what makes the later building worth doing.

### The Problem Beneath the Request

People almost never hand you a problem. They hand you a solution and call it a problem. Darnell said "I need a booking app." That is a requested solution. The actual problem, found by asking what goes wrong today, was that bookings double-booked the Main Hall and client contact details drifted out of sync. **Needs analysis** is the work of digging past the requested solution to the real problem underneath, because building the wrong fix well is still building the wrong fix.

Once the problem is named, analysis produces **requirements**: specific statements of what the solution must do. Saguaro Hall's short list came straight from its problems.

* Store each customer's contact details once, in one place.
* Prevent two bookings in the same space at the same time.
* Let a client request a date without seeing other clients' information.
* Show staff the week's bookings without letting them export the customer list.
* Cost little, because the venue runs lean.

Requirements are the contract for everything that follows. A design is judged against them, and so is the finished system. Vague requirements are how a project delivers something that runs perfectly and helps no one. Notice that not one requirement names Airtable, because requirements describe the need, not the tool. The tool comes next.

### Feasibility Is More Than Money

Before committing, a team checks whether the project can succeed, and money is only one of four questions. **Feasibility** is that check, across four kinds.

* **Technical:** can it be built with the tools and skills on hand? Saguaro Hall's staff can run a browser, so a web tool is technically feasible.
* **Economic:** does the benefit beat the cost? A free-plan database beats hours of manual cleanup, so it clears.
* **Operational:** will it fit the way people work, and will they use it? A form the front desk finds fussy will be abandoned no matter how elegant.
* **Schedule:** can it be done in the time available, before the next busy season?

A project that fails any one of these is not ready, even if the other three are strong. The most common trap is a plan that is technically and economically sound but operationally doomed, because nobody asked the people who would have to use it every day.

### Build, Buy, or Subscribe

Chapter 3 promised that by this chapter, choosing the tool stack would be the assignment itself. Here it is. Once the requirements are clear, a team faces one decision with three doors.

* **Build** a custom system from scratch. You get exactly what you want, and you own every hour of creating and maintaining it, forever.
* **Buy** a finished product and run it yourself. Faster than building, but you adapt to its shape.
* **Subscribe** to software as a service (**SaaS**), renting it monthly and letting the vendor host and update it. Airtable is this door.

| Door | You control | Speed to running | Who maintains it | Best when |
| ---- | ----------- | ---------------- | ---------------- | --------- |
| Build | Everything | Slowest | You, forever | A requirement no product meets |
| Buy | The setup | Medium | You, on your servers | You need it in-house and can run it |
| Subscribe | The configuration | Fastest | The vendor | A product already fits the need |

In 2026 the smart default has shifted toward subscribe, because a subscription gets you most of the way today, with maintenance and security handled by someone else. Building custom earns its cost only when a real requirement forces it: a workflow no product supports, data that cannot leave your walls, or scale no plan can carry. Saguaro Hall had none of those, so it subscribed to Airtable and was running in days instead of months. The boring answer that ships usually beats the ambitious one that stalls.

### Try It Yourself 11.2: Build, Buy, or Subscribe 🛠️

**Predict:** A neighborhood clinic needs to schedule patient appointments and send reminders. Predict in writing which door you would choose, build, buy, or subscribe, before reading further into your own reasoning.

**Run:** Test your pick against the four feasibility questions and the requirements a clinic would have (privacy of health data, staff skill, budget, timeline). Note which requirement most affects the choice.

**Explain:** In 1-2 sentences, name your choice and the single requirement that decided it. Then name one requirement that, if it were true, would flip you to a different door.

### Quick Check 11.2 ✅

1. Explain the difference between a requested solution and the real problem, using Darnell's "I need a booking app" as your example.
2. Name the four kinds of feasibility, and give a one-line Saguaro Hall example of each.
3. A shop owner insists on building a custom loyalty app from scratch. Name one requirement that would justify building, and one reason subscribing to an existing tool is usually the safer default.

---

## 11.3 Design, Build, Test, and Switch Over

With the problem named and the option chosen, the middle phases turn plans into a working system. Three of them, design, development, and implementation, carry the highest risk, because this is where the project meets both the data and the people.

### The Blueprint Comes First

**Design** turns requirements into a blueprint the builder can follow. For a database project, the heart of the design is the data model: the tables, the primary keys, the relationships. You already did this work in Chapter 10, when you decided that customers and bookings were two tables joined by a link. That decision was a design, and it traced straight back to a requirement (store each contact once). Design also covers the workflow, the views each role needs, and the security model, all decided before a single record is imported. A cheap way to test a design is a **prototype**: a rough draft of the system, built to be shown and thrown away. The team learns what is wrong while fixing it is still cheap.

### Building Is Configuration Now

When a team subscribes instead of building, the **development** phase is mostly configuration, not coding. Building Saguaro Hall's system meant creating the base, importing the data, setting field types, and wiring the link, the work you did by hand in the last chapter. That is the modern face of development: for many business problems, you assemble a solution from a service instead of writing it line by line.

Whatever a team builds, it writes down how the system works: the field types, the access rules, the steps to restore a backup. That record is not busywork. It is what lets the next person, or the same person a year later, maintain the system without taking it apart to understand it. A system a colleague can read and build on outlasts a clever one only its builder can run.

### Testing Means More Than "It Runs"

A system that opens without crashing is not a tested system. **Testing** checks the system against its requirements and against the messy cases real life produces. Good testing works from a list of cases, each tied to a requirement, and each with an expected result.

* A booking with no date should be refused.
* A guest count larger than the space holds should raise a flag.
* Two events in one space at one time should be blocked.
* A client using the request form should never see another client's contact details.

If the system passes a case, the requirement behind it holds. If it fails, you found the bug in a test instead of in front of a customer. The most honest test is **user acceptance testing**: put the front-desk staff in front of the system and watch whether they succeed, not whether the builder can. Chapter 12 will draw a sharp line between a system that runs and a system that is right, the difference between a crash and a quiet wrong answer. Testing is how you catch the second kind before a customer does.

### Switching Over Without Losing the People

The riskiest phase has the least code in it. **Conversion** is the move from the old system to the new one, and there are four ways to do it, trading safety against cost.

* **Direct** conversion shuts off the old system and starts the new one on the same day. Cheapest, and the riskiest: if the new system stumbles, there is nothing to fall back to.
* **Parallel** conversion runs both systems side by side for a while, so the old one catches anything the new one drops. Safest, and the most work, because staff do everything twice.
* **Phased** conversion switches one piece at a time, spreading the risk across weeks.
* **Pilot** conversion launches to one group first, learns, then rolls out to everyone.

| Strategy | How it works | Risk | Cost | Fits when |
| -------- | ------------ | ---- | ---- | --------- |
| Direct | Old off, new on, same day | Highest | Lowest | The old system must go and losses are survivable |
| Parallel | Both run together for a while | Lowest | Highest | A failure would be costly, as at Saguaro Hall |
| Phased | One piece switches at a time | Medium | Medium | The system splits into parts |
| Pilot | One group goes first | Medium | Medium | You can learn from a small group before all |

The choice is a judgment about how much a failure would cost. A venue that cannot afford to lose a single booking leans toward parallel, even though running two systems for two weeks is tedious. And every strategy shares one truth the phrase "systems project" hides: the hard part is the people. New software means new habits, and change management, training the staff and bringing them along, is where more projects fail than any technical step. You do not just switch a system. You switch everyone who uses it.

!!! tip "Tech in Your Field"
    Every major in this room will live through a system conversion, usually more than one, and the painful ones are never painful for technical reasons. Nursing and health sciences students will survive a hospital cutting over to a new electronic health record, where a rushed conversion risks patient safety, so hospitals run parallel and train for months. Business and entrepreneurship students will switch point-of-sale or accounting systems and learn that the staff who resist are the ones nobody trained. Public safety students will move to new dispatch or records systems where a botched cutover is a genuine emergency. Education and counseling students will watch a campus change its learning platform, and feel firsthand how conversion strategy and training decide whether people curse the new tool or thank it. The technology rarely fails alone. The rollout does.

### Try It Yourself 11.3: Pick the Conversion 🛠️

**Predict:** Saguaro Hall is a small venue that cannot afford to lose a booking, with two part-time front-desk staff who are new to databases. Predict in writing which of the four conversion strategies fits, and which would be reckless here.

**Run:** Weigh each strategy against the venue's low tolerance for lost bookings and its untrained staff. Consider what each would cost if the new base had a bad first week.

**Explain:** In 1-2 sentences, name the conversion strategy you would recommend and the specific risk it protects against. Then name the strategy you would refuse and why.

### Quick Check 11.3 ✅

1. Explain the difference between testing that a system "runs" and user acceptance testing, and say which one Darnell's front-desk staff should perform.
2. Match each conversion strategy to its main trade-off: direct, parallel, phased, and pilot.
3. A manager says the project is done because the software works. Name the human-side work that is still ahead, and the phase it belongs to.

---

## 11.4 Keep It Running: Maintenance, and the Low-Code, AI-Assisted Era

Launch day is not the finish line. It is the start of the longest phase, and the one where the systems life cycle proves it is a loop.

### Maintenance Is Most of the Life

Over a system's life, more time and money go to **maintenance** than to building it. Maintenance is the steady work of keeping a live system healthy: fixing what breaks, running audits, and adding the improvements users ask for once they depend on it. Saguaro Hall's project list ends with exactly this work. Schedule monthly data audits, set up a weekly backup export (the 3-2-1 habit from Chapter 6, now a routine), review who has access each quarter, and check for duplicate customer records. Each is small. Together they are the difference between a base that stays trustworthy and one that rots back into Chapter 10's mess.

And maintenance is where the loop closes. A request to "add a monthly revenue report" is not a chore. It is a new need, a small investigation, the cycle starting over on a system that is already running. The best teams expect this and plan for it, because a used system always grows.

### Audits and Steady Improvement

A live system drifts. People find shortcuts, stray data sneaks in through the edges, and last year's access list stops matching this year's staff. An **audit** is a scheduled check that the system still matches its own rules: the right people hold the right access, the data is clean, and the backups restore when tested. Saguaro Hall's plan audits for duplicate customers and reviews access each quarter, because a base is only as trustworthy as its last check. An audit that finds nothing is not wasted. It is the proof that nothing drifted.

The other half of maintenance is **continuous improvement**: many small, tested changes instead of one giant rewrite every few years. A new report view this month, a faster form next month, each a small turn of the loop. Small changes are easy to test and easy to undo when they miss. The big-rewrite habit saves every problem for one risky launch, which is how a working system gets replaced by a broken one.

### Ship Small, Learn Fast

Section 11.1 named the quick, iterative way modern teams run the cycle: **agile**. Instead of designing the entire system, building all of it, then revealing it months later, an agile team ships a small working slice, watches real people use it, and adjusts. The Chapter 10 base was one such slice. Saguaro Hall could go live with just the Bookings and Customers tables, then learn what the staff reach for most. The calendar and the reminders come later, each as its own small pass through the phases.

The payoff is that mistakes surface while they are cheap. A wrong guess caught in a two-week slice costs two weeks, not a year. Agile is not an excuse to skip the phases, and it is not a license to build without a plan. It runs the same six phases, faster and in smaller loops, so the feedback arrives before the budget is gone.

### Anyone Can Build. Fewer Can Decide.

The reason this chapter matters more in 2026, not less, is that building got easy. **Low-code and no-code** tools let you assemble working software by configuring instead of programming, and you have been using one all along: Airtable is a no-code database. AI coding assistants go further, drafting real code from a plain-language request, and Chapter 12 puts one to work. Together they collapse the development phase that used to take months.

To see the shift, compare two ways to build Saguaro Hall's base. The old way meant hiring a developer to write and host a custom application over months, at a cost a small venue could not carry. The no-code way meant dragging fields into a table over an afternoon, which is exactly what you did in Chapter 10. The work that once filled the entire development phase now fits inside a single lab.

Picture the difference. An AI assistant can draft an Airtable formula or a script to email booking reminders in seconds, and Chapter 12 will have you do exactly that. What it cannot do is know that Saguaro Hall needed reminders at all. It cannot know that the front desk would ignore a reminder that arrives at midnight, or that the whole feature should wait until after the busy season. Those are judgments, and they come from the phases, not the tool.

Here is what fast building does not collapse. It does not decide whether the project is worth doing, or name the real problem, or judge feasibility, or choose the conversion strategy that protects the people. A tool that builds fast still builds the wrong thing if no one did the analysis. This is the through-line this book has followed since Chapter 1, arriving at its clearest case. The role changes, the judgment stays. The professional in 2026 is not the one who can build, because soon everyone can. It is the one who knows what to build, whether to build it, and how to roll it out without breaking the people who depend on it. That person is you, by the end of the next lab.

### Try It Yourself 11.4: Spot the Loop 🛠️

**Predict:** In `project-tasks.csv`, the Maintenance phase holds the last nine tasks. Predict in writing which one or two of them are not "upkeep" at all, but a new need that would start the cycle over.

**Run:** Read the nine Maintenance task names. Separate the pure upkeep (audits, backups, fixes) from the ones that add something the system did not have before.

**Explain:** In 1-2 sentences, name a Maintenance task that is secretly a new investigation, and state what problem it would send back through the six phases.

### Quick Check 11.4 ✅

1. Explain why maintenance usually costs more over a system's life than the original build, and name two maintenance tasks a live booking base needs.
2. Airtable is a no-code tool and AI can draft code. Name one part of a systems project that neither one can do for you, and say why.
3. Restate the book's through-line ("the role changes, the judgment stays") in the context of a project where the building is automated.

---

## 11.5 Summary and Retrieval 💡

### Key Concepts

* The systems life cycle carries a project through six phases in order: investigation, analysis, design, development, implementation, and maintenance. Each has a job: name the problem, pin down requirements, draw the blueprint, build or subscribe, convert and train, then keep it running. The phases feed each other, and the last loops back to the first, because a used system always grows.
* The first phases produce clarity, not software. Needs analysis digs past the requested solution to the real problem, and requirements state exactly what the system must do. Feasibility checks four questions before committing: technical, economic, operational, and schedule. A project that fails any one is not ready, and the operational failure, software nobody will use, is the quietest and most common.
* Once requirements are set, a team chooses to build, buy, or subscribe. In 2026 subscribing to software as a service is the smart default, and building custom earns its cost only when a real requirement forces it. Design comes before building, testing checks the system against requirements and real cases instead of "it runs," and conversion (direct, parallel, phased, or pilot) trades safety against cost. The hardest part of any conversion is the people, which is why training and change management decide more projects than technology does.
* Maintenance is the longest and most expensive phase, and the point where the loop closes as new requests become new investigations. Low-code tools like Airtable and AI coding assistants have made building fast and cheap. That raises the value of the judgment they cannot replace: deciding what to build, whether to build it, and how to roll it out. The role changes, the judgment stays.

### Key Terms

See course glossary for full definitions

* system, systems life cycle (Section 11.1)
* needs analysis, requirements, feasibility, build versus buy versus subscribe, software as a service (SaaS) (Section 11.2)
* design, prototype, testing, user acceptance testing, conversion, change management (Section 11.3)
* maintenance, agile, low-code and no-code (Sections 11.1 and 11.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the six phases of the systems life cycle in order, with the purpose of each.
2. Explain the difference between a requested solution and the real problem, and name the phase that finds the difference.
3. Name the four kinds of feasibility, and give the one most projects underestimate.
4. State the four conversion strategies and the trade-off that separates the safest from the cheapest.
5. Explain why cheap, fast building tools make the planning phases more valuable, not less.

---

## 11.6 Skills Lab 11A: Track the Project: Views, Filters, and Reports

**Goal:** Run Saguaro Hall's booking-system rollout as a project tracker in Airtable. Read the project's health from its own data, and give Darnell a go or no-go recommendation with a conversion strategy he can defend.

**Dataset or starter files:** One provided file in `assets/code/chapter-11/` from the course data pack. `project-tasks.csv` holds 54 tasks across 11 fields, the full life cycle of the project that produced your Chapter 10 base. The folder README is the data dictionary. Download the data pack from Canvas, extract it, and import the file from the extracted `cis105` root. You will import the provided file, never retype it.

**Scenario:** The project is mid-Development and behind schedule, and Darnell has to decide whether to cut over to the new base or wait. The tracker holds the evidence: what is done, what is overdue, what is blocked, and one task that is quietly impossible. Your job is to build the views that surface all of it, then write the readout that tells Darnell what the data says.

!!! note
    This lab uses Airtable, this course's database tool, in any modern browser, on the free plan. Creating an Airtable account is free and needs no credit card. Nothing here requires a paid feature or an AI subscription. This lab reuses the Airtable skills from Chapter 10, so the import and field-typing steps will feel familiar.

### Part 1: Foundation (Aligns with MLO-11.1, MLO-11.2)

1. Create a new base named `Saguaro Hall Rollout`. Import `project-tasks.csv` into it, and rename the table `Tasks`.
2. Make Task ID the primary field, and confirm the values run `T-101` through `T-154`, unique.
3. Fix the field types Airtable guessed as text. Set Phase, Owner, Status, and Priority to Single select, Estimated Hours to Number, and Start Date and Due Date to Date.
4. Build a Grid view grouped by Phase. Confirm you see all six phases (Investigation, Analysis, Design, Development, Implementation, Maintenance) with nine tasks each. Read how the Status column shifts from Done in the early phases to Not Started in the late ones.
5. Record which phase holds most of the active (In Progress) work right now, and cite two task statuses as evidence.

### Part 2: Application (Aligns with MLO-11.2, MLO-11.3)

1. Build a Kanban view with Status as the stacking field, so tasks sit in columns by status. Airtable orders the stacks by how the values first appear in the data, so drag them into workflow order (Not Started, In Progress, Blocked, Done). This is the board a team runs its week on.
2. Build a filtered Grid view showing only High-priority tasks that are not Done. This is the attention list. Record how many tasks it holds.
3. Filter for Blocked tasks (you are looking for 2), and read their Notes to see what each is waiting on.
4. Find the overdue work. Filter for tasks whose Due Date is before the status date of July 11, 2026, and whose Status is not Done. Record the count (you are looking for 11) and how many are High priority.
5. Add a Calendar view on Due Date, so the deadlines spread across the year. Note how many crowd into the months the project is behind on.

### Part 3: Extension (Aligns with MLO-11.3)

1. Hunt the impossible task. Somewhere in the tracker, one task is marked In Progress while the task it depends on is still Not Started. Use the Depends On column to find it (compare each In Progress task to the status of the task in its Depends On field). Record the two Task IDs and explain in one line why that pairing cannot be true.
2. Total the remaining effort. Group by Phase and sum Estimated Hours, then note which phases still hold the most unfinished work.
3. Write the status readout. In a short document addressed to Darnell, state where the project stands (the current phase and roughly how much is done). Then name the top three risks you found in the data: the overdue High-priority work, the at-risk task, and the blocked tasks. Give a clear go or no-go recommendation for cutting over now.
4. Recommend a conversion strategy. In the same document, name which of the four strategies (direct, parallel, phased, pilot) Saguaro Hall should use, and defend it in two sentences against the venue's low tolerance for lost bookings.
5. Assemble your deliverable (see Submission) with your share link, three screenshots, your status readout, and your two Questions and Analysis answers.

### Questions & Analysis 🤔

Answer both questions in your submission document. These answers carry significant rubric weight.

1. Using the tracker's own data, recommend whether Saguaro Hall should cut over to the new base now or wait. Cite at least three specific signals from the tracker (name the tasks or counts: the at-risk task, the overdue High-priority work, what is still Not Started in Implementation). Name the conversion strategy you would use and why it fits this venue. Close with one thing the tracker cannot tell you that you would want to know before deciding.
2. Saguaro Hall chose to subscribe to Airtable instead of building a custom booking app or buying packaged venue software. Using the four kinds of feasibility from this chapter, argue why subscribing fit this project. Then describe one different requirement that, if Saguaro Hall had it, would have justified building a custom system instead.

**Submission:** Submit one PDF named `skills-lab-11a-lastname.pdf`. It contains, in order: a read-only share link to your grouped-by-phase Grid view, then three screenshots, then your status readout, then your two Questions and Analysis answers. The three screenshots are the Kanban board, the overdue or High-priority filtered view, and the Calendar view. Because the base lives in the cloud, the link is the deliverable, as it was in Chapter 10. Use your own last name in the file name.

### Rubric: Skills Lab 11A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s).

---

## 11.7 Review Questions 🔄️

1. **Remember:** Name the six phases of the systems life cycle in order, and give the one-sentence purpose of each.

2. **Understand:** Explain why the operational kind of feasibility is the one projects most often get wrong, and what happens to a system that is technically sound but operationally infeasible.

3. **Apply:** A neighborhood clinic is replacing its paper intake forms with a digital system and cannot afford to turn patients away during the switch. Name the conversion strategy that fits, and justify it in two sentences.

4. **Evaluate:** A manager wants to cut over directly to a new system this Friday to save the cost of running the old one alongside it. Staff training is not finished, and last year's data has not been migrated. Judge this decision against the phases and risks in this chapter. What is likely to go wrong, and what path would you recommend instead?

---

## Further Reading 📖

* [Airtable Support: Getting started with Airtable](https://support.airtable.com/docs/getting-started-with-airtable) - The tool this lab tracks the project in, including views, filtering, and grouping.
* [U.S. Bureau of Labor Statistics: Computer Systems Analysts](https://www.bls.gov/ooh/computer-and-information-technology/computer-systems-analysts.htm) - The federal career profile for the people who run the analysis and design phases this chapter teaches: duties, pay, and outlook.
* [U.S. Bureau of Labor Statistics: Project Management Specialists](https://www.bls.gov/ooh/business-and-financial/project-management-specialists.htm) - The career built around the planning, tracking, and rollout work at the center of this chapter.
* [Wikipedia: Systems development life cycle](https://en.wikipedia.org/wiki/Systems_development_life_cycle) - An overview of the systems development life cycle, whose exact phase names and counts vary by source, as a starting point for deeper reading.

---

## Looking Ahead ⏩

You have now followed a technology solution across its whole life, from a vague complaint to a running base that someone has to maintain. One piece of the professional's toolkit is still missing, and it is the one that turns repetitive work into something the computer does for you. Chapter 12 is the capstone. You will record your first macro, read the code it wrote, and put an AI coding assistant to work, then verify code you did not write the way a professional has to. It closes the loop this book opened in Chapter 1: the tools now draft, build, and automate, and the judgment about whether to trust what they produce stays with you.
