# Chapter 1: People, Data, and Intelligent Machines

It is 7:40 on a Tuesday morning, and the line at Desert Bloom Coffee already reaches the door. You skip it. Three taps on your phone and your order is placed, paid for, and waiting on the pickup shelf by the time you walk in. Nobody at the counter typed anything. Nobody ran your card. The whole transaction felt like magic, and that is exactly the problem. Magic cannot be fixed, improved, or questioned. Systems can.

This chapter pulls the curtain back on that coffee order. Behind every app you use sits the same six-part machine: people, procedures, software, hardware, data, and connectivity. Once you can name those parts, you can reason about any technology you meet, from a hospital's patient records to a food truck's payment reader. That vocabulary is the foundation of this whole course, and it belongs to every major in the room. About half of your classmates are studying business. Others are headed for nursing, public safety, the arts, and a dozen other fields. Every one of those careers now runs on this six-part machine, and AI is changing how, not whether, people like you drive it.

Here is the plan. You will learn the six parts and watch them work together in one coffee order. You will meet the computers this course talks about, from the phone in your pocket to the servers you will never see. You will sort software into its two layers and preview the AI assistants now built into everyday tools. Then you will open Word and produce something professionals still produce every day: a clean, formatted business letter, delivered as a PDF. No prior computing experience is expected anywhere in this book.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero)
* **Deliverables:** Skills Lab 1A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-1.1 (Remember):** Identify the six parts of an information system and the job each part does in an everyday app
* **MLO-1.2 (Understand):** Describe the major types of computers and software this course covers, using the correct term for each
* **MLO-1.3 (Apply):** Produce a formatted business letter in Word from provided content, edited and exported for a professional audience

### This chapter aligns with the following Course Learning Outcomes

* **CLO X (Understand):** Explain the terminology, uses, and limits of technology in business and society
* **CLO II (Analyze):** Classify system and application software and match each type to the tasks it serves
* **CLO XIII (Apply):** Produce documents, spreadsheets, databases, and presentations with industry-standard productivity software

---

## 1.1 Six Parts, One System

Ask most people what a computer system is, and they point at a screen. The screen is the least interesting part. An **information system** is the combination of six parts working together to turn raw facts into useful work: people, procedures, software, hardware, data, and connectivity. Take away any one of them and the coffee order from this chapter's opening never happens.

The most useful habit you can build this term is to look at any app and ask: where are the six parts hiding? Build that habit right now, on the order you just placed.

!!! note "How this book handles new words"
    Every key term appears in **bold** on first use and gets a plain definition on the spot. Each term also lands in the course glossary, the single source of truth for definitions. When a later chapter uses a term you half remember, check the glossary instead of guessing. Precise words are how technical people transfer trust, and building that vocabulary is itself a course outcome.

### One Tap, Six Parts

Walk back through that Desert Bloom order slowly.

You are the first part: a person. In this system you are the **end user**, the person the whole machine exists to serve. The shop's baristas and the developers who built the app are people in the system too.

**Procedures** are the rules and steps people follow when they work with a system. The barista confirms each incoming order with one tap, makes the drink, and sets it on the pickup shelf labeled with a first name. None of that is software. All of it is essential. When a business says "that's our policy," you are usually hearing a procedure.

**Software** is the set of instructions that tells a computer what to do. The ordering app on your phone is software. So is the register program that shows your order to the baristas.

**Hardware** is the physical equipment: your phone, the shop's register screen, and the payment reader by the counter. Hardware without software is a paperweight. Software without hardware is an idea.

**Data** is the raw material: your drink choice, the price, the time you ordered, the name on the cup. Each fact is small and almost meaningless alone.

**Connectivity** is the set of communication links that move data between devices. Your order crossed the Internet from your phone to the shop's register in under a second. Chapter 2 follows that trip in detail.

| Part | What it contributes | In your coffee order |
| ---- | ------------------- | -------------------- |
| People | Judgment, decisions, work | You, the baristas, the developers |
| Procedures | Rules and repeatable steps | Confirm, make, shelve, label |
| Software | Instructions computers follow | The ordering app, the register program |
| Hardware | Physical equipment | Phone, register screen, payment reader |
| Data | Raw facts | Drink, price, time, name |
| Connectivity | Links that move data | The Internet between phone and shop |

### From Data to Information

Data and information are not the same thing, and the difference explains why businesses care so much about both. **Data** is raw, unorganized facts: numbers, words, images, and sounds. **Information** is data that has been organized or processed into something meaningful enough to support a decision.

One order for a large oat-milk latte at 7:40 a.m. is data. Here is the same data after the register software summarizes a month of it: oat milk now outsells whole milk two to one before 9 a.m. That is information, and it changes what the owner stocks, schedules, and puts on the menu board. Same facts, new power. Every chapter in Part IV of this book is about that transformation at business scale.

