"""Generate assets/code/chapter-08/security-audit.xlsx (Skills Lab 8A).

Two worksheets. `AuditChecklist` is the 25-item personal security audit
students score themselves against (five categories, five items each,
0-2 points per item, 10 per category, 50 total). `ClassResults` is 54
anonymized category scores from a class-sized set of the same audit,
seeded synthetic, which gives every chart in the chapter and lab a
stable comparison series. Base seed 105 (documented in HANDOFF.md).
Byte-identical on every run.

Engineered properties (each verified by an assert below):
* ClassResults: 54 data rows by 7 columns (clears the 50-by-5 floor)
* Category averages are strictly ordered Devices > Accounts > Network
  > Privacy > Backups, each gap at least 0.5 points, so "the class is
  weakest exactly where Chapter 6 predicted" has one honest reading
* Backups is the weakest class category (pays the Chapter 6 backup
  thread), Devices the strongest (updates are on by default)
* Overall average total sits in the honest middle (24-28 of 50)
* No implausible rows: every total is at least 8 and at most 46
* The Backups column contains at least five zeros (the to-do list is
  real), and at least three students hold a perfect 10 somewhere
* All scores are integers 0-10, all totals equal the category sum

Rebuild:  python3 assets/code/_generators/generate_chapter08_data.py
"""

import hashlib
import io
import random
import re
import zipfile
from datetime import datetime

from openpyxl import Workbook

BASE_SEED = 105
OUTPUT_PATH = "assets/code/chapter-08/security-audit.xlsx"

CHECKLIST_HEADERS = ["Item ID", "Category", "Audit Item",
                     "Score 0 when", "Score 2 when", "Where to look",
                     "Your Score"]

# 25 items: five categories, five items each. Score 1 = partly true.
CHECKLIST = [
    ("SA-01", "Accounts", "Every important account has its own password",
     "One password unlocks several accounts",
     "No two important accounts share a password",
     "Your memory, or your password manager's reuse report"),
    ("SA-02", "Accounts", "A password manager stores your passwords",
     "Passwords live in your memory or a notebook",
     "A manager (built into the browser or a dedicated app) stores and fills them",
     "Browser or phone settings > Passwords"),
    ("SA-03", "Accounts", "Multifactor authentication protects your email",
     "Email opens with a password alone",
     "A second step (app code, key, or passkey) is required",
     "Your email account's security settings"),
    ("SA-04", "Accounts", "Multifactor authentication protects your money apps",
     "Bank and payment apps use a password alone",
     "Every money account requires a second step",
     "Each bank or payment app's security settings"),
    ("SA-05", "Accounts", "You use passkeys where sites offer them",
     "Never set one up",
     "Passkeys sign you in wherever they are offered",
     "Account security pages, phone passkey settings"),
    ("SA-06", "Devices", "The operating system updates itself",
     "Updates are off, delayed for months, or unknown",
     "Automatic updates are on and the system is current",
     "Windows Update, or macOS Software Update"),
    ("SA-07", "Devices", "Apps and browser stay current",
     "Update prompts get dismissed for weeks",
     "Apps update automatically or promptly",
     "App store updates page, browser About screen"),
    ("SA-08", "Devices", "Every device locks its screen",
     "Any device opens with no PIN or biometric",
     "Every phone and laptop requires a PIN, face, or fingerprint",
     "Lock screen settings on each device"),
    ("SA-09", "Devices", "Device storage is encrypted",
     "Encryption is off or you have never checked",
     "Device encryption, BitLocker, or FileVault is on (phones: on by default with a lock)",
     "Windows: Settings > Privacy & security. Mac: FileVault"),
    ("SA-10", "Devices", "Daily work happens in a standard account",
     "The account you live in is an administrator",
     "Daily account is standard, admin saved for deliberate changes",
     "User account settings (Chapter 4's least-power rule)"),
    ("SA-11", "Network", "Home Wi-Fi uses WPA2 or WPA3 encryption",
     "Network is open or the standard is unknown",
     "WPA2 or WPA3 is verified in router settings",
     "Router app or admin page, security section"),
    ("SA-12", "Network", "The router's admin password is not the factory one",
     "The password on the sticker still works",
     "Admin password changed to your own",
     "Router app or admin page, sign-in"),
    ("SA-13", "Network", "Router software gets updated",
     "Never updated, or you have never checked",
     "Auto-update on, or checked within the year",
     "Router app or admin page, firmware section"),
    ("SA-14", "Network", "Guests and gadgets use a guest network",
     "Everything joins the main network",
     "Visitors and smart-home devices ride a separate guest network",
     "Router app, guest network section (Chapter 7)"),
    ("SA-15", "Network", "Public Wi-Fi gets professional caution",
     "Any task on any open network",
     "Sensitive tasks wait for HTTPS you trust, your hotspot, or home",
     "Your own habits (Chapter 7's channels)"),
    ("SA-16", "Backups", "The files that matter exist in a second place",
     "One copy, on one device",
     "A current second copy exists somewhere else",
     "Count the truly separate places (Chapter 6)"),
    ("SA-17", "Backups", "Backup runs without you",
     "Backups happen when you remember",
     "File History, Time Machine, or cloud backup runs on its own",
     "Backup settings on your computer"),
    ("SA-18", "Backups", "One copy lives somewhere else entirely",
     "Every copy sits in one building",
     "Cloud or off-site copy exists (the 1 in 3-2-1)",
     "Your cloud storage, or the drive at a relative's"),
    ("SA-19", "Backups", "Phone photos and contacts back up automatically",
     "The phone is the only copy",
     "Photos and contacts sync to a cloud account",
     "Phone backup settings"),
    ("SA-20", "Backups", "You have tested a restore",
     "Never tried to get a file back",
     "You have recovered a real file from a backup at least once",
     "Try it: restore one old file today"),
    ("SA-21", "Privacy", "App permissions get reviewed",
     "Never opened the permissions list",
     "Camera, microphone, and location lists reviewed recently",
     "Phone settings > Privacy (Chapter 4)"),
    ("SA-22", "Privacy", "Social accounts had a privacy checkup",
     "Settings are whatever the defaults were",
     "You ran each platform's privacy checkup",
     "Each platform's privacy checkup tool"),
    ("SA-23", "Privacy", "You know what your AI assistant sees and keeps",
     "Never asked the two questions",
     "Checked what it can see and where your prompts go",
     "Assistant settings and data controls (Chapter 4)"),
    ("SA-24", "Privacy", "The browser blocks trackers, and you read cookie prompts",
     "Defaults everywhere, every prompt accepted",
     "Tracking protection on, cookie prompts answered deliberately",
     "Browser settings > Privacy"),
    ("SA-25", "Privacy", "Your email address gets breach-checked",
     "Never checked whether accounts appeared in breaches",
     "Breach alerts on (manager or monitor), and you acted on hits",
     "Password manager alerts or a breach-check site"),
]

