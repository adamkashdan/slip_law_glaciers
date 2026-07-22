**Numerical reconstruction of grounding-zone wedge (GZW) formation under frozen-bed conditions: why didn't MIS 2 GZWs form in Mackenzie Bay, southern part of the Beaufort Sea**

**Adam Y. Kashdan**

*Independent Researcher*, Montréal, Québec, Canada*

**Abstract**

The western sector of the Canadian Arctic, including Herschel, Richards, and Pullen (North Head) islands and Liverpool Bay, contains both relict massive ground ice and moraine complexes formed near the grounding line of the ancient Beaufort Sea ice sheet. Direct radiocarbon ages (via ¹⁴C and CO₂ extraction) from these massive ice bodies range from 32,220 to 25,830 cal yr BP, placing their formation in MIS 3 and the MIS 3/2 transition (Wetterich et al., 2023). This extends the only previous constraint of 21,290 cal yr BP (MIS 2). On the same shelf, seismic profiles show moraine ridges interpreted as grounding-zone wedges (GZWs) — sediment accumulations deposited where grounded ice meets a floating shelf. In a warm-based regime, subglacial meltwater decreases effective pressure, causing rapid sliding that erodes and shears the bed. Under these conditions, meter-scale massive ice bodies would have been sheared and destroyed during the Late Pleistocene. Their survival on Herschel Island and adjacent coastlands indicates that the bed remained frozen and stable.

We present a numerical model showing how a cold-based or transitional glacier can preserve massive ground ice while building GZWs. We show that the absence of MIS 2 GZWs in Mackenzie Bay is due to a lack of stabilization time during rapid ice retreat, comparing simulations for MIS 4 (long stillstands) and MIS 2 (rapid retreat).

**1. Introduction**

Well-preserved massive ground ice in the western Canadian Arctic contradicts models of a warm-based ice sheet. Active basal sliding would have sheared the substrate and destroyed the ice. Explaining their preservation requires a different subglacial thermal and mechanical state.

We propose that the ice sheet in this sector was frozen to its bed, either persistently cold-based or within a narrow thermal transition zone. Under these conditions, the glacier moves by internal deformation of the basal ice rather than sliding. The bed remains stationary relative to the ice sole, protecting the underlying massive ground ice from shear deformation and preserving its primary cryogenic structure.

This frozen-bed state is supported by the high hydraulic conductivity of the sandy subglacial till (~65% sand) and its Coulomb strength, which prevent excess pore pressure build-up. Under loading, deformation remains localized within the near-surface layer of the moraine, leaving deeper massive ice intact. The glaciotectonic thrust moraines described by Rampton (1988) in the Tuktoyaktuk coastlands likely represent local topographic pinning or transient thermal anomalies; elsewhere, the bed remained stable.

We apply our model to the Mackenzie Trough in the southern Beaufort Sea. Unlike other glaciated margins, this shelf lacks GZWs associated with the Last Glacial Maximum (MIS 2).

**2. Data (Batchelor et al., 2013)**

Batchelor et al. (2013) identified several key characteristics of the Mackenzie Bay margin:
* **Glacial footprint**: Two Quaternary ice sheets advanced across Mackenzie Bay to the shelf edge.
* **Lack of GZWs and fans**: Only one small, buried GZW exists, dating to an earlier glaciation (likely MIS 4). No GZWs are recorded for MIS 2, and the continental slope lacks the large trough-mouth fans typical of long-term ice stillstands.
* **Erosional slope**: The shelf slope is cut by canyons, indicating that Late Pleistocene sedimentation was primarily erosional rather than depositional.

**3. Methodology**

We developed a numerical model to evaluate proglacial landform development and the preservation of massive ground ice. The model couples three physical components:
1. **Ice Dynamics and Sliding Physics**: The Shallow Shelf Approximation (SSA) solver uses the regularized sliding law of Zoet & Iverson (2020) to capture the transition from viscous flow to Coulomb plasticity at the glacier sole. This removes numerical singularities at low speeds and defines the stress threshold for subglacial till deformation, allowing us to model the coupling between the ice and the bed without artificial erosion.
2. **Sediment Transport**: The Exner equation tracks sediment mass balance at the grounding line, converting local erosion and deposition into changes in bed elevation to simulate GZW growth.
3. **Thermal Subsurface State**: An enthalpy-based heat transfer solver models phase transitions in both the till and massive ice, accounting for latent heat buffering to evaluate the thermal stability of subglacial permafrost.

