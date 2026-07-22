**Numerical reconstruction of grounding-zone wedge (GZW) formation under frozen-bed conditions: why didn't MIS 2 GZWs form in Mackenzie Bay, southern part of the Beaufort Sea**

**Adam Y. Kashdan**

*Independent Researcher**, Montréal, Québec, Canada*

**Abstract**

The western sector of the Canadian Arctic, including Herschel, Richards, and Pullen (North Head) islands and Liverpool Bay, is characterized by a unique combination of relict massive ground ice and well-defined moraine complexes associated with the grounding line of the ancient ice sheet on the Beaufort Sea shelf. Using ¹⁴C and CO₂ extraction, other authors obtained direct ages of 32 220–25 830 cal yr BP from the massive ice bodies, placing their formation in MIS 3 and the MIS 3/2 transition (Wetterich et al., 2023). This extends the sole earlier constraint — a 21 290 cal yr BP CO₂‑derived radiocarbon date (MIS 2). On the same shelf, seismic profiles image a series of moraine ridges. We interpret these as grounding‑zone wedges (GZWs) — sediment piles built where grounded ice passes into a floating shelf. In a warm‑based setting, meltwater at the bed would cut effective pressure, allowing the ice to slide rapidly. Such sliding would erode and shear the substrate, making it hard to see how the observed ice bodies could have survived intact. Such sliding would erode and shear the substrate, making it extremely difficult to explain how intact, metres‑scale ice bodies could be preserved. If such conditions had prevailed over the western Canadian Arctic shelf during the Late Pleistocene, the permafrost table would have been sheared and the preserved bodies of massive ground ice — observed today on Herschel Island and adjacent coastlands — would have been largely destroyed. The very existence of these relict ice bodies, however, challenges this conventional view and points to a fundamentally different thermal and mechanical regime.

Here we present a numerical model that demonstrates how a cold-based or transition-regime glacier can preserve massive ice while still forming GZWs. We further explain the complete absence of MIS 2 GZWs in Mackenzie Bay as a consequence of insufficient time for wedge stabilisation, using quantitative simulations for MIS 4 (prolonged stillstands) vs MIS 2 (rapid retreat).

**1. Introduction**

The presence of well‑preserved massive ground ice in the western Canadian Arctic contradicts the conventional picture of a warm‑based ice sheet. If basal sliding had operated as assumed by classical models, the substrate would have been sheared and the ice bodies destroyed. Their survival, therefore, evades explanation under existing theory — and points toward a different set of subglacial conditions.

**Adhesive contact:** We propose that the ice sheet in this sector remained frozen to its bed — either persistently cold‑based or within a narrow thermal transition zone. Under such conditions, the glacier does not slide over the substrate; instead, the main velocity gradient shifts upward, into the basal ice layers. The bed itself stays fixed relative to the ice sole. As a result, the underlying massive ground ice is not subjected to shear deformation and retains its primary cryogenic structure.

**Damping role of frozen till**: High hydraulic conductivity (sandy till, ~65% sand) and the Coulomb strength of the underlying sediments prevent the build-up of excess pore pressure. Even under critical loads, deformation is localised within the moraine’s near-surface layer, leaving deep-seated ice bodies unaffected.

**Locality of glaciotectonics:** Rampton (1988) described "thrust moraines" from the Tuktoyaktuk coastlands, but these are not typical of the region. They occur only where local bed geometry or short‑lived thermal anomalies temporarily break the frozen‑bed condition. Elsewhere, the bed remained frozen and undeformed.

To show how well our model explains different scenarios, we applied it to data from the Mackenzie Trough in the southern Beaufort Sea. Unlike many other shelves, this region lacks grounding-zone wedges (GZWs) associated with the Last Glacial Maximum (MIS 2).

**2. Data (Batchelor et al., 2013)**

Research by Batchelor, Dowdeswell, and Pietras (2013) identified the following key features of Mackenzie Bay:

**Evidence of glacial activity**: Two Quaternary ice sheets extended across Mackenzie Bay, reaching the shelf edge.

**Absence of GZWs and trough-mouth fans**: Unlike typical glacial channels, only one small, isolated, buried GZW was found here, dating to an earlier glaciation (presumably the Illinoisian/Early Wisconsinian, MIS 4). No GZWs have been recorded for MIS 2. The continental slope lacks a large trough-mouth fan — an accumulative body characteristic of channels where a glacier remained stationary for a long time.

