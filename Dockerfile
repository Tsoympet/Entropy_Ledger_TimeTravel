# Reproducible environment for PDFs and simulations
FROM ubuntu:22.04

# Avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv git make \
    latexmk texlive-base texlive-latex-recommended texlive-latex-extra \
    texlive-fonts-recommended texlive-bibtex-extra texlive-science \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt /workspace/requirements.txt
RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

# Optional: MkDocs for docs site
RUN pip install mkdocs mkdocs-material

# Copy project
COPY . /workspace

# Default: build base PDF and run core sims
CMD bash -lc "cd tex && latexmk -pdf main.tex && cd ../code && python loop_dpi_sweep.py && python multiloop_sim.py && python pareto_tradeoff.py && python one_shot_converse.py && python single_shot_smoothed_bounds.py"
