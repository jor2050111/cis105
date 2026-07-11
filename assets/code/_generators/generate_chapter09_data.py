"""Generate assets/code/chapter-09/coffee-sales.xlsx (Skills Lab 9A).

Desert Bloom Coffee's June 2026 sales: one line item per row across
three locations, four full Monday-to-Sunday weeks (June 1-28), two
channels (Counter and the Bloom Ahead app), and five product
categories. Base seed 105 (documented in HANDOFF.md). Byte-identical
on every run.

Engineered properties (each verified by an assert below):
* At least 450 data rows by 12 columns (clears the 50-by-5 floor)
* The Campus location's weekend days average less than half its
  weekday days (no classes, no line), while 7th Street holds its
  weekends, so the chain-wide daily average HIDES the Campus dip:
  the segment story only appears when a pivot splits location by
  day type. This is the chapter's averages-conceal lesson.
* Bloom Ahead's share of revenue rises every week, week 1 through
  week 4, so a pivot by Week and Channel shows a clean trend
* App orders average a higher line total than counter orders (by at
  least $0.50), the Petal Points attach-rate story
* Cold Drinks is the top revenue category chain-wide (June in
  Phoenix) and Merch is the smallest, so "what sells most" has a
  seasonal answer students must read from the pivot, not assume
* Every Line Total equals Qty times Unit Price exactly

Rebuild:  python3 assets/code/_generators/generate_chapter09_data.py
"""

import hashlib
import io
import random
import re
import zipfile
from datetime import date, datetime, timedelta

from openpyxl import Workbook

BASE_SEED = 105
OUTPUT_PATH = "assets/code/chapter-09/coffee-sales.xlsx"

HEADERS = ["Order ID", "Date", "Week", "Day Type", "Location",
           "Daypart", "Channel", "Category", "Item", "Qty",
           "Unit Price ($)", "Line Total ($)"]

START = date(2026, 6, 1)  # a Monday; four full weeks end June 28

MENU = {
    "Hot Coffee": [("Drip Coffee", 3.00), ("Cortado", 4.50),
                   ("Latte", 5.00), ("Cappuccino", 4.75),
                   ("Mocha", 5.50)],
    "Cold Drinks": [("Cold Brew", 4.75), ("Iced Latte", 5.25),
                    ("Prickly Pear Lemonade", 4.25),
                    ("Iced Tea", 3.50)],
    "Tea": [("Chai Latte", 4.75), ("Herbal Pot", 4.00),
            ("Matcha Latte", 5.25)],
    "Bakery": [("Croissant", 3.75), ("Blueberry Muffin", 3.50),
               ("Sonoran Breakfast Burrito", 6.50), ("Cookie", 2.75)],
    "Merch": [("Bloom Mug", 14.00), ("Beans 1 lb Bag", 16.00),
              ("Tumbler", 22.00)],
}

# Category draw weights. June in Phoenix: cold drinks lead. The app
# channel skews toward pricier drinks and carries most merch sales
# (Petal Points members browse the whole menu while they wait).
COUNTER_WEIGHTS = [("Cold Drinks", 34), ("Hot Coffee", 30),
                   ("Bakery", 22), ("Tea", 12), ("Merch", 2)]
APP_WEIGHTS = [("Cold Drinks", 38), ("Hot Coffee", 26),
               ("Bakery", 18), ("Tea", 12), ("Merch", 6)]

# Line items per day by location: (weekday range, weekend range).
DAY_VOLUME = {
    "7th Street": ((7, 9), (7, 10)),
    "Roosevelt Row": ((5, 7), (5, 8)),
    "Campus": ((6, 8), (2, 3)),
}

# Bloom Ahead's share of orders grows week over week. Shares are
# allocated exactly (not drawn), so the weekly trend cannot wobble.
APP_SHARE_BY_WEEK = {1: 0.20, 2: 0.30, 3: 0.40, 4: 0.50}

DAYPART_WEIGHTS = [("Morning", 5), ("Afternoon", 3), ("Evening", 2)]


def weighted_choice(rng, pairs):
    total = sum(w for _, w in pairs)
    roll = rng.uniform(0, total)
    upto = 0.0
    for value, weight in pairs:
        upto += weight
        if roll <= upto:
            return value
    return pairs[-1][0]


def build_rows():
    rng = random.Random(BASE_SEED)
    # First pass: draw every day's line-item slots for the month.
    slots = []
    for day_offset in range(28):
        day = START + timedelta(days=day_offset)
        week = day_offset // 7 + 1
        weekend = day.weekday() >= 5
        day_type = "Weekend" if weekend else "Weekday"
        for location in ["7th Street", "Roosevelt Row", "Campus"]:
            lo, hi = DAY_VOLUME[location][1 if weekend else 0]
            for _ in range(rng.randint(lo, hi)):
                slots.append([day, week, day_type, location])

    # Second pass: allocate each week's channel mix exactly, so the
    # app's weekly share is engineered rather than drawn.
    app_flags = {}
    for week in [1, 2, 3, 4]:
        week_ids = [i for i, s in enumerate(slots) if s[1] == week]
        app_count = round(len(week_ids) * APP_SHARE_BY_WEEK[week])
        app_set = set(rng.sample(week_ids, app_count))
        for i in week_ids:
            app_flags[i] = i in app_set

    rows = []
    for i, (day, week, day_type, location) in enumerate(slots):
        app = app_flags[i]
        channel = "Bloom Ahead" if app else "Counter"
        weights = APP_WEIGHTS if app else COUNTER_WEIGHTS
        category = weighted_choice(rng, weights)
        item, price = rng.choice(MENU[category])
        if category == "Merch":
            qty = 1
        elif app:
            qty = rng.choice([1, 2, 2, 3, 3, 4])
        else:
            qty = rng.choice([1, 1, 1, 2, 2, 3])
        rows.append([day, week, day_type, location,
                     weighted_choice(rng, DAYPART_WEIGHTS),
                     channel, category, item, qty, price,
                     round(qty * price, 2)])
    return [["DB-%04d" % (1001 + i)] + row for i, row in enumerate(rows)]


