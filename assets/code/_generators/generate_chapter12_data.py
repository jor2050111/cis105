"""Generate the Chapter 12 Skills Lab data pack (Record It, Read It,
Rewrite It: Your First Macro).

Two files describe Renee Salazar's monthly reporting ritual at Saguaro
Hall, the event venue whose booking base students built in Chapter 10
and tracked to rollout in Chapter 11:

* booking-export.xlsx   October 2026, the base's first full month live.
                        Sheet OctoberExport: 63 bookings x 10 columns,
                        sorted by event date, no cancellations and no
                        contact details (the Airtable export view
                        filters and sorts before Renee downloads it, the
                        least-privilege habit from Chapters 8 and 10).
* ai-macro-draft.txt    The prompt Renee gave an AI assistant in
                        September, and the VBA procedure it drafted,
                        unchanged. Renee's prompt described September's
                        export, which held 60 bookings, so every range
                        is hardcoded to rows 2-61. On October's 63-row
                        export the draft runs without any error and
                        reports a wrong count and a short total: the
                        chapter's quiet-wrong-answer lesson.

Base seed 105 (documented in HANDOFF.md). The workbook build pins
document properties and zip timestamps (the family openpyxl fix), so
every run is byte-identical.

Continuity: the four October bookings already present in the Chapter 10
base (SH-1016, SH-1017, SH-1040, SH-1041) appear verbatim, imported
from generate_chapter10_data at build time so they can never drift. The
59 bookings taken after that July snapshot continue the ID series from
SH-1061.

Engineered properties (each verified by an assert below):
* 63 data rows x 10 columns (clears the 50-by-5 floor)
* Every Quoted Price equals space rate x hours + package fee + add-on
  fees, the exact Chapter 10 pricing model, imported not copied
* Dates ascend through October 2026 with no space double-booked on any
  date (the requirement the Chapter 11 lab tested), and every guest
  count fits its space (the venue learned from Chapter 10's overflows)
* The last three rows are the month's Oct 30-31 finale. The AI draft's
  hardcoded J2:J61 range misses exactly these three bookings, and their
  combined price is material (at least $4,000), so the short total
  misstates October, it does not round it
* The AI draft text still carries the stale range and the September
  label, so the shipped artifact matches what the chapter teaches

Rebuild:  python3 assets/code/_generators/generate_chapter12_data.py
"""

import hashlib
import io
import random
import re
import zipfile
from datetime import date, datetime

from openpyxl import Workbook

import generate_chapter10_data as g10

BASE_SEED = 105
WORKBOOK_PATH = "assets/code/chapter-12/booking-export.xlsx"
DRAFT_PATH = "assets/code/chapter-12/ai-macro-draft.txt"

HEADERS = ["Booking ID", "Event Date", "Space", "Organization",
           "Event Type", "Guest Count", "Hours", "Package", "Add-Ons",
           "Quoted Price"]

EXPORT_MONTH = 10
EXPORT_YEAR = 2026

# The month's closing weekend, hand-placed so the export's final three
# rows are known, dated Oct 30-31, and expensive enough that a total
# which silently drops them misstates the month. Fields follow the
# Chapter 10 org profiles (space, event type, guest range).
FINALE = [
    ("Central Library Friends", date(2026, 10, 30), "Main Hall",
     "Fundraiser", 210, 6, "Gold", ["Catering", "Decor"]),
    ("Phoenix Pride Alliance", date(2026, 10, 31), "Courtyard",
     "Fundraiser", 130, 4, "Silver", ["Extra Staff"]),
    ("Las Artes Folklórico", date(2026, 10, 31), "Main Hall",
     "Concert", 240, 5, "Silver", ["AV Package"]),
]

