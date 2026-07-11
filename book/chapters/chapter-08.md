# Chapter 8: Digital Self-Defense: Security, Privacy, and Ethics in the AI Era

The voicemail sounds exactly like Rosa from the roastery. Same warmth, same slight rush, same way she says "Maya, one thing." The message asks Desert Bloom to send this month's payment to a new account, and it needs to happen today because of "a bank switchover." Maya Reyes has paid Rosa's invoices for three years. Her thumb is already moving toward the banking app when a habit from this course taps her on the shoulder: verify before you trust. She calls Rosa back on the number she has always had. Rosa has no idea what she is talking about. The voice on the message was not Rosa. It was software, cloned from a few seconds of Rosa talking on the roastery's own social videos, and it nearly moved a month of payments to a stranger.

Nobody hacked anything in that story. No password fell, no firewall failed, no code ran. The attacker aimed at the person, because the person approves the payments, and the AI era has given that old trick a fluent new voice. This chapter is about that shift. The threats worth studying are not the movie kind. They are the emails, calls, and pop-ups engineered for the moment your attention dips, and the quiet trade in your personal data that makes them easier to aim.

The chapter runs in four moves, and they follow the arc of Part III. First, the data trail: who collects what about you, who sells it, and what rights you have over it. Second, the attacks: social engineering and malware, upgraded by the same AI tools you learned to use in Part I, each one arriving over a road Chapter 7 named. Third, the defense stack: passkeys, multifactor authentication, encryption, updates, and backups, ranked by what they defend against. Fourth, judgment: the ethics of what you copy, what you disclose about AI help, what your devices cost the planet, and, since this is also an Excel course, how to chart data without lying. The Skills Lab turns all of it on the person you can fix first: you.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero), builds on Chapter 7 (networks and roads), Chapter 6 (backups and Excel), and Chapter 4 (accounts and permissions)
* **Deliverables:** Skills Lab 8A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-8.1 (Analyze):** Break down how personal data is collected, traded, and attacked, from data brokers to AI-written scams (Sections 8.1 and 8.2)
* **MLO-8.2 (Evaluate):** Judge which safeguards close which risks, and prioritize the fixes a security audit reveals (Section 8.3)
* **MLO-8.3 (Apply):** Chart audit results in Excel so comparisons read accurately, applying Section 8.4's honesty and disclosure standards to your own work (Section 8.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO VI (Analyze):** Examine system security and privacy risks and the safeguards that reduce them
* **CLO XI (Evaluate):** Judge technology use against ethical and social standards, including the consequences of misuse
* **CLO XIII (Apply):** Produce documents, spreadsheets, databases, and presentations with industry-standard productivity software

---

## 8.1 The Data Trail You Leave

Chapter 3 told you some free products sell your attention or your data, and promised this chapter would examine that price tag. Here is the receipt. Nearly every app, site, and store you touch records the visit: what you looked at, how long, from where, on which device. Your **digital footprint** is the total trail of that data, the parts you posted on purpose and the much larger part collected while you were doing something else.

### Who Collects, and Who Resells

The companies you deal with directly collect data to run their services and to advertise, and most people have made rough peace with that. The industry fewer people know about is the resale layer. A **data broker** is a company whose product is you. It buys and assembles data from apps, retailers, public records, and loyalty programs. It then sells the finished profiles to advertisers, insurers, landlords, and anyone else who pays. You have never heard of most brokers, and none of them have accounts you opened. The profile still exists, and it is detailed enough to guess your income, health worries, and habits.

Why care, if you have nothing to hide? Two honest answers. First, profiles get used to price and screen you: what offers you see, what rates you are quoted, sometimes whether a landlord calls back. Second, that same data is the raw material of the attacks in Section 8.2. A scammer who knows your bank, your school, and your supplier's name writes a message you might believe. Maya's voice-clone call worked as well as it did because the caller knew who supplies Desert Bloom's beans. Privacy is not about hiding. It is about controlling the ammunition.

One misconception needs retiring here, because it gives people false confidence. The browser's private or incognito mode deletes history and cookies from that device when the window closes. That is all it does. The sites you visited, your provider, your school's network, and every account you signed into saw you normally. Private mode hides your trail from the next person who borrows the laptop, not from the Internet.

The two questions from Chapter 4 have been building toward this section all book: what does it see, and where does it go? You asked them about an assistant, then about cloud storage in Chapter 6, which promised this chapter would finish that conversation. Here is the finish: your files on a company's servers live under that company's terms, and the rights below are the leverage you hold over those terms. Ask the two questions now about everything: the loyalty app, the fitness tracker, the smart speaker in the kitchen. You will not always like the answers, and the point is to have chosen, which is what this chapter's audit measures.

