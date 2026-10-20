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
pricing.py           Pricing model shared by notebooks 06 and 07
decisions.md         Log of every deviation from the Task 2 plan
hair_salon_apts.py   Salon profiling script
hotel_bookings.py    Hotel profiling script
notebooks/
  01_clean_salon         Clean salon log, standardize services, engineer features
  02_clean_hotel         Clean hotel benchmark
  03_demand_eda          Demand tiers, hour/weekday tests, hotel benchmark, lead time
  04_forecast            Weekly forecast vs naive baseline (H1c)
  05_clustering          K-Means service clusters
  06_pricing_scenarios   Tiered pricing scenarios, H1a/H1b, C5 scorecard
  07_dashboard           Owner dashboard (plain-language HTML page)
outputs/
  figures/             Charts used in the report
  tables/              Tiers, clusters, scenario results, recommendations
  owner_dashboard.html Open in any browser
```

## Methods

- Methodology used is CRISP-DM (Chapman et al., 2000)
- Tools: Python (pandas, NumPy, SciPy, statsmodels, scikit-learn, Matplotlib) in Jupyter
  notebooks, VS Code in GitHub Codespaces
- Price-response assumptions from Thommen & Hintermann (2023), tested under conservative,
  base, and optimistic scenarios

## Reproducibility

Library versions are pinned in `requirements.txt`; random seeds and the train/holdouts are fixed in
`scenarios.py`.