The same move happens in every field. A single blood pressure reading is data. A chart showing the reading climbing across three shifts is information, and a nurse acts on it. One ticket sale is data. A graph showing that Thursday shows outsell Friday shows is information, and a theater manager reschedules around it. Whatever your major, your working life will sit somewhere on the path from data to decision.

### People Lead the System

Notice which part came first in the list. That order is not alphabetical. It is a claim, and this book will defend it all term: people lead the system, and the other five parts exist to serve them.

Software now drafts email, suggests replies, and answers questions in full paragraphs. It still cannot decide whether the answer is true, fair, or right for your situation. Three jobs stay human:

* **Judgment.** Choosing what the system should do, and when its output is good enough to use.
* **Verification.** Checking an answer against evidence before acting on it. You will practice this in Chapter 2 and in every lab in this book.
* **Trust decisions.** Deciding when to rely on an automated answer and when the stakes demand a human look.

Keep those three jobs in mind every time this book mentions AI. The tools draft. You decide.

### Six Questions for Any Broken System

The six-part model earns its keep the moment something goes wrong. When an app misbehaves, most people poke at the screen and hope. You can do better: walk the parts in order and ask what each one would look like if it were the problem.

Suppose the pickup shelf at Desert Bloom holds the wrong drink under your name. Walk it:

* **People?** Maybe a barista grabbed the wrong cup. Human error is the most common failure in any system.
* **Procedures?** Maybe two orders for "Alex" hit the shelf and the labeling procedure only uses first names. The rule failed, not the person.
* **Software?** Maybe the app sent your customization to the register as a blank line. A defect, and only the developers can fix it.
* **Hardware?** Maybe the register screen froze and the barista worked from memory.
* **Data?** Maybe your saved "usual" order was outdated, so the system did exactly what its records asked.
* **Connectivity?** Maybe the order arrived late or incomplete because the shop's connection dropped mid-sale.

Same symptom, six different causes, six different fixes. Naming the failing part is the first step of every troubleshooting conversation you will ever have, whether you are the customer, the employee, or the person the employee calls for help.

### Try It Yourself 1.1: Six Parts in Your Pocket 🛠️

**Predict:** Think of the last app you used before opening this chapter. If you had turned on airplane mode first, which of the six parts would have failed, and what exactly would you have seen on screen?

**Run:** Open that app now, turn on airplane mode, and try to do what you did earlier. Watch what still works and what breaks. Turn airplane mode back off.

**Explain:** In 1-2 sentences, name the part that failed and explain why some features kept working without it.

### Quick Check 1.1 ✅

1. A campus vending machine takes tap-to-pay cards, tracks its own inventory, and messages the supplier when it runs low. Name the six parts of that information system.
2. Your fitness app says you walked 9,214 steps yesterday. Give one example of data in that sentence and one example of information the app could build from a month of it.
3. A friend says the newest AI tools make the "people" part of the system optional. Using the three human jobs from this section, give one reason the claim fails.

---

## 1.2 The Machines You Will Meet

Every computer in your life, from a smartwatch to a supercomputer, follows the same recipe: hardware runs software, works on data, and connects to other machines. What changes is the packaging. This section is a field guide to the machines this course mentions, so every later chapter can name a device and move on.

### Computers in Your Bag

The most powerful computer most people own is the **smartphone**, a pocket computer with more processing power than the machines that flew the Apollo missions. Its main limits are screen size and typing speed, which is why longer work moves to bigger devices.

A **tablet** trades the phone's pocket size for a larger touchscreen. A **laptop** folds a full keyboard, screen, and battery into one portable case, and it is the standard machine for producing documents, worksheets, and presentations. A **desktop** gives up portability for power, more ports, and easy repairs, which keeps it common in offices, labs, and gaming setups.

Which one is best? Wrong question, and this course will train you out of asking it. The right question is: best for which task? Typing a ten-page report on a phone is misery. Carrying a desktop to class is comedy. Matching the machine to the task is a skill, and Chapter 6 turns it into a checklist you can defend.

### The AI PC and Its New Chip

Laptop ads now lean on a new label: the **AI PC**. The name marks a real change in the hardware. A conventional computer already has a processor to run your programs and a graphics chip to draw the screen. An AI PC adds a third worker, the **NPU** (neural processing unit), a chip built specifically for running AI features directly on the device.

Why put AI on the device instead of on the Internet? Speed and privacy. A live captioning feature or a background-blur effect works faster when no round trip to a distant server is needed, and your data never leaves the machine. Chapter 5 opens the case and looks at all three chips properly. For now, when you see "AI PC," read "a computer with a chip dedicated to AI work."

### Computers You Never See

Your phone and laptop are only the visible half of modern computing. The other half lives in buildings you will never visit.

