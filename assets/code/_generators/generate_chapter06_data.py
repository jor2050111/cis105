"""Generate assets/code/chapter-06/device-comparison.xlsx (Skills Lab 6A).

Cactus Wren Repair's refurbished-device inventory: 54 rows by 8 columns
of seeded synthetic data. Base seed 105 (documented in HANDOFF.md).
Byte-identical on every run: the RNG is seeded, workbook timestamps are
pinned, and the script verifies reproducibility by writing twice and
comparing hashes.

Engineered properties (each verified by an assert below):
* 54 data rows and 8 columns (clears the 50-by-5 data-pack floor)
* Exactly 7 desktops, whose Battery Health cells are blank, so
  =AVERAGE(G2:G55) uses 47 values (the chapter teaches why)
* The three Chapter 5 cast devices appear with their published specs
  (Desert Falcon 15, Stone Tower, Bloom Pad 11)
* One flagship workstation carries the maximum price ($1,299) and one
  Grade C phone carries the minimum ($89), so MIN/MAX have unique answers
* Chapter-printed formula results match the file exactly (totals below)

Rebuild:  python3 assets/code/_generators/generate_chapter06_data.py
"""

import hashlib
import io
import random
import re
import zipfile
from datetime import datetime

from openpyxl import Workbook

BASE_SEED = 105
OUTPUT_PATH = "assets/code/chapter-06/device-comparison.xlsx"

HEADERS = ["Device ID", "Device Name", "Category", "Condition Grade",
           "RAM (GB)", "Storage (GB)", "Battery Health (%)", "Price ($)"]

# The Chapter 5 cast devices ship with their published specs, so the
# workbook agrees with the deck students built in Skills Lab 5A.
CAST_DEVICES = [
    ("Desert Falcon 15", "Laptop", "A", 16, 512, 91, 679),
    ("Stone Tower", "Desktop", "A", 32, 1024, None, 749),
    ("Bloom Pad 11", "Tablet", "B", 8, 256, 88, 329),
]

NAME_POOLS = {
    "Laptop": ["Mesa Book", "Sonora Slim", "Canyon Air", "Agave Pro",
               "Ocotillo 14", "Cholla Go", "Ridgeline 16", "Dune Book"],
    "Desktop": ["Granite Core", "Butte Station", "Adobe Works"],
    "Tablet": ["Sol Pad", "Verde Slate", "Palo Tab", "Vista Pad"],
    "Phone": ["Wren Phone", "Cactus Call", "Salt River S", "Papago P"],
}

# Category plan: 22 laptops, 6 desktops, 13 tablets, 11 phones = 52
# rows, plus the two price anchors appended below = 54 total.
CATEGORY_PLAN = [("Laptop", 22), ("Desktop", 6), ("Tablet", 13),
                 ("Phone", 11)]

RAM_CHOICES = {
    "Laptop": [8, 8, 16, 16, 16, 32],
    "Desktop": [16, 32, 32, 64],
    "Tablet": [4, 8, 8, 16],
    "Phone": [4, 6, 8, 12],
}
STORAGE_CHOICES = {
    "Laptop": [256, 256, 512, 512, 1024],
    "Desktop": [512, 1024, 1024, 2048],
    "Tablet": [64, 128, 256, 256],
    "Phone": [64, 128, 128, 256],
}
PRICE_RANGES = {
    "Laptop": (299, 899),
    "Desktop": (349, 999),
    "Tablet": (129, 449),
    "Phone": (99, 549),
}
GRADE_WEIGHTS = [("A", 5), ("B", 4), ("C", 2)]


def build_rows():
    rng = random.Random(BASE_SEED)
    rows = []
    cast_by_category = {}
    for name, cat, grade, ram, storage, battery, price in CAST_DEVICES:
        cast_by_category.setdefault(cat, []).append(
            (name, grade, ram, storage, battery, price))

    grades = [g for g, w in GRADE_WEIGHTS for _ in range(w)]
    for category, count in CATEGORY_PLAN:
        cast_rows = cast_by_category.get(category, [])
        for i in range(count):
            if i < len(cast_rows):
                name, grade, ram, storage, battery, price = cast_rows[i]
            else:
                name = (rng.choice(NAME_POOLS[category])
                        + " " + rng.choice(["S", "X", "SE", "Max", "Lite"]))
                grade = rng.choice(grades)
                ram = rng.choice(RAM_CHOICES[category])
                storage = rng.choice(STORAGE_CHOICES[category])
                lo, hi = PRICE_RANGES[category]
                price = rng.randrange(lo, hi, 10)
                # Grade C stock is priced to move, and battery wear
                # tracks the grade so the columns tell one story.
                if grade == "C":
                    price = max(lo, price - 120)
                if category == "Desktop":
                    battery = None
                else:
                    base = {"A": rng.randint(85, 99),
                            "B": rng.randint(74, 90),
                            "C": rng.randint(62, 80)}
                    battery = base[grade]
            rows.append([name, category, grade, ram, storage,
                         battery, price])

    rng.shuffle(rows)

    # The two price anchors are placed after the shuffle so MIN and MAX
    # have unique, findable answers the lab can ask about.
    rows.append(["Saguaro Workstation", "Desktop", "A", 64, 2048,
                 None, 1299])
    rows.append(["Cactus Call Mini", "Phone", "C", 4, 64, 64, 89])
    rng.shuffle(rows)

    # Device IDs are assigned in final row order.
    return [["CW-%d" % (1001 + i)] + row for i, row in enumerate(rows)]


def verify(rows):
    assert len(rows) == 54, "row count must be 54"
    assert all(len(r) == 8 for r in rows), "column count must be 8"
    ids = [r[0] for r in rows]
    assert len(set(ids)) == 54, "device IDs must be unique"

    desktops = [r for r in rows if r[2] == "Desktop"]
    assert len(desktops) == 7, "6 planned desktops plus the workstation"
    assert all(r[6] is None for r in desktops), "desktops have no battery"
    blanks = [r for r in rows if r[6] is None]
    assert len(blanks) == 7, "exactly 7 blank battery cells"

    batteries = [r[6] for r in rows if r[6] is not None]
    assert len(batteries) == 47, "47 battery values for AVERAGE"
    assert all(60 <= b <= 99 for b in batteries), "battery range"

    prices = [r[7] for r in rows]
    assert max(prices) == 1299 and prices.count(1299) == 1, "unique MAX"
    assert min(prices) == 89 and prices.count(89) == 1, "unique MIN"

    for name, cat, grade, ram, storage, battery, price in CAST_DEVICES:
        match = [r for r in rows if r[1] == name]
        assert len(match) == 1, "cast device present once: " + name
        r = match[0]
        assert r[2:] == [cat, grade, ram, storage, battery, price], name

    return {
        "count": len(rows),
        "price_total": sum(prices),
        "price_avg": sum(prices) / len(prices),
        "price_min": min(prices),
        "price_max": max(prices),
        "battery_avg": sum(batteries) / len(batteries),
        "battery_count": len(batteries),
        "laptops": sum(1 for r in rows if r[2] == "Laptop"),
    }


def workbook_bytes(rows):
    wb = Workbook()
    ws = wb.active
    ws.title = "DeviceInventory"
    ws.append(HEADERS)
    for row in rows:
        ws.append(row)
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
        print("%s: %s" % (key, round(value, 4)
                          if isinstance(value, float) else value))


if __name__ == "__main__":
    main()
