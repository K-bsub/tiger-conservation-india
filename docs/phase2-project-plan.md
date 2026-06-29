# Phase 2 Project Plan: Tiger Corridor Connectivity & Threat Mapping in India

**Project Title:** Under Pressure: Mapping the Corridors and Threats That Shape India's Tiger Landscapes (2006–2022)

**Author:** Kiran Balasubramanian
**Phase 1 Story Map:** https://arcg.is/00bXi44
**Start Date:** TBD
**Cadence:** ~2 hours/week (open-ended)
**Last Updated:** February 21, 2026

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Relationship to Phase 1](#2-relationship-to-phase-1)
3. [Research Questions](#3-research-questions)
4. [Study Area](#4-study-area)
5. [Data Sources](#5-data-sources)
6. [Methods](#6-methods)
7. [Story Map Structure](#7-story-map-structure)
8. [Week-by-Week Plan](#8-week-by-week-plan)
9. [Naming Conventions](#9-naming-conventions)
10. [Risk Management](#10-risk-management)
11. [Success Criteria](#11-success-criteria)
12. [Progress Tracking](#12-progress-tracking)

---

## 1. Project Overview

### Purpose

Phase 1 told a story of recovery — tigers returning to reserves that protected them. Phase 2 asks what happens *between* reserves: how tigers move, where movement is blocked, and what human pressures threaten the gains made since 2006.

This project combines **corridor connectivity analysis** with **threat mapping** across the same seven reserves featured in Phase 1, producing a new standalone ArcGIS Story Map that links back to the original.

### Core Argument

Tiger population recovery inside reserves is necessary but not sufficient for long-term species survival. Connectivity between reserves — and the degree of threat in the landscapes between them — determines whether recovered populations can exchange individuals, maintain genetic diversity, and colonize new habitat.

### Deliverable

A published ArcGIS Story Map that:
- Visualizes connectivity corridors between the 7 Phase 1 reserves
- Maps human pressure (roads, settlements, agriculture) across inter-reserve landscapes
- Identifies high-threat and high-opportunity zones within corridors
- Tells a nuanced story: conservation success is real but fragile

---

## 2. Relationship to Phase 1

| Dimension | Phase 1 | Phase 2 |
|---|---|---|
| Focus | Inside reserves | Between reserves |
| Question | Which reserves recovered? | Can recovered populations persist and connect? |
| Primary data | NTCA census, GBIF points | OSM roads/settlements, forest cover, land use |
| Analysis | KDE, Hot Spot (Gi*) | Cost surface, least-cost paths, proximity analysis |
| Tone | Celebratory / success story | Cautionary / conservation urgency |
| Story Map link | Phase 1 published at arcg.is/00bXi44 | Will link back to Phase 1 in introduction |

**Reused data from Phase 1 (no re-download needed):**
- `tiger_project.gdb/Protected_Areas/India_Tiger_Reserves` — reserve boundaries
- `data/raw/osm/roads_major.shp` — road network
- `data/raw/osm/settlements.shp` — settlements
- `data/processed/forest/isfr_2021_reserve_corridors.xlsx` — corridor forest cover (Tables 4.9/4.10)
- `data/raw/wdpa/` — KBA protected area polygons
- `data/raw/administrative/` — Natural Earth boundaries
- `data/raw/elevation/srtm_30m_tiles/` — SRTM DEM (24 tiles)

---

## 3. Research Questions

1. **Connectivity:** Which of the 13 documented tiger corridors (ISFR 2021) retain sufficient forest cover to support tiger movement?
2. **Threat concentration:** Where are roads and settlements most densely concentrated within and adjacent to corridors?
3. **Corridor quality:** What is the relationship between corridor forest cover (already extracted from ISFR 2021 Tables 4.9/4.10) and road/settlement pressure?
4. **Priority zones:** Which corridor segments represent the highest-value intervention targets — high forest quality but elevated threat?

---

## 4. Study Area

**Same 7 reserves as Phase 1**, with analysis extended to the inter-reserve landscape within a **50 km buffer** of each reserve (matching the `Reserve_Buffer_50km` already in the geodatabase).

**13 tiger corridors from ISFR 2021 (already extracted):**

The corridor data from Tables 4.9/4.10 already exists in `data/processed/forest/isfr_2021_reserve_corridors.xlsx`. Spatial corridor boundaries will be obtained from the Wildlife Institute of India corridor dataset or approximated using least-cost path analysis (see Section 6).

**Landscape types represented:**
- Western Ghats (Bandipur–Nagarahole complex)
- Central India (Kanha–Pench)
- Semi-arid (Ranthambore and surrounds)
- Terai Arc (Corbett–Himalayan foothills)
- Northeast (Kaziranga–Karbi Anglong corridor)

---

## 5. Data Sources

### 5.1 Reused from Phase 1 (No Download Required)

| Dataset | Location | Use in Phase 2 |
|---|---|---|
| Reserve boundaries | `tiger_project.gdb/Protected_Areas/` | Zone definitions, corridor endpoints |
| Reserve buffer 50km | `tiger_project.gdb/` | Analysis extent |
| OSM roads | `data/raw/osm/roads_major.shp` | Threat layer — road density |
| OSM settlements | `data/raw/osm/settlements.shp` | Threat layer — settlement pressure |
| SRTM DEM | `data/raw/elevation/srtm_30m_tiles/` | Cost surface terrain component |
| ISFR 2021 corridor data | `data/processed/forest/isfr_2021_reserve_corridors.xlsx` | Corridor quality tabular values |
| GBIF tiger points | `tiger_project.gdb/Tiger_Occurrences/` | Occurrence context layer |
| Natural Earth admin | `data/raw/administrative/natural_earth/` | Map context |
| KBA polygons | `data/raw/wdpa/` | All protected area context |

### 5.2 New Data to Acquire

#### A. WII Tiger Corridor Spatial Boundaries *(Priority — Week 1)*

The Wildlife Institute of India has published spatial corridor boundaries for major Indian tiger landscapes. These are the authoritative corridor extents referenced in ISFR 2021 Chapter 4.

- **Source:** Wildlife Institute of India / NTCA
- **URL to check:** https://wii.gov.in / https://ntca.gov.in
- **Alternate source:** Published in peer-reviewed literature (e.g., Jhala et al. 2020 — corridor maps in supplementary data)
- **Format:** Shapefile or KMZ
- **Contingency:** If unavailable, generate approximate corridor zones using least-cost path analysis between reserve centroids (see Section 6.3)

#### B. Global Human Footprint / Human Pressure Index *(Week 1–2)*

A raster layer quantifying cumulative human pressure at fine spatial resolution — combines roads, settlements, agriculture, and population density into a single composite index.

- **Source Option 1:** Wildlife Conservation Society — Human Footprint 2009
  - URL: https://wcshumanfootprint.org/
  - Resolution: ~1 km
  - License: Free for non-commercial use
- **Source Option 2:** Global Human Modification Index (Kennedy et al. 2019)
  - URL: https://figshare.com/articles/dataset/Global_Human_Modification/7283087
  - Resolution: 1 km
  - License: CC BY 4.0
  - **Preferred** — more recent (2016 data), cleaner methodology
- **Format:** GeoTIFF
- **File size:** ~200–400 MB for South Asia subset

#### C. ESA WorldCover 2021 — Land Use / Land Cover *(Week 2)*

High-resolution (10 m) land cover classification for the inter-reserve landscape, distinguishing cropland, built-up, grassland, shrubland, and forest — critical for identifying non-forest matrix quality within corridors.

- **Source:** European Space Agency via Copernicus
- **URL:** https://viewer.esa-worldcover.org/worldcover/
- **Download:** https://worldcover2021.esa.int/downloader
- **Resolution:** 10 meters
- **Data year:** 2021
- **Format:** GeoTIFF (download by tile; India requires ~8–12 tiles)
- **License:** CC BY 4.0
- **File size:** ~3–6 GB for study area tiles (clip after download)

**Note:** ESA WorldCover is significantly higher resolution than the Global Forest Watch layer already in the project (30m, tree cover only vs. 10m, full land cover classes). It will replace GFW as the primary land cover layer for Phase 2.

#### D. India Population Density *(Week 2 — optional)*

District or sub-district population density for human pressure context narrative.

- **Source:** Census of India 2011 via DataMeet (already have district boundaries)
- **URL:** https://censusindia.gov.in or via open data portals
- **Alternate:** WorldPop India 2020 raster — https://www.worldpop.org/
  - Resolution: 100m
  - License: CC BY 4.0
  - More spatially precise than district-level census aggregates

---

## 6. Methods

### 6.1 Corridor Forest Quality Assessment (Tabular — Already Partially Complete)

**Tool:** Excel / ArcGIS table join  
**Input:** `data/processed/forest/isfr_2021_reserve_corridors.xlsx` (Tables 4.9/4.10, already extracted)

The tabular corridor data from Phase 1 Week 3 already contains VDF/MDF/OF breakdown and total forest cover percentage for 13 corridors. This will be the analytical backbone of corridor quality assessment.

**Steps:**
- Classify corridors into quality tiers: High (>60% forest), Moderate (40–60%), Low (<40%)
- Calculate open/degraded forest fraction as a fragmentation indicator
- Join to spatial corridor boundaries when acquired (Section 5.2A)

**Output:** `data/processed/corridors/corridor_quality_classification.xlsx`

### 6.2 Road and Settlement Density Analysis

**Tool:** ArcGIS Pro — Kernel Density (Spatial Analyst)  
**Inputs:** `roads_major.shp`, `settlements.shp`  
**Extent:** `Reserve_Buffer_50km`

**Road density surface:**
- Input: Road polylines clipped to 50km buffer
- Cell size: 1 km
- Search radius: 10 km
- Output: `Threat_RoadDensity_KDE` (km of road per km²)

**Settlement density surface:**
- Input: Settlement points clipped to 50km buffer
- Cell size: 1 km
- Search radius: 15 km
- Output: `Threat_SettlementDensity_KDE`

### 6.3 Least-Cost Path Analysis (Connectivity Corridors)

**Tool:** ArcGIS Pro — Cost Distance / Least-Cost Path (Spatial Analyst)  
**Use this if WII corridor spatial data is unavailable**

This method generates modeled movement corridors between reserve pairs based on a cost surface that penalizes non-forest land cover, steep slopes, roads, and settlements.

**Cost surface construction:**
- Base: ESA WorldCover 2021 — reclassify land cover to resistance values:
  - Forest (class 10): resistance = 1 (lowest cost)
  - Shrubland/grassland (class 20/30): resistance = 3
  - Cropland (class 40): resistance = 7
  - Built-up (class 50): resistance = 15
  - Water (class 80): resistance = 20 (barrier)
- Add road proximity penalty: buffer roads 500m → add +5 to cost surface within buffer
- Add elevation factor: slope raster from SRTM → reclassify steep slopes (>30°) to add +3

**Corridor pairs to model (connecting Phase 1 reserves):**

| Source Reserve | Target Reserve | Landscape | Priority |
|---|---|---|---|
| Bandipur | Nagarahole | Western Ghats | High |
| Kanha | Pench | Central India | High |
| Pench | Satpura (context) | Central India | Medium |
| Ranthambore | Mukundra (context) | Semi-Arid | Medium |
| Kaziranga | Karbi Anglong | Northeast | High |
| Corbett | Rajaji | Terai Arc | Medium |

**Steps per corridor pair:**
1. **Cost Distance** — from source reserve boundary → cost distance raster
2. **Cost Path** — from target reserve boundary back through cost distance → least-cost path line
3. **Corridor tool** — identify corridor zone using two cost distance surfaces (both directions) → corridor raster showing movement probability

**Output feature classes** (in `Analysis_Results/Connectivity/`):
- `LCP_[Source]_[Target]` — least-cost path polyline
- `Corridor_[Source]_[Target]` — corridor zone raster

### 6.4 Composite Threat Index

**Tool:** ArcGIS Pro — Raster Calculator (Spatial Analyst)  
**Purpose:** Combine road density, settlement density, and human footprint into a single threat score for each corridor zone

**Formula:**
```
Threat_Composite = (RoadDensity_Normalized × 0.35) +
                   (SettlementDensity_Normalized × 0.30) +
                   (HumanFootprint_Normalized × 0.35)
```

- All inputs normalized to 0–1 range using Min-Max scaling before combination
- Weights are illustrative — document chosen weights and justification
- Output classified into 5 threat levels using Natural Breaks (Jenks)

**Output:** `Threat_Composite_Index` raster, classified to 5 levels

### 6.5 Corridor Opportunity Analysis

**Tool:** ArcGIS Pro — Raster Calculator  
**Purpose:** Identify "high-value intervention zones" — areas of high ecological quality but elevated threat

**Logic:**
- High-opportunity zones = High forest quality (low cost) + High threat (high composite threat score)
- Matrix: cross-tabulate forest quality vs. threat level to identify priority zones

**Output:** `Corridor_Opportunity_Zones` raster — 4-class matrix:
- High quality / Low threat (protect and maintain)
- High quality / High threat (urgent intervention)
- Low quality / Low threat (restoration potential)
- Low quality / High threat (de-prioritize or buffer)

### 6.6 Reserve-Level Summary Statistics

**Tool:** ArcGIS Pro — Zonal Statistics / Summarize Within  
**Purpose:** Quantify threat exposure per reserve and per corridor

**Metrics per reserve:**
- Mean composite threat score within 50km buffer
- Road density (km/km²) within 50km buffer
- Settlement count within 50km buffer
- % of buffer area classified as cropland (from ESA WorldCover)

**Metrics per corridor:**
- Mean composite threat score within corridor zone
- % area classified as high-threat (top 2 Jenks classes)
- Forest cover % (from ISFR 2021 tabular data — already extracted)
- Corridor quality tier (from Section 6.1)

---

## 7. Story Map Structure

**Title:** *Under Pressure: The Corridors That Connect India's Tigers*

**Tone:** Informed urgency — acknowledging Phase 1 success while introducing the connectivity challenge. Not alarmist; evidence-based.

**Link to Phase 1:** Prominent callout in Introduction: *"This is Phase 2 of a two-part series. [Read Phase 1: India's Tiger Conservation Success Stories →]"*

### Sections

| # | Section Title | Content | Key Map / Visual |
|---|---|---|---|
| 1 | Introduction | Context on tiger connectivity; link to Phase 1; why corridors matter | Locator map — all 7 reserves + corridor zones overview |
| 2 | The Corridor Network | What corridors are; the 13 ISFR-documented corridors; forest quality classification | Web Map: corridor boundaries colored by forest quality tier |
| 3 | The Threat Landscape | Road and settlement density across the inter-reserve landscape | Web Map: composite threat index raster over corridor zones |
| 4 | Connecting the Dots | Least-cost path corridors; modeled movement routes between reserves | Web Map: LCP lines over threat surface |
| 5 | Reserve by Reserve | 7 reserve profiles — threat exposure for each + corridor quality of adjacent corridors | Accordion cards or sidecar panel per reserve |
| 6 | Where to Act | Opportunity zone map — high quality / high threat areas as priority intervention targets | Web Map: 4-class opportunity matrix |
| 7 | Conclusion & Credits | Key findings; link back to Phase 1; data sources; methodology link | Summary table — corridor quality vs. threat level |

---

## 8. Week-by-Week Plan

**Pace:** ~2 hours/week. Each week is a self-contained task that can expand or compress. Weeks marked ⭐ are critical path — delays here cascade.

---

### ⭐ Week 1: Data Acquisition & Corridor Research

**Goal:** Identify and download new datasets; determine whether WII corridor spatial data is available

**Tasks:**
- [x] Search WII and NTCA websites for downloadable tiger corridor shapefiles
- [x] Search Google Scholar / ResearchGate for Jhala et al. papers with corridor maps in supplementary data
- [x] Download Global Human Modification Index raster (figshare link in Section 5.2B)
- [x] Begin ESA WorldCover tile downloads (identify required tiles for study area)
- [x] Document all downloads in a Phase 2 `data-sources.md` addition

**Decision point:** If WII corridor boundaries are found → use them as authoritative corridor zones. If not → proceed to least-cost path modeling in Week 4.

**Time estimate:** 2 hours

**Deliverables:**
- ✅ Download status for all new datasets
- ✅ Decision recorded: WII corridors available / not available

---

### ⭐ Week 2: ESA WorldCover Processing & Land Cover Setup

**Goal:** Process ESA WorldCover tiles into a clipped, projected land cover raster for the study area

**Tasks:**
- [x] Finish ESA WorldCover tile downloads (tiles covering India study area)
- [x] Mosaic tiles in ArcGIS Pro → `ESA_WorldCover_India_Mosaic`
- [x] Clip to `Reserve_Buffer_50km` → `ESA_WorldCover_Clipped`
- [x] Reproject to UTM 43N → `ESA_WorldCover_UTM43N`
- [x] Verify class distribution: check pixel counts for forest, cropland, built-up classes
- [x] Process Human Modification Index: clip and reproject to match study area
- [x] Document processing steps in Phase 2 `methodology.md`

**Output feature classes / rasters:**
- `ESA_WorldCover_UTM43N` (10m, UTM 43N)
- `HumanMod_Index_UTM43N` (1km, UTM 43N)

**Time estimate:** 2 hours

---

### Week 3: Road & Settlement Threat Layers

**Goal:** Create road density and settlement density surfaces; begin composite threat layer

**Tasks:**
- [ ] Import and clip `roads_major.shp` to `Reserve_Buffer_50km` → `Roads_StudyArea`
- [ ] Import and clip `settlements.shp` to `Reserve_Buffer_50km` → `Settlements_StudyArea`
- [ ] Run Kernel Density on roads (line KDE, search radius 10km, cell size 1km) → `Threat_RoadDensity_KDE`
- [ ] Run Kernel Density on settlements (point KDE, search radius 15km, cell size 1km) → `Threat_SettlementDensity_KDE`
- [ ] Normalize both rasters to 0–1 range using Raster Calculator
- [ ] Normalize Human Modification Index to 0–1
- [ ] Combine into composite: `Threat_Composite_Index` (weighted sum — see Section 6.4)
- [ ] Classify composite using Natural Breaks (5 classes)

**Output rasters** (in `Analysis_Results/Threats/`):
- `Threat_RoadDensity_KDE`
- `Threat_SettlementDensity_KDE`
- `Threat_Composite_Index`
- `Threat_Composite_Classified`

**Time estimate:** 2 hours

---

### ⭐ Week 4: Corridor Zones & Connectivity Analysis

**Goal:** Either spatially join WII corridors OR run least-cost path analysis to generate modeled corridor zones

**Branch A — If WII corridor boundaries available:**
- [ ] Import and reproject WII corridor polygons → `Corridors_WII_UTM43N`
- [ ] Join tabular ISFR 2021 corridor quality data on corridor name
- [ ] Classify corridors by forest quality tier (High / Moderate / Low)
- [ ] Run Zonal Statistics: mean threat score per corridor zone

**Branch B — If WII corridors NOT available (least-cost path):**
- [ ] Reclassify ESA WorldCover to resistance values (see Section 6.3)
- [ ] Add road proximity penalty raster (buffer roads 500m, add cost)
- [ ] Add slope penalty from SRTM (reclassify slopes >30°)
- [ ] Combine into final cost surface → `Cost_Surface_UTM43N`
- [ ] For each of 6 corridor pairs: run Cost Distance + Cost Path tools
- [ ] Convert LCP rasters to polylines → `LCP_[Source]_[Target]` feature classes
- [ ] Run Corridor tool for each pair → corridor zone rasters

**Output** (regardless of branch):
- Spatial corridor zones with forest quality attributes
- Mean threat score per corridor

**Time estimate:** 2 hours (Branch A) or 3–4 hours over 2 sessions (Branch B)

---

### Week 5: Opportunity Zone Analysis & Reserve Statistics

**Goal:** Generate the opportunity zone classification and compile per-reserve threat statistics

**Tasks:**
- [ ] Cross-tabulate forest quality and threat level → `Corridor_Opportunity_Zones` raster (4-class matrix)
- [ ] Run Zonal Statistics as Table for each reserve: mean threat, road density, settlement count within 50km buffer
- [ ] Calculate % cropland per corridor zone (from ESA WorldCover)
- [ ] Populate `Phase2_Reserve_Stats` table with all metrics
- [ ] Validate results: do high-threat corridors match known problem areas in literature?
- [ ] Document findings and any unexpected results

**Output:**
- `Corridor_Opportunity_Zones` raster
- `Phase2_Reserve_Stats` table (in geodatabase)

**Validation check — known reference points:**
- Kanha–Pench corridor: known pressure from NH44 (National Highway) — should show high road density
- Kaziranga: NH715 (tea garden highway) documented threat — check threat index
- Ranthambore: isolated, surrounded by agricultural land — should show high cropland fraction

**Time estimate:** 2 hours

---

### Week 6: Web Map Development & Symbology

**Goal:** Build all web maps for the Story Map in ArcGIS Online

**Web maps to create:**

| Map | Layers | Key symbology |
|---|---|---|
| WM1 — Corridor Overview | Reserve boundaries, corridor zones colored by quality tier | Green (High) → Yellow (Moderate) → Orange (Low) |
| WM2 — Threat Landscape | Composite threat index raster, roads, settlements | Red sequential ramp (low → high threat) |
| WM3 — Least-Cost Paths | LCP lines, corridor zones, reserve boundaries | Gradient lines colored by corridor quality |
| WM4 — Opportunity Zones | 4-class opportunity matrix, reserve outlines | 2×2 color matrix (quality × threat) |
| Reserve detail maps (7) | Individual reserve + adjacent corridor + threat surface | Consistent with WM2 threat symbology |

**Symbology decisions:**
- Corridor quality: use ColorBrewer **YlOrBr** (yellow → orange → brown) — distinct from Phase 1 greens
- Threat ramp: **OrRd** 5-class sequential (light orange → deep red)
- Opportunity zones:
  - High quality / Low threat: `#2D6A4F` (dark green — protect)
  - High quality / High threat: `#D62828` (red — urgent action)
  - Low quality / Low threat: `#A8DADC` (pale blue — restore)
  - Low quality / High threat: `#6D6875` (muted purple — buffer/deprioritize)
- All colors to be WCAG AA verified before publishing

**Time estimate:** 2 hours

---

### Week 7: Story Map Narrative & Build

**Goal:** Write all narrative text and assemble Story Map in ArcGIS StoryMaps

**Tasks:**
- [ ] Draft narrative outline (section by section)
- [ ] Write Introduction — context on connectivity, link to Phase 1
- [ ] Write Section 2 — corridor network and quality
- [ ] Write Section 3 — threat landscape
- [ ] Write Section 4 — connectivity analysis and LCP interpretation
- [ ] Write Section 5 — 7 reserve profiles (threat exposure focus)
- [ ] Write Section 6 — opportunity zone interpretation
- [ ] Write Conclusion & Credits
- [ ] Assemble Story Map: add maps, text, charts, photos
- [ ] Add Phase 1 link prominently in Introduction and Conclusion

**Narrative sensitivities to manage (informed by Phase 1 experience):**
- Frame threats in terms of landscape pressure, not blame (avoid language that implies agricultural communities are the problem)
- Corridor modeling is approximation — caveat LCP results clearly as modeled estimates
- Human Modification Index is a global composite — note limitations for local decision-making
- Avoid making specific policy recommendations beyond the data

**Time estimate:** 2–3 hours (may extend to Week 8)

---

### Week 8: Review, Polish & Publish

**Goal:** QA, final revisions, publication

**Tasks:**
- [ ] Read Story Map start to finish — check narrative flow and factual accuracy
- [ ] Test all maps on desktop, tablet, mobile
- [ ] Verify all data citations and image attributions
- [ ] Check WCAG color accessibility for all symbology (coblis.com)
- [ ] Confirm Phase 1 link is live and correct
- [ ] Publish Story Map publicly
- [ ] Update GitHub repository with Phase 2 documentation
- [ ] Add Phase 2 link to Phase 1 Story Map credits/conclusion (cross-link)
- [ ] Finalize Phase 2 `methodology.md` and `data-sources.md`
- [ ] Write `final-report-phase2.md`

**Time estimate:** 2 hours

---

## 9. Naming Conventions

Follows Phase 1 conventions (`docs/naming-conventions.md`) with Phase 2 additions:

**New feature dataset:** `tiger_project.gdb/Connectivity/`

| Feature Class | Description |
|---|---|
| `Corridors_WII_UTM43N` | WII official corridor boundaries (if available) |
| `LCP_[Source]_[Target]` | Least-cost path polyline per reserve pair |
| `Corridor_[Source]_[Target]_Zone` | Corridor zone raster |
| `Corridor_Opportunity_Zones` | 4-class quality × threat matrix |

**New feature dataset:** `tiger_project.gdb/Threats/`

| Feature Class | Description |
|---|---|
| `Roads_StudyArea` | OSM roads clipped to Reserve_Buffer_50km |
| `Settlements_StudyArea` | OSM settlements clipped to Reserve_Buffer_50km |
| `Threat_RoadDensity_KDE` | Road KDE surface (km/km²) |
| `Threat_SettlementDensity_KDE` | Settlement KDE surface |
| `Threat_Composite_Index` | Weighted composite threat raster |
| `Threat_Composite_Classified` | Threat index classified to 5 Jenks classes |

**New rasters:**

| Raster | Description |
|---|---|
| `ESA_WorldCover_UTM43N` | Land cover 10m, UTM 43N |
| `HumanMod_Index_UTM43N` | Global Human Modification Index, 1km, UTM 43N |
| `Cost_Surface_UTM43N` | Resistance surface for LCP analysis |

**New tables:**

| Table | Description |
|---|---|
| `Phase2_Reserve_Stats` | Per-reserve threat and corridor metrics |
| `corridor_quality_classification.xlsx` | ISFR 2021 corridor tiers |

---

## 10. Risk Management

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| WII corridor boundaries unavailable | Medium | Medium | Least-cost path analysis as contingency (Section 6.3); modeled corridors are acceptable for Story Map narrative with clear caveats |
| ESA WorldCover download complexity | Medium | Medium | 8–12 tiles required; download over 2 sessions if needed; use GFW tree cover as fallback for forest/non-forest binary |
| LCP analysis slow on local machine | Medium | Low | Clip cost surface to individual corridor extent before running; run one pair at a time |
| Human Modification Index too coarse (1km) | Low | Low | Supplement with road/settlement KDE at 1km — same resolution, same story |
| Phase 1 Story Map link breaks | Low | Low | Use full URL (storymaps.arcgis.com) not short URL in Phase 2 narrative |
| Scope creep into more reserves or new analysis | Medium | Medium | Strictly hold to same 7 reserves; document expansion ideas for Phase 3 |
| 2 hours/week pace too slow for momentum | Medium | Medium | Each week is self-contained — acceptable to skip a week without losing continuity |

---

## 11. Success Criteria

- [ ] Published Phase 2 Story Map accessible via public URL
- [ ] Spatial corridor zones present for all or most of the 13 ISFR-documented corridors
- [ ] Composite threat index mapped across full study area
- [ ] Opportunity zone classification produced and interpretable
- [ ] Phase 1 and Phase 2 cross-linked in both Story Maps
- [ ] All analysis reproducible from documented methodology
- [ ] Corridor quality tiers consistent with ISFR 2021 tabular data already extracted

---

## 12. Progress Tracking

### Weekly Status

**Week 1 Status**
- Date:
- Progress: ✅ Complete
- Completed:
  ✅ Search WII and NTCA websites for downloadable tiger corridor shapefiles
  ✅ Download Global Human Modification Index raster (figshare link in Section 5.2B)
  ✅ Begin ESA WorldCover tile downloads (identify required tiles for study area)
  ✅ Document all downloads in a Phase 2 `data-sources.md` addition
- In Progress:
- Blockers:
- Decision — WII corridors: ✅ Available
  - 764 polylines in KML mix PA boundary lines (named) and corridor centerlines
    (`Name = 'Placemark'`). Selected by attribute to isolate corridors. Manual
    naming applied for all 6 study corridors. LCP modeling not required.
    Jhala et al. supplementary digitization contingency skipped.
- **Next Week Focus:** Complete ESA WorldCover mosaic (verify 14-tile coverage
  against all 6 corridor buffers); clip mosaic to `Reserve_Buffer_50km`;
  reproject ESA WorldCover and gHM to UTM 43N; begin OSM road/settlement
  kernel density surfaces; start composite threat index
- **Notes:**
  - Jhala et al. papers with corridor maps skipped — NTCA KML provides
    authoritative corridor geometry for all 6 study corridors
  - ESA WorldCover original downloader URL (worldcover2021.esa.int/downloader)
    is broken; tiles downloaded successfully via AWS S3 public bucket instead
  - ESA WorldCover tile list revised upward from 9 → 14 tiles after visual QC
    of mosaic against 50km reserve buffers revealed gaps at Kanha east,
    Corbett east, Kaziranga north and west
  - Recommend Clip → Project sequence for ESA WorldCover (not Project → Clip)
    to avoid processing full-India raster at 10m resolution

**Week 2 Status**
- Date: March 2026
- Progress: ✅ Complete
- Completed:
  ✅ Finish ESA WorldCover tile downloads (tiles covering India study area)
  ✅ Mosaic tiles in ArcGIS Pro → `ESA_WorldCover_India_Mosaic`
  ✅ Clip to `Reserve_Buffer_50km` → `ESA_WorldCover_Clipped`
  ✅ Reproject to UTM 43N → `ESA_WorldCover_UTM43N`
  ✅ Verify class distribution: check pixel counts for forest, cropland, built-up classes
  ✅ Process Human Modification Index: clip and reproject to match study area
  ✅ Document processing steps in Phase 2 `methodology.md`
- In Progress:
- Blockers:
- **Next Week Focus:**
  - Import and clip `roads_major.shp` to `Reserve_Buffer_50km` → `Roads_StudyArea`
  - Import and clip `settlements.shp` to `Reserve_Buffer_50km` → `Settlements_StudyArea`
  - Run Kernel Density on roads (line KDE, 10km search radius, 1km cell) → `Threat_RoadDensity_KDE`
  - Run Kernel Density on settlements (point KDE, 15km search radius, 1km cell) → `Threat_SettlementDensity_KDE`
  - Normalize road density, settlement density, and gHM rasters to 0–1
  - Combine into `Threat_Composite_Index` (weighted sum — roads 35%, settlements 30%, gHM 35%)
  - Classify composite using Natural Breaks (5 classes) → `Threat_Composite_Classified`
- **Notes:**
  - ESA WorldCover tile list revised from 9 → 15 tiles after visual QC
    against Reserve_Buffer_50km revealed gaps at Kanha east, Corbett east,
    Kaziranga north and west
  - Original ESA downloader (worldcover2021.esa.int/downloader) broken;
    all tiles downloaded via AWS S3 public bucket instead — identical product
  - Clip → Project sequence used for ESA WorldCover (not Project → Clip)
    to avoid processing full-India 10m raster; documented in
    phase2-methodology.md Decision 2
  - phase2-methodology.md created covering Sections 4.1–4.3 and full
    analysis methods (Sections 5.1–5.5); placeholder rows for class
    distribution table to be filled after Summarize Raster

**Week 3 Status**
- Date:
- Progress: 🟢 In Progress
  🟢 Import and clip `roads_major.shp` to `Reserve_Buffer_50km` → `Roads_StudyArea`
- Completed:
- In Progress:
- Blockers:
- **Next Week Focus:** 
- **Notes:**

*(Repeat template for Weeks 4–8)*

---

### Overall Project Health

**Current Status:** 🟢 In Progress
**Completion:** 14.3%
**Key open decision:** WII corridor boundary availability (determines Week 4 branch)

---

## Appendix: Phase 2 Data Citation Additions

### ESA WorldCover 2021

> Zanaga, D., Van De Kerchove, R., Daems, D., De Keersmaecker, W., Brockmann, C., Kirches, G., Wevers, J., Cartus, O., Santoro, M., Fritz, S., Lesiv, M., Herold, M., Tsendbazar, N.E., Xu, P., Ramoino, F., Arino, O. (2022). *ESA WorldCover 10 m 2021 v200*. https://doi.org/10.5281/zenodo.7254221

### Global Human Modification Index

> Kennedy, C.M., Oakleaf, J.R., Theobald, D.M., Baruch-Mordo, S., & Kiesecker, J. (2019). Managing the middle: A shift in conservation priorities based on the global human modification gradient. *Global Change Biology*, 25(3), 811–826. https://doi.org/10.1111/gcb.14549

### Wildlife Institute of India (Corridor Data — if obtained)

> Wildlife Institute of India. (Year). *Tiger Corridor Boundaries — [specific dataset name]*. Wildlife Institute of India, Dehradun, Uttarakhand. Accessed via [URL or formal data request].

---

*Phase 2 builds on: https://arcg.is/00bXi44*
*GitHub repository: https://github.com/K-bsub/tiger-conservation-india*
*Last Updated: March 22, 2026*