A **server** is a computer that provides data or services to other computers over a network. When you stream a show, check your grades, or place that coffee order, a server somewhere does the heavy lifting. Servers live by the thousands in data centers, which are warehouse-sized buildings full of racks, cooling, and backup power.

**Cloud computing** means using computing services, such as storage, software, and processing power, delivered over the Internet from those data centers. When your photos "back up to the cloud," they are copied to a company's servers. The cloud is not weather. It is somebody else's computer, professionally run, and this course treats it that way: useful, powerful, and worth understanding before you trust it.

At the far end of the scale sit machines almost nobody meets in person. Supercomputers fill rooms and model weather, proteins, and the training runs behind modern AI. Mainframe-class systems still process the world's card payments and insurance claims by the billions, decades after headlines declared them dead. You will not use one in this course, but your money moves through them weekly, so they belong on the map.

Two more machine families round out the field guide. A **wearable** is a small computer worn on the body, such as a smartwatch or a fitness band, that gathers data all day. The **Internet of Things** (IoT) is the growing crowd of everyday objects, such as doorbells, thermostats, and delivery trucks, fitted with sensors and network connections so they can send data over the Internet. A modern business is ringed with these quiet little computers, and Chapter 7 shows how they all connect.

Notice what wearables and IoT devices have in common: they are data factories. A smartwatch takes thousands of readings a day. A shop's smart thermostat logs every degree. None of it means anything until software organizes it into information a person can act on, which is the same data-to-information move you met in Section 1.1, running constantly and everywhere.

### One Order, Many Machines

Now chain the field guide together and watch how many machines touched your one coffee order:

1. Your **smartphone** ran the app and took the tap.
2. The order crossed the Internet (Chapter 2 traces the route) to a **server** in a data center, which recorded the sale, charged the payment, and logged the loyalty point.
3. The server pushed the order back down to the shop's register, a touchscreen **tablet** behind the counter.
4. The barista's **wearable** buzzed with the alert, and the shop's **IoT** thermostat kept the espresso bar at temperature the whole time.

Five machine categories, one small purchase, about two seconds. Nobody in the shop thinks about this chain until it breaks, and then the six-questions habit from Section 1.1 tells you exactly where to look. When a machine in the chain is yours to choose, Part II of this book gives you the checklist.

| Machine | Its strength | A task it fits |
| ------- | ------------ | -------------- |
| Smartphone | Always with you | Placing the coffee order |
| Tablet | Big touchscreen, light | Signing a delivery on a clipboard app |
| Laptop | Full keyboard, portable | Writing this chapter's Skills Lab letter |
| Desktop | Power, ports, easy upgrades | Editing the shop's promo video |
| Server | Serves thousands at once | Running the ordering system's back end |
| Wearable | Gathers data hands-free | Counting a nurse's steps on shift |
| IoT device | Senses and reports | The shop's smart thermostat |

### Try It Yourself 1.2: Meet Your Own Machine 🛠️

**Predict:** Your phone or laptop has an "About" screen that describes its own hardware. Before you look, write down two numbers you expect to find there and what you think each one measures.

**Run:** Open Settings and find the About page (About phone, or About this Mac, or System > About on Windows). Read the entries for processor or chip, memory, and storage.

**Explain:** In 1-2 sentences, state which number you predicted correctly and which entry surprised you. Keep this page in mind: Chapter 5 teaches you to read every line of it.

### Try It Yourself 1.3: Count Your Computers 🛠️

**Predict:** Using this section's field guide, write down how many computers you think you own or live with, counting wearables and IoT devices. Most people guess low. Write your number before counting.

**Run:** Now count for real. Phones, tablets, laptops, and consoles are the easy ones. Then hunt the quiet ones: watches, TVs, smart speakers, doorbells, thermostats, even a newer car. Anything that runs software and connects counts.

**Explain:** In 1-2 sentences, compare your prediction to your count and explain which category hid the most machines from your first guess.

### Quick Check 1.2 ✅

1. A nurse checks a patient's vitals on a wall-mounted tablet, and the readings appear instantly in a doctor's office across town. Name the machine categories involved and the part of the six-part system that linked them.
2. Explain the difference between a server and your laptop in one sentence about who each machine serves.
3. A bakery owner asks whether "moving to the cloud" means her sales records stop existing on any computer. Correct the misunderstanding in one sentence.

---

## 1.3 Software, Files, and the AI Moving In

Hardware is useless until software gives it instructions. This section sorts software into its two layers, introduces the four kinds of files you will produce this term, and previews the newest arrival inside everyday programs: the AI assistant.

### The Two Layers of Software

All software falls into two layers, and telling them apart is a course outcome you will use in every remaining chapter.

**System software** runs the computer itself. Its central piece is the **operating system** (OS), the program that starts the machine, manages its hardware, and launches everything else. Windows, macOS, iOS, and Android are operating systems. You rarely open the OS on purpose, but nothing runs without it. Two smaller system-software families ride along. A **utility** is a housekeeping program that backs up files, cleans storage, or guards against malware. A **device driver** is a small program that teaches the OS to talk to a specific printer, camera, or mouse. Chapter 4 gives the whole layer a chapter of its own.

