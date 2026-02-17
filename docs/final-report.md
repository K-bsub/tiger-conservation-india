# Final Report: Identifying Conservation Success Stories
## Spatial Analysis of Tiger Population Recovery in India's Protected Areas (2006–2022)

**Author:** Kiran Balasubramanian  
**Date Completed:** February 16, 2026  
**Course:** GIS Project  
**Repository:** https://github.com/K-bsub/tiger-conservation-india  
**Published Story Map:** https://storymaps.arcgis.com/stories/c9e21879e1b2483e81fc79fd357c59b2  
**Short URL:** https://arcg.is/00bXi44

---

## Table of Contents

1. [Project Summary](#1-project-summary)
2. [Objectives and Outcomes](#2-objectives-and-outcomes)
3. [Data and Methods](#3-data-and-methods)
4. [Key Findings](#4-key-findings)
5. [Deliverables](#5-deliverables)
6. [Challenges and How They Were Resolved](#6-challenges-and-how-they-were-resolved)
7. [Deviations from Original Proposal](#7-deviations-from-original-proposal)
8. [Limitations](#8-limitations)
9. [Lessons Learned](#9-lessons-learned)
10. [Future Work](#10-future-work)
11. [References](#11-references)

---

## 1. Project Summary

This project used GIS to identify and analyze tiger conservation success stories across seven major
protected areas in India between 2006 and 2022. Using NTCA All India Tiger Estimation census data
as the primary population source and GBIF occurrence records as the primary spatial distribution
source, the project produced a published ArcGIS Story Map presenting spatial and temporal patterns
in tiger population recovery.

India's national tiger population grew from approximately 1,411 tigers in 2006 to 3,682 in 2022 —
a 161% increase over 16 years. The seven featured reserves collectively demonstrate that this
recovery is not confined to a single region or habitat type: strong conservation outcomes were
documented across five distinct ecological landscapes, from the semi-arid Aravalli hills of
Rajasthan to the Brahmaputra floodplains of Assam.

The project was completed on schedule across 8 weeks, with all primary and secondary deliverables
produced. The Story Map was published publicly on February 16, 2026.

---

## 2. Objectives and Outcomes

| Objective | Status | Notes |
|---|---|---|
| Map tiger population density changes 2006–2022 | ✅ Complete | KDE baseline and current rasters produced; Swipe block in Story Map |
| Compare population growth rates across reserves | ✅ Complete | Chart 2 (growth ranking bar chart); Section 6 synthesis |
| Analyze spatial distribution patterns | ✅ Complete | Kernel density + hot spot analysis (Getis-Ord Gi*) |
| Examine habitat characteristics of successful reserves | ✅ Complete | ISFR 2021 forest cover, SRTM elevation, reserve area statistics |
| Publish ArcGIS Story Map with 5–7 reserves | ✅ Complete | 7 reserves, published February 16, 2026 |
| Document methodology for reproducibility | ✅ Complete | methodology.md, data-sources.md, proposal.md maintained throughout |

### Success Criteria — All Met

1. ✅ Functional, published Story Map accessible via public URL
2. ✅ 7 tiger reserves mapped with documented conservation success
3. ✅ Population trend data (2006–2022) presented in clear visualizations
4. ✅ Density mapping and hot spot analysis demonstrated
5. ✅ Meaningful insights about characteristics of successful conservation
6. ✅ Compelling, evidence-based conservation narrative
7. ✅ Properly cited data sources and methodology documentation

---

## 3. Data and Methods

### 3.1 Data Sources

| Dataset | Source | Role |
|---|---|---|
| Tiger population (5 census years) | NTCA All India Tiger Estimation Reports 2006–2022 | Primary population data |
| Protected area boundaries | KBA Global Database, BirdLife International (Feb 2026) | Reserve extents |
| Tiger occurrence records | GBIF.org (Feb 2026) — 1,411 records after filtering | Spatial distribution analysis |
| Forest cover (reserve level) | ISFR 2021 Chapter 4, Forest Survey of India | Habitat characterization |
| Elevation | NASA SRTM 1 Arc-Second Global DEM, USGS Earth Explorer (24 tiles) | Terrain characterization |
| Administrative boundaries | Natural Earth (public domain); DataMeet India CC BY 4.0 | Map context |
| Roads and settlements | OpenStreetMap via Geofabrik (ODbL) | Human footprint context |

All data publicly available. Full citations in `docs/data-sources.md`.

### 3.2 Coordinate Reference System

All analysis performed in **WGS 1984 UTM Zone 43N (EPSG: 32643)**. Raw data ingested in
WGS 1984 Geographic (EPSG: 4326) and reprojected prior to analysis.

### 3.3 Analytical Methods

**Kernel Density Estimation (ArcGIS Pro — Spatial Analyst)**
- Input: GBIF occurrence records split into two temporal windows
  - Baseline: 2006–2010 (116 points)
  - Current: 2018–2022 (908 points)
- Search radius: 20km (selected from 10/20/30km tests)
- Cell size: 1km × 1km
- Classification: Natural Breaks (Jenks), 5 classes
- Identical classification breaks applied to both periods via saved .lyrx file to
  ensure visual comparability

**Hot Spot Analysis — Getis-Ord Gi* (ArcGIS Pro — Spatial Statistics)**
- Input: GBIF occurrence records, full dataset 2006–2022 (1,411 points)
- Distance band: 50,000m (selected from Incremental Spatial Autocorrelation peak at 25km)
- Conceptualization: Fixed distance band
- FDR correction: Applied (Benjamini-Hochberg)
- Output: Gi_Bin field with confidence levels ±1/±2/±3

**Reserve-Level Statistics (Summarize Within)**
- Point counts per reserve for baseline and current periods
- Tigers per 100 km² (census and occurrence-based)
- Population growth calculations: absolute change, percent change, AAGR

**Habitat Characterization**
- Forest cover: ISFR 2021 Chapter 4 tabular extraction (VDF/MDF/OF per reserve)
- Elevation: Zonal Statistics as Table on SRTM_India_Clipped

---

## 4. Key Findings

### 4.1 Population Recovery — Seven Featured Reserves

| Reserve | 2006 | 2022 | Change | % Growth | Density (tigers/100 km²) |
|---|---|---|---|---|---|
| Pench TR (Combined) | 33 | 77 | +44 | **+133%** | 4.04 |
| Bandipur NP | 68 | 150 | +82 | **+121%** | 8.41 |
| Nagarahole NP | 78 | 141 | +63 | **+81%** | 12.23 |
| Ranthambore TR | 32 | 57 | +25 | **+78%** | 3.23 |
| Jim Corbett NP | 164 | 260 | +96 | **+58%** | 17.78* |
| Kanha NP | 89 | 105 | +16 | **+18%** | 5.07 |
| Kaziranga NP | 103† | 104 | +1 | n/a | ~8.80 |

*Corbett density figure uses KBA polygon area, which is smaller than legal TR area — likely inflated.  
†Kaziranga 2010 baseline (no 2006 reserve-level data available).

All five growth-ranked reserves exceeded the 50% threshold criterion. Kanha and Kaziranga
were included on stability and density grounds respectively.

### 4.2 Spatial Distribution — KDE and Hot Spot Results

Kernel density analysis confirmed increased detection concentration across the study period,
with the most pronounced shifts at Pench/Kanha (Central India corridor) and Bandipur/Nagarahole
(Western Ghats complex). The current period (2018–2022) shows substantially denser and more
extensive detection clusters at all reserves compared to the baseline.

Hot spot analysis (Getis-Ord Gi*) at a 50km distance band identified statistically significant
clusters (≥95% confidence) centered on Kanha/Pench and Kaziranga. Zero hot spots fell within
strict KBA reserve polygons — confirmed as GBIF observer bias toward roads and park gates at
reserve peripheries, not absence of clustering. The 50km buffer was used as the spatial filter
throughout to account for this pattern.

### 4.3 Ranthambore — Unexpected Observer Bias Finding

Ranthambore showed a Cold Spot cluster in the Gi* output despite strong population recovery
(+78%). This apparent contradiction was traced to GBIF observer concentration near the
Ranthambore fort and tourist zones on the reserve's eastern edge — a pedagogically useful
example of the gap between detection density and actual tiger density. This finding was
featured in Section 4 of the Story Map as a teaching moment about GBIF data interpretation.

### 4.4 Habitat Characteristics of Successful Reserves

| Reserve | Forest Cover | Elevation Range | Landscape |
|---|---|---|---|
| Pench | ~89% | 310–627m | Central Indian Sal-Teak |
| Bandipur | 84% | 384–1,453m | Western Ghats |
| Nagarahole | 84% | 692–965m | Western Ghats |
| Ranthambore | 77% | 214–509m | Semi-Arid Aravalli |
| Corbett | 44%* | 257–1,329m | Himalayan Terai-Bhabar |
| Kanha | 91% | 482–912m | Central Indian Sal-Bamboo |
| Kaziranga | 86% | 40–114m | Brahmaputra Alluvial Floodplain |

*Corbett forest cover anomaly (44%) likely reflects a TR boundary revision between 2011 and
2021 FSI assessments — not actual forest cover at that level.

Forest cover ≥77% in 6 of 7 reserves. Ranthambore's 77% forest cover in a state with
only 4.84% overall forest cover (ISFR 2017) is itself a remarkable conservation outcome.

### 4.5 Finding Not Confirmed: Reserve Size Does Not Predict Success

The original proposal anticipated that larger reserve size would correlate with tiger
population and growth. Bubble chart analysis showed no such relationship. Kanha (2,072 km²,
the largest reserve) achieved only 18% growth. Pench (~1,907 km² combined) achieved the
highest growth at 133%. Kaziranga (1,180 km²) holds the highest density despite a flat
population trend. The data suggests management intensity, prey availability, and landscape
connectivity are stronger predictors of conservation success than reserve area alone.

---

## 5. Deliverables

### Primary Deliverable
- ✅ **Published ArcGIS Story Map** — https://arcg.is/00bXi44
  - 7 narrative sections with navigation
  - 9 embedded web maps
  - 4 charts (population trends, growth ranking, density comparison, bubble chart)
  - 24 photos across 8 slideshows
  - Interactive Swipe block (KDE baseline vs. current)
  - Observer bias accordion, methodology and NTCA buttons

### Secondary Deliverables — Project Documentation
- ✅ `docs/proposal.md` — Project proposal with deviations section added
- ✅ `docs/methodology.md` — Full methodology, decisions log, change log
- ✅ `docs/data-sources.md` — Complete data inventory with citations and known issues
- ✅ `docs/final-report.md` — This document
- ✅ `docs/naming-conventions.md` — Feature class and field naming standards
- ✅ `docs/references.md` — Full bibliography

### Tertiary Deliverables — Geodatabase
- ✅ `data/geodatabase/tiger_project.gdb` — Complete project geodatabase including:
  - `Protected_Areas/Tiger_Reserves_Full` — master feature class with all attributes
  - `Tiger_Occurrences/GBIF_Tiger_Points_UTM43N` — full cleaned occurrence dataset
  - `Tiger_Occurrences/GBIF_Tiger_Baseline_2006_2010` — 116 points
  - `Tiger_Occurrences/GBIF_Tiger_Current_2018_2022` — 908 points
  - `Environmental_Data/SRTM_India_Clipped` — elevation raster
  - `Analysis_Results/KDE_Tiger_Baseline_2006_2010.tif`
  - `Analysis_Results/KDE_Tiger_Current_2018_2022.tif`
  - `Analysis_Results/HotSpot_Tiger_GiStar`
  - `Analysis_Results/Reserve_Summary_Stats`
- ✅ `data/processed/tiger_population_2006_2022.xlsx`
- ✅ `data/processed/forest/isfr_2021_reserve_corridors.xlsx`

### Supporting Deliverables
- ✅ GitHub repository — https://github.com/K-bsub/tiger-conservation-india
- ✅ `media/photo-attributions.md` — 24 photos documented with licenses
- ✅ `docs/symbology_scheme.html` — complete symbology reference for all web maps

---

## 6. Challenges and How They Were Resolved

**GBIF baseline record count (18 points at original threshold)**
The proposed coordinate uncertainty filter (<1km) left only 18 baseline records —
insufficient for kernel density estimation. The threshold was relaxed to IS NOT NULL
(any recorded uncertainty), recovering 116 baseline points. The trade-off (positional
imprecision in KDE) was accepted because the analysis operates at reserve scale rather
than sub-reserve precision. Documented as Decision 3 in methodology.md.

**iNaturalist coordinate obscuring (~22km offset)**
iNaturalist automatically offsets threatened species coordinates, making the 722 processed
records unsuitable for any reserve-scale spatial analysis. The dataset was excluded from
all analysis and Story Map content. GBIF alone provided sufficient occurrence data for all
three spatial analyses.

**ArcGIS Online hosted image layer limitation**
The free ArcGIS Online account used for this project does not support publishing raster
layers as hosted image services. KDE rasters could not be published directly to web maps.
Resolved by exporting classified KDE rasters as PNG images, uploading as media layers,
and using the StoryMaps Swipe block to present the comparison — ultimately producing a
more engaging interactive result than the originally planned side-by-side map embed.

**Jim Corbett boundary anomaly**
ISFR 2021 Chapter 4 showed a −594.65 km² forest change for Corbett between 2011 and 2021,
and KBA polygon area is substantially smaller than the legal TR area, inflating the
calculated density figure. Both anomalies were traced to boundary version mismatches between
data sources rather than real-world changes. Corbett was included in the Story Map with
explicit caveats in the stat card and narrative rather than excluded.

**Kaziranga missing 2006 baseline**
No reserve-level NTCA population estimate exists for Kaziranga in 2006 or 2010. Kaziranga
was excluded from percentage growth ranking but included in the analysis on density and
ecological significance grounds (~8.8 tigers/100 km²). Its narrative was reframed around
carrying capacity rather than growth trajectory.

---

## 7. Deviations from Original Proposal

See `docs/proposal.md` — Deviations from Original Proposal section for full detail.
Key deviations in summary:

- Protected area boundaries: WDPA → KBA Global Database (more current, cleaner geometries)
- iNaturalist: excluded from analysis due to ~22km coordinate obscuring
- GBIF threshold: relaxed from <1km to IS NOT NULL (insufficient baseline records otherwise)
- Reserve selection: multi-criterion threshold replacing top-quartile (N=6 too small)
- Forest cover: ISFR 2021 tabular extraction replacing ArcGIS Zonal Statistics (more accurate)
- KDE comparison: Swipe block replacing proposed side-by-side maps (more engaging)
- Story Map: 7 sections vs. 6 proposed chapters (improved narrative flow)
- Reserve size finding: original hypothesis not confirmed by data

---

## 8. Limitations

**GBIF/iNaturalist spatial bias.** Occurrence records concentrate near roads, park gates,
and tourist infrastructure. Kernel density outputs reflect observer effort as much as tiger
distribution. Maps are best interpreted as "detection hotspots" rather than absolute tiger
density surfaces. The Ranthambore Cold Spot result is the most visible expression of this
limitation in the results.

**Census temporal resolution.** NTCA censuses occur every four years. Within-period
dynamics (annual fluctuations, short-term recovery after poaching events) are not captured.
The 2006 and 2022 endpoints used throughout represent snapshots, not continuous monitoring.

**Population estimates, not counts.** All NTCA figures are statistical estimates from
Spatially Explicit Capture-Recapture (SECR) camera trap analysis. Point estimates
(midpoints) are used throughout for comparability; original confidence intervals are
available in the NTCA reports.

**Reserve boundary version mismatch.** KBA boundaries (2025) and ISFR 2021 TR boundaries
(WII digitization) differ in some reserves. Forest cover statistics use ISFR 2021 boundaries;
occurrence density analysis uses KBA boundaries. Corbett is the most affected reserve.

**SRTM vegetation bias.** SRTM radar reflects off tree canopy rather than bare ground in
dense forest. Elevation values in Bandipur, Nagarahole, Kanha, and Corbett represent
canopy height to some degree rather than pure terrain.

**Supplementary source for Bandipur/Nagarahole 2006 and 2010.** Individual reserve-level
NTCA data was not available for these two reserves in 2006 and 2010 census reports.
Values sourced from Singh & Sen (2015), cross-validated against 2014 Karnataka baselines.
Treated as supplementary; not primary.

---

## 9. Lessons Learned

**Source quality beats analytical sophistication.** The single highest-impact data decision
was identifying ISFR 2021 Chapter 4 as a direct tabular source for reserve forest cover —
eliminating the need for Zonal Statistics on a proxy raster and providing more accurate,
authoritative values. Finding the right primary source early saves significant processing
time and improves result quality.

**Small N complicates standard statistical approaches.** With only 6–7 comparable reserves,
standard methods like top-quartile selection yield trivially small outputs. The multi-criterion
threshold approach used here was better suited to the project scale, but this constraint should
be anticipated at the design stage for similar projects.

**GBIF record counts for wildlife are smaller than expected.** After filtering for coordinate
validity, duplicates, and uncertainty, only 116 baseline records remained from 3,488 raw
records — a 96.7% reduction. KDE at reserve scale is feasible with ~100 points but marginal;
future projects should assess filtered record counts before committing to density estimation
as a primary analysis method.

**Platform limitations shape deliverables.** The free ArcGIS Online account limitation on
hosted image layers forced the KDE raster workaround — which ultimately produced a better
Swipe interactive than the originally planned side-by-side static comparison. Constraints
can produce better outcomes when they force creative solutions.

**Documentation throughout is faster than documentation at the end.** Maintaining
methodology.md, the change log, and decision records throughout the 8 weeks meant the
final report and updated proposal were straightforward to write. The alternative —
reconstructing all decisions from memory at project end — would have been significantly
slower and less accurate.

**Political sensitivity in conservation narratives requires early consideration.**
Both the Kanha village relocation and Pench/Kipling issues arose late in the narrative
writing phase. For future public-facing conservation projects, a brief sensitivity review
of all reserve profiles before drafting narrative text would catch these issues earlier
in the writing process.

---

## 10. Future Work

The project was designed as Phase 1 of a modular multi-phase analysis. Possible expansions:

**Phase 2 — Corridor and Connectivity Analysis**
Tiger corridors connecting the seven featured reserves are partially documented in ISFR 2021
Chapter 4 (Tables 4.9/4.10, 13 corridors extracted). A full connectivity analysis using
Circuitscape or ArcGIS Corridor Designer would quantify habitat permeability between reserves
and identify pinch points. The Kanha-Pench corridor is the highest-priority candidate given
the confirmed hot spot cluster spanning both reserves.

**Phase 3 — Threat Assessment and Human-Wildlife Interface**
OSM roads, settlements data, and SRTM elevation are already downloaded and processed.
A proximity analysis (distance to roads, distance to settlements, road density within buffer
zones) would quantify human footprint around each reserve and complement the recovery
narrative with threat context.

**Phase 4 — Temporal Animation**
NTCA census data for all five periods (2006, 2010, 2014, 2018, 2022) is compiled in
`data/processed/tiger_population_2006_2022.xlsx`. An animated choropleth showing the
evolution of growth categories across census years would add a compelling temporal
dimension to the Story Map overview map.

**Data Gap — Annual Monitoring**
NTCA censuses at 4-year intervals are insufficient to capture within-period dynamics.
If annual or biennial camera trap data becomes available through WII or state forest
departments, incorporating it would substantially strengthen temporal analysis.

---

## 11. References

### Tiger Population Data

Jhala, Y.V., Gopal, R., & Qureshi, Q. (Eds.). (2008). *Status of Tigers in India 2006*.
National Tiger Conservation Authority, Government of India, New Delhi & Wildlife Institute
of India, Dehradun.

Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.). (2011). *Status of Tigers, Co-predators and
Prey in India 2010*. National Tiger Conservation Authority, Government of India, New Delhi
& Wildlife Institute of India, Dehradun.

Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.). (2015). *Status of Tigers, Co-predators and
Prey in India 2014*. National Tiger Conservation Authority, Government of India, New Delhi
& Wildlife Institute of India, Dehradun.

Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.). (2019). *Status of Tigers, Co-predators and
Prey in India 2018*. National Tiger Conservation Authority, Government of India, New Delhi
& Wildlife Institute of India, Dehradun.

Jhala, Y.V., Qureshi, Q., Nayak, A.K., et al. (2023). *All India Tiger Estimation Report
2022*. National Tiger Conservation Authority, Ministry of Environment, Forests and Climate
Change, Government of India, New Delhi & Wildlife Institute of India, Dehradun.

Singh, B.V.R., and Sen, A. (2015). Comparative Analysis of Tiger Landscape Complexes and
Reserves in India: An Evaluation of the Tiger Population 2006–2014. *Am Research Thoughts*,
Vol. 1, pp. 1796–1812.

### Spatial and Environmental Data

BirdLife International. (2026). *The World Database of Key Biodiversity Areas* (KBA
Partnership). February 2026 version. http://www.keybiodiversityareas.org/

Forest Survey of India. (2022). *India State of Forest Report 2021, Chapter 4: Assessment
of Forest Cover in Tiger Reserves and Lion Conservation Area of India*. Ministry of
Environment, Forest and Climate Change, Government of India, Dehradun.

Forest Survey of India. (2017). *India State of Forest Report 2017*. Ministry of
Environment, Forest and Climate Change, Government of India, Dehradun.

GBIF.org. (2026). *GBIF Occurrence Download: Panthera tigris in India*. Accessed February
5, 2026. https://www.gbif.org/

Hansen, M.C., Potapov, P.V., Moore, R., et al. (2013). High-resolution global maps of
21st-century forest cover change. *Science*, 342(6160), 850–853.
https://doi.org/10.1126/science.1244693

NASA Shuttle Radar Topography Mission (SRTM). (2013). *Shuttle Radar Topography Mission
(SRTM) Global* [Dataset]. Distributed by OpenTopography.
https://doi.org/10.5069/G9445JDF

Natural Earth. (2024). *1:10m Cultural and Physical Vectors*. https://www.naturalearthdata.com/

DataMeet India Community. (2011). *India District Boundaries* [Dataset]. CC BY 4.0.
https://github.com/datameet/maps

OpenStreetMap contributors. (2026). *OpenStreetMap Data* [Dataset]. Open Database License
(ODbL). Downloaded via Geofabrik: https://download.geofabrik.de/asia/india.html

---

*Document stored in: `docs/final-report.md`*  
*Project repository: https://github.com/K-bsub/tiger-conservation-india*  
*Story Map: https://arcg.is/00bXi44*