### The Rights You Have

The law is catching up to the brokers, unevenly. There is no single United States privacy law. There is a patchwork, and knowing its shape tells you which rights you can use.

* **FERPA** protects education records. Once a student turns 18 or enters college, those rights belong to the student, which means your grades and records here are yours to control.
* **HIPAA** protects health information held by providers, insurers, and their partners. The catch students miss: it covers your clinic, not your fitness app. The same heart-rate data that is protected in a hospital chart is ordinary commercial data in a wellness app's hands.
* **COPPA** restricts collecting data from children under 13, which is why platforms ask for birthdays.
* A growing list of states has passed broader privacy laws in the pattern Europe's **GDPR** set. These laws grant four rights: see what a company holds on you, correct it, delete it, and opt out of its sale. Companies increasingly offer those controls to everyone because separate versions per state cost more than one.

The practical upshot: privacy pages now contain working buttons. "Download your data" and "delete my account" requests are rights in a growing share of cases, not favors. Professionals use them, especially when leaving a service.

### Try It Yourself 8.1: Search Yourself 🛠️

**Predict:** Commit two predictions in writing: what the first page of results shows when a stranger searches your name plus your city, and one thing you hope is not there.

**Run:** Open a private browsing window (so your signed-in history does not shape the results) and run the search. Try your name in quotes, then add your school or workplace. Check the image results too.

**Explain:** In 1-2 sentences, compare the footprint you found to the one you predicted, and name one result you control directly (a profile you could edit or lock down).

### Try It Yourself 8.2: Ask the Two Questions of One App 🛠️

**Predict:** Pick one app you use daily. Commit predictions in writing: which permissions does it hold (camera, microphone, location, contacts), and does it share data with third parties?

**Run:** Check both answers. Permissions live in your phone's privacy settings (Chapter 4's tour). Sharing lives in the app's privacy settings or the app store listing's privacy section, which summarizes what the app collects and links.

**Explain:** In 1-2 sentences, report what it sees and where it goes, and state whether you would grant the same permissions again today.

### Quick Check 8.1 ✅

1. A classmate says "I have nothing to hide, so brokers can have it all." Give the two costs from this section that apply to people with nothing to hide.
2. A friend does their banking in incognito mode "for safety." State what private mode protected them from, and name one thing it did not touch.
3. Match the law to the situation: a professor posting exam scores publicly by student name, a hospital charting app, a tablet game collecting nine-year-olds' locations.

---

## 8.2 How Attacks Work Now

Chapter 7 gave you the map of roads into your life: email over your home connection, texts on the cellular network, calls, ads, downloads. Every attack in this section is traffic on one of those roads. And the headline change of the AI era is not new roads. It is better disguises.

### Social Engineering: Hacking the Person

**Social engineering** is manipulating people into breaking their own security: handing over a password, approving a payment, installing something. It dominates incident reports for one simple reason: asking a person is easier than beating a machine. The classic form is **phishing**, a fraudulent message dressed as a trusted one, fishing for credentials or money. Its variants are named for their roads: **smishing** rides text messages, **vishing** rides voice calls, and **spear phishing** is any of them aimed at one specific person, using details about you to earn belief. The data trail from Section 8.1 is where those details come from.

For years, the standard advice was "look for the typos." That advice is dead, and this course owes you the honest update. A large language model writes flawless, warm, brand-perfect prose in any style, in any language, in one second. Attackers know this. What AI cannot fake is context, so the living tells are about the situation, not the spelling:

* **Urgency on a deadline you did not set.** "Today," "immediately," "before your account closes." Pressure is the attacker's product, because hurry turns off the verification habit.
* **A requested change of channel or destination.** New payment account, new phone number, a link instead of the app you already use, a gift card instead of an invoice.
* **A sender address or link that does not match the name on it.** The display says your bank. The address does not. Chapter 2 taught you to read a URL before trusting it, and that habit now earns its keep.
* **A request the real party would not make.** Your bank does not need your password. IT does not need your sign-in code. Rosa does not change banks by voicemail.

The same generative tools raise two newer threats. A **deepfake** is AI-fabricated audio, video, or imagery of a real person, and **voice cloning**, the audio version, needs only seconds of source material. The defense is not becoming a forensic expert. It is Maya's move: verify through a channel you already trusted before the message arrived. Call the number you had. Walk to the office. Open the app directly instead of tapping the link. Professionals call this out-of-band verification, and it defeats a perfect fake, because it never argues with the fake at all.

One older con still earns its spot from Chapter 4: **scareware**, the pop-up that counts your "437 critical errors" and offers to fix them. Chapter 4 called it bait and promised the hook. Here it is: the "cleaner" is the infection, and the pop-up's real payload is panic. The tell is the same as ever. Real diagnostics do not arrive as ads.