**Application software** does your tasks. Word, Excel, PowerPoint, a browser, and the Desert Bloom ordering app are all applications. On phones we shorten the word to **app**, and the nickname has spread to every screen.

Here is the one-question test that sorts any program: does it serve the computer, or does it serve you? A file backup utility serves the machine. A slideshow about cactus care serves you.

| Layer | Serves | Examples |
| ----- | ------ | -------- |
| System software | The computer | Windows, macOS, iOS, Android, utilities |
| Application software | You and your tasks | Word, Excel, PowerPoint, browsers, the ordering app |

### Four Files You Will Produce

Applications produce files, and four file families carry most of the working world's output. You will produce all four in this course.

* **Documents** hold formatted text: letters, memos, reports, and flyers. Word processors such as Word create them. Maya's announcement letter is one, and you will produce it this week.
* **Worksheets** hold numbers in a grid of rows and columns, plus the formulas and charts that make the numbers talk. Spreadsheet programs such as Excel create them. Desert Bloom's monthly sales summary lives in one, and they arrive in Chapter 6.
* **Presentations** hold slides that support a talk: the shop's staff-training deck, a pitch to investors, a class project. PowerPoint owns this family, and you will build decks in Chapters 4 and 5.
* **Databases** hold organized collections of related data, built for searching and connecting records. The Bloom Ahead app's customer accounts and order history sit in one. This course builds databases in Airtable, a database tool that runs in your browser, in Chapters 10 and 11.

One detail before the extension list: Airtable bases live in the cloud instead of in files on your machine, so no Airtable extension appears below. Cloud tools trade the file for a login, a difference Chapter 10 examines up close.

Files announce their family in their names. A **file extension** is the short code after the dot in a file name that tells the computer (and you) what kind of file it is:

```text
announcement-letter.docx    Word document
fall-sales.xlsx             Excel workbook of worksheets
staff-training.pptx         PowerPoint presentation
customer-orders.csv         plain table of comma-separated values
```

One habit now, gratitude later: give files descriptive names. Six months from now, `draft2-final-FINAL.docx` tells you nothing. `bloom-ahead-launch-letter.docx` tells you everything.

### AI Assistants Move In

The biggest software story of this decade is not a new program. It is a new passenger inside the old ones. An **AI assistant** is software that responds to plain-language requests: it can draft text, summarize a document, suggest a formula, or answer a question in full sentences. The request you type or speak to it is called a **prompt**.

Two terms behind the label are worth learning now. **Artificial intelligence** (AI) is the broad family of techniques that let software perform tasks that normally require human judgment, such as recognizing a face or drafting a paragraph. **Generative AI** is the branch that creates new content, including text, images, and audio, in response to prompts. The assistant built into Word is generative AI with a friendly name. So are the chatbots you have likely met in a browser.

Here is what this course asks of you, starting now: treat an AI assistant like a fast, confident, occasionally wrong intern. It drafts in seconds. It never signs its work. When it summarizes a document, the summary can miss the point. When it answers a question, the answer can be flatly false while sounding sure of itself. The people in the system, Section 1.1's first and leading part, still own judgment, verification, and trust. Every Skills Lab in this book keeps those jobs in your hands.

A fair split of the labor looks like this:

* **Assistants are strong at** first drafts, summaries of long text, reformatting, suggesting formulas or phrasings, and explaining an unfamiliar term at 2 a.m. when no colleague is awake.
* **Assistants are weak at** knowing your situation, catching their own errors, telling truth from confident fiction, and taking responsibility. The signature line is yours.

### Changing Work, Not Ending It

You will hear two loud stories about AI and work. One says every job is about to vanish. The other says nothing will change. The evidence so far supports neither, and this book takes the working professional's view: tasks are shifting inside jobs, and the shift rewards people who can direct, check, and correct the tools.

!!! note
    "AI" in this book means the assistants, answer engines, and coding tools you can use today, not science-fiction machines with goals of their own. The tools are impressive and limited at the same time. Both halves of that sentence matter.

Look at how that plays out around one small shop. Maya at Desert Bloom no longer types her weekly sales summary. Register software drafts it, and her job moved up a level: reading it critically, spotting the numbers that look wrong, and deciding what to reorder. Her bookkeeper spends less time entering receipts and more time catching the categorization mistakes automated tools make. The agency that built her app uses AI coding assistants to draft routine code, and its developers now spend more of their day reviewing and testing. In each case the tool absorbed the repetitive layer of the work, and the human layer, the part that requires knowing the business, grew more valuable, not less.

