
# multiloop_sim.py
import numpy as np
import matplotlib.pyplot as plt

def run():
    rng = np.random.default_rng(321)
    m_list = [1,2,3,4,5]
    gains = []
    bounds = []
    p = 0.05
    for m in m_list:
        trials = 100000
        successes = rng.random((trials, m)) < p
        any_success = successes.any(axis=1)
        bits_per_success = 0.9
        I_total = (successes.sum(axis=1) * bits_per_success).mean()
        gains.append(I_total)
        cutset = m * (-np.log2(p))
        interf = max(0.0, cutset - (-np.log2(1 - (1-p)**m)))
        bounds.append(cutset - interf)
    plt.figure()
    plt.plot(m_list, gains, marker="o", label="Empirical total gain")
    plt.plot(m_list, bounds, marker="s", label="Network bound (with interference proxy)")
    plt.xlabel("Number of retro-loops (m)")
    plt.ylabel("Bits per attempt")
    plt.title("Multi-loop Network: Gain vs Cut-Set Bound")
    plt.legend()
    plt.savefig("../tex/figures/multiloop_gain.pdf", bbox_inches="tight")

if __name__ == "__main__":
    run()