def verify(rows):
    assert len(rows) >= 450, "at least 450 line items"
    assert all(len(r) == 12 for r in rows), "12 columns"
    ids = [r[0] for r in rows]
    assert len(set(ids)) == len(ids), "unique order IDs"
    for r in rows:
        assert abs(r[11] - r[9] * r[10]) < 0.005, "line total = qty*price"

    def revenue(pred):
        return sum(r[11] for r in rows if pred(r))

    total = revenue(lambda r: True)

    # Campus weekend dip, hidden at chain level.
    def daily_avg(location, day_type):
        days = {(r[1], r[4]) for r in rows
                if r[4] == location and r[3] == day_type}
        rev = revenue(lambda r: r[4] == location and r[3] == day_type)
        return rev / len({d for d, loc in days})

    campus_wd = daily_avg("Campus", "Weekday")
    campus_we = daily_avg("Campus", "Weekend")
    assert campus_we < 0.5 * campus_wd, "Campus weekend under half"
    seventh_wd = daily_avg("7th Street", "Weekday")
    seventh_we = daily_avg("7th Street", "Weekend")
    assert seventh_we >= 0.9 * seventh_wd, "7th Street holds weekends"

    chain_wd = revenue(lambda r: r[3] == "Weekday") / 20
    chain_we = revenue(lambda r: r[3] == "Weekend") / 8
    assert chain_we >= 0.72 * chain_wd, "chain average hides the dip"

    # App share rises weekly.
    shares = []
    for week in [1, 2, 3, 4]:
        wk = revenue(lambda r: r[2] == week)
        app = revenue(lambda r: r[2] == week and r[6] == "Bloom Ahead")
        shares.append(app / wk)
    assert shares == sorted(shares) and shares[0] < shares[3], \
        "app share rises every week"

    # App line totals outspend counter line totals.
    app_rows = [r[11] for r in rows if r[6] == "Bloom Ahead"]
    counter_rows = [r[11] for r in rows if r[6] == "Counter"]
    app_avg = sum(app_rows) / len(app_rows)
    counter_avg = sum(counter_rows) / len(counter_rows)
    assert app_avg >= counter_avg + 0.5, "app orders spend more"

    # Category ordering: Cold Drinks first, Merch last.
    cat_rev = {c: revenue(lambda r, c=c: r[7] == c) for c in MENU}
    ranked = sorted(cat_rev, key=cat_rev.get, reverse=True)
    assert ranked[0] == "Cold Drinks", "Cold Drinks lead June"
    assert ranked[-1] == "Merch", "Merch is smallest"

    loc_rev = {loc: revenue(lambda r, loc=loc: r[4] == loc)
               for loc in DAY_VOLUME}

    return {
        "rows": len(rows),
        "total_revenue": round(total, 2),
        "revenue_7th": round(loc_rev["7th Street"], 2),
        "revenue_roosevelt": round(loc_rev["Roosevelt Row"], 2),
        "revenue_campus": round(loc_rev["Campus"], 2),
        "campus_weekday_daily": round(campus_wd, 2),
        "campus_weekend_daily": round(campus_we, 2),
        "seventh_weekday_daily": round(seventh_wd, 2),
        "seventh_weekend_daily": round(seventh_we, 2),
        "chain_weekday_daily": round(chain_wd, 2),
        "chain_weekend_daily": round(chain_we, 2),
        "app_share_by_week": [round(s * 100, 1) for s in shares],
        "app_avg_line": round(app_avg, 2),
        "counter_avg_line": round(counter_avg, 2),
        "category_revenue": {c: round(v, 2)
                             for c, v in sorted(cat_rev.items(),
                                                key=lambda kv: -kv[1])},
    }


def workbook_bytes(rows):
    wb = Workbook()
    ws = wb.active
    ws.title = "SalesData"
    ws.append(HEADERS)
    for row in rows:
        ws.append(row)  # openpyxl stores the date as a real date cell

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
    rows = build_rows()
    stats = verify(rows)

    first = workbook_bytes(rows)
    second = workbook_bytes(rows)
    assert hashlib.md5(first).hexdigest() == hashlib.md5(second).hexdigest(), \
        "workbook bytes must be reproducible"

    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(first)

    print("wrote %s (md5 %s)" % (OUTPUT_PATH,
                                 hashlib.md5(first).hexdigest()))
    for key, value in stats.items():
        print("%s: %s" % (key, value))


if __name__ == "__main__":
    main()
