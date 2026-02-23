# Project Proposal: Mapping Tiger Corridor Connectivity and Threats in India

**Author:** Kiran Balasubramanian
**Date:** February 21, 2026
**Course:** GIS Project — Phase 2
**Project Type:** ArcGIS Story Map (Standalone, linked to Phase 1)
**Phase 1 Story Map:** https://arcg.is/00bXi44
**Last Updated:** February 21, 2026

---

## Title, Introduction and Statement of Problem

### Title

**Under Pressure: Spatial Analysis of Tiger Corridor Connectivity and Landscape Threats in India (2021)**

### Introduction

Phase 1 of this project documented a remarkable conservation achievement: India's tiger population more than doubled between 2006 and 2022, from approximately 1,411 to 3,682 individuals, with seven featured reserves showing consistent population recovery. That story, however, is incomplete. Tigers do not live in reserves alone — they move between them, dispersing across agricultural and human-dominated landscapes to colonize new habitat, find mates, and maintain the genetic diversity that wild populations require for long-term viability.

The landscapes between India's tiger reserves — the corridors that link isolated protected areas into a functioning metapopulation — are under mounting pressure from roads, agricultural expansion, and settlement growth. India's Forest Survey of India documented 13 major tiger corridors in the 2021 State of Forest Report, ranging from well-forested passages in the Western Ghats to heavily degraded strips in Central India and Rajasthan. The quality of these corridors, and the intensity of human pressure within them, will determine whether the population recovery documented in Phase 1 translates into long-term species survival or remains fragile and geographically isolated.

This project uses GIS to map corridor connectivity and landscape threats across the same seven reserves featured in Phase 1, shifting the analytical focus from inside protected areas to the inter-reserve landscape. The deliverable is a standalone ArcGIS Story Map that links directly to Phase 1, completing a two-part series on India's tiger conservation landscape.

### Statement of Purpose

The purpose of this project is to create an ArcGIS Story Map that examines the connectivity and threat landscape surrounding India's seven featured tiger reserves. Specific objectives include:

1. **Mapping corridor quality** across the 13 ISFR 2021-documented tiger corridors using forest cover classification (Very Dense Forest, Moderately Dense Forest, Open Forest) already extracted in Phase 1
2. **Quantifying human pressure** within and adjacent to corridors using road density, settlement density, and a composite human modification index
3. **Modeling least-cost movement corridors** between reserve pairs using land cover resistance surfaces, terrain data, and road barriers — to be used if authoritative WII corridor boundaries are unavailable
4. **Identifying priority intervention zones** by cross-tabulating corridor ecological quality against threat intensity to produce a 4-class opportunity matrix
5. **Communicating conservation urgency** through a narrative that acknowledges Phase 1 success while highlighting the fragility of connectivity in the inter-reserve landscape

### Study Area and Rationale

The study area is the same seven reserves featured in Phase 1, extended to the inter-reserve landscape within a 50 km buffer of each reserve:

| Reserve | State | Landscape | Phase 1 Growth Category |
|---|---|---|---|
| Bandipur National Park | Karnataka | Western Ghats | High growth |
| Nagarahole National Park | Karnataka | Western Ghats | High growth |
| Kanha National Park | Madhya Pradesh | Central India | Stable (high density) |
| Pench Tiger Reserve (Combined) | MP / Maharashtra | Central India | High growth |
| Ranthambore Tiger Reserve | Rajasthan | Semi-Arid | High growth |
| Kaziranga National Park | Assam | Northeast | Stable (at capacity) |
| Jim Corbett National Park | Uttarakhand | Terai Arc | Moderate growth |

**Why extend to the inter-reserve landscape?** Tiger reserves are not ecological islands. Long-term population viability depends on the ability of individuals — particularly dispersing young males — to move between reserves. Corridors maintain gene flow, allow recolonization after local extinction events, and support the broader metapopulation structure that sustains India's tiger population at the national level. Mapping the quality and threat level of these passages is the logical next step after documenting reserve-level recovery.

**Why the same seven reserves?** Maintaining continuity with Phase 1 allows the two Story Maps to function as a series. Readers of Phase 1 can follow a direct narrative thread: "Here is where tigers recovered — now here is what connects them and what threatens those connections."

---

## Data Discovery

### Primary Data Sources

#### ISFR 2021 Chapter 4 — Tiger Corridor Data *(Already Extracted)*

Tabular forest cover data for 13 tiger corridors, extracted in Phase 1 Week 3. This is the analytical backbone of corridor quality assessment and requires no additional download.

