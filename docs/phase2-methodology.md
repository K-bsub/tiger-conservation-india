# Methodology: Tiger Corridor Connectivity & Threat Mapping in India

**Project:** Under Pressure: Mapping the Corridors and Threats That Shape India's Tiger Landscapes  
**Author:** Kiran Balasubramanian  
**Repository:** https://github.com/K-bsub/tiger-conservation-india  
**Phase 1 Methodology:** `docs/methodology.md`  
**Last Updated:** March 29, 2026

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Coordinate Reference System](#2-coordinate-reference-system)
3. [Data Sources Summary](#3-data-sources-summary)
4. [Data Processing Log](#4-data-processing-log)
   - 4.1 [NTCA Corridor Spatial Data](#41-ntca-corridor-spatial-data)
   - 4.2 [ESA WorldCover 2021](#42-esa-worldcover-2021)
   - 4.3 [Global Human Modification Index (gHM)](#43-global-human-modification-index-ghm)
   - 4.4 [OSM Roads and Settlements (Reused)](#44-osm-roads-and-settlements-reused)
   - 4.5 [Reserve Boundaries and Buffers (Reused)](#45-reserve-boundaries-and-buffers-reused)
5. [Spatial Analysis Methods](#5-spatial-analysis-methods)
   - 5.1 [Corridor Forest Quality Assessment](#51-corridor-forest-quality-assessment)
   - 5.2 [Road and Settlement Density Surfaces](#52-road-and-settlement-density-surfaces)
   - 5.3 [Composite Threat Index](#53-composite-threat-index)
   - 5.4 [Corridor Zone Statistics](#54-corridor-zone-statistics)
   - 5.5 [Opportunity Zone Classification](#55-opportunity-zone-classification)
6. [Decisions and Justifications](#6-decisions-and-justifications)
7. [Known Limitations](#7-known-limitations)
8. [Software and Tools](#8-software-and-tools)
9. [Reproducibility](#9-reproducibility)
10. [Change Log](#10-change-log)

---

## 1. Project Overview

Phase 2 extends the Phase 1 tiger conservation analysis from within reserves to
the inter-reserve landscape. Using corridor spatial data, land cover, and human
pressure layers, this phase maps the connectivity infrastructure between the seven
Phase 1 reserves and assesses the degree of threat facing each corridor.

**Phase 1 Story Map:** https://arcg.is/00bXi44  
**Phase 1 methodology:** `docs/methodology.md`

**Same seven reserves as Phase 1:**

| Reserve | State | Landscape |
|---|---|---|
| Bandipur National Park | Karnataka | Western Ghats |
| Nagarahole National Park | Karnataka | Western Ghats |
| Kanha National Park | Madhya Pradesh | Central India |
| Pench Tiger Reserve (Combined) | MP / Maharashtra | Central India |
| Ranthambore Tiger Reserve | Rajasthan | Semi-Arid |
| Kaziranga National Park | Assam | Northeast |
| Jim Corbett National Park | Uttarakhand | Terai Arc |

**Six study corridors:**

| Corridor_ID | Corridor_Name | Reserves Connected |
|---|---|---|
| 1 | Corbett–Rajaji | Jim Corbett NP ↔ Rajaji NP |
| 2 | Kaziranga–Karbi Anglong | Kaziranga NP ↔ Karbi Anglong hills |
| 3 | Kanha–Pench | Kanha NP ↔ Pench TR |
| 4 | Kanha/Pench–Satpura | Kanha/Pench ↔ Satpura TR |
| 5 | Ranthambore–Mukundra | Ranthambore TR ↔ Mukundra Hills TR |
| 6 | Bandipur–Nagarahole | Bandipur NP ↔ Nagarahole NP ↔ BRT WLS |

---

## 2. Coordinate Reference System

**All analysis performed in:** WGS 1984 UTM Zone 43N (EPSG: 32643)

Same CRS as Phase 1 — no change. All new rasters and vector layers reprojected
to UTM 43N before analysis.

| Property | Value |
|---|---|
| Projection | Transverse Mercator |
| Central Meridian | 75°E |
| Units | Meters |
| Datum | WGS 1984 |
| Suitable for | Distance and area calculations across India |

**Raw data ingested in:** WGS 1984 Geographic (EPSG: 4326)  
All vector layers reprojected using ArcGIS Pro **Project** tool.  
Categorical rasters (ESA WorldCover) reprojected using **nearest neighbor** resampling.  
Continuous rasters (gHM) reprojected using **bilinear** resampling.

---

## 3. Data Sources Summary

### New datasets (Phase 2 only)

| Dataset | Source | Role | Status |
|---|---|---|---|
| NTCA corridor centerlines | NTCA DSS KML (July 2022) | Corridor spatial zones | ✅ Complete |
| ESA WorldCover 2021 | ESA / AWS S3 (14 tiles) | Land cover — corridor quality & threat | ✅ Complete |
| Global Human Modification Index | Kennedy et al. 2019 / figshare | Composite human pressure | ✅ Complete |

### Reused from Phase 1 (no re-download)

| Dataset | Location | Phase 2 Role |
|---|---|---|
| Reserve boundaries | `tiger_project.gdb/Protected_Areas/India_Tiger_Reserves` | Corridor endpoints, zone definitions |
| Reserve_Buffer_50km | `tiger_project.gdb/Reserve_Buffer_50km` | Analysis extent / clip mask |
| OSM roads | `data/raw/osm/roads_major.shp` | Road density threat surface |
| OSM settlements | `data/raw/osm/settlements.shp` | Settlement density threat surface |
| ISFR 2021 corridor data | `data/processed/forest/isfr_2021_reserve_corridors.xlsx` | Corridor forest quality (tabular) |
| SRTM DEM | `tiger_project.gdb/Environmental_Data/SRTM_India_Clipped` | Optional terrain context |
| Natural Earth admin | `data/raw/administrative/natural_earth/` | Map context |
| GBIF tiger points | `tiger_project.gdb/Tiger_Occurrences/` | Optional occurrence context |

Full citations in `docs/phase2-data-sources-addition.md`.

---

## 4. Data Processing Log

### 4.1 NTCA Corridor Spatial Data

**Date processed:** March 2026  
**Input file:** `data/raw/ntca/PA_TR_Corridor_Final.kml`  
**Output feature classes** (all in `tiger_project.gdb/Connectivity/`):

| Feature Class | CRS | Description |
|---|---|---|
| `NTCA_Corridors_Raw` | WGS 84 | Placemark polylines isolated from KML |
| `NTCA_Corridors_Named` | WGS 84 | Named and attributed per corridor |
| `NTCA_Corridors_Dissolved` | WGS 84 | Dissolved by Corridor_Name |
| `NTCA_Corridors_Buffered_5km` | UTM 43N | 5km buffer zones — use for all analysis |

**Processing steps:**

1. **Convert KML** — ArcGIS Pro **KML To Layer** tool on `PA_TR_Corridor_Final.kml`
   - Output: `PA_TR_Corridor_Final` group layer with `Polylines` and `Polygons` sublayers
2. **Inspect attribute table** — Polylines layer contains 764 features:
   - Named features (e.g., "Khir Ganga", "Malai Mahadeshwara") = PA boundary outlines
   - Unnamed features (`Name = 'Placemark'`) = corridor centerlines
3. **Select corridors** — Select by Attributes on Polylines:
   ```sql
   Name = 'Placemark'
   ```
4. **Export selection** → `NTCA_Corridors_Raw` (WGS 84)
5. **Add fields:**
   - `Corridor_Name` (Text, length 100)
   - `Corridor_ID` (Short Integer)
6. **Assign corridor names** — Select by Location for each corridor using
   `Reserve_Buffer_50km` as reference; manually entered `Corridor_Name` and
   `Corridor_ID` values for all 6 study corridors
7. **Dissolve** by `Corridor_Name` → `NTCA_Corridors_Dissolved` — merges
   fragmented multi-segment corridors into single multi-part polylines per corridor
8. **Buffer** 5,000 m → `NTCA_Corridors_Buffered_5km` (UTM 43N)
   - Dissolve type: All (produces single polygon per corridor)
   - Used as zone polygons for all subsequent zonal statistics and threat analysis

**Feature counts:**

| Stage | Count |
|---|---|
| Raw KML Polylines | 764 |
| After Name = 'Placemark' filter | [fill in after QC] |
| After dissolve (6 corridors) | 6 |
| After 5km buffer | 6 |

**Visual QC:** All 6 corridor geometries confirmed spatially correct by overlay
with `Tiger_Reserves_Full` in ArcGIS Pro Working Map.

**Known issues:**
- Corridor centerlines carry no meaningful name attribute in source KML —
  names assigned manually; assignment based on spatial proximity, not
  authoritative NTCA metadata
- Some corridors encoded as disconnected segments in KML — Dissolve merges
  these but creates multi-part geometries; verify topology after dissolve

---

### 4.2 ESA WorldCover 2021

**Date processed:** March 2026  
**Input files:** `data/raw/esa_worldcover/tiles/ESA_WorldCover_10m_2021_v200_*_Map.tif` (14 tiles)  
**Output feature classes** (all in `tiger_project.gdb/Threats/`):

| Output | CRS | Description |
|---|---|---|
| `ESA_WorldCover_India_Mosaic` | WGS 84 | Raw mosaic of all 14 tiles |
| `ESA_WorldCover_Clipped` | WGS 84 | Clipped to Reserve_Buffer_50km |
| `ESA_WorldCover_UTM43N` | UTM 43N | Final — reprojected, analysis-ready |

**Processing steps:**

1. **Download tiles** — 14 tiles via AWS S3 public bucket
   (`s3://esa-worldcover/`) using direct URL pattern:
   `https://esa-worldcover.s3.amazonaws.com/v200/2021/map/ESA_WorldCover_10m_2021_v200_{TILE}_Map.tif`
   > Note: Original ESA downloader (worldcover2021.esa.int/downloader) was
   > unavailable — AWS S3 used as alternative; identical product.
2. **Mosaic** — **Mosaic to New Raster** tool:
   - Input: all 14 tiles
   - Output: `ESA_WorldCover_India_Mosaic`
   - Pixel type: 8-bit unsigned
   - Number of bands: 1
   - Mosaic operator: First
3. **Visual QC** — Overlaid mosaic with `Reserve_Buffer_50km` in WGS 84;
   identified coverage gaps; tile list revised from 9 → 14 tiles after QC
4. **Clip** — **Extract by Mask** using `Reserve_Buffer_50km` →
   `ESA_WorldCover_Clipped` (WGS 84)
   > Clip before reproject to avoid processing full-India raster at 10m resolution
5. **Reproject** — **Project Raster** tool:
   - Output CRS: UTM 43N (EPSG: 32643)
   - Resampling: **Nearest neighbor** (categorical raster — preserves class values)
   - Cell size: 10 m
   - Output: `ESA_WorldCover_UTM43N`
6. **Verify class distribution** — **Summarize Raster** or attribute table
   of unique values; confirm key classes present across study area

**Tiles downloaded (14):**

| Tile | Coverage | Primary reserves/corridors |
|---|---|---|
| N09E075 | 9–12°N, 75–78°E | Bandipur, Nagarahole south |
| N12E075 | 12–15°N, 75–78°E | Bandipur, Nagarahole north |
| N21E075 | 21–24°N, 75–78°E | Ranthambore west buffer |
| N24E075 | 24–27°N, 75–78°E | Ranthambore, Mukundra corridor |
| N27E075 | 27–30°N, 75–78°E | Corbett west, Ranthambore north buffer |
| N21E078 | 21–24°N, 78–81°E | Kanha, Pench, Kanha–Pench corridor |
| N21E081 | 21–24°N, 81–84°E | Kanha buffer east |
| N24E078 | 24–27°N, 78–81°E | Central India north |
| N24E081 | 24–27°N, 81–84°E | Central India east |
| N27E078 | 27–30°N, 78–81°E | Jim Corbett |
| N27E081 | 27–30°N, 81–84°E | Corbett buffer east |
| N30E075 | 30–33°N, 75–78°E | Rajaji NP (Corbett–Rajaji corridor north end) |
| N30E078 | 30–33°N, 81–84°E | Rajaji NP (Corbett–Rajaji corridor north end) |
| N24E090 | 24–27°N, 90–93°E | Kaziranga buffer west |
| N24E093 | 24–27°N, 93–96°E | Kaziranga, Karbi Anglong corridor |
| N27E093 | 27–30°N, 93–96°E | Kaziranga buffer north |

> Note: Tile list grew from 9 (original estimate) to 14 after visual QC of
> mosaic against Reserve_Buffer_50km revealed gaps at Kanha east, Corbett
> east, and Kaziranga north and west.

**Class distribution verification (fill in after running Summarize Raster):**

| Class | Value | Pixel count | % of study area |
|---|---|---|---|
| Tree cover | 10 | [fill] | [fill] |
| Shrubland | 20 | [fill] | [fill] |
| Grassland | 30 | [fill] | [fill] |
| Cropland | 40 | [fill] | [fill] |
| Built-up | 50 | [fill] | [fill] |
| Bare / sparse vegetation | 60 | [fill] | [fill] |
| Permanent water | 80 | [fill] | [fill] |
| Herbaceous wetland | 90 | [fill] | [fill] |

**Known issues:**
- **Nearest neighbor resampling:** Minor pixel boundary shifts occur during
  reprojection but class values are not interpolated — acceptable for
  categorical analysis
- **Tree cover ≠ forest quality:** Class 10 includes plantations alongside
  natural forest — cannot distinguish without additional data
- **Overall accuracy:** 76.7% (Wageningen University validation) — interpret
  at landscape scale, not individual pixel level

---

### 4.3 Global Human Modification Index (gHM)

**Date processed:** March 2026  
**Input file:** `data/raw/human_modification/gHM.tif`  
**Output** (in `tiger_project.gdb/Threats/`):

| Output | CRS | Description |
|---|---|---|
| `HumanMod_Index_UTM43N` | UTM 43N | Clipped, reprojected, analysis-ready |

**Processing steps:**

1. **Download** — `gHM.tif` from figshare
   (https://figshare.com/articles/dataset/Global_Human_Modification/7283087);
   global GeoTIFF, ~32-bit float, values 0.0–1.0
2. **Verify NoData** — Check raster Properties → Source tab for NoData value;
   confirm valid range is 0.0–1.0 over land; ocean/outside-land areas masked
3. **Clip** — **Extract by Mask** using `Reserve_Buffer_50km` → intermediate
   clipped raster (WGS 84)
4. **Reproject** — **Project Raster** tool:
   - Output CRS: UTM 43N (EPSG: 32643)
   - Resampling: **Bilinear** (continuous index — interpolation appropriate)
   - Cell size: 1,000 m (matches native resolution)
   - Output: `HumanMod_Index_UTM43N`
5. **Verify statistics** — Run **Calculate Statistics**; confirm min ≈ 0,
   max ≤ 1.0 across study area; note mean gHM per corridor as a sanity check

**Expected value ranges by reserve context:**

| Context | Expected gHM | Rationale |
|---|---|---|
| Reserve interiors | 0.0–0.1 | Dense protected forest |
| Reserve buffer zones | 0.1–0.3 | Forest edge, low infrastructure |
| Kanha–Pench corridor | 0.3–0.6 | Agricultural matrix, NH44 pressure |
| Ranthambore surrounds | 0.4–0.7 | Semi-arid agriculture, isolated reserve |
| Kaziranga corridor | 0.4–0.7 | Tea estates, NH715 highway |
| Urban areas (Guwahati, etc.) | 0.7–1.0 | High modification |

**Known issues:**
- **2016 baseline** — does not capture post-2016 infrastructure development
  in India; road expansion and urbanization since 2016 not reflected
- **1 km resolution** — cannot resolve narrow corridor pinch points or
  individual road crossings; supplemented by OSM road KDE at same resolution
- **Bilinear resampling** used correctly for continuous index; contrast with
  ESA WorldCover (nearest neighbor)

---

### 4.4 OSM Roads and Settlements (Reused)

**Status:** ✅ Reused from Phase 1 — no reprocessing required  
**Input files:** `data/raw/osm/roads_major.shp`, `data/raw/osm/settlements.shp`  
**Phase 1 processing:** See `docs/methodology.md` Section 4.8

**Phase 2 additional steps:**
1. **Clip to study area** — Select by Location using `Reserve_Buffer_50km`:
   - Output: `tiger_project.gdb/Threats/Roads_StudyArea`
   - Output: `tiger_project.gdb/Threats/Settlements_StudyArea`
2. **Verify feature counts** after clip — document in Change Log

---

### 4.5 Reserve Boundaries and Buffers (Reused)

**Status:** ✅ Reused from Phase 1 — no reprocessing required

| Layer | Location | Phase 2 Use |
|---|---|---|
| `Tiger_Reserves_Full` | `tiger_project.gdb/Protected_Areas/` | Corridor endpoints; zonal statistics zones |
| `Reserve_Buffer_50km` | `tiger_project.gdb/` | Clip mask for all Phase 2 rasters |
| `Reserve_Buffer_50km_separate` | `tiger_project.gdb/` | Per-reserve threat statistics |

---

## 5. Spatial Analysis Methods

> **Status:** Methods defined. Execution begins Week 3.
> Parameters will be recorded here when analysis is run.

---

### 5.1 Corridor Forest Quality Assessment

**Tool:** Excel / ArcGIS table join (no new spatial analysis required)  
**Input:** `data/processed/forest/isfr_2021_reserve_corridors.xlsx`
(Tables 4.9/4.10 — already extracted in Phase 1 Week 3)

**Classification scheme:**

| Tier | Forest cover threshold | Corridor_Quality field value |
|---|---|---|
| High | ≥ 60% forest cover | `High` |
| Moderate | 30–59% forest cover | `Moderate` |
| Low | < 30% forest cover | `Low` |

**Steps:**
1. Add `Pct_Forest` field to `NTCA_Corridors_Dissolved` from ISFR 2021 tabular data
2. Calculate `Corridor_Quality` field using classification thresholds above
3. Join to `NTCA_Corridors_Buffered_5km` on `Corridor_Name`

**Output:** `NTCA_Corridors_Buffered_5km` with `Corridor_Quality` and
`Pct_Forest` attributes populated

---

### 5.2 Road and Settlement Density Surfaces

**Tool:** ArcGIS Pro — **Kernel Density** (Spatial Analyst)  
**Input:** `Roads_StudyArea` (line KDE), `Settlements_StudyArea` (point KDE)

**Parameters (to be finalized — document actual values used):**

| Parameter | Roads | Settlements |
|---|---|---|
| Search radius | 10,000 m | 15,000 m |
| Cell size | 1,000 m | 1,000 m |
| Area units | Square kilometers | Square kilometers |
| Output values | Densities | Densities |
| Population field | None (each segment = 1) | None (each point = 1) |

**Outputs:**
- `tiger_project.gdb/Threats/Threat_RoadDensity_KDE`
- `tiger_project.gdb/Threats/Threat_SettlementDensity_KDE`

**Note:** Search radius for roads (10 km) set to capture cumulative road
pressure across corridor width; settlement radius (15 km) set wider to
reflect broader zone of human activity influence on tiger movement.

---

### 5.3 Composite Threat Index

**Tool:** ArcGIS Pro — **Raster Calculator** (Spatial Analyst)  
**Inputs:** `Threat_RoadDensity_KDE`, `Threat_SettlementDensity_KDE`,
`HumanMod_Index_UTM43N`

**Workflow:**
1. **Normalize** each input to 0–1 scale using **Raster Calculator:**
   ```
   (Input - Min) / (Max - Min)
   ```
2. **Weighted combination:**
   ```
   (RoadDensity_norm × 0.35) + (SettlementDensity_norm × 0.30) + (gHM_norm × 0.35)
   ```
3. **Classify** output to 5 levels using **Natural Breaks (Jenks)** →
   `Threat_Composite_Classified`

**Weights rationale:**
- Roads (35%): Primary direct threat — vehicle strikes, disturbance, barrier effect
- Settlements (30%): Human-wildlife conflict, encroachment pressure
- gHM (35%): Captures broader landscape modification not in roads/settlements alone
  (agriculture intensity, land fragmentation)

**Outputs:**
- `tiger_project.gdb/Threats/Threat_Composite_Index` — continuous 0–1 surface
- `tiger_project.gdb/Threats/Threat_Composite_Classified` — 5-class Jenks

**Validation:** High-threat zones should align with known pressure points —
NH44 through Kanha–Pench corridor, NH715 at Kaziranga, agricultural
intensification around Ranthambore.

---

### 5.4 Corridor Zone Statistics

**Tool:** ArcGIS Pro — **Zonal Statistics as Table** (Spatial Analyst)  
**Zone layer:** `NTCA_Corridors_Buffered_5km`  
**Value rasters:** `Threat_Composite_Index`, `ESA_WorldCover_UTM43N`,
`HumanMod_Index_UTM43N`

**Metrics per corridor:**

| Metric | Raster input | Statistic | Field name |
|---|---|---|---|
| Mean threat score | Threat_Composite_Index | MEAN | `Mean_Threat` |
| Max threat score | Threat_Composite_Index | MAX | `Max_Threat` |
| Mean gHM | HumanMod_Index_UTM43N | MEAN | `Mean_gHM` |
| % tree cover | ESA_WorldCover_UTM43N | [tabulate areas, class 10] | `Pct_TreeCover` |
| % cropland | ESA_WorldCover_UTM43N | [tabulate areas, class 40] | `Pct_Cropland` |
| % built-up | ESA_WorldCover_UTM43N | [tabulate areas, class 50] | `Pct_BuiltUp` |

**Tool for land cover %:** **Tabulate Area** (Spatial Analyst) —
`NTCA_Corridors_Buffered_5km` as zone, `ESA_WorldCover_UTM43N` as class raster

**Output table:** `tiger_project.gdb/Phase2_Corridor_Stats`

---

### 5.5 Opportunity Zone Classification

**Tool:** ArcGIS Pro — **Raster Calculator**  
**Inputs:** `Threat_Composite_Classified`, `Corridor_Quality` (rasterized
from `NTCA_Corridors_Buffered_5km`)

**4-class matrix:**

| | Low Threat | High Threat |
|---|---|---|
| **High Quality** | 🟢 Protect — priority for maintenance | 🔴 Urgent — high value, high risk |
| **Low Quality** | 🔵 Restore — degraded but recoverable | 🟣 Buffer — low priority |

**Field values:** `Opportunity_Class` = `Protect` / `Urgent` / `Restore` / `Buffer`

**Output:** `tiger_project.gdb/Threats/Corridor_Opportunity_Zones`

---

## 6. Decisions and Justifications

---

**Decision 1: NTCA KML as corridor source (Path A)**  
*Date:* March 2026  
*Decision:* Use NTCA Decision Support System KML (`PA_TR_Corridor_Final`) as
the corridor spatial data source rather than WII shapefiles or least-cost path
modeling.  
*Justification:* KML confirmed to contain corridor centerlines (`Name = 'Placemark'`)
for all 6 study corridors. NTCA DSS data is the authoritative source used for
infrastructure clearance decisions — appropriate authority for a connectivity
analysis project.  
*Impact:* Least-cost path modeling (project plan Branch B) not required. WII
shapefile request and Jhala et al. supplementary digitization both skipped.
Saves approximately 1–2 weeks of analytical effort.

---

**Decision 2: Clip before reproject for ESA WorldCover**  
*Date:* March 2026  
*Decision:* Apply Extract by Mask (clip to `Reserve_Buffer_50km`) before
reprojecting ESA WorldCover, not after.  
*Justification:* Processing a full-India 10m raster through Project Raster
is extremely slow and produces a very large intermediate file. Clipping first
reduces input to study area only before the computationally expensive
reprojection step. Output is identical either way.  
*Impact:* Processing sequence: Mosaic → Clip → Project (not Mosaic → Project → Clip).

---

**Decision 3: 14 tiles for ESA WorldCover (revised from 9)**  
*Date:* March 2026  
*Decision:* Download 14 ESA WorldCover tiles rather than the originally
estimated 9.  
*Justification:* Visual QC of initial 9-tile mosaic against `Reserve_Buffer_50km`
revealed coverage gaps at Kanha east (N21E081), Central India east (N24E081),
Corbett buffer east (N27E081), Kaziranga buffer west (N24E090), and
Kaziranga buffer north (N27E093). All 5 gap tiles added.  
*Impact:* Total file size approximately 40–50% larger than original estimate;
mosaic processing time increased proportionally.

---

**Decision 4: 5 km corridor buffer width**  
*Date:* March 2026  
*Decision:* Buffer NTCA corridor centerlines by 5 km (either side) to create
corridor zone polygons.  
*Justification:* Tiger home ranges average 20–60 km² for females and up to
200 km² for males; a 5 km half-width captures the immediate movement zone
without over-extending into unrelated landscape. Standard practice in Indian
tiger corridor literature (e.g., ISFR 2021 corridor analysis uses similar
zone widths). Narrower buffers (1–2 km) would miss dispersal movement;
wider buffers (10+ km) would overlap reserve boundaries and adjacent corridors.  
*Impact:* Buffer width is an analytical choice, not an authoritative boundary.
Caveat in Story Map narrative accordingly.

---

**Decision 5: Composite threat index weights (35/30/35)**  
*Date:* Pending — to be recorded when analysis is run  
*Decision:* [Document actual weights chosen and justification]  
*Justification:* [Fill in]  
*Impact:* [Fill in]

---

## 7. Known Limitations

- **Corridor geometry type:** NTCA KML provides centerlines, not authoritative
  polygon zones. The 5 km buffer is an analytical approximation — actual
  functional corridor width varies by terrain, land cover, and tiger behavior.

- **ESA WorldCover accuracy:** Overall accuracy of 76.7% means approximately
  1 in 4 pixels may be misclassified. Interpret land cover statistics at
  corridor/landscape scale rather than individual pixel level.

- **gHM data currency:** 2016 baseline — a decade of infrastructure
  development, road expansion, and urbanization in India is not captured.
  Threat index likely underestimates current pressure in rapidly developing
  corridors.

- **NTCA KML currency:** July 2022 — corridor delineations may not reflect
  the most current WII corridor research. Treat as approximate authoritative
  boundaries rather than precise ecological corridor models.

- **OSM road completeness:** OSM coverage is densest in urban and tourist
  areas; minor forest roads and tracks may be missing, potentially
  underestimating road pressure in remote corridor sections.

- **Composite threat index subjectivity:** The 35/30/35 weighting scheme
  reflects a reasonable judgment about relative threat importance but is not
  derived from empirical tiger response data. Alternative weightings would
  produce different threat rankings.

- **Phase 1 boundary reuse:** Phase 2 analysis uses the same KBA boundaries
  as Phase 1 (`Tiger_Reserves_Full`). These are approximate, not legal
  boundaries — see Phase 1 methodology Section 7 for full boundary caveats.

---

## 8. Software and Tools

| Software | Version | Purpose |
|---|---|---|
| ArcGIS Pro | [fill in] | All GIS processing and analysis |
| ArcGIS Online | — | Web map hosting |
| ArcGIS StoryMaps | — | Story Map publication |
| Microsoft Excel | — | ISFR 2021 corridor tabular data |
| Git / GitHub | — | Version control |

**ArcGIS Extensions used:**
- Spatial Analyst (Kernel Density, Zonal Statistics, Extract by Mask,
  Raster Calculator, Tabulate Area)
- Data Management Tools (Mosaic to New Raster, Project Raster, Buffer,
  Dissolve, KML To Layer)

---

## 9. Reproducibility

All data sources are publicly available. To reproduce from scratch:

1. Download NTCA KML from https://ntca.gov.in/dss/ and convert with KML To Layer
2. Download 14 ESA WorldCover tiles via AWS S3 (URLs in `docs/phase2-data-sources-addition.md`)
3. Download gHM from https://figshare.com/articles/dataset/Global_Human_Modification/7283087
4. Reuse Phase 1 geodatabase assets — no re-download of OSM, SRTM, boundaries required
5. Follow processing steps in Section 4 in order (4.1 → 4.5)
6. Run spatial analyses in Section 5 after data prep complete
7. Corridor tabular data: `data/processed/forest/isfr_2021_reserve_corridors.xlsx`

**GitHub repository:** https://github.com/K-bsub/tiger-conservation-india  
Large data files (rasters) are not stored in the repository. See
`docs/phase2-data-sources-addition.md` for download links and instructions.

---

## 10. Change Log

| Date | Section | Change |
|---|---|---|
| March 2026 | 4.1 | NTCA KML downloaded, converted, corridors isolated and named |
| March 2026 | 4.1 | Corridors dissolved and buffered 5km → NTCA_Corridors_Buffered_5km |
| March 2026 | 4.2 | ESA WorldCover tiles downloaded (14 tiles after QC revision) |
| March 2026 | 4.2 | ESA WorldCover mosaicked, clipped, reprojected → ESA_WorldCover_UTM43N |
| March 2026 | 4.3 | gHM downloaded, clipped, reprojected → HumanMod_Index_UTM43N |
| March 2026 | 6 | Decision 1 recorded: NTCA KML as corridor source (Path A) |
| March 2026 | 6 | Decision 2 recorded: Clip before reproject for ESA WorldCover |
| March 2026 | 6 | Decision 3 recorded: 14 tiles revised from 9 |
| March 2026 | 6 | Decision 4 recorded: 5 km corridor buffer width |

---

*Document maintained in: `docs/phase2-methodology.md`*  
*Phase 1 methodology: `docs/methodology.md`*  
*Project repository: https://github.com/K-bsub/tiger-conservation-india*
