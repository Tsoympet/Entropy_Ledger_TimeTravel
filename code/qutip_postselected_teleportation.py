
# qutip_postselected_teleportation.py
"""
QuTiP-based toy model of heralded, postselected retrocausality via entanglement-assisted feedback.
Requires: pip install qutip
This is a schematic demonstration; it estimates success probability and loop information per attempt.
"""
import numpy as np
try:
    import qutip as qt
except Exception as e:
    qt = None

def run(trials=2000, depol=0.02, seed=123):
    rng = np.random.default_rng(seed)
    if qt is None:
        print("QuTiP not installed; please `pip install qutip` to run this simulation.")
        return {"p_succ": None, "I_bits_per_attempt": None}

    # Bell pair |Phi+>
    bell = (qt.basis(2,0).tensor(qt.basis(2,0)) + qt.basis(2,1).tensor(qt.basis(2,1))).unit()
    I = qt.qeye(2)
    X = qt.sigmax(); Z = qt.sigmaz()

    succ = 0
    info_bits = 0.0
    for _ in range(trials):
        # Future bit F encoded on qubit A
        F = rng.integers(0,2)
        psiF = qt.basis(2,F)

        # Entangle ancillas (A,B) as a Bell pair and couple psiF to A
        state = psiF.tensor(bell)

        # Dephasing noise channel on path (schematic)
        if depol>0:
            p = depol
            state = (1-p)*state + p*(Z.tensor(I.tensor(I))) * state

        # Bell measurement on (F,B) with heralding of a chosen outcome (postselection)
        # For toy: succeed with probability p_succ; when success, assume perfect classical correlation
        # Here we emulate herald by Bernoulli with p = 0.05 (tunable as function of depol)
        p_succ = max(0.01, 0.2*(1-depol))  # simple heuristic
        if rng.random() < p_succ:
            succ += 1
            # Assume on success, present bit P equals F with small error
            noise = 0.05 + 0.5*depol
            err = 1 if rng.random()<noise else 0
            I_succ = 1.0 - ( - (err*np.log2(err+(err==0)) + (1-err)*np.log2((1-err)+ (1-err==0))) )
            # For binary channel: I = 1 - h2(err); but with err ∈ {0,1} here we approximate:
            if err==0: I_succ = 1.0
            else: I_succ = 0.0
            info_bits += I_succ
    p_emp = succ / trials
    I_per_attempt = info_bits / trials
    return {"p_succ": p_emp, "I_bits_per_attempt": I_per_attempt, "bound_bits": -np.log2(max(1e-12,p_emp))}

if __name__ == "__main__":
    out = run()
    print(out)
