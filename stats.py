"""
stats.py - is a gap between two ways of asking real, or could it be chance?

Two standard tools, written out in plain Python (no extra libraries):
  wilson(k, n)        95% confidence range for a pass rate (Wilson score interval)
  fisher_p(a, n1, b, n2)  two-sided Fisher's exact test: how likely a gap at least this big
                          would be if the language made no difference at all
"""

from math import comb, sqrt


def wilson(k, n, z=1.96):
    """95% range for a rate of k successes out of n."""
    if n == 0:
        return 0.0, 0.0
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def fisher_p(a, n1, b, n2):
    """Two-sided Fisher's exact test for a/n1 versus b/n2."""
    total_yes, total = a + b, n1 + n2

    def prob(x):  # chance that group 1 gets exactly x of the successes
        return comb(n1, x) * comb(n2, total_yes - x) / comb(total, total_yes)

    observed = prob(a)
    low, high = max(0, total_yes - n2), min(n1, total_yes)
    return min(1.0, sum(prob(x) for x in range(low, high + 1) if prob(x) <= observed * (1 + 1e-9)))


def compare(results, metric, versions, baseline_for):
    """One row per version: rate, 95% range, and p-value against its English baseline.
    metric: a True/False column of results ('passed_all' or 'followed_format')."""
    rows = []
    for v in versions:
        base = baseline_for(v)
        if base is None or base == v:
            continue
        mine = results.loc[results["language"] == v, metric]
        ref = results.loc[results["language"] == base, metric]
        if mine.empty or ref.empty:
            continue
        k, n, kb, nb = int(mine.sum()), len(mine), int(ref.sum()), len(ref)
        lo, hi = wilson(k, n)
        rows.append({"version": v, "baseline": base, "k": k, "n": n, "kb": kb, "nb": nb,
                     "rate": k / n, "lo": lo, "hi": hi, "base_rate": kb / nb, "p": fisher_p(k, n, kb, nb)})
    return rows
