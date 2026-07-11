# Chapter 2: The Web at Work: Search, Communication, and E-commerce

Maya Reyes is thinking bigger than the pickup shelf. If Bloom Ahead can take orders from across the street, why not sell Desert Bloom's roasted beans across the country? She asked an AI assistant how online selling works and got back a confident, well-organized briefing in eleven seconds. It reads beautifully. It is also wrong in at least two places, and Maya cannot tell which two. Neither can you, yet. By the end of this chapter, you will be able to find out, prove it, and report it professionally.

That skill matters far beyond one coffee shop. The web is where every field now finds information, talks to customers and colleagues, and does business. It is also where anyone, and now any AI model, can publish anything with the same polished confidence. Chapter 1 gave people three jobs the machines cannot take: judgment, verification, and trust decisions. This chapter is where verification becomes a method you can run in minutes instead of a value you agree with in principle.

Here is the route. First you will see how the Internet grew into a utility and what happens in the seconds after you type a web address. Then you will put search engines and AI answer engines side by side and learn to fact-check both like a professional. Next you will tour the communication channels working life runs on, from email to video calls, and learn the memo, the format professionals still use to put findings on the record. Finally you will follow the money through e-commerce, from storefronts to safe transactions. The Skills Lab puts it all together: you will fact-check that AI briefing for Maya and deliver your findings in a formatted memo.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero), builds on Chapter 1's six-part system and Word basics
* **Deliverables:** Skills Lab 2A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-2.1 (Understand):** Explain how browsers, web servers, and HTML work together to deliver a web page when you type an address
* **MLO-2.2 (Apply):** Verify claims from search results and AI answer engines using lateral reading and credible sources
* **MLO-2.3 (Apply):** Produce a professionally formatted research memo in Word that reports verification findings with evidence

### This chapter aligns with the following Course Learning Outcomes

* **CLO IV (Understand):** Describe the technologies behind websites, including browsers, HTML, and web servers
* **CLO V (Apply):** Use the Internet to communicate, collaborate, and retrieve credible information
* **CLO VI (Analyze):** Examine system security and privacy risks and the safeguards that reduce them

---

## 2.1 How the Internet Became a Utility

Chapter 1 called connectivity one of the six parts of every information system. This chapter follows that part out of the coffee shop and around the planet. Start with a definition worth memorizing: the **Internet** is the global network of connected devices and the physical infrastructure that links them. Cables, cell towers, satellites, and data centers, all speaking common rules so that any device can reach any other.

### From Research Project to Public Square

The Internet did not start as a business. It started in 1969 as ARPANET, a U.S. research network connecting a handful of university computers. Email arrived in 1971 and became the network's first hit application. For twenty years the network belonged to researchers, and almost nobody else knew it existed.

The turn came in 1991, when Tim Berners-Lee invented the **World Wide Web** (the web). The web is a system of linked pages, reached through the Internet, that anyone can read with a browser and anyone can publish to. The Internet is the road system. The web is one kind of traffic on it, alongside email, streaming, gaming, and the app connections you used in Chapter 1. Keep the two terms separate and you will already be more precise than most headlines.

After the web, growth went vertical. Browsers made the web visual in the mid-1990s. Broadband made it fast in the 2000s. Smartphones put it in every pocket after 2007, and today roughly two thirds of humanity is online.

| Year | Milestone |
| ---- | --------- |
| 1969 | ARPANET connects its first computers |
| 1971 | The first network email is sent |
| 1991 | Tim Berners-Lee publishes the first web page |
| mid-1990s | Graphical browsers open the web to the public |
| 2007 | Smartphones put the web in every pocket |
| mid-2020s | AI answer engines join search engines as the web's front door |

That is why this chapter's title calls the Internet a utility. Like power and water, it is infrastructure daily life assumes, and businesses that lose it stop working.

### Nobody Owns It

Here is the strangest fact about infrastructure this important: nobody owns the Internet, and nobody runs it. Standards groups publish the common rules so every device speaks the same language. Providers own their own pieces: cable companies own cable, phone carriers own towers, and companies own their data centers. Undersea fiber lines, laid by groups of companies, carry almost all traffic between continents. The whole thing holds together by agreement, because being connected is worth more than being separate.

