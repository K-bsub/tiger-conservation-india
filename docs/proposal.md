```markdown
# Project Proposal: Mapping Tiger Conservation Success in India's National Parks

**Author:** Kiran Balasubramanian 
**Date:** February 4, 2026  
**Course:** GIS Project  
**Project Type:** ArcGIS Story Map

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

- **Data Type:** Forest cover classification data and vegetation type maps
- **Access:** https://fsi.nic.in
- **Format:** Raster/vector spatial data
- **Status:** Publicly available

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

**May Require Request:**
- ⚠️ Detailed spatial data from NTCA (formal data request may be needed)
- ⚠️ High-resolution forest cover data (FSI may require registration)

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

#### Data Clipping

Forest cover and elevation rasters will be clipped to the extent of tiger reserves to improve processing efficiency and focus analysis on relevant areas.

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
- [ ] Download GBIF tiger occurrence data
- [ ] Obtain WDPA reserve boundaries
- [ ] Access NTCA census reports (2006, 2010, 2014, 2018, 2022)
- [ ] Collect forest cover and elevation data
- [ ] Gather reserve photographs (Creative Commons or official sources)

### Phase 2: Data Processing (Weeks 3-4)
- [ ] Clean and filter occurrence data to study area and timeframe
- [ ] Extract census data from NTCA reports to tabular format
- [ ] Join temporal data to spatial boundaries
- [ ] Create population trend tables and calculate growth statistics
- [ ] Prepare all data in consistent projection and format

### Phase 3: Spatial Analysis (Week 5)
- [ ] Perform kernel density analysis
- [ ] Run hot spot analysis (Getis-Ord Gi*)
- [ ] Calculate zonal statistics for habitat characterization
- [ ] Generate reserve-level summary statistics
- [ ] Create time-series visualizations

### Phase 4: Map Development (Week 6)
- [ ] Design symbology and color schemes
- [ ] Create web maps in ArcGIS Online
- [ ] Configure popups and labels
- [ ] Generate chart graphics
- [ ] Prepare all map products

### Phase 5: Story Map Development (Week 7)
- [ ] Write narrative text for all sections
- [ ] Design Story Map layout and structure
- [ ] Add maps, charts, and media
- [ ] Integrate analysis results
- [ ] Review and refine content

### Phase 6: Finalization (Week 8)
- [ ] Test all interactive elements
- [ ] Gather feedback from test audience
- [ ] Make final revisions
- [ ] Publish Story Map
- [ ] Prepare final project report

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
**Last Updated:** February 4, 2026

---

*This proposal outlines Phase 1 of a multi-phase tiger conservation mapping project. The modular design allows for future expansion to include corridor analysis, threat assessment, and regional deep dives while establishing a foundation with positive conservation success stories.*
```