**Slope characteristics**: The continental slope of Mackenzie Bay is dissected by canyons, indicating an erosional (rather than accumulative) nature of Late Pleistocene sedimentation.

**3. Methodology**

The objective of this study is to numerically evaluate the conditions for proglacial landform development and identify the mechanisms that preserve ancient massive ground ice in the Beaufort Sea region. To achieve this, a numerical model was developed comprising three interconnected functional blocks that provide a comprehensive analysis of the "glacier–permafrost bed" system:

**Block I (Ice Dynamics and Sliding Physics):** We use the regularized sliding law of Zoet & Iverson (2020), which includes a Coulomb shear‑stress ceiling. This ceiling removes singularities at very low sliding speeds, so the numerical solution remains stable. It also defines the stress at which the bed material begins to deform plastically. Capturing this transition lets us simulate the mechanical coupling between the glacier sole and the frozen substrate without eroding the underlying massive ice — something a non‑regularized law would spuriously do.

**Block II (Geomorphological Sediment Transport):** We use the Exner equation to track sediment mass balance. It converts accumulation and erosion into changes in bed elevation. To model marginal moraine construction, we couple this equation with a sediment transport law. The coupled system then produces GZW geometries and captures postglacial reworking over time.

**Block III (Thermal Subsurface State)**: We model subsurface heat transfer using an enthalpy‑based solver. Instead of explicitly tracking the ice‑water boundary, we use a fixed‑grid method that lets the phase transition move through the grid cells. The enthalpy formulation handles latent heat release and uptake in both the porous till and the massive ice. This is critical because latent heat buffers temperature changes and directly controls whether relict ice bodies warm, degrade, or remain stable.

**4. Model Parametrization & Sensitivity**

The basal shear stress $\tau_b$ is governed by the regularized Coulomb sliding law proposed by Zoet & Iverson (2020):

$$\tau_b = \frac{\tau_{visc}^p \tau_c}{(\tau_{visc}^p + \tau_c^p)^{1/p}}$$

where $\tau_c = \mu_c N$ is the Coulomb sliding limit, $N$ is the effective pressure, $\mu_c$ is the friction coefficient, and $\tau_{visc} = A_{visc} U_b$ represents the viscous drag. When large clasts are present at the ice-bed interface, they concentrate stress, shifting the viscous-to-Coulomb transition to lower velocities by modifying the viscous component ($\tau_{visc} = A_{visc} \cdot f_{\text{clast}} \cdot U_b$, where the clast factor $f_{\text{clast}}$ is set to 3.0). If frozen-fringe debris is present on a hard bed, an additional rate-strengthening term is appended: $\tau_b \leftarrow \tau_b + 0.05 A_{visc} U_b$.

The proglacial sediment flux $q_s$ at the grounding line is modulated by the basal shear stress state:

$$q_s = q_{s,\text{base}} + \gamma \max(0, \tau_b - \tau_{\text{threshold}})$$

where $\tau_{\text{threshold}}$ is the critical shear threshold for till transport, and $\gamma$ is an erosion coefficient. In the Coulomb regime, the basal drag saturates, which caps the sediment flux at a maximum value (stabilizing the deposition process and preventing runaway erosion).


*Figure 1: Parameter sensitivity analysis of the Zoet & Iverson (2020) sliding law showing basal shear stress $\tau_b$ (left panel) and sediment flux $q_s$ (right panel) as functions of basal sliding speed $U_b$. Solid lines represent till beds with large clasts, and dashed lines represent till beds without clasts, evaluated across different friction coefficients ($\mu_c = 0.3, 0.6, 0.8$).*

The sensitivity sweep in Figure 1 demonstrates that higher friction coefficients ($\mu_c$) elevate the plastic Coulomb ceiling. The presence of clasts (solid curves) accelerates the transition from linear viscous behavior to Coulomb plasticity at much lower sliding velocities, stabilizing both the basal drag and the sediment flux earlier in the sliding cycle.

**5. Geological Scenarios and Stratigraphic Reconstruction**

We investigate two distinct geographic and stratigraphic domains: the Storfjorden trough (Svalbard margin) as a calibration case for staged retreat over bed topography, and the Mackenzie Trough (Beaufort Sea) to explain the absence of MIS 2 GZWs.

***5.1. Storfjorden: Calibration and Stacked GZW Mounds***

In Storfjorden, the subglacial topography consists of retrograde bed ridges that act as pins for the grounding line. Using ages derived from post-glacial sediment cores (Nielsen & Rasmussen 2018; Gusev et al. 2024), we model the formation of three grounding-zone wedges at progressive landward stillstands:

