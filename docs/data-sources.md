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

## Phase 2 Data Sources — Corridor Connectivity & Threat Mapping

**Phase 2 Project:** Under Pressure: Mapping the Corridors and Threats That Shape
India's Tiger Landscapes  
**Added:** March 22, 2026  
**Note:** All Phase 1 data sources (Sections 1–7) are reused in Phase 2 without
re-download. This section documents new datasets acquired specifically for Phase 2.

---

## 10. Tiger Corridor Spatial Data

### 10.1 NTCA Decision Support System — PA/TR/Corridor KML

Authoritative spatial boundaries for Protected Areas, Tiger Reserves, and tiger
movement corridors across India, published by NTCA for use in evaluating
infrastructure development projects near tiger habitat.

**Full Citation:**
> National Tiger Conservation Authority. (2022). *PA_TR_Corridor_Final* [KML
> Dataset]. Decision Support System, National Tiger Conservation Authority,
> Ministry of Environment, Forests and Climate Change, Government of India,
> New Delhi. Last updated July 2022. Available at: https://ntca.gov.in/dss/

- **Access URL:** https://ntca.gov.in/dss/
- **Direct download:** https://ntca.gov.in/wp-content/uploads/2022/07/PA_TR_Corridor_Final.zip
- **Access Method:** Direct ZIP download; no login required
- **Downloaded:** February 22, 2026
- **Data Currency:** July 2022
- **File (raw):** `data/raw/ntca/PA_TR_Corridor_Final/PA_TR_Corridor_Final.kml`
- **Coordinate System (raw):** WGS 1984 Geographic (EPSG:4326)
- **License:** Government of India; attribution required; research/education use

**Contents of KML:**
- `Polylines` layer — 764 features mixing PA boundary outlines (named) and
  corridor centerlines (unnamed; `Name = 'Placemark'`)
- `Polygons` layer — Protected area boundary polygons (redundant with KBA data)

**Processing steps (Phase 2):**
1. Converted KML to feature class using ArcGIS Pro **KML To Layer** tool
2. Selected all features where `Name = 'Placemark'` to isolate corridor centerlines
   from named PA boundary polylines
3. Exported selection to `tiger_project.gdb/Connectivity/NTCA_Corridors_Raw`
4. Added fields `Corridor_Name` (Text, 100) and `Corridor_ID` (Short Integer)
5. Manually assigned corridor names for all 6 study corridors using
   Select by Location against reserve boundaries
6. Dissolved by `Corridor_Name` to merge fragmented segments per corridor
7. Buffered 5 km to create `NTCA_Corridors_Buffered_5km` (zone polygons
   for zonal statistics and threat analysis)

**6 study corridors confirmed present:**

| Corridor_ID | Corridor_Name | Reserves Connected |
|---|---|---|
| 1 | Corbett–Rajaji | Jim Corbett NP ↔ Rajaji NP |
| 2 | Kaziranga–Karbi Anglong | Kaziranga NP ↔ Karbi Anglong hills |
| 3 | Kanha–Pench | Kanha NP ↔ Pench TR |
| 4 | Kanha/Pench–Satpura | Kanha/Pench ↔ Satpura TR |
| 5 | Ranthambore–Mukundra | Ranthambore TR ↔ Mukundra Hills TR |
| 6 | Bandipur–Nagarahole | Bandipur NP ↔ Nagarahole NP ↔ BRT WLS |

**Known Issues / Limitations:**
- **Corridor geometry type:** Centerlines (polylines), not polygon zones —
  buffered to 5 km for zonal analysis; buffer width is an analytical choice,
  not an authoritative boundary
- **Unnamed features:** Corridor centerlines carry no name attribute in the
  source KML (`Name = 'Placemark'`); names assigned manually in Phase 2
  based on spatial proximity to reserves
- **Data currency:** July 2022 — corridor boundaries may not reflect the most
  recent WII corridor delineations
