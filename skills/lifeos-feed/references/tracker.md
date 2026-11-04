# Task store spec

Tables: `sprints`, `plan_items`, `log_entries`, `decisions`, `questions`, `flags`, `day_reports`. History tables (append-only): `readings`, `snapshots`, `findings`.

| Table | Key columns |
|---|---|
| sprints | id, week_start, priorities, status |
| plan_items | id, sprint_id, title, outcome, size, status, carried_from |
| log_entries | id, ts, what, evidence, tag, status |
| decisions / questions / flags | id, ts, text, owner, status |
| day_reports | id, date, kind (start or end), audience, body |
| readings | id, plan_item_id, metric, value, taken_at (baseline flagged) |

Write order: log_entries, then plan_items status, then day_reports. Quality gate as column checks: no empty evidence, every plan item has an outcome, at most two in_progress. Read through named views (`v_open_items`, `v_day`, `v_week`). A user-owned store may rename columns; map once and keep the mapping in EntityOS.
