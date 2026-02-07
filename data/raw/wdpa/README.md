# WDPA / Key Biodiversity Areas Data

Protected areas dataset for India, downloaded from UN Biodiversity Lab / Key Biodiversity Areas portal.

---

## Download Information

| Attribute | Details |
|-----------|---------|
| **Source** | UN Biodiversity Lab / Key Biodiversity Areas |
| **Website** | http://www.keybiodiversityareas.org/ |
| **Download Date** | February 6, 2026 |
| **Downloaded By** | Kiran Balasubramanian |
| **Country** | India |
| **Format** | Shapefile |

---

## Dataset Details

### Files

**Raw Data (as downloaded):**
```
data/raw/wdpa/KBA_Data/KBAsGlobal_2025_September_02/
├── KBAsGlobal_2025_September_02_POL.shp
├── KBAsGlobal_2025_September_02_POL.shx
├── KBAsGlobal_2025_September_02_POL.dbf
├── KBAsGlobal_2025_September_02_POL.prj
```

**Processed Data:**
```
data/processed/india_kba.shp
```

### Coordinate System

**WGS 1984 (EPSG:4326)**
- Geographic Coordinate System
- Datum: WGS84
- Units: Decimal Degrees

---

## Dataset Characteristics

### Feature Counts

| Dataset | Feature Count |
|---------|--------------|
| Original Download | 620 protected areas |
| Tiger Reserves & National Parks | Filtered subset |
| Final Exported Dataset | 620 |

### Coverage

**Geographic Extent:**
- All of India
- Includes all states and union territories
- Comprehensive coverage of protected areas

**Types of Protected Areas Included:**
- National Parks
- Tiger Reserves
- Wildlife Sanctuaries
- Conservation Reserves
- Community Reserves
- Other protected designations

---

## Key Reserves Verified Present

All key tiger reserves verified in dataset:

### North India
- ✅ Jim Corbett National Park (Uttarakhand)
- ✅ Rajaji Tiger Reserve (Uttarakhand)
- ✅ Dudhwa Tiger Reserve (Uttar Pradesh)
- ✅ Ranthambore Tiger Reserve (Rajasthan)
- ✅ Sariska Tiger Reserve (Rajasthan)

### Central India
- ✅ Kanha National Park (Madhya Pradesh)
- ✅ Bandhavgarh National Park (Madhya Pradesh)
- ✅ Pench Tiger Reserve (Madhya Pradesh/Maharashtra)
- ✅ Satpura Tiger Reserve (Madhya Pradesh)

### South India
- ✅ Bandipur National Park (Karnataka)
- ✅ Nagarahole National Park (Karnataka)
- ✅ Bhadra Wildlife Sanctuary (Karnataka)
- ✅ Periyar Tiger Reserve (Kerala)
- ✅ Mudumalai National Park (Tamil Nadu)

### Northeast India
- ✅ Kaziranga National Park (Assam)
- ✅ Manas National Park (Assam)
- ✅ Nameri National Park (Assam)

### East India
- ✅ Sundarbans National Park (West Bengal)
- ✅ Similipal National Park (Odisha)

**Result:** No missing reserves from target list

---

## Data Processing

### Selection Criteria

Protected areas were filtered to focus on tiger reserves and national parks using:
```sql
-- Selection query used in ArcGIS Pro
NAME LIKE '%National Park%' OR 
NAME LIKE '%Tiger Reserve%' OR
NAME LIKE '%Wildlife Sanctuary%'
```

Alternative approach if needed:
- Manual selection by searching for known reserve names
- Selection by designation type field (if available)
- Selection by IUCN category

### Processing Steps

1. **Downloaded** data from UN Biodiversity Lab portal
2. **Saved** to `data/raw/wdpa/kba_download/`
3. **Loaded** into ArcGIS Pro project
4. **Verified** India coverage (620 protected areas)
5. **Opened** attribute table and explored fields
6. **Selected** tiger reserves and national parks
7. **Verified** all key reserves present
8. **Exported** selection to `data/processed/india_kba.shp`
9. **Quality checked** final dataset

---

## Important Fields

### Attribute Table Structure

Key fields in the dataset (field names may vary):

| Field Name | Type | Description |
|------------|------|-------------|
| `NatName` or `IntName` | Text | Protected area name |
| `Country` | Text | Country code (IND) |
| `SiteAreaKM2` | Number | Area in square kilometers |
| `IbaStatus` | Text | Protection status |

