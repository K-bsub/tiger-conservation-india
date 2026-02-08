# Naming Conventions - Tiger Conservation Project

## Feature Classes

### Format
`Category_Description_Detail`

### Rules
- PascalCase (capitalize first letter of each word)
- No spaces
- Descriptive but concise
- Include date/version if temporal

## Categories

### Protected_Areas/
- `India_Tiger_Reserves` - All tiger reserves (620 features)
- `Reserve_Boundaries_Featured` - Selected 5-7 reserves for Story Map

### Tiger_Occurrences/
- `GBIF_Tiger_Points_Raw` - Unprocessed GBIF data
- `GBIF_Tiger_Points_Cleaned` - Filtered and validated
- `Tiger_Points_YYYY_YYYY` - Temporal subsets

### Environmental_Data/
- `SRTM_Elevation_India` - Elevation points/contours
- `Forest_Cover_India` - Forest boundaries

### Analysis_Results/
- `Density_YYYY_YYYY` - Kernel density results
- `Hotspot_Analysis_Results` - Statistical clustering
- `Reserve_Statistics` - Calculated metrics

## Rasters
- `Elevation_SRTM_30m` - DEM
- `Density_Raster_YYYY` - Density surfaces
- Format: `Type_Source_Resolution`

## Tables
- `Census_Population_Data` - NTCA census
- `Reserve_Attributes` - Calculated statistics
- `Growth_Statistics` - Temporal analysis

## Field Naming

### Standard Fields
- `Reserve_Name` - Protected area name
- `State_Name` - Indian state
- `Area_km2` - Area in square kilometers
- `Population_2022` - Tiger count
- `Established_Year` - Year designated

### Rules
- Use underscores for spaces
- Include units in name when relevant
- Year suffix for temporal data
- Consistent capitalization
