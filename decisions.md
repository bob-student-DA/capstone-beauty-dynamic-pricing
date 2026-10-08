# Decision and Change Log

| Date | What happened | Action taken | Task 3 section |
|------|---------------|--------------|----------------|
| 2026-10-06 | Profiled Hotel Booking Demand: 119,390 x 32, 37.0% canceled, 4 columns with nulls | Planned handling for each null column | C, D |
| 2026-10-06 | First upload contained an unrelated file (atlantis.csv), not the salon data | Re-downloaded and verified file contents before loading | C (obstacle) |
| 2026-10-06 | Codespace restarted; unsaved profiling scripts lost | New private repo; enabled Auto Save; commit and push every session | B, C (obstacle) |
| 2026-10-06 | New environment missing pandas | Installed libraries, saved requirements.txt | D |
| 2026-10-06 | Salon README: dates shifted per client; times labeled UTC but fall 9:00-18:00 | Treat times as local; salon day of week exploratory; hotel used for day-of-week benchmark | C (governance), C1 |
| 2026-10-06 | Salon profile: 186 appts, 43.9 weeks, 1 provider, ~4/week, deposits all 0 | Forecast weekly instead of daily; clustering k = 2-4 | B, E |
| 2026-10-06 | Confirmed licenses: salon Apache 2.0, hotel CC BY 4.0 | Cite both; raw data not redistributed | C (governance) |
| 2026-10-08 | Zeng & Lin (2022) used simulated cases only | Replaced with Thommen & Hintermann (2023) field experiment for elasticity values | A |