# The AI assistant's draft, shipped exactly as "the assistant" returned
# it to Renee. The stale row count lives in HER prompt: the draft did
# what she asked, and what she asked stopped being true in October.
AI_DRAFT = '''\
Saguaro Hall: AI-drafted summary macro (for Skills Lab 12A, Part 3)
===================================================================

On September 30, 2026, with September's booking export open beside
her (60 bookings, rows 2 through 61), Renee Salazar asked an AI
assistant for help. Her prompt, word for word:

    Write an Excel VBA macro for my monthly booking export worksheet.
    Row 1 is headers. Booking IDs are in column A and quoted prices
    are in column J. The data runs from row 2 to row 61. Add a summary
    to the right of the data with the number of bookings and the total
    quoted revenue for the month.

The assistant's draft, unchanged:

Sub SummarizeExport()
    ' Adds a monthly summary block beside the booking export.
    Dim bookingCount As Long
    Dim totalRevenue As Double

    bookingCount = Application.WorksheetFunction.CountA(Range("A2:A61"))
    totalRevenue = Application.WorksheetFunction.Sum(Range("J2:J61"))

    Range("L1").Value = "September Summary"
    Range("L2").Value = "Bookings"
    Range("M2").Value = bookingCount
    Range("L3").Value = "Total quoted revenue"
    Range("M3").Value = totalRevenue
    Range("M3").NumberFormat = "$#,##0.00"
    Columns("L:M").AutoFit
End Sub
'''


def weighted_choice(rng, pairs):
    total = sum(w for _, w in pairs)
    roll = rng.uniform(0, total)
    upto = 0.0
    for value, weight in pairs:
        upto += weight
        if roll <= upto:
            return value
    return pairs[-1][0]


def inherited_october_bookings():
    """The Chapter 10 base's own October bookings, verbatim."""
    _, bookings, _ = g10.build_records()
    rows = []
    for b in bookings:
        if b["_date"].month == EXPORT_MONTH and b["Status"] != "Cancelled":
            rows.append({
                "Booking ID": b["Booking ID"],
                "Event Date": b["_date"],
                "Space": b["Space"],
                "Organization": b["Organization"],
                "Event Type": b["Event Type"],
                "Guest Count": b["Guest Count"],
                "Hours": b["Hours"],
                "Package": b["Package"],
                "Add-Ons": b["Add-Ons"],
            })
    return rows


def price_for(space, hours, package, addon_names):
    return (g10.SPACES[space]["rate"] * hours + g10.PACKAGES[package]
            + sum(g10.ADDONS[a] for a in addon_names))


def build_rows():
    # A distinct stream from Chapter 10's so the two chapters' draws
    # never mirror each other. Same base seed family, documented.
    rng = random.Random(BASE_SEED + 1200)

    inherited = inherited_october_bookings()
    taken_slots = {(b["Event Date"], b["Space"]) for b in inherited}

    finale = []
    for org, day, space, event_type, guests, hours, package, addons in \
            FINALE:
        assert (day, space) not in taken_slots
        taken_slots.add((day, space))
        finale.append({
            "Booking ID": None,  # assigned below with the other new IDs
            "Event Date": day,
            "Space": space,
            "Organization": org,
            "Event Type": event_type,
            "Guest Count": guests,
            "Hours": hours,
            "Package": package,
            "Add-Ons": ", ".join(addons),
        })

    # 56 drawn bookings on Oct 1-29 (the finale owns Oct 30-31), drawn
    # from the Chapter 10 org profiles with each org's booking count as
    # its weight, so the busy clients stay the busy clients.
    org_weights = [(profile[0], profile[6]) for profile in g10.ORGS]
    profiles = {profile[0]: profile for profile in g10.ORGS}

    drawn = []
    while len(drawn) < 56:
        org = weighted_choice(rng, org_weights)
        (_, _, _, _, _, _, _, pref_space, event_types,
         guest_range) = profiles[org]
        space = pref_space if rng.random() < 0.7 \
            else rng.choice(list(g10.SPACES))
        day = date(EXPORT_YEAR, EXPORT_MONTH, rng.randint(1, 29))
        if (day, space) in taken_slots:
            continue  # that space is spoken for that day: re-draw
        taken_slots.add((day, space))
        lo, hi = guest_range
        guests = min(rng.randint(lo, hi),
                     g10.SPACES[space]["capacity"])
        hours = rng.choice([2, 3, 3, 4, 4, 5, 6, 8])
        package = rng.choice(["Bronze", "Silver", "Silver",
                              "Gold", "Gold"])
        n_addons = rng.choice([0, 1, 1, 2])
        picks = rng.sample(list(g10.ADDONS), n_addons)
        picks = [a for a in g10.ADDONS if a in picks]
        drawn.append({
            "Booking ID": None,
            "Event Date": day,
            "Space": space,
            "Organization": org,
            "Event Type": rng.choice(event_types),
            "Guest Count": guests,
            "Hours": hours,
            "Package": package,
            "Add-Ons": ", ".join(picks) if picks else "None",
        })

    # New bookings arrived at the front desk in no particular calendar
    # order between July and October, so IDs continue the base's series
    # (SH-1061 on) in a shuffled arrival order, not event-date order.
    new_bookings = drawn + finale
    arrival = list(range(len(new_bookings)))
    rng.shuffle(arrival)
    for id_offset, booking_index in enumerate(arrival):
        new_bookings[booking_index]["Booking ID"] = \
            "SH-%04d" % (1061 + id_offset)

    rows = inherited + new_bookings
    rows.sort(key=lambda b: (b["Event Date"], b["Booking ID"]))
    return rows, inherited, finale


