# scenarios.py
# Price-response assumptions for the pricing scenario analysis.
# Set BEFORE any results were generated, per Task 2 section C4.
# Source: Thommen & Hintermann (2023) field experiment on off-peak discounts.
#   - elasticity: % change in bookings for a 1% change in price
#     (paper: about -0.7 overall, ranging from -0.57 to -0.95 by time of day)
#   - shift_share: share of clients lost to a peak premium who rebook
#     off-peak instead of leaving (paper: about half of extra discount sales
#     came from customers who would otherwise have paid full price)

SCENARIOS = {
    "conservative": {"elasticity": -0.57, "shift_share": 0.3},
    "base":         {"elasticity": -0.70, "shift_share": 0.5},
    "optimistic":   {"elasticity": -0.95, "shift_share": 0.7},
}