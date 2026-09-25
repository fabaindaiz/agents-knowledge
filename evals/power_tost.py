#!/usr/bin/env python3
"""Monte Carlo operating characteristics for Study 2 (PROTOCOL-general.md). Standard library only.

    python3 evals/power_tost.py [--margin 0.10] [--tasks 60 120] [--reps 3] [--hetero 0.10 0.20 0.30]
                                [--alpha 0.05] [--sims 2000]

power.py answers one question: how often a paired t-test detects an effect. A falsifiable "no effect"
or "no harm" hypothesis needs more numbers, and this prints them for each true effect:

- P(sig)     two-sided paired t-test at --alpha (pass the Holm-adjusted level for a family)
- P(harm)    significant and negative
- P(NI)      one-sided 95% lower bound above -margin (non-inferiority declared)
- P(TOST)    90% interval inside +-margin (equivalence declared)

Read them as the protocol's severity check: with the true effect at 0, P(TOST) and P(NI) are the chances
the study corroborates "no effect" and "no harm"; with the true effect at -margin, P(harm) is the chance
it refutes "no harm", and P(NI) and P(TOST) are the error rates of those claims, which must stay near 0.05.

Binary outcome. Each task draws a baseline success probability from Beta(A, B); the treated arm adds a
per-task effect drawn from Normal(nominal, hetero), clipped to [0, 1]. Clipping shrinks the realised
effect, so the nominal effect is solved for, by bisection, to make the REALISED mean effect equal the
target (the effect column is always the realised one).

This is the unclustered approximation. The frozen analysis script's simulation mode, with the real
cluster structure, supersedes these figures at G0.
"""
import argparse
import math
import random
import statistics
from statistics import NormalDist


def t_quantile(p: float, df: int) -> float:
    """Cornish-Fisher expansion of the t quantile; accurate to about 0.01 for df >= 10."""
    z = NormalDist().inv_cdf(p)
    g1 = (z ** 3 + z) / 4
    g2 = (5 * z ** 5 + 16 * z ** 3 + 3 * z) / 96
    return z + g1 / df + g2 / df ** 2


def realised(nominal, a, b, hetero, rng, draws=40000):
    tot = 0.0
    for _ in range(draws):
        p0 = rng.betavariate(a, b)
        tot += min(1.0, max(0.0, p0 + rng.gauss(nominal, hetero))) - p0
    return tot / draws


def nominal_for(target, a, b, hetero, rng):
    if target == 0:
        return 0.0
    lo, hi = (target * 3, target) if target < 0 else (target, target * 3)
    for _ in range(18):
        mid = (lo + hi) / 2
        if realised(mid, a, b, hetero, rng) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def simulate(n, k, nominal, a, b, hetero, margin, alpha, sims, rng):
    sig = ni = tost = harm = 0
    t2, t1 = t_quantile(1 - alpha / 2, n - 1), t_quantile(0.95, n - 1)
    for _ in range(sims):
        diffs = []
        for _ in range(n):
            p0 = rng.betavariate(a, b)
            p1 = min(1.0, max(0.0, p0 + rng.gauss(nominal, hetero)))
            diffs.append(sum(rng.random() < p1 for _ in range(k)) / k
                         - sum(rng.random() < p0 for _ in range(k)) / k)
        m = statistics.fmean(diffs)
        se = (statistics.stdev(diffs) or 1e-9) / math.sqrt(n)
        s = abs(m / se) > t2
        sig += s
        harm += s and m < 0
        ni += m - t1 * se > -margin
        tost += (m - t1 * se > -margin) and (m + t1 * se < margin)
    return sig / sims, harm / sims, ni / sims, tost / sims


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-a", type=float, default=0.6)
    ap.add_argument("--base-b", type=float, default=0.6)
    ap.add_argument("--margin", type=float, default=0.10)
    ap.add_argument("--tasks", type=int, nargs="+", default=[60, 120])
    ap.add_argument("--reps", type=int, nargs="+", default=[3])
    ap.add_argument("--hetero", type=float, nargs="+", default=[0.10, 0.20, 0.30])
    ap.add_argument("--alpha", type=float, default=0.05, help="two-sided level of the significance test")
    ap.add_argument("--sims", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20260924)
    a = ap.parse_args(argv)
    rng = random.Random(a.seed)
    m = a.margin
    print(f"Baseline Beta({a.base_a}, {a.base_b}), margin +-{m * 100:.0f} pp, significance at alpha {a.alpha}, "
          f"{a.sims} simulations per row; effects are realised means\n")
    print("| Effect SD | Tasks | Reps | Realised effect | P(sig) | P(harm) | P(NI) | P(TOST) |")
    print("|---:|---:|---:|---:|---:|---:|---:|---:|")
    for h in a.hetero:
        noms = {e: nominal_for(e, a.base_a, a.base_b, h, rng) for e in (0.0, -m, m)}
        for n in a.tasks:
            for k in a.reps:
                for e, nom in noms.items():
                    r = simulate(n, k, nom, a.base_a, a.base_b, h, m, a.alpha, a.sims, rng)
                    print(f"| {h * 100:.0f} pp | {n} | {k} | {e * 100:+.0f} pp | "
                          f"{r[0]:.2f} | {r[1]:.2f} | {r[2]:.2f} | {r[3]:.2f} |")


if __name__ == "__main__":
    main()