For you, two consequences matter. First, no single switch turns it off, which is why the Internet survives disasters that break any one provider. Second, no single authority checks what gets published on it, which is why Section 2.2's verification method is your job and not somebody else's. The openness that lets Maya sell beans nationwide is the same openness that lets anyone publish anything.

### Type an Address, Get a Page

Now slow down the everyday miracle. You type an address and a page appears in about a second. Four players make that happen.

A **browser** is the program that requests pages and displays them: Chrome, Edge, Safari, and Firefox are the big four. A **web page** is a single page of content. A **website** is a collection of related pages under one name, the way Desert Bloom's future site will have a home page, a menu page, and an ordering page. A **web server** is a computer, usually in a data center, that stores a website and answers requests for its pages around the clock. You met servers in Chapter 1. This is the specific kind the web runs on.

The address itself is a **URL**, the complete address of one page on the web. It has three working parts:

```text
https://  www.phoenixcollege.edu  /academics
rules     which site               which page
```

The front names the rules for the trip (`https` matters enough to get its own subsection in Section 2.4). The middle names the site. Everything after the slash names the page within it. Delete the page part and you land on the site's front door, which is a handy trick when a shared link is broken but the site is fine.

Put in motion, the round trip looks like this:

1. You type the URL or tap a link.
2. A directory service translates the site's name into the numeric address of its server. Machines route by number, people remember names.
3. Your browser sends a request across the Internet to that server.
4. The server finds the page and sends its files back.
5. Your browser turns those files into the formatted page you see.

When a page fails to load, one of those five steps broke. That is the six-questions habit from Chapter 1, applied to the web.

### The Language Pages Are Written In

What the server sends is not a picture of a page. It is text written in **HTML** (Hypertext Markup Language), the language that labels each piece of content so the browser knows what it is and how to present it. A tiny sample:

```html
<h1>Desert Bloom Coffee</h1>
<p>Order ahead with <strong>Bloom Ahead</strong>, our mobile app.</p>
```

```text
The browser renders:
a large heading "Desert Bloom Coffee", then a paragraph
with "Bloom Ahead" in bold.
```

The tags in angle brackets are labels, not decorations: `<h1>` marks a top-level heading, `<p>` marks a paragraph, `<strong>` marks emphasis. Your browser reads the labels and draws the page. Every site you have ever visited works this way, and you can prove it: every browser will show you the raw HTML it received. That is the next exercise. You will not write websites in this course, but you will recognize what they are made of, and in Chapter 12 you will see how web scripting builds on exactly this foundation.

### Try It Yourself 2.1: X-Ray a Web Page 🛠️

**Predict:** If you ask the browser to show a page's source instead of the rendered page, what do you expect to see: readable sentences, code, or a mix? Where do you think the page's visible text will be hiding?

**Run:** Visit any website. Right-click an empty spot and choose View Page Source (on Safari, another browser is easier for this). Skim the wall of HTML, then use ++ctrl+f++ or ++cmd+f++ to find one phrase you can see on the rendered page.

**Explain:** In 1-2 sentences, describe what surrounded the phrase you found and what the browser did between receiving that text and showing you the page.

### Try It Yourself 2.2: Take a URL Apart 🛠️

**Predict:** Find any URL with a path after the site name (a news article or a course page works well). Predict what will load if you delete everything after the site name and press Enter.

**Run:** Do it. Then compare the page you landed on against the page you started from, and read both URLs side by side.

**Explain:** In 1-2 sentences, explain what the two URLs share and what the deleted part was telling the server. Use the terms website and web page.

### Quick Check 2.1 ✅

1. A classmate says the Wi-Fi is "down" because one website will not load, but two other sites load fine. Using the five-step round trip, name the step that most likely failed and the evidence for your answer.
2. Explain the difference between the Internet and the web in your own words, using one example of Internet traffic that is not web traffic.
3. Desert Bloom's future site will have a home page, a menu page, and a bean-ordering page. Which terms from this section name the whole collection, one page of it, and the machine that serves it?