---

## Data Quality

### Strengths
- ✅ Comprehensive coverage of India's protected areas (620 sites)
- ✅ All major tiger reserves present
- ✅ Standard coordinate system (WGS 1984)
- ✅ Well-maintained international database
- ✅ Regular updates from authoritative sources

### Limitations
- ⚠️ Protected area boundaries may be approximate
- ⚠️ Name variations may exist (e.g., "National Park" vs "Tiger Reserve")
- ⚠️ Data version dependent on download date
- ⚠️ May not include very recent designation changes
- ⚠️ Some smaller protected areas may be missing

### Notes
- Dataset is suitable for broad-scale analysis
- For precise legal boundaries, consult official government sources
- Cross-reference with NTCA official lists for tiger reserve specifics

---

## Citation

BirdLife International (2026). The World Database of Key Biodiversity Areas. 
Developed by the KBA Partnership: BirdLife International, International Union 
for the Conservation of Nature, Amphibian Survival Alliance, Conservation 
International, Critical Ecosystem Partnership Fund, Global Environment 
Facility, NatureServe, Rainforest Trust, Royal Society for the Protection 
of Birds, Wildlife Conservation Society and World Wildlife Fund. 
February 2026 version. Downloaded from http://www.keybiodiversityareas.org/ 
on February 6, 2026.

**For maps and publications, use:**
Data source: UN Biodiversity Lab / Key Biodiversity Areas (2026)

---

## License and Usage

### Usage Rights
- ✅ Free for non-commercial use
- ✅ Academic research permitted
- ✅ Educational use permitted
- ⚠️ Attribution required
- ⚠️ Check website for commercial use restrictions

### Attribution Requirements
- Credit the KBA Partnership
- Include citation in all publications
- Reference the download date and version

---

## Related Data

### Complementary Datasets Used in Project

| Dataset | Purpose | Location |
|---------|---------|----------|
| **GBIF Tiger Occurrences** | Tiger sighting locations | `data/raw/gbif/` |
| **NTCA Census Data** | Population counts | `data/raw/ntca/` |
| **SRTM Elevation** | Terrain analysis | `data/raw/elevation/` |
| **Forest Cover** | Habitat characterization | `data/raw/forest/` |

---

## Contact and Support

### Data Provider
- **Organization:** UN Environment Programme World Conservation Monitoring Centre (UNEP-WCMC)
- **Website:** http://www.keybiodiversityareas.org/
- **Support:** Contact through website for data questions

### Project Contact
- **Researcher:** Kiran Balasubramanian
- **Project:** Tiger Conservation Success Stories in India
- **Date:** February 7, 2026

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-02-06 | 1.0 | Initial download from UN Biodiversity Lab |
| | | 620 protected areas for India |
| | | All key tiger reserves verified present |

---

## Next Steps

### Planned Processing
- [ ] Cross-reference reserve names with NTCA census data
- [ ] Calculate area statistics for featured reserves
- [ ] Reproject to UTM Zone 43N for analysis
- [ ] Create subset of 5-7 featured reserves
- [ ] Join population data from NTCA reports

### Integration with Project
- Week 2: Match reserve names to census data
- Week 3: Clean and standardize attributes
- Week 4: Prepare for spatial analysis
- Week 6: Use in web maps
- Week 7: Feature in Story Map

---

## Troubleshooting

### Common Issues

**Issue:** Cannot find specific reserve
- **Solution:** Try alternate name spellings, check NAME field variations

**Issue:** Coordinate system mismatch
- **Solution:** Original data is WGS 1984, reproject to UTM 43N for analysis

**Issue:** Boundary seems incorrect
- **Solution:** KBA boundaries are approximate, verify with official sources if critical

**Issue:** Need more recent data
- **Solution:** Re-download from KBA portal, check for updates

---

## References

### Documentation
- KBA Data Standards: http://www.keybiodiversityareas.org/kba-data
- WDPA User Manual: https://www.protectedplanet.net/en/resources/wdpa-manual
- Protected Planet: https://www.protectedplanet.net/

### Related Resources
- National Tiger Conservation Authority: https://ntca.gov.in/
- Wildlife Institute of India: https://wii.gov.in/
- Forest Survey of India: https://fsi.nic.in/

---

*Last updated: February 7, 2026*  
*For project: Tiger Conservation Success Stories (2006-2022)*  
*Repository: github.com/K-bsub/tiger-conservation-india*
