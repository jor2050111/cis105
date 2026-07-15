# Chapter 9: How Organizations Turn Data into Decisions

On the last Monday of June, Maya Reyes sits down with a spreadsheet she cannot read. Not because the numbers are hidden. Because there are too many of them. Desert Bloom is three locations now: the original shop on 7th Street, the Roosevelt Row store that opened in the spring, and the Campus location by the college. Four full weeks of June, every drink, pastry, and mug, sit in the export from her point-of-sale system, one line per item, hundreds of rows deep. Somewhere in there is the answer to the question keeping her up: her gut says Campus is in trouble, and 7th Street feels fine, and she cannot prove either. Her gut also cannot say what the fix would cost, or whether Bloom Ahead, the app she launched last fall with such hope, is growing or stalling.

Maya's problem is the problem of every business that ever grew: the data outgrew the owner. A one-shop operation runs on eyes and memory. A three-shop operation runs on numbers that have to travel, from registers to managers to the person deciding whether Campus stays open on Saturdays. This chapter is about the machinery of that trip. Not the cables (Chapter 7 covered the roads), and not the defenses (Chapter 8 armed you). This chapter is about the systems that turn a register tape into a decision, and the people, now joined by AI agents, who read them.

Part IV opens here, and it runs on a single idea: data becomes a decision only when it reaches the right person at the right altitude. First you will see who needs to know what, from the shift lead to the owner. Then the ladder of systems that carries data upward, summarizing at every rung. Then the modern front end: dashboards and AI agents, and the judgment that still belongs to humans. Finally the Excel thread delivers its most powerful tool yet. Chapter 8 promised that pivot tables answer in seconds what a thousand-row sheet will not surrender to scrolling. This chapter keeps that promise on Maya's own June.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero), builds on Chapter 6 (Excel tables, sort, filter), Chapter 8 (charts), and Chapter 1 (data versus information)
* **Deliverables:** Skills Lab 9A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **9.1 (Understand):** Describe how information needs change across a business's departments and management levels (Section 9.1)
* **9.2 (Analyze):** Differentiate the systems that carry data from transactions to decisions, including the dashboards and AI agents now in front of them (Sections 9.2 and 9.3)
* **9.3 (Apply):** Use sort, filter, and pivot tables to turn a sales table into answers to business questions (Section 9.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO XII (Understand):** Describe how the departments of a business and a range of career paths put technology to work
* **CLO IX (Evaluate):** Evaluate tasks and problems to select the technology tools and resources that fit
* **CLO XIII (Apply):** Produce documents, spreadsheets, databases, and presentations with industry-standard productivity software

---

## 9.1 Who Needs to Know What

Chapter 1 defined information as data organized into something meaningful enough to support a decision. This section adds the missing word: meaningful *to whom*. The same June sales data means different things to different people in the same company. Matching the data to the person is the first design problem of every business system.

### The Functions Inside Any Business

Watch Desert Bloom at three locations and you can see a company assembling itself. Someone schedules baristas and orders beans: that is operations. Someone prices the new tumbler and runs Petal Points, the app's loyalty rewards: marketing. Someone pays Rosa's roastery invoice and the payroll: accounting and finance. Someone hires, trains, and handles the paperwork when a barista leaves: human resources. And someone keeps the registers, the app, and the Wi-Fi running: information technology, even if today that someone is whichever manager reboots the router (a Chapter 7 skill).

In a three-shop company those are hats Maya wears and hands off one by one. In a hospital or a city government they are whole departments with floors of their own. The lesson that transfers: every function runs on its own slice of the data. Marketing wants to know what Petal Points members buy. Accounting wants the day's takings to match the bank deposit. Operations wants Tuesday's staffing to match Tuesday's rush. Same registers, different questions.

### The Levels Above the Functions

Cut the company the other way and you get **management levels**, and each level runs on a different altitude of information.

* **Supervisors** run the day: the shift lead who needs to know that the Campus store is out of cold brew *right now*. They need detail, this minute, about one thing.
* **Middle managers** run the month: the store manager comparing this week's sales to last week's, scheduling around the pattern. They read weekly summaries by store.
* **Top management** runs the years: Maya, deciding whether Campus stays open on weekends, whether a fourth location makes sense, whether the app deserves more investment. She needs trends and exceptions, stripped of almost every detail.

Here is the inversion students expect backward: the higher the decision, the *less* detail the decider should see. Maya does not need to know that order DB-1041 was an iced latte. She needs June by location, by week, by channel. Summarizing upward is not dumbing down. It is attention arithmetic: a person who can read four honest numbers can decide something, and a person handed 571 rows can only scroll. The skill of this whole chapter, on the human side, is choosing the right altitude for the reader. You will practice it in the lab when you compress Maya's June into exactly the numbers she needs.

One more actor now sits at every level, and Chapter 3 introduced it: the specialized software each function lives in. The point-of-sale system at the counter, the accounting package, the scheduling app. Those systems are where this chapter's data is born. Chapter 3 promised that point-of-sale and accounting software feed the dashboards this chapter examines, and Section 9.3 pays that debt.

!!! tip "Tech in Your Field"
    Every major in this room has a version of Maya's altitude problem. Nursing students will chart vitals into systems that are pure transaction capture. A charge nurse then reads the unit dashboard those charts feed: census, acuity, staffing, at a glance. Business and entrepreneurship students will live this chapter daily, from the register to the monthly review. Public safety students will file incident reports that roll up into the pattern maps and staffing decisions a commander reads. And education and counseling students will meet early-alert dashboards built from attendance and gradebook transactions, flagging which student needs a call this week. In every field, someone captures detail, someone reads summaries, and someone decides. This chapter is about all three seats, and you will sit in each of them.

### Try It Yourself 9.1: One Question per Floor 🛠️

**Predict:** Pick a business you know well: where you work, or a campus operation you see daily. Commit three predictions in writing: the single most urgent question today for a front-line worker, for a manager, and for the owner or director.

**Run:** Write the three questions, then test each against this section's altitude rule: which needs this-minute detail, which needs a weekly summary, which needs a trend or comparison?

**Explain:** In 1-2 sentences, state which question needed the least detail and why the person deciding the most gets the thinnest data.

### Quick Check 9.1 ✅

1. Route each item to its level: supervisor, middle manager, or top management. The items: a June-by-location revenue trend, a note that the espresso machine is down at Roosevelt Row, and a week-over-week look at morning staffing against morning sales.
2. A new analyst "helps" Maya by forwarding her the full 571-row June export. Using the attention arithmetic idea, explain the mistake and what the analyst should have sent instead.
3. Name two functions hiding inside "Maya handles it" at a three-shop company, and one question each function would ask of the same day's sales data.

---

## 9.2 From Receipt to Strategy: The Systems Ladder

Information does not climb from the register to Maya's desk on its own. A ladder of systems carries it, and each rung has a name, a job, and a reader. The names date from decades before the cloud, they still appear in job postings, and the concepts behind them run everything from Desert Bloom to a hospital chain.

### The Bottom Rung: Capturing Every Event

A **transaction processing system** (TPS) records the events a business runs on, one at a time, in full, as they happen: every sale, every payment, every booking. Desert Bloom's point-of-sale system is one. So is Bloom Ahead's ordering pipeline, the campus bookstore's register, and the reservation system where Darnell Brooks books Saguaro Hall's event dates. A TPS has one virtue above all others: it never sums up. Order DB-1041, an iced latte, quantity two, Campus, Tuesday morning, $10.50, exists forever as exactly that. Chapter 10 will show you the database where records like that live. This chapter cares about what happens to them next.

The TPS is also where data quality is won or lost, which is why businesses obsess over barcode scans (Chapter 6: a scan cannot mistype) and dropdown menus instead of free typing. A summary can only be as honest as the transactions beneath it. Garbage in, garbage up the ladder.

### The Middle Rungs: Summaries and What-Ifs

A **management information system** (MIS) turns transaction detail into routine summaries for running the business: sales by location by week, top items by store, hours worked against hours scheduled. The reports are regular, same-shaped, and aimed at middle management's altitude. When the Roosevelt Row manager gets Monday's email comparing her store's week to the chain's, that is the MIS rung doing its job.

A **decision support system** (DSS) serves the questions that do not repeat: the what-ifs. What happens to Campus's numbers if weekend hours drop to mornings only? What would a fourth location need to sell to cover its lease? A DSS combines data with models and lets a decider try scenarios before spending money. If that sounds like the Excel work you have been doing since Chapter 6 (assumption cells, live recalculation, comparisons), it should. A spreadsheet in skilled hands is the most widely deployed decision support system on Earth, and in the lab you will be Maya's.

The classic ladder had a top rung: executive support systems, built to give leadership a glance-sized view of the whole company. That rung still exists, and Section 9.3 shows what it turned into. Two more terms round out the family. **Business intelligence** (BI) is the umbrella name for the whole practice of turning a company's data into decisions. The phrase to **drill down** means moving from a summary to the detail beneath it. From June, to June at Campus, to June at Campus on weekends, to the single receipt. Drilling down is how a reader checks a summary against its receipts, and you will do it with a double-click in the lab.

### Try It Yourself 9.2: Count Your Transactions 🛠️

**Predict:** Commit a number in writing: how many transaction processing systems captured an event from you in the last 24 hours? (Purchases count, and so do quiz submissions, streaming plays, transit taps, and door-badge swipes.)

**Run:** List them. For each, name one field the system captured (time, amount, item, location) without you typing it.

**Explain:** In 1-2 sentences, compare the count to your prediction, and name which of your transactions probably reached a manager's summary somewhere.

### Quick Check 9.2 ✅

1. Classify each rung: the register that logs every latte, the Monday email comparing stores, the workbook where Maya models weekend closure, and a wall screen showing today's sales ticking upward.
2. A summary report says Campus sold $1,390.75 in June, and a skeptical manager wants proof. Name the move this section gives her, and where the proof ultimately lives.
3. Explain "garbage in, garbage up the ladder" using one example of a data-entry choice at the counter that would poison a monthly report.

---

## 9.3 Dashboards, Agents, and the Humans Still Deciding

The systems ladder is decades old. What changed in your lifetime is the front end: how the ladder's output reaches human eyes, and who, or what, reads it first.

### The Dashboard: The Ladder's Front Window

A **dashboard** is a live screen of charts and numbers summarizing an operation right now, named for the car part it imitates. Behind every one is the pipeline you just learned: transactions feed summaries, summaries feed the display. The charts on it are Chapter 8's charts doing full-time work. A column chart compares sales by location. A line chart draws the week's trend. A big number shows today against the same day last week. Modern dashboards refresh themselves and live where the reader lives: a wall screen at the counter, a phone app in Maya's pocket. That collapsed the old distance between the executive report and everyone else. The shift lead and the owner now look at the same screen at different altitudes.

Dashboards inherit chart ethics wholesale. A truncated axis lies on a wall screen exactly the way it lied in Section 8.4, with more viewers. And a dashboard adds a subtler trap: a number on a screen looks settled, and Chapter 2 taught you that confidence is not correctness. Professionals ask a dashboard the same two questions they ask any source: where does this number come from (which transactions, which definition of "a sale"), and what would make it wrong?

### From Expert Systems to AI Agents

Businesses have tried to bottle expertise for decades. The 1980s version was the **expert system**: a specialist's judgment captured as hundreds of hand-written if-then rules, one rule at a time. Expert systems still run narrow jobs (insurance pre-approvals, equipment diagnostics), and their limits taught the industry a lasting lesson: rules are brittle, and the world keeps producing situations nobody wrote a rule for.

The current generation is different machinery. An **AI agent** is software built on the large language models you met in Chapter 2, wired to a company's data and tools. It answers questions and carries out multi-step tasks in plain language. Instead of Maya learning query tools, she asks: "Which location grew fastest in June, and what drove it?" The agent queries the data, drafts the answer, sometimes builds the chart. This is Chapter 1's roadmap arriving at work: the assistant is no longer just drafting your documents. It is reading the company's data and proposing decisions.

Everything this book taught you about AI applies at full strength, with money on the line. Agents inherit the hallucination problem, so Chapter 2's habit applies. Treat the agent's answer as a draft. Check its numbers against the pivot or the report. Be suspicious in exact proportion to what the decision costs. The agent also only knows the data it can reach. Ask an agent with no access to Maya's registers why Campus dips on weekends and it will produce a fluent, generic guess. You will run that exact experiment below.

### Knowledge Work, Reshaped Department by Department

**Knowledge workers** are people whose work is mostly gathering, judging, and sharing information: analysts, planners, and a growing share of every job with a desk. This chapter's pipeline is their habitat, and AI agents just moved into it. The honest 2026 picture, department by department, is the through-line this book promised in Chapter 1: the role changes, the judgment stays.

* **Marketing** stopped waiting for the monthly report. Campaigns are dashboards now, and the analyst's job moved from compiling numbers to questioning them, exactly the skill your lab practices.
* **Accounting and finance** watched software absorb the recording (every transaction already lives in a TPS) and shifted toward what the numbers mean: forecasts, exceptions, and fraud patterns like Chapter 8's invoice scams.
* **Operations** runs on the freshest data in the building: staffing against demand, inventory against sales. The manager who can pivot a sales export makes better schedules than the one who cannot.
* **Human resources** reads its own dashboards (hiring pipelines, retention patterns) with a legal and ethical overlay you can now name: that data is people, and Chapter 8's privacy rules follow it.
* **Information technology** moved from fixing machines to running the pipeline itself: the systems ladder is IT's product, and every department is its customer.

Notice what every bullet shares. The tools draft, total, and flag. A person still decides, and the person who understands the pipeline (where the number was born, what got summarized away, what the agent might have invented) decides better. That person, by the end of this lab, is you.

### Try It Yourself 9.3: Ask an Agent Without the Data 🛠️

**Predict:** You will ask a free AI answer engine why a coffee shop's campus location might dip on weekends. Commit two predictions in writing: will the answer be plausible, and will it be specific to any real shop?

**Run:** Ask one (a search engine's answer box works, per this course's no-account rule). Read the response against what you know about Maya's actual situation.

**Explain:** In 1-2 sentences, state what the answer got right in general and what it could not possibly know. Then name what an agent would need before its answer beats your pivot table.

### Quick Check 9.3 ✅

1. Contrast the two generations in one sentence each: how an expert system knows things, and how an LLM-based agent produces answers. Then name the failure mode the newer one adds.
2. A manager says "the dashboard says Tuesday mornings are down 20 percent, so cut Tuesday staff." Give the two source questions this section says to ask before acting on any dashboard number.
3. Name two departments from this section and, for each, one task the software absorbed and one judgment that stayed human.

---

## 9.4 Ask the Grid: Sort, Filter, and the Pivot Table

Maya's June export is 571 rows by 12 columns: every line item, at every location, with its date, week, day type, daypart, channel, category, item, quantity, and totals. Chapter 6 gave you two tools for asking questions of data. This section returns them briefly before handing you the third, the one built for exactly this moment.

### Sort and Filter at Scale

Sorting and filtering work on 571 rows exactly as they worked on 54. Format the data as an Excel table and the header arrows appear. One upgrade earns a mention: the **multi-level sort**. Sort by one column and ties land wherever they fall. Data > Sort opens the full dialog, where you sort by Location, *then* by Line Total largest-first within each location, and the table organizes itself into three neat leaderboards. Filters also stack: filter Location to Campus and Category to Merch and you are looking at exactly the mugs and bean bags one store sold.

But watch what happens when you try to answer Maya's actual questions with these tools. "What was each location's June revenue?" Filter to 7th Street, read the status bar's sum, write it down, refilter to Roosevelt Row, repeat. Three questions like that and you are the summary system, doing rung-two work by hand. The grid can do that job itself.

### The Pivot Table: Summaries You Assemble

A **pivot table** is a summary table the grid builds for you: you name the categories and the math, and it groups every row and totals them in seconds. (Excel writes it PivotTable. The idea is bigger than the brand.) Where a formula answers one question in one cell, a pivot table answers a whole family of questions at once. It also rearranges itself when you change your mind. It is the single most valuable Excel skill on the analyst side of office life. It is also the MIS rung of the ladder, self-serve.

The mechanics: click anywhere in your data table, choose Insert > PivotTable, and accept New Worksheet. Excel presents an empty layout plus a field list, one field per column of your data. You build the summary by dragging fields into four boxes:

* **Rows:** the categories to group by (drag Location here and the pivot grows one row per store)
* **Values:** the numbers to compute (drag Line Total here and each row totals its store's sales)
* **Columns:** an optional second grouping, spread sideways (Day Type here splits every row into Weekday and Weekend)
* **Filters:** an optional gate over the whole table (Week here lets you show one week at a time)

Drag Location to Rows and Line Total to Values, and Maya's first question is answered before her coffee cools:

| Row Labels | Sum of Line Total ($) |
| ---------- | --------------------- |
| 7th Street | 2088.25 |
| Campus | 1390.75 |
| Roosevelt Row | 1515.75 |
| **Grand Total** | **4994.75** |

Three details make pivot output professional. Values default to SUM for numbers. Value Field Settings changes the math (COUNT for how many, AVERAGE for typical size) and sets the number format, so revenue reads as currency. Row labels sort A to Z by default, and More Sort Options under their header arrow re-sorts them by value, largest first. And the whole thing rebuilds when you drag differently: swap Location for Category and the same seconds produce June by product family. That swap is why analysts say "pivot": same data, new angle, no formulas written.

Two behaviors of pivot tables surprise everyone once, so meet them here. First, a pivot table is a view. It changes nothing in your data, exactly like Chapter 6's filters. Double-click any number in it and Excel opens a new sheet holding the exact source rows behind that number. That is Section 9.2's drill down as a literal double-click. Second, a pivot table does not watch its source. Edit a value it summarizes (a line total, say) and the pivot holds its old answer until you right-click it and choose Refresh. The live-grid rule from Chapter 6 has this one exception, and analysts who forget it present stale numbers with fresh confidence.

### Honest Denominators, One More Time

Pivots make totals effortless, and totals invite the Chapter 7 mistake at a new scale. The export's four full weeks hold 20 weekdays and 8 weekend days. A pivot of revenue by Day Type will show a much bigger weekday sum, and it means almost nothing: five weekdays for every two weekend days guarantees it. Before comparing unequal groups, divide by the days: weekday total over 20 against weekend total over 8 turns raw sums into honest daily averages. In the lab, that one division is what separates the true Campus story from the comfortable chain-wide average, and it is the difference between an analyst and a person with software.

### Try It Yourself 9.4: Your First Pivot, on Familiar Ground 🛠️

**Predict:** Chapter 3 promised that the Chapter 6 workbook would feed the Chapter 9 analysis, and here it is. Open your Chapter 6 file, `assets/code/chapter-06/device-comparison.xlsx` (a throwaway copy is fine). From memory of Skills Lab 6A, commit two predictions in writing: how many of the 54 devices are laptops, and which category carries the highest average price.

**Run:** Click in the data, Insert > PivotTable, New Worksheet. Drag Category to Rows, Device ID to Values (it becomes a COUNT), then Price to Values as a second entry and change it to AVERAGE with a currency format.

**Explain:** In 1-2 sentences, check both predictions against the pivot (22 laptops, and desktops average highest at about $813). State what this pivot did that Chapter 6's filters could not do in one view.

### Try It Yourself 9.5: Catch the Pivot Sleeping 🛠️

**Predict:** Still in the device file, with your pivot showing average prices: you will raise Stone Tower's price by $100 in the source data. Commit a prediction in writing: does the Desktop average in the pivot change by itself?

**Run:** Change the price, watch the pivot, then right-click the pivot and choose Refresh. Undo everything after (++ctrl+z++ or ++cmd+z++ works in reverse order).

**Explain:** In 1-2 sentences, state the rule this proves and the habit it demands before you ever present pivot numbers.

### Quick Check 9.4 ✅

1. Choose the tool for each job: sort, filter, pivot table, or a combination. The jobs: the single biggest sale in the file, June revenue for every category at every location in one view, and only the Campus merch rows.
2. A teammate panics: "your pivot deleted the other columns!" Reassure them in two sentences using the view idea, and name the double-click that proves the source rows still exist.
3. Your pivot says a category totals $995.75. A colleague corrects three of that category's line totals in the source sheet. State what the pivot shows now, why, and the exact move that fixes it.

---

## 9.5 Summary and Retrieval 💡

### Key Concepts

* Information needs an altitude. Functions (operations, marketing, accounting, HR, IT) each ask their own questions of the same data. Management levels need less detail as decisions get bigger. Supervisors run the day on specifics, middle managers run the month on summaries, and top management runs the years on trends. Summarizing upward is attention arithmetic, not dumbing down.
* Data climbs a ladder of systems. Transaction processing systems capture every event completely and never summarize. Management information systems turn transactions into routine summaries. Decision support systems host the what-ifs (a skilled spreadsheet is one). Business intelligence names the whole practice, and drilling down walks a summary back to its receipts. Summaries are only as honest as the transactions beneath them.
* The modern front end is the dashboard, charts doing full-time work, and the AI agent, a large language model connected to company data that answers questions in plain language. Both inherit old obligations: dashboards obey chart ethics and deserve source questions, and agents hallucinate, so their answers are drafts to verify against the data. Department by department, software absorbed the recording and the judgment stayed human.
* The pivot table is the self-serve summary rung: drag fields to Rows, Columns, Values, and Filters, and the grid groups and totals in seconds. It is a view: nothing in the source changes, and a double-click drills down to the rows behind any number. It does not refresh itself (right-click > Refresh before presenting). And its totals still need honest denominators: divide unequal groups by their day counts before comparing.

### Key Terms

See course glossary for full definitions

* management levels (Section 9.1)
* transaction processing system (TPS), management information system (MIS), decision support system (DSS), business intelligence, drill down (Section 9.2)
* dashboard, expert system, AI agent, knowledge worker (Section 9.3)
* multi-level sort, pivot table (Section 9.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the three management levels, the time horizon each runs on, and why detail shrinks as altitude rises.
2. Name the rungs of the systems ladder from register to decision, with one Desert Bloom example per rung.
3. State the two source questions to ask any dashboard number, and the verification habit that applies to an AI agent's answer.
4. Describe, from memory, how you would build a pivot table showing revenue by category at each location: which field goes in which box.
5. State the pivot table's two surprising behaviors (the view rule and the refresh rule) and the denominator rule for comparing weekdays to weekends.

---

## 9.6 Skills Lab 9A: Sort, Filter, Pivot: Answers from Sales Data

**Goal:** Be Maya's decision support for a morning. Compress 571 rows of June sales into the summaries, daily averages, and trend an owner can act on, then tell Maya what to do about the Campus store's weekends.

**Dataset or starter files:** One provided file in `assets/code/chapter-09/` from the course data pack. `coffee-sales.xlsx` holds Desert Bloom's June export on a worksheet named `SalesData`: 571 line items across three locations, four Monday-to-Sunday weeks, two channels, and five categories. The folder README is the data dictionary (the file is a teaching-sized sample: real months run far longer, and the pivots work the same). Download the data pack from Canvas, extract it, and work at the extracted `cis105` root. You will load the provided file, never retype it.

**Scenario:** Maya has four questions, in her own words. Where did June's money come from? What sells? Is Bloom Ahead growing or was the launch buzz? And what is wrong with Campus? She suspects the answer to the last one involves weekends. The export covers four full weeks, 20 weekdays and 8 weekend days, a fact your denominators will need.

!!! note
    Excel for the web can complete this lab: tables, multi-level sorts, and pivot tables (Insert > PivotTable) all work in the browser. The pivot field list is arranged slightly differently, and Refresh lives on the right-click menu in both versions.

### Part 1: Foundation (Aligns with Objective 9.3)

1. Open `coffee-sales.xlsx` and immediately save your working copy as `skills-lab-9a-lastname.xlsx` (File > Save As), so the pack original stays clean.
2. Look before you compute. Scroll the data once and read the 12 column headers against the README's data dictionary. Then confirm the row count: select column A, and the status bar's count reads 572, the header plus 571 data rows. Freeze the top row.
3. Format columns K and L as currency. Then format the data as an Excel table named `Sales`: click any cell in the data, Home > Format as Table, confirm headers, and name it on the Table Design tab.
4. Run a multi-level sort (Data > Sort): by Location A to Z, then by Line Total largest to smallest. Record the single biggest line item at Campus (ID, item, and amount) for your own bearings. Then re-sort by Order ID, A to Z (a text column sorts alphabetically), which restores chronological order.
5. Stack two filters: Location to Campus, Category to Merch. Read the status bar's sum of the visible Line Total cells and record it. Clear all filters and confirm all 571 rows return. You have just done rung-two work by hand, once, so the pivot's value is about to be obvious.

### Part 2: Application (Aligns with Objectives 9.3 and 9.2)

1. Build your first pivot. Click in the `Sales` table, Insert > PivotTable, New Worksheet. Rename the new sheet `RevenuePivots` (semantic names, always). Drag Location to Rows and Line Total to Values, then set the value's number format to currency (Value Field Settings > Number Format). Record the three location totals and the grand total: this is Maya's first question, answered.
2. Pivot the same data a second way: drag Location out of Rows and Category in. Sort the rows largest-first by revenue (the Row Labels arrow > More Sort Options, or right-click a value > Sort). Record the top category and its total, and notice what a Phoenix June does to the hot-versus-cold contest.
3. Add Count of Order ID to Values alongside the revenue. Two columns now describe each category: how much money, and how many line items. Note the category that is small in count but large per line. Merch sells rarely and dearly, and your two value columns just proved it.
4. Prove the view rule: double-click the Campus revenue number in your first pivot layout (rebuild it with Location in Rows if needed). Excel opens a sheet of exactly the Campus rows behind that number. That is drill down as a double-click. Delete the drill-down sheet after you look.
5. Prove the refresh rule: in the `Sales` table, find any Merch line and raise its Line Total by $10, typing over the value (call it a corrected transaction). Watch the pivot hold its old totals, right-click the pivot and choose Refresh, and watch Merch move. Then undo your change (++ctrl+z++ or ++cmd+z++) and Refresh again.

### Part 3: Extension (Aligns with Objectives 9.2 and 9.1)

1. Answer the Campus question honestly. Build a new pivot on a sheet named `CampusQuestion`: Location to Rows, Day Type to Columns, Line Total to Values (currency format). The weekday column will dwarf the weekend column everywhere, and Section 9.4 told you why that comparison is not yet honest.
2. Make the denominators honest. Beside the pivot, build a small block of daily averages: each location's weekday total divided by 20, and its weekend total divided by 8. Type the cell references by keyboard instead of clicking (clicking a pivot cell inserts a GETPIVOTDATA formula that will not fill), or retype the totals. Label the block clearly. Now read the story: two locations hold or even grow their weekends, and Campus falls off a cliff.
3. Answer the app question. Build a third pivot on a sheet named `AppTrend`: Week to Rows, Channel to Columns, Line Total to Values. Then change the math to percentages: right-click a value > Show Values As > % of Row Total. Read Bloom Ahead's share, week 1 through week 4, and record all four.
4. Chart the trend for Maya. From the `AppTrend` pivot, Insert > a clustered column PivotChart (or select the pivot's cells and insert a column chart in Excel for the web). Title it with the finding, label the axes, and check the honesty rules from Chapter 8: value axis at zero, title that states the claim.
5. Write the recommendation. In a cell below your daily-average block on `CampusQuestion`, write Maya three sentences about Campus weekends. Sentence one: the honest numbers, citing your weekday and weekend daily averages. Sentence two: one action (close weekends, shorten hours, or change the weekend offer). Sentence three: one thing she should check before acting that this file cannot tell her. Wrap the text and widen the cell so it reads cleanly.
6. Add a new worksheet named `Questions & Analysis`. Answer the two questions below in cells A1 and A3 with Wrap Text on.

### Questions & Analysis 🤔

Answer both questions on your `Questions & Analysis` worksheet. These answers carry significant rubric weight.

1. Compute the chain-wide daily averages from your Day Type pivot's grand totals: weekday total over 20, weekend total over 8. They sit close together, yet your Campus block tells a different story. Using your own numbers, explain how the chain-wide average concealed the Campus dip and which locations' strong weekends did the concealing. Then state the general rule about aggregates and segments that Section 9.4 and Chapter 7's denominator lesson both taught.
2. Bloom Ahead's revenue share grew every week of June (cite the four weekly shares). Argue both sides for Maya. First, why the trend is good news. Second, what it might be costing her that this file cannot show: think about what the counter loses, what the app charges her per order, and what Petal Points discounts do to margin. Close by naming the one follow-up question you would ask, and which rung of Section 9.2's systems ladder would answer it.

**Submission:** Submit one file: your workbook `skills-lab-9a-lastname.xlsx`. It carries the `Sales` table, the `RevenuePivots` sheet, the `CampusQuestion` sheet with its daily-average block and recommendation, the `AppTrend` sheet with its pivot chart, and the `Questions & Analysis` worksheet. The file name uses your own last name.

### Rubric: Skills Lab 9A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s). Your instructor sets
the point weights in your course. The criteria and levels are the
same everywhere.

---

## 9.7 Review Questions 🔄️

1. **Remember:** Match each system to its job: transaction processing system, management information system, decision support system, dashboard. Jobs: hosts what-if scenarios before money moves, records every event completely, displays live summaries where the reader lives, delivers routine summaries to middle management.

2. **Understand:** Maya's owner-level June review fits on one screen: four numbers and a chart, distilled from 571 rows. Explain what was traded away in that distillation, why the trade is correct at her altitude, and the move she can make (name it) when one summarized number needs proving.

3. **Apply:** A gym owner wants to know whether morning class attendance is growing against evening attendance across a 12-week export of check-in records. Name the fields you would drag to Rows, Columns, and Values, and the Show Values As choice that turns the answer into shares instead of raw counts.

4. **Evaluate:** An AI agent wired to Desert Bloom's dashboard recommends: "Close Campus on weekends. The data shows weekend revenue is weak." Judge the advice. What does the data genuinely support? What does the agent not know (name at least two missing pieces, cost-side or strategy-side)? And what should Maya do with the advice before acting on it?

---

## Further Reading 📖

* [Microsoft Support: Create a PivotTable to analyze worksheet data](https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576) - The official walkthrough of the tool this chapter centers on, including the field list and value settings.
* [Microsoft Support: Sort data in a range or table](https://support.microsoft.com/en-us/office/sort-data-in-a-range-or-table-62d0b95d-2a90-4610-a6ae-2e545c4a4654) - The full sorting reference, including the multi-level dialog this chapter uses.
* [U.S. Bureau of Labor Statistics: Occupational Outlook Handbook](https://www.bls.gov/ooh/) - The federal career reference behind this chapter's department-by-department picture: duties, outlooks, and how data reshapes each role.
* [Microsoft Support: Excel help and learning](https://support.microsoft.com/en-us/excel) - The standing reference for tables, sorting, filtering, and PivotTables.

---

## Looking Ahead ⏩

You can now follow a coffee order from the register to the owner's decision, and you have sat at every altitude on the way. But look at where your pivot's answers came from: hundreds of structured records, each one a set of fields holding exactly one fact. Chapter 10 goes to the place records like that live. You will learn how databases organize data into tables, fields, and relationships, and why every AI tool you have met this term sits on top of one. The questions your pivots answered become queries, which a database answers at any scale. The lab thread turns with it: Airtable arrives, and the bookings behind Saguaro Hall's calendar, a thread running since Chapter 4, become a base you design yourself.
