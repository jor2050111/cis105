"""Generate the Chapter 10 Skills Lab data pack (Airtable: From CSV to
Connected Base).

Two CSV files describe Saguaro Hall, the downtown Phoenix event venue
run by Darnell Brooks (introduced in Chapter 4):

* saguaro-bookings.csv    the flat "before": one row per event booking,
                          with the customer's email and phone COPIED onto
                          every row (the denormalization students fix by
                          linking a Customers table)
* saguaro-customers.csv   the clean dimension: one row per organization,
                          the contact details stored once

Base seed 105 (documented in HANDOFF.md). CSV text is written
deterministically, so every run is byte-identical.

Engineered properties (each verified by an assert below):
* Bookings clears the 50-by-5 floor (60 rows x 13 columns). Customers is
  a companion dimension table (24 rows x 6 columns), like the Chapter 8
  audit checklist.
* Referential integrity: every booking's Organization exists in the
  Customers table, so an Airtable link field matches cleanly with no
  phantom records.
* Repeat business: the top organization books 6 times and several book
  more than once, so "which organizations booked more than once" (the
  Chapter 3 promise) has a real answer the link makes visible.
* The contact email copied onto every booking always matches the
  Customers table (email is a stable key). The copied phone matches too,
  EXCEPT exactly one booking row where a digit drifted: the classic
  hazard of copying data instead of pointing at it.
* Quoted Price equals space rate x hours + package fee + add-on fees
  exactly, so every price is explainable and the total is reproducible.
* Exactly two bookings exceed their space's capacity (a feasibility flag
  students can spot), and all four booking statuses appear.

Rebuild:  python3 assets/code/_generators/generate_chapter10_data.py
"""

import csv
import hashlib
import io
import random
from datetime import date, timedelta

BASE_SEED = 105
BOOKINGS_PATH = "assets/code/chapter-10/saguaro-bookings.csv"
CUSTOMERS_PATH = "assets/code/chapter-10/saguaro-customers.csv"

# The status date: the day the venue pulled this export. Events before it
# that were not cancelled read as Completed; later ones are Confirmed or
# still Pending. Fixed so the status mix is deterministic.
STATUS_DATE = date(2026, 7, 1)

# Three rentable spaces, each with an hourly rate and a guest capacity.
SPACES = {
    "Main Hall": {"rate": 200, "capacity": 300},
    "Courtyard": {"rate": 150, "capacity": 150},
    "Meeting Room": {"rate": 60, "capacity": 40},
}

# Package fees on top of the room rate.
PACKAGES = {"Bronze": 0, "Silver": 350, "Gold": 750}

# Optional add-ons (an Airtable multiple-select field on import).
ADDONS = {
    "AV Package": 150,
    "Catering": 500,
    "Decor": 300,
    "Extra Staff": 200,
    "Parking": 100,
}

BOOKING_HEADERS = ["Booking ID", "Event Date", "Space", "Organization",
                   "Contact Email", "Contact Phone", "Event Type",
                   "Guest Count", "Hours", "Package", "Add-Ons",
                   "Status", "Quoted Price"]

CUSTOMER_HEADERS = ["Organization", "Contact Name", "Email", "Phone",
                    "Member Since", "Notes"]

