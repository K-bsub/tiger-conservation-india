# Project Proposal: Mapping Tiger Conservation Success in India's National Parks

**Author:** Kiran Balasubramanian 
**Date:** February 4, 2026  
**Course:** GIS Project  
**Project Type:** ArcGIS Story Map  
**Last Updated:** February 16, 2026  
**Published Story Map:** https://storymaps.arcgis.com/stories/c9e21879e1b2483e81fc79fd357c59b2  
**Short URL:** https://arcg.is/00bXi44

---

## Title, Introduction and Statement of Problem

### Title

**Identifying Conservation Success Stories: Spatial Analysis of Tiger Population Recovery in India's Protected Areas (2006-2022)**

### Introduction

India is home to approximately 70% of the world's wild tiger population, making it a critical nation for global tiger conservation. Following decades of population decline that brought tigers to the brink of extinction, India launched Project Tiger in 1973 and has since conducted systematic tiger censuses every four years through the National Tiger Conservation Authority (NTCA). Despite ongoing conservation challenges, several national parks and tiger reserves have demonstrated remarkable success in rebuilding tiger populations over the past two decades. This project will use GIS to identify and analyze the most successful tiger conservation areas in India, examining spatial patterns of population growth and recovery between 2006 and 2022. The analysis will focus on reserves that have shown consistent population increases, helping to highlight best practices in tiger conservation and identify key characteristics of successful protected areas.

### Statement of Purpose

The purpose of this project is to create an ArcGIS Story Map showcasing India's tiger conservation success stories by analyzing spatial and temporal patterns in tiger populations across major national parks and reserves. Specific objectives include:

1. **Mapping tiger population density changes** from 2006 to 2022 to identify reserves with the strongest recovery trends
2. **Comparing population growth rates** across successful reserves to rank conservation performance
3. **Analyzing spatial distribution patterns** to identify tiger population hotspots and core breeding areas
4. **Examining habitat characteristics** of successful reserves including forest cover, elevation profiles, and protected area size

### Study Area and Rationale

The study area encompasses India's major tiger reserves, with particular focus on confirmed success stories including:

- **Jim Corbett National Park** (Uttarakhand)
- **Kaziranga National Park** (Assam)
- **Bandipur National Park** (Karnataka)
- **Nagarahole National Park** (Karnataka)
- **Kanha National Park** (Madhya Pradesh)
- **Pench National Park** (Madhya Pradesh/Maharashtra)
- **Ranthambore National Park** (Rajasthan)

**Why India?** India was selected because it contains the world's largest tiger population and maintains the most comprehensive tiger monitoring program globally, with systematic census data spanning nearly two decades.

**Why focus on successful reserves?** The focus on successful reserves was chosen to create a positive conservation narrative that highlights effective management strategies while providing a foundation for future expansion to include connectivity analysis and threat assessment.

---

## Data Discovery

### Primary Data Sources

#### National Tiger Conservation Authority (NTCA)

- **Data Type:** Official tiger census data from All India Tiger Estimation Reports
- **Years Available:** 2006, 2010, 2014, 2018, 2022
- **Content:** Reserve-wise population estimates, distribution data, census methodology documentation
- **Access:** https://ntca.gov.in
- **Format:** PDF reports (data extraction required)
- **Status:** Publicly available; detailed spatial data may require formal data request

#### Global Biodiversity Information Facility (GBIF)

- **Data Type:** Tiger occurrence records (*Panthera tigris*)
- **Content:** GPS coordinates, observation dates, data sources, verification status
- **Access:** https://www.gbif.org
- **Format:** CSV, compatible with ArcGIS
- **Status:** Free download available

#### iNaturalist

- **Data Type:** Community-sourced, GPS-tagged tiger observations
- **Content:** Verified sightings with photos, coordinates, dates
- **Access:** API or bulk download interface
- **Format:** CSV/JSON
- **Status:** Free access

#### World Database on Protected Areas (WDPA)

- **Data Type:** Spatial boundaries for Indian tiger reserves and national parks
- **Maintained by:** UN Environment Programme
- **Access:** https://www.protectedplanet.net
- **Format:** Shapefile, GeoJSON
- **Status:** Free download available

