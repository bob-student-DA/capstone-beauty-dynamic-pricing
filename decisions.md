# Decision and Change Log

| Date | What happened | Action taken | Task 3 section |
|------|---------------|--------------|----------------|
| 2026-10-06 | Profiled Hotel Booking Demand: 119,390 x 32, 37.0% canceled, 4 columns with nulls | Planned handling for each null column | C, D |
| 2026-10-06 | First upload contained an unrelated file (atlantis.csv), not the salon data | Re-downloaded and verified file contents before loading | C (obstacle) |
| 2026-10-06 | Codespace restarted; unsaved profiling scripts lost | New private repo; enabled Auto Save; commit and push every session | B, C (obstacle) |
| 2026-10-06 | New environment was missing pandas | installed correct and necessary libraries, saved requirements.txt | D |
| 2026-10-06 | Salon README: dates shifted per client; times labeled UTC but fall 9:00-18:00 | Treat times local; salon day of week exploratory and hotel used for day-of-week benchmarks analysis | C (governance), C1 |
| 2026-10-06 | Salon profile: 186 appts, 43.9 weeks, 1 provider, approx 4/week, deposits all are $ 0 | Forecast weekly instead of daily; clustering k = 2-4 | B, E |
| 2026-10-06 | Confirmed licenses: salon Apache 2.0, hotel CC BY 4.0 | Cited both as raw data not redistributed | C (governance) |
| 2026-10-08 | Zeng & Lin (2022) used simulated cases only | Replaced with Thommen & Hintermann (2023) field experiment for elasticity values | A |
| 2026-10-08 | Scenario price response assumptions set from Thommen & Hintermann (2023) | Committed scenarios.py before any analysis | B, E3, F1 |
| 2026-10-19 | scenarios.py (committed 10-08) used one elasticity per scenario and varied shift_share 0.3-0.7; Task 2 C4 specifies separate discount/premium elasticities with shift_share ~0.5 | Corrected scenarios.py to match C4 (conservative -0.57/-0.95, base -0.70/-0.70, optimistic -0.95/-0.57, shift_share 0.5); added PRICE_GRID, TRAIN_FRAC, SEED. No results had been generated yet | B, E3 |
| 2026-10-19 | Salon log has one appointment at 1:00 (not noted in Task 2 D4, which listed only the 8:00 and two 18:00 starts) | Kept the row for weekly counts, lead time, status and clustering; excluded it from hour-of-day analysis as a probable entry error (1 of 186 = 0.5%, under the 5% cap). 8:00 and 18:00 snapped to 9:00 and 17:00 as planned | C (obstacle), D |
| 2026-10-19 | Service standardization produced 18 primary services, not the 26 estimated in Task 2 C4 | Add-ons (base color, extra bowls, deep conditioning) and minor services (brow wax, gloss) were treated as flags on the main service rather than separate services; mapping kept in 01_clean_salon | C, D |
| 2026-10-19 | "Free Consultation" (5 bookings) is a $0$ service | Kept in demand and clustering (uses capacity); revenue set to 0 in pricing scenarios (notebook 06) | D, E3 |
| 2026-10-19 | Hotel adr has 1 negative, 1,959 zero-rate this is complimentary, and 1 extreme (5,400) | Flagged adr_valid = False (1,961 rows, 1.6%); kept for booking counts and cancellation rate, excluded from nightlyrate analysis only | D |
| 2026-10-19 | Hotel data has 32,001 exact duplicate rows (26.8%) and no booking ID | Reported, not removed: identical rows may be separate rooms in one group booking (D4) | C1, D |
| 2026-10-19 | Data preparation complete | Planned end Oct 15| B |
| 2026-10-19 | Grid search returned +20% / 0% for every cluster | Evaluated the pre-registered grid policy (A) for H1a/H1b as planned; added a cluster-targeted ±10% comparison policy (B) designed after grid result, reflecting hotel weekday adr spread (6.5%) and the D5a premium-discounts | B, E3, F2 |
| 2026-10-20 | "Free Consultation|Color Correction|" was split on the pipe and counted as add-ons | Stopped splitting on pipes; treated as one service "Consultation"; add-on flag corrected from 39 to 34 bookings | D |
| 2026-10-20 | Median lead time 14.5 days, not 14 as stated in Task 2 D4 | Difference comes from excluding the 2 negative lead times as planned; 14.5 (IQR 4-44.25) used in report | D |
| 2026-10-20 | Hour-of-day booking volume not significant (Kruskal-Wallis p = 0.141) | Tiers kept per the C1 rule and treated as a working hypothesis; lead time by tier (p = 0.040) report as stronger evidence for a true peak premium | E, F1, G1 |
| 2026-10-20 | Training weeks showed a significant upward trend (p = 0.007), which SES doesnt model | Robust trend disappears once startup weeks 0-5 are not included (p = 0.893); holdout mean is below training mean, so SES kept as intended | E3 |
| 2026-10-20 | Demand and forecast completed | Planned end Oct 19 | B |
| 2026-10-20 | First clustering iteration for womens haircut volume (37) dominated scale and consultation had only 3 training bookings | CRISP-DM looped back to data prep: removed consultations from clustering because it was $0 and transformed log volume. k = 4 by lowest DBI (0.781); silhouette 0.337 below 0.40 target, rported as finding | B, E3, F1 |
| 2026-10-20 | Clustering completed | Planned end Oct 22| B |
| 2026-10-20 | Pricing logic needed by both notebook 06 anddashboard | Moved into a shared module (pricing.py) so both use same calcs | D, E2 |
| 2026-10-20 | Evaluation and pricing scenarios complete | Planned end Oct 25| B |
| 2026-10-20 | First dashboard draft (Plotly dropdowns) used heavy analysis terms and was hard for non technical potential business owners to read | Rebuilt as a plain-language single HTML page with one interactive 'what-if tool' (JavaScript, no Plotly); math mirrors pricing.py and verified in notebook 07 | B, G2 |
| 2026-10-20 | Dashboard completed | Planned end Oct 27; finished Oct 20 | B |
| 2026-10-20 | Dashboard terms from the analysis (revenue index, elasticity, scenario) would be hard for non-technical owners to read | Built the Plotly dashboard as a plain-language page: busy/steady/quiet hours, everyday service names, dollars per month, scenario filter labeled Cautious / Most likely / Hopeful; math mirrors pricing.py and is verified in notebook 07 | B, G2 |