That pattern is why this course exists in its current form. Every chapter hands you a tool's output and asks you to judge it, because judging output is becoming the job. You will polish a drafted letter in this chapter's lab, fact-check AI claims in Chapter 2, and read machine-written macro code in Chapter 12. All three are the same exercise wearing different clothes.

The six parts from Section 1.1 are also this book's table of contents in disguise. Here is the roadmap for the whole term:

| Part of this book | System parts it covers | You will work in |
| ----------------- | ---------------------- | ---------------- |
| Part I (Ch 1-3) | The whole system, people first | Word |
| Part II (Ch 4-6) | Software layers and hardware | PowerPoint, Excel |
| Part III (Ch 7-8) | Connectivity, and the risks that ride on it | Excel |
| Part IV (Ch 9-12) | Data becoming decisions, work becoming automation | Excel, Airtable, VBA |

Three threads run through all four parts: cloud computing, the Internet of Things, and the AI tools this section introduced. Each later chapter picks the threads up where they belong. By the last chapter you will record a macro, read the code it generates, and decide whether to trust it. That is the six-part habit, applied to code.

!!! tip "Tech in Your Field"
    The six-part system is already your field's daily equipment. Nursing students will chart in electronic health records, where a wrong entry travels at connection speed and verification habits protect patients. Business and entrepreneurship students will run shops on point-of-sale data like Desert Bloom's, deciding which AI-generated sales summary to trust before ordering inventory. Visual and performing arts students will publish through platforms whose software decides who sees their work, and knowing the system behind the feed is a career skill. Public safety students will file reports into databases that dispatchers and courts rely on. In every one of these rooms, the role is changing, not disappearing, and the judgment stays with the person who can name the parts.

### Try It Yourself 1.4: Name That File 🛠️

**Predict:** A coworker sends you four files: `menu-refresh.docx`, `tip-share.xlsx`, `open-mic-night.pptx`, and `loyalty-signups.csv`. Before opening anything, write down which program opens each one and which of the four file families it belongs to.

**Run:** Check your predictions against the extension list in this section. Then look at five files you already have (Downloads is a good hunting ground) and identify each one's family.

**Explain:** In 1-2 sentences, explain how extensions let you plan work you have not opened yet. Which of your own five files was hardest to classify, and why?

### Try It Yourself 1.5: Quiz the Machine 🛠️

**Predict:** Think of a topic you know deeply: your neighborhood, your job, a hobby, a team. If an AI answer summarized that topic in one paragraph, do you expect it to be fully right, mostly right with something off, or wrong in some clear way? Write down your call.

**Run:** Search the topic in any search engine. If an AI-generated answer box appears at the top, read it slowly and check every claim against what you know. No AI answer? Pick the top regular result and check it the same way. No account or paid tool is needed.

**Explain:** In 1-2 sentences, report what you found and why a confident tone is not evidence. You just did professional verification. Chapter 2 sharpens it into a method.

### Quick Check 1.3 ✅

1. Classify each of the following as system software or application software, and defend one answer: Android, Excel, a disk cleanup utility, the Desert Bloom ordering app.
2. The shop owner wants to track which pastries sell out by weekday and see it as a chart. Which file family fits, and which program from this course creates it?
3. An AI assistant inside Word offers to draft a refund policy for the shop. Name two of the three human jobs from Section 1.1 that still apply before that policy goes on the wall, and say what each one looks like here.

---

## 1.4 From Data to Document: Your First Business Letter

Every field in this book still runs on documents. Offers arrive as letters. Projects start as proposals. Decisions get recorded in memos, and the person who can produce a clean, professional document quickly is valuable in every office. This section gives you the working tour of Word that Skills Lab 1A builds on.

### A Quick Tour of Word

Open Word and start a blank document. Almost everything you need lives on the **ribbon**, the strip of tabs and buttons across the top of the window. Each tab groups related tools:

* **Home** holds the everyday tools: font, size, bold, alignment, spacing, and Find and Replace.
* **Insert** adds things to the document: page breaks, tables, pictures, and today's date.
* **Layout** controls the page itself: margins, orientation, and columns.
* **Review** holds **Editor**, Word's built-in spelling and grammar checker, which marks suspected errors as you type.

Word saves files in the `.docx` format you met in Section 1.3. When Word is signed in to a Microsoft 365 account, AutoSave can store the file in the cloud and save every change as you make it. Wherever you save, the rule is the same: name the file descriptively the first time.

One more landmark: the File tab at the far left is different from the others. Instead of tools, it opens the document's business office: New, Open, Save As, Export, and Print all live there. Every lab in this course ends with a trip to the File tab, so learn the route early.

The tour ends where every work session should begin: saving. Professionals lose less work than students, and the difference is habits, not luck. Three of them cost nothing:

1. **Save before you start working, not after.** The moment you paste content into a new document, save it with its final, descriptive name. An unsaved document with an hour of edits is a bet against every power cord in the building.
2. **One task, one folder.** Keep each project's files together, next to the materials they came from. The course data pack already models this: every chapter's files live in their own `assets/code/chapter-NN` folder, and your lab work saves right alongside them at the extracted `cis105` root.
3. **Name for your future self.** A good file name states the project and the content, in lowercase, with hyphens instead of spaces: `bloom-ahead-launch-letter.docx`. Version numbers beat adjectives. `letter-v2.docx` means something. `letter-final-REAL.docx` is a confession.

AutoSave changes the rhythm but not the responsibility. With AutoSave on, Word saves continuously to the cloud, and Version History (under the file name in the title bar) lets you step back to earlier versions. With AutoSave off, ++ctrl+s++ (Windows) or ++cmd+s++ (Mac) after every meaningful change is the oldest habit in computing, and it still works.

### The Shape of a Business Letter

A business letter is a formatted document with a job: deliver news from an organization to a reader, clearly, on one page if possible. The standard block style puts every element flush against the left margin, with a blank line between elements:

```text
[Letterhead: business name and address]
[Date]

[Greeting],

[Body paragraphs: the news, then the details, then the thanks]

[Closing],
[Name]
[Title, business name]
```

The format is not decoration. A reader who gets fifty letters a year knows exactly where to look for the date, the point, and the sender. Meeting that expectation is a courtesy, and breaking it costs you attention.

Word ships templates for letters, and using one later is no sin. The lab has you build the format from a blank page once, on purpose. A template user who knows the bones can fix a template. A template user who does not is stuck with whatever the template guessed.

Formatting carries meaning inside the body too. Bold pulls the eye to what matters most, such as a launch date. Consistent spacing signals care. A letter in three fonts signals the opposite. In the lab you will make these choices deliberately and defend them.

### Select, Then Act

Nearly every formatting move in Word follows one two-step rhythm: select the text first, then apply the change. Nothing selected means Word does not know what you are talking about. Once the rhythm is in your hands, the ribbon stops being a wall of buttons and becomes a menu of actions waiting for a target.

Here is the rhythm applied to a letter, in the order professionals work:

1. Select all the text (++ctrl+a++ or ++cmd+a++) and set the font and size once. One pass, one consistent document.
2. Select all again and set the paragraph spacing (Home > Line and Paragraph Spacing). Structure before decoration.
3. Select only the letterhead line and enlarge it. Now the exception stands out against a consistent background.
4. Select individual phrases last, and bold only what the reader must not miss.

Work in that order and you never fight yourself. Decorate first and every later change undoes something you already did. The same whole-document-first principle returns in Chapter 3, where Word's styles turn it into automation.

### Try It Yourself 1.6: Rebuild the Skeleton 🛠️

**Predict:** Without looking back at the skeleton in the previous subsection, write down the block-letter elements you remember, in order. Which element do you suspect you have forgotten or misplaced?

**Run:** Open a blank Word document and lay out the skeleton from your memory list, one placeholder line per element. Then compare against the skeleton in this chapter and fix the differences.

**Explain:** In 1-2 sentences, name what you missed or misordered and why that element matters to the reader. Retrieval like this is how the format becomes yours before the lab.

### Deliver Clean

Editing is where a draft becomes a document, and Word gives you three tools for the job.

**Find and Replace** (press ++ctrl+h++ on Windows, or use Edit > Find > Replace on a Mac) changes every occurrence of a phrase at once. When a business renames a product, one Replace All beats fifty careful re-readings, and it never misses one.

**Editor** (on the Review tab) flags spelling and grammar problems and suggests fixes. Run it on everything you write. Then, and this is the professional habit, read the text once aloud anyway. Editor catches words spelled wrong. It is far weaker against words spelled correctly but used wrongly, and a letter that confuses "exited" with "excited" ships embarrassment at connection speed.

When the letter is final, deliver a **PDF**, a file format that locks your layout so the document looks the same on every device. Use File > Save As (or File > Export) and choose PDF. Send the PDF, keep the `.docx`: the PDF is for readers, the Word file is for the next edit.

```text
skills-lab-1a-vega.docx    the editable original (yours)
skills-lab-1a-vega.pdf     the locked copy (the reader's)
```

Before anything leaves your hands, run the same short inspection professionals run on every outgoing document. Borrow it whole:

* Names spelled correctly, starting with the recipient's. A misspelled name loses the reader in the first line.
* The date is current and the placeholder text is gone. Search for `[` to catch forgotten placeholders fast.
* One font family, one size for body text, emphasis used once or twice at most.
* Editor has run, and you have read the text aloud once for the errors Editor cannot see.
* The file name is descriptive and professional, because the reader sees it in the email attachment line.
* The version you send is the format the reader needs, usually PDF.

Six lines of checking cost about two minutes. A public mistake costs more, and unlike the AI assistant from Section 1.3, you sign your work.