- **Data Type:** VDF / MDF / OF forest cover breakdown per corridor, % of corridor area
- **Source:** Forest Survey of India, *India State of Forest Report 2021*, Chapter 4, Tables 4.9 and 4.10
- **File:** `data/processed/forest/isfr_2021_reserve_corridors.xlsx`
- **Status:** ✅ Already extracted — no additional work required

#### WII Tiger Corridor Spatial Boundaries *(To Be Investigated — Week 1)*

The Wildlife Institute of India maintains spatial boundaries for India's major tiger corridors, which underlie the tabular data in ISFR 2021 Chapter 4. If available, these polygons provide the authoritative corridor extents for spatial analysis.

- **Data Type:** Polygon boundaries for tiger corridors
- **Source:** Wildlife Institute of India / NTCA
- **URLs to check:** https://wii.gov.in / https://ntca.gov.in
- **Alternate:** Supplementary data in peer-reviewed publications (e.g., Jhala et al. corridor studies)
- **Format:** Shapefile or KMZ
- **Status:** ⚠️ Availability unknown — to be investigated in Week 1
- **Contingency:** If unavailable, least-cost path analysis will generate modeled corridor zones (see Methods)

#### ESA WorldCover 2021

High-resolution land cover classification essential for characterizing the non-forest matrix within corridors and constructing the cost surface for connectivity modeling.

- **Data Type:** 11-class land cover raster (forest, cropland, built-up, grassland, shrubland, water, etc.)
- **Source:** European Space Agency / Copernicus Programme
- **Access URL:** https://worldcover2021.esa.int/downloader
- **Resolution:** 10 meters
- **Data Year:** 2021
- **Format:** GeoTIFF (India coverage requires approximately 8–12 tiles)
- **File size:** ~3–6 GB before clipping to study area
- **License:** CC BY 4.0 — attribution required
- **Status:** Available for free download; no account required

**Known limitations:**
- 10m resolution may overestimate forest in areas with scattered trees
- Land cover classes do not distinguish forest quality (dense vs. open) — supplement with ISFR 2021 data for reserve interiors
- 2021 data year; consistent with ISFR 2021 assessment period

#### Global Human Modification Index (Kennedy et al. 2019)

A composite raster quantifying cumulative human pressure at 1 km resolution, combining roads, settlements, agriculture, mining, and energy infrastructure into a single 0–1 index. Used as one component of the composite threat layer.

- **Data Type:** Continuous raster, values 0 (no modification) to 1 (maximum modification)
- **Source:** Kennedy et al. (2019) via figshare
- **Access URL:** https://figshare.com/articles/dataset/Global_Human_Modification/7283087
- **Resolution:** ~1 km
- **Data Year:** 2016 baseline
- **Format:** GeoTIFF
- **File size:** ~200–400 MB for South Asia subset
- **License:** CC BY 4.0
- **Status:** Available for free download; no account required

**Full citation:**
> Kennedy, C.M., Oakleaf, J.R., Theobald, D.M., Baruch-Mordo, S., & Kiesecker, J. (2019). Managing the middle: A shift in conservation priorities based on the global human modification gradient. *Global Change Biology*, 25(3), 811–826. https://doi.org/10.1111/gcb.14549

### Supporting Spatial Data Sources (Reused from Phase 1)

All of the following datasets are already downloaded, processed, and in the project geodatabase. No re-download is required.

| Dataset | Phase 1 Location | Phase 2 Use |
|---|---|---|
| Reserve boundaries | `tiger_project.gdb/Protected_Areas/India_Tiger_Reserves` | Corridor endpoints; zone definitions |
| Reserve buffer 50km | `tiger_project.gdb/Reserve_Buffer_50km` | Analysis extent for all rasters |
| OSM roads (major) | `data/raw/osm/roads_major.shp` | Road density threat layer |
| OSM settlements | `data/raw/osm/settlements.shp` | Settlement density threat layer |
| SRTM DEM (24 tiles) | `data/raw/elevation/srtm_30m_tiles/` | Slope component of cost surface |
| SRTM clipped | `tiger_project.gdb/Environmental_Data/SRTM_India_Clipped` | Ready for cost surface derivation |
| KBA protected areas | `data/raw/wdpa/` | All protected areas context layer |
| Natural Earth admin | `data/raw/administrative/natural_earth/` | Map context |
| DataMeet districts | `data/raw/administrative/districts/2011_Dist.shp` | District-level narrative context |

### Data Availability Assessment

