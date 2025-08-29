# Quick Start

## Local build
```bash
pip install -r requirements.txt
cd tex && latexmk -pdf main.tex
```

## Simulations
```bash
cd code
python loop_dpi_sweep.py
python multiloop_sim.py
python pareto_tradeoff.py
python one_shot_converse.py
python single_shot_smoothed_bounds.py
python qutip_heatmap.py
```

## MkDocs site
```bash
pip install mkdocs mkdocs-material
mkdocs serve
# open http://127.0.0.1:8000
```
