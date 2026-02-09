# Forest Cover Data

Forest cover and tree cover data for tiger conservation analysis in India.

---

## Data Sources

### Primary Source: Global Forest Watch

**Dataset:** Tropical Tree Cover  
**Website:** https://www.globalforestwatch.org/  
**Download Date:** February 9, 2026  
**Data Year:** 2020  
**Coverage:** India

**Files Downloaded:**
- `Tropical_Tree_Cover_polygons.shp` (Shapefile format)
- `Tropical_Tree_Cover_polygons.geojson` (GeoJSON format)

**Spatial Characteristics:**
- **Resolution:** 30 meters
- **Format:** Vector polygons (106 polygons covering India)
- **Coordinate System:** WGS 1984 (EPSG:4326)
- **Source:** Hansen et al. Global Forest Change dataset

**Attributes:**
- Tree cover percentage
- Polygon area
- Data year (2020)

---

### Secondary Source: Forest Survey of India

**Reports Downloaded:**

#### India State of Forest Report (ISFR) 2021
- **Published:** 2022
- **Assessment Period:** 2019-2021
- **Publisher:** Forest Survey of India, Ministry of Environment, Forest and Climate Change
- **Download Date:** February 9, 2026
- **Files:** `*-2021.pdf`
- **Pages:** [total pages]
- **Website:** https://fsi.nic.in/

**Contains:**
- National forest cover statistics
- State-wise forest cover data
- Forest type classification maps
- Trends in forest cover change
- Tiger landscape assessments

#### India State of Forest Report (ISFR) 2017
- **Published:** 2017
- **Assessment Period:** 2015-2017
- **Publisher:** Forest Survey of India, Ministry of Environment, Forest and Climate Change
- **Download Date:** February 9, 2026
- **File:** `*-2017.pdf`
- **Website:** https://fsi.nic.in/

**Contains:**
- Baseline forest cover for 2018 tiger census comparison
- Historical forest cover trends
- State-wise analysis
- Forest density classification

---

## FSI Forest Classification System

Forest Survey of India classifies forests based on **canopy density:**

| Class | Canopy Density | Description |
|-------|----------------|-------------|
| **Very Dense Forest (VDF)** | >70% | Dense, closed canopy forest |
| **Moderately Dense Forest (MDF)** | 40-70% | Medium density forest |
| **Open Forest (OF)** | 10-40% | Sparse, open canopy forest |
| **Scrub** | <10% | Very sparse woody vegetation |
| **Non-Forest** | - | Other land uses |

**Minimum Mappable Unit:** 1 hectare  
**Mapping Scale:** 1:50,000  
**Satellite Data:** LISS-III (23.5m resolution)

---

## Data Coverage

### Geographic Extent

**States Covered:**
- Uttarakhand
- Uttar Pradesh
- Bihar
- Karnataka
- Kerala
- Tamil Nadu
- Assam
- Madhya Pradesh
- Maharashtra
- Rajasthan
- Odisha
- Chhattisgarh
- Telangana
- Andhra Pradesh

### Tiger Reserves Coverage

All 7 featured reserves have forest cover data:
- ✅ Jim Corbett National Park (Uttarakhand)
- ✅ Kaziranga National Park (Assam)
- ✅ Bandipur National Park (Karnataka)
- ✅ Nagarahole National Park (Karnataka)
- ✅ Kanha National Park (Madhya Pradesh)
- ✅ Pench Tiger Reserve (Madhya Pradesh/Maharashtra)
- ✅ Ranthambore National Park (Rajasthan)

---

## File Organization
```
data/raw/forest/
├── global_forest_watch/
│   ├── Tropical_Tree_Cover_polygons.shp
│   ├── Tropical_Tree_Cover_polygons.shx
│   ├── Tropical_Tree_Cover_polygons.dbf
│   ├── Tropical_Tree_Cover_polygons.prj
│   ├── Tropical_Tree_Cover_polygons.geojson
│   └── metadata.xml
├── fsi_reports/
│   ├── *-2021.pdf
│   └── *-2017.pdf
└── README.md (this file)
```

---

## Data Quality Assessment

### Global Forest Watch Data

**Strengths:**
- ✅ High spatial resolution (30m)
- ✅ Consistent global methodology
- ✅ Peer-reviewed dataset (Hansen et al. 2013)
- ✅ Regularly updated
- ✅ Free and openly accessible
- ✅ Vector format - easy to use in GIS

