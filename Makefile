# Root Makefile for building PDFs and running simulations
.PHONY: all base aps prl nature nature_portfolio sims figures clean distclean

all: sims figures base aps prl nature

base:
	@echo "Building base article (tex/main.tex)"
	cd tex && latexmk -pdf -interaction=nonstopmode main.tex

aps:
	@echo "Building APS/PRL (tex_aps/main.tex)"
	cd tex_aps && latexmk -pdf -interaction=nonstopmode main.tex

prl:
	@echo "Building PRL-length cut (tex_aps/prl_cut.tex)"
	cd tex_aps && latexmk -pdf -interaction=nonstopmode prl_cut.tex

nature:
	@echo "Building Nature-style mimic (tex_nature/main.tex)"
	cd tex_nature && latexmk -pdf -interaction=nonstopmode main.tex

nature_portfolio:
	@echo "Building Nature Portfolio class (if installed)"
	cd tex_nature_portfolio && latexmk -pdf -interaction=nonstopmode main.tex || true

sims:
	@echo "Running simulations"
	cd code && python loop_dpi_sweep.py
	cd code && python multiloop_sim.py
	cd code && python pareto_tradeoff.py
	cd code && python one_shot_converse.py
	cd code && python single_shot_smoothed_bounds.py
	cd code && python qutip_heatmap.py
	cd code && python qutip_postselected_teleportation.py || true
	cd code && python iontrap_heralding_sim.py

figures: sims
	@echo "Figures generated under tex/figures"

clean:
	latexmk -C tex/main.tex || true
	latexmk -C tex_aps/main.tex || true
	latexmk -C tex_aps/prl_cut.tex || true
	latexmk -C tex_nature/main.tex || true
	latexmk -C tex_nature/nature_cut.tex || true
	latexmk -C tex_nature_portfolio/main.tex || true

distclean: clean
	find . -type f -name "*.pdf" -not -path "./tex/figures/*" -delete || true


docker-build:
	docker build -t entropy-ledger:latest .
docker-run:
	docker run --rm -v $(PWD):/workspace entropy-ledger:latest