- **Fragmented geometry:** Some corridors encoded as multiple disconnected
  segments in the KML; dissolved to single multi-part features per corridor
- **Not peer-reviewed spatial data:** KML intended for infrastructure clearance
  screening, not published corridor research — treat as authoritative for
  approximate extents only; cross-reference with ISFR 2021 tabular corridor
  data (already in `data/processed/forest/isfr_2021_reserve_corridors.xlsx`)

---

## 11. Land Cover Data

### 11.1 ESA WorldCover 2021 — 10m Global Land Cover

High-resolution land cover classification used as the primary land cover layer
for Phase 2 corridor quality and threat analysis, replacing the Global Forest
Watch tree cover layer (Section 4.1) for inter-reserve landscape characterization.

**Full Citation:**
> Zanaga, D., Van De Kerchove, R., Daems, D., De Keersmaecker, W., Brockmann,
> C., Kirches, G., Wevers, J., Cartus, O., Santoro, M., Fritz, S., Lesiv, M.,
> Herold, M., Tsendbazar, N.E., Xu, P., Ramoino, F., & Arino, O. (2022).
> *ESA WorldCover 10 m 2021 v200*. https://doi.org/10.5281/zenodo.7254221

- **Access URL:** https://esa-worldcover.org/en/data-access
- **Access Method:** Direct GeoTIFF download via AWS public S3 bucket
  (`s3://esa-worldcover/`); no account required
- **Tile URL pattern:**
  `https://esa-worldcover.s3.amazonaws.com/v200/2021/map/ESA_WorldCover_10m_2021_v200_{TILE}_Map.tif`
- **Downloaded:** March 21-22, 2026
- **Product version:** WorldCover 2021 v200
- **Data year:** 2020
- **Resolution:** 10 meters
- **Coordinate System (raw):** WGS 1984 Geographic (EPSG:4326)
- **Format:** Cloud Optimized GeoTIFF (COG), 8-bit unsigned integer
- **License:** CC BY 4.0 — attribution required

**Tiles downloaded (19 tiles):**

| Tile | Coverage | Reserves/corridors covered |
|---|---|---|
| N09E075 | 9–12°N, 75–78°E | Bandipur, Nagarahole (south) |
| N12E075 | 12–15°N, 75–78°E | Bandipur, Nagarahole (north), BRT corridor |
| N21E075 | 21–24°N, 75–78°E | Ranthambore (west buffer) |
| N21E078 | 21–24°N, 78–81°E | Ranthambore (west buffer) |
| N24E075 | 24–27°N, 75–78°E | Ranthambore, Mukundra corridor |
| N27E075 | 27–30°N, 75–78°E | Ranthambore buffer north, Corbett west |
| N21E078 | 21–24°N, 78–81°E | Kanha, Pench, Kanha–Pench corridor |
| N21E081 | 21–24°N, 81–84°E | Kanha buffer east |
| N24E075 | 24–27°N, 75–78°E | Central India north |
| N24E078 | 24–27°N, 78–81°E | Central India north |
| N24E081 | 24–27°N, 81–84°E | Central India east |
| N27E075 | 27–30°N, 75–78°E | Jim Corbett |
| N27E078 | 27–30°N, 78–81°E | Jim Corbett |
| N27E081 | 27–30°N, 81–84°E | Corbett buffer east |
| N27E090 | 27–30°N, 90–93°E | Corbett buffer east |
| N30E075 | 30–33°N, 75–78°E | Rajaji NP (Corbett–Rajaji corridor north end) |
| N30E078 | 30–33°N, 81–84°E | Rajaji NP (Corbett–Rajaji corridor north end) |
| N24E090 | 24–27°N, 90–93°E | Kaziranga buffer west |
| N24E093 | 24–27°N, 93–96°E | Kaziranga, Karbi Anglong corridor |
| N27E093 | 27–30°N, 93–96°E | Kaziranga buffer north |