# The 24 organizations that rent Saguaro Hall. Each row:
# (Organization, Contact Name, Email, Phone, Member Since, Notes,
#  booking_count, preferred_space, [event types], (guest_lo, guest_hi)).
# Booking counts sum to 60. The recurring course cast (Desert Bloom
# Coffee, Cactus Wren Repair, the college bookstore) appears as clients.
ORGS = [
    ("City of Phoenix Parks and Rec", "Priya Raman",
     "events@phoenixparks.gov", "602-555-0110", 2019,
     "Civic partner, standard rate", 6, "Courtyard",
     ["Community Meeting", "Market", "Fundraiser"], (60, 140)),
    ("Phoenix Camera Club", "Hector Villaseñor",
     "hello@phxcameraclub.org", "602-555-0121", 2020,
     "Repeat client, prefers weeknights", 5, "Meeting Room",
     ["Workshop", "Networking"], (12, 38)),
    ("Valle Verde High School", "Dana Whitfield",
     "activities@valleverde.edu", "602-555-0132", 2021,
     "Nonprofit rate applies", 4, "Main Hall",
     ["Fundraiser", "Concert"], (120, 280)),
    ("Roosevelt Row Arts", "Marcus Bell",
     "book@rooseveltrow.org", "602-555-0143", 2019,
     "Arts district partner", 4, "Courtyard",
     ["Market", "Concert", "Networking"], (80, 150)),
    ("Desert Bloom Coffee", "Maya Reyes",
     "maya@desertbloomcoffee.com", "602-555-0154", 2022,
     "Loyalty-member events", 3, "Meeting Room",
     ["Networking", "Workshop"], (20, 40)),
    ("Sonoran Small Business Alliance", "Grace Okonkwo",
     "team@sonoranbiz.org", "602-555-0165", 2020,
     "Monthly mixers", 4, "Courtyard",
     ["Networking", "Conference"], (50, 120)),
    ("Grand Canal Rotary", "Tomás Delgado",
     "club@grandcanalrotary.org", "602-555-0176", 2018,
     "Charter member", 4, "Main Hall",
     ["Fundraiser", "Community Meeting"], (90, 200)),
    ("Phoenix College Bookstore", "Elena Fuentes",
     "store@phoenixcollege.edu", "602-555-0187", 2021,
     "Campus partner", 2, "Meeting Room",
     ["Workshop", "Market"], (25, 40)),
    ("Cactus Wren Repair", "Amir Haddad",
     "hello@cactuswrenrepair.com", "602-555-0173", 2023,
     "Tech-help nights", 2, "Meeting Room",
     ["Workshop"], (15, 35)),
    ("Las Artes Folklórico", "Rosa Jiménez",
     "info@lasartesfolklorico.org", "602-555-0198", 2019,
     "Cultural performances", 2, "Main Hall",
     ["Concert", "Quinceañera"], (150, 300)),
    ("Encanto Neighborhood Association", "Will Foster",
     "board@encantoneighbors.org", "602-555-0209", 2020,
     "Quarterly meetings", 2, "Courtyard",
     ["Community Meeting"], (40, 90)),
    ("Desert Sky Robotics", "Aisha Nkemelu",
     "coach@desertskyrobotics.org", "602-555-0210", 2022,
     "Student robotics team", 3, "Main Hall",
     ["Conference", "Workshop"], (80, 180)),
    ("Maryvale Health Coalition", "Dr. Lena Park",
     "outreach@maryvalehealth.org", "602-555-0221", 2021,
     "Health fairs, nonprofit rate", 3, "Courtyard",
     ["Fundraiser", "Community Meeting"], (70, 140)),
    ("South Mountain Hikers", "Ben Carter",
     "trailhead@southmtnhikers.org", "602-555-0232", 2020,
     "Outdoor club", 3, "Courtyard",
     ["Networking", "Community Meeting"], (30, 80)),
    ("Phoenix Youth Soccer League", "Sofia Marín",
     "league@phxyouthsoccer.org", "602-555-0243", 2021,
     "Awards nights", 2, "Main Hall",
     ["Fundraiser"], (120, 260)),
    ("Rio Salado Beekeepers", "Owen Tran",
     "hive@riosaladobees.org", "602-555-0254", 2022,
     "Small hobby group", 2, "Meeting Room",
     ["Workshop", "Community Meeting"], (18, 36)),
    ("Central Library Friends", "Nadia Rahman",
     "friends@centrallibrary.org", "602-555-0265", 2019,
     "Annual gala", 2, "Main Hall",
     ["Fundraiser"], (140, 240)),
    ("Ahwatukee Chamber Singers", "Grant Mills",
     "sing@ahwatukeechamber.org", "602-555-0276", 2020,
     "Seasonal concerts", 1, "Main Hall",
     ["Concert"], (160, 300)),
    ("Tempe Tech Meetup", "Ravi Shah",
     "organizers@tempetech.dev", "602-555-0287", 2023,
     "Evening talks", 1, "Meeting Room",
     ["Networking"], (25, 40)),
    ("Nguyen Family", "Kim Nguyen",
     "kimnguyen.family@example.com", "602-555-0298", 2026,
     "Private event", 1, "Courtyard",
     ["Wedding"], (90, 130)),
    ("Okafor Family", "Chidi Okafor",
     "okafor.celebration@example.com", "602-555-0309", 2026,
     "Private event", 1, "Main Hall",
     ["Wedding"], (180, 260)),
    ("Sacred Heart Parish", "Fr. Diego Ramos",
     "office@sacredheartphx.org", "602-555-0310", 2018,
     "Community celebrations", 1, "Main Hall",
     ["Quinceañera"], (150, 280)),
    ("Phoenix Pride Alliance", "Jordan Lee",
     "events@phxpride.org", "602-555-0321", 2021,
     "Community fundraiser", 1, "Courtyard",
     ["Fundraiser", "Networking"], (100, 150)),
    ("Downtown Farmers Market", "Hannah Berg",
     "market@downtownphxmarket.org", "602-555-0332", 2020,
     "Seasonal market", 1, "Courtyard",
     ["Market"], (80, 150)),
]