**4. Model Parametrization & Sensitivity**

Basal shear stress $\tau_b$ follows the regularized Coulomb sliding law (Zoet & Iverson, 2020):

$$\tau_b = \frac{\tau_{visc}^p \tau_c}{(\tau_{visc}^p + \tau_c^p)^{1/p}}$$

where $\tau_c = \mu_c N$ is the Coulomb sliding limit, $N$ is the effective pressure, $\mu_c$ is the friction coefficient, and $\tau_{visc} = A_{visc} U_b$ represents the viscous drag. When large clasts are present at the ice-bed interface, they concentrate stress, shifting the viscous-to-Coulomb transition to lower velocities by modifying the viscous component ($\tau_{visc} = A_{visc} \cdot f_{\text{clast}} \cdot U_b$, where the clast factor $f_{\text{clast}}$ is set to 3.0). For a hard bed with frozen-fringe debris, an additional rate-strengthening term is added: $\tau_b \leftarrow \tau_b + 0.05 A_{visc} U_b$.

The proglacial sediment flux $q_s$ at the grounding line is modulated by the basal shear stress:

$$q_s = q_{s,\text{base}} + \gamma \max(0, \tau_b - \tau_{\text{threshold}})$$

where $\tau_{\text{threshold}}$ is the critical shear threshold for till transport, and $\gamma$ is an erosion coefficient. In the Coulomb regime, basal drag saturates, capping the sediment flux at a maximum value to prevent runaway erosion.

*Figure 1: Parameter sensitivity analysis of the Zoet & Iverson (2020) sliding law showing basal shear stress $\tau_b$ (left panel) and sediment flux $q_s$ (right panel) as functions of basal sliding speed $U_b$. Solid lines represent till beds with large clasts, and dashed lines represent till beds without clasts, evaluated across different friction coefficients ($\mu_c = 0.3, 0.6, 0.8$).*

The parameter sweep in Figure 1 shows that higher friction coefficients ($\mu_c$) increase the Coulomb ceiling. Clasts (solid curves) accelerate the transition from linear viscous behavior to Coulomb plasticity at lower sliding velocities, stabilizing basal drag and sediment flux.

**5. Geological Scenarios and Stratigraphic Reconstruction**

We simulate two geographic areas: the Storfjorden trough (Svalbard margin) to calibrate retreat over pinning points, and the Mackenzie Trough (Beaufort Sea) to examine GZW formation under different retreat rates.

***5.1. Storfjorden: Calibration and Stacked GZW Mounds***

In Storfjorden, subglacial topography consists of retrograde bed ridges that pin the grounding line. Using ages from post-glacial sediment cores (Nielsen & Rasmussen 2018; Gusev et al. 2024), we model three grounding-zone wedges at progressive landward stillstands:
* **Outer GZW** (core HH12-1209GC, basal age ~14.25 ka BP): Grounding line stabilized at 24 km, forming a 38 m thick wedge over 1,000 years.
* **Middle GZW** (core JM10-12GC, basal age ~12.66 ka BP): Grounding line stabilized at 15 km, forming a 38 m thick wedge over 1,590 years.
* **Inner GZW** (core NP05-86GC, basal age ~11.46 ka BP): Grounding line stabilized at 5 km, forming a 38 m thick wedge over 1,200 years.

*Figure 2: Simulated stratigraphy of the Storfjorden trough calibrated to the R_2018 seismic profile. The upper panel displays the stratigraphic horizons (TPQ: Top Pre-Quaternary, TG: Top Glacial, Seabed). The lower panel shows the filled geologic units (basement bedrock, glacial deposits GD, and deglacial-to-Holocene drape DHD) and locates the three GZW mounds with their respective ages and thicknesses.*

The simulation matches the observed seismic stratigraphic units: a thin till sheet (~4 m) in the outer zone, a thicker till basin (~10 m) between the middle and inner wedges, and a conformable drape of post-glacial sediment (DHD) overlying the wedges.

***5.2. Mackenzie Margin: Classic vs. Lateral GZWs***

Unlike Storfjorden, the Mackenzie Margin shows a binary behavior. Under prolonged stillstand conditions (such as the early Wisconsinan glaciation, MIS 4), the ice stream had sufficient time to build massive sediment barriers:
* **Classic GZW**: Formed at the ice-stream terminus (thickness ~127 m), requiring a stabilization period of ~2,650 years under steady-state sediment flux ($q_s \approx 0.048\text{ m}^2/\text{yr}$).
* **Lateral GZW**: Formed along the lateral ice-stream margin where shear stresses are highest (thickness ~200 m), requiring a stillstand of ~4,170 years.