### Try It Yourself 1.7: Catch What the Checker Misses 🛠️

**Predict:** You type this sentence into Word: "Their going to love the new app." Will Editor flag it? If so, what will it object to, and what will it suggest?

**Run:** Open a blank Word document, type the sentence exactly, and open Editor from the Review tab. Read what it flags and what it proposes. Delete the practice text afterward.

**Explain:** In 1-2 sentences, explain what this tells you about the division of labor between Editor and you. Which of the two catches meaning?

### Quick Check 1.4 ✅

1. List the block-style letter elements in order from the top of the page to the bottom.
2. You need to change "Grand Ave" to "Grand Avenue" in 23 places in a long letter. Name the tool, the tab or shortcut that opens it, and the reason it beats manual editing.
3. Why does the customer get the PDF while you keep the `.docx`? Answer in one sentence about what each format is for.

---

## 1.5 Summary and Retrieval 💡

### Key Concepts

* An information system is six parts working together: people, procedures, software, hardware, data, and connectivity. People come first because judgment, verification, and trust decisions stay human even as AI spreads through the other five parts.
* The six parts double as a troubleshooting tool: when a system misbehaves, walk the parts in order and ask what each would look like as the cause. One symptom can have six different fixes.
* Data is raw facts. Information is data organized until it can support a decision. Turning one into the other is the core business use of every technology in this book.
* Computers differ by packaging, not by recipe: smartphones, tablets, laptops, and desktops in your bag, plus servers, wearables, and IoT devices out of sight. AI PCs add an NPU, a chip dedicated to running AI features on the device. The cloud is professionally run servers reached over the Internet.
* Software has two layers. System software (led by the operating system) runs the computer. Application software does your tasks and produces four file families: documents, worksheets, presentations, and databases. File extensions announce the family.
* AI assistants are generative AI built into everyday programs. They draft fast and verify nothing, so the human jobs from Section 1.1 apply to every answer they produce.
* A business letter in block style, edited with Find and Replace plus Editor, read once aloud, and delivered as a PDF, is a complete professional workflow you now own.

### Key Terms

See course glossary for full definitions