**Confirmed available — no download needed:**
- ✅ ISFR 2021 corridor tabular data (already extracted)
- ✅ OSM roads and settlements (already downloaded)
- ✅ SRTM elevation (already processed)
- ✅ Reserve boundaries and buffer (already in geodatabase)

**Available for download — straightforward:**
- ✅ ESA WorldCover 2021 (free, CC BY 4.0, direct tile download)
- ✅ Global Human Modification Index (free, CC BY 4.0, figshare)

**Availability unknown — investigate Week 1:**
- ⚠️ WII tiger corridor spatial boundaries

**Contingency Plan:**
If WII corridor spatial boundaries are unavailable, least-cost path (LCP) analysis will generate modeled corridor zones between all six reserve pairs using ESA WorldCover as the primary resistance surface. LCP corridors are an established method in conservation biology and will be clearly labeled as modeled estimates in the Story Map narrative. This contingency adds approximately one additional week of analysis time but does not change the analytical scope or Story Map structure.

---

## Methods and Anticipated Results

### Data Preparation and Processing

#### Land Cover Processing

ESA WorldCover 2021 tiles covering India's study area will be mosaicked, reprojected to WGS 1984 UTM Zone 43N (EPSG: 32643), and clipped to the `Reserve_Buffer_50km` extent. Class values will be verified against ESA's published class definitions before use in cost surface construction and landscape composition analysis.

#### Threat Layer Construction

OSM road and settlement layers from Phase 1 will be clipped to the 50 km buffer extent and used as inputs for Kernel Density Estimation (KDE) surfaces, producing continuous road density and settlement density rasters at 1 km resolution. These will be normalized to a 0–1 range and combined with the Human Modification Index raster in a weighted composite threat index.

#### Coordinate Reference System

All analysis performed in WGS 1984 UTM Zone 43N (EPSG: 32643), consistent with Phase 1. All new rasters reprojected to this CRS with cell sizes matched to the coarsest input (1 km for threat index; 10 m for WorldCover where used independently).

### Analysis Methods

#### 1. Corridor Quality Classification

Using the ISFR 2021 tabular data already extracted, corridors will be classified into three quality tiers based on total forest cover as a percentage of corridor area:

- **High quality:** > 60% forest cover
- **Moderate quality:** 40–60% forest cover
- **Low quality:** < 40% forest cover

The VDF / MDF / OF breakdown will also be used to derive a fragmentation indicator — the ratio of Open Forest to total forest cover, where a high OF fraction suggests degraded or edge-dominated forest.

#### 2. Road and Settlement Density Analysis

Kernel Density Estimation applied separately to roads (line features) and settlements (point features) within the 50 km buffer, producing continuous surfaces of human infrastructure pressure. Parameters:

- Road density: search radius 10 km, cell size 1 km, output in km of road per km²
- Settlement density: search radius 15 km, cell size 1 km

#### 3. Composite Threat Index

A weighted combination of three normalized (0–1) input rasters:

| Component | Weight | Rationale |
|---|---|---|
| Road density KDE | 35% | Direct barrier to tiger movement; vehicle mortality risk |
| Settlement density KDE | 30% | Human-tiger conflict risk; habitat avoidance |
| Human Modification Index | 35% | Integrates additional pressures (agriculture, energy) beyond OSM coverage |

Output classified using Natural Breaks (Jenks) into 5 threat levels. Weights and classification will be documented and justified in `docs/phase2-methodology.md`.

#### 4. Least-Cost Path Corridor Modeling *(if WII boundaries unavailable)*

A resistance surface will be constructed from ESA WorldCover (reclassified to movement resistance values), road proximity buffers, and SRTM-derived slope. Cost Distance and Cost Path tools in ArcGIS Pro will generate least-cost movement paths between six reserve pairs. The Corridor tool will generate corridor zones (areas within a specified cost threshold of the least-cost path) representing plausible movement zones rather than single-pixel paths.

Reserve pairs for modeling:

| Pair | Landscape | Known corridor name (ISFR 2021) |
|---|---|---|
| Bandipur — Nagarahole | Western Ghats | Bandipur–Nagarahole corridor |
| Kanha — Pench | Central India | Kanha–Pench corridor |
| Pench — Satpura | Central India | Pench–Satpura corridor (context) |
| Ranthambore — Mukundra | Semi-Arid | Ranthambore–Mukundra corridor |
| Kaziranga — Karbi Anglong | Northeast | Kaziranga–Karbi Anglong corridor |
| Corbett — Rajaji | Terai Arc | Corbett–Rajaji corridor |

#### 5. Corridor Opportunity Analysis

