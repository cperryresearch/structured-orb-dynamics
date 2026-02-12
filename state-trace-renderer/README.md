## State Trace Renderer

## Overview

The State Trace Renderer is a small visualization utility used within the Structured Orb Dynamics (SOD) workflow to display precomputed state-segmented motion traces together with their supporting geometric signals.

It exists solely to make segmentation structure visible for inspection.

The renderer does not implement segmentation logic, classification, or inference. All state construction occurs upstream within the SOD methodology. This component only renders results that have already been computed.

If removed, no scientific capability is lost. It is a visualization aid only.


## Scope and Role

Structured Orb Dynamics defines the geometric quantities, persistence constraints, and rules that produce a State-Segmented Motion Trace.

The renderer consumes those outputs and presents them in a consistent, reproducible visual form. Its role is limited to inspection and communication. It does not contribute to the derivation of states or to any downstream decision process.

This separation between method and visualization is intentional. The renderer is not part of the analytical framework; it is a supporting instrument.


## Inputs

Inputs consist of a time-ordered trajectory sampled at fixed cadence, per-sample state labels produced upstream, and one or more supporting geometric signals.

These inputs are treated as immutable. The renderer performs no resampling, smoothing, interpolation, or feature construction.


## Outputs

The output consists of deterministic figures showing the trajectory colored by preassigned state together with aligned plots of the provided geometric signal(s).

No statistics, summaries, or derived measurements are produced. The figures are intended for direct visual inspection only.


## Constraints

To preserve methodological integrity, the renderer applies no transformations beyond plotting. Data are displayed as provided. No filtering, enhancement, or optimization steps are introduced.

The component is not a model, classifier, or decision system. It makes no claims and draws no conclusions.


## Relationship to the Repository

This directory contains only the minimal code required to render State-Segmented Motion Traces for documentation, examples, and reproducible figures accompanying the SOD manuscript.

It should remain small, bounded, and implementation-focused.

## Reproducibility Notes

The State Trace Renderer is designed to produce deterministic output from fixed inputs.

To support reproducibility:

- The renderer performs **no state computation, smoothing, resampling, or inference**.
- All figures are generated from precomputed artifacts.
- The canonical example (`examples/barn_swallow_vi_b_example.png`) is treated as a reference output.
- Equal-aspect geometry is enforced to prevent spatial distortion.
- Fixed SOD state color mapping is applied consistently.

---

### Environment

Reproducibility was verified using:

- Python 3.11.x  
- matplotlib 3.8.x  
- numpy 1.26.x  

Exact versions may be pinned in a `requirements.txt` file if stricter environment locking is required.

---

### Deterministic Output Verification

Running:

```bash
python src/render_trace.py
```

should regenerate the canonical example PNG without visual deviation.

Optional hash verification instructions are provided below.

---

### Canonical PNG SHA256

Reference file: `examples/barn_swallow_vi_b_example.png`

SHA256:

63053D7CBFB11561ACCA8E2C08FE1909516DAF4BB9A0BC88028D42F193634E21

After regenerating the figure, recompute the hash locally and confirm byte-level identity to verify deterministic rendering.

