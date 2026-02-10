# Administrative Boundaries - India

Administrative boundary data for reference and context in tiger conservation analysis.

---

## Data Sources

### Natural Earth Data

**Website:** https://www.naturalearthdata.com/  
**Download Date:** February 10, 2026  
**Scale:** 1:10,000,000 (1:10m - Large scale detail)  
**License:** Public Domain  

---

## Datasets Downloaded

### 1. Admin 0 - Countries

**File:** `ne_10m_admin_0_countries.zip`  
**Source:** https://www.naturalearthdata.com/downloads/10m-cultural-vectors/  
**Contains:** Country boundaries worldwide  
**Used for:** India country boundary  

**Attributes:**
- `ADMIN` - Country name
- `ISO_A2` - 2-letter country code (IN for India)
- `ISO_A3` - 3-letter country code (IND)
- `CONTINENT` - Continent name
- `REGION_UN` - UN region classification
- `SUBREGION` - Sub-region
- `POP_EST` - Population estimate
- `GDP_MD_EST` - GDP estimate (million USD)
- `NAME` - Short name

### 2. Admin 1 - States and Provinces

**File:** `ne_10m_admin_1_states_provinces.zip`  
**Source:** https://www.naturalearthdata.com/downloads/10m-cultural-vectors/  
**Contains:** State/province boundaries worldwide  
**Used for:** Indian state boundaries  

**Attributes:**
- `admin` - Country name (India)
- `name` - State/province name
- `name_en` - English name
- `type` - Administrative type
- `type_en` - Type in English (State, Union Territory)
- `region` - Region name
- `iso_3166_2` - ISO 3166-2 code (IN-XX)

**Indian States Included (36 total):**

**States (28):**
1. Andhra Pradesh
2. Arunachal Pradesh
3. Assam
4. Bihar
5. Chhattisgarh
6. Goa
7. Gujarat
8. Haryana
9. Himachal Pradesh
10. Jharkhand
11. Karnataka
12. Kerala
13. Madhya Pradesh
14. Maharashtra
15. Manipur
16. Meghalaya
17. Mizoram
18. Nagaland
19. Odisha
20. Punjab
21. Rajasthan
22. Sikkim
23. Tamil Nadu
24. Telangana
25. Tripura
26. Uttar Pradesh
27. Uttarakhand
28. West Bengal

**Union Territories (8):**
1. Andaman and Nicobar Islands
2. Chandigarh
3. Dadra and Nagar Haveli and Daman and Diu
4. Delhi
5. Jammu and Kashmir
6. Ladakh
7. Lakshadweep
8. Puducherry

### 3. Populated Places

**File:** `ne_10m_populated_places.zip`  
**Source:** https://www.naturalearthdata.com/downloads/10m-cultural-vectors/  
**Contains:** Major cities and towns  
**Used for:** Context and labeling in maps  

**Attributes:**
- `NAME` - City name
- `ADM0NAME` - Country
- `ADM1NAME` - State/province
- `POP_MAX` - Maximum population estimate
- `LATITUDE` - Latitude
- `LONGITUDE` - Longitude

---

## District Boundaries

**Source:** DataMeet India
**File:** `2011_Dist.shp`
**Download Date:** February 10, 2026  

**Characteristics:**
- **Total Districts:** 641
- **Attributes:** DISTRICT, ST_NM, censuscode
- **Projection:** WGS 1984

**Source-specific notes:**
- Repository for all spatial data.
- All datasets in this repository is shared under CC BY 4.0 license.
- India boundaries by DataMeet India community (CC BY 4.0)

---

## Coordinate System

### Source Projection

**All Natural Earth Data:**
- **Coordinate System:** WGS 1984 (Geographic Coordinate System)
- **WKID:** 4326
- **Linear Unit:** Degree
- **Angular Unit:** Degree
- **Prime Meridian:** Greenwich
- **Datum:** WGS 1984

### Project Projection (for analysis)

**Will reproject to:**
- **WGS 1984 UTM Zone 43N (EPSG: 32643)**
- Used for accurate area/distance calculations
- Matches other project datasets

---

## Data Quality Notes

### Strengths

- ✅ Public domain - no licensing restrictions
- ✅ Globally consistent dataset
- ✅ Well-maintained and regularly updated
- ✅ Clean topology - no gaps or overlaps
- ✅ Comprehensive attributes
- ✅ Widely used and trusted source
- ✅ Multiple scales available

### Limitations

**Generalization:**
- ⚠️ 1:10m scale = simplified boundaries
- ⚠️ Small-scale features removed
- ⚠️ Not suitable for cadastral/property-level mapping
- ⚠️ Good for regional/national scale analysis

**Disputed Boundaries:**
- ⚠️ International boundaries may not reflect official position
- ⚠️ Particularly: Kashmir region boundaries
- ⚠️ Use official Survey of India data for authoritative boundaries

**No District Level:**
- ⚠️ Natural Earth doesn't include Admin 2 for India
- ⚠️ Need supplementary source for districts

**Currency:**
- ⚠️ May not reflect very recent administrative changes
- ⚠️ Check version date (usually 1-2 years behind)

---

## Usage in Tiger Project

### Applications

**Reference Context:**
- State boundaries for maps
- Country outline for study area
- City locations for context

**Story Map:**
- Background boundaries
- State labels
- Major cities near reserves
- River systems context