A 4-class matrix cross-tabulating corridor ecological quality (High / Low, derived from ISFR 2021 classification) against threat intensity (High / Low, from composite threat index) to identify priority intervention zones:

| Class | Quality | Threat | Management Implication |
|---|---|---|---|
| Protect | High | Low | Maintain current conditions; prevent encroachment |
| Urgent Action | High | High | High-value corridor under active pressure — priority for intervention |
| Restoration Potential | Low | Low | Degraded but relatively undisturbed — candidate for restoration |
| Buffer / Deprioritize | Low | High | Low ecological value and high pressure — focus resources elsewhere |

#### 6. Reserve-Level Threat Statistics

Zonal Statistics and Summarize Within tools used to calculate per-reserve metrics within the 50 km buffer:

- Mean composite threat score
- Road density (km/km²)
- Settlement count
- % area classified as cropland (from ESA WorldCover)
- % area classified as built-up

### Expected Results and Deliverables

#### Primary Deliverable: ArcGIS Story Map

**Title:** *Under Pressure: The Corridors That Connect India's Tigers*

**Structure:**

1. **Introduction** — Context on connectivity and metapopulation dynamics; explicit link to Phase 1 Story Map; why corridors matter for long-term tiger survival

2. **The Corridor Network** — ISFR 2021 corridor quality classification; map of corridors colored by forest quality tier; which corridors are healthy and which are degraded

3. **The Threat Landscape** — Composite threat index mapped across the inter-reserve landscape; road and settlement density surfaces; narrative on key threat hotspots (e.g., NH44 through Kanha–Pench, highway through Kaziranga)

4. **Connecting the Dots** — Least-cost path corridors or WII boundaries; modeled movement routes between reserves; relationship between LCP alignment and threat exposure

5. **Reserve by Reserve** — Seven reserve profiles focused on threat exposure and corridor quality of adjacent passages

6. **Where to Act** — Opportunity zone map; priority intervention targets identified; conservation framing emphasizing possibility rather than despair

7. **Conclusion & Credits** — Key findings; link back to Phase 1; data sources; methodology note

#### Anticipated Findings

- **Western Ghats (Bandipur–Nagarahole):** Relatively high corridor forest quality; moderate threat from tourism and peripheral roads — likely the most intact corridor in the study
- **Central India (Kanha–Pench):** NH44 (National Highway 44) bisects the primary corridor — expected to show the highest road density threat score of any corridor pair
- **Northeast (Kaziranga):** NH715 (the tea garden highway) is a documented tiger mortality hotspot — should appear as a concentrated high-threat zone in the road density surface
- **Semi-Arid (Ranthambore):** Isolated by agricultural land on most sides; expected high cropland fraction (ESA WorldCover) and moderate-to-high composite threat score
- **Terai Arc (Corbett):** Relatively intact foothills to the east; threat concentrated along the Terai plain to the south where agriculture and settlements are dense

#### Future Expansion Potential (Phase 3)

- Temporal analysis: land cover change in corridors (2000–2021 using Hansen forest loss data)
- Human-wildlife conflict mapping using published incident databases
- Regional deep dives into individual corridor restoration case studies
- Prey species distribution analysis (deer, gaur, elephant) as indirect tiger habitat indicator

---

## Project Timeline

**Pace:** Approximately 2 hours per week, open-ended cadence. Each week is a self-contained unit.

### Phase Timeline

| Week | Milestone | Key Deliverables | Status |
|---|---|---|---|
| **Week 1** | Data acquisition & corridor research | WII corridor decision; new datasets downloaded | ⚪ Not Started |
| **Week 2** | ESA WorldCover & land cover setup | WorldCover mosaicked, clipped, projected; HMI processed | ⚪ Not Started |
| **Week 3** | Road & settlement threat layers | Road KDE, settlement KDE, composite threat index | ⚪ Not Started |
| **Week 4** | Corridor zones & connectivity analysis | WII join OR least-cost paths; corridor quality spatial layer | ⚪ Not Started |
| **Week 5** | Opportunity zone analysis & reserve stats | Opportunity zones raster; Phase2_Reserve_Stats table | ⚪ Not Started |
| **Week 6** | Web map development & symbology | 4+ web maps published to ArcGIS Online | ⚪ Not Started |
| **Week 7** | Story Map narrative & build | Story Map assembled with all content | ⚪ Not Started |
| **Week 8** | Review, polish & publish | Published Story Map; documentation complete | ⚪ Not Started |

---

## Challenges and Limitations

### Anticipated Challenges

