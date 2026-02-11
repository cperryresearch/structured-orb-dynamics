:::
#!/usr/bin/env python3
"""
State Trace Renderer

Pure visualization only.
Consumes precomputed arrays and renders:
• trajectory colored by state
• supporting geometric signal vs time

No computation. No smoothing. No inference.
"""

import json
import numpy as np
import matplotlib.pyplot as plt

---------------------------------------------------------------------
Fixed SOD palette (locked standard)
---------------------------------------------------------------------

PALETTE = {
"Straight": "#4C78A8", # muted blue
"Turn": "#F58518", # amber
"Hover": "#54A24B", # green
"Orb": "#9D755D", # neutral/desaturated
}

---------------------------------------------------------------------
Loader
---------------------------------------------------------------------

def load_bundle(path):
data = np.load(path, allow_pickle=True)

xy = data["xy"]
state = data["state"]
signal = data["signal"]
t = data["t"] if "t" in data else np.arange(len(xy))

meta = {}
if "meta_json" in data:
    meta = json.loads(str(data["meta_json"]))

return xy, state, signal, t, meta

---------------------------------------------------------------------
Plotter
---------------------------------------------------------------------

def render_trace(bundle_path, out_path="trace.png"):
xy, state, signal, t, meta = load_bundle(bundle_path)

fig, (ax_traj, ax_sig) = plt.subplots(
    2, 1,
    figsize=(6, 6),
    height_ratios=[2, 1],
    constrained_layout=True
)

# ---- Panel A: trajectory ----
for s in np.unique(state):
    mask = state == s
    ax_traj.plot(
        xy[mask, 0],
        xy[mask, 1],
        color=PALETTE.get(s, "black"),
        linewidth=2,
        label=s
    )

ax_traj.set_xlabel("x")
ax_traj.set_ylabel("y")
ax_traj.set_title("State-Segmented Trajectory")
ax_traj.legend(frameon=False)

# ---- Panel B: signal ----
ax_sig.plot(t, signal, linewidth=1)
ax_sig.set_xlabel("time")
ax_sig.set_ylabel("signal")

if meta:
    fig.suptitle(meta.get("dataset", "State Trace Renderer Example"))

fig.savefig(out_path, dpi=300)
plt.close(fig)

---------------------------------------------------------------------

if name == "main":
render_trace(
"../examples/barn_swallow_vi_b_example.npz",
"barn_swallow_vi_b_example.png"
)
:::
