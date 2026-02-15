# Methodology: Tiger Conservation Success Stories in India (2006–2022)

**Project:** Identifying Conservation Success Stories: Spatial Analysis of Tiger Population Recovery  
**Author:** Kiran Balasubramanian  
**Repository:** https://github.com/K-bsub/tiger-conservation-india  
**Last Updated:** February 14, 2026

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Coordinate Reference System](#2-coordinate-reference-system)
3. [Data Sources Summary](#3-data-sources-summary)
4. [Data Processing Log](#4-data-processing-log)
   - 4.1 [Protected Area Boundaries (KBA/WDPA)](#41-protected-area-boundaries-kbawdpa)
   - 4.2 [Tiger Population Data (NTCA)](#42-tiger-population-data-ntca)
   - 4.3 [GBIF Occurrence Records](#43-gbif-occurrence-records)
   - 4.4 [iNaturalist Occurrence Records](#44-inaturalist-occurrence-records)
   - 4.5 [Forest Cover Data (ISFR 2021 & 2017)](#45-forest-cover-data-isfr-2021--2017)
   - 4.6 [Elevation Data (SRTM)](#46-elevation-data-srtm)
   - 4.7 [Administrative Boundaries](#47-administrative-boundaries)
   - 4.8 [Infrastructure Data (OSM)](#48-infrastructure-data-osm)
5. [Spatial Analysis Methods](#5-spatial-analysis-methods)
   - 5.1 [Population Trend Analysis](#51-population-trend-analysis)
   - 5.2 [Kernel Density Estimation](#52-kernel-density-estimation)
   - 5.3 [Hot Spot Analysis](#53-hot-spot-analysis)
   - 5.4 [Reserve-Level Statistics](#54-reserve-level-statistics)
   - 5.5 [Habitat Characterization](#55-habitat-characterization)
6. [Decisions and Justifications](#6-decisions-and-justifications)
7. [Known Limitations](#7-known-limitations)
8. [Software and Tools](#8-software-and-tools)
9. [Reproducibility](#9-reproducibility)
10. [Change Log](#10-change-log)

---

## 1. Project Overview

This project uses GIS to identify and analyze tiger conservation success stories in India's
protected areas between 2006 and 2022. The primary deliverable is an ArcGIS Story Map
presenting spatial and temporal patterns in tiger population recovery across seven featured
reserves.

**Seven featured reserves:**

| Reserve | State | Landscape |
|---|---|---|
| Bandipur National Park | Karnataka | Western Ghats |
| Nagarahole National Park | Karnataka | Western Ghats |
| Kanha National Park | Madhya Pradesh | Central India |
| Pench Tiger Reserve (Combined) | MP / Maharashtra | Central India |
| Ranthambore Tiger Reserve | Rajasthan | Semi-Arid |
| Kaziranga National Park | Assam | Northeast |
| Jim Corbett National Park | Uttarakhand | Terai Arc |

> Note: Pench is treated as a single combined MP/Maharashtra landscape (Decision 5, Section 6).
> Jim Corbett is included for landscape context; forest boundary data requires
> verification (see Section 6).

---

## 2. Coordinate Reference System

**All analysis performed in:** WGS 1984 UTM Zone 43N (EPSG: 32643)

| Property | Value |
|---|---|
| Projection | Transverse Mercator |
| Central Meridian | 75°E |
| Units | Meters |
| Datum | WGS 1984 |
| Suitable for | Distance and area calculations across India |

**Raw data ingested in:** WGS 1984 Geographic (EPSG: 4326)  
All vector layers reprojected using ArcGIS Pro **Project** tool before analysis.  
All rasters reprojected using **Project Raster** tool with bilinear resampling.

---

## 3. Data Sources Summary

| Dataset | Source | Role | Status |
|---|---|---|---|
| Protected area boundaries | KBA / UN Biodiversity Lab (2026) | Reserve extents | ✅ Complete |
| Tiger population (NTCA) | NTCA Reports 2006–2022 | Primary population data | ✅ Complete |
| GBIF tiger occurrences | GBIF.org (Feb 2026) | Spatial distribution | ✅ Processed |
| iNaturalist observations | iNaturalist (Feb 2026) | Supplementary distribution | ✅ Processed |
| Forest cover — reserve level | ISFR 2021 Chapter 4 (FSI) | Habitat characterization | ✅ Complete (tabular) |
| Forest cover — landscape context | ISFR 2017 state chapters (FSI) | District-level context | ✅ Complete (tabular) |
| Elevation (SRTM) | USGS Earth Explorer (2000) | Terrain characterization | ✅ Complete (24 tiles) |
| Admin boundaries | Natural Earth (2024) | Map context | ✅ Downloaded |
| Districts | DataMeet India (2011) | Sub-state context | ✅ Downloaded |
| Roads & settlements | OpenStreetMap via Geofabrik (2026) | Human footprint context | ✅ Downloaded |

Full citations in `docs/data-sources.md`.

---

## 4. Data Processing Log

### 4.1 Protected Area Boundaries (KBA/WDPA)

**Date processed:** February 6, 2026  
**Input file:** `data/raw/wdpa/KBA_Data/KBAsGlobal_2025_September_02/KBAsGlobal_2025_September_02_POL.shp`  
**Output:** `tiger_project.gdb/Protected_Areas/India_Tiger_Reserves`

**Steps:**
1. Downloaded 3 WDPA polygon shapefiles (shp_0, shp_1, shp_2) from KBA portal
2. Merged all 3 into `india_protected_areas_merged` using **Merge** tool
3. Ran **Delete Identical** on `WDPAID` field to remove duplicate polygons
4. Filtered to tiger reserves and national parks using **Select by Attributes:**
   ```sql
   DESIG_ENG = 'National Park'
   OR DESIG_ENG = 'Tiger Reserve'
   OR DESIG_ENG = 'Wildlife Sanctuary'
   ```
5. Manually verified all 7 featured reserves present
6. Exported selection to geodatabase feature class
7. Reprojected from WGS 1984 → UTM 43N using **Project** tool

**Record counts:**
- Final exported features: 620

**Decision:**
Pench Tiger Reserve — combined landscape approach
Date: February 13, 2026
Decision: Pench treated as a single combined landscape (MP + Maharashtra)
rather than split by state.
Justification: NTCA census reports do not provide consistent state-level
splits for Pench across all five census years (2006–2022). Population figures
reflect the full trans-boundary landscape survey area. Splitting would require
proportional allocation not supported by source data.
Spatial treatment: MP and MH KBA polygons dissolved into a single feature
(Pench Tiger Reserve Combined, Reserve_ID = 4).
Impact: Project now has 7 reserves (not 8) as distinct spatial units.

**Known issues:**
- KBA boundaries are approximate — not legal boundaries
- Name variations exist between KBA and NTCA naming conventions
- Standardized name field `Reserve_Name_Std` created for joins (see Section 4.2)

---

### 4.2 Tiger Population Data (NTCA)

**Date processed:** February 8–10, 2026  
**Input files:** `data/raw/ntca/Tiger_Status_2006.pdf` through `Tiger_Status_2022.pdf`  
**Output:** `data/processed/tiger_population_2006_2022.xlsx`

**Extraction method:** Manual extraction from PDF tables (census chapters)

**Data structure (wide format):**

| Field | Description |
|---|---|
| `Reserve_Name` | Official NTCA reserve name |
| `Reserve_Name_Std` | Standardized name (for spatial joins) |
| `State` | Indian state |
| `Pop_2006` | Population estimate, 2006 census |
| `Pop_2010` | Population estimate, 2010 census |
| `Pop_2014` | Population estimate, 2014 census |
| `Pop_2018` | Population estimate, 2018 census |
| `Pop_2022` | Population estimate, 2022 census |
| `Abs_Change` | 2022 minus 2006 (absolute) |
| `Pct_Change` | Percent change 2006→2022 |
| `AAGR` | Average annual growth rate |

**Supplementary source:**  
Bandipur and Nagarahole 2006 and 2010 values not available at individual reserve level
in NTCA reports. Supplemented from Singh & Sen (2015), cross-validated against 2014
Karnataka baselines. See `docs/data-sources.md` Section 1.2.

**Join verification — Tiger_Reserves_Population**
Completed: February 13, 2026
Join method: Add Join on Reserve_ID (integer), exported as permanent feature class

Results:
  Reserve_ID 1  Bandipur NP          Year_2006: 68   Year_2022: 150  ✅
  Reserve_ID 2  Nagarahole NP        Year_2006: 78   Year_2022: 141  ✅
  Reserve_ID 3  Kanha NP             Year_2006: 89   Year_2022: 105  ✅
  Reserve_ID 4  Pench TR (Combined)  Year_2006: 33   Year_2022: 77   ✅
  Reserve_ID 6  Ranthambore TR       Year_2006: 32   Year_2022: 57   ✅
  Reserve_ID 7  Kaziranga NP         Year_2006: NULL Year_2022: 104  ✅ (NULL expected)
  Reserve_ID 8  Jim Corbett NP       Year_2006: 164  Year_2022: 260  ✅

Missing matches: None
Unmatched spatial features: None
Final feature class: tiger_project.gdb/Protected_Areas/Tiger_Reserves_Population

**Steps — joining to spatial data (Week 4):**
1. Import XLSX table into ArcGIS Pro via **Add Data**
2. Open **Add Join** on `India_Tiger_Reserves` feature class
3. Join field: `Reserve_Name_Std` (both datasets)
4. Validate: all 7 reserves matched; no nulls in population fields
5. Export joined result as `Tiger_Reserves_Population` feature class

---

### 4.3 GBIF Occurrence Records

**Date processed:** February 12, 2026  
**Input file:** `data/raw/gbif/tiger_india_2006_2022_*.csv`  
**Output feature classes** (all in `tiger_project.gdb/Tiger_Occurrences/`):

| Feature Class | CRS | Description |
|---|---|---|
| `GBIF_Tiger_Points_Raw` | WGS84 | Original import, no filtering |
| `GBIF_Tiger_Points_Cleaned` | WGS84 | Filtered and deduplicated |
| `GBIF_Tiger_Points_UTM43N` | UTM 43N | Reprojected — **use for all analysis** |
| `GBIF_Tiger_Baseline_2006_2012` | UTM 43N | Subset for density baseline |
| `GBIF_Tiger_Current_2013_2022` | UTM 43N | Subset for current density |

**Processing steps:**

1. **Import CSV** — Added `tiger_india_2006_2022_*.csv` to map via Catalog pane
2. **Display XY Data:**
   - X field: `decimalLongitude`
   - Y field: `decimalLatitude`
   - CRS: WGS 1984 (EPSG:4326)
3. **Filter valid coordinates** — Select by Attributes:
   ```sql
   decimalLatitude IS NOT NULL
   AND decimalLongitude IS NOT NULL
   AND decimalLatitude <> 0
   AND decimalLongitude <> 0
   AND decimalLatitude BETWEEN 6 AND 38
   AND decimalLongitude BETWEEN 68 AND 98
   ```
4. **Remove duplicates** — Delete Identical on fields:
   `decimalLatitude`, `decimalLongitude`, `eventDate`, `species`
5. **Filter coordinate uncertainty:**
   ```sql
   coordinateUncertaintyInMeters <= [1000 / 5000/ 10000]
   AND coordinateUncertaintyInMeters IS NOT NULL
   ```
   > Decision: Used threshold of 10,000m — see Section 6 for justification.
6. **Export to feature class** — `GBIF_Tiger_Points_Cleaned` (WGS84)
7. **Reproject** — `GBIF_Tiger_Points_UTM43N` (UTM 43N, EPSG:32643)
8. **Create time subsets:**
   - Baseline: `year >= 2006 AND year <= 2010` → `GBIF_Tiger_Baseline_2006_2010`
   - Current: `year >= 2018 AND year <= 2022` → `GBIF_Tiger_Current_2018_2022`

**Record counts:**

| Stage | Count |
|---|---|
| Raw CSV records (2006–2022) | 3488 |
| After coordinate validation | 3474 |
| After duplicate removal | 1628 |
| After uncertainty filter | 1411 |
| Baseline subset (2006–2010) | 116 |
| Current subset (2018–2022) | 908 |

---

### 4.4 iNaturalist Occurrence Records

**Status:** ⬜ Pending — to be completed Week 3

**Input file:** `data/raw/inaturalist/inaturalist_tiger_india_research_2006_2022.csv`  
**Expected output:** `tiger_project.gdb/Tiger_Occurrences/iNat_Tiger_Points_UTM43N`

**Planned steps (mirror GBIF workflow):**
1. Import CSV and Display XY Data
2. Filter valid coordinates (same bounds as GBIF)
3. Verify research-grade only (`quality_grade = 'research'`)
4. Remove duplicates with GBIF using `decimalLatitude`, `decimalLongitude`, `eventDate`
5. Apply coordinate uncertainty filter — same threshold as GBIF decision
6. Export and reproject to UTM 43N

**Record counts:**

| Stage | Count |
|---|---|
| Raw CSV records (2006–2022) | 1037 |
| After coordinate validation | 1037 |
| After uncertainty filter | 722 |
| Final — iNat_Tiger_Points_UTM43N | 722 |

**⚠️ Critical note on iNaturalist coordinates:**  
iNaturalist automatically offsets threatened species coordinates by up to ~22 km (~0.2°).
Tiger point locations from iNaturalist **cannot be used for precise spatial analysis.**
Suitable for: broad distribution patterns, presence/absence at district level, temporal trends.
Not suitable for: density estimation, precise habitat modeling, corridor analysis.

**Decision on combining with GBIF:** 
Keep GBIF and iNaturalist datasets separate.
- GBIF used for: kernel density, hot spot analysis, reserve statistics
- iNaturalist used for: Story Map narrative context layer only
- Rationale: iNaturalist coordinate obscuring (~22 km offset) makes records
  unsuitable for precise spatial analysis. Merging would degrade GBIF
  dataset quality without meaningful analytical benefit.

---

### 4.5 Forest Cover Data (ISFR 2021 & 2017)

**Date processed:** February 12, 2026  
**Output file:** `data/processed/forest/isfr_2021_reserve_corridors.xlsx`  
**Secondary output:** `data/processed/forest/isfr_2017_forest_cover.xlsx`

#### ISFR 2021 — Primary Source (Reserve-Boundary Level)

**Source:** FSI India State of Forest Report 2021, Chapter 4 (Tables 4.5, 4.9, 4.10)  
**Spatial unit:** Digitized Tiger Reserve boundaries (WII, Dehradun) — not administrative proxies  
**Method:** Manual tabular extraction from PDF Chapter 4

**Data extracted:**

| Table | Content | Reserves |
|---|---|---|
| Table 4.5 | VDF / MDF / OF / Total forest, 2011 & 2021, % of TR, change | All 7 (+Jim Corbett) |
| Table 4.9/4.10 | Forest cover in 13 tiger corridors (VDF/MDF/OF) | Corridors relevant to project |

**Key values (2021 assessment):**

| Reserve | TR Area (km²) | Forest 2021 (km²) | % of TR | 2011→2021 Change (km²) |
|---|---|---|---|---|
| Bandipur | 1,784.47 | 1,497.63 | 83.93% | −43.35 |
| Nagarahole | 1,152.74 | 970.71 | 84.21% | −0.70 |
| Kanha | 2,071.51 | 1,886.37 | 91.05% | −7.39 |
| Pench (MP) | 1,168.66 | 1,070.09 | 91.57% | −6.11 |
| Pench (MH) | 738.28 | 625.57 | 84.73% | −5.24 |
| Ranthambore | 1,765.57 | 1,360.30 | 77.05% | +177.20 |
| Kaziranga | 1,180.35 | 1,180.16 | 86.00% | +274.48 |
| Jim Corbett | 1,462.66 | 652.38 | 44.60% | −594.65 ⚠️ |

> ⚠️ Jim Corbett −594.65 km² change almost certainly reflects a TR boundary revision
> between assessments, not actual forest loss. Do not use as forest loss data without
> first verifying against NTCA shapefile boundary versions.

**Join to spatial data (Week 4):**
- Import ISFR 2021 reserve sheet as table
- Join to `India_Tiger_Reserves` on `Reserve_Name_Std`
- Fields to add: `TR_Area_sqkm`, `VDF_2021`, `MDF_2021`, `OF_2021`,
  `Total_Forest_2021`, `Pct_of_TR_2021`, `Forest_Change_sqkm`

**Note — ArcGIS Zonal Statistics:**  
Zonal Statistics on FSI raster is **not required** for this project's tabular analysis.
Reserve-level forest values already obtained from ISFR 2021 Chapter 4 directly.
If a VDF/MDF/OF visualization raster layer is desired for the Story Map, defer to
Week 6 and request FSI raster data from fsi.nic.in at that time (optional).

#### ISFR 2017 — Secondary Source (District-Level Landscape Context)

**Source:** FSI ISFR 2017, state chapters: Karnataka, Madhya Pradesh, Maharashtra,
Rajasthan, Assam, Uttarakhand  
**Spatial unit:** District (administrative proxy — not reserve boundary)  
**Role:** Landscape context for Story Map narrative only; not used for reserve-level analysis

---

### 4.6 Elevation Data (SRTM)

**Status:** ✅ Complete — February 13, 2026

**Input:** `data/raw/elevation/srtm_30m_tiles/*.tif` (24 tiles)  
**Output feature classes** (all in `tiger_project.gdb/Environmental_Data/`):

| Feature Class | CRS | Description |
|---|---|---|
| `SRTM_India_Mosaic` | WGS84 | Raw mosaic of all 24 tiles, 16-bit signed |
| `SRTM_India_UTM43N` | UTM 43N | Reprojected, 30m cell, bilinear — intermediate |
| `SRTM_India_Clipped` | UTM 43N | Final — clipped to Reserve_Buffer_50km |

**Processing steps completed:**
1. **Mosaic to New Raster** — 24 tiles → `SRTM_India_Mosaic` (WGS84, 16-bit signed, 1 band)
2. **Project Raster** → `SRTM_India_UTM43N` (UTM 43N, 30m cell size, bilinear resampling)
3. **Buffer** — `Project_Reserves_Clean` + 50km dissolved → `Reserve_Buffer_50km`
4. **Extract by Mask** → `SRTM_India_Clipped`
5. **NoData verified:** −32768 confirmed in raster properties; statistics minimum > 0m
6. **Coverage verified** visually over all 7 reserves

**Complete tile list (24 tiles):**

| Reserve | Core tiles (original 13) | Buffer tiles (11 added) |
|---|---|---|
| Jim Corbett | N29E078, N29E079, N30E078 | — |
| Kaziranga | N26E093, N26E094 | N26E092, N27E092, N27E093 |
| Bandipur | N11E076, N12E076 | N11E075, N12E075 |
| Nagarahole | N11E076, N12E076 | N11E075, N12E075 |
| Kanha | N22E080, N22E081 | N21E080, N21E081 |
| Pench | N21E079, N21E080 | N21E078, N22E078, N22E079 |
| Ranthambore | N26E076, N26E077 | N25E076 |

**All 24 unique tiles:**
N11E075, N11E076, N12E075, N12E076, N21E078, N21E079, N21E080, N21E081,
N22E078, N22E079, N22E080, N22E081, N25E076, N26E076, N26E077, N26E092,
N26E093, N26E094, N27E092, N27E093, N29E078, N29E079, N30E078

**Note — tile count change:** Initial download was 13 core tiles. Visual QC against
50km buffers revealed 11 additional tiles needed for complete buffer coverage (gaps
visible at west edge of Kaziranga, west edge of Bandipur/Nagarahole, south of
Ranthambore, west/north of Pench, south of Kanha). Downloaded via USGS Earth Explorer.

**Elevation ranges observed:**

| Reserve | Min (m) | Max (m) | Mean (m) | Std (m) |
|---|---|---|---|---|
| Bandipur | 384 | 1453 | 874.7 | 119.2 |
| Nagarahole | 692 | 965 | 810.8 | 48.7 |
| Kanha | 482 | 912 | 698.8 | 103.3 |
| Pench | 310 | 627 | 453.6 | 66.6 |
| Ranthambore | 214 | 509 | 352.4 | 78 |
| Kaziranga | 40 | 114 | 77.8 | 5.4 |
| Jim Corbett | 257 | 1329 | 535.1 | 169..8 |

> Run **Zonal Statistics as Table** on `SRTM_India_Clipped` using `Project_Reserves_Clean`
> as zones to populate the table above (Week 5).

**⚠️ Known limitation:** SRTM radar reflects off tree canopy in dense forest — elevation
values in Bandipur, Nagarahole, Kanha, and Corbett represent canopy height, not bare
ground terrain.

---

### 4.7 Administrative Boundaries

**Status:** ✅ Downloaded — to be imported Week 3

**Files in:** `data/raw/administrative/natural_earth/` and `data/raw/administrative/districts/`

| Layer | File | Use |
|---|---|---|
| India country boundary | `ne_10m_admin_0_countries/` | Clipping mask, national maps |
| State boundaries | `ne_10m_admin_1_states_provinces/` | State-level context |
| District boundaries | `2011_Dist.shp` (DataMeet) | District-level context |
| Populated places | `ne_10m_populated_places/` | Map labeling |
| Rivers | `ne_10m_rivers_lake_centerlines/` | Geographic context |

All will be reprojected to UTM 43N on import.

---

### 4.8 Infrastructure Data (OSM)

**Status:** ✅ Downloaded — to be imported Week 3

**Files extracted from** `data/raw/osm/india-latest-free.shp.zip`:
- `data/raw/osm/roads_major.shp` — motorway, trunk, primary, secondary roads
- `data/raw/osm/settlements.shp` — cities and towns (population > 1,000)

Used for: human disturbance context layers in Story Map; proximity analysis if needed.

---

## 5. Spatial Analysis Methods

> **Status:** Methods defined; execution pending Week 5.  
> Parameters will be recorded here when analysis is run.

---

### 5.1 Population Trend Analysis

**Tool:** Microsoft Excel / Python (no ArcGIS tool required)  
**Input:** `data/processed/tiger_population_2006_2022.xlsx`

**Calculations:**
- Absolute change: `Pop_2022 − Pop_2006`
- Percent change: `((Pop_2022 − Pop_2006) / Pop_2006) × 100`
- Average annual growth rate (AAGR): `((Pop_2022 / Pop_2006)^(1/16) − 1) × 100`
- Tigers per 100 km²: `Population / (TR_Area_sqkm / 100)`
- Rank by percent change

**Output:** Summary table for Story Map; chart data for population trend line graph

---

### 5.2 Kernel Density Estimation

**Tool:** ArcGIS Pro — Kernel Density (Spatial Analyst)  
**Input:** `GBIF_Tiger_Baseline_2006_2012` and `GBIF_Tiger_Current_2013_2022`

**Parameters (to be finalized during analysis — document actual values used):**

| Parameter | Planned Value | Actual Value Used |
|---|---|---|
| Search radius | Test 10 km, 20 km, 30 km | [fill in] |
| Cell size | 1 km (1,000 m) | [fill in] |
| Area units | Square kilometers | Square kilometers |
| Output values | Densities | Densities |
| Population field | None (each point = 1) | — |

**Outputs:**
- `KDE_Tiger_Baseline_2006_2010.tif`
- `KDE_Tiger_Current_2018_2022.tif`

Both saved to `tiger_project.gdb/Analysis_Results/`

**Post-processing:**
- Classify into 5–7 density classes using Natural Breaks (Jenks)
- Use identical classification breaks for both rasters to enable direct comparison
- Export classified versions as image files for Story Map

---

### 5.3 Hot Spot Analysis

**Tool:** ArcGIS Pro — Hot Spot Analysis (Getis-Ord Gi*) (Spatial Statistics)  
**Input:** `GBIF_Tiger_Points_UTM43N` (full dataset)

**Parameters (to be finalized — document actual values used):**

| Parameter | Planned Approach | Actual Value Used |
|---|---|---|
| Distance band | Test Incremental Spatial Autocorrelation first | [fill in] |
| Conceptualization | Fixed distance band | [fill in] |
| Significance level | p < 0.05, p < 0.01, p < 0.001 | — |

**Output:** `HotSpot_Tiger_GiStar` feature class in `Analysis_Results/`

**Interpretation:** Features classified as Hot Spot (99%), Hot Spot (95%), Hot Spot (90%),
Not Significant, Cold Spot (90%), Cold Spot (95%), Cold Spot (99%).

---

### 5.4 Reserve-Level Statistics

**Tool:** ArcGIS Pro — Summarize Within / Spatial Join  
**Inputs:** Tiger_Reserves_Full, GBIF_Tiger_Points_UTM43N, GBIF_Tiger_Baseline_2006_2010, GBIF_Tiger_Current_2018_2022

**Metrics calculated per reserve:**

| Metric | Method |
|---|---|
| Total GBIF occurrence points | Summarize Within |
| Points per 100 km² | Calculate Field: `count / (area_sqkm / 100)` |
| Tigers per 100 km² (census) | Calculate Field: `Pop_2022 / (TR_Area_sqkm / 100)` |
| Population growth rank | Sort + rank by `Pct_Change` |
| Forest cover % | Joined from ISFR 2021 |
| Mean elevation | Zonal Statistics (Week 4) |

---

### 5.5 Habitat Characterization

**Tool:** ArcGIS Pro — Zonal Statistics as Table (Spatial Analyst)  
**Input raster:** `SRTM_India_Clipped`  
**Input zones:** `India_Tiger_Reserves`

**Statistics to extract:** MIN, MAX, MEAN, STD (elevation in meters)

**Forest characterization:** Obtained directly from ISFR 2021 tabular extraction
(Section 4.5) — no raster analysis required for forest type classification.

---

## 6. Decisions and Justifications

This section records analytical decisions that deviate from the original project plan or
involve trade-offs, for transparency and reproducibility.

---

**Decision 1: ISFR 2021 Chapter 4 as primary forest source**  
*Date:* February 12, 2026  
*Decision:* Use ISFR 2021 Chapter 4 (reserve-boundary level) as the primary forest cover
source rather than running ArcGIS Zonal Statistics on FSI rasters.  
*Justification:* ISFR 2021 Chapter 4 provides VDF/MDF/OF values measured directly from
digitized Tiger Reserve boundaries by FSI/WII — these are more accurate than a proxy
zonal statistics approach on publicly available rasters. Tabular extraction is complete
for all 7 reserves.  
*Impact:* ArcGIS Zonal Statistics for forest cover removed from Week 3 scope;
deferred to optional visualization task in Week 6.

---

**Decision 2: Jim Corbett boundary anomaly**  
*Date:* February 12, 2026  
*Decision:* Flag Jim Corbett's −594.65 km² forest change (2011→2021) as a likely
boundary revision; do not use as evidence of forest loss in Story Map narrative.  
*Justification:* A loss of 595 km² of forest (45% of the reserve's 2011 area) in one
decade is not consistent with forest monitoring data from other sources or known
management history of Corbett. Most likely cause is a change in the digitized TR boundary
between 2011 and 2021 FSI assessments.  
*Action required:* Verify against NTCA shapefile boundary versions before Week 5 analysis.

---

**Decision 3: GBIF coordinate uncertainty threshold**  
Date: February 14, 2026
Decision: Accept all records where coordinateUncertaintyInMeters IS NOT NULL
  (i.e. any recorded uncertainty value, no upper limit).
Justification: At a 10,000m threshold only 181 records remained — 18 in the
  baseline period (2006–2010), insufficient for kernel density estimation.
  Relaxing to IS NOT NULL recovers ~1,200–1,400 records. Records with high
  uncertainty (>10km) will produce positional imprecision in KDE outputs but
  will cluster correctly at the reserve level for Summarize Within analysis.
  The 22km iNaturalist coordinate offset means this threshold is consistent
  with the iNaturalist data quality standard already accepted for that layer.
Impact: 40.5% of raw records retained after all filters.
  Baseline (2006–2010): 116 records.
  Current (2018–2022): 908 records.

---

**Decision 4: GBIF temporal subsets — 2006–2012 vs 2013–2022**  
Date: February 14, 2026
Decision: Split occurrence data into 2006–2010 (baseline) and 2018–2022
  (current) windows, aligned with NTCA census periods.
Justification: Census-aligned windows make the Story Map narrative directly
  comparable to NTCA population estimates — "detections near the time of the
  2006/2010 census" vs "detections near the time of the 2018/2022 census."
  The original 2006–2012 / 2013–2022 split (Decision 4, Feb 12) is superseded
  by this revision following the uncertainty filter change.
  2018–2022 window used for current period (not 2013–2022) to avoid blurring
  two census cycles in the "current" layer.
Impact: Replaces GBIF_Tiger_Baseline_2006_2012 and GBIF_Tiger_Current_2013_2022.
  Old layers deleted from GDB.

---

**Decision 5: Featured reserve selection criteria**
Date: February 13, 2026
Method: Multi-criterion threshold applied to 7 candidate reserves

Primary criterion:   Percent population change ≥ 50% (2006–2022 baseline)
Supporting criterion: Population ≥ 50 tigers in 2022

Strict top-quartile not used — with N=6 comparable reserves,
a 75th percentile cutoff yields only 2 reserves (Pench 133%,
Bandipur 121%), insufficient for a 5–7 reserve Story Map.

Final 7 reserves selected:
  Growth category  — Pench, Bandipur, Nagarahole, Ranthambore, Jim Corbett
  Stable/capacity  — Kanha (18% growth, strong absolute population),
                     Kaziranga (stable at carrying capacity, highest
                     density in India ~10 tigers/100km²)

Landscape coverage: Western Ghats (2), Central India (2),
                    Semi-Arid (1), Terai Arc (1), Northeast (1)

Excluded from growth ranking: Kaziranga — different baseline year
  (2010 vs 2006); included on density/stability grounds instead.

---

## 7. Known Limitations

- **GBIF/iNaturalist spatial bias:** Occurrence records are concentrated near roads,
  park gates, and tourist areas. Kernel density outputs reflect observer effort as much
  as tiger distribution. Interpret density maps as "detection hotspots," not absolute
  tiger density.

- **iNaturalist coordinate obscuring:** Threatened species coordinates offset up to
  ~22 km. iNaturalist points cannot be used for precise reserve-level spatial analysis.

- **Census temporal resolution:** NTCA census conducted every 4 years only (2006, 2010,
  2014, 2018, 2022). Changes between years are interpolated; within-period dynamics
  are not captured.

- **SRTM vegetation bias:** Radar signal reflects off canopy in dense forest reserves
  (Bandipur, Nagarahole, Kanha, Corbett). Elevation values in these areas represent
  canopy height, not terrain.

- **ISFR 2021 spatial data unavailable:** Chapter 4 provides statistics only; the
  underlying FSI raster/vector data used to produce Table 4.5 is not publicly available.
  Vector data would require a formal request to FSI, Dehradun.

- **Reserve boundary version mismatch:** KBA boundaries (2025) and ISFR 2021 TR
  boundaries (WII digitization) may differ slightly. All forest cover statistics
  use ISFR 2021 boundaries; occurrence density analysis uses KBA boundaries.

- **Population estimates, not counts:** All NTCA figures are statistical estimates
  (SECR camera-trap method), not exact population counts. Confidence intervals exist
  in original reports but point estimates (midpoints) are used throughout this project
  for comparability.

---

## 8. Software and Tools

| Software | Version | Purpose |
|---|---|---|
| ArcGIS Pro | [fill in] | All GIS processing and analysis |
| ArcGIS Online | — | Web map hosting |
| ArcGIS StoryMaps | — | Story Map publication |
| Microsoft Excel | — | NTCA data extraction; ISFR tabular data |
| Python (optional) | 3.x | Data preprocessing scripts if needed |
| Git / GitHub | — | Version control |

**ArcGIS Extensions used:**
- Spatial Analyst (Kernel Density, Zonal Statistics, Extract by Mask)
- Spatial Statistics (Hot Spot Analysis)
- Data Management Tools (Project, Merge, Delete Identical)

---

## 9. Reproducibility

All data sources are publicly available. To reproduce this analysis from scratch:

1. Download all datasets following instructions in `docs/data-sources.md`
2. Create file geodatabase at `data/geodatabase/tiger_project.gdb`
3. Follow processing steps in Section 4 in order (4.1 → 4.8)
4. Run spatial analyses in Section 5 after Week 4 data prep is complete
5. Population data table: `data/processed/tiger_population_2006_2022.xlsx`
6. Forest data table: `data/processed/forest/isfr_2021_reserve_corridors.xlsx`

**GitHub repository:** https://github.com/K-bsub/tiger-conservation-india  
Large data files (shapefiles, rasters) are not stored in the repository due to size
constraints. See `data/README.md` for download links and instructions.

---

## 10. Change Log

| Date | Section | Change |
|---|---|---|
| 2026-02-06 | 4.1 | Protected area boundaries downloaded and imported |
| 2026-02-08 | 4.2 | NTCA population data extracted for all 5 census years |
| 2026-02-09 | 4.5 | Global Forest Watch tree cover data downloaded |
| 2026-02-09 | 4.6 | SRTM elevation tiles downloaded (19 tiles) |
| 2026-02-10 | 4.7 | Natural Earth admin boundaries downloaded |
| 2026-02-10 | 4.8 | OSM roads and settlements downloaded |
| 2026-02-11 | 4.5 | ISFR 2017 district-level data extracted (6 state chapters) |
| 2026-02-12 | 2 | Coordinate reference system established: UTM 43N |
| 2026-02-12 | 4.5 | ISFR 2021 Chapter 4 extracted — all 7 reserves + 13 corridors |
| 2026-02-12 | 6 | Decision recorded: ISFR 2021 as primary forest source |
| 2026-02-12 | 6 | Decision recorded: Jim Corbett boundary anomaly flagged |
| 2026-02-13 | 4.3 | GBIF occurrence data processed — 181 |
| 2026-02-13 | 4.4 | iNaturalist occurrence data processed — 722 |
| 2026-02-13 | 4.6 | SRTM mosaic complete — 24 tiles (13 original + 11 added after QC) |
| 2026-02-13 | 4.6 | SRTM clipped to Reserve_Buffer_50km — SRTM_India_Clipped complete |
| 2026-02-13 | 3   | SRTM status updated to ✅ Complete (24 tiles) |
| 2026-02-13 | 1   | Pench rows consolidated to single combined landscape entry |

---

*Document maintained in: `docs/methodology.md`*  
*Project repository: https://github.com/K-bsub/tiger-conservation-india*
