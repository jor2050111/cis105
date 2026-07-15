# Chapter 12: Automate Your Work: Macros, VBA, and AI Coding Assistants

On the first business day of November, Renee Salazar sat down to a ritual. Saguaro Hall's booking base, the one you built in Chapter 10 and tracked to rollout in Chapter 11, had just finished October, its first full month running solo. Renee opened the export view and downloaded the month's 63 bookings to Excel. Then came the same routine she performs every month: bold the header row, widen the columns, format the prices as currency, freeze the top row. Twenty minutes of identical clicks, in the same order, on a file that changes but a routine that never does. Somewhere around the fourth click she asked the question this chapter exists to answer. If the steps never change, why is a person doing them?

That question is programming's front door. A computer is a machine built to follow instructions, and until now you have delivered every instruction by hand, one click at a time. This chapter shows you how to hand the computer the whole list. You will not become a software developer in one chapter, and you do not need to. You need the 2026 version of computer fluency: the ability to automate a repetitive task, read the code that automation produces, and judge whether to trust it. Every major in this room has a version of Renee's ritual waiting for it.

There is one more reason this chapter closes the book. Renee also asked an AI assistant to help, and it wrote her a working macro in seconds. That macro runs without a single error message, and it hands Darnell a wrong number for October. The last skill this course teaches is the one Chapter 1 promised: the tools now draft, build, and automate, and the judgment about whether to trust what they produce stays with you. By the end of the Skills Lab, you will have recorded your first macro, read the code it wrote, and caught the AI draft's quiet mistake before it reached the boss.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero), builds on the Excel thread of Chapters 6-9, the Saguaro Hall project of Chapters 10-11, and Chapter 2's look inside a web page
* **Deliverables:** Skills Lab 12A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **12.1 (Understand):** Outline the path a program takes from a named need to tested, documented code, using pseudocode and the three logic structures (Section 12.1)
* **12.2 (Analyze):** Differentiate syntax errors from logic errors in code you did not write (Sections 12.1 and 12.4)
* **12.3 (Create):** Create working Excel macros by recording, reading, editing, and repairing VBA in the Visual Basic Editor (Sections 12.3 and 12.4, Skills Lab 12A)

### This chapter aligns with the following Course Learning Outcomes

* **CLO VII (Create):** Create macros and explain the basics of Visual Basic for Applications (VBA)
* **CLO IV (Understand):** Describe the technologies behind websites, including browsers, HTML, and web servers
* **CLO IX (Evaluate):** Evaluate tasks and problems to select the technology tools and resources that fit
* **CLO XIII (Apply):** Produce documents, spreadsheets, databases, and presentations with industry-standard productivity software

---

## 12.1 From Ritual to Recipe: What a Program Is

A **program** is a set of instructions a computer follows to do a task. That is the whole definition. Chapter 1 told you software is programs, and every app you have used this term, from Word to Airtable, is instructions someone wrote. What is new today is who writes them. This section shows you the shape all programs share, because you are about to write one.

Renee's ritual is already almost a program. She performs the same steps, in the same order, on every month's export. Chapter 2 gave you the word for that: an algorithm, a step-by-step procedure software follows. The only difference between her ritual and a program is the audience. A ritual runs on a person's patience. A program runs on a machine, and machines need the steps spelled out exactly.

### Six Steps, Desk-Sized

Chapter 11 walked you through the six phases that carry a whole system from complaint to rollout. A single program travels the same loop at desk scale, and professionals give its stops similar names.

* **Say what it must do.** One sentence, before any code: "Format the monthly export and total the quoted revenue." Vague goals produce vague programs.
* **Sketch the logic.** Plan the steps in plain language first (the design tools below).
* **Write the code.** Type it, record it, or have an assistant draft it. In 2026 this is the fastest step, which is exactly why the others matter more.
* **Test it.** Run the code against data where you already know the right answer, and watch the edges.
* **Write it down.** Add comments saying WHY, so a colleague, or you in March, can read and build on it.
* **Keep it alive.** Data grows and needs shift. A program is maintained, or it quietly rots, like any system from Chapter 11.

Notice what this list does to the panic most people feel about "coding." Writing code is one step of six, and the other five are thinking skills you have practiced all term: naming problems, planning, testing against evidence, documenting decisions.

### Sketching Logic: Pseudocode and Flowcharts

Programmers sketch before they build, the way Chapter 11's design phase drew blueprints before configuration. **Pseudocode** is a plain-language draft of a program's steps, written for humans, with no grammar rules to trip on. A **flowchart** is the same plan drawn as a diagram, with boxes for actions and diamonds for decisions, so the paths through the logic are visible. Here is pseudocode for a check Saguaro Hall might run on any export:

```text
FOR each booking row in the export
    IF the Guest Count is larger than the space's capacity
        mark the row "over capacity"
    OTHERWISE
        leave the row alone
END FOR
```