*Figure 3: Simulated stratigraphic cross-sections for Classic (terminus-type, upper panel) and Lateral (margin-type, lower panel) grounding-zone wedges along the Mackenzie Shelf, representing the MIS 4 glaciation. The classic GZW is buried under 20 m of post-glacial sediment, while the lateral GZW remains near-surface.*

**6. Dynamic Flowline Simulations: MIS 4 vs. MIS 2**

To test why GZWs did not form during the Last Glacial Maximum (MIS 2) in Mackenzie Bay, we coupled 1D ice flowline dynamics to the bed-updating model, comparing two configurations:
* **Storfjorden**: A bed with retrograde ridges under a gradual 30% reduction in accumulation forcing over 6,000 years.
* **Mackenzie**: A smooth, prograde bed (linear slope) with a rapid 65% reduction in accumulation forcing over 500 years.

*Figure 4: Coupled SSA flowline and dynamic bed-update simulation. Panel A: Grounding-line retreat trajectory over time. Panel B: Zoet sediment flux $q_s$ at the grounding line. Panel C: Resulting stratigraphy and stacked GZW deposits for the Storfjorden scenario. Panel D: Resulting stratigraphy for the Mackenzie scenario.*

In the Storfjorden scenario, retrograde ridges act as structural pins. The grounding line stalls at each ridge during retreat. Steady sediment flux at these pinning points builds stacked GZWs that shallow the water column and buttress the ice stream.

In the Mackenzie scenario, the smooth prograde bed and rapid forcing trigger continuous retreat. The sediment is distributed broadly instead of accumulating at a fixed grounding line, resulting in a thin till drape (< 1 m) rather than a wedge.

**7. Geothermal and Subsurface Permafrost Structure**

To characterize the thermal state of the subglacial strata, we simulated transient 1D permafrost temperatures and ice saturation along the Mackenzie Shelf transect (adapted from the SuPerMAP framework; Overduin et al., 2019).

*Figure 5: Synthetic cross-section of the Mackenzie Shelf permafrost thermal regime. The upper panel displays the subsurface temperature field $T(x, y)$ with key isotherms ($-5, -2, -1, 0\ ^\circ\text{C}$). The lower panel displays the corresponding ice saturation $S(x, y)$, highlighting the cold, ice-saturated relict permafrost wedge extending offshore.*

The model shows an offshore wedge of relict permafrost that remains ice-saturated ($S \approx 1$) at depth due to temperatures below $-1.5\ ^\circ\text{C}$. Near the shelf edge, the permafrost degrades due to warming marine boundary conditions. The presence of this cold, ice-bearing permafrost supports a cold-based or transitional subglacial boundary. Because the ice remains frozen to the bed, the main shear deformation is accommodated within the basal ice layers, preserving the structural integrity of the underlying permafrost.


**8. Discussion: Preservation of Relict Ice and Glaciotectonics**

During the transition when basal ice warms toward the pressure-melting point, subglacial till saturation and shear stress evolve transiently (Zoet & Iverson, 2020). Using an enthalpy method coupled with the regularized sliding law captures this transition. The model builds grounding-zone wedges during this transient phase while the underlying permafrost and massive ice remain stable.

We hypothesize that ancient massive ice in the Western Arctic was preserved by a cold-based or transitional glacier regime, where shear deformation was absorbed by basal ice layers rather than the bed. In this regime, the frozen boundary layer acts as a buffer. Testing this hypothesis requires drilling and core sampling across subglacial till and ground-ice profiles, along with microseismic anisotropy measurements to assess subglacial shear distribution.

Our simulations show that in the cold-based scenario, zero sliding velocity at the ice-bed interface shifts the main shear strain rate gradient into the basal ice column. Consequently, the subglacial permafrost and massive ground ice remain undeformed ($u = 0, \dot{\epsilon}_{xz} = 0$), preserving their cryogenic structures. Under a warm-based regime, active sliding ($u_b > 0$) causes significant shear deformation to penetrate tens of meters into the bed, which would deform and destroy massive ground ice deposits.

The absence of GZWs in Mackenzie Bay indicates that wedge formation requires both sediment supply and sufficient stabilization time during slow or halted ice retreat.

**9. Conclusion**

