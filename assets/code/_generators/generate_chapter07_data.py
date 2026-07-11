"""Generate assets/code/chapter-07/internet-plans.xlsx (Skills Lab 7A).

The Phoenix-area Internet plan comparison sheet Darnell Brooks uses to
replace Saguaro Hall's failing connection: 54 rows by 10 columns across
nine fictional providers and six technologies. The rows are designed by
hand (a plan sheet is a market, not a random draw), and this script is
the single source of truth that rebuilds the file byte-identically and
verifies every property the chapter's prose cites.

Engineered properties (each verified by an assert below):
* 54 data rows and 10 columns (clears the 50-by-5 data-pack floor)
* The cheapest ADVERTISED plan (Copper Basin Basic 25, $30) is not the
  cheapest TRUE-cost plan (Roadrunner Essential 100, $40) once the
  equipment fee is added; both minimums are unique
* Exactly 13 plans meet Saguaro Hall's venue requirements (download
  >= 300, upload >= 30, latency <= 100 ms, Unlimited data), with a
  unique cheapest qualifier: Sonoran Fiber Home 300 at $65 true cost
* Roadrunner Surge 500 fails the venue test on its data cap ALONE
  (every other number qualifies), the lab's cap-matters lesson
* GEO satellite latency (610-650 ms) versus LEO (40-55 ms) differs by
  more than 10x; no GEO plan can pass the latency requirement
* Cost per Mbps: unique best (Sonoran Pro 2000) and unique worst
  (Copper Basin Rural 10), so the denominator lesson has one answer
* IF-example counts printed for the chapter: uploads >= 20 Mbps and
  true cost <= $100

Rebuild:  python3 assets/code/_generators/generate_chapter07_data.py
"""

import hashlib
import io
import re
import zipfile
from datetime import datetime

from openpyxl import Workbook

OUTPUT_PATH = "assets/code/chapter-07/internet-plans.xlsx"

HEADERS = ["Plan ID", "Provider", "Technology", "Plan Name",
           "Download (Mbps)", "Upload (Mbps)", "Latency (ms)",
           "Advertised Price ($/mo)", "Equipment Fee ($/mo)", "Data Cap"]

# Saguaro Hall's requirements, quoted in the chapter and the lab.
VENUE_DOWN = 300
VENUE_UP = 30
VENUE_LATENCY = 100
VENUE_CAP = "Unlimited"

