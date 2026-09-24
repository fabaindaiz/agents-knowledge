#!/usr/bin/env python3
"""Monte Carlo power for the primary contrast, before any data exist. Standard library only.

    python3 evals/power.py [--base-a A --base-b B] [--effects 0.1 0.2 0.3] [--tasks 10 20 40]
                           [--reps 2 3 5] [--hetero 0.1] [--sims 2000]

Each simulated task draws a baseline success probability from Beta(A, B): the default is U-shaped,
because agent tasks mostly sit near always-pass or never-pass, and those tasks carry no information.
The condition under test adds a per-task effect drawn from Normal(effect, hetero), clipped to [0, 1].
Each task runs K repetitions per condition; the test is a two-sided paired t-test on the per-task
mean differences, at alpha 0.05. Replace A and B with values fitted to the pilot's baseline rates.
"""
import argparse
import math
import random
import statistics

T975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228,
        12: 2.179, 15: 2.131, 19: 2.093, 20: 2.086, 25: 2.060, 29: 2.045, 30: 2.042, 39: 2.023, 40: 2.021,
        59: 2.001, 60: 2.000, 79: 1.990, 80: 1.990, 119: 1.980}


def tcrit(df):
    keys = sorted(T975)
    for k in keys:
        if df <= k:
            return T975[k]
    return 1.96


def simulate(n, k, effect, a, b, hetero, sims, rng):
    hits = 0
    for _ in range(sims):
        diffs = []
        for _ in range(n):
            p0 = rng.betavariate(a, b)
            p1 = min(1.0, max(0.0, p0 + rng.gauss(effect, hetero)))
            s1 = sum(rng.random() < p1 for _ in range(k)) / k
            s0 = sum(rng.random() < p0 for _ in range(k)) / k
            diffs.append(s1 - s0)
        sd = statistics.stdev(diffs)
        if sd == 0:
            hits += statistics.fmean(diffs) != 0
            continue
        t = statistics.fmean(diffs) / (sd / math.sqrt(n))
        hits += abs(t) > tcrit(n - 1)
    return hits / sims


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-a", type=float, default=0.6)
    ap.add_argument("--base-b", type=float, default=0.6)
    ap.add_argument("--effects", type=float, nargs="+", default=[0.1, 0.2, 0.3])
    ap.add_argument("--tasks", type=int, nargs="+", default=[10, 20, 30, 40, 60])
    ap.add_argument("--reps", type=int, nargs="+", default=[2, 3, 5])
    ap.add_argument("--hetero", type=float, default=0.10)
    ap.add_argument("--sims", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20260924)
    a = ap.parse_args(argv)
    rng = random.Random(a.seed)
    print(f"Power, two-sided paired t-test at alpha 0.05; baseline Beta({a.base_a}, {a.base_b}), "
          f"per-task effect sd {a.hetero}, {a.sims} simulations per cell\n")
    print("| Effect | Reps | " + " | ".join(f"{n} tasks" for n in a.tasks) + " |")
    print("|---:|---:|" + "---:|" * len(a.tasks))
    for e in a.effects:
        for k in a.reps:
            row = [f"{simulate(n, k, e, a.base_a, a.base_b, a.hetero, a.sims, rng):.2f}" for n in a.tasks]
            print(f"| {e * 100:.0f} pp | {k} | " + " | ".join(row) + " |")


if __name__ == "__main__":
    main()