**Outer GZW** (calibrated to core HH12-1209GC, basal age ~14.25 ka BP): Grounding line stabilized at 24 km, forming a wedge with a peak thickness of 38 m over a duration of 1,000 years.

**Middle GZW** (calibrated to core JM10-12GC, basal age ~12.66 ka BP): Grounding line stabilized at 15 km, forming a wedge with a peak thickness of 38 m over a duration of 1,590 years.

**Inner GZW** (calibrated to core NP05-86GC, basal age ~11.46 ka BP): Grounding line stabilized at 5 km, forming a wedge with a peak thickness of 38 m over a duration of 1,200 years.


*Figure 2: Simulated stratigraphy of the Storfjorden trough calibrated to the R_2018 seismic profile. The upper panel displays the stratigraphic horizons (TPQ: Top Pre-Quaternary, TG: Top Glacial, Seabed). The lower panel shows the filled geologic units (basement bedrock, glacial deposits GD, and deglacial-to-Holocene drape DHD) and locates the three GZW mounds with their respective ages and thicknesses.*

The simulation successfully reproduces the observed seismic stratigraphic units: a thin background till sheet (~4 m) in the outer zone, a thicker till basin (~10 m) between the middle and inner wedges, and a conformable drape of post-glacial sediment (DHD) overlaying the wedges.

***5.2. Mackenzie Margin: Classic vs. Lateral GZWs***

Unlike the staged, topography-pinned retreat of Storfjorden, the Mackenzie Margin shows a binary behavior. Under prolonged stillstand conditions (such as the early Wisconsinan glaciation, MIS 4), the ice stream had sufficient time to build massive sediment barriers:

**Classic GZW**: Formed at the ice-stream terminus (reaching a thickness of ~127 m), requiring a stabilization period of ~2,650 years under steady-state sediment flux ($q_s \approx 0.048\text{ m}^2/\text{yr}$).

**Lateral GZW**: Formed along the lateral ice-stream margin where shear stresses are highest (reaching a thickness of ~200 m), requiring a stillstand of ~4,170 years.


*Figure 3: Simulated stratigraphic cross-sections for Classic (terminus-type, upper panel) and Lateral (margin-type, lower panel) grounding-zone wedges along the Mackenzie Shelf, representing the MIS 4 glaciation. The classic GZW is buried under 20 m of post-glacial sediment, while the lateral GZW remains near-surface.*

**6. Dynamic Flowline Simulations: MIS 4 vs. MIS 2**

To test why GZWs did not form during the Last Glacial Maximum (MIS 2) in Mackenzie Bay, we coupled the 1D ice flowline equations directly to the dynamic bed-updating model.

We contrasted two physical configurations:

**Storfjorden Configuration**: A bed containing retrograde ridges with a gradual 30% reduction in accumulation forcing over 6,000 years.

**Mackenzie Configuration**: A smooth, prograde bed (linear slope) with a rapid 65% reduction in accumulation forcing over 500 years.


*Figure 4: Coupled SSA flowline and dynamic bed-update simulation. Panel A: Grounding-line retreat trajectory over time. Panel B: Zoet sediment flux $q_s$ at the grounding line. Panel C: Resulting stratigraphy and stacked GZW deposits for the Storfjorden scenario. Panel D: Resulting stratigraphy for the Mackenzie scenario.*

The coupled model reveals that:

In the **Storfjorden** scenario, the retrograde ridges act as structural pins. As the grounding line retreats, it temporarily stalls at each ridge. The sediment flux $q_s$ remains active at the stillstand, allowing massive sediment volumes to accumulate and build distinct, stacked GZWs that shallow the water column and provide mechanical buttressing.

In the **Mackenzie** scenario, the combination of a smooth prograde bed and rapid retreat forcing (MIS 2) prevents the grounding line from stalling. The grounding line retreats continuously. Consequently, the sediment flux is distributed over a wide area rather than concentrated at a single point, depositing a thin, conformable till drape (< 1 m) rather than a GZW.

**7. Geothermal and Subsurface Permafrost Structure**

To characterize the thermal state of the subglacial strata, we implemented a transient 1-D permafrost temperature and ice saturation field along the Mackenzie Shelf transect (adapted from the 2019 SuPerMAP framework).