def build_records():
    rng = random.Random(BASE_SEED)
    customers = []
    bookings = []

    # Spread event dates deterministically across 2026. A rolling cursor
    # walks the year so dates land in every quarter and the calendar view
    # has something to show, with roughly half before the status date.
    day_cursor = 6

    booking_id = 1001
    for (org, contact, email, phone, since, notes, count,
         pref_space, event_types, guest_range) in ORGS:
        customers.append([org, contact, email, phone, since, notes])
        for _ in range(count):
            # Space: usually the preferred one, sometimes another.
            if rng.random() < 0.7:
                space = pref_space
            else:
                space = rng.choice(list(SPACES))
            event_type = rng.choice(event_types)
            lo, hi = guest_range
            # A real venue never books more guests than a space holds, so
            # cap the draw at capacity. The only overflows are the two
            # planted below (the feasibility flag students spot).
            guests = min(rng.randint(lo, hi), SPACES[space]["capacity"])
            hours = rng.choice([2, 3, 3, 4, 4, 5, 6, 8])
            package = rng.choice(["Bronze", "Silver", "Silver",
                                  "Gold", "Gold"])
            # Zero to two add-ons.
            n_addons = rng.choice([0, 1, 1, 2])
            picks = rng.sample(list(ADDONS), n_addons)
            # Keep a stable, readable order for multi-select import.
            picks = [a for a in ADDONS if a in picks]
            addons = ", ".join(picks) if picks else "None"

            price = (SPACES[space]["rate"] * hours + PACKAGES[package]
                     + sum(ADDONS[a] for a in picks))

            day_cursor = (day_cursor + rng.randint(9, 21)) % 360
            event_date = date(2026, 1, 1) + timedelta(days=day_cursor)

            bookings.append({
                "Booking ID": "SH-%04d" % booking_id,
                "Event Date": event_date.isoformat(),
                "Space": space,
                "Organization": org,
                "Contact Email": email,
                "Contact Phone": phone,
                "Event Type": event_type,
                "Guest Count": guests,
                "Hours": hours,
                "Package": package,
                "Add-Ons": addons,
                "_price": price,
                "_date": event_date,
            })
            booking_id += 1

    # Force exactly two capacity overflows (a feasibility flag). Pick two
    # bookings deterministically and push their guest count over capacity.
    overflow_targets = [b for b in bookings
                        if b["Guest Count"] <= SPACES[b["Space"]]["capacity"]]
    for b in rng.sample(overflow_targets, 2):
        b["Guest Count"] = SPACES[b["Space"]]["capacity"] + rng.randint(5, 25)

    # Assign status. A fixed handful cancel; past events complete; the
    # rest are confirmed or pending by how soon they are.
    cancelled = set(rng.sample(range(len(bookings)), 6))
    for i, b in enumerate(bookings):
        if i in cancelled:
            b["Status"] = "Cancelled"
        elif b["_date"] < STATUS_DATE:
            b["Status"] = "Completed"
        else:
            days_out = (b["_date"] - STATUS_DATE).days
            b["Status"] = "Confirmed" if days_out <= 75 else "Pending"

    # Plant exactly one phone drift: copy a wrong digit onto a single
    # booking row whose organization has more than one booking (so the
    # Customers table still holds the one correct value).
    multi = [b for b in bookings
             if sum(1 for x in bookings
                    if x["Organization"] == b["Organization"]) > 1]
    drift = rng.choice(multi)
    good = drift["Contact Phone"]
    drift["Contact Phone"] = good[:-1] + ("7" if good[-1] != "7" else "3")
    drift_id = drift["Booking ID"]

    return customers, bookings, drift_id


def rows_for_csv(bookings):
    out = []
    for b in bookings:
        out.append([b["Booking ID"], b["Event Date"], b["Space"],
                    b["Organization"], b["Contact Email"],
                    b["Contact Phone"], b["Event Type"],
                    b["Guest Count"], b["Hours"], b["Package"],
                    b["Add-Ons"], b["Status"], b["_price"]])
    return out


