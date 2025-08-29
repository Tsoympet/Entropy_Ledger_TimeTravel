
# pareto_tradeoff.py
import numpy as np
import matplotlib.pyplot as plt

def h2(x):
    x = max(1e-12, min(1-1e-12, x))
    return -x*np.log2(x) - (1-x)*np.log2(1-x)

def KL_div(a,b):
    eps=1e-12
    a=np.clip(a,eps,1); b=np.clip(b,eps,1)
    return np.sum(a*np.log2(a/b))

def run():
    ps = np.logspace(-3, -0.1, 30)
    q_vals = np.linspace(0.0, 0.4, 10)
    pts = []
    for p in ps:
        for q in q_vals:
            noise = 0.05
            Tadv = p * (1 - h2(noise))
            prior = np.array([1-p, p])
            mass_remove = q * prior[1]
            p_star = np.array([prior[0] + mass_remove, prior[1] - mass_remove])
            p_star = p_star / p_star.sum()
            ED = KL_div(prior, p_star)
            pts.append((Tadv, ED))
    pts = np.array(pts)
    order = np.argsort(pts[:,0])
    x = pts[order,0]
    y = pts[order,1]
    y_env = np.minimum.accumulate(y[::-1])[::-1]
    plt.figure()
    plt.scatter(pts[:,0], pts[:,1], s=8, alpha=0.5, label="Feasible points")
    plt.plot(x, y_env, label="Pareto-like envelope")
    plt.xlabel("Temporal Advantage (bits per attempt)")
    plt.ylabel("Entropy Debt (bits, kT=1)")
    plt.title("Trade-off between Temporal Advantage and Entropy Debt")
    plt.legend()
    plt.savefig("../tex/figures/pareto_frontier.pdf", bbox_inches="tight")

if __name__ == "__main__":
    run()
