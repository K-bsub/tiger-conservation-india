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
- (To be populated in Week 2)

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

**Ready for next steps:**
- Week 2: Add NTCA census data (as tables)
- Week 3: Add elevation and forest data
- Week 5: Store analysis results

---

## Commit to GitHub

**Summary:**
```
Document geodatabase structure and naming conventions
```

**Description:**
```
- Create naming-conventions.md with standardized rules
- Document tiger_project.gdb structure
- Define 4 feature datasets: Protected_Areas, Tiger_Occurrences, Environmental_Data, Analysis_Results
- Set coordinate system to WGS 1984 UTM Zone 43N
- Establish PascalCase naming standard
- Update data README with geodatabase info