### Malware: Hostile Software on Your Machine

**Malware** is any software built to harm: to steal, spy, encrypt, or hijack. The family names describe behavior, and four cover most of what you will meet. A **virus** attaches to files and spreads when they do. A **trojan** poses as something you want (a free app, a cracked game, that fake cleaner) and does its work after you invite it in. **Spyware** watches quietly, and its nastiest form, the **keylogger**, records what you type, passwords included. **Ransomware** encrypts your files and sells them back to you. It is the one this book has been arming you against since Chapter 6, because an offline, versioned backup turns "pay or lose everything" into "restore and move on." One honest caveat: some crews also steal copies and threaten to publish them, damage no backup undoes, which is why the prevention layers still matter. Law enforcement advises against paying, and payment buys no guarantee.

How does malware arrive? Overwhelmingly, it is invited. Attachments that beg to be opened. Downloads from the open web, which Chapter 3 flagged for exactly this moment: outside a store's vetting, you are the vetting layer. Fake updates from ads instead of real ones from Settings (Chapter 4's update-source rule was malware defense all along). And two platform myths need retiring together: Macs and iPhones get malware too (fewer targets historically meant fewer attacks, not immunity), and phones are computers, which Chapter 1 established on page one.

Two crimes sit at the end of these pipelines. **Identity theft** is using someone's stolen personal data to open accounts, file claims, or commit fraud in their name, and it is the direct monetization of breaches and brokers. And e-commerce fraud is Chapter 2's debt paid: the too-good listing, the storefront that is only a checkout page, the "shipping problem" text after you did order something. The same context tells apply, and the card protections from Chapter 2 (credit over debit online, statements read monthly) are the safety net.

### Try It Yourself 8.3: Two Messages, One Fake 🛠️

**Predict:** Both messages below are typo-free. Read them once, commit your verdict in writing for each (real or scam), and name the tell you used.

> **Message A:** "Sun Valley Credit Union: Your statement is ready. View it anytime in the mobile app or at the branch. Questions? Call the number on the back of your card."

> **Message B:** "Sun Valley Credit Union: Suspicious sign-in detected. Your account will be locked in 2 hours. Verify your identity now at sunvalley-secure-alerts.com to avoid interruption."

**Run:** Test each against the four living tells: manufactured urgency, changed destination, mismatched address, and a request the real party would not make. Count how many each message trips.

**Explain:** In 1-2 sentences, deliver the verdicts, and state what Message B wants you to skip (the out-of-band step: opening the real app or calling the real number yourself).

### Quick Check 8.2 ✅

1. Name each attack: a text about an unpaid toll, a "grandson" call in a matching voice, a mass email to the whole school, and a personal email citing your manager and this week's project.
2. A friend says they can spot phishing "because scam grammar is always bad." Explain what changed, and give them two situational tells that still work.
3. Map each to its Chapter 7 road, then name the defense habit: a fake "free Wi-Fi" network at the airport, and a QR code sticker on a parking meter (Chapter 6 flagged this one).

---

## 8.3 The Defense Stack

No single defense stops everything, which is why professionals stack them: each layer catches some of what slips past the one before. Here is the stack in priority order, each layer tagged with what it defends against. This ranking is also the grading logic of your Skills Lab audit, so read it as the answer key to your own security.

### Layer 1: Accounts. Passwords, Managers, and Passkeys

Most break-ins are sign-ins. A **data breach** is the mass theft of a service's stored user data, and breached password lists circulate for years. Attackers take a leaked email-and-password pair and try it everywhere, which is why reuse is the single most dangerous habit in personal security. One breach anywhere becomes a master key everywhere.

The fix costs one decision. A **password manager** generates, stores, and fills a different strong password for every account, so no two accounts share a fate. You remember one master passphrase, and length beats cleverness: four random words outlast `P@ssw0rd1` by centuries of guessing. Browsers and phones now build managers in, and a dedicated app adds breach alerts that tell you when a stored password appears in a leak.

The next step retires the password altogether. A **passkey** signs you in with the same face, fingerprint, or PIN that unlocks your device, using cryptography under the hood. There is nothing to remember, nothing reused, and, the professional reason to care, nothing to phish: a passkey only works on the real site, so the fake one gets nothing. Where a site offers a passkey, take it.

**Multifactor authentication** (MFA) is the second lock for everything else: after the password, prove yourself once more with an app code, a prompt, or a key. A stolen password alone then fails. Any MFA beats none, app codes beat texted codes (thieves hijack phone numbers), and one account deserves it before all others: your email. Email is where every other account sends its reset links. Whoever holds your inbox holds the keys to the rest of your life, which is why the audit weighs it the way it does.

