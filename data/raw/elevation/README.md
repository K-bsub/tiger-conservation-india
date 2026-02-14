# SRTM Elevation Data

Digital Elevation Model (DEM) for tiger habitat analysis in India.

---

## Data Source

**Dataset:** Shuttle Radar Topography Mission (SRTM)  
**Version:** SRTM 1 Arc-Second Global  
**Source:** USGS Earth Explorer  
**Website:** https://earthexplorer.usgs.gov/  
**Download Date:** February 9–13, 2026 (13 core tiles Feb 9; 11 buffer tiles Feb 13)  
**Data Collection Date:** February 2000 (Shuttle mission)

---

## Dataset Characteristics

### Spatial Resolution

- **Horizontal Resolution:** 30 meters (~1 arc-second)
- **Vertical Accuracy:** ±16 meters (absolute)
- **Vertical Precision:** ±6 meters (relative)

### Coordinate System

- **Coordinate System:** Geographic (Lat/Long)
- **Datum:** WGS 1984 (EPSG:4326)
- **Vertical Datum:** EGM96 (Earth Gravitational Model 1996)
- **Units:** Meters above sea level

### Data Format

- **Format:** GeoTIFF
- **Bit Depth:** 16-bit signed integer
- **Compression:** LZW (if applicable)
- **NoData Value:** -32768

### Coverage

- **Geographic Extent:** 11°N to 31°N, 73°E to 95°E
- **Tile Size:** 1° × 1° (approximately 111 km × 111 km at equator)
- **Total Tiles:** 24 tiles (13 core + 11 additional for 50km buffer coverage)
- **Total File Size:** ~600 MB

---

## Tiles Downloaded

See `srtm_metadata/tile_index.txt` for complete list.

### Coverage by Reserve

| Reserve | Core Tiles | Buffer Tiles (50km) | Coverage |
|---------|------------|---------------------|----------|
| Jim Corbett NP | N29E078, N29E079, N30E078 | — | ✅ Complete |
| Kaziranga NP | N26E093, N26E094 | N26E092, N27E092, N27E093 | ✅ Complete |
| Bandipur NP | N11E076, N12E076 | N11E075, N12E075 | ✅ Complete |
| Nagarahole NP | N11E076, N12E076 | N11E075, N12E075 | ✅ Complete |
| Kanha NP | N22E080, N22E081 | N21E080, N21E081 | ✅ Complete |
| Pench TR | N21E079, N21E080 | N21E078, N22E078, N22E079 | ✅ Complete |
| Ranthambore NP | N26E076, N26E077 | N25E076 | ✅ Complete |

**Note:** Initial download (Feb 9) included 13 core tiles. Visual QC of 50km buffers
revealed gaps at western edges of Kaziranga, Bandipur/Nagarahole, Pench and southern
edges of Ranthambore/Kanha. 11 additional tiles downloaded Feb 13 to complete coverage.

---

## Data Quality Notes

### Strengths

- ✅ Global coverage with consistent quality
- ✅ High vertical accuracy for topographic analysis
- ✅ Freely available
- ✅ Well-documented and widely used
- ✅ Suitable for landscape-scale habitat modeling
- ✅ One-time acquisition = no temporal variability

### Limitations

**Data Voids:**
- ⚠️ Some areas have data gaps (lakes, steep terrain)
- ⚠️ Voids filled with interpolation in processed versions
- ⚠️ Check for voids in high-altitude areas

**Vegetation Bias:**
- ⚠️ Radar reflects off tree canopy, not ground
- ⚠️ Dense forest areas show canopy height, not terrain
- ⚠️ More accurate in open areas and sparse vegetation

**Age of Data:**
- ⚠️ Collected in 2000 (24 years old)
- ⚠️ Terrain changes from erosion, landslides minimal
- ⚠️ Good enough for long-term habitat characteristics

**Spatial Resolution:**
- ⚠️ 30m may be too coarse for micro-topography
- ⚠️ Good for regional/reserve-level analysis
- ⚠️ Cannot capture small terrain features (<30m)

---

## Processing Status

**Completed February 13, 2026:**

1. **✅ Mosaic Tiles** — 24 tiles → `SRTM_India_Mosaic` (WGS84, 16-bit signed)
2. **✅ Reproject** — `SRTM_India_UTM43N` (UTM 43N, 30m cell, bilinear resampling)
3. **✅ Buffer** — `Reserve_Buffer_50km` (Project_Reserves_Clean + 50km dissolved)
4. **✅ Clip to Study Area** — `SRTM_India_Clipped` (Extract by Mask)
5. **✅ NoData verified** — −32768 confirmed; statistics minimum > 0m
6. **✅ Coverage verified** — all 7 reserves confirmed

**Pending (Week 5):**

7. **⬜ Zonal Statistics** — MIN/MAX/MEAN/STD per reserve → `reserve_elevation_stats`
8. **⬜ Slope** — `slope_degrees.tif`
9. **⬜ Aspect** — `aspect.tif`
10. **⬜ Terrain Ruggedness Index (TRI)** — Focal Statistics STD 3×3 → `terrain_ruggedness.tif`
11. **⬜ Hillshade** — for Story Map visualization

---

## Usage in Tiger Project

### Spatial Analysis Applications

**Habitat Characterization:**
- Elevation range within each reserve
- Mean elevation per reserve
- Terrain complexity metrics

**Density Modeling:**
- Use as covariate in SECR models
- Tigers prefer certain elevation ranges
- Ruggedness affects prey distribution