**Limitations:**
- ⚠️ Tree cover ≠ forest cover (includes plantations, orchards)
- ⚠️ Data from 2020 (2 years before tiger census)
- ⚠️ No forest type classification (only tree cover presence)
- ⚠️ May include non-native plantations
- ⚠️ Cloud cover can affect tropical regions

**Accuracy:**
- Overall accuracy: ~85% (Hansen et al. 2013)
- Better in dry deciduous forests
- Lower accuracy in dense evergreen forests

### FSI Reports

**Strengths:**
- ✅ Official government data - most authoritative
- ✅ Consistent methodology across India
- ✅ Detailed forest type classification
- ✅ Distinguishes forest density classes
- ✅ State-wise detailed analysis
- ✅ Biennial updates since 1987
- ✅ Ground-truthed data

**Limitations:**
- ⚠️ Digital spatial data not publicly available (PDF only)
- ⚠️ 1-2 year lag between assessment and publication
- ⚠️ ISFR 2021 data collected 2019-2021 (before 2022 census)
- ⚠️ Requires georeferencing for spatial analysis
- ⚠️ Minimum mapping unit (1 ha) misses small patches

---

## Key Statistics from ISFR 2021

### National Forest Cover

- **Total Forest Cover:** 7,13,789 km² (21.71% of India)
- **Tree Cover:** 95,748 km² (2.91% of India)
- **Total Green Cover:** 8,09,537 km² (24.62% of India)

**Forest Density Distribution:**
- Very Dense Forest (VDF): 99,779 km² (14.00%)
- Moderately Dense Forest (MDF): 3,08,171 km² (43.17%)
- Open Forest (OF): 3,05,839 km² (42.83%)

### Forest Cover in Tiger States

**Top States by Forest Cover:**
1. Madhya Pradesh: 77,493 km² (25.11% of state area)
2. Arunachal Pradesh: 66,964 km²
3. Chhattisgarh: 55,717 km²
4. Odisha: 52,156 km²
5. Maharashtra: 50,778 km² (16.47% of state area)

**Project States:**
- Karnataka: 43,356 km² (22.62% of state area)
- Assam: 28,326 km² (36.10% of state area)
- Uttarakhand: 24,394 km² (45.44% of state area)
- Rajasthan: 16,767 km² (4.90% of state area)
- Uttar Pradesh: 16,583 km² (6.88% of state area)

### Forest Change (2019-2021)

- **Net Gain:** 2,261 km² (increase since ISFR 2019)
- **Major Gains:** Andhra Pradesh (+647 km²), Telangana (+632 km²)
- **Losses:** Some northeastern states due to shifting cultivation

---

## Usage in Tiger Project

### Applications

**Week 3-4: Data Processing**
- Import GFW shapefiles to geodatabase
- Clip to tiger reserve boundaries
- Reproject to WGS 1984 UTM Zone 43N
- Calculate forest statistics per reserve

**Week 5: Spatial Analysis**
- Use as covariate in tiger density models
- Overlay with tiger occurrence points
- Assess habitat quality (VDF = best tiger habitat)
- Calculate forest cover metrics:
  - Total forest area per reserve
  - Percentage forest cover
  - Forest density distribution

**Week 6-7: Visualization & Story Map**
- Background forest cover maps
- Habitat quality visualization
- Reserve landscape context
- Forest change trends (2017 vs 2021)

**Analysis Metrics:**
- Forest area within each reserve
- Forest density classes (VDF/MDF/OF)
- Correlation with tiger population density
- Habitat connectivity assessment

---

## Data Processing Workflow

**Planned for Week 3:**

1. **Import GFW Shapefile**
   - Add to ArcGIS Pro
   - Export to `tiger_project.gdb/Environmental_Data/Tree_Cover_India`

2. **Reproject**
   - Transform to WGS 1984 UTM Zone 43N
   - Match project coordinate system

3. **Clip to Study Area**
   - Extract forest cover for 7 featured reserves
   - Create reserve-specific forest layers

4. **Calculate Statistics**
   - Total forest area per reserve
   - Mean tree cover percentage
   - Forest fragmentation metrics

5. **Integrate FSI Data** (if needed)
   - Extract forest density classes from PDF maps
   - Georeference maps if digital data unavailable
   - Cross-validate with GFW data

6. **Export Processed Data**
   - Save to `data/processed/forest/`
   - Create summary tables
   - Document processing steps

---

## Citations

### For Global Forest Watch Data