# (provider, technology, equipment fee) -> list of
# (plan name, down, up, latency, advertised price, data cap)
PROVIDERS = [
    ("Sonoran Fiber", "Fiber", 0, [
        ("Basic 50", 50, 50, 9, 45, "Unlimited"),
        ("Starter 100", 100, 100, 9, 55, "Unlimited"),
        ("Home 300", 300, 300, 8, 65, "Unlimited"),
        ("Office 500", 500, 500, 8, 75, "Unlimited"),
        ("Gig 1000", 1000, 1000, 8, 80, "Unlimited"),
        ("Pro 2000", 2000, 2000, 7, 110, "Unlimited"),
    ]),
    ("Pima Fiber Co-op", "Fiber", 10, [
        ("Neighbor 25", 25, 25, 13, 35, "Unlimited"),
        ("Neighbor 50", 50, 50, 12, 40, "Unlimited"),
        ("Neighbor 150", 150, 150, 12, 60, "Unlimited"),
        ("Community 300", 300, 300, 12, 70, "Unlimited"),
        ("Neighbor 500", 500, 500, 11, 75, "Unlimited"),
        ("Neighbor Gig", 1000, 1000, 11, 90, "Unlimited"),
    ]),
    ("Camelback Cable", "Cable", 12, [
        ("Essential 75", 75, 10, 26, 45, "Unlimited"),
        ("Starter 100", 100, 15, 25, 50, "Unlimited"),
        ("Standard 200", 200, 20, 24, 60, "Unlimited"),
        ("Value 300", 300, 20, 23, 65, "Unlimited"),
        ("Turbo 600", 600, 30, 22, 75, "Unlimited"),
        ("Blaze 1200", 1200, 35, 20, 95, "Unlimited"),
    ]),
    ("Grand Canal Cable", "Cable", 14, [
        ("Intro 50", 50, 5, 30, 35, "Unlimited"),
        ("Basic 100", 100, 10, 28, 40, "Unlimited"),
        ("Plus 250", 250, 20, 27, 60, "Unlimited"),
        ("Family 400", 400, 25, 26, 70, "Unlimited"),
        ("Max 900", 900, 30, 25, 85, "Unlimited"),
        ("Ultra 1500", 1500, 40, 24, 105, "Unlimited"),
    ]),
    ("Cholla 5G Home", "5G Home", 0, [
        ("Lite 50", 50, 8, 45, 42, "Unlimited"),
        ("Saver 100", 100, 12, 42, 45, "Unlimited"),
        ("Core 200", 200, 15, 40, 50, "Unlimited"),
        ("Plus 300", 300, 18, 40, 60, "Unlimited"),
        ("Max 400", 400, 22, 38, 65, "1 TB"),
        ("Ultra 600", 600, 25, 35, 70, "1.5 TB"),
    ]),
    ("Roadrunner Wireless", "5G Home", 0, [
        ("Essential 100", 100, 10, 45, 40, "300 GB"),
        ("Go 150", 150, 12, 44, 45, "300 GB"),
        ("Unlimited 200", 200, 15, 42, 55, "Unlimited"),
        ("Boost 300", 300, 25, 40, 60, "300 GB"),
        ("Surge 500", 500, 30, 38, 75, "600 GB"),
        ("Business 400", 400, 35, 36, 90, "Unlimited"),
    ]),
    ("Copper Basin DSL", "DSL", 15, [
        ("Rural 10", 10, 1, 45, 32, "Unlimited"),
        ("Basic 25", 25, 3, 38, 30, "Unlimited"),
        ("Legacy 40", 40, 5, 37, 36, "Unlimited"),
        ("Home 50", 50, 6, 36, 38, "Unlimited"),
        ("Office 75", 75, 8, 35, 42, "Unlimited"),
        ("Plus 100", 100, 12, 34, 45, "Unlimited"),
    ]),
    ("Desert Sky Satellite", "Satellite (GEO)", 15, [
        ("Basic 15", 15, 2, 650, 45, "40 GB"),
        ("Bronze 25", 25, 3, 640, 50, "60 GB"),
        ("Traveler 30", 30, 3, 640, 60, "60 GB"),
        ("Silver 50", 50, 4, 630, 70, "100 GB"),
        ("Gold 100", 100, 5, 620, 90, "200 GB"),
        ("Platinum 150", 150, 6, 610, 120, "300 GB"),
    ]),
    ("Swift Orbit Satellite", "Satellite (LEO)", 15, [
        ("Lite 80", 80, 12, 50, 80, "Unlimited"),
        ("Starter 120", 120, 18, 48, 90, "Unlimited"),
        ("Roam 100", 100, 15, 55, 120, "Unlimited"),
        ("Standard 150", 150, 20, 45, 99, "Unlimited"),
        ("Priority 250", 250, 25, 42, 140, "Unlimited"),
        ("Business 350", 350, 30, 40, 190, "Unlimited"),
    ]),
]


def build_rows():
    rows = []
    for provider, tech, fee, plans in PROVIDERS:
        for name, down, up, latency, price, cap in plans:
            rows.append([provider, tech, name, down, up, latency,
                         price, fee, cap])
    # Plan IDs are assigned in sheet order, matching the provider blocks
    # a printed comparison sheet would use.
    return [["IP-%d" % (101 + i)] + row for i, row in enumerate(rows)]


def true_cost(row):
    return row[7] + row[8]


def meets_venue(row):
    return (row[4] >= VENUE_DOWN and row[5] >= VENUE_UP
            and row[6] <= VENUE_LATENCY and row[9] == VENUE_CAP)