### Supporting Spatial Data Sources

#### Forest Survey of India

- **Data Type:** Forest cover classification — VDF/MDF/OF at reserve-boundary level
- **Primary source:** ISFR 2021, Chapter 4 — Assessment of Forest Cover in Tiger Reserves;
  provides exact forest cover within each TR boundary (not district proxies), with
  2011 vs. 2021 decadal comparison and tiger corridor data
- **Secondary source:** ISFR 2017 state chapters — district-level landscape context
- **Access:** https://fsi.nic.in
- **Format:** PDF reports (tabular extraction); raster/vector data requires FSI request
- **Status:** ✅ Tabular data fully extracted; forest cover analysis complete

#### SRTM (Shuttle Radar Topography Mission)

- **Data Type:** Digital elevation models
- **Access:** USGS Earth Explorer
- **Resolution:** 30m or 90m
- **Format:** GeoTIFF
- **Status:** Free download

#### Natural Earth Data

- **Data Type:** India administrative boundaries (states, districts)
- **Access:** https://www.naturalearthdata.com
- **Format:** Shapefile
- **Status:** Public domain

#### OpenStreetMap (OSM)

- **Data Type:** Roads, settlements, infrastructure features
- **Access:** Geofabrik or QuickOSM plugin
- **Format:** Shapefile, GeoPackage
- **Status:** Open data

### Data Availability Assessment

**Confirmed Available:**
- ✅ NTCA census reports (public documents)
- ✅ GBIF occurrence data (direct download)
- ✅ WDPA protected area boundaries (direct download)
- ✅ Elevation data (USGS)
- ✅ Administrative boundaries (Natural Earth)
- ✅ Forest cover data — ISFR 2021 Chapter 4 (tabular extraction complete;
  reserve-boundary VDF/MDF/OF for all 7 reserves extracted February 2026)

**May Require Request:**
- ⚠️ Detailed spatial data from NTCA (formal data request may be needed)
- ⚠️ FSI forest cover raster/vector (requires registration; deferred —
  tabular values from ISFR 2021 already satisfy analysis requirements)

**Contingency Plan:**
If comprehensive spatial data from NTCA is unavailable, I will supplement with GBIF and iNaturalist point data to create density maps and distribution analyses. No data creation is anticipated as all necessary datasets exist in public repositories, though data cleaning and format standardization will be required to integrate temporal census data with spatial occurrence records.

---

## Methods and Anticipated Results

### Data Preparation and Processing

#### Census Data Integration

Tiger census data from NTCA reports (2006-2022) will be extracted and compiled into a tabular database linking reserve names to population counts for each census year. This temporal data will be joined to WDPA protected area polygons using reserve names as the common field, creating a spatially-enabled time-series dataset.

#### Point Data Cleaning

GBIF and iNaturalist point observations will be filtered to include only verified tiger sightings within the study timeframe (2006-2022), then cleaned to remove duplicate records and observations with poor coordinate accuracy (>1km uncertainty).

#### Spatial Reference

All spatial data will be projected to **WGS 1984 UTM Zone 43N** to maintain accurate distance and area calculations for India.

#### Forest Cover Data

Forest cover at the reserve level is sourced from ISFR 2021 Chapter 4 (Table 4.5),
which provides VDF/MDF/OF measurements taken directly from digitized Tiger Reserve
boundaries. This eliminates the need for ArcGIS Zonal Statistics for tabular analysis.
If a VDF/MDF/OF visualization raster layer is desired for the Story Map, FSI raster
data will be requested and processed in Week 6 (optional). District-level context
from ISFR 2017 is retained for landscape narrative purposes.

#### Data Clipping

Elevation rasters will be clipped to the extent of tiger reserves to improve
processing efficiency and focus analysis on relevant areas.

### Analysis Methods

#### 1. Population Trend Analysis

- Calculate percent change and absolute growth in tiger numbers for each reserve between 2006 and 2022
- Identify reserves in the top quartile of population growth
- Generate time-series data for visualization

#### 2. Spatial Density Analysis