- **WII corridor boundaries:** Authoritative spatial corridor polygons may not be publicly downloadable without a formal data request to WII. Least-cost path modeling is a well-established contingency but adds analytical complexity and requires clear caveats in the Story Map narrative.
- **ESA WorldCover tile volume:** Approximately 8–12 tiles are needed for full study area coverage (~3–6 GB before clipping). Download and mosaicking may require multiple sessions within the Week 2 allocation.
- **Cost surface parameterization:** Resistance values assigned to land cover classes (e.g., cropland resistance = 7, built-up = 15) are informed by the literature but involve judgment calls. All parameter choices will be documented and justified.
- **OSM completeness in remote areas:** OSM road coverage is densest near urban and tourist areas. Minor forest tracks and informal roads in reserve interiors may be underrepresented, leading to underestimation of road pressure in remote corridor segments.

### Project Limitations

- **Human Modification Index temporal mismatch:** The Kennedy et al. index uses a 2016 data baseline; ESA WorldCover is 2021. Threat surfaces are not temporally uniform — noted in methodology but not corrected for.
- **Least-cost path as model, not ground truth:** If WII boundaries are unavailable, modeled corridors represent ecologically plausible movement routes, not verified movement paths. Tiger GPS telemetry data (not publicly available) would be needed for validation.
- **District-level population data:** If WorldPop raster is not incorporated, human population pressure is approximated through settlement point density rather than actual population counts — a coarser measure.
- **Static snapshot:** Analysis represents a single time period (approximately 2021). Corridor degradation trends over time are noted as a Phase 3 expansion opportunity.
- **Scope:** Phase 2 focuses on the seven Phase 1 reserves only. India has 53 tiger reserves; this project does not claim national coverage.

### Mitigation Strategies

- Document all parameter choices and their literature basis in `docs/phase2-methodology.md`
- Label least-cost path outputs clearly as modeled estimates in all Story Map text
- Use multiple threat data sources (OSM + Human Modification Index) to partially compensate for OSM incompleteness
- Frame the opportunity zone classification as a screening tool for prioritization, not a prescriptive management plan
- Cross-reference threat findings against published literature on known problem corridors (NH44, NH715) as validation checkpoints

---

## References and Resources

### Primary Literature

Jhala, Y.V., Qureshi, Q., Nayak, A.K., Chauhan, J.S., Sharma, K., Panchal, N., Talukdar, G., Sadhu, A., Dutta, R., Kandwal, R., & Nigam, P. (2023). *All India Tiger Estimation Report 2022*. National Tiger Conservation Authority & Wildlife Institute of India.

Forest Survey of India. (2022). *India State of Forest Report 2021, Chapter 4: Assessment of Forest Cover in Tiger Reserves and Lion Conservation Area of India*. Ministry of Environment, Forest and Climate Change, Government of India.

Kennedy, C.M., Oakleaf, J.R., Theobald, D.M., Baruch-Mordo, S., & Kiesecker, J. (2019). Managing the middle: A shift in conservation priorities based on the global human modification gradient. *Global Change Biology*, 25(3), 811–826. https://doi.org/10.1111/gcb.14549

Zanaga, D., et al. (2022). *ESA WorldCover 10 m 2021 v200*. https://doi.org/10.5281/zenodo.7254221

### Connectivity Literature (Background Reading)

Wikramanayake, E., Dinerstein, E., Seidensticker, J., Lumpkin, S., Pandav, B., Shrestha, M., Mishra, H., Ballou, J., Johnsingh, A.J.T., Chestin, I., Sunarto, S., Christiansen, P., Manandhar, A., Bolze, D., Robinson, J.G., & Lamoreaux, J. (2011). A landscape-based conservation strategy to double the wild tiger population. *Conservation Letters*, 4(3), 219–227.

Gopal, R., Sinha, P.R., & Mathur, V.B. (2010). Conservation of tigers and other wildlife in India with particular reference to tiger reserves. *World Heritage Papers*, 26.

### GIS Resources

Esri. *Cost Distance* tool reference. ArcGIS Pro documentation.
Esri. *Cost Path* tool reference. ArcGIS Pro documentation.
Esri. *Corridor* tool reference. ArcGIS Pro documentation.
Esri. *Kernel Density* tool reference. ArcGIS Pro documentation.

---

## Contact Information

**Project Author:** Kiran Balasubramanian
**Phase 1 Story Map:** https://arcg.is/00bXi44
**GitHub Repository:** https://github.com/K-bsub/tiger-conservation-india
**Date Created:** February 21, 2026
**Last Updated:** February 21, 2026
