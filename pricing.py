# Price-response model for the tiered pricing scenario analysis - Task 2 C4
# Revenue is index: one booking at the owners base price = 1 x weight

import numpy as np
import pandas as pd


def apply_pricing(peak, mid, off, prem, disc, e_prem, e_disc, shift_share):
    """
    Return new (peak, mid, off) booking counts under tiered pricing.
    - Peak premium: |e_prem| * prem of peak bookings are lost;
      shift_share of those lost rebook off-peak instead of leaving.
    - Off-peak discount: |e_disc| * disc new off-peak bookings are gained.
    - Mid-tier price is unchanged.
    """
    lost = peak * abs(e_prem) * prem
    shifted = lost * shift_share
    gained = off * abs(e_disc) * disc
    return peak - lost, mid, off + gained + shifted


def revenue(peak, mid, off, prem=0.0, disc=0.0, w=1.0):
    """Revenue index: peak at (1 + prem), mid at 1, off at (1 - disc), times weight."""
    return w * (peak * (1 + prem) + mid + off * (1 - disc))


def evaluate(counts, policy, scenario, weights):
    """
    counts:   DataFrame indexed by (week_index, cluster) with columns peak, mid, off
    policy:   {cluster: (premium, discount)}; clusters not listed stay flat
    scenario: {"e_prem", "e_disc", "shift_share"}
    weights:  {cluster: relative price weight}; missing = 1.0
    Returns one row per week with flat vs tiered revenue and off-peak share.
    """
    rows = []
    for (wk, c), r in counts.iterrows():
        p, d = policy.get(c, (0.0, 0.0))
        w = weights.get(c, 1.0)
        npk, nmd, nof = apply_pricing(r["peak"], r["mid"], r["off"], p, d,
                                      scenario["e_prem"], scenario["e_disc"],
                                      scenario["shift_share"])
        rows.append({
            "week": wk, "cluster": c,
            "flat_rev": revenue(r["peak"], r["mid"], r["off"], w=w),
            "tier_rev": revenue(npk, nmd, nof, p, d, w),
            "flat_off": r["off"], "tier_off": nof,
            "flat_tot": r["peak"] + r["mid"] + r["off"], "tier_tot": npk + nmd + nof,
        })
    wk = pd.DataFrame(rows).groupby("week").sum(numeric_only=True).drop(columns="cluster")
    wk["flat_share"] = np.where(wk["flat_tot"] > 0, wk["flat_off"] / wk["flat_tot"], np.nan)
    wk["tier_share"] = np.where(wk["tier_tot"] > 0, wk["tier_off"] / wk["tier_tot"], np.nan)
    wk["rev_pct_change"] = np.where(wk["flat_rev"] > 0,
                                    (wk["tier_rev"] - wk["flat_rev"]) / wk["flat_rev"] * 100, np.nan)
    return wk