Every program ever written, from this sketch to the largest app on your phone, arranges its steps using just three patterns, called **logic structures**. Sequence runs steps in order, one after the next. Selection chooses between paths based on a test (the IF above). Repetition repeats steps until a condition says stop (the FOR above, which repeats once per row). Three patterns, combined and nested, are the entire vocabulary. When Section 12.3 shows you real code, you will already know its grammar.

### Two Ways to Be Wrong

Testing is where programs earn trust, and Chapter 11 promised this chapter would draw a sharp line between a system that runs and a system that is right. Here is the line. A **syntax error** breaks the language's grammar rules, and the program will not run at all. You get a loud complaint, usually pointing near the problem, and nothing happens until you fix it. A **logic error** breaks no grammar rules. The program runs to the end, looks finished, and produces a wrong answer. Nothing complains. Nothing turns red. The wrongness just sits there in a cell, waiting to be believed.

Here is why the quiet kind is the dangerous kind. A crash interrupts you, so it gets fixed on the spot. A wrong answer interrupts nobody, so it can survive, unquestioned, and ride into a decision: a misquoted price, a short revenue total, a flag that never got raised. **Debugging** is the craft of finding and fixing both kinds. Its first tool is the one Chapter 9 taught you at the pivot table: know what the answer should be before you look at what the answer is. You will use exactly that tool on an AI's code in the Skills Lab.

### Try It Yourself 12.1: Trace the Recipe 🛠️

**Predict:** Open `booking-export.xlsx` from the data pack (any Excel can open it, even in the browser: only the macro work later needs the desktop app). Read the over-capacity pseudocode above against the venue's limits: Main Hall holds 300, Courtyard 150, Meeting Room 40. Before checking any rows, predict in writing how many of October's 63 bookings the sketch would flag.

**Run:** Trace the logic by hand against three cases, so both paths of the selection get exercised. Use `SH-1071` (Main Hall, 210 guests), `SH-1085` (Courtyard, 130 guests), and one booking October never took: a hypothetical 175 guests in the Courtyard. Then scan the Guest Count column against each row's space.

**Explain:** In 1-2 sentences, state how many rows the program would flag and whether a result of "nothing flagged" means the program failed or succeeded. (Chapter 11 said the same thing about audits that find nothing.)

### Quick Check 12.1 ✅

1. Name the six desk-scale steps that carry a program from a named need to code someone can maintain, in order.
2. A macro runs to completion and reports a total. A week later the total turns out to be wrong. Which kind of error is this, and why did no message appear?
3. Identify the logic structures in the over-capacity pseudocode: where is the repetition, and where is the selection?

---

## 12.2 From Switches to Sentences: How Code Reached the Prompt

You are about to read and edit real code, so it helps to know what code is underneath, and why today you can almost write it in English. The story is one long climb toward human language, and you are living at the top of it.

### What the Processor Understands

Chapter 5 introduced the CPU as the part that executes instructions. Here is its native tongue. **Machine language** is the processor's own instruction set, written as patterns of ones and zeros. One real instruction from the most common laptop processor family looks like this:

```text
10110000 01100001
```

That pattern tells the chip to move one value into one storage slot. Every program you have ever run, Word, Excel, the browser, ends up as millions of patterns like it, because ones and zeros are all the hardware can execute. Nobody wants to write at that altitude, and early programmers had no choice.

The climb out happened in two great steps. First came **assembly language**, which swapped the raw patterns for short human-readable abbreviations that map closely onto the processor's own instructions. Better, but still one line of code per tiny step. Then came the languages most software is written in today, called high-level languages, where one readable line can stand for hundreds of machine instructions. A **programming language** is any of these formal languages for writing instructions, each with a strict grammar (now you know why syntax errors are a thing). Python and JavaScript are the household names of this altitude, and the VBA you will meet in the next section lives there too. Because the processor still speaks only machine language, high-level code gets translated down, in two classic strategies: a **compiler** translates a program before it runs, and an **interpreter** translates it while it runs. Modern languages usually blend the two, and the blend is invisible to you. What matters is that the translation always happens, and the destination is always the same ones and zeros.

### Code Is Already in Your Apps

Here is the part of the story that touches your daily life. Code does not only live in standalone programs. It rides inside the documents and pages you already use, and you have been inches from it all term.

Remember Chapter 2, where you viewed a web page's source and found HTML holding the page's structure? HTML is labels, not logic: it cannot decide, repeat, or calculate. When a page needs behavior, it carries a **scripting language**, code embedded inside a host so the host can run it. On the web that language is **JavaScript**, and the browser executes it the moment the page loads:

```html
<script>
  // The browser runs this script as it builds the page.
  alert("Welcome to Saguaro Hall!");
</script>
```