def rows_for_sheet(rows):
    out = []
    for b in rows:
        addons = b["Add-Ons"]
        addon_names = [] if addons == "None" else addons.split(", ")
        out.append([b["Booking ID"], b["Event Date"], b["Space"],
                    b["Organization"], b["Event Type"],
                    b["Guest Count"], b["Hours"], b["Package"],
                    addons,
                    price_for(b["Space"], b["Hours"], b["Package"],
                              addon_names)])
    return out


def verify(rows, inherited, finale):
    sheet_rows = rows_for_sheet(rows)
    assert len(sheet_rows) == 63, "63 October bookings"
    assert all(len(r) == 10 for r in sheet_rows), "10 columns"

    ids = [r[0] for r in sheet_rows]
    assert len(set(ids)) == 63, "unique booking IDs"

    dates = [r[1] for r in sheet_rows]
    assert all(d.year == EXPORT_YEAR and d.month == EXPORT_MONTH
               for d in dates), "all October 2026"
    assert dates == sorted(dates), "sorted by event date"

    slots = [(r[1], r[2]) for r in sheet_rows]
    assert len(set(slots)) == 63, "no space double-booked on a date"

    for r in sheet_rows:
        assert r[5] <= g10.SPACES[r[2]]["capacity"], \
            "guest counts fit the space"
        addon_names = [] if r[8] == "None" else r[8].split(", ")
        assert r[9] == price_for(r[2], r[6], r[7], addon_names), \
            "price reproduces from the model"

    # The Chapter 10 base's October bookings appear verbatim.
    by_id = {r[0]: r for r in sheet_rows}
    assert len(inherited) == 4, "four bookings inherited from Chapter 10"
    for b in inherited:
        r = by_id[b["Booking ID"]]
        addon_names = ([] if b["Add-Ons"] == "None"
                       else b["Add-Ons"].split(", "))
        assert (r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]) == (
            b["Event Date"], b["Space"], b["Organization"],
            b["Event Type"], b["Guest Count"], b["Hours"],
            b["Package"], b["Add-Ons"]), "Chapter 10 rows unchanged"
        assert r[9] == price_for(b["Space"], b["Hours"], b["Package"],
                                 addon_names), "Chapter 10 price holds"

    # The quiet wrong answer, pinned. The AI draft sums sheet rows 2-61,
    # which is the first 60 data rows; the last three (the finale) fall
    # outside it, and they are material.
    correct_total = sum(r[9] for r in sheet_rows)
    buggy_total = sum(r[9] for r in sheet_rows[:60])
    shortfall = correct_total - buggy_total
    finale_ids = {r[0] for r in sheet_rows[60:]}
    assert [r[1] for r in sheet_rows[60:]] == \
        [date(2026, 10, 30), date(2026, 10, 31), date(2026, 10, 31)], \
        "the finale rows close the sheet"
    assert shortfall == sum(
        price_for(space, hours, package, addons)
        for _, _, space, _, _, hours, package, addons in FINALE), \
        "the shortfall is exactly the finale"
    assert shortfall >= 4000, "the miss is material, not a rounding slip"

    assert 'Range("J2:J61")' in AI_DRAFT, "stale range ships in the draft"
    assert "September Summary" in AI_DRAFT, "stale label ships too"

    biggest = max(sheet_rows, key=lambda r: r[9])
    space_counts = {}
    for r in sheet_rows:
        space_counts[r[2]] = space_counts.get(r[2], 0) + 1

    return {
        "bookings": len(sheet_rows),
        "correct_total": correct_total,
        "buggy_total": buggy_total,
        "shortfall": shortfall,
        "finale_ids_in_sheet_order": [r[0] for r in sheet_rows[60:]],
        "finale_prices": [r[9] for r in sheet_rows[60:]],
        "inherited_ids": sorted(b["Booking ID"] for b in inherited),
        "biggest_booking": "%s (%s, $%d)" % (biggest[0], biggest[3],
                                             biggest[9]),
        "space_counts": space_counts,
        "first_row": sheet_rows[0][0],
        "last_row_number": len(sheet_rows) + 1,
    }