**Files:**
- Raw tiles: `data/raw/esa_worldcover/ESA_WorldCover_10m_2021_v200_{TILE}_Map.tif`
- Mosaic: `ESA_WorldCover_India_Mosaic` (WGS84, 8-bit unsigned, 1 band)
- Analysis-ready: `tiger_project.gdb/Threats/ESA_WorldCover_UTM43N`
  (clipped to `Reserve_Buffer_50km`, reprojected UTM 43N, nearest neighbor)

**Land cover classes:**

| Value | Class | Relevance to corridor analysis |
|---|---|---|
| 10 | Tree cover | Core tiger habitat / high corridor quality |
| 20 | Shrubland | Marginal habitat |
| 30 | Grassland | Marginal — important prey habitat |
| 40 | Cropland | Human pressure / movement barrier |
| 50 | Built-up | High barrier / threat |
| 60 | Bare / sparse vegetation | Semi-arid matrix (Ranthambore) |
| 80 | Permanent water bodies | Physical barrier |
| 90 | Herbaceous wetland | Kaziranga floodplain context |
| 95 | Mangroves | Coastal — not relevant to study area |
| 100 | Moss and lichen | High altitude — not relevant |

**Known Issues / Limitations:**
- **Overall accuracy:** 76.7% (Wageningen University independent validation) —
  lower than SRTM or census data; interpret land cover patterns at landscape
  scale, not individual pixel level
- **Tree cover ≠ forest quality:** Class 10 includes plantations and degraded
  forest alongside natural forest — cannot distinguish dense natural forest
  from monoculture plantation without additional data
- **Temporal gap:** 2021 land cover; some recent land use changes post-2021
  not captured
- **Resampling:** Nearest neighbor used for UTM 43N reprojection to preserve
  categorical class integrity — pixel boundaries shift slightly but class
  values are not interpolated
- **Supersedes GFW layer for Phase 2:** ESA WorldCover preferred over Global
  Forest Watch (Section 4.1) for inter-reserve analysis due to full land cover
  classification vs. tree cover only, and higher thematic detail

---

## 12. Human Pressure Data

### 12.1 Global Human Modification Index (gHM)

A composite raster quantifying cumulative human modification of terrestrial
land surfaces, combining infrastructure, agriculture, urbanization, and
human population density into a single continuous index (0–1 scale). Used
as a pre-computed human pressure layer to complement road and settlement
kernel density analysis.

**Full Citation:**
> Kennedy, C.M., Oakleaf, J.R., Theobald, D.M., Baruch-Mordo, S., &
> Kiesecker, J. (2019). Managing the middle: A shift in conservation
> priorities based on the global human modification gradient. *Global Change
> Biology*, 25(3), 811–826. https://doi.org/10.1111/gcb.14549

**Dataset citation:**
> Kennedy, C.M., Oakleaf, J.R., Theobald, D.M., Baruch-Mordo, S., &
> Kiesecker, J. (2019). *Global Human Modification* [Dataset]. figshare.
> https://figshare.com/articles/dataset/Global_Human_Modification/7283087

- **Access URL:** https://figshare.com/articles/dataset/Global_Human_Modification/7283087
- **Access Method:** Direct GeoTIFF download from figshare; no account required
- **Downloaded:** March 2026
- **Data year:** 2016 (most recent available at time of download)
- **Resolution:** ~1 km (0.009 decimal degrees)
- **Coordinate System (raw):** WGS 1984 Geographic (EPSG:4326)
- **Value range:** 0.0 (no modification) to 1.0 (complete modification)
- **Format:** GeoTIFF, 32-bit float
- **License:** CC BY 4.0 — attribution required

**Files:**
- Raw: `data/raw/human_modification/gHM.tif`
- Analysis-ready: `tiger_project.gdb/Threats/HumanMod_Index_UTM43N`
  (clipped to `Reserve_Buffer_50km`, reprojected UTM 43N, bilinear resampling,
  1000m cell size)

**Index components (from Kennedy et al. 2019):**
Built environments, agriculture (cropland, pasture), transportation
infrastructure, mining and energy production, and human population density.