---

## 2.2 Getting Results Versus Getting the Truth

The web holds more pages than any person could read in a thousand lifetimes, and two kinds of software offer to hand you the right one. This section puts them side by side, because they earn trust in different ways, and then teaches the verification method that works on both.

### How a Search Engine Finds Anything

A **search engine** is software that builds a searchable index of the web and ranks matching pages for each query. Google, Bing, and DuckDuckGo work the same way at heart. Automated crawlers follow links and read pages around the clock. The engine files what they find in a giant index, the way a library catalog files books. When you search, an **algorithm**, a step-by-step procedure software follows, scores the indexed pages against your words and returns a ranked list in a fraction of a second.

Notice what a search engine hands you: a list of pages, with the judging left to you. Ranking is not truth. Position one means the algorithm scored it well, and businesses work hard to earn that slot because it brings customers. A few habits sharpen your results:

* Put exact phrases in quotation marks: `"petal points"` finds that phrase, not the separate words.
* Add `site:` to search one site: `beans site:census.gov` searches only that domain.
* Use a minus sign to exclude a word: `jaguar -car` when you mean the animal.
* Search less like a question and more like the answer: `arizona food handler card cost` beats `how much does it cost to get a food thing in arizona?`

### Enter the Answer Engine

Beside the ranked list, something new now answers in full sentences. An **answer engine** is AI software that composes a direct, conversational answer to your question instead of a list of pages. Some live inside search engines as AI answer boxes. Others are standalone chat tools. Under the hood sits a **large language model** (LLM), an AI system trained on enormous amounts of text that generates fluent language by predicting, word by word, what should come next.

That design explains both the magic and the danger. The magic: an LLM can synthesize a readable answer from patterns across millions of pages, which beats opening ten links when you need orientation fast. The danger: it composes. It does not look truth up in a table. When the patterns run thin, it can produce a **hallucination**, a confident, fluent statement that happens to be false. The tone does not change when the facts do, and an answer engine also carries no publication date guarantee: it may describe last year's web.

So match the tool to the job, the habit this course keeps drilling:

| | Search engine | Answer engine |
| --- | ------------- | ------------- |
| Hands you | A ranked list of pages | A composed answer |
| Judging the source | You can, the pages are right there | Harder, the answer may cite loosely or not at all |
| Freshness | Pages can be checked for dates | The model may describe last year's web |
| Best for | Finding the source itself | Orientation, brainstorming, summaries |
| Worst failure | A polished page that ranks well and lies | A hallucination delivered in perfect confidence |

For anything you will act on, spend money on, repeat to a customer, or submit for a grade, run the verification method below on either tool's output. Getting results is instant. Getting the truth takes about ninety more seconds.

### Lateral Reading: Verify Like a Fact-Checker

Start with a quick screen of whatever page or answer is in front of you. Five questions, five seconds each: Who wrote this, and are they named? When was it published? Why does it exist (to inform, to sell, to persuade, to farm clicks)? What evidence does it show? Who hosts it? A page that fails several of those questions rarely deserves a deeper look.

But the screen has a ceiling, and here is why. Anyone can publish a professional-looking page, and generative AI now writes floods of them: plausible articles, fake reviews, invented experts, at a cost of nothing. The page's own claims about itself are exactly what a liar controls. So professional fact-checkers do something beginners find strange: they spend almost no time on the page they are checking. Instead they read laterally. **Lateral reading** means leaving the page and opening new tabs to see what the rest of the web says about the claim and its source. Studies of professional fact-checkers show it beats staring harder at a polished page, because polish is what liars and language models are best at.

Run it as five steps:

1. **Pause.** Do not share, act, or answer yet. Confidence is a feeling, not a verdict.
2. **Isolate the claim.** State exactly what is being asserted, in one sentence, with numbers and dates attached.
3. **Leave the page.** Open a new tab and search the claim and its source. What do unrelated, credible outlets say?
4. **Favor accountable sources.** Prefer sources with editors, expertise, and something to lose: government statistics agencies, major news organizations, universities, and established reference works. Trace viral claims to the **primary source**, the original document or dataset the claim is built on.
5. **Deliver a verdict.** Confirmed, refuted, or unverified. Unverified is a legitimate professional answer, and saying it honestly beats guessing.

