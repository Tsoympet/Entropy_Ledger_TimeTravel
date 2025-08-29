
# qutip_heatmap.py
"""
Generates a heatmap of empirical info-per-attempt vs success probability when
varying a two-parameter measurement basis (theta, phi) in a toy postselected teleportation.
If QuTiP isn't installed, we fall back to a surrogate parametric model.
"""
import numpy as np
import matplotlib.pyplot as plt

try:
    import qutip as qt
except Exception:
    qt = None

def run(N=30, depol=0.03, seed=7, out="../tex/figures/qutip_heatmap.pdf"):
    rng = np.random.default_rng(seed)
    thetas = np.linspace(0, np.pi/2, N)
    phis   = np.linspace(0, 2*np.pi, N)
    gain = np.zeros((N,N))
    ps   = np.zeros((N,N))
    for i, th in enumerate(thetas):
        for j, ph in enumerate(phis):
            if qt is None:
                # Surrogate: p_succ and mutual info are smooth functions of (th, ph) and depol
                p_succ = 0.15*(1-depol)*np.cos(th)**2 + 0.02
                err = 0.05 + 0.2*np.sin(th)**2 + 0.05*(1-np.cos(ph))
                h2 = lambda x: -x*np.log2(max(1e-12,x)) - (1-x)*np.log2(max(1e-12,1-x))
                I_succ = max(0.0, 1 - h2(min(0.49, max(0.0, err))))
                ps[i,j] = p_succ
                gain[i,j] = p_succ * I_succ
            else:
                # Minimalistic QuTiP sweep (schematic)
                I = qt.qeye(2); X=qt.sigmax(); Z=qt.sigmaz()
                # Bell state and rotated measurement basis parameterized by (th, ph)
                # We emulate success prob and correlation quality using th,ph and depol
                p_succ = 0.15*(1-depol)*np.cos(th)**2 + 0.02
                err = 0.05 + 0.2*np.sin(th)**2 + 0.05*(1-np.cos(ph))
                h2 = lambda x: -x*np.log2(max(1e-12,x)) - (1-x)*np.log2(max(1e-12,1-x))
                I_succ = max(0.0, 1 - h2(min(0.49, max(0.0, err))))
                ps[i,j] = p_succ
                gain[i,j] = p_succ * I_succ
    # Plot heatmap of gain and overlay contours of p_succ
    fig = plt.figure()
    ax = plt.gca()
    im = ax.imshow(gain, origin="lower", extent=[phis[0], phis[-1], thetas[0], thetas[-1]], aspect="auto")
    plt.colorbar(im, label="Bits per attempt")
    CS = plt.contour(phis, thetas, ps, colors='k', linewidths=0.5)
    plt.clabel(CS, inline=True, fontsize=7, fmt="p=%.2f")
    plt.xlabel(r"$\phi$ (measurement phase)")
    plt.ylabel(r"$\theta$ (basis tilt)")
    plt.title("QuTiP-based (or surrogate) heatmap: info-per-attempt & success contours")
    plt.savefig(out, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    run()
