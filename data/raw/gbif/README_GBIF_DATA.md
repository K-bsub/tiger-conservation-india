# GBIF Tiger Occurrence Data - India

## Overview

This folder contains tiger (*Panthera tigris*) occurrence data downloaded from the Global Biodiversity Information Facility (GBIF) for India.

## Data Source

- **Source:** GBIF.org
- **Species:** *Panthera tigris* (Tiger)
- **Geographic scope:** India
- **Download date:** February 5, 2026
- **Query:** `scientificName='Panthera tigris' AND country='IN'`

## Files

### Data Files
- `tiger_india_2006_2022_YYYYMMDD_HHMMSS.csv` - Filtered tiger occurrences (2006-2022)
- `tiger_india_ALL_YEARS_YYYYMMDD_HHMMSS.csv` - Complete dataset (all years)
- `tiger_india_raw_YYYYMMDD_HHMMSS.json` - Raw GBIF API response

### Metadata
- `download_summary_YYYYMMDD_HHMMSS.json` - Download statistics and metadata
- `README.md` - This file

## Data Fields

Key fields in the CSV files:

- **gbifID** - Unique GBIF record identifier
- **taxonKey** - GBIF taxonomic key
- **scientificName** - Full scientific name with authority
- **species** - Species name (*Panthera tigris*)
- **subspecies** - Subspecies if identified
- **decimalLatitude/Longitude** - Geographic coordinates (WGS84)
- **coordinateUncertaintyInMeters** - Spatial accuracy estimate
- **country** - Country (India)
- **stateProvince** - Indian state/union territory
- **locality** - Specific location description
- **eventDate** - Date of observation/collection (YYYY-MM-DD)
- **year/month/day** - Parsed date components
- **basisOfRecord** - Type of record (HUMAN_OBSERVATION, MACHINE_OBSERVATION, etc.)
- **institutionCode** - Data provider institution
- **datasetName** - Source dataset
- **publisher** - Data publisher
- **license** - Data usage license

## Data Statistics

See `download_summary_*.json` for complete statistics including:
- Total number of records
- Date range coverage
- Number of states represented
- Records with/without coordinates
- Basis of record distribution

## Citation

When using this data, please cite:

```
GBIF.org (05 February 2026) GBIF Occurrence Download
https://doi.org/10.15468/dl.XXXXX
```

Replace XXXXX with the actual DOI from your download if available.

## Quality Notes

- Coordinate uncertainty varies from <1m to >100km
- Records include historical museum specimens and recent observations
- Some records may lack precise geographic coordinates
- Multiple data sources and collection methods are represented
- Review individual record metadata for quality assessment

## Data Usage

### Loading in Python

```python
import pandas as pd

# Load the filtered dataset (2006-2022)
df = pd.read_csv('tiger_india_2006_2022_20260205_082513.csv')

# Basic exploration
print(f"Total records: {len(df):,}")
print(f"Date range: {df['year'].min()}-{df['year'].max()}")
print(f"States: {df['stateProvince'].nunique()}")

# View top states
print(df['stateProvince'].value_counts())
```

### Loading in R

```r
library(readr)

# Load data
df <- read_csv("tiger_india_2006_2022_20260205_082513.csv")

# Summary
summary(df)
table(df$stateProvince)
```

## Known Issues

- Some records may have incomplete location information
- Historical records may have lower spatial precision
- Taxonomic identification varies by data source
- Not all observations have been verified by experts

## Updates

To download updated data, use the provided Python script:
```bash
python download_data.py
```

## License

Data is provided under various licenses by original publishers. Check the `license` field in individual records for specific terms. Most records are under CC BY 4.0 or CC BY-NC 4.0.

## Contact

For questions about this data:
- **GBIF Portal:** https://www.gbif.org/
- **GBIF Support:** https://www.gbif.org/contact
- **Species Page:** https://www.gbif.org/species/search?q=Panthera%20tigris

## Related Resources

- **IUCN Red List (Tigers):** https://www.iucnredlist.org/species/15955/214862019
- **GBIF API Documentation:** https://www.gbif.org/developer/occurrence
- **Tiger Conservation:** https://www.tigersforeverforum.org/

## Reproducing This Data

This dataset is not included in the repository due to size constraints.
To download the data yourself:

### Prerequisites
```bash
pip install requests pandas
```

### Download
```bash
cd data/raw/gbif
python download_data.py
```

This will download the latest GBIF data for tigers in India and save it
to this directory.

**Expected files:**
- `tiger_india_2006_2022_YYYYMMDD_HHMMSS.csv` (~4,000 records, ~2MB)
- `tiger_india_ALL_YEARS_YYYYMMDD_HHMMSS.csv` (~4,500 records, ~2.5MB)
- `download_summary_YYYYMMDD_HHMMSS.json` (metadata)

### Alternative: Use Provided Data
If you just want to explore the data without re-downloading:
- Contact [kbsub@umich.edu](mailto:kbsub@umich.edu) for access

---

*Data downloaded using GBIF API with scientific name query to ensure accurate species identification.*