* information system, end user, procedures, software, hardware, data, information, connectivity (Section 1.1)
* smartphone, tablet, laptop, desktop, AI PC, NPU, server, cloud computing, wearable, Internet of Things (Section 1.2)
* system software, operating system, utility, device driver, application software, app, document, worksheet, presentation, database, file extension, AI assistant, prompt, artificial intelligence, generative AI (Section 1.3)
* ribbon, Find and Replace, Editor, PDF (Section 1.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. List the six parts of an information system and give each one a five-word job description.
2. Explain the difference between data and information using an example from a job you have held or want.
3. A neighbor is laptop shopping and asks what makes something an "AI PC." Give the one-sentence answer.
4. Sort these into system or application software from memory: macOS, PowerPoint, a browser, a disk cleanup utility, Android.
5. Recite the block-style letter elements in order, then name the editing step that catches errors Editor cannot.

---

## 1.6 Skills Lab 1A: From Blank Page to Business Letter

**Goal:** Take Desert Bloom Coffee's rough announcement draft from a blank page to a polished, formatted business letter, delivered as a PDF the owner could mail tomorrow.

**Dataset or starter files:** Provided files in `assets/code/chapter-01/` from the course data pack. `letter-content.docx` is the owner's unformatted draft, editing problems included on purpose. `app-fact-sheet.docx` is the staff fact sheet for the new Bloom Ahead ordering app. Download the data pack from Canvas, extract it, and work at the extracted `cis105` root. You will copy the provided text, never retype it.

**Scenario:** Maya Reyes owns Desert Bloom Coffee, the Phoenix shop from this chapter. Her new mobile ordering app, Bloom Ahead, launches October 5, and she has drafted a letter to her regular customers. The draft has the right heart and the wrong everything else. She has asked you to make it professional.

### Part 1: Foundation (Aligns with MLO-1.3)

1. Open `letter-content.docx` from the data pack. Select all of its text (++ctrl+a++ on Windows, ++cmd+a++ on Mac) and copy it.
2. Create a new blank Word document and paste the text in. This blank document becomes your letter. Save it now as `skills-lab-1a-lastname.docx`, using your own last name.
3. Build the letterhead at the top: the shop name on its own line, then the address line from the top of the fact sheet. Make the shop name larger and bold so it reads as a letterhead.
4. Replace the `[Today's Date]` placeholder with the date you are working. Insert > Date & Time places it for you, or type it in a formal format.
5. Set the whole letter in one clean, professional font (Aptos and Calibri both work) at 11 or 12 point, flush left in block style, with a blank line between elements. Compare your structure against the skeleton in Section 1.4.

### Part 2: Application (Aligns with MLO-1.3)

1. The shop's registered name is "Desert Bloom Coffee," but the draft slips into an older name in places. Use Find and Replace to change every "Desert Bloom Cafe" to "Desert Bloom Coffee." Use Replace All, and record how many replacements Word reports (you will need the number for your Questions & Analysis answers).
2. Run Editor from the Review tab and fix every spelling error it finds. The draft ships with three.
3. Now read the letter aloud once, slowly. One word in the draft is spelled correctly but wrong for its sentence. Find it and fix it, and note whether Editor had flagged it for you.
4. Make two deliberate emphasis choices: bold the app name and the launch date (and nothing else). Then set line spacing so the letter breathes: 1.15 spacing with space after paragraphs reads well on screen and paper.

### Part 3: Extension (Aligns with MLO-1.1, MLO-1.2)

1. Open `app-fact-sheet.docx` and read all twelve facts. The fact sheet was written for staff, not customers.
2. The draft contains a placeholder paragraph marked `[HOW IT WORKS...]`. Replace it with a short section of your own: 3-4 sentences in plain customer language explaining how Bloom Ahead works, built from at least three facts you select from the sheet. Translate, do not copy: "iOS 16 or later" is a staff fact, "works on most phones" is customer language.
3. Your new section must mention, in everyday words, at least three of the six system parts from Section 1.1 (for example: the phone, the app, the Internet connection, the baristas). No need to name them technically. The reader should simply see the system working.
4. Proofread your added section with the full Part 2 toolkit: Editor, then one read-aloud pass.
5. Export the finished letter as a PDF named `skills-lab-1a-lastname.pdf` using File > Save As or File > Export. This PDF is the deliverable Maya would put in the mail.

### Questions & Analysis 🤔

Add a page break at the end of your Word document (Insert > Page Break), add the heading "Questions & Analysis," and answer both questions there. These answers carry significant rubric weight. The PDF you exported in Part 3 should NOT include this page, so export before you add it, or export again without it.

1. Map the Bloom Ahead ordering flow onto all six parts of an information system, citing at least four specific details from the fact sheet as evidence. Which part do customers notice least, and why does the letter still depend on it?
2. Maya could have asked an AI assistant to draft and polish this letter in seconds. Using two specific fixes you made in Part 2 or Part 3, explain what your judgment added that a fast draft could not guarantee. Include the Replace All count from Part 2 in one of your examples.

**Submission:** Submit two files: your Word document `skills-lab-1a-lastname.docx` (letter plus your labeled Questions & Analysis page) and the exported `skills-lab-1a-lastname.pdf` (letter only). Both files use your own last name.

### Rubric: Skills Lab 1A

Every Skills Lab in this book is graded with the same 16-point rubric.
Bookmark the [Skills Lab Rubric](../skills-lab-rubric.md) page for
quick reference in later chapters.

--8<-- "skills-lab-rubric.md:rubric"

---

## 1.7 Review Questions 🔄️

1. **Remember:** List the six parts of an information system and pair each with one example from this chapter that is not the coffee shop.

2. **Understand:** A food truck logs every sale on a tablet register. Explain, in 2-3 sentences, how that raw sales data could become information that changes what the truck stocks next week.

3. **Apply:** The truck's owner asks you to recommend a setup for three tasks: taking payments at the window, writing a one-page supplier agreement, and tracking daily sales totals for the month. For each task, name the device type, the software layer or program, and the file family involved.

4. **Analyze:** A headline claims a new AI assistant will "replace office workers." Break one office task you know into its six system parts, then identify which parts the assistant can genuinely take over and which parts stay with people. Support your split with the three human jobs from Section 1.1.

---

## Further Reading 📖

* [GCFGlobal: Computer Basics](https://edu.gcfglobal.org/en/computerbasics/) - Free, plain-language tutorials on hardware, software, and operating systems, with short videos matched to this chapter's depth.
* [GCFGlobal: Word](https://edu.gcfglobal.org/en/word/) - A free tutorial series on Word's ribbon, formatting, and editing tools, useful alongside Skills Lab 1A.
* [Microsoft Support: Word help and learning](https://support.microsoft.com/en-us/word) - The official reference for the current Word, including step-by-step pages for every tool the lab uses.
* [Pew Research Center: Internet and Technology](https://www.pewresearch.org/internet/) - Ongoing survey research on how Americans use technology, a source of the kind of information (not just data) this chapter defines.
* [Elements of AI](https://www.elementsofai.com/) - A free online introduction to what AI can and cannot do, built by the University of Helsinki for readers without a technical background.

---

## Looking Ahead ⏩

You can now name the six parts behind any app, and you have shipped your first professional document. Chapter 2 follows the connectivity part out of the building. You will see how the Internet grew, what happens when you type a web address, and how to verify what search engines and AI answer engines hand back. The letter you polished this week becomes a research memo next, and the verification habit you started in Try It Yourself 1.5 becomes a method.
