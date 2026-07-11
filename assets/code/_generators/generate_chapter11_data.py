"""Generate the Chapter 11 Skills Lab data pack (Airtable: Track the
Project).

One CSV file, project-tasks.csv, is the task list for a real systems
project: Saguaro Hall's move from a flat booking spreadsheet to the
connected Airtable base students built in Chapter 10. The 54 tasks run
across the six phases of the systems life cycle, so a student who
imports the file into Airtable can group by phase, track status on a
Kanban board, spot overdue work, and find the one task that is running
ahead of a prerequisite that has not started.

Base seed 105 (documented in HANDOFF.md). The task list is fully
specified below (no random draws), and dates are computed from fixed
phase windows, so every run is byte-identical.

The status date (the day this snapshot was pulled) is 2026-07-11. As of
that day the project is mid-Development, so the early phases read Done,
Development is a mix, and the later phases are mostly Not Started.

Engineered properties (each verified by an assert below):
* 54 rows by 11 columns (clears the 50-by-5 floor).
* All six phases appear, nine tasks each, so a group-by-phase view is
  balanced.
* All four statuses appear (Not Started, In Progress, Blocked, Done).
* Every Depends On value is either blank or a valid Task ID.
* Exactly one task is "at risk": it is In Progress while the task it
  depends on is still Not Started (a state that cannot be true, the
  planted flaw students find). Its ID is reported.
* A known set of tasks is overdue: past its Due Date on the status date
  and not yet Done. The count and the High-priority subset are reported.

Rebuild:  python3 assets/code/_generators/generate_chapter11_data.py
"""

import csv
import hashlib
import io
from datetime import date, timedelta

BASE_SEED = 105  # no random draws; the task list below is the source
OUTPUT_PATH = "assets/code/chapter-11/project-tasks.csv"
STATUS_DATE = date(2026, 7, 11)

HEADERS = ["Task ID", "Phase", "Task Name", "Owner", "Status",
           "Priority", "Estimated Hours", "Start Date", "Due Date",
           "Depends On", "Notes"]

# Each phase has a start date and a step (days between task starts).
PHASE_WINDOWS = {
    "Investigation": (date(2026, 1, 13), 4),
    "Analysis": (date(2026, 2, 17), 4),
    "Design": (date(2026, 3, 24), 4),
    "Development": (date(2026, 4, 21), 5),
    "Implementation": (date(2026, 6, 23), 6),
    "Maintenance": (date(2026, 7, 28), 9),
}