def workbook_bytes(rows):
    wb = Workbook()
    ws = wb.active
    ws.title = "OctoberExport"
    ws.append(HEADERS)
    for row in rows_for_sheet(rows):
        ws.append(row)  # openpyxl stores Event Date as a real date cell
    for cell in ws["B"][1:]:
        cell.number_format = "YYYY-MM-DD"

    # Pinned metadata plus normalized zip-entry timestamps keep every
    # rebuild byte-identical (openpyxl stamps entries with save time).
    pinned = datetime(2026, 7, 11, 12, 0, 0)
    wb.properties.creator = "CIS105 course data pack"
    wb.properties.created = pinned
    wb.properties.modified = pinned
    buffer = io.BytesIO()
    wb.save(buffer)

    source = zipfile.ZipFile(io.BytesIO(buffer.getvalue()))
    normalized = io.BytesIO()
    with zipfile.ZipFile(normalized, "w", zipfile.ZIP_DEFLATED) as archive:
        for item in source.infolist():
            info = zipfile.ZipInfo(item.filename,
                                   date_time=(2026, 7, 11, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = item.external_attr
            payload = source.read(item.filename)
            if item.filename == "docProps/core.xml":
                # openpyxl restamps dcterms:modified at save time, so the
                # pinned property never survives wb.save(). Pin it here,
                # where every entry already gets a pinned zip timestamp.
                payload = re.sub(
                    rb"<dcterms:(created|modified)([^>]*)>[^<]*"
                    rb"</dcterms:\1>",
                    rb"<dcterms:\1\2>2026-07-11T12:00:00Z</dcterms:\1>",
                    payload)
            archive.writestr(info, payload)
    return normalized.getvalue()


def main():
    rows, inherited, finale = build_rows()
    stats = verify(rows, inherited, finale)

    first = workbook_bytes(rows)
    second = workbook_bytes(rows)
    assert hashlib.md5(first).hexdigest() == \
        hashlib.md5(second).hexdigest(), \
        "workbook bytes must be reproducible"

    rows2, inherited2, finale2 = build_rows()
    assert rows_for_sheet(rows2) == rows_for_sheet(rows), \
        "row build must be reproducible"

    with open(WORKBOOK_PATH, "wb") as handle:
        handle.write(first)
    print("wrote %s (md5 %s)" % (WORKBOOK_PATH,
                                 hashlib.md5(first).hexdigest()))

    draft_bytes = AI_DRAFT.encode("utf-8")
    with open(DRAFT_PATH, "wb") as handle:
        handle.write(draft_bytes)
    print("wrote %s (md5 %s)" % (DRAFT_PATH,
                                 hashlib.md5(draft_bytes).hexdigest()))

    print("---- answer key ----")
    for key, value in stats.items():
        print("%s: %s" % (key, value))


if __name__ == "__main__":
    main()
