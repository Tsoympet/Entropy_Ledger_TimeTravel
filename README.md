
# The Entropy Ledger: Resource Theory and Information Inequalities for Consistent Time Travel

This bundle contains:
- `tex/` a complete LaTeX scaffold with theorem statements, sections, and a figure
- `code/sim_loop_dpi.py` a toy simulation for Loop-DPI and Entropy Ledger trade-offs
- `tex/figures/loop_dpi_bound.pdf` a ready-made plot used by the paper

## Compile
Use any standard LaTeX (no biblatex required):
```
cd tex
pdflatex main.tex
pdflatex main.tex
```
(Compile twice for references.)

## Run the simulation
```
cd code
python sim_loop_dpi.py
```

## Notes on "real" time travel
- \*\*Forward\*\*: Realized via relativistic time dilation (fast/strong-gravity trajectories).
- \*\*Backward (operational)\*\*: Emulated using heralded postselection and entanglement-assisted feedback. The net information gain per attempt is bounded by `-log2(p_succ)` bits, and enforcing Novikov consistency costs at least `kT * KL` (Entropy Ledger).


## Heavier simulations
- `code/loop_dpi_sweep.py`: sweeps p_succ and compares empirical gain vs bound; writes PDF figure.
- `code/multiloop_sim.py`: simulates multiple retro-loops and compares to a cut-set style bound.
- `code/pareto_tradeoff.py`: generates a Pareto-like frontier between Temporal Advantage and Entropy Debt.
- `code/one_shot_converse.py`: surrogate demonstration of the strong converse.


## Journal-style templates
- **APS/PRL**: `tex_aps/main.tex` (revtex4-2). Compile with `pdflatex main.tex` inside `tex_aps/`.
- **Nature-style**: `tex_nature/main.tex` (article mimic). Compile with `pdflatex main.tex` inside `tex_nature/`.

## QuTiP and ion-trap sims
- `code/qutip_postselected_teleportation.py` (requires `pip install qutip`).
- `code/iontrap_heralding_sim.py` (pure NumPy surrogate).
- `code/single_shot_smoothed_bounds.py` generates `one_shot_smoothed.pdf`.


## Nature-portfolio class
- `tex_nature_portfolio/main.tex` uses the `nature` class if available (fallback: use `tex_nature/main.tex`).

## PRL and Nature cuts
- PRL-length cut: `tex_aps/prl_cut.tex`
- Nature-length cut: `tex_nature/nature_cut.tex`

## QuTiP heatmap
- `code/qutip_heatmap.py` generates `tex/figures/qutip_heatmap.pdf` (already generated here).


## CI Status
![Build PDFs](https://github.com/USER/REPO/actions/workflows/latex.yml/badge.svg) ![Run Simulations](https://github.com/USER/REPO/actions/workflows/simulations.yml/badge.svg)

Replace `USER/REPO` with your GitHub handle and repository name to activate badges.


## Makefile
- `make` or `make all`: run simulations and build Base/APS/PRL/Nature PDFs
- `make sims` generates/refreshes all figures under `tex/figures`
- `make base|aps|prl|nature|nature_portfolio` to build specific targets
- `make clean` and `make distclean` for cleanup

## Releases on tags
- Pushing a tag like `v1.0.0` triggers `.github/workflows/release.yml`, which rebuilds figures and PDFs and **attaches** them to the GitHub Release.


## Docs (MkDocs)
- Edit markdown in `docs/`, build locally with `mkdocs serve`, and the CI in `.github/workflows/gh-pages.yml` deploys to GitHub Pages on push to `main`.
- Set `site_url` and `repo_url` in `mkdocs.yml` (replace `YOUR_USER/YOUR_REPO`). Enable Pages in repo settings.

## Docker
- Build: `make docker-build`
- Run: `make docker-run`


## Citation
- Cite the software/paper via **`CITATION.cff`** (GitHub renders this automatically).
- Once Zenodo is enabled and a release is tagged, replace `10.5281/zenodo.TBD` with your **concept DOI** and add the versioned DOI for each new release.

### Example BibTeX
```bibtex
@software{entropy_ledger_2025,
  title={The Entropy Ledger: Consistent Time Travel},
  author={Ts., Spiros and Collaborators},
  year={2025},
  doi={10.5281/zenodo.TBD},
  url={https://github.com/YOUR_USER/YOUR_REPO}
}
```