# The task list. Each row:
# (Phase, Task Name, Owner, Status, Priority, Hours, Depends On, Notes)
# Depends On is a Task ID string ("" if none). Task IDs are assigned
# T-101.. in this order, so the phase ID ranges are:
#   Investigation T-101..T-109, Analysis T-110..T-118,
#   Design T-119..T-127, Development T-128..T-136,
#   Implementation T-137..T-145, Maintenance T-146..T-154.
TASKS = [
    # ---- Investigation (T-101..T-109), all Done ----
    ("Investigation", "Document the current booking pain points",
     "Renee Salazar", "Done", "High", 6, "",
     "Double-bookings and drifted contact numbers"),
    ("Investigation", "Interview front-desk staff on the current process",
     "Renee Salazar", "Done", "Medium", 5, "T-101", ""),
    ("Investigation", "Estimate the cost of the manual process",
     "Renee Salazar", "Done", "Medium", 4, "T-102", "Staff hours per week"),
    ("Investigation", "Define project scope and goals",
     "Darnell Brooks", "Done", "High", 5, "T-101",
     "One connected base, no lost bookings"),
    ("Investigation", "Assess technical feasibility",
     "Sam Ortiz", "Done", "High", 6, "T-104",
     "Can staff run a browser tool?"),
    ("Investigation", "Assess economic feasibility and budget",
     "Darnell Brooks", "Done", "High", 5, "T-104", "Free-plan target"),
    ("Investigation", "Assess operational feasibility with staff",
     "Renee Salazar", "Done", "Medium", 4, "T-105", ""),
    ("Investigation", "Write the preliminary findings report",
     "Renee Salazar", "Done", "Medium", 6, "T-105", ""),
    ("Investigation", "Get sponsor approval to proceed",
     "Darnell Brooks", "Done", "High", 2, "T-108", "Go/no-go gate"),
    # ---- Analysis (T-110..T-118), all Done ----
    ("Analysis", "Gather booking requirements from staff",
     "Renee Salazar", "Done", "High", 6, "T-109", ""),
    ("Analysis", "Gather requirements from event clients",
     "Renee Salazar", "Done", "Medium", 5, "T-109", ""),
    ("Analysis", "Analyze the current flat export",
     "Sam Ortiz", "Done", "High", 5, "T-110",
     "The denormalized booking CSV"),
    ("Analysis", "List the fields a booking must capture",
     "Sam Ortiz", "Done", "Medium", 4, "T-112", ""),
    ("Analysis", "Define the customer-to-booking relationship",
     "Sam Ortiz", "Done", "High", 5, "T-113",
     "One customer, many bookings"),
    ("Analysis", "Evaluate build versus buy versus subscribe",
     "Darnell Brooks", "Done", "High", 6, "T-112",
     "Decision memo for the sponsor"),
    ("Analysis", "Compare Airtable, Access, and a custom build",
     "Sam Ortiz", "Done", "Medium", 5, "T-115", ""),
    ("Analysis", "Write the requirements specification",
     "Renee Salazar", "Done", "High", 7, "T-114", ""),
    ("Analysis", "Get sign-off on the requirements",
     "Darnell Brooks", "Done", "High", 2, "T-117", "Requirements gate"),
    # ---- Design (T-119..T-127), mostly Done, two slipped ----
    ("Design", "Design the Bookings and Customers tables",
     "Sam Ortiz", "Done", "High", 6, "T-118", ""),
    ("Design", "Choose the primary keys",
     "Sam Ortiz", "Done", "High", 3, "T-119", "Booking ID, Organization"),
    ("Design", "Define every field type",
     "Sam Ortiz", "Done", "Medium", 5, "T-120", ""),
    ("Design", "Design the linked relationship",
     "Sam Ortiz", "Done", "High", 4, "T-120", ""),
    ("Design", "Design the four working views",
     "Sam Ortiz", "Done", "Medium", 5, "T-121",
     "Grid, Calendar, Kanban, Form"),
    ("Design", "Design the least-privilege access levels",
     "Sam Ortiz", "Blocked", "High", 4, "T-122",
     "Waiting on the sponsor's staff-role list"),
    ("Design", "Design the client intake form",
     "Renee Salazar", "Done", "Medium", 4, "T-123", ""),
    ("Design", "Build a clickable prototype base",
     "Sam Ortiz", "In Progress", "High", 8, "T-124", ""),
    ("Design", "Review the prototype with front-desk staff",
     "Renee Salazar", "Not Started", "Medium", 3, "T-126", ""),
    # ---- Development (T-128..T-136), the current phase, a mix ----
    ("Development", "Create the Airtable base",
     "Sam Ortiz", "Done", "High", 3, "T-125", ""),
    ("Development", "Import and clean the bookings data",
     "Sam Ortiz", "Done", "High", 5, "T-128", ""),
    ("Development", "Build the Customers table",
     "Sam Ortiz", "Done", "Medium", 4, "T-129", ""),
    ("Development", "Build the linked-record relationship",
     "Sam Ortiz", "In Progress", "High", 5, "T-130", ""),
    ("Development", "Configure field types and validation",
     "Sam Ortiz", "In Progress", "Medium", 5, "T-131", ""),
    ("Development", "Build the four views",
     "Sam Ortiz", "Not Started", "Medium", 6, "T-131", ""),
    ("Development", "Set up the client intake form",
     "Renee Salazar", "Not Started", "Medium", 4, "T-133", ""),
    ("Development", "Configure permissions and collaborators",
     "Sam Ortiz", "Blocked", "High", 4, "T-124",
     "Blocked by the access-level design"),
    ("Development", "Load the historical bookings",
     "Renee Salazar", "Not Started", "High", 6, "T-129", ""),
    # ---- Implementation (T-137..T-145), mostly ahead, the plant ----
    ("Implementation", "Choose a conversion strategy",
     "Darnell Brooks", "Done", "High", 4, "T-115",
     "Parallel run chosen"),
    ("Implementation", "Write the staff training guide",
     "Renee Salazar", "In Progress", "Medium", 6, "T-132", ""),
    ("Implementation", "Train the front-desk staff",
     "Renee Salazar", "Not Started", "High", 5, "T-138", ""),
    ("Implementation", "Run the old and new systems in parallel",
     "Renee Salazar", "In Progress", "High", 10, "T-136",
     "Two-week overlap with the old system"),
    ("Implementation", "Test the intake form with a real client",
     "Renee Salazar", "Not Started", "Medium", 3, "T-133", ""),
    ("Implementation", "Cut over to the new base",
     "Darnell Brooks", "Not Started", "High", 4, "T-140", "Go-live"),
    ("Implementation", "Decommission the old spreadsheet",
     "Sam Ortiz", "Not Started", "Low", 2, "T-142", ""),
    ("Implementation", "Hold a post-launch check-in",
     "Darnell Brooks", "Not Started", "Medium", 2, "T-142", ""),
    ("Implementation", "Confirm no bookings were lost in the move",
     "Renee Salazar", "Not Started", "High", 4, "T-142", ""),
    # ---- Maintenance (T-146..T-154), all Not Started ----
    ("Maintenance", "Schedule monthly data audits",
     "Renee Salazar", "Not Started", "Medium", 3, "T-142", ""),
    ("Maintenance", "Set up a weekly export backup",
     "Sam Ortiz", "Not Started", "High", 3, "T-142",
     "The 3-2-1 habit from Chapter 6"),
    ("Maintenance", "Collect user feedback for one month",
     "Renee Salazar", "Not Started", "Low", 4, "T-143", ""),
    ("Maintenance", "Fix issues reported after launch",
     "Sam Ortiz", "Not Started", "Medium", 6, "T-144", ""),
    ("Maintenance", "Add a monthly revenue report view",
     "Sam Ortiz", "Not Started", "Low", 4, "T-149",
     "Requested enhancement"),
    ("Maintenance", "Review access levels quarterly",
     "Darnell Brooks", "Not Started", "Medium", 2, "T-142", ""),
    ("Maintenance", "Audit for duplicate customer records",
     "Sam Ortiz", "Not Started", "Medium", 3, "T-146", ""),
    ("Maintenance", "Plan an automated reminder feature",
     "Sam Ortiz", "Not Started", "Low", 5, "T-150",
     "Possible Chapter 12 macro work"),
    ("Maintenance", "Write the one-page user guide",
     "Renee Salazar", "Not Started", "Medium", 4, "T-143", ""),
]


