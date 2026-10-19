### capstone-beauty-dynamic-pricing

# Dynamic Pricing for Appointment-Based Beauty Businesses

WGU B.S. Data Analytics Capstone (D502) — Bobbie Hickman

Can historical slot density be used to set time-based price adjustments that
shift bookings into off-peak hours and increase weekly revenue? This project
applies revenue-management principles (Kimes & Chase, 1998) to one stylist's
appointment log, using hotel booking data as a benchmark.

## Data

Raw data is not redistributed (see licenses). Download both from Kaggle and
place them as shown:

| Dataset | Source | License | Path |
|---|---|---|---|
| Hair Salon Appointments (Anonymous) | [White (2025)](https://www.kaggle.com/datasets/calebhwhite/hair-salon-appointments-anonymous) | Apache 2.0 | `data/salon/appointments_anonymized.csv` |
| Hotel Booking Demand | [Mostipak (2020)](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) | CC BY 4.0 | `data/hotel_bookings.csv` |

## Setup

```bash
pip install -r requirements.txt
```

Run the notebooks in order (Kernel → Restart & Run All).

## Project structure

```
scenarios.py         Price-response assumptions, locked before analysis
decisions.md         Log of every deviation from the Task 2 plan
hair_salon_apts.py   Salon profiling script
hotel_bookings.py    Hotel profiling script
notebooks/
  01_clean_salon     Clean salon log, engineer features
  02_clean_hotel     Clean hotel benchmark
  03_demand_eda      Hour-of-day demand, tiers, diagnostic tests
  04_forecast        Weekly forecast vs naive baseline (H1c)
  05_clustering      K-Means service clusters
  06_pricing         Tiered pricing scenarios (H1a, H1b)
  07_dashboard       Owner dashboard (Plotly HTML)
outputs/             Figures, cluster table, dashboard
```

## Reproducibility

Library versions are pinned in `requirements.txt`; random seeds are fixed in
`scenarios.py`.