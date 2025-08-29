
# single_shot_smoothed_bounds.py
"""
Generates a plot illustrating single-shot (smoothed) entropy bounds:
We estimate achievable bits per attempt using smooth min-entropy H_min^δ and
compare to the Loop-DPI asymptote. This is a conceptual surrogate using
empirical frequencies and the bound:
    achievable <= H_0^δ(X) - H_min^δ(X|Y)
for a binary-variable toy with heralding success p_succ.
"""
import numpy as np
import matplotlib.pyplot as plt

def H_min_smooth(pmax, delta):
    # H_min^δ ≈ -log2( max(p) - δ ), clipped
    val = max(1e-12, pmax - delta)
    return -np.log2(val)

def H0_smooth(support, delta):
    # H0^δ ≈ log2( support + 2*delta ) as a crude surrogate
    return np.log2(max(1.0, support + 2*delta))

def run():
    rng = np.random.default_rng(2025)
    deltas = [0.0, 1e-3, 5e-3, 1e-2]
    ps = np.logspace(-3, -0.05, 30)
    plt.figure()
    for delta in deltas:
        ach = []
        for p in ps:
            # Toy binary with success p; on success, channel error e=0.05
            e = 0.05
            # Conditional max-prob for (X|Y, success) ~ max(1-e, e)
            pmax = max(1-e, e)
            Hmin = H_min_smooth(pmax, delta)
            H0 = H0_smooth(2, delta)   # binary support
            # Per attempt achievable bits <= p * (H0 - Hmin)
            ach_bits = p * max(0.0, H0 - Hmin)
            ach.append(ach_bits)
        plt.plot(ps, ach, label=f"one-shot upper (δ={delta})")
    # Add Loop-DPI asymptote
    bound = -np.log2(ps)
    plt.plot(ps, bound, label=r"Loop-DPI $-\log_2 p_{succ}$")
    plt.xscale("log")
    plt.xlabel("Success probability $p_{succ}$")
    plt.ylabel("Bits per attempt")
    plt.title("Single-shot smoothed entropy bounds vs Loop-DPI")
    plt.legend()
    plt.savefig("../tex/figures/one_shot_smoothed.pdf", bbox_inches="tight")

if __name__ == "__main__":
    run()
