# Tiger Conservation Success Stories: India's Protected Areas (2006-2022)

An interactive web story analyzing spatial and temporal patterns of tiger population recovery in India's national parks and tiger reserves. Spatial analysis performed in ArcGIS Pro; presented as a free, permanent static site (Leaflet + Chart.js on GitHub Pages).

## Project Overview

This project examines tiger conservation success in India by mapping population changes across seven major protected areas from 2006 to 2022. Using official NTCA census data, GBIF occurrence records, and GIS spatial analysis, it identifies reserves with the strongest recovery trends and documents the habitat and management conditions associated with conservation success.

**[View Live Story](https://k-bsub.github.io/tiger-conservation-india/)**  
Live URL: https://k-bsub.github.io/tiger-conservation-india/

*Originally published as an ArcGIS Story Map (since rebuilt as a free, permanent static site — see [Phase 1b rebuild](docs/phase1b-storymap-rebuild-proposal.md)).*

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

## Story Contents

- 7 narrative sections with a sticky navigation bar
- 9 embedded interactive Leaflet maps (overview choropleth, KDE swipe comparison, hot spot analysis, 7 reserve detail maps via a shared reserve selector)
- 4 Chart.js charts (population trends, growth ranking, density comparison, area vs. population bubble chart)
- 22 photos across 8 slideshows, each with per-image caption and attribution
- Leaflet side-by-side swipe comparing 2006–2010 vs. 2018–2022 detection density
- Observer-bias note explaining GBIF spatial limitations

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

**Spatial analysis (Phase 1):**
- **ArcGIS Pro** — Spatial analysis, kernel density estimation, hot spot analysis (Getis-Ord Gi*), zonal statistics
- **Python** — Data processing automation
- **Microsoft Excel** — NTCA data extraction and tabular processing

**Presentation layer (Phase 1b rebuild):**
- **Leaflet.js** — Interactive maps (GeoJSON, `leaflet.markercluster`, `leaflet-side-by-side` swipe)
- **Chart.js** — Population trend and comparative charts
- **Hand-built HTML/CSS/JS** — Scrollytelling narrative shell
- **GitHub Pages** — Free, permanent static hosting

> The project was originally published as an ArcGIS Story Map (ArcGIS Online + ArcGIS StoryMaps). It was rebuilt on free, static infrastructure after the hosted feature services were suspended by an ArcGIS Online credit overdraft. See [docs/phase1b-storymap-rebuild-proposal.md](docs/phase1b-storymap-rebuild-proposal.md) for the full rationale.

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
│   ├── phase1b-storymap-rebuild-proposal.md   Static-site rebuild plan
│   └── symbology_scheme.html Web map symbology reference (WCAG AA compliant)
├── index.html                The story (landing page — narrative shell)
├── overview.html             Overview choropleth map
├── detections.html           Hot spot (Gi*) + GBIF points map
├── density.html              KDE swipe comparison map
├── reserves.html             Reserve detail map (selector; ?reserve=ID)
├── data/
│   ├── raw/                  Original downloaded datasets (not in repo -- see below)
│   ├── processed/            Extracted tables, cleaned datasets, and chart HTML
│   │   ├── tiger_population_2006_2022.xlsx
│   │   ├── forest/isfr_2021_reserve_corridors.xlsx
│   │   └── chart1–4_*.html   Chart.js charts embedded in the story
│   ├── *.geojson             Map layers (reserves, hotspot, GBIF points)
│   ├── kde_*_3857.png        KDE raster overlays for the swipe map
│   └── geodatabase/          ArcGIS Pro geodatabase (not in repo -- see below)
├── media/
│   ├── photos_processed/     22 reserve and tiger photos (CC BY-SA 4.0 / Unsplash)
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
4. View the [live story](https://k-bsub.github.io/tiger-conservation-india/)

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
*Originally published (ArcGIS Story Map): February 16, 2026*  
*Rebuilt as static site (GitHub Pages): June 2026*  
*Live: https://k-bsub.github.io/tiger-conservation-india/*
