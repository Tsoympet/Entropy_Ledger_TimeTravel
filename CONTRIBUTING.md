# Contributing

Thanks for your interest!

## Dev setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running simulations
```bash
cd code
python loop_dpi_sweep.py
python multiloop_sim.py
python pareto_tradeoff.py
python one_shot_converse.py
python single_shot_smoothed_bounds.py
# optional (falls back to surrogate if QuTiP not installed)
python qutip_heatmap.py
python qutip_postselected_teleportation.py
python iontrap_heralding_sim.py
```

## Building PDFs
```bash
cd tex && latexmk -pdf main.tex
cd ../tex_aps && latexmk -pdf main.tex
cd ../tex_nature && latexmk -pdf main.tex
```

## Pull requests
- Keep PRs focused.
- Include figures generated in `tex/figures/` (these are artifacts; CI also rebuilds them).
- Add/update references in `tex/refs.bib`.
