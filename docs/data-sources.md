# Data Sources

**Project:** Tiger Conservation Success Stories in India (2006–2022)  
**Repository:** https://github.com/K-bsub/tiger-conservation-india  
**Last Updated:** February 12, 2026  
**Compiled by:** Kiran Balasubramanian

---

## Table of Contents

1. [Tiger Population Data](#1-tiger-population-data)
2. [Protected Area Boundaries](#2-protected-area-boundaries)
3. [Tiger Occurrence Records](#3-tiger-occurrence-records)
4. [Forest Cover Data](#4-forest-cover-data)
5. [Elevation Data](#5-elevation-data)
6. [Administrative Boundaries](#6-administrative-boundaries)
7. [Infrastructure Data](#7-infrastructure-data)
8. [How to Reproduce This Dataset](#8-how-to-reproduce-this-dataset)
9. [License Summary](#9-license-summary)

---

## 1. Tiger Population Data

### 1.1 NTCA All India Tiger Estimation Reports

The primary source for tiger population counts at each featured reserve. Five
census rounds are used in this project, spanning 2006–2022.

#### 2006 Census

**Full Citation:**
> Jhala, Y.V., Gopal, R., & Qureshi, Q. (Eds.). (2008). *Status of Tigers in
> India 2006*. National Tiger Conservation Authority, Government of India,
> New Delhi & Wildlife Institute of India, Dehradun.

- **Access URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/Statusof_Tigers2008.pdf
- **Access Method:** Direct PDF download (no login required)
- **Downloaded:** February 8, 2026
- **National Total:** ~1,411 tigers
- **File:** `data/raw/ntca/Tiger_Status_2006.pdf`

**Known Issues / Limitations:**
- Some reserves reported at landscape level rather than individual reserve level
- Older survey methodology with lower camera trap coverage than later censuses
- Reserve-specific data for Bandipur and Nagarahole not available at individual
  level — supplemented by Singh & Sen (2015); see Section 1.2
- Higher uncertainty in estimates compared to 2014–2022 censuses

---

#### 2010 Census

**Full Citation:**
> Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.). (2011). *Status of Tigers,
> Co-predators and Prey in India 2010*. National Tiger Conservation Authority,
> Government of India, New Delhi & Wildlife Institute of India, Dehradun.

- **Access URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/Statusof_Tigers2010.pdf
- **Access Method:** Direct PDF download (no login required)
- **Downloaded:** February 8, 2026
- **National Total:** 1,706 tigers
- **File:** `data/raw/ntca/Tiger_Status_2010.pdf`
- **Key Pages:** pp. 3, 39, 143

**Known Issues / Limitations:**
- Transition period in methodology — some individual reserve data not published
  separately from landscape totals
- Bandipur and Nagarahole data supplemented from Singh & Sen (2015)

---

#### 2014 Census

**Full Citation:**
> Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.). (2015). *Status of Tigers,
> Co-predators and Prey in India 2014*. National Tiger Conservation Authority,
> Government of India, New Delhi & Wildlife Institute of India, Dehradun.

- **Access URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/AITE_2014_fullreport.pdf
- **Access Method:** Direct PDF download (no login required)
- **Downloaded:** February 8, 2026
- **National Total:** 2,226 tigers
- **File:** `data/raw/ntca/Tiger_Status_2014.pdf`
- **Key Pages:** p. 20

**Known Issues / Limitations:**
- Some reserve boundaries expanded compared to earlier censuses; population
  increases partly reflect expanded survey areas
- Point estimates (midpoints) used for consistency; original reports include
  confidence intervals

---

#### 2018 Census

**Full Citation:**
> Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.). (2019). *Status of Tigers,
> Co-predators and Prey in India 2018*. National Tiger Conservation Authority,
> Government of India, New Delhi & Wildlife Institute of India, Dehradun.

- **Access URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/Tiger_Status_Report_2018.pdf
- **Access Method:** Direct PDF download (no login required)
- **Downloaded:** February 8, 2026
- **National Total:** 2,967 tigers
- **File:** `data/raw/ntca/Tiger_Status_2018.pdf`
- **Key Pages:** pp. 40–41

**Known Issues / Limitations:**
- Point estimates used; original confidence intervals available in report

---

#### 2022 Census

**Full Citation:**
> Jhala, Y.V., Qureshi, Q., Nayak, A.K., Chauhan, J.S., Sharma, K., Panchal,
> N., Talukdar, G., Sadhu, A., Dutta, R., Kandwal, R., & Nigam, P. (2023).
> *All India Tiger Estimation Report 2022*. National Tiger Conservation
> Authority, Ministry of Environment, Forests and Climate Change, Government
> of India, New Delhi & Wildlife Institute of India, Dehradun.

- **Access URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/status_of_tiger-copredators-2022.pdf
- **Access Method:** Direct PDF download (no login required)
- **Downloaded:** February 8, 2026
- **National Total:** 3,682 tigers
- **File:** `data/raw/ntca/Tiger_Status_2022.pdf`
- **Key Pages:** pp. 20–21

**Known Issues / Limitations:**
- Most recent census; methodology most standardized and comparable across
  reserves
- Point estimates used throughout this project for consistency

---

### 1.2 Supplementary Research Publication

Used to fill data gaps for Bandipur and Nagarahole National Parks for census
years 2006 and 2010, which were not available at individual reserve level in
the NTCA reports.

**Full Citation:**
> Singh, Bhanwar Vishvendra Raj, and Anjan Sen. (2015). "Comparative Analysis
> of Tiger Landscape Complexes and Reserves in India: An Evaluation of the
> Tiger Population 2006–2014." *Am Research Thoughts*, Vol. 1, pp. 1796–1812.

- **Access URL:** https://www.researchgate.net/publication/281864332
- **Access Method:** Free download via ResearchGate (account may be required)
- **Downloaded:** February 8, 2026
- **File:** `data/raw/ntca/` (supplementary reference)

**Known Issues / Limitations:**
- Published in a lower-impact journal (Am Research Thoughts) — treat as
  supplementary, not primary
- Data cross-validated against NTCA 2014 Karnataka baselines and found
  consistent with regional trends
- Used only for 2006 and 2010 Bandipur and Nagarahole estimates where no
  NTCA reserve-level data exists
- Authors affiliated with Mohanlal Sukhadia University and University of Delhi

---

### Methodological Notes (All NTCA Data)

- All population figures are **estimates**, not exact counts, derived from
  camera trap capture-recapture (SECR) analysis
- Point estimates (midpoints) are used throughout this project for consistency;
  original confidence intervals are available in each PDF report
- Reserve boundary expansions between census years mean some apparent
  population increases partially reflect a larger surveyed area rather than
  true population growth
- Data was extracted manually from PDF reports and compiled into
  `data/processed/tiger_population_2006_2022.xlsx`

---

## 2. Protected Area Boundaries

### 2.1 KBA Global — Key Biodiversity Areas

Polygon boundaries for all protected areas in India, used to define tiger
reserve extents and study area.

**Full Citation:**
> BirdLife International. (2026). *The World Database of Key Biodiversity
> Areas*. Developed by the KBA Partnership: BirdLife International,
> International Union for the Conservation of Nature, Amphibian Survival
> Alliance, Conservation International, Critical Ecosystem Partnership Fund,
> Global Environment Facility, NatureServe, Rainforest Trust, Royal Society
> for the Protection of Birds, Wildlife Conservation Society, and World
> Wildlife Fund. February 2026 version. Available at:
> http://www.keybiodiversityareas.org/

- **Access URL:** http://www.keybiodiversityareas.org/
- **Access Method:** Free download via KBA portal (account registration required)
- **Downloaded:** February 6, 2026
- **Dataset Version:** KBAsGlobal_2025_September_02
- **File:** `data/raw/wdpa/KBA_Data/KBAsGlobal_2025_September_02/KBAsGlobal_2025_September_02_POL.shp`
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **Feature Count:** 620 protected areas for India
- **License:** Free for non-commercial use; attribution required

**Known Issues / Limitations:**
- Protected area boundaries are approximate and may not reflect precise legal
  boundaries — consult official Survey of India data for authoritative extents
- Name variations exist (e.g., some reserves listed as "National Park" vs.
  "Tiger Reserve") — cross-reference with NTCA official lists
- May not include very recent designation changes (dataset version is
  September 2025)
- Some smaller protected areas and community reserves may be missing

---

## 3. Tiger Occurrence Records

### 3.1 GBIF Tiger Occurrences

Georeferenced tiger occurrence records aggregated from multiple institutions,
used as supplementary distribution data.

**Full Citation:**
> GBIF.org. (2026). *GBIF Occurrence Download: Panthera tigris in India*.
> https://doi.org/10.15468/dl.XXXXX *(replace with actual DOI from download)*

- **Access URL:** https://www.gbif.org/
- **Access Method:** Download via GBIF Occurrence API or web portal; free
  account required for bulk downloads
  - Query: `scientificName='Panthera tigris' AND country='IN'`
- **Downloaded:** February 5, 2026
- **File:** `data/raw/gbif/tiger_india_2006_2022_*.csv` (~4,000 records, ~2 MB)
- **Full dataset:** `data/raw/gbif/tiger_india_ALL_YEARS_*.csv` (~4,500 records, ~2.5 MB)
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **License:** CC BY 4.0 / CC0 (varies by individual record)

**Known Issues / Limitations:**
- Coordinate uncertainty ranges from <1 m to >100 km — filter by
  `coordinateUncertaintyInMeters` before spatial analysis
- Includes historical museum specimens with low spatial precision
- Multiple data sources and collection methods represented; quality varies
  by contributing institution
- Not all records are expert-verified; cross-reference photos where possible
- Data should be treated as supplementary to official NTCA census counts

---

### 3.2 iNaturalist Tiger Observations

Citizen science tiger observations with community verification, used for
supplementary distribution patterns and public engagement context.

**Full Citation:**
> iNaturalist contributors. (2026). *iNaturalist Research-grade Observations:
> Panthera tigris in India, 2006–2022*. iNaturalist.org. Occurrence dataset
> accessed via https://www.inaturalist.org on February 8, 2026.

- **Access URL:** https://www.inaturalist.org/observations
- **Access Method:** Web export via Explore page
  - Filters applied: Species = *Panthera tigris*, Location = India,
    Quality Grade = Research Grade, Has Photos = Yes,
    Captive = Excluded, Date = 2006-01-01 to 2022-12-31
  - Export → CSV format → delivered by email
- **Downloaded:** February 8, 2026
- **File:** `data/raw/inaturalist/inaturalist_tiger_india_research_2006_2022.csv`
- **Record Count:** 1,037 research-grade observations
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **License:** CC BY / CC BY-NC (varies by individual observer)

**Known Issues / Limitations:**
- **Coordinate obscuring (critical):** iNaturalist automatically offsets
  coordinates for threatened species by up to ~22 km (~0.2°). Tiger location
  data cannot be used for precise spatial analysis — suitable for broad
  distribution and presence/absence at district level only
- **Positional accuracy:** 54.4% of records have positional accuracy >1,000 m;
  filter to <500 m for any spatial analysis
- **Temporal bias:** Most observations are from more recent years due to
  platform growth; data is not temporally uniform across 2006–2022
- **Observer bias:** Concentrated near roads, park gates, and tourist areas;
  not representative of actual tiger distribution across reserve interiors
- **Not suitable for:** Population density estimation, precise habitat
  modeling, or movement/corridor analysis
- **Suitable for:** Broad distribution patterns, presence/absence at district
  level, temporal trends (relative), public engagement storytelling

---

## 4. Forest Cover Data

### 4.1 Global Forest Watch — Tropical Tree Cover

High-resolution tree cover data used as a forest habitat proxy for spatial
analysis and visualization.

**Full Citation:**
> Hansen, M.C., Potapov, P.V., Moore, R., Hancher, M., Turubanova, S.A.,
> Tyukavina, A., Thau, D., Stehman, S.V., Goetz, S.J., Loveland, T.R.,
> Kommareddy, A., Egorov, A., Chini, L., Justice, C.O., & Townshend, J.R.G.
> (2013). High-resolution global maps of 21st-century forest cover change.
> *Science*, 342(6160), 850–853. https://doi.org/10.1126/science.1244693
>
> Data accessed via Global Forest Watch: https://www.globalforestwatch.org/

- **Access URL:** https://data.globalforestwatch.org/
- **Access Method:** Navigate to Tropical Tree Cover dataset → select India →
  download shapefile; free, no account required
- **Downloaded:** February 9, 2026
- **Data Year:** 2020
- **Files:**
  - `data/raw/forest/global_forest_watch/Tropical_Tree_Cover_polygons.shp`
  - `data/raw/forest/global_forest_watch/Tropical_Tree_Cover_polygons.geojson`
- **Coverage:** 106 polygons covering India
- **Resolution:** 30 meters
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **License:** Open access; attribution required (cite Hansen et al. 2013)
- **Role in project:** Visualization layer (optional); canopy cover context

**Known Issues / Limitations:**
- **Tree cover ≠ forest cover:** Dataset includes plantations, orchards, and
  other non-forest tree cover — not directly comparable to FSI forest
  classification
- **Temporal gap:** Data year is 2020; tiger census is 2022
- **No forest type classification:** Only tree cover presence/absence, not
  VDF/MDF/OF density classes
- **Overall accuracy:** ~85% (Hansen et al. 2013)

---

### 4.2 India State of Forest Report 2021 — Chapter 4 *(PRIMARY SOURCE)*

**⭐ PRIMARY source for reserve-level forest cover in this project.**
Chapter 4 provides VDF/MDF/OF data measured directly from digitized Tiger
Reserve boundaries (WII, Dehradun) — not district-level proxies. Includes
decadal change (2011→2021) and corridor forest cover for all 52 reserves.

**Full Citation:**
> Forest Survey of India. (2022). *India State of Forest Report 2021,
> Chapter 4: Assessment of Forest Cover in Tiger Reserves and Lion
> Conservation Area of India*. Ministry of Environment, Forest and Climate
> Change, Government of India, Dehradun, Uttarakhand.
> Available at: https://fsi.nic.in/

- **Access URL:** https://fsi.nic.in/forest-report-2021
- **Access Method:** Direct PDF download from FSI website; no account required
- **Downloaded:** February 12, 2026
- **Assessment Period:** Data period 2019–2020
- **File:** `data/raw/forest/fsi_reports/chapter-4-2021.pdf`
- **Processed output:** `data/processed/forest/isfr_2021_reserve_corridors.xlsx`
- **License:** Government of India open data; attribution required

**Data extracted for this project (all 7 reserves):**

| Table | Contents | Status |
|---|---|---|
| Table 4.5 | VDF/MDF/OF within TR boundary, 2011 & 2021, % of TR area, change | ✅ Extracted |
| Table 4.9 / 4.10 | Forest cover in 13 tiger corridors (VDF/MDF/OF, % of corridor) | ✅ Extracted |
| Table 4.6 | Wetlands within tiger reserves (area in ha) | Available if needed |
| Table 4.7 | Forest type groups (Champion & Seth classification) | Available if needed |

**Key values (7 project reserves, ISFR 2021):**

| Reserve | TR Area (sq km) | Forest 2021 (sq km) | % of TR | 2011→2021 Change |
|---|---|---|---|---|
| Bandipur | 1,784.47 | 1,497.63 | 83.93% | −43.35 |
| Nagarahole | 1,152.74 | 970.71 | 84.21% | −0.70 (stable) |
| Kanha | 2,071.51 | 1,886.37 | 91.05% | −7.39 |
| Pench (MP) | 1,168.66 | 1,070.09 | 91.57% | −6.11 |
| Pench (MH) | 738.28 | 625.57 | 84.73% | −5.24 |
| Ranthambore | 1,765.57 | 1,360.30 | 77.05% | **+177.20 ▲** |
| Kaziranga | 1,180.35 | 1,180.16 | 86.00% | **+274.48 ▲** |
| Jim Corbett | 1,462.66 | 652.38 | 44.60% | ⚠ Boundary change — verify |

**Known Issues / Limitations:**
- **Spatial data not publicly available** — Chapter 4 provides statistics from
  digitized TR boundaries; vector/raster data requires official FSI/WII request
- **Jim Corbett anomaly:** −594.65 sq km change almost certainly reflects a TR
  boundary revision between 2011 and 2021 assessments, not actual forest loss;
  cross-check against NTCA shapefile
- **Minimum mapping unit:** 1 hectare
- **ArcGIS Zonal Statistics:** NOT required for tabular analysis (values already
  extracted). Only needed if building a VDF/MDF/OF visualization raster layer
  (deferred to Week 6, optional)

---

### 4.3 India State of Forest Report 2017 — State Chapters *(SECONDARY / CONTEXT)*

Used as a **landscape context layer** — provides district-level forest cover
data for the broader geography surrounding each reserve. Superseded by ISFR
2021 Chapter 4 for reserve-level analysis.

**Full Citation:**
> Forest Survey of India. (2017). *India State of Forest Report 2017*.
> Ministry of Environment, Forest and Climate Change, Government of India,
> Dehradun, Uttarakhand. Available at: https://fsi.nic.in/

- **Access URL:** https://fsi.nic.in/forest-report-2017
- **Access Method:** Direct PDF download; no account required
- **Downloaded:** February 9–12, 2026
- **Assessment Period:** Data period Oct–Dec 2015
- **Files downloaded:** Karnataka, Madhya Pradesh, Maharashtra, Rajasthan,
  Assam, Uttarakhand state chapters
- **Files:** `data/raw/forest/fsi_reports/*-isfr-2017.pdf`
- **Processed output:** `data/processed/forest/isfr_2017_forest_cover.xlsx`
- **License:** Government of India open data; attribution required

**Role in project:**
- District-level VDF/MDF/OF context for the landscape surrounding each reserve
- Useful for Story Map narrative (e.g., Rajasthan state has only 4.84% forest
  cover, making Ranthambore's tiger success more striking)
- **Not used** for reserve-level forest cover statistics (superseded by ISFR 2021)

**Known Issues / Limitations:**
- District-level data only — reserve boundary not used; values are proxies
- 2017 assessment; older than ISFR 2021
- Same spatial data limitations as ISFR 2021

---

## 5. Elevation Data

### 5.1 SRTM 1 Arc-Second Global DEM

Digital Elevation Model for terrain characterization, slope/aspect derivation,
and as a covariate in SECR density models.

**Full Citation (primary):**
> NASA Shuttle Radar Topography Mission (SRTM). (2013). *Shuttle Radar
> Topography Mission (SRTM) Global* [Dataset]. Distributed by OpenTopography.
> https://doi.org/10.5069/G9445JDF

**Full Citation (alternative):**
> U.S. Geological Survey. (2000). *Shuttle Radar Topography Mission 1
> Arc-Second Global elevation data* [Dataset]. U.S. Geological Survey.
> https://earthexplorer.usgs.gov/

- **Access URL:** https://earthexplorer.usgs.gov/
- **Access Method:** Free download via USGS Earth Explorer; free account
  registration required. Navigate to: Digital Elevation → SRTM →
  SRTM 1 Arc-Second Global → download GeoTIFF tiles
- **Downloaded:** February 9–13, 2026 (initial 13 tiles Feb 9; 11 additional tiles Feb 13 after buffer QC)
- **Data Collection Date:** February 2000 (Space Shuttle Endeavour mission)
- **Files:** `data/raw/elevation/srtm_30m_tiles/*.tif` (24 tiles)
- **Total File Size:** ~600 MB
- **Geographic Coverage:** 11°N–31°N, 73°E–94°E
- **Horizontal Resolution:** 30 meters (~1 arc-second)
- **Vertical Accuracy:** ±16 m absolute, ±6 m relative
- **Vertical Datum:** EGM96
- **Coordinate System:** WGS 1984 Geographic (EPSG:4326)
- **Format:** GeoTIFF, 16-bit signed integer; NoData = -32768
- **License:** Public domain

**Tiles by Reserve (24 tiles total):**

| Reserve | Core tiles | Buffer tiles (50km) |
|---|---|---|
| Jim Corbett NP | N29E078, N29E079, N30E078 | — |
| Kaziranga NP | N26E093, N26E094 | N26E092, N27E092, N27E093 |
| Bandipur NP | N11E076, N12E076 | N11E075, N12E075 |
| Nagarahole NP | N11E076, N12E076 | N11E075, N12E075 |
| Kanha NP | N22E080, N22E081 | N21E080, N21E081 |
| Pench TR | N21E079, N21E080 | N21E078, N22E078, N22E079 |
| Ranthambore NP | N26E076, N26E077 | N25E076 |

**Complete tile list (alphabetical):**  
N11E075, N11E076, N12E075, N12E076, N21E078, N21E079, N21E080, N21E081,
N22E078, N22E079, N22E080, N22E081, N25E076, N26E076, N26E077, N26E092,
N26E093, N26E094, N27E092, N27E093, N29E078, N29E079, N30E078

**Known Issues / Limitations:**
- **Vegetation bias (critical):** Radar signal reflects off tree canopy, not
  bare ground — elevation values in dense forest areas represent canopy height,
  not terrain. Affects accuracy in Bandipur, Nagarahole, Kanha, and Corbett
- **Data age:** Collected in 2000; 24 years old. Terrain changes from erosion
  and landslides are minimal, but human landscape changes are not captured
- **Data voids:** Some areas have gaps (steep terrain, water bodies) filled
  with interpolation in the processed version
- **Spatial resolution:** 30 m may be too coarse for micro-topography or
  features smaller than 30 m
- **Not suitable for:** Property or plot-level terrain analysis

---

## 6. Administrative Boundaries

### 6.1 Natural Earth — Admin 0 Countries

India country boundary used as clipping mask and for national-scale maps.

**Full Citation:**
> Natural Earth. (2024). *1:10m Cultural Vectors — Admin 0 Countries* [Dataset].
> Free vector and raster map data. https://www.naturalearthdata.com/

- **Access URL:** https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
- **Access Method:** Direct shapefile download; no account required
- **Downloaded:** February 10, 2026
- **Scale:** 1:10,000,000
- **File:** `data/raw/administrative/natural_earth/ne_10m_admin_0_countries/`
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **License:** Public domain; no restrictions

---

### 6.2 Natural Earth — Admin 1 States and Provinces

Indian state and union territory boundaries for state-level aggregation and
spatial joins.

**Full Citation:**
> Natural Earth. (2024). *1:10m Cultural Vectors — Admin 1 States and
> Provinces* [Dataset]. Free vector and raster map data.
> https://www.naturalearthdata.com/

- **Access URL:** https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
- **Access Method:** Direct shapefile download; no account required
- **Downloaded:** February 10, 2026
- **Scale:** 1:10,000,000
- **File:** `data/raw/administrative/natural_earth/ne_10m_admin_1_states_provinces/`
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **Feature Count:** 36 Indian states and union territories (verified)
- **License:** Public domain; no restrictions

**Known Issues / Limitations (all Natural Earth layers):**
- **Generalization:** Boundaries are simplified at 1:10m scale — not suitable
  for cadastral or property-level mapping; appropriate for regional/national
  scale only
- **Disputed boundaries:** International boundaries, particularly Kashmir, may
  not reflect the official Government of India position. Use Survey of India
  data for authoritative boundaries in publications
- **Currency:** May be 1–2 years behind recent administrative changes
- **No Admin 2:** Natural Earth does not include district-level data for India

---

### 6.3 Natural Earth — Populated Places and Rivers

Major cities, towns, and river systems used for geographic context and map
labeling in the Story Map.

**Full Citation:**
> Natural Earth. (2024). *1:10m Cultural and Physical Vectors — Populated
> Places; Rivers and Lake Centerlines* [Datasets]. Free vector and raster map
> data. https://www.naturalearthdata.com/

- **Access URL:** https://www.naturalearthdata.com/downloads/10m-cultural-vectors/ (populated places)  
  https://www.naturalearthdata.com/downloads/10m-physical-vectors/ (rivers)
- **Access Method:** Direct shapefile download; no account required
- **Downloaded:** February 10, 2026
- **Files:**
  - `data/raw/administrative/natural_earth/ne_10m_populated_places/`
  - `data/raw/administrative/natural_earth/ne_10m_rivers_lake_centerlines/`
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **License:** Public domain; no restrictions

---

### 6.4 DataMeet India — District Boundaries

District-level administrative boundaries for district-level aggregation and
optional sub-state analysis.

**Full Citation:**
> DataMeet India Community. (2011). *India District Boundaries* [Dataset].
> GitHub repository: https://github.com/datameet/maps. License: CC BY 4.0.
> District boundaries based on Census of India 2011 delimitation.

- **Access URL:** https://github.com/datameet/maps/tree/master/Districts
- **Access Method:** Direct download from GitHub; no account required
- **Downloaded:** February 10, 2026
- **Data Year:** 2011 (Census of India delimitation)
- **File:** `data/raw/administrative/districts/2011_Dist.shp`
- **Feature Count:** 641 districts
- **Attributes:** `DISTRICT`, `ST_NM`, `censuscode`
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **License:** CC BY 4.0 — attribution required in all publications

**Known Issues / Limitations:**
- Boundaries reflect **2011 Census delimitation** — new districts created
  since 2011 (e.g., several states have reorganized districts) are not
  reflected
- Community-maintained dataset; not an official Government of India source
- Attribute fields are minimal — district name, state name, and census code
  only; no population or area data included
- For authoritative district boundaries, consult the Survey of India or
  Census of India 2011 portal

---

## 7. Infrastructure Data

### 7.1 OpenStreetMap — Roads and Settlements

Road network and settlement data for human disturbance analysis and proximity
modeling.

**Full Citation:**
> OpenStreetMap contributors. (2026). *OpenStreetMap Data* [Dataset].
> OpenStreetMap Foundation. www.openstreetmap.org. Available under the Open
> Database License (ODbL). Downloaded via Geofabrik:
> https://download.geofabrik.de/asia/india.html

- **Access URL:** https://download.geofabrik.de/asia/india.html
- **Access Method:** Direct shapefile download (`india-latest-free.shp.zip`);
  no account required; file size ~700 MB zipped
- **Downloaded:** February 10, 2026
- **Data Currency:** Continuously updated (OSM snapshot as of download date)
- **Files extracted:**
  - `data/raw/osm/roads_major.shp` — motorway, trunk, primary, secondary roads
  - `data/raw/osm/settlements.shp` — cities and towns with population >1,000
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **License:** Open Database License (ODbL) — attribution and share-alike
  required

**Roads attributes:** `highway` (road class), `name`, `ref` (route number)  
**Settlements attributes:** `name`, `place` (city/town/village), `population`

**Known Issues / Limitations:**
- **Variable completeness:** OSM coverage is densest in urban and tourist
  areas; remote forest roads and minor tracks may be missing
- **No quality guarantee:** Contributed by volunteers; individual features
  may have errors in geometry, classification, or attributes
- **Temporal snapshot:** Data reflects OSM at the download date; not tied to
  a specific year for temporal analysis
- **Population values:** Settlement population estimates are often missing or
  outdated in OSM — use census data for authoritative population figures
- **Not suitable for:** Authoritative road network analysis or navigation;
  suitable for proximity and density analysis only

---

## 8. How to Reproduce This Dataset

All data used in this project is publicly available. Follow these steps to
re-download from scratch:

1. **NTCA Census PDFs** — Download all 5 reports directly from ntca.gov.in
   using URLs in Section 1.1
2. **KBA Boundaries** — Register at keybiodiversityareas.org and download
   India KBA dataset
3. **GBIF Occurrences** — Use GBIF web portal or API with query
   `scientificName='Panthera tigris' AND country='IN'`
4. **iNaturalist Observations** — Use Explore page filters (see Section 3.2)
   and export as CSV
5. **Global Forest Watch** — Download Tropical Tree Cover shapefile for India
   from data.globalforestwatch.org
6. **FSI Reports** — Download ISFR 2017 and 2021 PDFs from fsi.nic.in
7. **SRTM Elevation** — Register at earthexplorer.usgs.gov, search SRTM
   1 Arc-Second Global, select 19 tiles covering study area
8. **Natural Earth** — Download Admin 0, Admin 1, Populated Places, and
   Rivers from naturalearthdata.com/downloads/10m-cultural-vectors/
9. **DataMeet Districts** — Download `2011_Dist.shp` from
   github.com/datameet/maps
10. **OSM Roads/Settlements** — Download `india-latest-free.shp.zip` from
    download.geofabrik.de/asia/india.html and extract relevant layers

For the Singh & Sen (2015) paper, search ResearchGate or Google Scholar for:
"Comparative Analysis of Tiger Landscape Complexes and Reserves in India 2015"

---

## 9. License Summary

| Dataset | License | Attribution Required | Commercial Use |
|---|---|---|---|
| NTCA Census Reports | Government of India | Yes | Research/education |
| KBA Boundaries | Non-commercial | Yes | No |
| GBIF Occurrences | CC BY 4.0 / CC0 | Yes | Allowed |
| iNaturalist Observations | CC BY / CC BY-NC | Yes | Check per record |
| Global Forest Watch | Open Access | Yes (Hansen et al.) | Allowed |
| FSI Reports | Government of India | Yes | Research/education |
| SRTM Elevation | Public Domain | No | Allowed |
| Natural Earth (all) | Public Domain | No | Allowed |
| DataMeet Districts | CC BY 4.0 | Yes | Allowed |
| OpenStreetMap | ODbL | Yes | Allowed (share-alike) |
| Singh & Sen (2015) | Academic Fair Use | Yes (cite paper) | No |

---

## Story Map Attribution Block

Use this in the Story Map "Data Sources" or "Credits" section:

```
Data Sources:

Tiger Population: National Tiger Conservation Authority All India Tiger
Estimation Reports (2006–2022); Bandipur/Nagarahole 2006 & 2010 data from
Singh & Sen (2015), Am Research Thoughts, Vol. 1.

Protected Areas: KBA Global Database, BirdLife International / KBA
Partnership (February 2026), keybiodiversityareas.org.

Tiger Occurrences: GBIF.org (2026); iNaturalist contributors (2026),
research-grade observations.

Forest Cover: Forest Survey of India, *India State of Forest Report 2021*,
Chapter 4 — Assessment of Forest Cover in Tiger Reserves (primary source,
reserve-boundary level data); ISFR 2017 state chapters (landscape context);
Hansen et al. (2013), Science 342:850–853, via Global Forest Watch
(visualization layer).

Elevation: NASA SRTM 1 Arc-Second Global DEM (2000), via USGS Earth Explorer.

Administrative Boundaries: Natural Earth (public domain),
naturalearthdata.com; DataMeet India (CC BY 4.0), github.com/datameet/maps.

Roads & Settlements: OpenStreetMap contributors (ODbL),
download.geofabrik.de.
```

---

*Document maintained in: `docs/data-sources.md`*  
*Project repository: https://github.com/K-bsub/tiger-conservation-india*