### Layer 2: Devices and Data. Updates, Encryption, Least Power

Three habits from earlier chapters turn out to have been security layers all along. Updates come first. Chapter 4 taught that a patch's release makes the hole it fixes public knowledge. Automatic updates on the OS, the browser, and the router (Chapter 7) close those doors on a schedule. **Encryption** guards the data itself. HTTPS scrambles traffic in transit (Chapter 2's padlock). Device encryption (BitLocker or Device encryption on Windows, FileVault on Mac, on by default on a locked phone) makes a stolen laptop a brick instead of a filing cabinet. Set a screen lock and the rest mostly follows.

Least power, third: Chapter 4 promised a whole defense built on the least-privilege idea, and this stack is it. Daily work in a standard account means a bad click cannot install what you could not. App permissions kept minimal mean a compromised app sees less. The principle scales from your user account to Saguaro Hall's front desk to every corporation you will ever work for. Give each account the least power that does the job, and a mistake stays small.

The built-in guards deserve their line: modern systems ship an **antivirus** (Microsoft Defender, on by default under Windows Security) and a **firewall**, software that blocks unrequested incoming connections. Leave both on. Buying more is optional. Turning them off is not.

A **VPN** (virtual private network) encrypts all your traffic to a relay before it heads onward, hiding it from the local network. Useful on networks you distrust, and oversold: HTTPS already protects most of what matters, and a free VPN is Chapter 3's rule in costume. If you are not paying, your browsing data is likely the product, which makes a shady free VPN a privacy downgrade wearing a privacy costume.

### Layer 3: The Human Protocol

The layers above are settings. This one is a habit set, and it stopped Maya's voice clone when no setting could have.

* **Slow down on demand.** Urgency is the attack. Any message that needs money, credentials, or a change "right now" has earned a pause, not a click.
* **Verify out-of-band.** Contact the real party through a channel you already had: the saved number, the official app, the address on the card. Never through the message's own link or number.
* **Treat requests for codes as attacks.** No legitimate caller asks you to read back an MFA code. That code is the burglar asking you to hold the door.
* **Check your exposure on schedule.** Breach alerts from your password manager (or a reputable breach-check site) tell you which passwords to rotate. Statements and credit reports catch identity theft early, and a **credit freeze**, free at the three bureaus, blocks new accounts in your name until you thaw it.

### Layer 4: The Safety Net

When ransomware encrypts the laptop anyway, when the phone drowns anyway, the last layer is the one Chapter 6 built: the 3-2-1 backup, with one copy offline and elsewhere. Backups are the only layer that undoes damage instead of preventing it, which is why they anchor the stack.

And when a device leaves your hands, the stack follows it out the door. Chapter 6 drew the line between deleting and wiping: deletion removes the listing, and a wipe (a factory reset with encryption on) makes the data unrecoverable. Cactus Wren wipes every trade-in and says so on the receipt, because the previous owner's tax returns are not part of the sale. Yours are not either. Wipe before you sell, donate, or recycle, and Section 8.4 picks up what happens to the device after that.

!!! tip "Tech in Your Field"
    The defense stack is a job duty in every major here. Nursing and health sciences students will work under HIPAA, where a phished hospital account is a reportable breach and patient trust is the casualty. Their clinical systems live on exactly the networks Chapter 7 mapped. Business and entrepreneurship students inherit Maya's problem: payment fraud aimed at whoever approves invoices, plus custody of customer data that laws increasingly treat as a liability to protect. Public safety and law students will handle evidence whose integrity depends on chain-of-custody discipline, in a world where deepfakes make "the recording proves it" a claim that needs verifying. And visual and performing arts students defend the account that is the business: a hijacked portfolio or channel is a stolen storefront. Different stakes, same stack.

### Try It Yourself 8.4: The MFA Sprint 🛠️

**Predict:** Commit predictions in writing: of your email, your bank, and your most-used social account, how many currently require a second factor at sign-in? Which of the three would hurt most to lose?

**Run:** Check all three in their security settings. While you are in your email's settings, look for a passkey option and note whether one is offered.

**Explain:** In 1-2 sentences, report the count against your prediction, and defend which account you would fix first (this section argued for one in particular).

### Try It Yourself 8.5: Find the Wipe (Do Not Pull the Trigger) 🛠️

**Predict:** Commit a prediction in writing: where on your phone is the factory reset, and what does its warning screen promise about your data?

**Run:** Find the reset screen in Settings and read it carefully. **Do not run it.** Confirm your phone reports encryption is on (it is, on any modern phone with a screen lock).

**Explain:** In 1-2 sentences, explain what this screen would do that dragging files to the trash would not, and when in a device's life this button is the professional move.

### Quick Check 8.3 ✅

