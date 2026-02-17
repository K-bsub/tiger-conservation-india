# Tiger Conservation Success Stories: India's Protected Areas (2006-2022)

An ArcGIS Story Map analyzing spatial and temporal patterns of tiger population recovery in India's national parks and tiger reserves.

## Project Overview

This project examines tiger conservation success in India by mapping population changes across seven major protected areas from 2006 to 2022. Using official NTCA census data, GBIF occurrence records, and GIS spatial analysis, it identifies reserves with the strongest recovery trends and documents the habitat and management conditions associated with conservation success.

**[View Live Story Map](https://arcg.is/00bXi44)**  
Full URL: https://storymaps.arcgis.com/stories/c9e21879e1b2483e81fc79fd357c59b2

India's national tiger population grew from ~1,411 tigers in 2006 to 3,682 in 2022 — a 161% increase over 16 years. The seven featured reserves demonstrate that this recovery spans five distinct ecological landscapes.

## Key Results

| Reserve | 2006 | 2022 | Growth |
|---|---|---|---|
| Pench TR (Combined) | 33 | 77 | +133% |
| Bandipur NP | 68 | 150 | +121% |
| Nagarahole NP | 78 | 141 | +81% |
| Ranthambore TR | 32 | 57 | +78% |
| Jim Corbett NP | 164 | 260 | +58% |
| Kanha NP | 89 | 105 | +18% |
| Kaziranga NP | 103 (2010) | 104 | stable |

## Story Map Contents

- 7 narrative sections with navigation
- 9 embedded web maps (overview choropleth, KDE swipe comparison, hot spot analysis, 6 reserve detail maps)
- 4 charts (population trends, growth ranking, density comparison, area vs. population bubble chart)
- 24 photos across 8 slideshows
- Interactive Swipe block comparing 2006-2010 vs. 2018-2022 detection density
- Observer bias accordion explaining GBIF spatial limitations

## Study Area

Seven tiger reserves across five ecological landscapes:

| Reserve | State | Landscape |
|---|---|---|
| Jim Corbett NP | Uttarakhand | Himalayan Terai-Bhabar |
| Kaziranga NP | Assam | Brahmaputra Alluvial Floodplain |
| Bandipur NP | Karnataka | Western Ghats |
| Nagarahole NP | Karnataka | Western Ghats |
| Kanha NP | Madhya Pradesh | Central Indian Sal-Bamboo |
| Pench TR (Combined) | MP / Maharashtra | Central Indian Sal-Teak |
| Ranthambore TR | Rajasthan | Semi-Arid Aravalli |

## Tools and Technologies

- **ArcGIS Pro** — Spatial analysis, kernel density estimation, hot spot analysis (Getis-Ord Gi*), zonal statistics
- **ArcGIS Online** — Web map hosting and publishing
- **ArcGIS StoryMaps** — Narrative presentation and interactive maps
- **Chart.js** — Population trend and comparative charts
- **Python** - Data processing automation
- **Microsoft Excel** — NTCA data extraction and tabular processing

## Repository Structure

```
tiger-conservation-india/
├── docs/
│   ├── proposal.md           Project proposal + deviations from original plan
│   ├── methodology.md        Full methods, decisions log, change log
│   ├── data-sources.md       Complete data inventory with citations
│   ├── naming-conventions.md Feature class and field naming standards
│   ├── references.md         Full bibliography
│   ├── final-report.md       Project final report
│   └── symbology_scheme.html Web map symbology reference (WCAG AA compliant)
├── data/
│   ├── raw/                  Original downloaded datasets (not in repo -- see below)
│   ├── processed/            Extracted tables and cleaned datasets
│   │   ├── tiger_population_2006_2022.xlsx
│   │   └── forest/isfr_2021_reserve_corridors.xlsx
│   └── geodatabase/          ArcGIS Pro geodatabase (not in repo -- see below)
├── media/
│   ├── photos/reserves/      24 reserve and tiger photos (CC BY-SA 4.0 / Unsplash)
│   ├── charts/               Chart PNG exports
│   └── photo-attributions.md Photo license documentation
└── README.md
```

**Note:** Large files (shapefiles, rasters, geodatabase) are not stored in this repository
due to size constraints. See `docs/data-sources.md` for download instructions to reproduce
the full dataset from publicly available sources.

## Data Sources

| Dataset | Source | License |
|---|---|---|
| Tiger population (2006-2022) | NTCA All India Tiger Estimation Reports | Govt. of India |
| Protected area boundaries | KBA Global Database, BirdLife International (Feb 2026) | Non-commercial |
| Tiger occurrences | GBIF.org (1,411 records after filtering) | CC BY 4.0 / CC0 |
| Forest cover | ISFR 2021 Chapter 4, Forest Survey of India | Govt. of India |
| Elevation | NASA SRTM 1 Arc-Second Global, USGS Earth Explorer | Public domain |
| Admin boundaries | Natural Earth; DataMeet India | Public domain / CC BY 4.0 |
| Roads and settlements | OpenStreetMap via Geofabrik | ODbL |

Full citations with access URLs, known issues, and reproduction instructions:
[docs/data-sources.md](docs/data-sources.md)

## Reproducing This Analysis

All data sources are publicly available. To reproduce from scratch:

1. Download all datasets following `docs/data-sources.md`
2. Create geodatabase at `data/geodatabase/tiger_project.gdb`
3. Follow processing steps in `docs/methodology.md` Section 4 (4.1 to 4.8)
4. Run spatial analyses per `docs/methodology.md` Section 5
5. All analytical decisions documented in `docs/methodology.md` Section 6

## Getting Started

1. Read the [project proposal](docs/proposal.md) for scope and objectives
2. See [methodology](docs/methodology.md) for full technical documentation
3. Read the [final report](docs/final-report.md) for results and findings
4. View the [live Story Map](https://arcg.is/00bXi44)

## Author

**Kiran Balasubramanian**
- Master's degree in Aerospace Engineering, University of Michigan, Ann Arbor
- Background in algorithms, data science, and physics-based models
- Learning spatial analysis and GIS applications
- Contact: [kbsub@umich.edu](mailto:kbsub@umich.edu)

## License

This project is licensed under the MIT License -- see LICENSE file for details.

Map content and visualizations: Creative Commons Attribution 4.0 International

## Acknowledgments

- National Tiger Conservation Authority for census data
- Wildlife Institute of India for research support and ISFR 2021 Chapter 4 data
- GBIF data contributors
- Photo contributors -- full attributions in [media/photo-attributions.md](media/photo-attributions.md)
- Conservation organizations and forest department staff protecting India's tigers

---

*Project Status: **Complete***  
*Story Map Published: February 16, 2026*  
*Last Updated: February 16, 2026*