The method works on a stranger's post, a search result, an AI answer, and your own memory. In the Skills Lab you will run it five times against Maya's briefing and put the verdicts in writing.

!!! tip "Tech in Your Field"
    Lateral reading is billed as a news-literacy skill, but it is daily equipment across the majors in this room. Nursing and health sciences students will field patients' questions about treatments they read about online, and checking claims against primary sources is patient safety, not homework. Business students will vet suppliers, influencer metrics, and AI market summaries before money moves. Public safety and law students will see AI-polished misinformation move faster than corrections, and verification is now part of the badge. Communication and arts students publish into the same feeds, where sourcing accurately is what separates a reputation from a rumor. The tools got faster at asserting. Your fields pay you to be right.

### Try It Yourself 2.3: Same Question, Two Engines 🛠️

**Predict:** Pick a factual question in a field you care about. If you ask a search engine and an AI answer box the same question, predict one way the two responses will differ beyond formatting.

**Run:** Search the question in any search engine and read the AI answer box if one appears, then the top three ranked results. No AI box? Compare the top result against the next two instead. Note what each response cites, and whether the answers agree.

**Explain:** In 1-2 sentences, describe which response made it easier to judge WHERE the information came from, and what that means for how you should use each tool.

### Try It Yourself 2.4: The Ninety-Second Fact-Check 🛠️

**Predict:** Find one factual claim in your feeds or in an AI answer from the last exercise. Before checking, write your gut verdict: confirmed, refuted, or unverified, and your confidence from 1 to 5.

**Run:** Run the five lateral reading steps on the claim. Time yourself. Stop at two unrelated credible sources or ninety seconds, whichever comes second.

**Explain:** In 1-2 sentences, compare your gut verdict to your evidence verdict and name which of the five steps changed the picture most.

### Quick Check 2.2 ✅

1. A search engine and an answer engine both respond to "is dark roast coffee lower in caffeine?" Describe one way each could mislead you, and which failure is harder to notice.
2. Why is "unverified" a professionally acceptable verdict, and what would you do next with a claim you could not verify but need for a decision?
3. Your cousin forwards a screenshot claiming a new Arizona law bans gas stoves. Which lateral reading step do you run first, and what kind of source would settle it?

---

## 2.3 Communicating Like a Professional

Finding truth is half the job. Moving it to the right person, in the right format, is the other half. Working life runs on a handful of channels, each with its own norms, and choosing well is a judgment call you will make dozens of times a day.

### Email Still Runs the Working World

**Email** is the formal backbone of professional communication: written messages, delivered to an address, kept on record. Half a century after the first one crossed ARPANET, offers, invoices, approvals, and complaints still travel by email because it works across every organization and leaves a trail.

