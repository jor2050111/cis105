# Chapter 7: Networks Everywhere: From Wi-Fi to Satellite Internet

Saturday night at Saguaro Hall, and the room is full. Three hundred guests are watching a panel on stage, and eighty more bought tickets to watch from home. Twenty minutes in, the home viewers start posting the same word: frozen. Darnell Brooks checks the Wi-Fi and sees full bars. The bars do not help him, because the bars were never the problem. The venue's Internet plan carries 100 megabits per second downhill into the building and only 10 uphill out of it, and a livestream is an uphill job. The stream dies on a road everyone assumed was wide open.

Monday morning, Darnell does what professionals do after a bad Saturday: he turns the problem into a comparison. Fifty-four Internet plans serve his block, across fiber, cable, 5G home service, DSL, and two kinds of satellite. Somewhere in that pile is the right plan, hiding behind sticker prices, equipment fees, and speed numbers that do not mean what most buyers think they mean. Chapter 6 promised you would choose an Internet plan with formulas instead of vibes. This is that chapter.

Here is the route. First, the roads themselves: the wired and wireless channels that carry data, and why each one has a shape. Second, the on-ramp you rent from a provider, and the numbers on the plan that decide what your connection can do. Third, networks at every scale, from the earbuds in your pocket to the planet-wide network of networks, plus the first habits that keep yours safe. Finally, the Excel thread picks up where Chapter 6 left it. You will meet cell references that fill themselves, one dollar sign that changes everything, and an IF function that turns 54 rows of marketing into a shortlist.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None (chapters teach from zero), builds on Chapter 6 (Excel formulas and functions) and Chapter 2 (how the web delivers a page)
* **Deliverables:** Skills Lab 7A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **7.1 (Understand):** Explain how data travels the wired and wireless channels that connect people, devices, and the cloud (Section 7.1)
* **7.2 (Analyze):** Compare Internet connections and network types using the numbers that describe them: download, upload, latency, and true cost (Sections 7.2 and 7.3)
* **7.3 (Apply):** Build Excel formulas that combine cell references, the fill handle, and the IF function to test options against requirements (Section 7.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO III (Understand):** Explain how networks share resources and support communication in homes and businesses
* **CLO VI (Analyze):** Examine system security and privacy risks and the safeguards that reduce them
* **CLO XIII (Apply):** Produce documents, spreadsheets, databases, and presentations with industry-standard productivity software

---

## 7.1 The Roads Data Travels

A **network** is two or more devices connected so they can share data and resources. You have used networks on every page of this book: Chapter 1's cloud, Chapter 2's web, Chapter 6's sync. What those chapters treated as scenery, this chapter treats as machinery. Every file, call, and coffee order travels a physical path, and each kind of path has a shape: how much it carries, how far it reaches, and what it costs.

### The Wired Roads

Wired channels move data through something you could trip over. The champion is **fiber-optic cable**, hair-thin strands of glass carrying data as pulses of light. Fiber is the fastest road in common use, and it has a trait no other home connection matches: it is usually **symmetric**, meaning uploads run as fast as downloads. Remember Darnell's Saturday. Symmetry is not a luxury spec. It is the difference between watching streams and sending one.

Most of the Internet's long-distance traffic rides fiber, including the undersea cables that link continents. The question in any neighborhood is only how close the glass gets to you. Cable Internet runs the last stretch over the copper coaxial line that once carried cable TV: fast downhill, much slower uphill, and shared with the neighbors. **DSL** runs over old telephone wiring: available almost everywhere phones ever reached, and slow by modern standards. Inside buildings, an **Ethernet** cable is the workhorse: a cheap cord that gives a desk, a printer, or a game console a fast, steady link no one has to share the air with.

### The Wireless Roads

Wireless channels move data by radio, and each one trades range against speed and power.

**Wi-Fi** is wireless networking for one building: your router speaks radio to every device within roughly a house-sized bubble. Here is the misconception this chapter exists to retire: Wi-Fi is not the Internet. Wi-Fi is the last hundred feet. Full bars grade the trip from your couch to the router, and say nothing about the road beyond it. Darnell had full bars over a 10 Mbps uphill road, which is like a six-lane driveway feeding a dirt path.

**Bluetooth** is shorter-range radio for a personal bubble: earbuds, watches, keyboards, and car dashboards, all within about 30 feet, sipping power slowly enough to live on a coin-sized battery. A **cellular network** covers cities and highways from towers, and **5G**, the current generation, is fast enough that carriers now sell it as home Internet. That product, sold as 5G home Internet, is a **fixed wireless access** plan: a receiver in your window replaces a cable into your wall. Its honest fine print is that you share the tower, so speeds breathe with the neighborhood's demand.

One more cellular trick belongs in your kit. A **hotspot** is a phone sharing its cellular connection over Wi-Fi, which turns it into a pocket router for a laptop, a tablet, or a card reader. It is how a food truck sells where no cable reaches, and how a student submits an assignment the night the apartment Wi-Fi dies. The data still rides the phone's cellular plan, so the plan's limits ride along too.

**Satellite Internet** reaches the places wires and towers never will, and its two versions could not behave more differently. Traditional satellites sit in **geostationary orbit** (GEO), parked 22,000 miles up so a dish can point at one spot in the sky. Radio takes about half a second to make that round trip, physics' own fee, before any server even answers. Newer constellations fly in **low Earth orbit** (LEO), a few hundred miles up, cutting that delay to a fraction and finally making satellite service feel like ground service. In the plan sheet you will work with this chapter, the GEO plans sit at 610 to 650 milliseconds of delay and the LEO plans at 40 to 55. Same idea, different altitude, more than ten times the wait.

| Channel | How data travels | Where it wins |
| ------- | ---------------- | ------------- |
| Fiber | Light through glass | Speed, and uploads as fast as downloads |
| Cable | Copper coaxial line | Fast downloads where fiber has not arrived |
| DSL | Telephone wiring | Availability, not speed |
| Ethernet | A cord in the building | Steady links for desks and consoles |
| Wi-Fi | Radio, one building | The last hundred feet to your devices |
| Bluetooth | Radio, one person | Earbuds, watches, accessories |
| Cellular / 5G | Radio from towers | Phones everywhere, homes near capacity |
| Satellite GEO / LEO | Radio from orbit | Reaching past the last road |

### Try It Yourself 7.1: Count Your Radios 🛠️

**Predict:** Your phone is a bundle of wireless channels. Commit a number in writing: how many distinct radios does it carry? Then name the ones you can.

**Run:** Open Settings and hunt: Wi-Fi, Bluetooth, cellular, GPS (Chapter 6 called it a sensor, and it is also a radio receiver), and NFC, the tap-to-pay radio, if your phone pays at registers.

**Explain:** In 1-2 sentences, compare your count to what you found, and name which radio you would lose last and why.

### Try It Yourself 7.2: Wi-Fi Versus Cellular Face-Off 🛠️

**Predict:** You will run a speed test twice on your phone, once on Wi-Fi and once on cellular data. Commit two predictions in writing: which connection wins on download, and whether either upload comes close to its download.

**Run:** Search "speed test" in your browser and run the test on Wi-Fi. Note download, upload, and the delay number (often labeled ping or latency). Turn Wi-Fi off, run it again on cellular, and note all three. (No data plan? Run the test near your router and again two rooms away, and watch what distance does.)

**Explain:** In 1-2 sentences, report which prediction held and which number surprised you most. Keep these numbers. Section 7.2 names them properly.

### Quick Check 7.1 ✅

1. A rural clinic can get 100 Mbps from a GEO satellite plan or 80 Mbps from a LEO plan. The clinic runs video visits all day. Which plan serves it better, and which number (not speed) decides?
2. A friend says "my Wi-Fi is slow" while sitting next to the router with full bars. Using the last-hundred-feet idea, name the more likely suspect and one way to test it.
3. Classify each as a wired or wireless channel, and name its typical range: Bluetooth, Ethernet, fiber, Wi-Fi, cellular.

---

## 7.2 Your On-Ramp: Modems, Routers, and the Numbers on the Plan

Chapter 2 followed a web address from your keyboard to a server and back. This section walks the same trip one layer down, because buying a connection means renting the first mile of that trip, and the plan's numbers describe exactly what you rented.

### The Boxes by the Wall

Two jobs sit between your provider's road and your devices, whether they live in one box or two. The **modem** translates: it converts the provider's signal (light, coaxial, phone line, or radio) into standard networking data. The **router** directs: it takes that one incoming connection and shares it among every device in the building, deciding which traffic belongs to which machine. Home Wi-Fi comes from the router's built-in radio. Offices and larger homes add extra transmitters so the bubble covers every room.

The router also runs the building's private address book. Every connected device gets a local address, while the whole building shares one public address on the Internet. That is why your laptop and phone look like one customer to the outside world: the router is standing at the door, sorting the mail.

### How the Trip Works: Packets, Addresses, and the Phone Book

Data does not travel as one long stream. Everything you send is chopped into **packets**, small labeled pieces that travel independently and reassemble at the destination. A **protocol** is a shared rulebook that lets billions of devices from thousands of makers cooperate, and the Internet's core rulebook is called **TCP/IP**. You never see it work, which is the point. Two rules from it explain most everyday mysteries.

First, every device on the Internet has an **IP address**, a numeric street address that routers use to deliver packets. Second, people do not remember numbers, so the **DNS** (Domain Name System) acts as the Internet's phone book, translating a name like `phoenixcollege.edu` into the IP address behind it. When a page will not load, the problem is somewhere in that chain: your radio link, your router, the provider's road, the phone book, or the server itself. Knowing the chain exists is the first step of every fix.

### The Numbers That Matter

Now the plan sheet. Every Internet plan describes itself with a handful of numbers, and buyers who can read them stop paying for the wrong things.

**Bandwidth** is how much data the connection can move per second, and **broadband** is the general term for always-on, high-bandwidth service. Bandwidth is measured in **Mbps** (megabits per second), and the unit hides a trap: bits are not bytes. Eight bits make one byte, so a 100 Mbps connection moves about 12.5 megabytes of file per second. At 25 Mbps, a 2 GB game update takes about ten and a half minutes. At 300 Mbps, it lands in under a minute. When a download feels slower than the plan promised, do the divide-by-eight check before blaming anyone.

Every plan quotes two bandwidth numbers, and the second one is the forgotten one. Download is the road into your building: streaming, browsing, updates. Upload is the road out: video calls, cloud backups, posting content, and livestreams. Wired plans other than fiber are built lopsided because homes historically consumed more than they sent. Then working life moved onto video calls, and Chapter 6's cloud sync started pushing your files uphill all day. Chapter 6's storage table said cloud speed "depends on your connection." This is the dependency: sync rides your upload, and a thin upload makes the cloud feel slow no matter what you pay for download.

**Latency** is the delay before data starts moving: the round-trip time for a packet, measured in milliseconds (ms). Bandwidth is how wide the road is. Latency is how long the first car takes to arrive. Streaming a movie forgives high latency because the player buffers ahead. A video call does not, because conversation cannot buffer. Neither can gaming, or the hybrid Q&A session that made Darnell's Saturday miserable. This is why those GEO satellite plans, whatever their bandwidth, cannot host a natural conversation: half a second of physics sits between every question and its answer.

One more number hides in the fine print: the **data cap**, a monthly limit on how much you can move before the provider slows or charges you. Caps show up most on satellite and some 5G home plans. A capped plan can be a fine deal for light use and a monthly cliff for a family of streamers, which is why the cap column belongs in any honest comparison.

### Buying Without the Sales Pitch

Advertised speeds begin with the words "up to," and the honest way to read them is as a ceiling, not a promise. Cable slows at 7 p.m. when the neighborhood gets home. Fixed wireless breathes with tower load. The speed test you ran in Try It Yourself 7.2 is the tool that keeps everyone honest: run it at the hours you care about, and compare what you measured to what you bought.

Since 2024, United States providers must publish a **broadband label** for every plan: a standardized fact sheet, modeled on nutrition labels, listing the monthly price, every added fee, typical speeds, and typical latency. The label exists because the sticker price and the real bill are different numbers. A plan advertised at $30 with a $15 monthly equipment fee costs $45, every month, and the cheapest sticker in a market is routinely not the cheapest bill. In this chapter's plan sheet, that exact trap is waiting: the lowest advertised price and the lowest true cost belong to two different plans, and Skills Lab 7A makes the grid expose it.

!!! tip "Tech in Your Field"
    The plan numbers in this section are operating decisions in every major here. Nursing and health sciences students will run telehealth visits where upload and latency decide whether a remote exam works, and home health monitors quietly stream vitals over patients' connections. Business and entrepreneurship students will pick the plan behind the card reader, because a point of sale with no connection is a store that cannot sell. Visual and performing arts students price upload the way truckers price diesel: a livestreamed show or a portfolio upload rides the number nobody advertises. And public safety students will file body-cam footage and field reports over cellular links chosen by the agency for coverage, not price. The professional does not memorize the plans. The professional reads the numbers.

### Try It Yourself 7.3: Read a Real Label 🛠️

**Predict:** Pick any Internet provider you have heard of. Commit two predictions in writing: whether its advertised price includes equipment fees, and whether its typical upload is more or less than one quarter of its typical download.

**Run:** Search the provider's name plus "broadband label" (or open a plan page and look for "Broadband Facts"). Read the label: price, fees, typical download, typical upload, typical latency.

**Explain:** In 1-2 sentences, report the true monthly cost versus the advertised one, and the download-to-upload ratio. You just did by hand what your formulas will do 54 times in the lab.

### Quick Check 7.2 ✅

1. A classmate on a 100 Mbps plan downloads a 25 MB file and times it at about two seconds. They feel cheated because "100 should move 100." Check their math with the bits-versus-bytes rule and give the verdict in one sentence.
2. A household runs three video calls at once, every weekday. Rank the three numbers from this section (download, upload, latency) by how much they matter to that household, and defend your top pick.
3. Plan A advertises $30 with a $15 equipment fee. Plan B advertises $40, fee included. State each plan's true monthly cost, then state the general rule about sticker prices this comparison teaches.

---

## 7.3 Networks at Every Scale: From Your Pocket to the Planet

Networks come in sizes, and the sizes have names. Learning them is not vocabulary for its own sake. Each scale answers a different question: who owns it, what it shares, and where its problems get fixed.

### Four Sizes of Network

A **PAN** (personal area network) is the bubble around one person: your phone, earbuds, and watch, usually linked by Bluetooth. A **LAN** (local area network) covers one building or campus under one owner: your apartment's router and everything on it, a coffee shop's registers and printer, a college's labs. A **MAN** (metropolitan area network) spans a city, the scale of a transit system's stations or a district's campuses. A **WAN** (wide area network) crosses regions by linking smaller networks together, and the Internet is the WAN of WANs: the planet's network of networks, which no one owns and everyone connects to.

The scales nest. Your earbuds (PAN) hang off your phone, which sits on your apartment's LAN, which reaches the world through your provider's WAN. When something breaks, professionals ask which ring failed: the earbud pairing, the Wi-Fi, or the road out of the building? That one habit, locating the failure ring, turns "the Internet is down" into a fixable sentence.

### Who Serves Whom: Two Ways to Share

Networks exist to share resources: one printer for a whole office, one plan for a whole family, one file for a whole team. The sharing runs on two arrangements.

In a **client/server network**, dedicated machines (servers) hold the resources and everyone else (clients) asks for them. You met the pattern in Chapter 2: your browser asks, a web server answers. The same shape runs email, cloud storage, and every app with an account. Servers make sharing manageable: one place to secure, back up, and fix. In a **peer-to-peer network**, devices trade directly with no boss in the middle. Your phone AirDropping a photo to a friend's laptop is peer-to-peer, and so are the earbuds in your PAN. Small, quick, and simple, and exactly wrong for anything that needs central control.

The arrangement is a job description, not a machine type. Maya's Desert Bloom register is a client of her cloud point-of-sale service all day, and becomes a peer for ten seconds when it beams a receipt to a customer's phone.

### The Machines That Joined Themselves

Chapter 1 promised this chapter would show how the quiet little computers connect, and here they are. A **smart home** is a LAN where the thermostat, doorbell, plugs, and speakers are all clients: sensor bundles with radios, reporting to apps and taking commands. Businesses run the same pattern at fleet scale. Saguaro Hall's thermostats log every room, and Cactus Wren's security cameras watch the shop, all riding the same network as the registers.

Two facts about that crowd matter this early. First, some of these devices think for themselves now. **Edge computing** means processing data on or near the device instead of shipping everything to the cloud: the doorbell that recognizes motion locally and uploads only the clip that matters. The NPU story from Chapter 5 is edge computing in your laptop. Second, every one of those devices is a door onto your network, and too many of them ship with the same password as every other unit in the store. That is a Chapter 8 problem, and you now know why it lives on a Chapter 7 map.

### First Locks on Your Own Network

Chapter 8 covers defense properly. But three network habits belong here, because they are settings on the router you now understand:

* **Turn on the network's encryption.** **WPA3** (or its older sibling WPA2) scrambles Wi-Fi traffic so nearby strangers cannot read it, and it is the difference between a network with walls and one with curtains. Every router offers it. Verify yours uses it.
* **Change the router's own password.** The admin password that came printed on the box is public knowledge. A router still wearing it can be reconfigured by anyone who reaches it. This is Chapter 4's default-settings lesson, one box further out.
* **Give guests and gadgets their own lane.** A **guest network** is a second Wi-Fi name the router hosts, kept separate from your own devices. Visitors browse without touching your machines, and it is the right parking spot for smart-home gadgets whose security you cannot vouch for.

Update the router's software on schedule, too. Chapter 4's patching rule did not stop applying just because the computer is shaped like a shoebox with antennas.

### Try It Yourself 7.4: Map Your Own LAN 🛠️

**Predict:** Commit a number in writing: how many devices are on your home network right now? Count in your head: phones, laptops, TVs, consoles, speakers, plugs, doorbells.

**Run:** Check the truth. Your router's app (or its status page) lists connected devices. No access to the router? Census by hand, room by room, and check whether a guest network is broadcasting alongside the main one.

**Explain:** In 1-2 sentences, compare the count to your prediction, and name which devices you had forgotten were computers on your network.

### Try It Yourself 7.5: Sort the Servers from the Peers 🛠️

**Predict:** For each, commit a guess: client/server or peer-to-peer? (a) Watching a show on a streaming service. (b) AirDropping photos to a friend. (c) Sending an email. (d) Your earbuds playing your phone's audio.

**Run:** Reason through each one, or discuss with a classmate: is there a dedicated machine in the middle holding the resource, or are two devices trading directly?

**Explain:** In 1-2 sentences, state the question you asked to classify them, and why email involves servers even though it feels person-to-person.

### Quick Check 7.3 ✅

1. Place each on its scale: PAN, LAN, MAN, or WAN. The items: a fitness band paired to a phone, a campus computer lab, a transit system's citywide station network, and the connection between Phoenix and a server in Ohio. Add one more: a food truck's card reader riding its owner's phone.
2. A five-person design studio keeps project files on each person's laptop and trades them by AirDrop. Deadlines keep finding stale versions. Name the network arrangement they are using, the one they need, and what the switch buys them.
3. A neighbor's new smart doorbell and plugs all joined the main home Wi-Fi. Using this section's habits, name two settings changes you would recommend first and one sentence of reasoning for each. Then name the pattern the doorbell uses when it recognizes motion on the device and uploads only the clip.

---

## 7.4 Formulas That Decide: References and the IF Function

Chapter 6 taught the grid to total a column. This section teaches it to reason: to compute a new fact for every row, and then to pass judgment on each one. These two moves, filled formulas and the IF function, are what turn Darnell's 54-plan pile into a decision.

Open the lab file for this chapter, `assets/code/chapter-07/internet-plans.xlsx`, and look at the columns: each plan's download, upload, latency, advertised price, equipment fee, and data cap. Everything below runs on that sheet.

### References That Travel: The Fill Handle

Section 7.2 taught that a plan's real bill is the advertised price plus the equipment fee. In the sheet those live in columns H and I, so the first plan's true cost is one formula in cell K2:

```text
=H2+I2         shows 45 (row 2's $45 price + $0 fee)
```

Now the move that makes spreadsheets scale. Select K2 and find the **fill handle**, the small square at the cell's lower-right corner. Drag it down and Excel copies the formula into each row, adjusting the references as it goes: K3 becomes `=H3+I3`, K4 becomes `=H4+I4`, all the way down. One formula, 54 true costs, four seconds.

That adjusting behavior has a name. A **relative reference** like `H2` means "the cell two columns left of me," so when the formula moves down a row, the reference moves with it. This is exactly what you want when every row should do the same job on its own data, and it is the default. The fill handle plus relative references is how professionals avoid typing a formula 54 times, and why Chapter 6 called hand-typed totals the original sin of spreadsheets.

### The Dollar Sign That Locks: Absolute References

Sometimes a formula needs one foot planted. Suppose Darnell wants each plan's cost over a planning horizon, and he keeps the horizon in one cell, Q1, set to 12 months. The obvious formula in L2 is `=K2*Q1`, and it works, for exactly one row. Fill it down and disaster arrives quietly: L3 becomes `=K3*Q2`, and Q2 is not the horizon. The reference to Q1 slid downhill with the fill, because relative references always do.

The fix is the **absolute reference**: dollar signs that pin a reference so filling cannot move it.

```text
=K2*$Q$1       fills down as =K3*$Q$1, =K4*$Q$1, ...
```

Read `$Q$1` as "exactly Q1, always." The dollar sign here has nothing to do with money. It is a lock, and it comes with a habit worth naming: the shared-assumption cell. When many formulas depend on one value (a horizon, a tax rate, a budget), keep that value in one labeled cell and lock every reference to it. Change Q1 from 12 to 24 and every row's horizon cost doubles instantly, which is Chapter 6's live-grid promise paying off at scale.

### IF: The Formula That Judges

`SUM` and `AVERAGE` compute amounts. The **IF function** computes a verdict. Give it a test, a result for true, and a result for false:

```text
=IF(F2>=20, "Streams fine", "Too slow")
```

Row 2's upload is 50 Mbps, so the test `F2>=20` is true and the cell shows `Streams fine`. Filled down the column, the formula grades all 54 plans in one gesture, and 28 of them pass. The test in the middle is called a **logical test**, and it can compare any cell against any value or any other cell.

Verdicts get sharper when tests combine. Wrapping tests in `AND()` requires all of them to pass, which is how a buyer's whole checklist becomes one column:

```text
=IF(AND(E2>=300, F2>=30, G2<=100, J2="Unlimited"), "Yes", "No")
```

That formula is Saguaro Hall's Saturday, translated: download at least 300, upload at least 30, latency at most 100 ms, and no cap. Filled down the sheet it says Yes exactly 13 times, and the lab will make you find them. One habit before you trust any IF column: test the boundary. A plan with an upload of exactly 20 passes `F2>=20` and fails `F2>20`. Off-by-one verdicts look fine and grade wrong, so check a row where the value equals the threshold and confirm the verdict you intended.

### Try It Yourself 7.6: Watch the Address Move 🛠️

**Predict:** In the lab file, you will put `=H2+I2` in K2 and fill it down two rows. Commit two predictions in writing: what formula will K3 contain, and what value will K4 show? (Row 3 is a $55 plan with no fee. Row 4 is a $65 plan with no fee.)

**Run:** Work in a throwaway copy of `internet-plans.xlsx` (the lab restarts from a clean original). Type the formula, fill down with the fill handle, and click K3 and K4 to read their formulas in the formula bar.

**Explain:** In 1-2 sentences, describe what the fill handle did to the row numbers and why that behavior is the right default.

### Try It Yourself 7.7: Break the Lock, Then Fix It 🛠️

**Predict:** In your throwaway copy from Try It Yourself 7.6, set the stage: type 12 in Q1 (a planning horizon) and 100 in Q2 (a budget). You will put `=K2*Q1` in L2 and fill it down two rows. Commit a prediction in writing: what goes wrong in L3 and L4, and what will each show? (K3 is 55 and K4 is 65.)

**Run:** Fill it and read the damage: L3 computes `=K3*Q2`, which is 55 times the budget, and L4 multiplies by an empty cell. Now fix L2 to `=K2*$Q$1` and fill again.

**Explain:** In 1-2 sentences, state what the dollar signs changed, and give the rule for when a reference must be absolute.

### Quick Check 7.4 ✅

1. A treasurer builds `=B2*C1` where C1 holds the club's dues rate, then fills it down 30 rows and gets zeros everywhere below row 2. Diagnose the bug in one sentence and write the corrected formula.
2. Write the IF formula that shows "Call-ready" when the latency in G2 is 100 or less and "Laggy" otherwise. Then state what a plan with latency of exactly 100 shows, and why.
3. Chapter 6 sorted and filtered to find answers. This section computed new columns instead. For Darnell's 54-plan decision, explain in one sentence why he needs both.

---

## 7.5 Summary and Retrieval 💡

### Key Concepts

* Data travels channels with shapes. Fiber is fastest and symmetric, cable is fast-down slow-up, DSL is available and slow, and Ethernet steadies the desk. Wireless trades range for speed. Bluetooth wraps a person, and Wi-Fi covers a building: the last 30 feet, never the Internet itself. 5G covers cities and now sells as fixed wireless home service. Satellite reaches past the last road, with GEO paying half a second of physics that LEO constellations avoid.
* Your on-ramp is rented machinery plus fine print. The modem translates the provider's signal, the router shares it and runs the building's addresses, packets carry everything under the TCP/IP rulebook, and DNS turns names into IP addresses. The plan's numbers divide the work: download for consuming, upload for calls, sync, and streams, latency for anything conversational, and the data cap for how much month your plan can hold. True cost is the advertised price plus every fee, and the broadband label exists because those differ.
* Networks nest by scale: PAN, LAN, MAN, WAN, with the Internet as the network of networks. Resources are shared client/server (a dedicated machine holds them) or peer-to-peer (devices trade directly), and the arrangement is a job, not a machine. Smart homes and IoT fleets put dozens of quiet clients on your LAN, some thinking locally at the edge, every one of them a door. First locks: WPA3 encryption, a changed router password, a guest network for visitors and gadgets, and router updates on schedule.
* The grid reasons row by row. Relative references travel when filled, which scales one formula to 54 rows. Absolute references (`$Q$1`) lock a shared assumption so filling cannot bend it. IF turns a logical test into a verdict, AND stacks a whole checklist into one column, and boundaries deserve a test of their own.

### Key Terms

See course glossary for full definitions

* network, fiber-optic cable, symmetric, DSL, Ethernet, Wi-Fi, Bluetooth, cellular network, 5G, fixed wireless access, hotspot, satellite Internet, geostationary orbit, low Earth orbit (Section 7.1)
* modem, router, packet, protocol, TCP/IP, IP address, DNS, bandwidth, broadband, Mbps, latency, data cap, broadband label (Section 7.2)
* PAN, LAN, MAN, WAN, client/server network, peer-to-peer network, smart home, edge computing, WPA3, guest network (Section 7.3)
* fill handle, relative reference, absolute reference, IF function, logical test (Section 7.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the six connection technologies from this chapter's plan sheet and one buying fact about each.
2. Explain the difference between bandwidth and latency using the road metaphor, and name one task that punishes each when it is bad.
3. Recite the chain a web request travels, from your device's radio to a faraway server, naming the boxes and translations along the way.
4. Write, from memory, the formula for row 2's true monthly cost, and the version of `=K2*Q1` that survives being filled down 54 rows.
5. State the three router habits from Section 7.3 and what each one defends against.

---

## 7.6 Skills Lab 7A: Let Formulas Do the Math: Choosing an Internet Plan

**Goal:** Turn a 54-plan comparison sheet into a defensible recommendation for Saguaro Hall, using filled formulas, one locked assumption cell, and IF verdicts, so the winner is computed instead of guessed.

**Dataset or starter files:** One provided file in `assets/code/chapter-07/` from the course data pack. `internet-plans.xlsx` holds 54 Internet plans on a worksheet named `InternetPlans`: provider, technology, plan name, download, upload, latency, advertised price, equipment fee, and data cap. The folder README is the data dictionary. Download the data pack from Canvas, extract it, and work at the extracted `cis105` root. You will load the provided file, never retype it.

**Scenario:** After the Saturday stream failure, Darnell Brooks wants a plan that can host a hybrid event without flinching. His requirements: download at least 300 Mbps, upload at least 30 Mbps, latency at most 100 ms, and no data cap. Among plans that clear all four bars, the lowest true monthly cost wins. The venue's current plan is in the sheet (IP-120), so your workbook will also show him exactly what he is escaping.

!!! note
    Excel for the web can complete this lab (open the file from OneDrive). The fill handle, absolute references, and IF all work in the browser. Desktop Excel remains smoother, and Chapter 12's macro work will require it.

### Part 1: Foundation (Aligns with Objective 7.3)

1. Open `internet-plans.xlsx` and immediately save your working copy as `skills-lab-7a-lastname.xlsx` (File > Save As), so the pack original stays clean.
2. Look before you compute. Scroll all 54 rows once and read the six technologies in column C. Find the venue's current plan, IP-120, and note its download, upload, and equipment fee for later.
3. Freeze the header row (View > Freeze Panes > Freeze Top Row).
4. Format columns H and I as currency (select their data, Home tab, currency format). Widen any column that shows `###`.
5. Add the first computed column. In K1 type the header `True Monthly Cost ($)`. In K2 write the formula that adds row 2's advertised price and equipment fee, then fill it down through row 55 with the fill handle. Format the column as currency. Spot-check one row by mental math before moving on.

### Part 2: Application (Aligns with Objectives 7.2 and 7.3)

1. Build the assumptions block. In P1 type `Planning horizon (months)` and in Q1 type `12`. In P2 type `Monthly budget ($)` and in Q2 type `100`. Labeled assumption cells are the shared-value pattern from Section 7.4.
2. In L1 type `Cost Over Horizon ($)`. In L2 write the horizon formula with the reference to Q1 locked absolute, fill it down, and format as currency. If any row shows a wildly oversized number or a zero, you have relived Try It Yourself 7.7: fix the lock and refill.
3. In M1 type `Cost per Mbps ($)`. In M2 divide row 2's true monthly cost by its download speed, fill down, and format as currency. Note which plan lands cheapest per Mbps and which most expensive. Review Question 4 returns to this ranking, and the two ends of it are a lesson in denominators.
4. In N1 type `In Budget?`. In N2 write an IF that shows `Yes` when the true monthly cost is at or under the budget in Q2 (locked absolute) and `No` otherwise, then fill down. Count the Yes verdicts with `=COUNTIF(N2:N55,"Yes")` in N57 (COUNTIF counts the cells that match a value, Chapter 6's counting family with a test attached).
5. Prove the assumption cells earn their keep: change Q1 to 24 and watch column L double, then set it back to 12. Change Q2 to 60 and watch the Yes count fall, then set it back to 100. Those two moments are the proof that one labeled assumption cell beats fifty-four edits.

### Part 3: Extension (Aligns with Objectives 7.1 and 7.2)

1. Format the data plus your new columns as an Excel table named `Plans`. Click any cell inside the plan rows (B2 works), then Home > Format as Table, confirm headers, and set the name on the Table Design tab. Sort by Advertised Price, smallest first, and record the top plan's ID and true cost. Then sort by True Monthly Cost, smallest first, and record the new top plan. You have caught the sticker trap: keep both plan IDs for Questions & Analysis.
2. Add the venue verdict. In O1 type `Meets Venue Needs`. In O2 write the IF with AND from Section 7.4: download at least 300, upload at least 30, latency at most 100, and a Data Cap equal to `Unlimited`. Confirm the table filled the whole column for you. Filter it to Yes and count the qualifiers (the status bar or a COUNTIF both work).
3. Crown the winner. With the filter still on, sort by True Monthly Cost, smallest first, and identify the cheapest qualifying plan. Compare it honestly to the runner-up: what does the next $10 per month buy? Then spare one glance for a near-miss: IP-135 (Surge 500) undercuts most of your qualifiers and clears every bar except one. Find the column that killed it, and notice that caps disqualify plans that look perfect everywhere else.
4. Clear all filters and confirm all 54 rows return.
5. Write the recommendation. In R2, write Darnell a two-sentence recommendation naming the winning plan and its true monthly cost. State in plain terms what it fixes about IP-120: compare their uploads, and name the channel difference behind them. Wrap the text (Home > Wrap Text) and widen the cell so it reads cleanly.
6. Add a new worksheet named `Questions & Analysis` (the + beside the sheet tab). Answer the two questions below in cells A1 and A3 with Wrap Text on.

### Questions & Analysis 🤔

Answer both questions on your `Questions & Analysis` worksheet. These answers carry significant rubric weight.

1. Your two Part 3 sorts crowned different plans: the lowest sticker price and the lowest true monthly cost. Name both plans with their IDs and your computed K-column values, and explain how a $30 plan loses to a $40 plan. Then explain why even the true-cost champion cannot serve Saguaro Hall, citing the specific columns that disqualify it. End with the one-sentence rule you would give any buyer about advertised prices.
2. Your venue filter left a shortlist, and your sort crowned the cheapest qualifier, a plan that clears the 300 Mbps download bar with nothing to spare. The next plan up costs $10 more per month for far more headroom. Make the call: which one do you sign, and why, in terms of what a room full of connected guests does to a network? Then name one factor that matters to this decision that no column in the sheet measures, and say how Darnell could check it before signing.

**Submission:** Submit one file: your workbook `skills-lab-7a-lastname.xlsx` with the computed columns K through O, the assumptions block, the `Plans` table, your recommendation in R2, and the `Questions & Analysis` worksheet. The file name uses your own last name.

### Rubric: Skills Lab 7A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s). Your instructor sets
the point weights in your course. The criteria and levels are the
same everywhere.

---

## 7.7 Review Questions 🔄️

1. **Remember:** Match each technology to its defining trait: fiber, cable, DSL, 5G home, GEO satellite, LEO satellite. Traits: shares a tower with the neighborhood, symmetric speeds, rides old phone lines, half a second of physics, orbits low enough for calls, fast down but slow up over TV-era lines.

2. **Understand:** A friend's video calls stutter even though a speed test shows 200 Mbps download. Using two other numbers from this chapter, explain what the speed test's download figure failed to rule out, and which of the two you would check first for a call problem.

3. **Apply:** A student apartment weighs two plans: 300 Mbps cable at $50 plus a $14 equipment fee, or 150 Mbps fiber at $60 with no fee. Compute both true monthly costs, then choose for a household of three streamers, one of whom uploads gameplay videos nightly. Defend the choice with the numbers that decided it.

4. **Evaluate:** Darnell's neighbor looks at your finished lab workbook and says the venue should buy the 2,000 Mbps plan "because your own sheet shows it has the best cost per Mbps." Judge the advice. Use the difference between a good denominator and a good decision, and name what the venue's requirements say the extra 1,700 Mbps would be worth.

---

## Further Reading 📖

* [FCC: Broadband Consumer Labels](https://www.fcc.gov/broadbandlabels) - The federal rule behind the labels you read in Try It Yourself 7.3, with samples of the label format.
* [FCC: Household Broadband Guide](https://www.fcc.gov/consumers/guides/household-broadband-guide) - The regulator's plain-language table of how much speed common household loads need.
* [MDN: Understanding Latency](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Understanding_latency) - A developer-grade but readable explanation of the delay number and what inflates it.
* [Microsoft Support: Excel help and learning](https://support.microsoft.com/en-us/excel) - The official reference for the fill handle, cell references, IF, AND, and COUNTIF.

---

## Looking Ahead ⏩

You can now read the roads: every channel data travels, every number on the plan, and every scale of network your life runs across. Chapter 8 follows the traffic. Every threat in it arrives over a road this chapter named, and the AI era has made the attackers faster writers. You will meet the defense stack (passkeys, multifactor authentication, encryption, updates, and the backups Chapter 6 already gave you), and Chapter 4's two assistant questions finally get their full answer. The Excel thread adds charts, because a defense you can measure is a defense you can argue for.
