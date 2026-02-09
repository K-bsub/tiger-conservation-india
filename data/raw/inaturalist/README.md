# iNaturalist Tiger Observations - India

Citizen science tiger observations from iNaturalist platform.

---

## Download Information

**Source:** iNaturalist (www.inaturalist.org)  
**Download Date:** February 8, 2026  
**Query Parameters:**
- **Species:** Panthera tigris (Tiger)
- **Location:** India
- **Quality Grade:** Research Grade
- **Date Range:** 2006-01-01 to 2022-12-31
- **Has Photos:** Yes
- **Captive:** Excluded

**Downloaded File:** `inaturalist_tiger_india_research_2006_2022.csv`

---

## Dataset Characteristics

### Summary Statistics

- **Total Observations:** 1037 records
- **Date Range:** Januar 12, 2006 to December 26, 2022
- **Observers:** [unique count] contributors
- **States Covered:** [list major states]
- **Average Positional Accuracy:** [value] meters

### Geographic Coverage

**States with Most Observations:**
1. Madhya Pradesh: 210 observations
2. Maharashtra: 140 observations
3. Rajasthan: 89 observations

**Reserves with Noted Observations:**
- Jim Corbett National Park: 9
- Kaziranga National Park: 3
- Bandipur National Park: 0
- Nagarhole National Park: 0
- Kanha National Park: 6
- Pench National Park: 12
- Ranthambore National Park: 5

---

## Data Quality Notes

### Quality Grade Breakdown

- **Research Grade:** 1037 observations
  - At least 2/3 of identifiers agree on species
  - Has date and location
  - Not captive/cultivated

### Known Issues

**Coordinate Obscuring:**
- iNaturalist automatically obscures coordinates for threatened species
- Tiger coordinates may be offset by up to 0.2 degrees (~22 km)
- **Impact:** Cannot use for precise location analysis
- **Use for:** General distribution, presence/absence only

**Positional Accuracy:**
- Range: 2 to 1000000 meters
- Records with accuracy >1000m: 564 (54.4%)
- **Recommendation:** Filter to <500m for spatial analysis

**Temporal Bias:**
- Most observations: 2022
- Sparse data before: 2006
- **Note:** More recent years have more observations (platform growth)

**Observer Bias:**
- Concentrated near: Roads, tourist areas, park gates
- Sparse in: Remote areas, conflict zones
- **Impact:** Not representative of actual tiger distribution

**Verification Status:**
- All observations are "Research Grade" = verified by community
- Some may still be misidentifications
- Cross-reference with photos when possible

### Data Limitations

**Not Suitable For:**
- ❌ Population density estimation
- ❌ Precise habitat modeling
- ❌ Movement/corridor analysis (coordinate obscuring)

**Suitable For:**
- ✅ Broad distribution patterns
- ✅ Presence/absence at district level
- ✅ Supplementing GBIF data
- ✅ Temporal trends (relative)
- ✅ Public engagement stories

---

## Data Processing

### Cleaning Steps Needed

1. **Remove Captive Animals:**
   - Filter: `captive_cultivated = FALSE`

2. **Remove Poor Coordinates:**
   - Filter: `positional_accuracy < 1000` meters
   - Remove records with NULL coordinates

3. **Temporal Filter:**
   - Keep: 2006-01-01 to 2022-12-31 (matches NTCA census period)

4. **Remove Duplicates:**
   - Same user, same location, same day
   - Keep most accurate observation

5. **Add Reserve Attribution:**
   - Spatial join with protected area boundaries
   - Identify which observations fall within reserves

### Processed Output

- **File:** `data/processed/inaturalist_tiger_cleaned.csv`
- **Expected records after cleaning:** 564

---

## Citation

**For iNaturalist Data:**
```
iNaturalist contributors. (2026). iNaturalist Research-grade Observations. 
Panthera tigris observations in India. iNaturalist.org. 
Occurrence dataset https://www.inaturalist.org accessed via 
iNaturalist.org on [download date].
```

**For Story Map:**

"Supplementary tiger observations from iNaturalist, a citizen science platform 
(www.inaturalist.org, accessed February 2026)."

---

## License

iNaturalist data is available under various Creative Commons licenses depending 
on individual observer choices. Most observations are CC-BY or CC-BY-NC.

**Usage Rights:**
- ✅ Use for non-commercial research
- ✅ Use for educational purposes
- ⚠️ Must attribute original observers when using specific observations
- ⚠️ Check individual licenses for commercial use

---

## Comparison with GBIF

**iNaturalist vs GBIF:**

| Aspect | iNaturalist | GBIF |
|--------|-------------|------|
| **Data Source** | Citizen scientists | Multiple institutions |
| **Verification** | Community consensus | Varies by source |
| **Temporal** | Mostly 2010+ | Includes historical |
| **Coordinate Quality** | Often obscured | Usually precise |
| **Photo Documentation** | Always has photos | Sometimes |
| **Quantity (India)** | Moderate | Higher |

**Recommendation:** Use GBIF as primary, iNaturalist as supplementary

---

## Contact

**iNaturalist Platform:**
- Website: https://www.inaturalist.org
- Help: https://www.inaturalist.org/pages/help
- Forum: https://forum.inaturalist.org

**Data Issues:**
- Report via iNaturalist platform
- Flag individual observations if needed

---

*Last Updated: February [date], 2026*  
*Downloaded for: Tiger Conservation Success Stories Project*

---

## Step 9: Quick Data Cleaning in Excel

### Basic Cleaning Steps

1. **Open CSV in Excel**

2. **Remove Captive Animals:**
   - Filter column `captive_cultivated`
   - Show only `FALSE` or blank

3. **Check Coordinate Quality:**
   - Add filter to `positional_accuracy`
   - Filter: Values < 1000 (meters)

4. **Remove Duplicates:**
   - Data → Remove Duplicates
   - Based on: `user_login`, `latitude`, `longitude`, `observed_on`

5. **Save Cleaned Version:**
   data/processed/inaturalist_tiger_cleaned.csv