The `<script>` tag is HTML's way of saying "code lives here." That is web scripting: the browser is an app that runs code shipped inside pages, which is how a page can respond, update, and misbehave. (JavaScript long ago escaped the browser and runs on servers too, but the browser is where you will meet it first.) Chapter 4 promised you would see code driving an app again, and Excel keeps the same arrangement. Its embedded language is VBA, and a workbook can carry code the way a page carries a script. Same pattern, different host, and it is the pattern the whole next section stands on.

### The Newest Altitude: The Prompt

The climb's newest step arrived in your lifetime. Chapter 1 defined the prompt: a plain-language request to an AI assistant. Ask one to "write an Excel macro that totals column J," and it will draft working VBA in seconds. It is tempting to call English the newest programming language, and the industry half-jokes exactly that. Hold on to the half that is a joke.

A prompt is not a program. When Renee's assistant read her prompt, the assistant wrote the program, and the same prompt on a different day can produce different code. The code is where the behavior lives. It is what runs, what fails, and what someone must read when the number looks wrong. The prompt raised the altitude of who can produce code. It did not change what code is, and it did not transfer the responsibility for being right. Section 12.4 turns that responsibility into a workflow.

### Try It Yourself 12.2: Find the Script in the Page 🛠️

**Predict:** This textbook is itself a website. Based on this section, predict in writing whether its pages carry JavaScript, and what a page this simple would even need code for.

**Run:** Open any chapter of the course site in a browser and view the page source, the same move you learned in Chapter 2. Search the source (++ctrl+f++ or ++cmd+f++) for `<script`.

**Explain:** In 1-2 sentences, report what you found and name one behavior on the page (search, instant navigation, the light/dark toggle) that structure-only HTML could not provide.

### Quick Check 12.2 ✅

1. Arrange these from closest-to-the-hardware to closest-to-human-language: high-level language, machine language, prompt, assembly language.
2. Explain the difference between what HTML does for a web page and what JavaScript does for it, in one sentence each.
3. A classmate says prompts have made programming languages obsolete. Using the difference between a prompt and a program, correct the claim in two sentences.

---

## 12.3 Record It: Macros and the Code They Write

Excel has been keeping a secret from you for seven chapters. Behind its ribbon sits a full programming language, and you do not have to write a line of it to start. You can perform a task once and have Excel write the code itself.

### What Deserves Automation

A **macro** is a recorded or written set of instructions that replays inside an Office app. Before recording one, professionals run a task through a short test, because not every chore is worth automating. Renee's ritual passes on every count.

* **Same steps, same order, every time?** Her formatting routine has not changed since the base went live.
* **Often enough to matter?** Twelve times a year, twenty minutes each: four hours of clicking annually.
* **A cost when it is done wrong?** A missed step means a misread readout on Darnell's desk.

A task that passes is a macro candidate. A task that fails the first test (the steps change with judgment calls each time) is not, and forcing automation onto judgment work is how you automate a mistake. This is Chapter 9's tool-selection habit and CLO IX applied to your own workload: the decision comes before the technology.

### Recording: Excel Writes the First Draft

The **macro recorder** watches the commands you perform and writes each one down as code. You turn it on, do the task once, and stop it. From then on the whole routine replays in about a second. Two facts about the recorder will save you confusion later. It records the commands you complete and the cells you select, not your mouse travel or your scrolling. And it records locations exactly as you touched them. A macro recorded on rows 1 through 64 will happily do the same thing to any sheet you run it on, and only to those rows.

Recorded macros need a home that can hold code. A regular `.xlsx` workbook cannot store macros at all. Saving your work as a **macro-enabled workbook**, the `.xlsm` format, keeps the code with the file, and Excel will warn you if a save is about to strip your macros out. The lab makes this the first thing you do, so twenty minutes of work never vanishes on the first save.

One more honest fact: a macro run cannot be undone. Running one clears Excel's undo history, so ++ctrl+z++ will not bring back what a macro changed. Professionals treat that as a rule of thumb: save first, and test macros on a copy of the sheet, never on the only copy of the data.

### Reading What the Recorder Wrote