- Apply **kernel density estimation** to tiger occurrence points
- Create heat maps showing spatial concentration of tiger sightings
- Allow identification of core areas within successful reserves
- Compare density patterns between 2006 and 2022

#### 3. Hot Spot Analysis

- Use **Hot Spot Analysis (Getis-Ord Gi*)** tool
- Identify statistically significant clusters of tiger observations
- Distinguish genuine population centers from random sightings
- Map confidence levels of clustering

#### 4. Reserve-Level Statistics

Calculate for each reserve:
- Tigers per 100 square kilometers (population density)
- Total population (absolute numbers)
- Growth rate ranking (comparative performance)
- Population change category (high growth, moderate, stable, declining)

#### 5. Habitat Characterization

- Apply **zonal statistics** to extract mean elevation for each reserve
- Determine dominant forest types within reserve boundaries
- Calculate reserve area and perimeter
- Identify habitat conditions in successful conservation areas

#### 6. Time-Series Visualization

- Plot population trajectories for top-performing reserves
- Show recovery patterns from 2006 baseline through 2022
- Create comparative line graphs for multiple reserves
- Generate bar charts for growth rate rankings

### Expected Results and Deliverables

#### Primary Deliverable: ArcGIS Story Map

**Structure:**

1. **Introduction Chapter**
   - Context: Tiger conservation in India
   - Historical background of Project Tiger
   - Importance of systematic monitoring

2. **Success Stories Chapter** (Main Focus)
   - Interactive web map displaying tiger reserve boundaries
   - Color-coded by population growth category (high, moderate, stable, declining)
   - Clickable popups with reserve details

3. **Population Trends Section**
   - Line graphs showing tiger population changes over time for 5-7 featured reserves
   - Bar chart ranking reserves by percent population increase
   - Statistical summary tables

4. **Spatial Analysis Section**
   - Kernel density heat maps showing tiger concentration hotspots
   - Side-by-side comparison: 2006 vs 2022
   - Demonstrates geographic expansion of populations in successful reserves

5. **Comparative Analysis Section**
   - Reserve profile cards (infographic style) including:
     - Current population
     - Reserve area
     - Tigers per 100 km²
     - Elevation range
     - Dominant habitat type
   - Embedded maps for each featured reserve

6. **Key Findings & Conclusion**
   - Characteristics of successful reserves
   - Conservation best practices identified
   - Call to action for continued conservation support

#### Anticipated Findings

- **Top Performing Regions:**
  - Karnataka's connected reserve complex (Bandipur-Nagarahole)
  - Madhya Pradesh's central Indian reserves (Kanha-Pench)
  
- **Population Increases:**
  - 50-150% increases over the study period in successful reserves
  - Identification of specific reserves exceeding national average growth
  
- **Spatial Patterns:**
  - Expansion of tiger populations from core areas into buffer zones
  - Increased density in well-protected, prey-rich habitats
  
- **Habitat Characteristics:**
  - Successful reserves likely to show:
    - Larger protected area size (>500 km²)
    - Dense forest cover (>70%)
    - Moderate elevations (200-800m)
    - Connectivity to other protected areas

#### Future Expansion Potential

The modular Story Map design will allow future expansion to include:
- **Phase 2:** Corridor analysis and connectivity assessment
- **Phase 3:** Threat mapping and human-wildlife interface analysis
- **Phase 4:** Detailed case studies of individual reserves

### Map Products

**Expected map outputs:**

1. **Overview Map:** All Indian tiger reserves with population change symbology
2. **Density Maps:** Kernel density heat maps (2006 baseline and 2022 current)
3. **Hot Spot Maps:** Statistical clustering analysis results
4. **Reserve Detail Maps:** Individual maps for 5-7 featured reserves
5. **Comparative Maps:** Side-by-side temporal comparisons
6. **Reference Maps:** Study area context with states and major features

**Symbology approach:**
- Green color scheme for success/growth
- Graduated colors for population categories
- Proportional symbols for point data
- Transparent overlays for density surfaces

---

## Project Timeline

