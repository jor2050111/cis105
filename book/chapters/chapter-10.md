# Chapter 10: Where Data Lives: Tables, Records, and Relationships

Darnell Brooks runs Saguaro Hall, the downtown Phoenix event venue you met in Chapter 4. This week a problem arrived that no update notice could explain. He went to call the City of Phoenix Parks contact, pulled their number off a recent booking, and reached a dead line. He tried again from an older booking, and a different number rang through. Same client, two phone numbers, both living in his own records. One of them is wrong, and the export from his booking system will not tell him which.

Look at why this happened, because it is the whole chapter in one mistake. Darnell's booking system hands him a flat table: one row per booking, and every row repeats the client's name, email, and phone. The City of Phoenix Parks has booked Saguaro Hall six times, so their phone number sits in his file six times. Type it once by hand, on one booking, and now the file disagrees with itself. The data did not break. The design did. A fact that should live in one place was copied into six, and copies drift.

This chapter is about the place data lives when it is built to stay honest. Chapter 9 left you with hundreds of records, each one a set of fields holding exactly one fact, and promised to show you where records like that belong. Here it is: the database. You will learn how a database organizes data into fields, records, tables, and the relationships that let tables link without repeating themselves. Then the Skills Lab thread turns. Airtable arrives, and the bookings behind Saguaro Hall's calendar, a thread running since Chapter 4, become a connected base you design yourself. By the end, Darnell's phone problem cannot happen, because the phone will live in one place, and you will have built it.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero), builds on Chapter 9 (records and fields), Chapter 6 (sort, filter, views), Chapter 8 (least privilege), and Chapter 1 (a file versus a login)
* **Deliverables:** Skills Lab 10A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-10.1 (Understand):** Explain how a database organizes data into fields, records, tables, and relationships, and how a key links tables without duplication (Sections 10.1 and 10.2)
* **MLO-10.2 (Apply):** Build a connected Airtable base with typed fields, linked tables, and filtered views that answer business questions (Sections 10.1 through 10.3 and Skills Lab 10A)
* **MLO-10.3 (Analyze):** Examine the security, privacy, and data-quality risks a shared database carries and the safeguards that reduce them (Section 10.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO XIII (Apply):** Produce documents, spreadsheets, databases, and presentations with industry-standard productivity software
* **CLO VI (Analyze):** Examine system security and privacy risks and the safeguards that reduce them
* **CLO X (Understand):** Explain the terminology, uses, and limits of technology in business and society

---

## 10.1 From Cells to Records: How a Database Sees Data

Chapter 9 handed you a 571-row sales export and taught you to summarize it. You already know its shape without naming it. Each row was one sale, and each column held one kind of fact. A database gives those parts names and adds one thing a spreadsheet does not enforce: rules about what each piece of data is allowed to be.

### The Ladder from a Character to a Base

Data stacks up in a fixed order, and every level has a name you will hear in job postings and app menus for the rest of your career.

* A **character** is one letter, digit, or symbol. The `M` in Main Hall.
* A **field** is a single named piece of data about one thing, and in a database it has a **field type** that fixes what it can hold. Saguaro Hall's Event Date field holds a date, its Guest Count field holds a number, its Contact Email field holds an email address. The type is the difference from a spreadsheet cell, which will hold anything you type. A date field rejects "next Tuesday." That refusal is a feature.
* A **record** is everything the database knows about one thing, all its fields together. One booking, `SH-1005`, is a record: its date, space, organization, guest count, price, and status in a single row.
* A **table** is a stack of records of the same kind. Saguaro Hall's Bookings table holds one record per booking, every row the same shape.
* A **database** is an organized collection of related tables. Airtable calls one a **base**. Saguaro Hall's base will hold a Bookings table and a Customers table, connected.

This ladder (character, field, record, table, base) is the **data hierarchy**, and it is worth memorizing because every database tool on Earth is built on it. Order DB-1041 from Chapter 9, the iced latte that a transaction system recorded and never summarized, was a record. This chapter is the place records like that live.

You might ask why not keep using a spreadsheet. Chapter 6 sorted and filtered a device sheet, Chapter 9 pivoted a sales export, and a single Airtable table looks like a grid too. The line between them is what the tool enforces and connects. A spreadsheet trusts you to keep every cell consistent by hand. A database enforces the type of each field, links related tables so a fact lives once, and serves many people at the same time. When your data is one short list you check yourself, a spreadsheet is fine. When it repeats, connects, and other people depend on it, a database earns its keep. Saguaro Hall crossed that line the day one client's phone number could be wrong in six places.

### The View You Think In, and the One You Never See

Here is a distinction that trips up nearly everyone, so meet it head on. The friendly grid of rows and fields you work in is the **logical view**: data organized the way a human thinks about it. Underneath, the database stores those records as bytes scattered across a disk or a server, in whatever arrangement runs fastest. That is the **physical view**, and you never touch it. You do not decide where on the drive booking `SH-1005` sits, or in what order. The database hides all of that and shows you the clean logical picture instead.

That hiding is the point, not a limitation. Because the tool manages the physical storage, you get to ask questions in human terms ("show me every Pending booking") without knowing or caring how the bytes are filed. A spreadsheet blurs the two views: the cells you see are close to how the file is stored. A database separates them on purpose, and that separation is what lets one database serve millions of records and thousands of people at once.

### No File to Save

Chapter 1 flagged one more difference and promised this chapter would examine it up close. When you build a base in Airtable, no file lands on your computer. There is no `booking.xlsx` to save, email, or lose on a thumb drive. The base lives on Airtable's servers, saves itself as you type, and reaches you through a login from any browser on any machine. Chapter 1 called this the trade of a file for a login, and it is the daily reality of cloud tools. The upside is real: your base follows you everywhere, and several people can work in it at the same time. So is the cost: you do not hold the file, and no connection means no access. You will feel both in the lab, starting with the small surprise of finishing your work and having nothing to "save as."

### Try It Yourself 10.1: Find the Record 🛠️

**Predict:** You will open the booking export from the data pack, `saguaro-bookings.csv`, in any spreadsheet app or text viewer. Before you do, commit a number in writing: how many fields (columns) do you think describe one booking?

**Run:** Open the file and find the row for booking `SH-1005`. Count its columns, and read across its fields. Then find every row where the Organization is City of Phoenix Parks and Rec.

**Explain:** In 1-2 sentences, state how many fields one booking record holds, and name one field whose type is clearly not plain text (a date, a number, an email). Then note how many times the City of Phoenix Parks contact information repeats.

### Quick Check 10.1 ✅

1. Put the data hierarchy in order from smallest to largest, and give a Saguaro Hall example of each level: character, field, record, table, base.
2. A classmate says "a field is just a spreadsheet cell." Name the one thing a database field has that a spreadsheet cell does not, and give an example of an entry it would refuse.
3. Explain the difference between the logical view and the physical view of a database, and state which one you manage.

---

## 10.2 Keys and the End of Duplication

Now name Darnell's problem precisely and fix it for good. His flat export copies each customer's contact details onto every booking. The City of Phoenix Parks email and phone appear six times, once per booking, and the moment one copy changes, the copies disagree. Booking `SH-1005` says one thing, the client's five other bookings say another, and a confirmation call goes nowhere. Repeated data is not just wasteful. It rots.

### The Key That Names a Record

Before two tables can connect, each record needs a stable handle. A **primary key** is a field whose value is unique for every record and never changes, so it can stand in for the whole record. Saguaro Hall's Booking ID does this job: `SH-1005` points to exactly one booking, today and next year.

New database builders reach for the wrong handle constantly, so be deliberate. A name is a bad key: two clients can share one, and people change their names. A row's position is worse, because sorting moves it. Even a phone number fails, as Darnell just learned, because it changes and can be mistyped. A good key is unique, stable, and meaningless enough that nothing makes it change. That is why systems mint IDs like `SH-1005` or `DB-1041` instead of trusting a name.

### The Link That Replaces the Copy

Here is the move that ends the drift. Instead of copying the customer onto every booking, store each customer once, in their own table, and have each booking **point** to the right customer. That pointer is a **foreign key**: a field in one table that holds the key of a record in another table. Airtable builds it for you with a field type called a **linked record**, and the connection it creates between two tables is a **relationship**.

The difference between a copy and a pointer is the difference between Darnell's bad week and a clean base. A copy is frozen at the moment you typed it, and it goes stale in silence. A pointer always reads the live customer record, so you fix the phone number once, in the Customers table, and all six bookings show the correction instantly. Chapter 9 warned that a summary is only as honest as the transactions beneath it. This is the same truth one floor down: a booking is only as honest as the customer data it points to, and pointing beats copying every time.

Most business relationships have a shape worth naming: **one-to-many**. One customer has many bookings. One student has many enrollments. One product appears on many orders. The "one" side stores each fact once, and the "many" side points back. Organizing tables this way, so each fact lives in exactly one place, is called **normalization**. You do not need the full theory to use the habit: when a fact repeats, give it its own table and link to it.

### The Question a Worksheet Cannot Answer

Chapter 3 promised that a database answers questions like "which customers ordered twice this month?" without breaking a sweat, and that the Chapter 10 base would answer questions no worksheet could hold. This is that payoff. In the flat export, "which organizations booked more than once?" means scrolling and tallying by eye. In a connected base, the answer is already there: open any customer and their linked bookings are listed with them. Across Saguaro Hall's 24 organizations, 17 have booked more than once, and the City of Phoenix Parks leads with six. A relationship turned a counting chore into a fact the base already knows.

### Try It Yourself 10.2: Copy Versus Point 🛠️

**Predict:** In `saguaro-bookings.csv`, the City of Phoenix Parks contact details repeat on every one of their bookings. Predict two numbers in writing. If their office phone changed, how many cells would you edit in this flat file? How many in a base where the customer is stored once?

**Run:** Count the City of Phoenix Parks rows in the file. Then find booking `SH-1005` and compare its Contact Phone to the other City of Phoenix Parks bookings. One of them disagrees.

**Explain:** In 1-2 sentences, state the flat-file edit count versus the connected-base edit count, and explain how storing the phone once would have prevented the disagreement you just found.

### Quick Check 10.2 ✅

1. Darnell suggests using the client's organization name as the key that links bookings to customers. Give one reason a name makes a poor primary key, and name a better choice from the booking data.
2. Explain the difference between copying a customer's phone onto a booking and pointing to it with a linked record. Which one prevents the drift Darnell hit, and why?
3. A field repeats the same supplier address on 40 product rows. Name the design fix in one sentence, using the words table and relationship.

---

## 10.3 The Database Underneath: Queries, Views, and Timing

You have met the parts and the relationships. Now meet the software that runs them, and the two ways every database answers a question and shows its data.

### The Software That Guards the Data

A **database management system** (DBMS) is the software that stores a database, enforces its field types and keys, controls who may see it, and answers questions about it. Airtable is a DBMS with a friendly face. So is Microsoft Access, and so are the industrial engines running behind the apps you used today. The Bloom Ahead coffee app from Chapter 1 keeps its customer accounts and order history in a database, and a DBMS answers every "what did I order last time?" tap. Your learning platform, your bank's app, the airline's seat map: each is a screen sitting on a database, and a DBMS stands between the two. Chapter 9 said every AI tool this term sits on a database. So does nearly every other tool.

### A Query Is Just a Question

The word **query** sounds like code, and it scares people off. It should not. A query is a question you ask your data, and answering it is what a database does best. "Show me every Pending booking." "Which spaces are free next Saturday?" "Which organizations booked more than once?" Those are queries. Chapter 9 said the questions your pivot tables answered would become queries a database answers at any scale, and that is exactly the shift. In Airtable you ask them with filters, sorts, and groups, no code required. Larger databases share a written query language called **structured query language** (SQL), the sentence you write to ask for precise slices of data. You will not write SQL in this course, but you should know the name, because it is the language under a large share of the business world's questions.

### A View Is a Lens, Not a Change

Chapter 6 let you sort and filter a device sheet and called it the first taste of the database questions this chapter asks properly. Here is the proper version. A **view** is a saved lens on a table: a chosen filter, sort, grouping, and set of visible fields. The records underneath never change. Filter the Bookings table to Status is Pending and you see 12 bookings, but you deleted nothing. Clear the filter and all 60 return. This is Chapter 6's rule, promoted: the data does not change, only your window onto it.

A database beats a spreadsheet here in a way that matters at work. Many people can hold different views of the same table at the same time. Darnell keeps a Pending view for follow-ups, the events coordinator keeps a view grouped by space, and a client sees only a calendar. One set of records, many lenses, all live. Airtable's free plan gives you several view types to build from: Grid, Calendar, Kanban, Gallery, and Form. You will build four of them in the lab.

### Now, or on a Schedule

One more distinction runs through every business system, and it decides how fresh an answer has to be. **Real-time processing** handles each event the instant it happens. When a client books the Main Hall for a date, that booking must register immediately, or two clients could claim the same Saturday. **Batch processing** collects events and handles them together, later, on a schedule. Payroll runs once a pay period. A bank posts the day's card charges overnight. Saguaro Hall's month-end invoice run gathers every completed booking and bills them in one sweep.

Neither is old-fashioned. The question is only whether the answer must be current this second. A double-booking cannot wait, so bookings are real-time. An invoice can wait for the month to close, and running it in one nightly batch is cheaper and simpler than billing each event the moment it ends. Most companies run both, side by side, and knowing which a task needs is a real design decision. The database most business apps run on, the kind that stores data in linked tables of rows and fields, is called a **relational database**, and it handles both timings. Other shapes exist for special jobs, but the relational model is the workhorse you will meet almost everywhere.

### Try It Yourself 10.3: Name the Timing 🛠️

**Predict:** Think of two things you did online in the last day: one that had to update instantly, and one that could safely wait for a nightly run. Predict in writing which of your two is real-time and which is batch.

**Run:** Test each against this section's rule. Did the result have to be correct the instant you acted (a seat reserved, a payment authorized), or would a scheduled sweep have been fine (a monthly statement, a weekly report)?

**Explain:** In 1-2 sentences, name your real-time example and your batch example, and state the cost of getting the timing wrong for the real-time one.

### Quick Check 10.3 ✅

1. State in one sentence what a DBMS does that a plain spreadsheet file does not, and name two DBMS tools from this section.
2. Rewrite this pivot-table question from Chapter 9 as a database query in plain language: "revenue by category at each location." Then name the Airtable tools (filter, sort, group) you would reach for.
3. Classify each as real-time or batch, and defend one: reserving an event date, generating end-of-month invoices, and authorizing a card payment at the counter.

---

## 10.4 Who Can See It: Security, Privacy, and Data Quality

A database is a pile of other people's information, gathered in one place and easy to copy. Saguaro Hall's base holds 24 organizations' names, emails, and phone numbers. That is personal data, and Chapter 8's privacy rules follow it into every row. The convenience that makes a database powerful, one place holding everything, is the same property that makes it a target. This section is the guardrail.

### Least Power, One Floor Down

Chapter 8 built a whole defense on one idea: give each account the least power that does its job, so a mistake or a bad click stays small. That principle scales straight into the database. Not everyone who touches Saguaro Hall's base should be able to do everything to it. Darnell's two weekend front-desk hires need to read the day's bookings, not export the entire customer list. A volunteer setting up chairs needs nothing at all.

A DBMS enforces this through **access control**: rules that decide who may see or change which data. Airtable offers levels you can match to the job. A creator builds and restructures. An editor changes records. A commenter can only discuss. A read-only viewer looks but cannot touch. And a **form** lets an outsider submit one record, a booking request, without ever seeing the table behind it. Match each person to the least level that does their work, and Chapter 8's principle protects a database exactly the way it protected a laptop.

!!! tip "Tech in Your Field"
    Every major in this room will work inside a database built from these parts, and will answer for the data in it. Nursing and health sciences students will chart in electronic health records, where the same privacy law from Chapter 8 (HIPAA) governs who may open a patient's row. Business and entrepreneurship students will run customer relationship databases, and the contact list is the company's most valuable and most breachable asset. Public safety students will file into records systems where an access log shows who read what, and reading a file without cause is itself a violation. Education and counseling students will work in student information systems where a federal law (FERPA) fences off grades and notes. The tool changes by field, the parts do not, and in every one of them the person who understands access control is the person trusted with the keys.

### Honest Data at the Door

Chapter 9 gave you a phrase: garbage in, garbage up the ladder. **Data validation** is how a database fights that garbage at the moment of entry: rules that check each value as it arrives. A single-select field offers a fixed list of choices instead of a free-typed box. A date field expects a date. A form can mark a field required so it cannot be skipped. Stricter databases enforce these rules hard and refuse anything that does not fit, while a lighter tool like Airtable leans on them more gently, which leaves some of the discipline to you. Either way, the strongest safeguard in this lab was not a field rejecting a bad value. It was the design. Store each customer's phone once, in the Customers table, and it cannot drift across six bookings, whatever a single field will or will not accept. The connected base is not just tidier. It is more honest, by construction.

### The Base Under the Robot

Chapter 9 introduced the AI agent, software that reads a company's data and drafts answers in plain language. Now you can see what it stands on. An agent is only as good as the database beneath it. Point one at a clean, connected base with honest types and clear relationships, and it can answer "which client should we call back first?" well. Point the same agent at Darnell's flat export, with its drifted phones and its facts copied six ways, and it will answer with confidence and be wrong, because it inherited the mess. Every AI tool this term sits on a database. The quality of the base decides the quality of the answer, which means the design work in this chapter is the groundwork the smartest tool cannot skip.

### Try It Yourself 10.4: Assign the Least Power 🛠️

**Predict:** Three people touch Saguaro Hall's base: Darnell (the manager), a weekend front-desk hire who checks in guests, and an event client who wants to request a date. Predict in writing which Airtable access level each should get: creator, editor, read-only viewer, or a form only.

**Run:** Open Airtable's Share menu, or its documentation on collaborator permissions, and read what each level can do. Check your three guesses against the real capabilities, and correct any that handed out too much power.

**Explain:** In 1-2 sentences, justify the front-desk hire's level against the least-privilege principle, and name one thing that hire should not be able to do.

### Quick Check 10.4 ✅

1. Apply least privilege: a new volunteer needs to submit event ideas but should never see the customer list. Name the Airtable access choice that fits, and say why it is safer than making them an editor.
2. Give one example of a field type or rule that stops bad data at entry, and name the error it prevents.
3. Two AI agents answer the same question. One reads a clean connected base, the other reads a flat export full of copied, drifted data. Explain why their answers differ even though the question is identical.

---

## 10.5 Summary and Retrieval 💡

### Key Concepts

* Data stacks in a fixed hierarchy: character, field, record, table, and base. A field carries a type that a spreadsheet cell does not, so a database refuses values that do not fit. You work in the logical view, the friendly grid, while the database hides the physical storage. In the cloud, a base trades the saved file for a login, following you to any machine and letting several people work at once.
* Repeated data drifts. A primary key is a unique, stable handle for a record, and a name or a phone number makes a poor one. A foreign key, built in Airtable as a linked record, points to a record in another table instead of copying it, so a fact fixed once is fixed everywhere. Storing each fact in one place is normalization, and it turns "which organizations booked twice?" into a question the base already answers.
* A DBMS stores the data, enforces the rules, and answers questions. A query is a question, asked with filters, sorts, and groups (or written in SQL), not a feat of coding. A view is a saved lens: the records never change, and many people can hold different views at once. Real-time processing handles each event instantly, batch processing handles events on a schedule, and most businesses run both.
* A database concentrates personal data, so Chapter 8's rules follow it. Access control gives each person the least power that does the job, from creator down to a form that reveals nothing. Data validation keeps garbage out at the door, and a connected base cannot drift the way a flat file does. Every AI tool sits on a database, and the quality of the base sets the ceiling on the quality of the answer.

### Key Terms

See course glossary for full definitions

* character, field, field type, record, table, database, base, data hierarchy, logical view, physical view (Section 10.1)
* primary key, foreign key, linked record, relationship, one-to-many relationship, normalization (Section 10.2)
* database management system (DBMS), query, structured query language (SQL), view, real-time processing, batch processing, relational database (Section 10.3)
* access control, data validation (Section 10.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the data hierarchy from smallest to largest, and give a Saguaro Hall example at each level.
2. State what makes a good primary key, and explain why a person's name usually fails the test.
3. Explain, in your own words, how a linked record prevents the phone-number drift that opened this chapter.
4. Define a query and a view, and state the one thing a view never does to the data underneath.
5. Name two access levels a DBMS can grant and the least-privilege reason you would choose a lower one for a part-time worker.

---

## 10.6 Skills Lab 10A: From CSV to Connected Base

**Goal:** Turn Saguaro Hall's flat booking export into a connected two-table base where each fact lives once, then use it to answer Darnell's real questions and defend who is allowed to see what.

**Dataset or starter files:** Two provided files in `assets/code/chapter-10/` from the course data pack. `saguaro-bookings.csv` holds 60 event bookings across 13 fields. `saguaro-customers.csv` holds 24 organizations, the clean contact list the bookings will link to. The folder README is the data dictionary. Download the data pack from Canvas, extract it, and import the files from the extracted `cis105` root. You will import the provided files, never retype them.

**Scenario:** Darnell's booking system exports a flat table that copies every customer's contact details onto every booking, which is how one client's phone number came to disagree with itself. You will rebuild his data as a connected base: bookings in one table, customers in another, joined by a relationship, so a fact fixed once is fixed everywhere. Then you will build the views he needs and decide who gets which keys.

!!! note
    This lab uses Airtable, this course's database tool, in any modern browser. Creating an Airtable account is free and needs no credit card, the same way your Microsoft 365 account is free through the college. Everything below stays inside Airtable's free plan. Nothing here requires a paid feature or an AI subscription.

### Part 1: Foundation (Aligns with MLO-10.1, MLO-10.2)

1. Create a new base named `Saguaro Hall Bookings` (semantic names, always). In the first table, use Add or import and choose CSV file to import `saguaro-bookings.csv`. Rename the table `Bookings`.
2. Set the primary field. Make Booking ID the first field, and confirm every value is unique (`SH-1001` through `SH-1060`). This is your primary key. Airtable does not enforce uniqueness for you, so that check is yours to make.
3. Fix the field types Airtable guessed as plain text. Set Event Date to Date, Guest Count and Hours to Number, Quoted Price to Currency, Contact Email to Email, and Contact Phone to Phone number. Set Space, Package, and Status to Single select. Set Add-Ons to Multiple select, and when Airtable offers to split the comma-separated values, accept, so `Decor, Parking` becomes two tags.
4. Feel the duplication before you fix it. Sort the table by Organization (A to Z), and look at the six City of Phoenix Parks and Rec rows. Their email and phone are copied down every row. Find booking `SH-1005` and confirm its Contact Phone disagrees with the client's other bookings. Record the two different numbers for your write-up.
5. Build a clean Grid view showing Booking ID, Event Date, Space, Organization, Status, and Quoted Price. This is your working view.

### Part 2: Application (Aligns with MLO-10.1, MLO-10.2)

1. Add a second table to the base by importing `saguaro-customers.csv`. Rename it `Customers`, and make Organization its primary field. This is the one place each customer's details will live.
2. Build the relationship. In the Bookings table, change the Organization field's type to Link to another record, and point it at the Customers table. Airtable matches each booking's organization name to a customer and links them. Because the names match exactly, no duplicate customer records are created. Spot-check that the links resolved cleanly.
3. See the relationship pay off. Open the City of Phoenix Parks and Rec record in the Customers table and confirm its six linked bookings appear together. This is the question a worksheet could not answer, now answered by the base.
4. Retire the copies. In the Bookings table, delete the Contact Email and Contact Phone fields. Those facts now live once, in Customers, reached through the link. Confirm that `SH-1005`'s drifted phone is gone, because the number now exists in exactly one place.
5. Answer a repeat-customer query. Group or scan the Customers table to list the organizations with more than one linked booking, and record how many there are (you are looking for 17 of the 24).

### Part 3: Extension (Aligns with MLO-10.2, MLO-10.3)

1. Build the views Darnell runs his week on. Create a Grid view filtered to Status is Pending (record the count), a second Grid view grouped by Space, and a Calendar view on Event Date so the month's bookings show on a calendar.
2. Add a Kanban view with Status as the stacking field, so bookings move through Confirmed, Pending, Completed, and Cancelled columns like cards. Note how a view rearranges the same records without changing them.
3. Flag the over-capacity bookings. Filter one space at a time and look for a Guest Count larger than that space holds (the Meeting Room seats 40, the Courtyard 150, the Main Hall 300). Two bookings break the rule. Record their Booking IDs, and note each one's Status: one was Cancelled, and one was Completed. Decide which is the real warning.
4. Set up honest intake. Create a Form view on the Bookings table for a client to request a date. Include only the fields an outsider should fill: event date, space, event type, guest count, and hours. Leave the linked Organization field off the form, because on a form a linked field lets an outsider search your customer list, the opposite of least privilege. Add one plain text field for the client to type their organization name instead. This is least privilege built into a screen.
5. Write the access plan. In a short document, name the Airtable access level you would give each of three people: Darnell, a weekend front-desk hire, and an event client. Justify each in one sentence against the least-privilege principle.
6. Assemble your deliverable (see Submission) with your share link, three screenshots, and your written answers.

### Questions & Analysis 🤔

Answer both questions in your submission document. These answers carry significant rubric weight.

1. The flat export copied each customer's phone onto every booking, and one copy, `SH-1005`, drifted to a wrong number. Using your connected base, explain why storing the phone once in the Customers table makes that class of error impossible. Name one other field in the original booking export that was needlessly copied and belonged in Customers. Close with the one-sentence rule you would give any team about where a fact should live.
2. Darnell wants his two weekend front-desk hires to check the day's bookings but never see or export the full customer contact list, and he wants event clients to request their own dates. Assign each of the three roles (front-desk hire, event client, and Darnell himself) an Airtable access level or view, and justify each against the least-privilege principle from Chapter 8. Then name one privacy risk that remains even after your permissions are set correctly.

**Submission:** Submit one PDF named `skills-lab-10a-lastname.pdf`. It contains, in order: a read-only share link to your `Bookings` grid view (Share, then a shared view link), then three screenshots, then your access plan, then your two Questions and Analysis answers. The three screenshots are the City of Phoenix Parks customer record showing its six linked bookings, one Part 3 view of your choice, and your Form. Because the base lives in the cloud, the link is the file, which is the Chapter 1 trade made concrete. Use your own last name in the file name.

### Rubric: Skills Lab 10A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s).

---

## 10.7 Review Questions 🔄️

1. **Remember:** Match each term to its meaning: primary key, foreign key, record, view. Meanings: a unique handle for one record, a pointer to a record in another table, everything known about one thing, and a saved lens that filters without changing data.

2. **Understand:** Explain why a database separates the logical view from the physical view, and give one thing you can do because the physical storage is hidden from you.

3. **Apply:** A gym exports a flat sign-up sheet where each class row repeats the member's name, email, and membership level. Name the two tables you would split it into, state the primary key of each, and name the field that becomes the link between them.

4. **Evaluate:** A new volunteer proposes emailing the full customer CSV to every staff member so "everyone has a copy just in case." Judge this plan against the least-privilege principle and the drift problem from this chapter. What are the risks, and what connected-base alternative would you recommend instead, naming the access levels involved?

---

## Further Reading 📖

* [Airtable Support: Getting started with Airtable](https://support.airtable.com/docs/getting-started-with-airtable) - The official first-steps guide to bases, tables, fields, and records, the tool this chapter builds in.
* [Airtable Support: Linked record fields](https://support.airtable.com/docs/linking-records-in-airtable) - How to build the relationship between two tables, the core move of this chapter's lab.
* [Airtable Support: Getting started with Airtable views](https://support.airtable.com/docs/getting-started-with-airtable-views) - Grid, Calendar, Kanban, Gallery, and Form views, and how a view filters and sorts without changing the data.
* [Federal Trade Commission: Protecting Personal Information, A Guide for Business](https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business) - The federal guide to safeguarding the personal data a database concentrates, including access control and disposal.

---

## Looking Ahead ⏩

You built a database, but step back and notice what it was: a solution to a problem, chosen and assembled on purpose. Somebody had to decide that Saguaro Hall needed a connected base instead of a flat export, weigh the cost, design the tables, test it, and move the staff over without losing a booking. That work has a name and a shape. Chapter 11 zooms out from the base to the whole project: the six phases that carry a technology solution from naming the problem to switching everyone over. You will also face the decision every organization now weighs, whether to build a tool, buy one, or subscribe to it. The Airtable thread comes with you. This time you will run a systems project inside a tracker base, and the project you track is the same rollout that produced the base you just built.
