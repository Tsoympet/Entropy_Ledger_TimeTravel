
# iontrap_heralding_sim.py
"""
Toy schematic for an ion-trap style heralded postselection using an ancilla readout.
No external deps; this is a probabilistic surrogate capturing success rate and info gain.
"""
import numpy as np
from math import log2

def h2(x):
    x = max(1e-12, min(1-1e-12, x))
    return -x*np.log2(x) - (1-x)*np.log2(1-x)

def run(trials=200000, p_succ=0.05, readout_error=0.01, coupling_noise=0.03, seed=42):
    rng = np.random.default_rng(seed)
    F = rng.integers(0,2,size=trials)
    # Heralded success with false positives/negatives from readout error
    herald_true = rng.random(trials) < p_succ
    herald_obs = herald_true ^ (rng.random(trials) < readout_error)
    success = herald_obs & herald_true

    # On success, present bit correlates with F with noise from coupling
    flip = rng.random(trials) < coupling_noise
    P = rng.integers(0,2,size=trials)
    P[success] = F[success] ^ flip[success]

    if success.sum()>0:
        err = (P[success]!=F[success]).mean()
        I_succ = 1 - h2(err)
    else:
        I_succ = 0.0
    I_total = success.mean() * I_succ
    bound = -np.log2(max(1e-12,success.mean()))
    return {"p_succ_eff": float(success.mean()), "I_bits_per_attempt": float(I_total), "bound_bits": float(bound)}

if __name__ == "__main__":
    print(run())
