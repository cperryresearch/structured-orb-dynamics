## How to Use This Page

This page provides a structured orientation to the Structured Orb Dynamics (SOD) project.
It is intended as a reference for readers who want to understand the scope, posture,
artifacts, and limits of the framework before engaging with the manuscript or code.

This page does not introduce new results or claims.

---

## Geometry-First Posture

Looking for the geometry-first framework? Start with the methodology overview here:  

https://github.com/cperryresearch/structured-orb-dynamics/tree/main/methodology

---

## Structured Orb Dynamics  

Unified Manuscript, Code, and Data Repository

This repository is intended for researchers interested in geometry-based motion characterization under uncertainty.

This repository contains the materials supporting the study *Structured Orb Dynamics*.  
All components — manuscript, data, and analysis code — are maintained together to support transparency and reproducibility.

The project analyzes image-plane motion using a minimal set of geometric tools.  
Curvature, basic derivative estimates, and a simple state model are used to summarize apparent motion in stabilized infrared recordings (PR-018).  

No physical assumptions are imposed; all results derive strictly from quantities observable in the image plane.

A standard scientific Python stack is sufficient (NumPy, SciPy, Matplotlib).

---

## What Structured Orb Dynamics Is Not

Structured Orb Dynamics is not a predictive model, an intent classifier,
or an operational system.

It does not infer physical mechanisms, forces, or agency.

All outputs are geometric summaries of observed motion under uncertainty.

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

Example (command sequence only):

```bash
python tracking/run_tracking.py
python features/compute_features.py
python model/run_state_model.py
```
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

---

## Interpretation (Scope-Limited)

These results demonstrate that:
- Increased sampling cadence alone is insufficient to produce Hover classification
- Persistence gating prevents spurious state detection
- The SOD framework remains conservative under both coarse and fine sampling

No new empirical claims are introduced.

Core SOD definitions, thresholds, and state rules remain unchanged.

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

All future extensions will retain geometry-first constraints and explicit negative controls.

---

## How to Engage

Questions, clarifications, and technical discussion are welcome via GitHub Discussions. This project favors careful, scope-aware discussion over speculative interpretation.
