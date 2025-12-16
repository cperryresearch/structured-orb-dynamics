## 📍 Geometry-First Motion Analysis

Looking for the Geometry-First framework? Start with the [methodology folder here](https://github.com/cperryresearch/structured-orb-dynamics/tree/main/methodology).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17846786.svg)](https://doi.org/10.5281/zenodo.17846786)

# Structured Orb Dynamics  
Unified Manuscript and Data Repository 

This repository contains the materials supporting the study *Structured Orb Dynamics*.  
All components—manuscript, data, and analysis code—are kept together for transparency and reproducibility.

The project analyzes image-plane motion using a minimal set of geometric tools.  
Curvature, basic derivative estimates, and a simple state model are used to summarize the apparent motion in a stabilized infrared recording (PR-018).  
No physical assumptions are imposed; all results derive strictly from what can be measured directly in the video frames.

A standard scientific Python stack is sufficient (numpy, scipy, matplotlib).

---

## Latest Update (v1.3.0)

**Methodological robustness update.**

This release adds **Appendix A: Observable Robustness and Non-Causal Validation**, defining a protocol-ready set of non-causal checks for curvature-based motion-state transitions, including:

- Track continuity verification
- Estimator robustness under smoothing and subsampling
- Algorithmic change-point detection
- Baseline uncertainty and confidence distinction

No results, datasets, figures, or conclusions were changed.

**Note on versioning:** Zenodo assigns internal archival version numbers to each record update. The manuscript’s semantic version (v1.3.0) is authoritative and is reflected in the title, changelog, and release notes.

## Author

**Cassandra Perry**  
Independent Researcher  
ORCID: https://orcid.org/0009-0001-1998-1481

## Downloads

The latest version of the unified manuscript and full repository snapshot is archived on Zenodo:

- **Concept DOI (always resolves to the latest version):**  
  https://doi.org/10.5281/zenodo.17945669

This DOI provides access to:
- The unified manuscript (PDF)
- A full repository snapshot (ZIP)
- Versioned archival records for citation and reproducibility

For citation, use the concept DOI (it always resolves to the latest archived version).

---

## Repository Layout

`manuscript/` – PDF and LaTeX source files for the full write-up (Parts I–V).  
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

PR-018 is the only dataset in this release where a stable trajectory could be reconstructed.  
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
No trajectory could be extracted, and therefore no curvature or state estimates are available within the current framework.

---

## Research Roadmap

The current release corresponds to the unified foundation (Parts I–V).

Planned future work includes:
- Part VI: Comparative multi-dataset analysis
- Part VII: Orb Motion Classifier (machine learning)
- Part VIII: Physics-informed kinematic envelope analysis

These components will be added in future versioned releases.

---

## Citation

Use the Zenodo concept DOI above to cite the latest version of this repository.

If this repository or its methods are used, please cite:

Perry, C. (2025). *Structured Orb Dynamics: Unified Manuscript and Data Repository (v1.2.0).* Zenodo.  
https://doi.org/10.5281/zenodo.17904630

For references to the evolving project and its complete version history, use the concept DOI:  
https://doi.org/10.5281/zenodo.17846786

### BibTeX
@misc{perry2025_structured_orb_dynamics_v120,
  author    = {Perry, Cassandra},
  title     = {Structured Orb Dynamics: Unified Manuscript and Data Repository (v1.2.0)},
  year      = {2025},
  doi       = {10.5281/zenodo.17904630},
  url       = {https://doi.org/10.5281/zenodo.17904630},
  publisher = {Zenodo}
}