def verify(rows):
    assert len(rows) == 54, "row count must be 54"
    assert all(len(r) == 10 for r in rows), "column count must be 10"
    ids = [r[0] for r in rows]
    assert len(set(ids)) == 54, "plan IDs must be unique"

    # Sticker minimum and true-cost minimum are different plans, and
    # each minimum is unique so the lab has one right answer.
    advertised = [r[7] for r in rows]
    trues = [true_cost(r) for r in rows]
    assert advertised.count(min(advertised)) == 1, "unique sticker min"
    assert trues.count(min(trues)) == 1, "unique true-cost min"
    sticker_min = min(rows, key=lambda r: r[7])
    true_min = min(rows, key=true_cost)
    assert sticker_min[3] == "Basic 25" and sticker_min[7] == 30
    assert true_min[3] == "Essential 100" and true_cost(true_min) == 40
    assert sticker_min[0] != true_min[0], "sticker and true differ"
    assert true_cost(sticker_min) == 45, "Basic 25 true cost is 45"

    # Venue filter: exactly 13 qualifiers, one cheapest.
    qualifiers = [r for r in rows if meets_venue(r)]
    assert len(qualifiers) == 13, "exactly 13 venue qualifiers"
    q_costs = sorted(true_cost(r) for r in qualifiers)
    assert q_costs[0] == 65 and q_costs[1] == 75, "unique cheapest at 65"
    winner = min(qualifiers, key=true_cost)
    assert (winner[1], winner[3]) == ("Sonoran Fiber", "Home 300")

    # Surge 500 fails the venue test on the data cap alone.
    surge = [r for r in rows if r[3] == "Surge 500"][0]
    assert surge[4] >= VENUE_DOWN and surge[5] >= VENUE_UP
    assert surge[6] <= VENUE_LATENCY and surge[9] != VENUE_CAP
    assert true_cost(surge) == 75, "Surge 500 true cost is 75"

    # Satellite latency: every GEO plan fails on latency, every LEO
    # plan passes it, and the technologies differ by more than 10x.
    geo = [r for r in rows if r[2] == "Satellite (GEO)"]
    leo = [r for r in rows if r[2] == "Satellite (LEO)"]
    assert len(geo) == 6 and len(leo) == 6
    assert all(r[6] > VENUE_LATENCY for r in geo), "GEO fails latency"
    assert all(r[6] <= VENUE_LATENCY for r in leo), "LEO passes latency"
    assert min(r[6] for r in geo) > 10 * max(r[6] for r in leo)

    # Cost per Mbps: unique best and worst, and neither is the
    # cheapest monthly plan (the denominator lesson).
    per_mbps = [(true_cost(r) / r[4], r) for r in rows]
    per_mbps.sort(key=lambda pair: pair[0])
    assert per_mbps[0][0] < per_mbps[1][0], "unique best per Mbps"
    assert per_mbps[-1][0] > per_mbps[-2][0], "unique worst per Mbps"
    best, worst = per_mbps[0][1], per_mbps[-1][1]
    assert (best[1], best[3]) == ("Sonoran Fiber", "Pro 2000")
    assert (worst[1], worst[3]) == ("Copper Basin DSL", "Rural 10")
    assert best[3] != true_min[3], "best per Mbps is not cheapest"

    return {
        "count": len(rows),
        "sticker_min": "%s %s at $%d (true $%d)" % (
            sticker_min[1], sticker_min[3], sticker_min[7],
            true_cost(sticker_min)),
        "true_min": "%s %s at $%d" % (
            true_min[1], true_min[3], true_cost(true_min)),
        "venue_qualifiers": len(qualifiers),
        "venue_winner": "%s %s at $%d true" % (
            winner[1], winner[3], true_cost(winner)),
        "best_per_mbps": "%s %s at $%.3f" % (
            best[1], best[3], true_cost(best) / best[4]),
        "worst_per_mbps": "%s %s at $%.2f" % (
            worst[1], worst[3], true_cost(worst) / worst[4]),
        "uploads_20_up": sum(1 for r in rows if r[5] >= 20),
        "true_cost_le_100": sum(1 for r in rows if true_cost(r) <= 100),
        "row2_true_cost": true_cost(rows[0]),
        "geo_latency_range": "%d-%d ms" % (min(r[6] for r in geo),
                                           max(r[6] for r in geo)),
        "leo_latency_range": "%d-%d ms" % (min(r[6] for r in leo),
                                           max(r[6] for r in leo)),
    }


def workbook_bytes(rows):
    wb = Workbook()
    ws = wb.active
    ws.title = "InternetPlans"
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
        print("%s: %s" % (key, value))


if __name__ == "__main__":
    main()