RESULT_HEADERS = ["Student ID", "Accounts", "Devices", "Network",
                  "Backups", "Privacy", "Total"]

# Target score profile per category: (weights over 0-10ish draws)
# tuned so Devices > Accounts > Network > Privacy > Backups.
CATEGORY_PROFILES = {
    "Accounts": [3, 4, 5, 5, 6, 6, 6, 7, 7, 8, 9],
    "Devices":  [4, 5, 6, 6, 7, 7, 7, 8, 8, 9, 10],
    "Network":  [2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9],
    "Privacy":  [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8],
    "Backups":  [0, 0, 1, 2, 3, 3, 4, 4, 5, 6, 8],
}


def build_results():
    rng = random.Random(BASE_SEED)
    rows = []
    for i in range(54):
        row = ["ST-%02d" % (i + 1)]
        for cat in ["Accounts", "Devices", "Network", "Backups",
                    "Privacy"]:
            row.append(rng.choice(CATEGORY_PROFILES[cat]))
        row.append(sum(row[1:6]))
        rows.append(row)
    return rows


def verify(rows):
    assert len(rows) == 54, "54 class rows"
    assert all(len(r) == 7 for r in rows), "7 columns"
    ids = [r[0] for r in rows]
    assert len(set(ids)) == 54, "unique student IDs"
    for r in rows:
        assert all(isinstance(v, int) and 0 <= v <= 10 for v in r[1:6])
        assert r[6] == sum(r[1:6]), "total equals category sum"
        assert 8 <= r[6] <= 46, "no implausible totals"

    def avg(col):
        return sum(r[col] for r in rows) / len(rows)

    averages = {"Accounts": avg(1), "Devices": avg(2), "Network": avg(3),
                "Backups": avg(4), "Privacy": avg(5)}
    order = ["Devices", "Accounts", "Network", "Privacy", "Backups"]
    for a, b in zip(order, order[1:]):
        assert averages[a] >= averages[b] + 0.5, \
            "category order %s > %s by 0.5+" % (a, b)

    total_avg = avg(6)
    assert 24 <= total_avg <= 28, "overall average in the honest middle"
    assert sum(1 for r in rows if r[4] == 0) >= 5, "Backups zeros exist"
    assert sum(1 for r in rows
               if 10 in r[1:6]) >= 3, "some perfect categories"

    assert len(CHECKLIST) == 25, "25 audit items"
    cats = [c[1] for c in CHECKLIST]
    for cat in ["Accounts", "Devices", "Network", "Backups", "Privacy"]:
        assert cats.count(cat) == 5, "5 items per category"

    return dict({k: round(v, 2) for k, v in averages.items()},
                total_avg=round(total_avg, 2),
                backups_zeros=sum(1 for r in rows if r[4] == 0))


def workbook_bytes(rows):
    wb = Workbook()
    checklist = wb.active
    checklist.title = "AuditChecklist"
    checklist.append(CHECKLIST_HEADERS)
    for item in CHECKLIST:
        checklist.append(list(item) + [None])

    results = wb.create_sheet("ClassResults")
    results.append(RESULT_HEADERS)
    for row in rows:
        results.append(row)

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
    rows = build_results()
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
