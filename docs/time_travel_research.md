# Time Travel Research Catalog

This document catalogs relevant time travel research from GitHub, academic sources, and the broader scientific community that relates to the Entropy Ledger framework.

## Overview

Our research on consistent time travel via the Entropy Ledger framework intersects with several active areas of research in quantum information theory, general relativity, and computational physics. This catalog identifies key repositories, implementations, and theoretical frameworks that complement our work.

## GitHub Repositories & Code Implementations

### Active Research Projects

#### 1. **qhronology** (lgbishop/qhronology)
- **Description**: A Python package for studying quantum models of closed timelike curves and simulating general quantum information processing & computation
- **Language**: Python
- **Stars**: 2
- **Last Updated**: February 2026
- **Repository**: [github.com/lgbishop/qhronology](https://github.com/lgbishop/qhronology)
- **Relevant Files**: 
  - `src/qhronology/quantum/prescriptions.py` - CTC prescription implementations
- **Relevance**: Implements multiple CTC prescriptions (Deutsch, P-CTC) that could validate our theoretical framework

#### 2. **toroidal-ctc-sim** (FreeDeathTV/toroidal-ctc-sim)
- **Description**: Desktop analogue for closed timelike curves using spin-biased FDTD waves
- **Language**: Python
- **Last Updated**: November 2025
- **Repository**: [github.com/FreeDeathTV/toroidal-ctc-sim](https://github.com/FreeDeathTV/toroidal-ctc-sim)
- **Relevance**: Provides FDTD-based simulation approach that could complement our QuTiP simulations

#### 3. **Quantum-time-travel** (MiChaelinzo/Quantum-time-travel)
- **Description**: Quantum time loop implementations
- **Language**: Python
- **Repository**: [github.com/MiChaelinzo/Quantum-time-travel](https://github.com/MiChaelinzo/Quantum-time-travel)
- **Relevant Files**:
  - `quantum_time_loop.py` - Core time loop implementation
- **Relevance**: Practical implementation of quantum time loops using closed timelike curves

#### 4. **TimeTravelMetric** (OfficialAdamRivers/TimeTravelMetric)
- **Description**: A mathematically validated spacetime metric solution exhibiting closed timelike curves for theoretical time travel
- **Last Updated**: September 2025
- **Repository**: [github.com/OfficialAdamRivers/TimeTravelMetric](https://github.com/OfficialAdamRivers/TimeTravelMetric)
- **Relevance**: Provides GR-based metric solutions that could inform the relativistic interpretation of our model

#### 5. **time-loop-utility** (Wong-Innovations/time-loop-utility)
- **Description**: A mod that adds closed timelike curves to Minecraft
- **Language**: Java
- **Repository**: [github.com/Wong-Innovations/time-loop-utility](https://github.com/Wong-Innovations/time-loop-utility)
- **Relevance**: Educational visualization tool for CTC concepts

### Related Code Implementations

The following code files were identified through GitHub code search and may contain useful algorithms:

- **quantum_time_loop.py** - Quantum time loop implementations with CTC models
- **temporal_quantum_processing.py** - Temporal aspects of quantum processing
- **temporal_causality_engine.py** - Causality enforcement in temporal systems
- **spacetime_metric_modulation_algorithms.py** - Algorithms for spacetime metric manipulation
- **time_advanced_analysis.py** - Advanced analysis of time-related phenomena

## Theoretical Frameworks

### CTC Prescriptions

1. **Deutsch-CTC Model**
   - Fixed-point formulation for quantum systems with CTCs
   - Maximum entropy principle for consistency resolution
   - Relevant to our monotone analysis

2. **Postselected CTC (P-CTC) Model**
   - Uses postselection to simulate CTCs
   - Directly relates to our heralded postselection approach
   - Success probability bounds connect to our `-log2(p_succ)` information gain

3. **Lloyd's CTC Model**
   - Quantum teleportation-based approach
   - Connects to our `qutip_postselected_teleportation.py` implementation

### Information-Theoretic Constraints

Our research identifies several information-theoretic bounds on time travel:

1. **Entropy Ledger**: `kT * KL` cost for Novikov consistency (this work)
2. **Information Gain Bound**: `-log2(p_succ)` bits per successful attempt
3. **Temporal Advantage vs. Entropy Debt**: Pareto-optimal tradeoff frontier
4. **Loop-DPI Inequality**: Data processing inequality for closed causal loops

## Key Research Areas

### 1. Closed Timelike Curves (CTCs)
- Mathematical frameworks for time-loop consistency
- Quantum vs. classical CTCs
- Spacetime geometry considerations

### 2. Quantum Retrocausality
- Postselection and weak measurements
- Delayed-choice quantum eraser
- Quantum steering and entanglement

### 3. Heralded Quantum Teleportation
- Success probability and information gain
- Entanglement-assisted feedback
- Resource costs and thermodynamic bounds

### 4. Temporal Quantum Processing
- Quantum circuits with temporal feedback
- Causality preservation in quantum networks
- Time-ordered quantum operations

### 5. Spacetime Metric Engineering
- Alcubierre-type metrics
- Traversable wormholes (Morris-Thorne)
- Energy conditions and exotic matter

## Academic Literature References

### Foundational Papers

1. **Deutsch, D. (1991)** - "Quantum mechanics near closed timelike lines"
   - Physical Review D, 44(10), 3197
   - Seminal work on quantum CTCs

2. **Lloyd, S., et al. (2011)** - "Quantum mechanics of time travel through post-selected teleportation"
   - Physical Review D, 84(2), 025007
   - P-CTC model and quantum information approach

3. **Allen, J.M.A., et al. (2017)** - "Quantum Common Causes and Quantum Causal Models"
   - Physical Review X, 7(3), 031021
   - Causal structure in quantum theory

4. **Chiribella, G., et al. (2013)** - "Quantum computations without definite causal structure"
   - Physical Review A, 88(2), 022318
   - Indefinite causal order

### Thermodynamic and Information Theory

1. **Sagawa, T., & Ueda, M. (2012)** - "Nonequilibrium thermodynamics of feedback control"
   - Physical Review E, 85(2), 021104
   - Relevant to our entropy costs

2. **Landauer, R. (1961)** - "Irreversibility and heat generation in the computing process"
   - IBM Journal of Research and Development, 5(3), 183-191
   - Fundamental bounds on information erasure

3. **Bennett, C.H. (1973)** - "Logical reversibility of computation"
   - IBM Journal of Research and Development, 17(6), 525-532
   - Reversible computation and time-symmetry

## Connection to Our Framework

### How External Research Validates Our Approach

1. **CTC Prescriptions**: The qhronology package implements both Deutsch and P-CTC models, allowing us to validate our Loop-DPI bounds against established frameworks

2. **Postselection Costs**: Lloyd's teleportation-based approach confirms our `-log2(p_succ)` information gain bound

3. **Entropy Requirements**: Literature on Maxwell's demon and feedback control supports our `kT * KL` Novikov consistency cost

4. **Simulation Methods**: FDTD and QuTiP approaches in external repositories provide complementary numerical techniques

### Integration Opportunities

1. **Benchmarking**: Compare our `sim_loop_dpi.py` against qhronology implementations
2. **Extended Simulations**: Incorporate FDTD methods from toroidal-ctc-sim
3. **Metric Solutions**: Use TimeTravelMetric for GR-consistent interpretations
4. **Educational Tools**: Reference time-loop-utility for pedagogical explanations

## Future Research Directions

Based on the surveyed research, we identify the following promising directions:

1. **Hybrid CTC Models**: Combine Deutsch and P-CTC prescriptions with Entropy Ledger constraints
2. **Experimental Proposals**: Design ion-trap or photonic implementations of Loop-DPI
3. **Computational Complexity**: Explore time-travel-assisted algorithms (CTC-computing)
4. **Relativistic Extensions**: Incorporate full GR metrics beyond operational quantum models
5. **Multi-party Scenarios**: Extend to multiple agents sharing retro-resources

## Tools and Software Ecosystem

### Python Packages
- **QuTiP**: Quantum toolbox in Python (used in our simulations)
- **qhronology**: CTC-specific quantum package
- **NumPy/SciPy**: Numerical foundations
- **Matplotlib**: Visualization (our figures)

### Simulation Frameworks
- **FDTD**: Finite-difference time-domain (electromagnetics)
- **Quantum circuits**: Qiskit, Cirq potential integrations
- **LaTeX**: Documentation and paper writing (our tex/ directory)

### Development Tools
- **Git/GitHub**: Version control and collaboration
- **MkDocs**: Documentation site generation (our setup)
- **Docker**: Containerized reproducibility (our Dockerfile)
- **CI/CD**: Automated testing and builds (our workflows)

## Contributing to the Ecosystem

Researchers interested in consistent time travel via the Entropy Ledger framework can:

1. Compare implementations against existing CTC simulators
2. Submit PRs to integrate our Loop-DPI code into broader packages
3. Cross-reference papers citing both our work and the research cataloged here
4. Collaborate on experimental realizations of our theoretical predictions

## Staying Current

This research catalog should be updated periodically to track:
- New repository releases and stars
- arXiv preprints on quantum CTCs and retrocausality
- Experimental demonstrations of postselected teleportation
- Advances in quantum computing hardware enabling CTC emulation

**Last Updated**: February 2026

---

*For citations of this catalog and the Entropy Ledger framework, see [`CITATION.cff`](../CITATION.cff)*