### Phase 1: Data Collection (Weeks 1-2)
- [x] Download GBIF tiger occurrence data
- [x] Obtain WDPA reserve boundaries
- [x] Access NTCA census reports (2006, 2010, 2014, 2018, 2022)
- [x] Collect forest cover and elevation data
- [x] Gather reserve photographs (Creative Commons or official sources)

### Phase 2: Data Processing (Weeks 3-4)
- [x] Clean and filter occurrence data to study area and timeframe
- [x] Extract census data from NTCA reports to tabular format
- [x] Join temporal data to spatial boundaries
- [x] Create population trend tables and calculate growth statistics
- [x] Prepare all data in consistent projection and format

### Phase 3: Spatial Analysis (Week 5)
- [x] Perform kernel density analysis
- [x] Run hot spot analysis (Getis-Ord Gi*)
- [x] Calculate zonal statistics for habitat characterization
- [x] Generate reserve-level summary statistics
- [x] Create time-series visualizations

### Phase 4: Map Development (Week 6)
- [x] Design symbology and color schemes
- [x] Create web maps in ArcGIS Online
- [x] Configure popups and labels
- [x] Generate chart graphics
- [x] Prepare all map products

### Phase 5: Story Map Development (Week 7)
- [x] Write narrative text for all sections
- [x] Design Story Map layout and structure
- [x] Add maps, charts, and media
- [x] Integrate analysis results
- [x] Review and refine content

### Phase 6: Finalization (Week 8)
- [x] Test all interactive elements
- [x] Gather feedback from test audience
- [x] Make final revisions
- [x] Publish Story Map
- [x] Prepare final project report

---

## Success Criteria

This project will be considered successful if it:

1. ✅ Creates a functional, published ArcGIS Story Map accessible via web link
2. ✅ Clearly identifies and maps 5-7 tiger reserves with documented conservation success
3. ✅ Presents temporal population trend data (2006-2022) in clear visualizations
4. ✅ Demonstrates spatial analysis skills including density mapping and hot spot analysis
5. ✅ Provides meaningful insights about characteristics of successful tiger conservation
6. ✅ Tells a compelling, evidence-based story about conservation achievements
7. ✅ Includes properly cited data sources and methodology documentation

---

## Challenges and Limitations

### Anticipated Challenges

- **Data extraction complexity:** NTCA census data in PDF format requires manual extraction
- **Spatial data availability:** Detailed spatial data from NTCA may require formal requests
- **Data integration:** Combining temporal census counts with spatial occurrence points
- **Scale variation:** Census data at reserve level vs. point observations at specific locations

### Project Limitations

- **Temporal resolution:** Census data available only at 4-year intervals (not annual)
- **Spatial precision:** Census methods estimate populations within reserves, not exact locations
- **Verification status:** Community-sourced data (iNaturalist) may include unverified observations
- **Scope limitation:** Phase 1 focuses only on success stories, not comprehensive assessment

### Mitigation Strategies

- Supplement official census data with occurrence point data for spatial detail
- Clearly document data sources and quality levels
- Use multiple data sources to validate findings
- Design Story Map structure to allow future expansion with additional analyses

---

## References and Resources

### Primary Literature

- National Tiger Conservation Authority. (2023). *All India Tiger Estimation Report 2022*. Government of India.
- Jhala, Y. V., Qureshi, Q., & Nayak, A. K. (Eds.). (2020). *Status of Tigers, Copredators and Prey in India 2018*. National Tiger Conservation Authority & Wildlife Institute of India.

### Data Documentation

- GBIF.org. *Panthera tigris* occurrence records. https://www.gbif.org
- UNEP-WCMC and IUCN. (2023). *Protected Planet: The World Database on Protected Areas*. https://www.protectedplanet.net
- iNaturalist. Tiger observations. https://www.inaturalist.org

### GIS Resources

- Esri. *ArcGIS StoryMaps* documentation. https://doc.arcgis.com/en/arcgis-storymaps/
- Esri. *Kernel Density* tool reference. ArcGIS Pro documentation.
- Esri. *Hot Spot Analysis (Getis-Ord Gi*)* tool reference. ArcGIS Pro documentation.