def build_rows():
    rows = []
    # Assign Task IDs and per-phase computed dates.
    phase_index = {}
    for offset, task in enumerate(TASKS):
        (phase, name, owner, status, priority, hours,
         depends, notes) = task
        i = phase_index.get(phase, 0)
        phase_index[phase] = i + 1
        start_base, step = PHASE_WINDOWS[phase]
        start = start_base + timedelta(days=i * step)
        # Due date scales with the estimated hours, minimum three days.
        due = start + timedelta(days=max(3, hours // 2 + 2))
        task_id = "T-%03d" % (101 + offset)
        rows.append([task_id, phase, name, owner, status, priority,
                     hours, start.isoformat(), due.isoformat(),
                     depends, notes])
    return rows


def verify(rows):
    assert len(rows) == 54, "54 tasks"
    assert all(len(r) == 11 for r in rows), "11 columns"
    ids = [r[0] for r in rows]
    assert len(set(ids)) == 54, "unique task IDs"
    id_set = set(ids)
    by_id = {r[0]: r for r in rows}

    phases = ["Investigation", "Analysis", "Design", "Development",
              "Implementation", "Maintenance"]
    phase_counts = {p: sum(1 for r in rows if r[1] == p) for p in phases}
    assert set(phase_counts) == set(phases), "all six phases present"
    assert all(c == 9 for c in phase_counts.values()), "nine tasks each"

    statuses = {r[4] for r in rows}
    assert statuses == {"Not Started", "In Progress", "Blocked", "Done"}, \
        "all four statuses appear"

    # Dependencies resolve.
    for r in rows:
        dep = r[9]
        assert dep == "" or dep in id_set, "Depends On is blank or valid"
        assert dep != r[0], "a task cannot depend on itself"

    # The at-risk plant: In Progress while its dependency is Not Started.
    STATUS = 4
    at_risk = []
    for r in rows:
        dep = r[9]
        if dep and r[STATUS] == "In Progress" \
                and by_id[dep][STATUS] == "Not Started":
            at_risk.append(r[0])
    assert len(at_risk) == 1, "exactly one at-risk task"

    # Overdue: past Due Date on the status date and not Done.
    overdue = [r for r in rows
               if date.fromisoformat(r[8]) < STATUS_DATE
               and r[STATUS] != "Done"]
    overdue_ids = [r[0] for r in overdue]
    overdue_high = [r[0] for r in overdue if r[5] == "High"]
    # Pin the figures the chapter, lab, and README publish, so a future
    # edit to the task list cannot silently drift them.
    assert len(overdue) == 11, "eleven tasks overdue on the status date"
    assert len(overdue_high) == 6, "six overdue tasks are High priority"

    hours_by_phase = {p: sum(r[6] for r in rows if r[1] == p)
                      for p in phases}
    status_counts = {s: sum(1 for r in rows if r[4] == s)
                     for s in ["Done", "In Progress", "Blocked",
                               "Not Started"]}
    priority_counts = {p: sum(1 for r in rows if r[5] == p)
                       for p in ["High", "Medium", "Low"]}
    assert status_counts == {"Done": 28, "In Progress": 5,
                             "Blocked": 2, "Not Started": 19}, \
        "status counts pinned to the published figures"
    assert priority_counts == {"High": 27, "Medium": 23, "Low": 4}, \
        "priority counts pinned to the published figures"
    assert sum(r[6] for r in rows) == 246, "total hours pinned to 246"

    return {
        "tasks": len(rows),
        "phase_counts": phase_counts,
        "status_counts": status_counts,
        "priority_counts": priority_counts,
        "total_hours": sum(r[6] for r in rows),
        "hours_by_phase": hours_by_phase,
        "at_risk_task": at_risk[0],
        "at_risk_depends_on": by_id[at_risk[0]][9],
        "overdue_count": len(overdue),
        "overdue_ids": overdue_ids,
        "overdue_high": overdue_high,
    }


def csv_bytes(headers, rows):
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def main():
    rows = build_rows()
    stats = verify(rows)

    payload = csv_bytes(HEADERS, rows)
    again = csv_bytes(HEADERS, build_rows())
    assert hashlib.md5(payload).hexdigest() == \
        hashlib.md5(again).hexdigest(), "CSV bytes reproducible"

    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)
    print("wrote %s (md5 %s, %d bytes)"
          % (OUTPUT_PATH, hashlib.md5(payload).hexdigest(), len(payload)))

    print("---- answer key ----")
    for key, value in stats.items():
        print("%s: %s" % (key, value))


if __name__ == "__main__":
    main()
