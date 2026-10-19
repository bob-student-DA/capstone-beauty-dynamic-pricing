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
| 2026-10-08 | Scenario price-response assumptions set from Thommen & Hintermann (2023) | Committed scenarios.py before any analysis | B, E3, F1 |
| 2026-10-19 | scenarios.py (committed 10-08) used one elasticity per scenario and varied shift_share 0.3-0.7; Task 2 C4 specifies separate discount/premium elasticities with shift_share ~0.5 | Corrected scenarios.py to match C4 (conservative -0.57/-0.95, base -0.70/-0.70, optimistic -0.95/-0.57, shift_share 0.5); added PRICE_GRID, TRAIN_FRAC, SEED. No results had been generated yet | B, E3 |
| 2026-10-19 | Salon log has one appointment at 1:00 (not noted in Task 2 D4, which listed only the 8:00 and two 18:00 starts) | Kept the row for weekly counts, lead time, status and clustering; excluded it from hour-of-day analysis as a probable entry error (1 of 186 = 0.5%, under the 5% cap). 8:00 and 18:00 snapped to 9:00 and 17:00 as planned | C (obstacle), D |
| 2026-10-19 | Service standardization produced 18 primary services, not the 26 estimated in Task 2 C4 | Add-ons (base color, extra bowls, deep conditioning) and minor services (brow wax) were treated as flags on the main service rather than separate services; mapping kept in 01_clean_salon | C, D |
| 2026-10-19 | "Free Consultation" (5 bookings) is a no-charge service | Kept in demand and clustering (uses capacity); revenue weight set to 0 in pricing scenarios (notebook 06) | D, E3 |