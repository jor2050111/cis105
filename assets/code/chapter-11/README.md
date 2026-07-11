# Chapter 11 Data Pack: Track the Project

Starter file for Skills Lab 11A. Work at the extracted `cis105` root and
import the file into Airtable from `assets/code/chapter-11/`.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `project-tasks.csv` | CSV, 54 data rows by 11 columns | Skills Lab 11A, all parts, plus the Section 11.1 examples |

## The scenario

This is the task list for a real systems project: Saguaro Hall's move
from a flat booking spreadsheet to the connected Airtable base students
built in Chapter 10. The 54 tasks run across the six phases of the
systems life cycle, so importing the file gives students a working
project tracker. The snapshot was pulled on the status date
**2026-07-11**, when the project is mid-Development and behind schedule,
which is what makes the tracker worth reading.

## Data dictionary

**project-tasks.csv:** one row per task.

| Column | Header | Type in Airtable | Notes |
| ------ | ------ | ---------------- | ----- |
| A | Task ID | Single line text | `T-101` through `T-154`, unique (the primary key) |
| B | Phase | Single select | One of the six life-cycle phases |
| C | Task Name | Single line text | What the task is |
| D | Owner | Single select | Darnell Brooks, Renee Salazar, or Sam Ortiz |
| E | Status | Single select | Not Started, In Progress, Blocked, or Done |
| F | Priority | Single select | High, Medium, or Low |
| G | Estimated Hours | Number | Planned effort |
| H | Start Date | Date | ISO date in 2026 |
| I | Due Date | Date | ISO date in 2026 |
| J | Depends On | Link to Tasks (starts as text) | A Task ID this task waits on, or blank |
| K | Notes | Long text | Free-text task notes |

The six phases, in order: Investigation, Analysis, Design, Development,
Implementation, Maintenance. The project team is the venue manager
(Darnell Brooks, the sponsor), the office manager (Renee Salazar), a
hired IT consultant (Sam Ortiz), and the front-desk staff.

## Engineered properties the chapter and lab rely on

* 54 tasks, nine in each of the six phases, so a group-by-phase view is
  balanced.
* All four statuses appear: Done 28, In Progress 5, Blocked 2, Not
  Started 19.
* Priority: High 27, Medium 23, Low 4.
* Total estimated effort is 246 hours. By phase: Investigation 43,
  Analysis 45, Design 42, Development 42, Implementation 40,
  Maintenance 34.
* Every Depends On value is blank or a valid Task ID, and no task
  depends on itself.
* **One task is at risk:** `T-140` (Run the old and new systems in
  parallel) is In Progress, but the task it depends on, `T-136` (Load
  the historical bookings), is still Not Started. You cannot run a
  meaningful parallel test before the data is loaded. Students find this
  by comparing each task's status to its dependency's status.
* **Overdue work:** on the status date 2026-07-11, 11 tasks are past
  their Due Date and not Done, 6 of them High priority. This is the
  "what needs attention" signal the project readout reports.

## Reproducibility

Seeded synthetic data, base seed 105. The task list is fully specified
in the generator (no random draws) and dates are computed from fixed
phase windows, so rerunning the generator rebuilds the file
byte-identically:

```bash
python3 assets/code/_generators/generate_chapter11_data.py
```

The script's asserts verify every engineered property above before
writing. The generator needs only the Python standard library.

## Source and license

Original content authored for this course. Saguaro Hall, the project
team, and every task are fictional. Copyright 2026 Jorge Vega, Phoenix
College. Provided for CIS105 coursework.