A frozen-bed or transitional thermal regime explains the preservation of relict massive ice beneath the Beaufort shelf. Below the pressure-melting point, ice sheet motion is accommodated by internal deformation within the basal ice column rather than basal sliding. The regularized sliding law, incorporating a Coulomb limit and a coarse-debris term, simulates grounding-zone wedge growth without introducing shear deformation into the deeper permafrost. The model shows that wedge formation can arise from internal feedbacks between ice, sediment, and heat transfer without requiring external tectonic or climatic forcing.

***Future Research***

Future work will analyze the influence of local lithology, including grain-size distribution, on permafrost preservation. Additionally, transient paleo-climatic simulations using CryoGrid.jl along the Mackenzie transect will replace the synthetic thermal visualization with observation-constrained permafrost evolution.

***Code and Data Availability***

All numerical simulation codes (Python and Julia) for the coupled SSA flowline, basal sliding parameter sweeps, sediment transport, and subsurface thermal modeling, along with calibration datasets and plotting scripts, are openly available at https://github.com/adamkashdan/slip_law_glaciers.


**References**

Batchelor, C. L., Dowdeswell, J. A., & Pietras, J. T. (2013). Variable history of Quaternary ice-sheet advance across the Beaufort Sea margin, Arctic Ocean. *Geology*. https://doi.org/10.1130/G33669.1

Bennett, M. R., & Glasser, N. F. (2009). *Glacial Geology: Ice Sheets and Landforms* (2nd ed.). Wiley-Blackwell.

Gusev, E. A., Krylov, A. A., Sazonov, A. Yu., Elkina, D. V., Karpikov, A. A., Khosnulina, T. I., Zykov, E. A., Paltsev, I. O., Lodochnikova, A. S., Khokhulya, A. V., Parfenyuk, S. N., Rikhman, M. A., Rogova, I. V., Golosnoy, A. S., Bordukov, K. Yu., Zakharov, V. Yu., & Krylov, A. V. (2024). Quaternary sediments of the Storfjorden trough (Barents Sea). *Relief and Quaternary deposits of the Arctic, Subarctic and North-West Russia,* (11), 69–80. (in Russian). https://doi.org/10.24412/2687-1092-2024-11-69-80

Kashdan, A. Y., & Sheinkman, V. S. (2025). The origin of Herschel Island (Canadian Arctic): a paleocryological approach. In *Relief and Quaternary deposits of the Arctic, Subarctic and North-West Russia*, (12), 87–94. (in Russian). https://doi.org/10.24412/2687-1092-2025-12-87-94

Murton, J. B., Waller, R. I., Hart, J. K., Whiteman, C. A., Pollard, W. H., & Clark, I. D. (2004). Stratigraphy and glaciotectonic structures of permafrost deformed beneath the northwest margin of the Laurentide Ice Sheet, Tuktoyaktuk Coastlands, Canada. *Journal of Glaciology*, 50(170), 399–412.

Overduin, P. P., Schneider von Deimling, T., Miesner, F., Grigoriev, M. N., Ruppel, C. D., Vasiliev, A., et al. (2019). Submarine permafrost map in the Arctic modeled using 1-D transient heat flux (SuPerMAP). *Journal of Geophysical Research: Oceans*, 124, 3490–3507. https://doi.org/10.1029/2018JC014675

Potapov, I. I., & Snigur, K. S. (2019). Solving of the Exner equation for morphologically complex bed. *Computer Research and Modeling*, 11(3), 449–461.

Rampton, V. N. (1988). Quaternary geology of the Tuktoyaktuk coastlands, Northwest Territories. *Geological Survey of Canada, Memoir 423*. https://doi.org/10.4095/126937

Schlegel, R., Zoet, L. K., Booth, A. D., Smith, A. M., Clark, R. A., & Brisbourne, A. M. (2025). Subglacial landscape formation and sediment discharge: Relating basal conditions to bedform dimensions and properties at Rutford Ice Stream, West Antarctica. *Boreas*.

Wetterich, S., Kizyakov, A. I., Opel, T., Grotheer, H., Mollenhauer, G., & Fritz, M. (2023). Ground‑ice origin and age on Herschel Island (Qikiqtaruk), Yukon, Canada. Quaternary Science Advances, 10, 100077. https://doi.org/10.1016/j.qsa.2023.100077

Zoet, L. K., & Iverson, N. R. (2020). A slip law for glaciers on deformable beds. *Science*, 368(6486), 76–78. https://doi.org/10.1126/science.aaz1183
