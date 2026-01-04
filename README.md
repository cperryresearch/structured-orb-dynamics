## 📍 Geometry-First Motion Analysis

Looking for the geometry-first framework? Start with the methodology overview here:  
https://github.com/cperryresearch/structured-orb-dynamics/tree/main/methodology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18148257.svg)](https://doi.org/10.5281/zenodo.18148257)

# Structured Orb Dynamics  
Unified Manuscript and Data Repository

This repository is intended for researchers interested in geometry-based motion characterization under uncertainty.

This repository contains the materials supporting the study *Structured Orb Dynamics*.  
All components — manuscript, data, and analysis code — are maintained together to support transparency and reproducibility.

The project analyzes image-plane motion using a minimal set of geometric tools.  
Curvature, basic derivative estimates, and a simple state model are used to summarize apparent motion in stabilized infrared recordings (PR-018).  
No physical assumptions are imposed; all results derive strictly from quantities observable in the image plane.

A standard scientific Python stack is sufficient (NumPy, SciPy, Matplotlib).

---

## Licensing

- **Code**: MIT License (see `LICENSE`)
- **Manuscript, figures, and documentation**: Creative Commons Attribution 4.0 International (CC BY 4.0)  
  (see `LICENSE-DOCS.md`)

---

## Citation and Archival Record

The Structured Orb Dynamics project is archived on Zenodo.

- **Latest version (v1.5.0 — Validation Release):**  
  https://doi.org/10.5281/zenodo.18148257

- **Concept DOI (resolves to all versions):**  
  https://doi.org/10.5281/zenodo.17846786
  
---

## Latest Update (v1.5.0)

**Validation-focused release confirming SOD restraint.**

This release extends Part VI with two rigorously bounded validation studies designed
to test failure modes of the Structured Orb Dynamics (SOD) state framework under
realistic biological motion conditions.

### Added in v1.5.0

**Part VI-B — Formal Negative Control**
- Barn Swallow (Hirundidae) GPS data at coarse cadence (600 s)
- Empirically derived hover threshold (P10 speed)
- Persistence gating enforced
- Result: **0% Hover occupancy**, as expected

**Part VI-C — High-Cadence Boundary Test**
- High-frequency (300 Hz) hummingbird flight trials
- Same hover rule and persistence requirements applied unchanged
- Result: **No persistent Hover state identified**

### Interpretation

These results demonstrate that:
- Increased sampling cadence alone is insufficient to produce Hover classification
- Persistence gating prevents spurious state detection
- The SOD framework remains conservative under both coarse and fine sampling

No new empirical claims are introduced.
Core SOD definitions, thresholds, and state rules remain unchanged.

---

## Author

**Cassandra Perry**  
Independent Researcher  
ORCID: https://orcid.org/0009-0001-1998-1481

---

## Downloads

The unified manuscript and full repository snapshot are archived on Zenodo:

- **Latest version (v1.5.0):**  
  https://doi.org/10.5281/zenodo.18148257

- **Concept DOI (always resolves to the latest version):**  
  https://doi.org/10.5281/zenodo.17846786
  
Each record includes:
- Unified manuscript (PDF)
- Full repository snapshot (ZIP)
- Versioned archival metadata for citation and reproducibility

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

The current release corresponds to the unified foundation (Parts I–V) with
validation extensions in Part VI.

Planned future work includes:
- Extended comparative datasets (Part VI continuation)
- Part VII: Orb Motion Classifier (machine learning)
- Part VIII: Physics-informed kinematic envelope analysis

All future extensions will retain geometry-first constraints and explicit
negative controls.

---

## Citation

Use the Zenodo concept DOI above to cite the latest version of this repository.
https://doi.org/10.5281/zenodo.17846786

For version-specific citation (v1.5.0):

Perry, C. (2026). Structured Orb Dynamics: Unified Manuscript and Data Repository
(v1.5.0 — Validation Release). Zenodo.
https://doi.org/10.5281/zenodo.18148257

### BibTeX
@misc{perry2026_structured_orb_dynamics_v150,
  author    = {Perry, Cassandra},
  title     = {Structured Orb Dynamics: Unified Manuscript and Data Repository (v1.5.0 — Validation Release)},
  year      = {2026},
  doi       = {10.5281/zenodo.18148257},
  url       = {https://doi.org/10.5281/zenodo.18148257},
  publisher = {Zenodo}