The recorder's code is written in **Visual Basic for Applications** (VBA), the programming language built into the major Microsoft 365 desktop apps such as Word and Excel. To see it, you open the **Visual Basic Editor** (VBE), a separate window that shows the code living in your workbook (Developer tab, then Visual Basic). Inside, code sits in a **module**, a container page for code, and each macro is a **procedure**: a named block that starts with `Sub` and ends with `End Sub`. Here is what the recorder writes for a two-step recording, bolding the header row and filling it yellow. This is the recorder's own style, untrimmed (your recorder's exact lines may differ a little by Excel version and platform):

```vba
Sub FormatHeader()
'
' FormatHeader Macro
'
    Range("A1:J1").Select
    Selection.Font.Bold = True
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 65535
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
End Sub
```

Read it like the plain sentences it almost is. Select cells A1 through J1. Make the selection's font bold. Then a block about the selection's interior, its fill, where the recorder wrote down six settings when you only chose one: the color. That verbosity is the recorder's signature. It records every default the dialog touched, not just your decision. Lines that begin with an apostrophe are **comments**, notes for humans that the computer skips, and the recorder starts every macro with a few. Your job when editing is to add the comment that matters, the WHY, the same documentation standard your labs have graded all term.

Once you can read a macro, you can edit one, and this is where VBA stops being a recording and starts being a language. Cleaned by hand, the same macro says only what you meant:

```vba
Sub FormatHeader()
    ' Header format for the monthly readout: bold on yellow,
    ' so the print copy reads at a glance in the venue office.
    Range("A1:J1").Font.Bold = True
    Range("A1:J1").Interior.Color = 65535
End Sub
```

Written VBA can also do what no recording can: remember a value and reuse it. A **variable** is a named storage box a program fills and reads as it runs, declared in VBA with `Dim`:

```vba
Dim lastRow As Long
' Ask the sheet where its data ends instead of assuming it.
lastRow = Cells(Rows.Count, "A").End(xlUp).Row
```

That pair of lines starts at the bottom row of column A and jumps up to the last filled cell, then stores that row number in `lastRow`. It is the code version of asking "how much data is there this month?" Hold on to it. It is about to matter more than any other code in this chapter.

!!! tip "Tech in Your Field"
    The monthly ritual is universal, and so is this fix. Business and entrepreneurship students will meet spreadsheets that get the same month-end formatting and totals every close, which is why accounting teams keep small macro libraries. Nursing and health sciences students will see unit schedules and supply counts rebuilt on the same template every week, and the informatics nurses who automate them. Public safety students will watch a records clerk turn the monthly incident export into the chief's report, the same transformation every month. Arts and communication students will settle box-office and content-calendar spreadsheets after every show and every campaign. In each field the role is shifting the same direction, not disappearing: less time performing the ritual, more time checking what the automated version produced.

### The Security Turn

Code that lives inside a document cuts both ways, and you knew this before this chapter named it. Chapter 8 taught you that attachments carry attacks. A macro is code that runs on your machine, so a workbook from a stranger can carry a hostile macro the way a phishing link carries a fake login page. Attackers have used exactly that trick for decades.

This is why Excel treats arriving macros as guilty until proven innocent, and the details differ by platform. On Windows, files that come from the Internet are marked on the way in, and Excel blocks their macros outright, showing a red banner with no button to run them. On a Mac, Excel warns you and asks before enabling any workbook's macros. Even a macro workbook you made yourself greets you with a notification the first time you reopen it, and that is the system working. The professional habit has two parts, and reading code is only one of them. Run macros from a source you trust, in a file you expected, whose code you have opened and read. When any of those three is missing, the macro does not run, no matter how urgent the file claims to be. Notice this lab never asks you to enable a stranger's code. You will build your macros yourself, and the AI draft ships as plain text you read first and paste in with your own hands.

### Try It Yourself 12.3: Count the Recorder's Lines 🛠️

**Predict:** You just watched two actions (bold, fill) become a dozen-plus lines of recorded VBA. The lab's full recording adds three more actions: widening all ten columns, formatting column J as currency, and freezing the top row. Predict in writing how many total lines your recorded `FormatExport` macro will hold, counting `Sub`, `End Sub`, and comments.

**Run:** Read the untrimmed `FormatHeader` recording above and mark which lines came from a decision you made versus defaults the recorder wrote down anyway. (You will check your line-count prediction against your own recording in the lab.)

**Explain:** In 1-2 sentences, explain why the recorder writes settings you never chose, and why that makes recorded macros longer, not smarter, than written ones.

### Quick Check 12.3 ✅

1. Apply the three-part automation test to a task you did this week and report the verdict with one sentence of evidence per part.
2. Your classmate recorded a macro, saved the workbook as `.xlsx`, and lost the macro. Explain what happened and the save that would have prevented it.
3. A workbook arrives by email from an address you do not recognize, and its banner says macros were blocked. State the professional response, and the Chapter 8 threat this block is defending against.

---

## 12.4 Drafted by a Machine, Signed by You: AI Coding Assistants

Chapter 11 promised that this chapter would put an AI coding assistant to work. Here is what that looks like, and what it demands of you.

An **AI coding assistant** is an AI tool that writes, explains, and edits code from plain-language requests. Some live in chat windows, some inside programming editors, and some inside the Office apps themselves. Given "write a macro that totals my quoted-price column," one will produce a competent draft in seconds, usually with its own comments. They are genuinely good, and they are now a standard part of how software gets written. Professionals who refuse them are giving away speed. Professionals who trust them blind are giving away something worse.

### Fluent Is Not Correct

You already know why, because you met this exact failure in Chapter 2. An answer engine can produce a hallucination: fluent, confident, wrong. A coding assistant inherits the same trait, with one upgrade in danger. Drafted code can fail loudly, with a crash you catch in seconds, and when it does, you fix it and move on. The failures that matter are the ones that survive that first run: fluent code built on a wrong assumption, which runs clean and produces a plausible number. A crash cannot reach Darnell's desk. A plausible number can.

The most common failure is not exotic. The assistant builds exactly what the prompt describes, and the prompt describes the world as it was. Renee told her assistant in September that the export's data runs from row 2 to row 61, which was true, in September. The draft it returned hardcodes that assumption into every line:

```vba
bookingCount = Application.WorksheetFunction.CountA(Range("A2:A61"))
totalRevenue = Application.WorksheetFunction.Sum(Range("J2:J61"))
```

Run on October's export, this code does not fail. It counts 60 of October's 63 bookings, sums rows that stop three bookings short, and reports both with a straight face. The draft was right about September, and nobody told it about October. That is what a stale assumption looks like: not a bug in the assistant, a bug in the handoff between a human and a machine that only knows what it was told.

### The Verification Workflow

So the skill of 2026 is not writing code from scratch. It is verifying code you did not write, and it has four moves. They should feel familiar: they are Chapter 2's fact-checking discipline pointed at code instead of claims.

* **Read it first.** Before running anything, read the code and say what each line does in plain language. You can read VBA now: `Sub`, ranges, variables, comments. Anything you cannot explain, you ask about or look up, before it touches data.
* **Test it against a known answer.** Compute the ground truth with a tool you trust before you run the draft. A status-bar count and a `SUM` formula take thirty seconds, and they turn "looks right" into "matches or does not."
* **Check the edges.** The first row, the last row, and next month. Ask what happens when the data grows, shrinks, or shifts. Hardcoded ranges fail exactly here, and so do most stale assumptions.
* **Sign it.** The moment you run code, its output becomes your work. "The AI wrote it" is not a defense a professional gets to use, any more than "the intern drafted it" excuses an unread report.

The durable fix for Renee's draft is the variable you met in Section 12.3. Instead of assuming where the data ends, ask the sheet:

```vba
Dim lastRow As Long
' Find the last filled row in column A, so next month still works.
lastRow = Cells(Rows.Count, "A").End(xlUp).Row
totalRevenue = Application.WorksheetFunction.Sum(Range("J2:J" & lastRow))
```

The `&` glues the row number onto the range address, so the range is built fresh from whatever the sheet holds, this month and every month after. One variable turns a September-only macro into a monthly tool. In the lab, you will make exactly this repair and prove it against your own ground truth.

### The Loop This Book Opened

Step back and look at where the course ends. In Chapter 1 you polished a letter an assistant drafted. In Chapter 2 you fact-checked claims a machine composed. Now you have verified and repaired code a machine wrote. Three deliverables, one spine: the tools draft, and you decide. Every chapter between them told the same story from a different floor of the system, from the hardware up through networks, security, data, and planning.

The judgment that stays with you is not a consolation prize for humans. It is the working skill. Anyone can ask an assistant for a macro. The person Saguaro Hall needs is the one who knows what to ask for, reads what comes back, tests it against a known answer, and signs it. After the next lab, that person is you.

### Try It Yourself 12.4: Read the Draft Before You Run It 🛠️

**Predict:** Open `ai-macro-draft.txt` from the data pack and read Renee's September prompt and the assistant's full draft, without opening Excel. Predict in writing the exact count and whether the total will be high, low, or right when this runs on October's 63-booking export.

**Run:** Apply move one of the workflow: say in plain language, line by line, what the draft does. Note every place a location or a month is hardcoded.

**Explain:** In 1-2 sentences, name the stale assumption, where it came from (read the prompt again), and which verification move would catch it even if you had never seen the code.

### Quick Check 12.4 ✅

1. Explain why the AI-drafted mistakes that survive to reach a decision-maker are usually logic errors, not syntax errors, and why that raises the stakes instead of lowering them.
2. List the four moves of the verification workflow in order, and name the Chapter 2 habit the whole workflow descends from.
3. A teammate says checking AI code defeats the purpose because verification takes time. Using Renee's $5,400 miss, argue the economics in two sentences.

---

## 12.5 Summary and Retrieval 💡

### Key Concepts

* A program is instructions a computer follows. It reaches working form through six desk-scale steps: say what it must do, sketch the logic, write the code, test it, write it down, keep it alive. Pseudocode and flowcharts sketch the plan, and three logic structures (sequence, selection, repetition) are the entire grammar of the steps. Testing separates the two ways code goes wrong: syntax errors crash loudly, and logic errors run clean and answer wrong. The quiet kind is the expensive kind.
* Programming languages climbed from the processor's machine language toward human language: assembly, then high-level languages like Python, JavaScript, and VBA, translated down by compilers and interpreters. Code also rides inside hosts: the browser runs JavaScript shipped in a page's HTML, and Excel runs VBA shipped in a workbook. The prompt is the newest altitude, and it produces code without replacing the need to read it.
* A macro automates a repetitive Office task, and the recorder writes its VBA for you. The code is verbose, honest, and readable in the Visual Basic Editor, where it lives in modules as Sub procedures with apostrophe comments. Macros need the macro-enabled `.xlsm` format and cannot be undone after they run. Excel challenges them when a file arrives from the Internet, because code in a document is a Chapter 8 attack surface as well as a tool.
* An AI coding assistant drafts working code from a prompt, and its failures are typically quiet: fluent code built on a stale or wrong assumption, like a range hardcoded to last month's row count. The verification workflow answers it: read the code first, test it against a known answer, check the edges, and sign what you ship. The tools draft. You decide.

### Key Terms

See course glossary for full definitions

* program, pseudocode, flowchart, logic structure, syntax error, logic error, debugging (Section 12.1)
* machine language, assembly language, programming language, compiler, interpreter, scripting language, JavaScript (Section 12.2)
* macro, macro recorder, macro-enabled workbook, Visual Basic for Applications (VBA), Visual Basic Editor, module, procedure, comment, variable (Section 12.3)
* AI coding assistant (Section 12.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the six desk-scale steps of building a program, and name the step where most beginners are tempted to start.
2. Explain the difference between a syntax error and a logic error, and state which one an AI coding assistant is more likely to hand you.
3. Name the three logic structures and point to one place this chapter's pseudocode used each.
4. State what the macro recorder does and does not capture, and why recorded code runs longer than written code.
5. Recite the four moves of the verification workflow and apply the second move to a macro that claims your sheet holds $78,510.

---

## 12.6 Skills Lab 12A: Record It, Read It, Rewrite It: Your First Macro

**Goal:** Take over Renee's monthly readout: record the formatting macro yourself, read and improve the code Excel writes, then verify the AI-drafted summary macro and repair its quiet mistake before Darnell reads October's number.

**Dataset or starter files:** Two provided files in `assets/code/chapter-12/` from the course data pack. `booking-export.xlsx` is October 2026's raw booking export from the Saguaro Hall base: one worksheet named `OctoberExport`, 63 bookings by 10 columns, sorted by event date. It carries no cancellations and no customer contact details, because the export view filtered both out before download (the least-privilege habit from Chapters 8 and 10). `ai-macro-draft.txt` holds Renee's September prompt and the macro an AI assistant drafted from it, unchanged. The folder README is the data dictionary. Download the data pack from Canvas, extract it, and work at the extracted `cis105` root. You will load the provided files, never retype the data.

**Scenario:** October was the base's first full month running solo, and the monthly readout ritual is now yours. Renee's formatting routine wants to become a macro, and her AI-drafted summary macro has never been checked by anyone who can read it. This month, that person exists.

!!! note
    This lab requires desktop Excel on Windows or macOS (Microsoft 365 is free through Phoenix College). Excel for the web can open the export, but it cannot record or run macros, the requirement Chapters 3, 6, and 7 flagged. No AI account or subscription is needed: the AI draft ships in the data pack as plain text, so every student verifies the same artifact.

### Part 1: Foundation (Aligns with Objectives 12.1 and 12.3)

1. Open `booking-export.xlsx` in desktop Excel. If Excel opens it in Protected View, click Enable Editing: the pack traveled from the Internet, and Excel says so. Then use File > Save As to save your working copy as `skills-lab-12a-lastname.xlsm`, picking **Excel Macro-Enabled Workbook** in the file-type list (Windows calls the list "Save as type," Mac calls it "File Format"). The `.xlsx` format cannot hold the macros you are about to create.
2. Show the Developer tab if it is hidden. On Windows: File > Options > Customize Ribbon, and check Developer. On Mac: Excel > Settings (older versions say Preferences) > Ribbon & Toolbar, and check Developer.
3. Look before you automate. Confirm the data's shape the Chapter 9 way: select column A and read the status bar's count (you are looking for 64, the header plus 63 bookings). Note the last data row's number for later.
4. Right-click the `OctoberExport` sheet tab, choose Move or Copy, and check Create a copy. The copy arrives named `OctoberExport (2)`, so double-click its tab and rename it `RawBackup`. A macro run cannot be undone, so the backup is your safety net, and rule one of professional macro work.
5. Plan before you record: write your five formatting steps as pseudocode, in order, in a note you will paste into your deliverable later. The five steps: bold the header row, fill the header with a standard color, autofit all ten columns, format column J as currency, freeze the top row.
6. Click back to the `OctoberExport` sheet tab (duplicating leaves the copy active, and an unqualified macro formats whatever sheet is active). On the Developer tab, click Record Macro. Name it `FormatExport` (macro names allow no spaces), leave the shortcut key empty (a shortcut can silently override an Excel command), set Store macro in to **This Workbook**, and click OK. Everything you do now is being written down.
7. Perform your five steps exactly once, in your planned order. Click the row 1 heading to select the whole header row, apply bold, then a fill from the Standard Colors row of the fill menu (theme colors record differently, so use the standard row). Drag across the column headings A through J and autofit their width (Home > Format > AutoFit Column Width). Click the column J heading to select the whole column, open Format Cells (++ctrl+1++ or ++cmd+1++), and choose Currency. Selecting the whole column, not a row range, keeps your macro honest when November runs longer. Finish with View > Freeze Panes > Freeze Top Row. Click Stop Recording on the Developer tab.
8. Prove the macro. Duplicate `RawBackup` the same way you made it and name the copy `SecondRun`. With `SecondRun` active, run your macro (Developer > Macros > `FormatExport` > Run) and watch the ritual happen in about a second. Twenty minutes a month just became one click.

### Part 2: Application (Aligns with Objectives 12.2 and 12.3)

1. Open the Visual Basic Editor (Developer > Visual Basic) and find your code: in the Project pane, expand Modules and open `Module1`. Read `FormatExport` top to bottom next to your pseudocode plan, and match each planned step to the block of code it produced. Check your Try It Yourself 12.3 line-count prediction against the real thing.
2. Document it like a professional. Add a comment header inside the procedure (your name, the date, and one line saying WHY this macro exists), plus one WHY comment above each of your five step blocks. Comments start with an apostrophe. Your standard is the course's: a colleague could read and build on this.
3. Count the recorder's extras. In your deliverable note, record how many lines you never asked for (default settings inside With blocks, extra selections). This is the recorder's verbosity, and you just read straight through it.
4. Edit code by hand. In the fill block, change the `.Color` value to `65535` if it is not already, run the macro on `SecondRun`, and confirm the header turns yellow. You have now modified a program.
5. Make the macro yours. Design one improvement Renee never asked for, your call: a sixth formatting step, a smarter target, a cleanup the readout needs. Add it by re-recording or by editing the code, put a WHY comment above it with the word `IMPROVEMENT`, and run the macro on `SecondRun` to prove it works. This step is graded on your design choice, not its size.
6. Break it on purpose, safely. Delete the closing quotation mark from `"A1:J1"` (or your recording's equivalent range). Excel may complain the moment you leave the line, or when you run the macro: either way, read the loud message, and note that nothing ran at all. Restore the quotation mark, run the macro on `SecondRun` again, and confirm it works end to end. That was a syntax error: the cheap, honest kind. Write one sentence in your note about how it announced itself.

### Part 3: Extension (Aligns with Objectives 12.2 and 12.3)

1. Read before you run: open `ai-macro-draft.txt`, read Renee's prompt and the assistant's draft, and write a one-line prediction in your note of what the draft will report on October's export.
2. Establish ground truth with tools you trust, before the draft runs. The booking count is your Part 1 status-bar count minus the header: 63. For the money, click an empty cell beside the data on `OctoberExport`, in column L (try `L10`), and enter `=SUM(J2:J64)`, using the last data row you confirmed. Keep column A clean: the repair you will make later measures the data by column A, and a stray value there would poison it. Write both numbers in your note (you are looking for 63 bookings and $83,910).
3. Run the draft against your ground truth. First click the `OctoberExport` sheet tab, because the draft reads whatever sheet is active, the lesson from Part 1. In the VBE, choose Insert > Module, paste the draft's code into the new module, click inside `SummarizeExport`, and run it (++f5++ or Run > Run Sub). It finishes with no error message, and its summary block appears beside the data: 60 bookings, $78,510, labeled September. Compare both numbers to your ground truth and record all four in your note (its count and total, your count and total). The gap: three bookings and $5,400, on a readout headed for Darnell's desk.
4. Diagnose it. Reread the draft's code and Renee's prompt, and write the root cause in one sentence: where did the ranges `A2:A61` and `J2:J61` come from, and what changed between September and October? Which of the two error kinds is this, given that nothing crashed?
5. Repair it durably. A quick fix (typing 64 where 61 was) would break again in November, so make the repair that asks the sheet instead of assuming. Your repaired procedure should match this shape, with the label freed from any month:

    ```vba
    Sub SummarizeExport()
        ' Summarize the monthly export, whatever size the month is.
        Dim lastRow As Long
        Dim bookingCount As Long
        Dim totalRevenue As Double

        ' Ask the sheet where its data ends instead of assuming it.
        lastRow = Cells(Rows.Count, "A").End(xlUp).Row

        bookingCount = Application.WorksheetFunction.CountA(Range("A2:A" & lastRow))
        totalRevenue = Application.WorksheetFunction.Sum(Range("J2:J" & lastRow))

        Range("L1").Value = "Monthly Summary"
        Range("L2").Value = "Bookings"
        Range("M2").Value = bookingCount
        Range("L3").Value = "Total quoted revenue"
        Range("M3").Value = totalRevenue
        Range("M3").NumberFormat = "$#,##0.00"
        Columns("L:M").AutoFit
    End Sub
    ```

    Run it and verify: the summary block must now match your ground truth exactly, and running it twice must leave one summary, not two.

6. Assemble the deliverable. Add a worksheet named `Questions & Analysis`. Paste in your running note: the pseudocode plan, line counts, your IMPROVEMENT choice, the broken-on-purpose sentence, your prediction, and the four-number evidence block from step 3. Then answer the two questions below in labeled cells with Wrap Text on. Delete your `=SUM` scratch cell, save the `.xlsm`, and confirm your four sheets and your macros are all present. One last rehearsal for the road: close the workbook and reopen it. Excel will ask before enabling your macros (a banner on Windows, a dialog on Mac). It is your file and your code, so enable them, and notice you just practiced the security habit from Section 12.3.

### Questions & Analysis 🤔

Answer both questions on your `Questions & Analysis` worksheet. These answers carry significant rubric weight.

1. The AI draft ran without a single error message and still handed Darnell a wrong October. Use your own Part 2 and Part 3 evidence: how the broken-quote error announced itself, versus the draft's 60 and $78,510 against your 63 and $83,910. Explain the difference between a syntax error and a logic error, and why the quiet kind is the one that reaches a decision-maker. Close by naming the verification move that caught the draft, and one earlier place in this course you used the same known-answer habit.
2. Renee's ritual passed the automation test, and yours is out there. Name one repetitive computer task from your own field, job, or major, and run it through the three-part test from Section 12.3. Then decide what you would do: record it, ask an AI assistant to draft something bigger, or leave it manual. Defend the decision in 2-3 sentences, including who verifies the output and what a quiet wrong answer would cost in that setting.

**Submission:** Submit one file: your macro-enabled workbook `skills-lab-12a-lastname.xlsm`. It contains the formatted `OctoberExport` sheet with the corrected summary block, your `RawBackup` and `SecondRun` sheets, and the `Questions & Analysis` worksheet. Its VBA project holds your commented `FormatExport` (including your `IMPROVEMENT` step) and the repaired `SummarizeExport`. The file name uses your own last name.

### Rubric: Skills Lab 12A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s). Your instructor sets
the point weights in your course. The criteria and levels are the
same everywhere.

---

## 12.7 Review Questions 🔄️

1. **Remember:** Name the six desk-scale steps that carry a program from a named need to maintained code, and state which workbook format can store a macro.

2. **Apply:** A clinic's front-desk coordinator spends fifteen minutes every Friday reformatting the week's appointment export the same way: header styling, column widths, a currency column, a frozen top row. Apply the three-part automation test to this task and state your verdict with one sentence of evidence per part.

3. **Evaluate:** A coworker says, "I ran the macro and it finished with no error message, so the numbers are right." Judge that claim using the two kinds of errors from this chapter, and name the specific evidence you would demand before the numbers reach a decision-maker.

4. **Create:** Design, without building it, an automation plan for one repetitive task in your own field. Name the task, and write four to six lines of pseudocode using at least two of the three logic structures. Then state the two checks from the verification workflow you would run before trusting the plan's first output.

---

## Further Reading 📖

* [Microsoft Support: Quick start: Create a macro](https://support.microsoft.com/en-us/office/quick-start-create-a-macro-741130ca-080d-49f5-9471-1e5fb3d581a8) - Microsoft's own walkthrough of recording, running, and editing a macro, the same moves as Skills Lab 12A.
* [Microsoft Learn: Getting started with VBA in Office](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office) - The official next step when you want to write VBA beyond what the recorder produces.
* [Microsoft Learn: Macros from the internet are blocked by default in Office](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked) - Why Excel blocks arriving macros, the security default Section 12.3 teaches.
* [U.S. Bureau of Labor Statistics: Software Developers, Quality Assurance Analysts, and Testers](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) - The federal career profile for the people who write and test programs full time: duties, pay, and outlook.
* [MDN Web Docs: What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript) - A beginner-level introduction to the web's scripting language from Section 12.2.

---

## Course Conclusion: Where You Go from Here

This is the end of the book, and the loop it opened in Chapter 1 is closed. You started by naming the six parts of an information system and polishing a machine-drafted letter. You end having produced documents, decks, workbooks, a database, and a rollout plan, and having repaired code a machine wrote, with the judgment calls yours at every step. The tools will keep getting faster at drafting, building, and automating. Every one of them will still need what you now have: someone who checks the output against a known answer before it reaches a decision. Your field is full of twenty-minute rituals nobody has questioned yet, and you know what to do with the next one.
