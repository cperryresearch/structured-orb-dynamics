[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17856369.svg)](https://doi.org/10.5281/zenodo.17856369)
[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.178467867.svg)](https://doi.org/10.5281/zenodo.178467867)

# Structured Orb Dynamics  
Unified Manuscript and Data Repository (v1.2.0)

This repository contains the materials supporting the study *Structured Orb Dynamics*.  
All components—manuscript, data, and analysis code—are kept together for transparency and reproducibility.

The project analyzes image-plane motion using a minimal set of geometric tools.  
Curvature, basic derivative estimates, and a simple state model are used to summarize the apparent motion in a stabilized infrared recording (PR-018).  
No physical assumptions are imposed; all results derive strictly from what can be measured directly in the video frames.

A standard scientific Python stack is sufficient (numpy, scipy, matplotlib).

---

## Downloads (v1.2.0)

Unified Manuscript (PDF):  
https://zenodo.org/records/17856369/files/Structured_Orb_Dynamics___Unified_Manuscript___Data_Repository.pdf

Full Repository Snapshot (ZIP):  
https://zenodo.org/records/17856369/files/Structured_Orb_Dynamics___Unified_Manuscript___Data_Repository.zip

---

## Repository Layout

`manuscript/` – PDF and LaTeX source files for the full write-up (Parts I–IV).  
`code/` – Scripts for tracking, smoothing, curvature estimation, and feature extraction.  
`data/` – Processed PR-018 trajectory and feature series used in the figures.  
`results/` – Plots, traces, and reconstructed motion visualizations.  
`supplement/` – Short notes on the GIMBAL dataset (qualitative only).

Running the scripts will regenerate the feature series and the plots.  
Paths may need adjustment depending on the environment.

Example:
python tracking/run_tracking.py  
python features/compute_features.py  
python model/run_state_model.py

---

## PR-018 Summary

PR-018 is the only dataset where a stable trajectory could be reconstructed.  
The workflow consists of:

1. Frame stabilization around the target  
2. Centroid extraction  
3. Track smoothing  
4. Computation of velocity, acceleration, curvature, and curvature rate  
5. Running the simple state model and saving the resulting probabilities  

The results reproduced here match those described in the manuscript.

---

## GIMBAL Note

A brief qualitative write-up is included.  
No trajectory could be extracted, and therefore no curvature or state estimates are available.

---

## Research Roadmap

The current release corresponds to the unified foundation (Parts I–IV).  
Planned future work includes:

- Part IV: Instrumentation and reconstruction accuracy  
- Part V: Comparative multi-dataset analysis  
- Part VI: Orb Motion Classifier (machine learning)  
- Part VII: Physics-informed kinematic envelope analysis  

These components will be added in future versioned releases.

---

## Citation

If this work is used, please cite:

Perry, C. (2025). *Structured Orb Dynamics: Unified Manuscript and Data Repository (v1.2.0).* Zenodo.  
https://doi.org/10.5281/zenodo.17856369

For references to the evolving project and its complete version history, use the concept DOI:  
https://doi.org/10.5281/zenodo.178467867

### BibTeX
@misc{perry2025_structured_orb_dynamics_v120,  
  author       = {Perry, Cassandra},  
  title        = {Structured Orb Dynamics: Unified Manuscript and Data Repository (v1.2.0)},  
  year         = {2025},  
  doi          = {10.5281/zenodo.17856369},  
  publisher    = {Zenodo},  
  url          = {https://doi.org/10.5281/zenodo.17856369}  
}

## Community & Contributions

Structured Orb Dynamics welcomes clear, reproducible, and geometry-focused contributions.  
If you would like to participate, please read the project’s contribution guidelines:

➡️ **See: [CONTRIBUTING.md](CONTRIBUTING.md)**

### What kinds of contributions are encouraged?

- Reproducibility checks for figures or classifier outputs  
- Improvements in clarity of definitions, notation, or documentation  
- Small refinements that enhance determinism or transparency  
- Well-reasoned, scope-aligned discussions about geometric inference  

### What is outside the scope?

- Physical speculation (range, speed, size, intent, etc.)  
- Platform or sensor calibration  
- Claims about object identity or nature  
- Non-deterministic code changes  

Pinned Issue #1 gives a concise overview of project scope and engagement expectations.

We appreciate contributions that uphold clarity, reproducibility, and rigor.
