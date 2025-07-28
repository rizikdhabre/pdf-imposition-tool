from math import ceil
from typing import List, Tuple

# ---------------------------------------------------------------------------
# 1.  Decide how many 20/24 or 28/32 page signatures we need
# ---------------------------------------------------------------------------

def plan_signatures(total_pages: int) -> Tuple[List[int], int]:
    """
    Return a list with the size of every signature in gathering order
    (28, 32, 28, …) **and** the number of blank pages that must be appended
    to the input PDF so its length matches the plan.

    >>> plan_signatures(152)[0]
    [28, 32, 28, 32, 32]
    """
    # choose family
    if total_pages <= 150:
        base, up = 20, 24
    else:
        base, up = 28, 32

    k, r = divmod(total_pages, base)
    upgrades = ceil(r / 4) if r else 0
    blanks   = upgrades * 4 - r if r else 0

    baseline = k - upgrades  # remaining plain-size signatures

    # gather: always start with base, alternate, then dump the rest
    sigs = []
    use_base = True
    while baseline or upgrades:
        if use_base and baseline:
            sigs.append(base)
            baseline -= 1
        elif not use_base and upgrades:
            sigs.append(up)
            upgrades -= 1
        else:
            sigs.extend([base] * baseline)
            sigs.extend([up]   * upgrades)
            break
        use_base = not use_base
    return sigs, blanks


def panel_count(fold_target: str) -> int:
    """Return number of panels per A4 sheet based on fold level."""
    levels = {"A5": 2, "A6": 4, "A7": 8}
    return levels.get(fold_target.upper(), 2) * 2  # front + back panels


def build_folded_panel_order(total_pages: int, fold_target: str) -> Tuple[List[int], int]:
    """
    Return the page order needed to create a folded booklet.

    This stub assumes no advanced imposition logic — it returns a
    sequential page order for now. Replace with real folding logic later.
    """
    order = list(range(1, total_pages + 1))
    return order, len(order)
