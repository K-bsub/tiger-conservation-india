# Project Geodatabase Structure

## Location
`data/geodatabase/tiger_project.gdb`

## Coordinate System
**WGS 1984 UTM Zone 43N (EPSG: 32643)**
- Projection: Transverse Mercator
- Units: Meters
- Suitable for accurate distance/area calculations in India

## Feature Datasets

### Protected_Areas
Protected area boundaries and reserves

**Current contents:**
- India_Tiger_Reserves (620 features)

### Tiger_Occurrences
Tiger sighting locations from various sources

**Current contents:**
- GBIF_Tiger_Points_Raw

### Environmental_Data
Elevation, terrain, forest cover

**Current contents:**
- (SRTM raster import pending — Week 3)
- FSI forest cover raster import pending (visualization layer — Week 3, optional)

### Analysis_Results
Outputs from spatial analyses

**Current contents:**
- (To be populated in Week 5)

## Naming Conventions
See `docs/naming-conventions.md` for detailed naming standards.

## Created
February 6, 2026
```

---

## Quick Summary

**What You've Accomplished:**

✅ **Organized geodatabase** with 4 feature datasets  
✅ **Set coordinate system** to UTM 43N (proper for India analysis)  
✅ **Imported tiger reserves** into Protected_Areas dataset  
✅ **Imported GBIF data** into Tiger_Occurrences dataset  
✅ **Established naming conventions** for consistency  
✅ **Documented structure** for reproducibility  
✅ **Forest cover data extracted** — ISFR 2021 Chapter 4 (reserve-boundary level, all 7 reserves)  
✅ **Tiger corridor data extracted** — ISFR 2021 Tables 4.9/4.10 (13 corridors, VDF/MDF/OF)  
✅ **ISFR 2017 district-level context** — retained as secondary/landscape source  

**Forest Cover Status: COMPLETE (tabular)**  
Reserve-level VDF/MDF/OF values and 2011→2021 change fully extracted from ISFR 2021.  
ArcGIS Zonal Statistics on FSI raster is **not required** for tabular analysis — only needed  
if a VDF/MDF/OF visualization layer is desired in the Story Map (deferred to Week 6, optional).  

**Ready for next steps:**
- Week 3: Process occurrence data; join NTCA census to reserve boundaries; import SRTM elevation
- Week 4: Build time-series population table; join ISFR 2021 forest stats to reserve attributes
- Week 5: Spatial analysis (kernel density, hot spots, reserve statistics)
- Week 6 (optional): Import FSI raster for forest visualization layer

---

## Commit to GitHub

**Summary:**
```
Add ISFR 2021 forest/corridor data; update geodatabase docs
```

**Description:**
```
- Extract reserve-boundary forest cover from ISFR 2021 Ch.4 Table 4.5
  (all 7 project reserves) — supersedes ISFR 2017 district-level proxy data
- Extract tiger corridor forest cover Tables 4.9/4.10 (13 corridors)
- Add isfr_2021_reserve_corridors.xlsx to data/processed/forest/
- Add isfr_2017_forest_cover.xlsx to data/processed/forest/ (context layer)
- Forest cover tabular extraction complete; ArcGIS Zonal Statistics deferred
  to Week 6 as optional visualization task only
- Update geodatabase docs: Environmental_Data contents and next-step notes
- Set coordinate system WGS 1984 UTM Zone 43N; PascalCase naming standard