1. You open a new bank account tonight. Put these in the order you would do them, and justify the first: enable MFA, let the password manager generate the password, add the account to your monthly statement check.
2. Ransomware hits a freelancer's laptop. Name the one layer that gets the files back, the property it needs for that to work (Chapter 6 taught it), and one reason paying is a bad plan even when affordable.
3. A friend installs a free VPN "so public Wi-Fi is safe now." Evaluate the move in two sentences, using this section's rule about free products and what HTTPS already covers.

---

## 8.4 Integrity: Ethics, AI Disclosure, and Honest Charts

Chapter 2 planted a line this section finishes: something can be legal and still wrong. Security asked "can someone take what is mine?" Ethics asks "what do I owe everyone else?" In a term when AI drafts your prose and your charts argue your case, integrity is a technical skill, and this section treats it as one.

### Whose Work Is It: Copyright, Plagiarism, and AI

**Copyright** is automatic: the moment someone fixes original work in tangible form (a photo, a song, a paragraph, code), the law protects it, no registration or symbol required. Using someone's work generally needs permission, a license, or a recognized exception, and "it was on the Internet" is none of those. Licenses are how permission scales: **Creative Commons** licenses let creators pre-approve uses (the model open textbooks run on), and open-source licenses do the same for code.

**Plagiarism** is the ethics-shaped version of the same offense: presenting someone else's work or ideas as your own. It is not always illegal, and it does not need to be. It ends careers on its own authority. The AI era adds the question Chapter 3 promised this chapter would take up: whose work is an assistant's draft? The rules differ by course and employer, and the professional habits are stable across all of them. Know the policy before you use the tool. Where AI help is allowed, disclose it plainly ("drafted with an AI assistant, verified and edited by me"). Where it is not, do the work. And do not lean on AI detectors to referee any of this. They misfire in both directions, flagging honest writers and missing polished machine text. That is why disclosure (a human telling the truth) beats detection (a machine guessing at one).