def verify(customers, bookings, drift_id):
    assert len(bookings) == 60, "60 bookings"
    assert all(len(r) == 13 for r in rows_for_csv(bookings)), "13 columns"
    assert len(customers) == 24, "24 customers"
    assert len(set(b["Booking ID"] for b in bookings)) == 60, "unique IDs"

    cust_by_org = {c[0]: c for c in customers}
    assert len(cust_by_org) == 24, "unique organizations"

    # Referential integrity.
    for b in bookings:
        assert b["Organization"] in cust_by_org, "org must exist"

    # Every customer has at least one booking (no orphan dimension rows).
    booked = {b["Organization"] for b in bookings}
    assert booked == set(cust_by_org), "every customer books at least once"

    # Repeat business: a clear leader and several repeats.
    counts = {}
    for b in bookings:
        counts[b["Organization"]] = counts.get(b["Organization"], 0) + 1
    top_org = max(counts, key=counts.get)
    assert counts[top_org] == 6, "top organization books 6 times"
    repeaters = sum(1 for c in counts.values() if c > 1)
    assert repeaters >= 8, "several organizations book more than once"

    # Price formula holds for every row.
    for b in bookings:
        picks = [] if b["Add-Ons"] == "None" else b["Add-Ons"].split(", ")
        expected = (SPACES[b["Space"]]["rate"] * b["Hours"]
                    + PACKAGES[b["Package"]] + sum(ADDONS[a] for a in picks))
        assert b["_price"] == expected, "price = rate*hours + pkg + addons"

    # Email always consistent; phone consistent except the one drift.
    phone_mismatch = []
    for b in bookings:
        c = cust_by_org[b["Organization"]]
        assert b["Contact Email"] == c[2], "email matches the dimension"
        if b["Contact Phone"] != c[3]:
            phone_mismatch.append(b["Booking ID"])
    assert phone_mismatch == [drift_id], "exactly one planted phone drift"

    # Exactly two capacity overflows.
    overflow = [b["Booking ID"] for b in bookings
                if b["Guest Count"] > SPACES[b["Space"]]["capacity"]]
    assert len(overflow) == 2, "exactly two capacity overflows"

    # All four statuses present.
    statuses = {b["Status"] for b in bookings}
    assert statuses == {"Confirmed", "Pending", "Completed", "Cancelled"}, \
        "all four statuses appear"

    status_counts = {s: sum(1 for b in bookings if b["Status"] == s)
                     for s in ["Confirmed", "Pending", "Completed",
                               "Cancelled"]}
    space_counts = {s: sum(1 for b in bookings if b["Space"] == s)
                    for s in SPACES}
    total_quoted = sum(b["_price"] for b in bookings)
    realized = sum(b["_price"] for b in bookings
                   if b["Status"] != "Cancelled")

    top3 = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:3]

    return {
        "bookings": len(bookings),
        "customers": len(customers),
        "top_org": "%s (%d bookings)" % (top_org, counts[top_org]),
        "top3_orgs": top3,
        "repeat_orgs": repeaters,
        "status_counts": status_counts,
        "space_counts": space_counts,
        "total_quoted": total_quoted,
        "realized_revenue": realized,
        "drift_booking": drift_id,
        "overflow_bookings": overflow,
    }


def csv_bytes(headers, rows):
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def main():
    customers, bookings, drift_id = build_records()
    stats = verify(customers, bookings, drift_id)

    booking_rows = rows_for_csv(bookings)
    files = {
        BOOKINGS_PATH: csv_bytes(BOOKING_HEADERS, booking_rows),
        CUSTOMERS_PATH: csv_bytes(CUSTOMER_HEADERS, customers),
    }

    # Prove byte-reproducibility: rebuild and compare.
    customers2, bookings2, drift2 = build_records()
    again = {
        BOOKINGS_PATH: csv_bytes(BOOKING_HEADERS, rows_for_csv(bookings2)),
        CUSTOMERS_PATH: csv_bytes(CUSTOMER_HEADERS, customers2),
    }
    for path in files:
        assert hashlib.md5(files[path]).hexdigest() == \
            hashlib.md5(again[path]).hexdigest(), "CSV bytes reproducible"

    for path, payload in files.items():
        with open(path, "wb") as handle:
            handle.write(payload)
        print("wrote %s (md5 %s, %d bytes)"
              % (path, hashlib.md5(payload).hexdigest(), len(payload)))

    print("---- answer key ----")
    for key, value in stats.items():
        print("%s: %s" % (key, value))


if __name__ == "__main__":
    main()
