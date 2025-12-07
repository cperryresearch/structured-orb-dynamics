[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17839162.svg)](https://doi.org/10.5281/zenodo.17839162)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17839414.svg)](https://doi.org/10.5281/zenodo.17839414)

Structured Orb Dynamics

Unified Manuscript and Data Repository

This repo collects the materials used in the study.

The manuscript, code, and the PR018 analysis are kept together so the workflow is easy to follow.

The project looks at image-plane motion using a set of simple geometric tools.

Curvature, basic derivative estimates, and a small state model were used to summarize the motion seen in a stabilized infrared recording (PR018).
No physical model is assumed; everything is based on what can be measured directly in the frames.

Install the usual Python packages (numpy, scipy, matplotlib). Nothing special is required.

Repository layout

manuscript/
PDF and source files. This is the full write-up that explains the reasoning and the steps.
Parts I–IV match the sections referenced in the release notes.

code/
Small set of scripts used for tracking, smoothing, and feature extraction.
Includes the functions for estimating curvature, curvature rate, and the state-likelihood routine.

data/
Processed track for PR018 (not the raw video).
Feature time series used in the plots.
Stored so the analysis can be checked without re-running everything.

results/
Figures used in the manuscript.
State-probability traces and related output.

supplement/
Notes on the GIMBAL video.
Explains what could be evaluated and what could not due to parallax and missing metadata.

Running the scripts will recreate the feature series and the plots.  
Paths may need to be changed depending on your setup.

python tracking/run_tracking.py
python features/compute_features.py
python model/run_state_model.py

PR018 summary

PR018 is the only dataset where a usable trajectory could be reconstructed.
The basic steps:

– stabilize the frames around the target
– extract a centroid track
– smooth the track
– compute velocity, acceleration, curvature, and curvature rate
– run the simple state model and save the probabilities

The results here are the same ones described in the manuscript.

GIMBAL note

A short write-up is included.
Only qualitative observations were possible.
No trajectory, no curvature estimates, no state sequence.

How to run the code

The scripts use standard Python packages (numpy, scipy, matplotlib).
Running them will recreate the feature series and the plots.
Paths may need to be edited depending on your setup.

python tracking/run_tracking.py
python features/compute_features.py
python model/run_state_model.py


Output is saved into the results/ folder.

Citation

If this work is used, please cite the manuscript:

Perry, C. (2025). Structured Orb Dynamics: Unified Manuscript and Data Repository.

DOI links are listed in the repository.