Chapter 2 also left a workplace promise here: why hidden copies of mail age badly. BCC has honest uses (protecting a list's addresses), and it has a corrosive one: quietly looping someone into a conversation the other person believes is private. Forwarded threads and screenshots live forever, and "who else was reading" eventually surfaces. The professional rule is transparency's version of 3-2-1: write every message as if it will be read aloud later, to the person it was about, because sometimes it is.

The last piece of citizenship is the oldest: people are on the other end of the wire. **Cyberbullying** (harassment, pile-ons, and account-hijacking pranks carried out through screens) is the same act it is offline, with better reach and worse permanence. The bystander move that costs the least and helps the most is refusing to amplify. The evidence move (screenshots with dates, saved before blocking) turns "it happened" into something a school or platform can act on.

### What the Machines Cost: Sustainable Computing

Chapter 5 called refurbished the greener buy and promised the rest of the story. **E-waste**, discarded electronics, is the world's fastest-growing household waste stream, and the phones and laptops in it carry both recoverable metals and toxic materials that do not belong in landfills. **Green computing** is the practice of cutting computing's footprint, and a student-sized version fits in four habits:

* **Use devices longer.** The greenest device is the one that never had to be manufactured.
* **Buy refurbished where it serves.** Chapter 5's counter conversation was climate advice too.
* **Power-manage what you own:** sleep schedules, sensible brightness, and off when idle for days.
* **Retire hardware properly.** Wipe it (Section 8.3), then donate it or hand it to a certified electronics recycler. Not a drawer, not a dumpster.

The AI era adds a new line to the bill. Training and serving large models runs on data centers that draw serious electricity and cooling water, and the industry's growth is reshaping regional grids, including in Arizona. One query costs little. Billions per day add up. This book has told you what AI tools are good for since Chapter 1, and this is the honest other column. Using them deliberately, for tasks where they earn their cost, is both a professional habit and an environmental one.

### Charts That Tell the Truth

Judgment has a visual form, and it is the last Excel skill of Part III. A **chart** turns numbers into a picture so a pattern becomes visible at a glance, and the same power that reveals patterns can fake them. Chart literacy is therefore two skills: building the right chart, and refusing to build a dishonest one.

Match the chart to the question, the way you match the tool to the task (Chapter 3's rule, drawn instead of installed):

| The question | The chart |
| ------------ | --------- |
| Compare amounts across categories | **Column chart** (or its sideways twin the **bar chart**, better when labels are long) |
| Show change over time | **Line chart** |
| Show parts of one whole | **Pie chart**, and only with a few slices. Beyond that, a bar chart reads better |

Excel makes the mechanics almost free. Select the data including its headers, choose Insert > Recommended Charts, and pick. Every chart then needs its paperwork: a title that states the finding (not "Chart 1" but "Backups lag every other category"), labeled axes, and data labels where exact values matter. A chart with no labeled axes is an opinion in a costume.

Now the honesty rule, on real numbers. The class results that ship in this chapter's data pack average 7.0 in Devices and 3.5 in Backups. In an honest column chart, with the value axis starting at zero, the Devices bar stands twice as tall as the Backups bar, because the number is twice as big. Now doctor the chart: set the axis to start at 3 instead of zero, and the same data shows a Devices bar nearly nine times the Backups bar. Nothing was edited but the frame, and the story went from "twice as strong" to "Backups barely exists." That trick, the truncated axis, is the most common chart lie in the wild, and it works in both directions. A vendor stretches a trivial gap into a cliff. A team shrinks a bad trend into a ripple.

Two rules keep your own charts honest, and Try It Yourself 8.6 makes you break both on purpose so you recognize the crime. Column and bar charts start their value axis at zero, no exceptions, because bars argue by length. And titles plus labels state the comparison plainly, so the picture and the numbers agree in public.

### Try It Yourself 8.6: Make the Chart Lie, Then Confess 🛠️

**Predict:** You will chart the five class category averages from `assets/code/chapter-08/security-audit.xlsx` (ClassResults sheet), then set the axis minimum to 3. Commit two predictions in writing: which category's bar nearly vanishes, and does the doctored chart make the class look better or worse at security overall?

**Run:** On the ClassResults sheet, type the five category names in I1 through M1, and beneath each its average: `=AVERAGE(B2:B55)` in I2 for Accounts, and so on through M2. Select I1:M2, then Insert > Recommended Charts > the first column chart. Then double-click the vertical axis and set Minimum to 3. Look at the two stories. Set it back to 0.

**Explain:** In 1-2 sentences, name what changed and what did not, and state the zero-baseline rule in your own words.

### Quick Check 8.4 ✅

1. A course allows AI assistance with disclosure. One student submits AI-drafted work with a disclosure line. Another submits fully original work run through an "AI detector" that flags it anyway. Judge both situations using this section's disclosure-beats-detection argument.
2. Pick the chart type and one required element: monthly sales for a year, survey results across six majors, one budget split into four spending kinds.
3. A software vendor's column chart shows its product at 99.9% and a rival at 99.3%, with the axis running from 99.0 to 100. Describe what the eye concludes, what the numbers say, and the fix.

---

## 8.5 Summary and Retrieval 💡

### Key Concepts

* Your digital footprint is larger than what you posted, and data brokers assemble and resell it without holding an account you opened. The profile prices you, screens you, and arms the scams aimed at you. Private mode only cleans the local device. The legal patchwork (FERPA, HIPAA, COPPA, GDPR-style state laws) grants real rights: see, correct, delete, opt out. Use the two questions everywhere: what does it see, where does it go.
* Attacks aim at people first. Phishing and its road-named variants (smishing, vishing, spear phishing) now arrive in flawless AI prose, so the living tells are situational: manufactured urgency, changed destinations, mismatched addresses, requests the real party would not make. Deepfakes and voice clones fall to out-of-band verification, not to squinting. Malware's four families (virus, trojan, spyware with its keylogger form, ransomware) are usually invited: attachments, unvetted downloads, fake updates. Every platform is a target.
* Defense is a stack. Accounts first: a password manager ends reuse, passkeys end phishing, and MFA guards everything else, email before all. Devices next: automatic updates, device encryption, screen locks, least privilege, and the built-in antivirus and firewall left on. Then the human protocol: slow down, verify out-of-band, never surrender codes, watch your exposure. Beneath it all, the 3-2-1 backup, the one layer that undoes damage, and the wipe that clears a device before it leaves your hands.
* Integrity is a technical skill. Copyright is automatic and licenses scale permission, plagiarism ends careers without a courtroom, and AI help follows the policy and gets disclosed, because disclosure beats detection. Devices carry a footprint (e-waste, and AI's energy bill), so use longer, buy refurbished, wipe, and recycle certified. Charts argue by length: value axes start at zero, titles state findings, and the truncated axis is a lie you now know how to catch.

### Key Terms

See course glossary for full definitions

* digital footprint, data broker, FERPA, HIPAA, COPPA, GDPR (Section 8.1)
* social engineering, phishing, smishing, vishing, spear phishing, deepfake, voice cloning, scareware, malware, virus, trojan, spyware, keylogger, ransomware, identity theft (Section 8.2)
* password manager, passkey, multifactor authentication (MFA), antivirus, firewall, VPN, credit freeze, data breach (Section 8.3)
* copyright, Creative Commons, plagiarism, cyberbullying, e-waste, green computing, chart, column chart, bar chart, line chart, pie chart (Section 8.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the four living tells of a social-engineered message, and the one verification move that defeats even a perfect deepfake.
2. Name the four malware families from this chapter, plus the keylogger inside one of them, and give one identifying behavior for each.
3. Rebuild the defense stack from memory: the four layers, one tool per layer, and the account that gets MFA first, with the reason.
4. State what a credit freeze does, what a wipe does that deletion does not, and where each belongs in a life event (new lease, selling a laptop).
5. Give the two honest-chart rules and explain, using the class numbers (7.0 versus 3.5), how a truncated axis changes the story.

---

## 8.6 Skills Lab 8A: Score Your Own Security: An Audit in Charts

**Goal:** Run the 25-item security audit on yourself, compare your results against a class-sized baseline with your first cross-sheet formulas, and present the findings in honest charts that justify your two highest-priority fixes.

**Dataset or starter files:** One provided file in `assets/code/chapter-08/` from the course data pack. `security-audit.xlsx` holds two worksheets: `AuditChecklist` (25 items in five categories, with scoring anchors and a blank Your Score column) and `ClassResults` (54 anonymized category scores from the same audit). The folder README is the data dictionary. Download the data pack from Canvas, extract it, and work at the extracted `cis105` root. You will load the provided file, never retype it.

**Scenario:** Section 8.3 handed you the defense stack. This lab finds out where yours stands. You will score yourself honestly, and honesty is safe here: **your security score does not affect your grade.** The rubric grades your formulas, your charts, and your analysis. A truthful 19 out of 50 with a sharp fix-it plan outscores a fictional 48 every time. Notice, too, what the class file does not contain: names. The results are anonymized, which is Section 8.1's lesson applied by whoever built the file.

!!! note
    Excel for the web can complete this lab: charts, cross-sheet formulas, and axis settings all work in the browser, though menus sit in slightly different places. Desktop Excel remains smoother for chart formatting.

### Part 1: Foundation (Aligns with MLO-8.2)

1. Open `security-audit.xlsx` and immediately save your working copy as `skills-lab-8a-lastname.xlsx` (File > Save As), so the pack original stays clean.
2. Read the `AuditChecklist` sheet once, top to bottom: 25 items, five categories, and for each item the anchors that define a 0 and a 2 (1 means partly true). Freeze the top row (View > Freeze Panes > Freeze Top Row).
3. Score yourself. In G2 through G26, enter 0, 1, or 2 for each item, checking the honest answer where the Where to look column points. Two rules: no blanks (unsure means 0, because unverified security is unproven security), and no aspirational scoring (the audit measures today, not your plans).
4. Total it. In F28 type `My total`, and in G28 write the SUM of your 25 scores. In F29 type `Out of`, and in G29 type 50. Sanity-check the total against your sense of the week you just read about.

### Part 2: Application (Aligns with MLO-8.2, MLO-8.3)

1. Build the comparison table. In I1, J1, and K1 type the headers `Category`, `My Score`, `Class Average`. In I2 through I6 type the five category names in checklist order: Accounts, Devices, Network, Backups, Privacy.
2. Fill My Score with SUMs of your five-row category blocks: J2 is `=SUM(G2:G6)` for Accounts, J3 is `=SUM(G7:G11)` for Devices, and so on down to J6 for Privacy (rows 22-26).
3. Fill Class Average with your first cross-sheet formulas. A reference can point at another worksheet by naming it before an exclamation point: K2 is `=AVERAGE(ClassResults!B2:B55)`. Build the matching formula for each category column (C through F), and read the five results. They should land near 6.4, 7.0, 5.7, 3.5, and 4.4.
4. Count your zeros: in I8 type `My zero items`, and in J8 use COUNTIF (Chapter 7's counting-with-a-test) across G2:G26 to count the 0 scores. Those items are your to-do list, and Questions & Analysis will ask about them by ID.
5. Format the table's numbers to one decimal place (Home tab, number group) so your scores and the class averages read cleanly side by side.

### Part 3: Extension (Aligns with MLO-8.3, MLO-8.1)

1. Build the honest chart. Select the comparison table (I1 through K6) and Insert > Recommended Charts > clustered column. Title it with a finding, not a label: name the category where you trail the class most (or lead it, if you do). Confirm the value axis starts at 0, and add data labels.
2. Build the confession chart. Copy the chart (Ctrl+C, Ctrl+V on Windows, Cmd+C, Cmd+V on a Mac), and on the copy set the vertical axis Minimum to 3 (double-click the axis, Axis Options). Retitle the copy `Distorted: axis starts at 3. Do not trust`. Note that any bar whose value sits under 3 vanishes from the copy entirely, which is part of the lie. You have now built the truncated-axis trick on your own data and labeled it as one.
3. Read what the distortion did to YOUR story: which of your gaps grew, which shrank, and whether the doctored version flatters you or indicts you. Keep the answer for Questions & Analysis.
4. Write the priority plan. In I11, write a two-sentence recommendation to yourself naming the two fixes you will make first, each citing a specific item ID from the checklist (for example, SA-03 before SA-13). Wrap the text and widen the cell so it reads cleanly.
5. Add a new worksheet named `Questions & Analysis` (the + beside the sheet tabs). Answer the two questions below in cells A1 and A3 with Wrap Text on.

### Questions & Analysis 🤔

Answer both questions on your `Questions & Analysis` worksheet. These answers carry significant rubric weight.

1. Compare your audit to the class baseline using your own numbers: name your weakest category and the class's weakest (cite your J and K values), and state whether they match. Then defend your two priority fixes from Part 3, and explain why "fix the lowest-scoring category first" is not automatically the right rule. Section 8.3's ranking of the layers, and what each one defends, is your evidence: an account fix can outrank a network fix even when the network number is lower.
2. Your Distorted chart tells a different story than your honest one, using identical numbers. Describe what it did to your largest gap. Name one party who would benefit from publishing a chart distorted in each direction: one that inflates a gap, one that hides a gap. Then state the two rules from Section 8.4 that keep your own charts honest. Close with one sentence connecting chart honesty to this section's larger theme: why disclosure and honest framing are the same professional habit whether the artifact is a chart, a citation, or an AI-assisted draft.

**Submission:** Submit one file: your workbook `skills-lab-8a-lastname.xlsx` with the scored checklist, the comparison table with cross-sheet formulas, both labeled charts (honest and distorted), your priority plan in I11, and the `Questions & Analysis` worksheet. The file name uses your own last name.

### Rubric: Skills Lab 8A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s).

---

## 8.7 Review Questions 🔄️

1. **Remember:** Match each name to its behavior: phishing, vishing, scareware, ransomware, keylogger, deepfake. Behaviors: encrypts files for payment, fabricated media of a real person, fraudulent message fishing for credentials, records keystrokes, fake alert selling fake repairs, voice-call fraud.

2. **Understand:** A customer tells Amir "I deleted all my files, so the laptop is safe to sell." Explain, in terms a customer accepts, what deletion leaves behind, what a wipe with encryption does instead, and why Cactus Wren prints "data wiped and verified" on every refurb receipt. Close with where the machines too broken to resell should go, and why the answer is never the dumpster.

3. **Apply:** A friend reuses one password everywhere, has no MFA anywhere, backs up nothing, and keeps auto-updates on. Choose the first three fixes in order, name the specific risk each closes, and defend why updates did not make your list.

4. **Evaluate:** A department head presents a column chart titled "Incidents down dramatically" with a value axis from 40 to 50, showing last year at 49 and this year at 43. Judge the chart and the claim: what does the framing exaggerate, what would an honest zero-axis version show, and what single question about the data would you ask before drawing any conclusion?

---

## Further Reading 📖

* [CISA: Secure Our World](https://www.cisa.gov/secure-our-world) - The U.S. cybersecurity agency's plain-language home for the passwords, MFA, updates, and backup habits this chapter stacks.
* [FTC: How to Recognize and Avoid Phishing Scams](https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams) - The consumer-protection agency's current guidance, with real reported examples.
* [FIDO Alliance: Passkeys](https://fidoalliance.org/passkeys/) - The industry group behind passkeys explains how they work and where they are supported.
* [EFF: Surveillance Self-Defense](https://ssd.eff.org/) - The Electronic Frontier Foundation's guides to reducing your data trail, tool by tool and situation by situation.
* [EPA: Electronics Donation and Recycling](https://www.epa.gov/recycle/electronics-donation-and-recycling) - Where retired devices should go, and why, from the environmental agency.
* [Microsoft Support: Create a chart from start to finish](https://support.microsoft.com/en-us/office/create-a-chart-from-start-to-finish-0baf399e-dd61-4e18-8a73-b3fd5d5680c2) - The official walkthrough of chart creation, elements, and formatting in Excel.

---

## Looking Ahead ⏩

Part III is complete: you can map how data travels, name the threats riding every road, defend yourself in ranked layers, and make the case with charts that tell the truth. Part IV turns from defense to decisions. Chapter 9 scales the course's businesses up: Desert Bloom becomes three locations and a data problem. You will follow information from the register to the dashboard to the decision, meeting the systems (and now the AI agents) that run that pipeline. The Excel thread grows with the data: sorting and filtering return from Chapter 6, and pivot tables arrive, the tool that answers in seconds what a thousand-row sales sheet will not surrender to scrolling.