**Full Citation:**
```
Hansen, M. C., P. V. Potapov, R. Moore, M. Hancher, S. A. Turubanova, 
A. Tyukavina, D. Thau, S. V. Stehman, S. J. Goetz, T. R. Loveland, 
A. Kommareddy, A. Egorov, L. Chini, C. O. Justice, and J. R. G. Townshend. 
2013. "High-Resolution Global Maps of 21st-Century Forest Cover Change." 
Science 342 (15 November): 850–53. 

Data available from: http://earthenginepartners.appspot.com/science-2013-global-forest
Accessed via Global Forest Watch: https://www.globalforestwatch.org/
```

**In-text citation:** (Hansen et al. 2013)

### For FSI Reports

**ISFR 2021:**
```
Forest Survey of India. (2022). India State of Forest Report 2021. 
Ministry of Environment, Forest and Climate Change, Government of India, 
Dehradun, Uttarakhand.
```

**ISFR 2017:**
```
Forest Survey of India. (2017). India State of Forest Report 2017. 
Ministry of Environment, Forest and Climate Change, Government of India, 
Dehradun, Uttarakhand.
```

**In-text citation:** (FSI 2022) or (FSI 2017)

### For Story Map

**Recommended attribution:**
```
"Forest cover data from Global Forest Watch (Hansen et al. 2013) and 
India State of Forest Reports 2017 & 2021 (Forest Survey of India)."
```

---

## Data Licensing

### Global Forest Watch

- **License:** Open access
- **Attribution:** Required (cite Hansen et al. 2013)
- **Commercial Use:** Allowed
- **Modification:** Allowed
- **Redistribution:** Allowed with attribution

### FSI Reports

- **License:** Government of India open data
- **Attribution:** Required (cite FSI and report year)
- **Commercial Use:** Generally allowed for research/education
- **Usage:** Public domain for non-commercial purposes
- **Redistribution:** PDF reports can be shared with attribution

---

## Known Data Gaps

### Missing Digital Data

- FSI digital spatial data (shapefiles/rasters) not publicly available
- Would need official request to FSI for vector/raster formats
- Current FSI data limited to PDF reports with static maps

### Temporal Alignment

- GFW data: 2020
- ISFR 2021 data: Collected 2019-2021
- Tiger census: 2021-2022
- **Gap:** ~1-2 years between forest and tiger data

### Classification Differences

- GFW: Binary tree cover (present/absent)
- FSI: Four-class density (VDF/MDF/OF/Scrub)
- Not directly comparable - complementary datasets

---

## Future Data Needs

**For enhanced analysis:**

- [ ] FSI digital spatial data (official request)
- [ ] Forest type classification (sal, teak, evergreen, etc.)
- [ ] NDVI (vegetation index) data from Landsat/Sentinel
- [ ] Forest fragmentation metrics
- [ ] Historical forest cover (2006, 2010, 2014) for trend analysis

**Potential sources:**
- ISRO Bhuvan portal
- National Remote Sensing Centre (NRSC)
- ESA Sentinel data
- NASA MODIS vegetation products

---

## Contact Information

### Global Forest Watch
- **Website:** https://www.globalforestwatch.org/
- **Contact:** https://www.globalforestwatch.org/help/contact-us
- **Forum:** https://groups.google.com/forum/#!forum/globalforestwatch

### Forest Survey of India
- **Address:** Kaulagarh Road, P.O. IPE, Dehradun - 248195, Uttarakhand
- **Phone:** +91-135-2224949, 2755826
- **Email:** fsi-dgfr@nic.in
- **Website:** https://fsi.nic.in/

**For FSI Digital Data Requests:**
- Contact FSI directly via email
- Specify: Research purpose, area of interest, data format
- Processing time: 1-4 weeks typically

---

## Version History

**Version 1.0** - February 9, 2026
- Initial data collection
- Downloaded GFW shapefiles and GeoJSON
- Downloaded ISFR 2021 and 2017 reports
- Created documentation

**Planned Updates:**
- Week 3: Process and import to geodatabase
- Week 3: Calculate reserve-specific statistics
- Week 5: Integration with tiger density models

---

## Notes

**Data Status:** Raw data collected, processing pending (Week 3)

**Priority:** Medium-High (needed for habitat analysis and density modeling)

**Next Steps:**
1. Import GFW shapefile to ArcGIS Pro (Week 3)
2. Clip to tiger reserve boundaries (Week 3)
3. Calculate forest statistics (Week 3)
4. Use as covariate in SECR models (Week 5)
5. Create forest cover visualizations (Week 6-7)

---

*Last Updated: February 9, 2026*  
*Compiled by: Kiran Balasubramanian*  
*Project: Tiger Conservation Success Stories in India (2006-2022)*