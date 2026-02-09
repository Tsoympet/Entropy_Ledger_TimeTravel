# Using Time Travel Research in Our Framework

This guide explains how to integrate findings from the Time Travel Research Catalog into your work with the Entropy Ledger framework.

## Quick Integration Guide

### 1. Comparing CTC Models

Our framework uses postselected teleportation (similar to Lloyd's P-CTC model). To compare with other models:

```python
# Our approach (see code/qutip_postselected_teleportation.py)
import qutip as qt

# Compare with Deutsch-CTC from external packages
# pip install qhronology (if available)
# from qhronology.quantum.prescriptions import deutsch_ctc, p_ctc
```

### 2. Validating Loop-DPI Bounds

To validate our Loop-DPI inequality against literature:

1. **Review**: `docs/time_travel_research.md` for information-theoretic bounds
2. **Compare**: Our `-log2(p_succ)` bound with Lloyd et al. (2011)
3. **Benchmark**: Run `code/loop_dpi_sweep.py` and cross-check results

### 3. Entropy Ledger Verification

Our `kT * KL` cost relates to:
- Landauer's principle (1961) - information erasure cost
- Sagawa & Ueda (2012) - feedback control thermodynamics
- Bennett (1973) - reversible computation

```python
# See code/sim_loop_dpi.py for implementation
# Entropy cost calculation:
entropy_debt = k_B * T * kl_divergence(rho_before, rho_after)
```

### 4. Extending Simulations

#### Using QuTiP (our current approach)
```bash
cd code
python qutip_postselected_teleportation.py
python qutip_heatmap.py
```

#### Comparing with FDTD methods (from toroidal-ctc-sim)
- FDTD provides electromagnetic wave analogue of CTCs
- Could complement our quantum circuit approach
- See: `docs/time_travel_research.md` § "toroidal-ctc-sim"

### 5. Accessing Academic References

All references are in BibTeX format:

```bash
# View bibliography
cat docs/time_travel_references.bib

# Use in LaTeX papers
# Add to tex/main.tex or tex_aps/main.tex:
# \bibliography{../docs/time_travel_references}
```

Key papers to cite alongside our work:
- **Deutsch (1991)**: Original CTC formulation
- **Lloyd et al. (2011)**: P-CTC via postselection
- **Landauer (1961)**: Thermodynamic bounds
- **Chiribella et al. (2013)**: Indefinite causal order

### 6. Exploring External Repositories

#### qhronology (Python package)
```bash
# To install and test (if publicly available)
pip install qhronology

# Compare prescriptions
python -c "from qhronology.quantum import prescriptions; help(prescriptions)"
```

#### toroidal-ctc-sim (FDTD approach)
```bash
# Clone and run (example)
git clone https://github.com/FreeDeathTV/toroidal-ctc-sim
cd toroidal-ctc-sim
# Follow their README for setup
```

### 7. Research Workflow

When incorporating external research:

1. **Literature Review**: Start with `docs/time_travel_research.md`
2. **Identify Relevant Work**: Match research areas to your needs
3. **Access Code**: Clone repositories or review code snippets
4. **Benchmark**: Compare implementations against our `code/` directory
5. **Cite**: Add references from `docs/time_travel_references.bib`
6. **Document**: Update research catalog if you find new work

### 8. Connecting Theory to Code

| Theoretical Concept | Our Implementation | External Reference |
|---------------------|--------------------|--------------------|
| P-CTC postselection | `qutip_postselected_teleportation.py` | Lloyd et al. (2011) |
| Loop-DPI inequality | `sim_loop_dpi.py` | Data processing inequality (Lieb & Ruskai) |
| Entropy Ledger | `sim_loop_dpi.py` (KL cost) | Sagawa & Ueda (2012) |
| Ion trap simulation | `iontrap_heralding_sim.py` | Experimental proposals |
| Pareto frontier | `pareto_tradeoff.py` | Resource theory framework |

### 9. Experimental Proposals

Based on surveyed research:

1. **Photonic Implementation**
   - Use heralded single photon sources
   - Postselection via photodetectors
   - See: Ringbauer et al. (2014)

2. **Ion Trap Approach**
   - Our simulation: `code/iontrap_heralding_sim.py`
   - Heralded operations with trapped ions
   - Verify Loop-DPI bounds experimentally

3. **Superconducting Qubits**
   - Adapt our QuTiP simulations
   - Target IBM Q or Google Sycamore
   - Measure entropy costs directly

### 10. Contributing Back

If you use external research in your Entropy Ledger work:

1. **Update the Catalog**: Add new repositories to `docs/time_travel_research.md`
2. **Add References**: Include BibTeX entries in `docs/time_travel_references.bib`
3. **Document Integration**: Note how external work validates/extends our framework
4. **Share Results**: Open PRs or issues in relevant repositories
5. **Cross-cite**: Help build the time travel research ecosystem

## Common Research Questions

### Q: Which CTC prescription should I use?

**A**: For consistency with our framework:
- **P-CTC (Lloyd model)**: Best match for postselected teleportation
- **Deutsch-CTC**: Alternative for maximum entropy approach
- Compare both using qhronology package

### Q: How do I validate the Entropy Ledger cost?

**A**: 
1. Run `code/sim_loop_dpi.py`
2. Measure `kT * KL(ρ_initial || ρ_final)`
3. Compare with feedback control literature (Sagawa & Ueda)
4. Check Landauer bound: `kT ln(2)` per bit erased

### Q: Where can I find experimental data?

**A**:
- Ringbauer et al. (2014): Photonic CTC simulation
- Bouwmeester et al. (1997): Quantum teleportation
- Our proposals: `docs/experiments.md`

### Q: How does this relate to relativistic time travel?

**A**:
- **Forward**: Actual time dilation (Twin Paradox)
- **Backward (operational)**: Postselection mimics CTCs
- **Full GR**: See Morris-Thorne wormholes, Alcubierre drive
- **Our focus**: Information-theoretic operational framework

## Further Reading

- **Main catalog**: `docs/time_travel_research.md`
- **Bibliography**: `docs/time_travel_references.bib`
- **Theory**: `docs/theory.md`
- **FAQ**: `docs/faq.md`

## Staying Updated

Track new research:
- GitHub: Watch qhronology and related repositories
- arXiv: Set alerts for "closed timelike curves", "quantum retrocausality"
- Journals: Physical Review D, Nature Physics, Quantum
- Conferences: QIP, QCMC, GR conferences

---

*Last updated: February 2026*
