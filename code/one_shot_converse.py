
# one_shot_converse.py
import numpy as np
import matplotlib.pyplot as plt

def run():
    n_list = [50, 100, 200, 400, 800]
    target_factor = 1.3
    p = 0.05
    errors = []
    for n in n_list:
        err = 1.0 - (p)**(int(n * target_factor))
        errors.append(min(1.0, err))
    plt.figure()
    plt.plot(n_list, errors, marker="o")
    plt.xlabel("Blocklength n")
    plt.ylabel("Overall error (surrogate)")
    plt.title("One-shot Strong Converse: Error explodes when exceeding Loop-DPI")
    plt.savefig("../tex/figures/one_shot_converse.pdf", bbox_inches="tight")

if __name__ == "__main__":
    run()