**Interpretation for study area:**

| gHM Value | Interpretation | Expected locations |
|---|---|---|
| 0.0–0.1 | Very low modification | Reserve interiors, dense forest |
| 0.1–0.3 | Low modification | Buffer zones, forest edge |
| 0.3–0.6 | Moderate modification | Agricultural matrix, rural areas |
| 0.6–0.8 | High modification | Peri-urban, intensive agriculture |
| 0.8–1.0 | Very high modification | Urban areas, industrial zones |

**Known Issues / Limitations:**
- **Data currency:** 2016 baseline — a decade old at time of use; significant
  infrastructure development in India since 2016 (road expansion, urbanization)
  not captured
- **Resolution:** 1 km — too coarse to detect narrow corridor pinch points or
  individual road crossings; supplemented by OSM road KDE at same resolution
- **Global composite:** Index weights calibrated globally, not optimized for
  Indian tiger landscape context — local road and settlement KDE surfaces
  (Section 7.1) may better capture fine-scale threats
- **Bilinear resampling used:** gHM is a continuous index (not categorical),
  so bilinear resampling is appropriate for reprojection — contrast with
  ESA WorldCover (nearest neighbor)
- **Not suitable for:** Sub-kilometer threat assessment or individual feature
  identification; suitable for landscape-scale corridor quality ranking

---

## 13. Phase 2 Reproduce This Dataset

New datasets only — all Phase 1 datasets reproduced per Section 8.

1. **NTCA Corridor KML** — Download `PA_TR_Corridor_Final.zip` from
   https://ntca.gov.in/dss/ and convert using ArcGIS Pro KML To Layer tool
2. **ESA WorldCover 2021** — Download 15 tiles via AWS S3 public bucket using
   URL pattern in Section 11.1; no account required
3. **Global Human Modification Index** — Download `gHM.tif` from
   https://figshare.com/articles/dataset/Global_Human_Modification/7283087

---

## 14. Phase 2 License Summary

| Dataset | License | Attribution Required | Commercial Use |
|---|---|---|---|
| NTCA Corridor KML | Government of India | Yes | Research/education |
| ESA WorldCover 2021 | CC BY 4.0 | Yes (Zanaga et al. 2022) | Allowed |
| Global Human Modification Index | CC BY 4.0 | Yes (Kennedy et al. 2019) | Allowed |

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

## Phase 2 Story Map Attribution Block

Use this in the Phase 2 Story Map "Data Sources" or "Credits" section:

```
Data Sources:

Tiger Corridors: National Tiger Conservation Authority Decision Support
System, PA_TR_Corridor_Final KML (July 2022), ntca.gov.in/dss/.
Corridor names assigned based on ISFR 2021 Chapter 4 corridor documentation
(Forest Survey of India, 2022).

Land Cover: Zanaga et al. (2022). ESA WorldCover 10 m 2021 v200.
doi:10.5281/zenodo.7254221. © ESA WorldCover project 2021 / Contains
modified Copernicus Sentinel data (2021) processed by ESA WorldCover
consortium.

Human Modification: Kennedy et al. (2019). Global Human Modification Index.
Global Change Biology, 25(3), 811–826. doi:10.1111/gcb.14549. Dataset via
figshare.com.

Roads & Settlements: OpenStreetMap contributors (ODbL),
download.geofabrik.de. [Reused from Phase 1]

Forest Cover (corridor quality): Forest Survey of India, India State of
Forest Report 2021, Chapter 4, Tables 4.9/4.10 — forest cover in tiger
corridors. [Reused from Phase 1]
```

---

*Phase 2 data sources appended to: `docs/data-sources.md`*  
*Phase 2 project: Under Pressure — Corridor Connectivity & Threat Mapping*  
*Project repository: https://github.com/K-bsub/tiger-conservation-india*

---

*Document maintained in: `docs/data-sources.md`*  
*Project repository: https://github.com/K-bsub/tiger-conservation-india*