**Analysis:**
- Clip data to India boundary
- Aggregate statistics by state
- Calculate reserves per state
- Regional grouping

**Spatial Joins:**
- Assign tiger occurrences to states
- Calculate populations by administrative unit
- State-level summaries for Story Map

---

## Data Processing

### Processed Datasets Created

**In geodatabase: `tiger_project.gdb/Reference/`**

1. **India_Boundary**
   - Single polygon of India
   - Extracted from Admin 0 countries
   - Projection: WGS 1984 UTM Zone 43N

2. **India_States**
   - 36 state/UT polygons
   - Extracted from Admin 1
   - Projection: WGS 1984 UTM Zone 43N
   - Attributes preserved

3. **India_Districts** (if obtained)
   - ~700+ district polygons
   - From supplementary source
   - Projection: WGS 1984 UTM Zone 43N

4. **Tiger_State_Boundaries**
   - Subset: Only states with tiger reserves
   - 14 states included
   - Used for focused mapping

5. **Major_Cities_India**
   - Populated places in India
   - Population > 100,000
   - For labeling and context

### States with Tiger Reserves

**14 states included in project:**
1. Uttarakhand (Jim Corbett)
2. Assam (Kaziranga)
3. Karnataka (Bandipur, Nagarahole)
4. Madhya Pradesh (Kanha, Pench)
5. Rajasthan (Ranthambore)
6. Maharashtra (Pench, Tadoba)
7. Uttar Pradesh (Dudhwa, Pilibhit)
8. Bihar (Valmiki)
9. West Bengal (Sundarbans)
10. Tamil Nadu (Mudumalai, Anamalai)
11. Kerala (Periyar, Wayanad)
12. Odisha (Similipal)
13. Chhattisgarh (Achanakmar)
14. Telangana (Kawal)

---

## Statistics

### India Overview

**From Natural Earth attributes:**
- **Area:** ~3,287,000 km²
- **Population (estimate):** ~1.4 billion
- **Capital:** New Delhi
- **Total States/UTs:** 36

### Tiger Reserve States

**Forest Cover (from ISFR 2021):**
- Madhya Pradesh: 77,493 km² forest
- Karnataka: 43,356 km² forest
- Uttarakhand: 24,394 km² forest
- Maharashtra: 50,778 km² forest
- Rajasthan: 16,767 km² forest
- Assam: 28,326 km² forest

---

## File Formats

### Shapefile Components

Each dataset includes:
- `.shp` - Geometry
- `.shx` - Shape index
- `.dbf` - Attribute table
- `.prj` - Projection information
- `.cpg` - Character encoding (UTF-8)
- `.xml` - Metadata (optional)

---

## Citations

### Natural Earth Data

**Full Citation:**
```
Natural Earth (2024). 1:10m Cultural Vectors. 
Free vector and raster map data at naturalearthdata.com. 
https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
```

**In-text:** (Natural Earth 2024)

**For Story Map:**
```
"Administrative boundaries from Natural Earth, a public domain map dataset 
(naturalearthdata.com, accessed February 2026)."
```

### District Data Citation

**DataMeet:**
```
DataMeet (2011). India Administrative Boundaries. 
GitHub repository: https://github.com/datameet/maps
License: CC BY 4.0
```

---

## License and Usage Rights

### Natural Earth

**License:** Public Domain  
**Usage:** Free for any use  
**Attribution:** Not required but appreciated  
**Modification:** Allowed  
**Commercial Use:** Allowed  

**Terms:**
- No restrictions on use
- No warranty provided
- Use at your own risk

### District Data

**DataMeet:** CC BY 4.0 (requires attribution)  

---

## Alternative Sources

If Natural Earth doesn't meet needs:

### GADM (Database of Global Administrative Areas)

**URL:** https://gadm.org/download_country.html  
**Resolution:** High detail (multiple levels)  
**Format:** Shapefile, GeoPackage  
**License:** Free for non-commercial use  

### India Census

**URL:** https://censusindia.gov.in/  
**Official:** Government of India  
**Data:** District and sub-district  
**Note:** May require navigation/request  

### OpenStreetMap

**URL:** https://download.geofabrik.de/asia/india.html  
**Format:** OSM, Shapefile  
**License:** ODbL (Open Database License)  
**Detail:** Very high detail  

---

## Quality Control Checklist

Before using data:

- [x] All shapefiles downloaded and extracted
- [x] Files open in ArcGIS Pro without errors
- [x] Coordinate system is WGS 1984 (EPSG:4326)
- [x] India boundary present and correct
- [x] All 36 states/UTs present
- [x] No missing geometries
- [x] Attribute table complete
- [x] State names spelled correctly
- [x] District data obtained (if needed)
- [x] Documentation complete

---

## Integration Notes

### Week 3 Processing

**Tasks:**
1. Import to geodatabase Reference feature dataset
2. Reproject to UTM Zone 43N
3. Filter to India only
4. Simplify attributes (keep essential fields)
5. Create state subset (14 tiger states)

### With Other Data

**Spatial Joins:**
- Tiger occurrences → States (which state?)
- Reserves → States (state assignment)
- Forest cover → States (forest by state)

**Clipping:**
- Use India boundary to clip national datasets
- Use state boundaries for state-specific maps

---

*Last Updated: February 10, 2026*  
*Downloaded for: Tiger Conservation Success Stories Project*  
*Source: Natural Earth Data (Public Domain)*