---

## Contact Information

**Project Author:** Kiran Balasubramanian
**Institution/Affiliation:** GIS Course Project  
**Date Created:** February 4, 2026  
**Last Updated:** February 16, 2026

---

## Deviations from Original Proposal

This section documents decisions made during execution that differed from the original proposal. All deviations are recorded in full in `docs/methodology.md` Change Log and Decisions sections.

---

### 1. Protected Area Boundaries: WDPA → KBA Global Database

**Proposed:** WDPA via protectedplanet.net (UN Environment Programme)  
**Actual:** KBA Global Database, BirdLife International / KBA Partnership (February 2026), keybiodiversityareas.org  
**Reason:** KBA portal provided a more current dataset (September 2025 version) and cleaner polygon geometries for the Indian tiger reserves. WDPA and KBA share significant overlap in underlying data; the KBA source satisfied the same analytical requirements.

---

### 2. iNaturalist: Excluded from Analysis and Story Map

**Proposed:** iNaturalist as a primary supplementary data source combined with GBIF for density and distribution analysis  
**Actual:** iNaturalist data downloaded and processed (722 records after filtering) but excluded from all spatial analysis and Story Map content  
**Reason:** iNaturalist automatically offsets coordinates for threatened species by up to ~22 km (~0.2°). This coordinate obscuring makes records unsuitable for kernel density estimation, hot spot analysis, or reserve-level point counting. Merging with GBIF would have degraded GBIF dataset quality without analytical benefit. iNaturalist is not cited in the Story Map credits as it contributed no visible content.

---

### 3. GBIF Coordinate Uncertainty Threshold Relaxed

**Proposed:** Filter to records with coordinate uncertainty >1km excluded (i.e., accept only records with <1km uncertainty)  
**Actual:** Threshold relaxed to IS NOT NULL (any recorded uncertainty value accepted, no upper limit)  
**Reason:** At a 1km threshold, only 18 baseline records (2006–2010) remained — insufficient for kernel density estimation. Relaxing to IS NOT NULL recovered 116 baseline and 908 current-period records. Records with high uncertainty produce positional imprecision in KDE outputs but cluster correctly at reserve level for Summarize Within analysis. The 22km iNaturalist offset accepted for the narrative context layer set a precedent for the relaxed threshold. Full justification in methodology.md Decision 3.

---

### 4. Temporal Subsets Aligned to Census Windows

**Proposed:** Temporal subsets not explicitly defined in proposal  
**Actual:** GBIF occurrence data split into 2006–2010 (baseline) and 2018–2022 (current), aligned with NTCA census periods  
**Reason:** Census-aligned windows make the Story Map narrative directly comparable to NTCA population estimates. An earlier split of 2006–2012 / 2013–2022 was tested and rejected — it blurred two census cycles in the "current" layer. Full justification in methodology.md Decision 4.

---

### 5. Reserve Selection: Multi-Criterion Threshold vs. Top Quartile

**Proposed:** Identify reserves in the top quartile of population growth  
**Actual:** Multi-criterion threshold applied: primary criterion ≥50% growth (2006–2022), supporting criterion ≥50 tigers in 2022; Kanha and Kaziranga included on stability/density grounds  
**Reason:** With only N=6 comparable reserves (Kaziranga excluded from growth ranking due to missing 2006 baseline), a strict 75th percentile cutoff yielded only 2 reserves — insufficient for a 5–7 reserve Story Map. The multi-criterion approach preserved landscape diversity coverage (5 ecological zones) while maintaining analytical rigor. Full justification in methodology.md Decision 5.

---

### 6. Pench Treated as Single Combined Landscape

**Proposed:** Pench listed as a single reserve; state-split not discussed  
**Actual:** Formally documented as a single MP/Maharashtra combined landscape (Reserve_ID 4) throughout all spatial layers, population tables, and narrative  
**Reason:** NTCA census reports do not provide consistent state-level splits for Pench across all five census years. Population figures reflect the full trans-boundary survey area. Splitting would require proportional allocation not supported by source data.

---

### 7. Forest Cover: Zonal Statistics Replaced by ISFR 2021 Tabular Extraction

