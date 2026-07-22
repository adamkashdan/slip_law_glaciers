# Glacier Dynamics Modeling & Grounding Zone Wedge (GZW) Formation

This repository contains a suite of Python and Julia numerical models focused on glacier sliding dynamics, thermal regimes, and sediment transport/accumulation leading to the formation of Grounding Zone Wedges (GZWs) at the grounding line of ice streams.

The models incorporate modern glaciological slip formulations (Zoet & Iverson 2020) and ice-stream flow dynamics (Shallow Shelf Approximation, SSA).

---

## 🔬 Key Physical Concepts

1. **Zoet-Iverson Sliding Law (Zoet & Iverson 2020)**  
   Implemented as a regularized Coulomb friction law (see the function `[regularized_coulomb_drag](file:///Users/esteebarin/slip_law_glaciers/zoet_parameter_sensitivity.py#L14)`). The model accounts for:
   * Presence of clasts and debris (`has_clasts` and `has_debris`).
   * Bed type (`bed_type`: soft sediment vs. hard bedrock).
   * Dependency of basal shear stress ($\tau_b$) on sliding velocity ($U_b$) and effective pressure ($N$).

2. **Grounding Line Sedimentation & Bathymetric Evolution**  
   The growth of Grounding Zone Wedges (GZWs) is simulated by coupling sediment flux transport (see the function `[compute_sediment_flux](file:///Users/esteebarin/slip_law_glaciers/zoet_parameter_sensitivity.py#L24)`) with the Exner mass conservation equation to update seafloor bathymetry over time.

3. **Glacial Regimes: Warm-based vs. Cold-based**  
   Models include distinct vertical profiles for velocity and shear strain rates:
   * **Warm-based**: Significant basal slip at the ice-bed interface and shear penetration into the subglacial permafrost bed.
   * **Cold-based**: Adhesive contact with the bed ($u=0$ at the interface, preserving subglacial landforms) with shear localization confined to a thin basal ice layer.

---

## 📂 File Directory & Script Index

### 🖥️ Core Simulators & Models
* `[SSA_dynamic_gzw.py](file:///Users/esteebarin/slip_law_glaciers/SSA_dynamic_gzw.py)` — Coupled 1D SSA (Shallow Shelf Approximation) ice flowline + dynamic GZW sedimentation. It simulates two main scenarios:
  1. *Storfjorden* — retrograde bed ridges causing grounding line stillstands and stacked GZWs.
  2. *Mackenzie Bay* — smooth prograde bed with rapid retreat and no stillstands.
* `[SSA_simple.py](file:///Users/esteebarin/slip_law_glaciers/SSA_simple.py)` — A Python port of the 1D SSA flowline glacier model (Robel 2021).
* `[ice_stream_ocean_model.py](file:///Users/esteebarin/slip_law_glaciers/ice_stream_ocean_model.py)` — Coupled ice-stream-ocean simulator with the Zoet sliding law, dynamic bathymetry updates, and grounding line position tracking.

### 📊 Parameter Sensitivity & Visualization
* `[plot_cold_based_demonstration.py](file:///Users/esteebarin/slip_law_glaciers/plot_cold_based_demonstration.py)` — Visualizes vertical velocity and shear strain rate profiles comparing warm vs. cold-based glaciers. Saves output to `[cold_based_shear_preservation.png](file:///Users/esteebarin/slip_law_glaciers/cold_based_shear_preservation.png)`.
* `[zoet_parameter_sensitivity.py](file:///Users/esteebarin/slip_law_glaciers/zoet_parameter_sensitivity.py)` — Parameter sensitivity analysis for the Zoet & Iverson (2020) law, exploring relationships between velocity, shear stress, and sediment flux.
* `[zoet_stick_slip_cycles_storfjordenGWZs.py](file:///Users/esteebarin/slip_law_glaciers/zoet_stick_slip_cycles_storfjordenGWZs.py)` — GZW formation and stick-slip cycle simulator calibrated to the R_2018 seismic profile (Storfjorden).
* `[zoet_stick_slip_cycles_mackenzieGWZs.py](file:///Users/esteebarin/slip_law_glaciers/zoet_stick_slip_cycles_mackenzieGWZs.py)` — Stick-slip and GZW simulator calibrated to the AG_2014 seismic profile (Amundsen Gulf / Mackenzie Margin).
* `[mackenzie_transect_plot.jl](file:///Users/esteebarin/slip_law_glaciers/mackenzie_transect_plot.jl)` — A Julia script used for plotting/processing Mackenzie transect data.

---

## ⚙️ Setup & Execution

The project is configured to run with Python 3.12 (stored in the virtual environment `env/`).

### Running Simulations

To run any Python model, use the virtual environment's Python interpreter:

```bash
# Generate the warm vs. cold-based comparison plot
env/bin/python plot_cold_based_demonstration.py

# Analyze sliding law parameter sensitivity
env/bin/python zoet_parameter_sensitivity.py
```

All generated plots and figures are saved directly in the project root directory.