
"""
Toy simulation of the Loop-DPI / Entropy Ledger trade-off.

We model a postselected retro-edge with success probability p_succ.
On success, a "future" bit F is perfectly copied back to influence a present bit P.
On failure, no influence is applied and the trial is discarded (heralding).

We compute the net information gain per ATTEMPT as:
    gain = p_succ * I(P;F | success)
which is upper-bounded by -log2(p_succ) in our theory when accounting for optimal
coding strategies and resource normalization.

We also emulate a "paradox tax": if a fraction q of histories are paradoxical
(conflicting constraints), we minimally reweight to remove them and compute
ED ≈ kT * KL(P || P*). We set kT=1 for normalized units.
"""
import numpy as np
from math import log2
import json

def mutual_information_binary(p):
    """MI of a BSC with crossover p when input is fair: I = 1 - h2(p)."""
    def h2(x):
        x = max(1e-12, min(1-1e-12, x))
        return -x*np.log2(x) - (1-x)*np.log2(1-x)
    return 1 - h2(p)

def simulate(p_succ=0.1, noise=0.0, paradox_frac=0.0, trials=100000, seed=42):
    rng = np.random.default_rng(seed)
    F = rng.integers(0,2,size=trials)  # future bit
    success = rng.random(trials) < p_succ

    # On success, present bit P = F flipped by noise; on failure P independent fair
    flip = rng.random(trials) < noise
    P = rng.integers(0,2,size=trials)  # start as fair
    P[success] = F[success] ^ flip[success]

    # Empirical MI across ALL attempts:
    # We estimate MI by conditioning: I_total = p_succ * I(P;F | success)
    # (since when not success, P is independent of F by construction)
    if success.sum() > 0:
        # estimate error rate on successful subset
        err = (P[success] != F[success]).mean()
        I_success = mutual_information_binary(err)
    else:
        I_success = 0.0
    I_total = p_succ * I_success

    # Paradox tax: remove a fraction q of the most conflicting histories.
    # We approximate by upweighting the remaining mass uniformly.
    q = paradox_frac
    KL = 0.0
    if q > 0:
        # prior over histories: success/failure ~ Bernoulli(p_succ)
        # we project onto a set with paradox mass removed
        p_prior = np.array([1-p_succ, p_succ])  # [fail, success]
        p_star = np.array([1-q, 0.0]) * (1.0/(1.0-q)) * np.array([p_prior[0], p_prior[1]])  # naive scaling
        # normalize properly (remove paradox mass q from success channel)
        mass_remove = q * p_prior[1]
        p_star = np.array([p_prior[0] + mass_remove, p_prior[1] - mass_remove])
        p_star = p_star / p_star.sum()
        def KL_div(p, q):
            eps = 1e-12
            p = np.clip(p, eps, 1)
            q = np.clip(q, eps, 1)
            return np.sum(p * np.log2(p/q))
        KL = KL_div(p_prior, p_star)  # in bits; ED ~ kT * KL

    return {
        "p_succ": p_succ,
        "noise": noise,
        "paradox_frac": paradox_frac,
        "I_success_bits": I_success,
        "I_total_bits_per_attempt": I_total,
        "loop_dpi_bound_bits": -np.log2(max(1e-12,p_succ)),
        "entropy_debt_bits": KL
    }

if __name__ == "__main__":
    grid = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    out = [simulate(p, noise=0.05, paradox_frac=0.1) for p in grid]
    print(json.dumps(out, indent=2))
