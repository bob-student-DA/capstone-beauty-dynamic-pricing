# scenarios.py
# Price respons assumptions for pricing scenario analysis
# Locked before results  generated (Task 2, section C4)
# Source: Thommen & Hintermann (2023) field experiment on off-peak discounts.
#
#   e_disc      : elasticity of off-peak demand to a discount
#                 (how many new off-peak bookings a discount attracts)
#   e_prem      : elasticity of peak demand to a premium
#                 (how many peak clients a premium pushes out)
#   shift_share : share of clients pushed out of peak who rebook off peak
#                 instead of leaving
#
# Paper range: -0.57 (morning trains) to -0.95 (evening trains), -0.70 overall.
# Conservative = weakest discount response + strongest peak drop-out.
# Optimistic   = strongest discount response + weakest peak drop-out.

SCENARIOS = {
    "conservative": {"e_disc": -0.57, "e_prem": -0.95, "shift_share": 0.5},
    "base":         {"e_disc": -0.70, "e_prem": -0.70, "shift_share": 0.5},
    "optimistic":   {"e_disc": -0.95, "e_prem": -0.57, "shift_share": 0.5},
}

# Premium and discount levels tested (C4), capped at 20% (C5 criterion 4)
PRICE_GRID = [0.00, 0.05, 0.10, 0.15, 0.20]

# Chronological split for tiers forecast and pricing (C1, C4)
TRAIN_FRAC = 0.70

# Fixed seed for K-Means, bootstrap CIs (C3 reproducibility)
SEED = 42