*Figure 5: Synthetic cross-section of the Mackenzie Shelf permafrost thermal regime. The upper panel displays the subsurface temperature field $T(x, y)$ with key isotherms ($-5, -2, -1, 0\ ^\circ\text{C}$). The lower panel displays the corresponding ice saturation $S(x, y)$, highlighting the cold, ice-saturated relict permafrost wedge extending offshore.*

The modeling reveals a prominent offshore wedge of relict permafrost that is highly ice-saturated ($S \approx 1$) at depth due to temperatures remaining below $-1.5\ ^\circ\text{C}$. Near the shelf edge, the permafrost degrades due to warming offshore boundary conditions. The presence of this cold, ice-bearing permafrost shelf supports the "cold-based" or transitional subglacial boundary conditions. The subglacial permafrost retains its structural integrity because the ice sheet sole remains frozen to or in adhesive contact with the bed, shifting the main shearing deformation upward into the basal ice layers.


**8. Discussion: Preservation of Relict Ice and Glaciotectonics**

We focus on the phase transition when basal ice warms toward the pressure‑melting point. Laboratory tests show (Zoet & Iverson, 2020) that till saturation and steady‑state shear stress do not develop instantly; both evolve over time. The gradual nature of this transition justifies our use of the enthalpy method and the regularized sliding law. Together, these tools capture the transient regime between a frozen bed and active sliding. During this window, the model builds the thickest grounding‑zone wedges while the permafrost and underlying massive ice remain mechanically undisturbed.

The results allow us to hypothesize a preservation mechanism for ancient massive ice in the Western Arctic, based on the formation of a "cold thin glacier" regime with a thin, deformable zone (< 0.5 m). In this regime, the lower cold glacial ice acts as a protective layer that absorbs shear deformations, ensuring the underlying ground ice remains in an elastic state. To verify this hypothesis, drilling operations in proglacial ablation zones are required, followed by core sampling of the entire subglacial and ground-ice profiles and microseismic anisotropy measurements in the near-surface layer to assess the distribution of deformation.

**Numerical demonstration**: The results (Fig. 6) show that in the cold-based scenario, the basal shear stress and velocity profiles confirm the complete preservation of the permafrost substrate. Because the ice remains frozen to the bed, the sliding velocity at the ice-bed interface is zero. The main shear strain rate gradient shifts entirely into the basal ice layers of the glacier (localized within a thin shear zone at the base of the ice column). Consequently, the subglacial permafrost and massive ground ice remain in a stationary, undeformed state ($u = 0, \dot{\epsilon}_{xz} = 0$), preserving their cryogenic structures. In contrast, under a warm-based regime, active sliding at the interface occurs ($u_b > 0$), and significant shear deformation penetrates tens of meters into the bed, inevitably deforming and destroying massive ground ice deposits.


*Figure 6: Vertical profiles of velocity $u(z)$ (solid lines) and shear strain rate $\dot{\epsilon}_{xz}$ (dashed lines) for a warm-based glacier with basal sliding and shear penetration into the permafrost bed (left panel) versus a cold-based glacier where the bed is frozen and shear is entirely localized within the basal ice (right panel).*

The absence of GZWs in Mackenzie Bay provides compelling confirmation of our thesis that wedge formation requires not only sediment but also a sufficient time window for its accumulation in the proglacial zone during a relatively slow (or halted by other factors) glacial retreat.

**9. Conclusion**

Our results identify a frozen-bed or narrowly transitional thermal regime as the key to preserving relict massive ice beneath the Beaufort shelf. When basal temperatures stay below the pressure-melting point, the ice sheet does not slide over its bed. Instead, motion is accommodated by internal deformation within the lowermost ice column and, where present, within a thin (<0.5 m) layer of frozen till. The sliding law we implemented in Block I — with its regularized Coulomb limit and coarse-debris term — reproduces the observed sequence of grounding-zone wedges without allowing shear to penetrate into the deeper permafrost. The model also demonstrates that wedge formation arises from internal ice-sediment-thermal feedbacks. No external forcing — neither tectonic pulses nor climatic oscillations — is required to generate the observed stratigraphic pattern.

***Future Research***

Future research will focus on a detailed analysis of the influence of local lithological factors, including the grain-size distribution of moraines, on the preservation of relict ice. In addition, full paleo-climatic simulations using CryoGrid.jl along the Mackenzie transect will replace the current synthetic thermal visualisation with observation-constrained permafrost evolution.

***Data Available***

All Python scripts used for data acquisition, gap-filling, statistical analysis and figure production, together with the processed dataset, are openly available at https://github.com/adamkashdan/slip_law_glaciers.


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