**Visualization:**
- 3D terrain views of reserves
- Hillshade backgrounds for maps
- Topographic context for Story Map

**Corridor Analysis:**
- Assess terrain barriers to movement
- Identify valley corridors
- Evaluate connectivity feasibility

### Expected Elevation Ranges

**By Reserve (approximate):**
- Jim Corbett: 400m - 1,200m (Shivalik hills)
- Kaziranga: 40m - 80m (floodplain)
- Bandipur: 680m - 1,454m (Western Ghats)
- Nagarahole: 700m - 960m (Western Ghats)
- Kanha: 450m - 900m (Central Highlands)
- Pench: 400m - 620m (Central Highlands)
- Ranthambore: 250m - 520m (Aravalli range)

---

## Data Processing Workflow

**Planned for Week 3:**

### Step 1: Mosaic Tiles
```
Raster → Mosaic To New Raster
Input: All SRTM tiles
Output: india_elevation_30m.tif
Coordinate System: WGS 1984 UTM Zone 43N
```

### Step 2: Clip to Study Area
```
Extract by Mask
Input: Mosaicked elevation
Mask: Tiger reserve buffer (50km)
Output: elevation_study_area.tif
```

### Step 3: Derive Slope
```
Surface → Slope
Input: elevation_study_area.tif
Output: slope_degrees.tif
Z Factor: 1 (if in meters)
```

### Step 4: Derive Aspect
```
Surface → Aspect
Input: elevation_study_area.tif
Output: aspect.tif
```

### Step 5: Calculate TRI
```
Focal Statistics
Input: elevation_study_area.tif
Neighborhood: Rectangle 3x3
Statistic: STD (standard deviation)
Output: terrain_ruggedness.tif
```

### Step 6: Extract to Reserves
```
Zonal Statistics as Table
Zone: India_Tiger_Reserves
Value Raster: elevation_study_area.tif
Statistics: MIN, MAX, MEAN, STD
Output: reserve_elevation_stats.dbf
```

---

## Citation

**For SRTM Data:**
```
NASA Shuttle Radar Topography Mission (SRTM) (2013). 
Shuttle Radar Topography Mission (SRTM) Global. 
Distributed by OpenTopography. 
https://doi.org/10.5069/G9445JDF

Data accessed via USGS Earth Explorer, February 2026.
```

**Alternative citation:**
```
U.S. Geological Survey (2000). Shuttle Radar Topography Mission 
1 Arc-Second Global elevation data [Dataset]. U.S. Geological Survey. 
https://earthexplorer.usgs.gov/
```

**In-text:** (NASA SRTM 2013) or (USGS 2000)

**For Story Map:**
```
"Elevation data from NASA Shuttle Radar Topography Mission (SRTM), 
30-meter resolution, accessed via USGS Earth Explorer."
```

---

## Technical Specifications

### File Format Details

**GeoTIFF Tags:**
- ModelPixelScaleTag: 0.000277778, 0.000277778, 0
- ModelTiepointTag: 0, 0, 0, [Lon], [Lat], 0
- GeoKeyDirectoryTag: WGS84, Geographic

**Raster Statistics (typical):**
- Minimum: ~0m (sea level, if coastal)
- Maximum: ~2000-3000m (depending on area)
- Mean: Varies by region
- NoData: -32768

### Processing Notes

**Resampling Methods:**
- Upsampling: Bilinear interpolation
- Downsampling: Cubic convolution
- Do NOT use Nearest Neighbor (creates artifacts)

**Reprojection:**
- Always reproject before analysis
- Use Bilinear for continuous elevation
- Maintain cell size (30m → 30m)

---

## Known Issues & Solutions

### Issue 1: Data Voids

**Problem:** Black holes in DEM  
**Solution:** Use SRTM void-filled version or interpolate in ArcGIS  
**Tool:** Focal Statistics → Mean (3×3 neighborhood)

### Issue 2: Edge Mismatch

**Problem:** Tile edges don't align perfectly  
**Solution:** Use Mosaic To New Raster with BLEND mosaic method  

### Issue 3: File Size Too Large

**Problem:** Mosaicked DEM is huge  
**Solution:** Clip to buffered study area first, then mosaic only needed tiles

### Issue 4: Vertical Datum

**Problem:** Elevation values seem off  
**Check:** Ensure vertical datum is EGM96  
**Convert:** If needed, use transformation to local datum

---

## Alternative Data Sources

If SRTM doesn't meet needs:

### Higher Resolution Options

**ALOS PALSAR (12.5m):**
- URL: https://www.eorc.jaxa.jp/ALOS/en/aw3d30/
- Resolution: 12.5 meters
- Coverage: Global
- More recent (2006-2011)

**ASTER GDEM (30m):**
- URL: https://asterweb.jpl.nasa.gov/gdem.asp
- Resolution: 30 meters
- More recent than SRTM
- Higher vertical accuracy in some areas

**Cartosat DEM (India-specific):**
- Source: ISRO/NRSC
- Resolution: 10 meters
- India coverage
- May require official request

---

## Quality Control Checklist

- [x] All tiles downloaded successfully (24 tiles)
- [x] No corrupted files (check file sizes)
- [x] Tiles cover all 7 tiger reserves + 50km buffers
- [x] Coordinate system is WGS 1984 (raw); UTM 43N (processed)
- [x] NoData values properly defined (−32768)
- [x] Visual check: No obvious artifacts
- [x] Elevation values reasonable for region
- [x] Metadata documented

---

*Last Updated: February 13, 2026*