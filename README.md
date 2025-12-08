[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17852764.svg)](https://doi.org/10.5281/zenodo.17852764)
[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.178467867.svg)](https://doi.org/10.5281/zenodo.178467867)

### Structured Orb Dynamics  
Unified Manuscript and Data Repository

This repo collects the materials used in the study.  
The manuscript, code, and the PR018 analysis are kept together so the workflow is easy to follow.

The project looks at image-plane motion using a set of simple geometric tools.  
Curvature, basic derivative estimates, and a small state model were used to summarize the motion seen in a stabilized infrared recording (PR018).  
No physical model is assumed; everything is based on what can be measured directly in the frames.

Install the usual Python packages (numpy, scipy, matplotlib). Nothing special is required.

### Repository Layout

manuscript/  PDF and source files. Full write-up (Parts I–IV).

code/   Small set of scripts for tracking, smoothing, and feature extraction.

data/  Processed track for PR018 (not the raw video). Feature series used in the plots.

results/  Figures and probability traces.

supplement/  Notes on the GIMBAL dataset (only qualitative observations possible).

Running the scripts will recreate the feature series and the plots.  
Paths may need to be changed depending on your setup.

python tracking/run_tracking.py  
python features/compute_features.py  
python model/run_state_model.py

### PR-018 Summary

PR-018 is the only dataset where a usable trajectory could be reconstructed.  
Basic steps:

– stabilize the frames around the target  
– extract a centroid track  
– smooth the track  
– compute velocity, acceleration, curvature, and curvature rate  
– run the simple state model and save the probabilities

### The results here match those described in the manuscript.

### GIMBAL Note

A short write-up is included.  
Only qualitative observations were possible.  
No trajectory, no curvature estimates, no state sequence.

### Citation

If this work is used, please cite:

Perry, C. (2025).  Structured Orb Dynamics: Unified Manuscript and Data Repository (v1.1.0).  
Zenodo. https://doi.org/10.5281/zenodo.17852764


You may also cite the concept DOI if referring to the full version history:
Concept DOI: https://doi.org/10.5281/zenodo.178467867