**Proposed:** Apply ArcGIS Zonal Statistics to extract forest cover within reserve boundaries  
**Actual:** Forest cover values obtained directly from ISFR 2021 Chapter 4 (Table 4.5), which provides VDF/MDF/OF measurements taken from digitized Tiger Reserve boundaries by FSI/WII  
**Reason:** ISFR 2021 Chapter 4 values are more accurate than a proxy zonal statistics approach on publicly available rasters, as they are measured from authoritative TR boundary digitizations not publicly available. Eliminated the need for FSI raster data request. ArcGIS Zonal Statistics for forest cover was removed from scope.

---

### 8. Kaziranga: No 2006 Baseline — Excluded from Growth Ranking

**Proposed:** All 7 reserves analyzed across full 2006–2022 period  
**Actual:** Kaziranga has no reserve-level NTCA estimate for 2006; baseline begins 2010. Excluded from percentage growth ranking; included in analysis on density/stability grounds (~8.8 tigers/100 km², among highest in world)  
**Reason:** No reserve-level data available in NTCA 2006 or 2010 reports; 2010 census was the first to provide a Kaziranga-specific figure. Kaziranga's conservation story is better told through density than growth rate.

---

### 9. Anticipated Finding Not Confirmed: Reserve Size Does Not Predict Success

**Proposed:** "Successful reserves likely to show larger protected area size (>500 km²)"  
**Actual:** Bubble chart analysis (reserve area vs. 2022 population, sized by growth rate) showed no clear relationship between reserve size and tiger population or growth rate. Kanha, the largest reserve at 2,072 km², has a smaller 2022 population than Corbett (400 km² smaller). Pench achieved the highest growth rate of any reserve at a moderate combined area.  
**Implication:** The key predictors of tiger recovery appear to be management intensity, prey biomass, and connectivity — not reserve area alone. This finding was featured in Section 6 of the Story Map.

---

### 10. Story Map Structure: 7 Sections vs. 6 Proposed Chapters

**Proposed:** 6-chapter structure (Introduction, Success Stories, Population Trends, Spatial Analysis, Comparative Analysis, Key Findings & Conclusion)  
**Actual:** 7-section structure with navigation (Introduction, The Overview Map, The Numbers, Where Tigers Are Detected, Reserve Profiles, What the Data Shows, Conclusion & Credits)  
**Reason:** Separating the Overview Map into its own section improved narrative flow — readers orient spatially before encountering data. "Comparative Analysis" and "Key Findings" were merged into "What the Data Shows" and "Conclusion" for tighter synthesis. Section names were also simplified for nav bar legibility.

---

### 11. KDE Comparison: Swipe Block vs. Side-by-Side Maps

**Proposed:** "Side-by-side comparison: 2006 vs 2022"  
**Actual:** ArcGIS StoryMaps Swipe block — single interactive element with draggable divider comparing baseline and current KDE rasters  
**Reason:** StoryMaps Swipe tool provides a more engaging and spatially precise comparison than static side-by-side maps, allowing readers to examine specific locations across both time periods simultaneously. Paragraphs updated to describe the swipe interaction.

---

### 12. Narrative Content: Two Political Sensitivity Revisions

**Kanha — Baiga village relocation:** Original draft included a paragraph acknowledging the contested history of tribal village relocations from Kanha's core zone in the 1970s. Revised to focus on institutional continuity and management longevity to avoid political framing in a conservation-focused Story Map.

**Pench — Kipling / *The Jungle Book*:** Original draft referenced Rudyard Kipling's *The Jungle Book* and its Seeonee/Pench connection. Revised to a conservation-focused landscape description due to concerns about centering a British colonial author in a narrative about Indian conservation achievement.

---

*This deviations section documents the gap between proposal and execution for academic transparency. All analytical decisions are justified in detail in `docs/methodology.md`.*

---

*This proposal outlines Phase 1 of a multi-phase tiger conservation mapping project. The modular design allows for future expansion to include corridor analysis, threat assessment, and regional deep dives while establishing a foundation with positive conservation success stories.*