The address fields carry meaning of their own. To is for the people you expect to act. CC (carbon copy) keeps others informed with no action expected, and everyone can see who got it. BCC (blind carbon copy) hides its recipients from everyone else, which is right for large announcement lists (it protects strangers' addresses) and wrong for quietly looping your boss into a dispute. People notice, and Chapter 8 returns to why hidden copies of workplace mail age badly.

Professional email has learned habits, and they are worth adopting before someone judges you for lacking them:

* **Subject lines carry the message.** "Bean supplier contract: signature needed by Friday" gets action. "Question" gets buried.
* **Front-load the point.** First sentence says what you need and by when. Detail follows.
* **One screen, one topic.** Past that, the message wants to be a document (or a meeting).
* **Reply thoughtfully.** Reply All is for people who need the answer, not everyone who saw the question.
* **Name attachments like a professional.** Chapter 1's file-naming habit shows up here: the reader sees `bloom-ahead-launch-letter.pdf` in the attachment line.
* **Assume permanence.** Email is stored, searchable, and forwardable. Write nothing you would not stand behind later.

### Pick the Channel, Then the Words

Newer channels did not replace email. They took slices of the job. **Messaging** apps (Teams chat, Slack, texts) carry quick, informal, back-and-forth conversation. A **video call** carries meetings when people cannot share a room, with its own norms: camera framing, mute discipline, and an agenda so the meeting earns its slot. The choice among them is a professional signal:

| Channel | Reach for it when | Watch out for |
| ------- | ----------------- | ------------- |
| Email | The message is formal, needs a record, or crosses organizations | Slow for rapid back-and-forth |
| Messaging | The question is quick and the group is close | Interruptions, and informality that reads wrong when forwarded |
| Video call | The topic needs discussion, tone, or screens shared live | Meetings that should have been an email |
| Document or memo | The findings must stand on their own and be filed | Nobody reads it if a one-line message would do |

The rule of thumb: the more formal, consequential, or permanent the content, the further right on the table you go. Announcing the bean launch date to staff is a message. Reporting which AI claims survived fact-checking is a memo.

Video calls deserve one more minute, because every field now interviews, trains, and meets on camera:

* Test your audio, camera, and background before the meeting starts, not during it.
* Stay muted when you are not speaking. Every keyboard and dog in the room disagrees with you about how quiet they are.
* Look at the camera when you speak, and keep your face lit from the front.
* Bring an agenda. A meeting without one was probably an email, and everyone in it knows.

### The Memo: Findings on the Record

A **memo** (memorandum) is a short internal document that puts information on the record: findings, decisions, recommendations. Where a letter travels outside the organization (you wrote one in Chapter 1), a memo stays inside it. The format is rigid on purpose, so readers can process it at a glance:

```text
MEMORANDUM

TO:      Maya Reyes, Owner
FROM:    Your Name, Research Assistant
DATE:    October 12
RE:      Fact-check of AI briefing on online bean sales

SUMMARY
The bottom line, in two or three sentences, first.

FINDINGS
The evidence, organized under headings or in a table.

RECOMMENDATION
What you advise, and why, in plain language.
```

Two features make a memo professional. First, the summary leads: busy readers get the verdict before the evidence, a pattern called bottom line up front. Second, every finding carries its evidence: a claim, a verdict, and the source that settled it. That structure is exactly what the Skills Lab asks you to build. Few sentences are more employable in any field than "I checked, here is what I found, and here is how I know."

### Platforms, Podcasts, and the Creator Economy

One more communication layer matters because your fields increasingly work inside it. Social platforms distribute posts, video, and audio through ranking algorithms, the same idea that orders search results, tuned to hold attention. Podcasts put long-form audio on every commute. Around them has grown the **creator economy**: people earning income by publishing directly to audiences through platforms. It runs from a barista's latte-art videos that fill Desert Bloom's weekend seats to a nurse explaining vaccine schedules to two million followers.

For professionals the platform layer cuts both ways. It is free reach for a small business and a portfolio for an artist. It is also the fastest pipe misinformation has ever had, which is why platform literacy and Section 2.2's verification method travel together. What the algorithm rewards is engagement. What your career rewards is being right, and Section 2.4's marketplace reviews will make the same point about money.

### Try It Yourself 2.5: Subject Line Surgery 🛠️

**Predict:** Here is an email subject line to a manager: "quick question". Predict how long the reply takes versus a rewritten subject, and write your improved version before reading on.

**Run:** Rewrite the subject twice: once for the same manager, once as a message to a coworker. Then open your own inbox and find the best and worst subject lines of the week. (School announcements count.)

**Explain:** In 1-2 sentences, explain what your best inbox example did that your worst did not, using the front-load habit from this section.

### Quick Check 2.3 ✅

1. Pick the channel for each situation, then defend one of your choices. The situations: telling staff the espresso machine repair is delayed an hour, reporting your fact-check findings to the owner, and asking a coworker which milk supplier called.
2. Name the two features that make a memo readable at a glance, and explain what "bottom line up front" saves a busy reader.
3. A friend building a following says the algorithm "decides what is true" on their platform. Correct that in one sentence using terms from this section.

---

## 2.4 Buying and Selling Online

Maya's question that opened this chapter was an e-commerce question. **E-commerce** is buying and selling goods and services over the Internet, and it is no longer a separate world from "regular" business. The register in Chapter 1 was already e-commerce with a shorter commute.

### Three Shapes of Online Selling

Most online selling takes one of three shapes, and a small business usually ends up mixing them:

* A **storefront** is the business's own site or app, like Bloom Ahead: full control of brand, prices, and customer data, in exchange for building and marketing it yourself.
* An **online marketplace** is a platform hosting many sellers (Amazon, Etsy, eBay): instant reach and built-in payments, in exchange for fees and the platform's rules.
* Consumer-to-consumer selling moves goods between individuals through resale apps and auction sites, where the platform mostly referees.

Businesses also sell to each other (Desert Bloom buys beans, cups, and machine parts online), and that business-to-business layer dwarfs consumer shopping in dollar volume. For Maya, the storefront-versus-marketplace decision is a judgment call about control, cost, and reach, exactly the kind of tool-fit question Chapter 3 turns into a method.

### The Safe Transaction

Sending a card number across a public network sounds reckless until you see the safeguards. The web's answer is **HTTPS**, the secure version of the web's delivery rules. The padlock icon beside the URL means the connection uses **encryption**: your data is scrambled in transit so eavesdroppers see gibberish instead of your card number.

Read that carefully, because it is one of the most misunderstood icons on the Internet. The padlock certifies the connection, not the seller. A scam site can use HTTPS, and most now do. The padlock means nobody can listen in while you send your card number, including while you send it to a thief.

The other safeguards are procedural, Chapter 1's quiet system part:

* Legitimate checkouts hand your card to a **payment processor**, a specialized company that handles the charge, so the shop never stores your full card number. (Bloom Ahead works this way. Check the Chapter 1 fact sheet.)
* Credit cards and payment services carry dispute processes, which is why sellers who demand wire transfers or gift cards are announcing themselves as thieves.
* A **digital wallet** (Apple Pay, Google Pay, and their kin) stores your cards on your phone and pays with a one-time code instead of your card number. The seller never sees the number at all. The same tap that buys your latte at Desert Bloom's counter is e-commerce hardware in your pocket.
* Records protect you: confirmation emails and order histories are your receipts. Email's permanence, from Section 2.3, working in your favor.

### When the Deal Is the Bait

E-commerce scams are a security topic, and Chapter 8 gives online threats a full chapter. But because buying happens weekly, three checks belong in this one:

1. **Price sanity.** A price far below every other seller is not a deal. It is bait.
2. **Seller verification.** Run Section 2.2 laterally: search the seller's name plus "scam" or "reviews" in a new tab. An honest shop has a trail: an address, a return policy, and reviews on sites it does not control. And read reviews with the same skepticism, because AI can generate a thousand glowing fakes overnight. Look for the specific, mixed, dated reviews that are hard to fake at scale.
3. **Payment sanity.** Card or established payment service, always. Anything unrecoverable (wire, gift cards, crypto payment to a stranger) is a no.

Notice what just happened: the verification method you learned for claims works on sellers, reviews, and deals without modification. Truth-checking and safe buying are the same skill pointed at different targets.

### Try It Yourself 2.6: Read the Padlock 🛠️

**Predict:** Click the padlock (or the settings icon) next to a browser's address bar and you will see connection details. Predict what the browser will certify: the connection, the company's honesty, both, or neither?

**Run:** Visit any major shopping site, click the icon beside the URL, and read what the browser reports. Then find the site's return policy page and note how quickly you can locate a physical address or contact page.

**Explain:** In 1-2 sentences, explain what the padlock proved, what it could not prove, and which of this section's three checks covered the gap.

### Quick Check 2.4 ✅

1. Maya can sell beans through her own Bloom Ahead storefront, through a marketplace, or both. Give one advantage and one cost of each shape.
2. A site shows a padlock, a countdown timer, a price 70 percent below everyone else, and accepts payment only by gift card. Rate the four signals from most to least trustworthy and explain the top and bottom of your ranking.
3. Explain in one sentence why a payment processor means a small shop never needs to store your card number, and why that protects both of you.

---

## 2.5 Summary and Retrieval 💡

### Key Concepts

* The Internet is the global network and its physical infrastructure. The web is one service on it: linked pages, born in 1991, delivered by request. Together they grew from a 1969 research project into infrastructure daily life assumes.
* A page arrives in five steps: address typed, name translated to a server's number, request sent, files returned, page rendered by the browser from HTML, the labeling language every page is written in.
* Search engines index and rank pages, leaving judgment to you. Answer engines, powered by large language models, compose fluent answers that can hallucinate. Both are useful. Neither is a verdict.
* Lateral reading is the verification method: pause, isolate the claim, leave the page, favor accountable and primary sources, and deliver a verdict. Confirmed, refuted, and unverified are all professional answers.
* Professional communication is channel choice plus norms: email for the record, messaging for speed, video calls for discussion, and the memo for findings that must stand on their own, summary first.
* E-commerce runs through storefronts and marketplaces. HTTPS encrypts the connection but does not vouch for the seller, so safe buying is lateral reading plus payment sanity: processors and cards, never unrecoverable payment to strangers.

### Key Terms

See course glossary for full definitions

* Internet, World Wide Web, browser, web page, website, web server, URL, HTML (Section 2.1)
* search engine, algorithm, answer engine, large language model, hallucination, lateral reading, primary source (Section 2.2)
* email, messaging, video call, memo, creator economy (Section 2.3)
* e-commerce, storefront, online marketplace, HTTPS, encryption, payment processor, digital wallet (Section 2.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the five steps between typing a URL and seeing a page, and name the language the returned files are written in.
2. Explain the difference between how a search engine and an answer engine produce what you see, and name the failure unique to the answer engine.
3. List the five steps of lateral reading and state which one you personally skip most often.
4. A finding must go on the record for a busy reader. Name the format, its four header lines, and what comes first in its body.
5. State what the HTTPS padlock does and does not certify, and name one payment rule that protects you when the padlock cannot.

---

## 2.6 Skills Lab 2A: Fact-Check the Machine: A Research Memo

**Goal:** Verify five claims from an AI-generated briefing using lateral reading, then deliver your verdicts to Desert Bloom's owner as a professionally formatted research memo.

**Dataset or starter files:** One provided file in `assets/code/chapter-02/` from the course data pack. `ai-briefing.docx` is the briefing Maya's AI assistant produced about the web and online selling, authored for this course in the style of AI assistant output so every student examines the same artifact. Eight numbered claims, confident throughout, correctness varies. Download the data pack from Canvas, extract it, and work at the extracted `cis105` root. No AI account or paid tool is needed anywhere in this lab.

**Scenario:** Before Maya spends money putting Desert Bloom's beans online, she wants to know how much of her AI briefing she can trust. Your job is not to embarrass the machine or to defend it. Your job is verdicts with evidence, on the record.

### Part 1: Foundation (Aligns with MLO-2.3)

1. Create a new blank Word document and save it as `skills-lab-2a-lastname.docx`.
2. Build the memo header exactly as Section 2.3 shows: MEMORANDUM title, then TO (Maya Reyes, Owner), FROM (your name and role), DATE (today), and RE (one line stating the memo's purpose). Bold the four labels.
3. Add three section headings below the header: Summary, Findings, and Recommendation. Style them consistently (bold or a slightly larger size, your call, applied identically to all three). Leave Summary empty for now. You will write it last, the way professionals do.
4. Open `ai-briefing.docx` from the data pack and read all eight claims before choosing any. Notice your own gut reactions as you read. Part 2 tests them.

### Part 2: Application (Aligns with MLO-2.2)

1. Choose five of the eight claims. Your five must include at least one claim you suspect is true and at least one you suspect is false.
2. In the Findings section, insert a table (Insert > Table) with three columns and six rows. Type the header row: Claim, Verdict, Evidence and source. Bold the header row.
3. Run the five-step lateral reading method from Section 2.2 on each chosen claim. For each, record: the claim (shortened to its testable core), your verdict (Confirmed, Refuted, or Unverified), and the evidence with its source. Name the source and include enough detail that Maya could find it: the organization, the page title, and the address.
4. Verdict discipline: at least two unrelated, credible sources for every Confirmed or Refuted verdict. If ninety seconds of honest searching per source leaves a claim unsettled, Unverified is the correct verdict. Say so plainly.

### Part 3: Extension (Aligns with MLO-2.1, MLO-2.3)

1. Write the Recommendation section: 3-5 sentences advising Maya how to use AI briefings in the future, grounded in your table. Base every general statement on a specific row.
2. Maya will soon choose a platform for the bean store, and she should know what she is buying. Add one short paragraph to the Recommendation explaining what happens between a customer typing her future site's address and the order page appearing. Use the round trip from Section 2.1 without technical jargon: name what the browser, the server, and HTML each contribute in words Maya would use.
3. Now write the Summary at the top: 2-3 sentences with the bottom line up front. How many claims held, how many fell, and your one-sentence verdict on the briefing.
4. Add a footer with a page number (Insert > Page Number), run Editor, and read the memo aloud once, the Chapter 1 habit.
5. Export the memo as `skills-lab-2a-lastname.pdf`. Export before adding the Questions & Analysis page below, so the PDF stays a clean deliverable.

### Questions & Analysis 🤔

Add a page break at the end of your Word document, add the heading "Questions & Analysis," and answer both questions there. These answers carry significant rubric weight.

1. Pick the claim whose verdict was hardest to reach. Walk through what each lateral reading step contributed, name the sources that settled it (or failed to), and state what the briefing's confident tone concealed about it.
2. The AI briefing cost Maya eleven seconds. Your memo cost her an hour of your time. Using two specific rows from your findings table, argue where the memo earned that cost, and describe one situation where the briefing alone would genuinely be the right tool.

**Submission:** Submit two files: your Word document `skills-lab-2a-lastname.docx` (memo plus your labeled Questions & Analysis page) and the exported `skills-lab-2a-lastname.pdf` (memo only). Both files use your own last name.

### Rubric: Skills Lab 2A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s).

---

## 2.7 Review Questions 🔄️

1. **Remember:** Name the four players that deliver a web page (the program, the address, the machine, and the language) and state what each contributes.

2. **Understand:** A friend says "I asked AI, so I already researched it." Explain, in 2-3 sentences, the difference between retrieving ranked pages, generating an answer, and verifying a claim.

3. **Apply:** You are buying a refurbished laptop for school from an unfamiliar site: padlock present, prices moderate, reviews glowing but all posted the same week, payment by card or "Zelle discount." Walk through the checks you would run, in order, and state your decision rule.

4. **Analyze:** Take one claim you saw online this week and run lateral reading on it. Report the claim, your steps, your sources, and your verdict, then compare how the claim's original presentation (tone, polish, popularity) related to what the evidence showed.

---

## Further Reading 📖

* [MDN: How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) - A beginner-level walkthrough of browsers, servers, and page delivery, one level deeper than this chapter.
* [Google: How Search Works](https://www.google.com/search/howsearchworks/) - The search company's own plain-language tour of crawling, indexing, and ranking.
* [Civic Online Reasoning](https://cor.stanford.edu/) - Stanford's free lessons and videos on lateral reading, the method Section 2.2 teaches, with practice examples.
* [Internet Society: Brief History of the Internet](https://www.internetsociety.org/internet/history-internet/brief-history-internet/) - The origin story told by people who were there, from ARPANET to the public Internet.
* [FTC: Online Shopping](https://consumer.ftc.gov/articles/online-shopping) - The U.S. consumer protection agency's checklist for safe online buying, disputes, and refunds.

---

## Looking Ahead ⏩

You can now trace a page to your screen, fact-check what arrives, and put findings on the record. Chapter 3 turns to the applications themselves: the word processors, spreadsheets, and specialized tools you choose among every day, and the AI copilots now riding inside them. The question stops being "what does this tool do" and becomes "which tool fits this task," a decision habit you will use for the rest of the course and your career.
