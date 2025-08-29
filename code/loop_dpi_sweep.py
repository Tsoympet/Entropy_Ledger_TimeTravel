
# loop_dpi_sweep.py
import numpy as np
import matplotlib.pyplot as plt

def mutual_information_binary(p):
    def h2(x):
        x = max(1e-12, min(1-1e-12, x))
        return -x*np.log2(x) - (1-x)*np.log2(1-x)
    return 1 - h2(p)

def run():
    rng = np.random.default_rng(123)
    ps = np.logspace(-3, -0.05, 20)
    I_emp = []
    bound = []
    for p_succ in ps:
        trials = 200000
        F = rng.integers(0,2,size=trials)
        success = rng.random(trials) < p_succ
        noise = 0.05
        flip = rng.random(trials) < noise
        P = rng.integers(0,2,size=trials)
        P[success] = F[success] ^ flip[success]
        if success.sum()>0:
            err = (P[success]!=F[success]).mean()
            I_succ = mutual_information_binary(err)
        else:
            I_succ = 0.0
        I_total = p_succ * I_succ
        I_emp.append(I_total)
        bound.append(-np.log2(max(1e-12,p_succ)))
    ps = np.array(ps)
    I_emp = np.array(I_emp)
    bound = np.array(bound)

    plt.figure()
    plt.plot(ps, I_emp, label="Empirical loop gain per attempt")
    plt.plot(ps, bound, label=r"Loop-DPI bound $-\log_2 p_{succ}$")
    plt.xscale("log")
    plt.xlabel("Success probability $p_{succ}$")
    plt.ylabel("Bits per attempt")
    plt.title("Empirical Loop Gain vs Theoretical Bound")
    plt.legend()
    plt.savefig("../tex/figures/empirical_vs_bound.pdf", bbox_inches="tight")

if __name__ == "__main__":
    run()
