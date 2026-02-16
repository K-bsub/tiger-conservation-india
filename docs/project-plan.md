# Project Plan: Tiger Conservation Success Stories in India

**Project Title:** Identifying Conservation Success Stories: Spatial Analysis of Tiger Population Recovery in India's Protected Areas (2006-2022)

**Author:** Kiran Balasubramanian
**Start Date:** February 4, 2026  
**Target Completion:** April 2026 (8 weeks)  
**Last Updated:** February 16, 2026

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Goals and Objectives](#project-goals-and-objectives)
3. [Milestones and Timeline](#milestones-and-timeline)
4. [Detailed Task Breakdown](#detailed-task-breakdown)
5. [Resource Requirements](#resource-requirements)
6. [Risk Management](#risk-management)
7. [Quality Assurance](#quality-assurance)
8. [Progress Tracking](#progress-tracking)

---

## Project Overview

### Purpose

Create an ArcGIS Story Map that showcases India's tiger conservation success stories by analyzing spatial and temporal patterns in tiger populations across major national parks and reserves from 2006 to 2022.

### Scope

**Phase 1 (Current):** Focus on conservation success stories
- Identify 5-7 reserves with strong population recovery
- Analyze temporal trends (2006-2022)
- Map spatial distribution patterns
- Characterize successful habitat conditions

**Future Phases (Optional Expansion):**
- Phase 2: Corridor and connectivity analysis
- Phase 3: Threat assessment and human-wildlife interface
- Phase 4: Regional deep dives and case studies

### Deliverables

1. **Primary:** Published ArcGIS Story Map with interactive maps and visualizations
2. **Secondary:** Project documentation (proposal, methodology, data dictionary)
3. **Tertiary:** Geodatabase with processed data and analysis results
4. **Supporting:** GitHub repository with all project materials

---

## Project Goals and Objectives

### Primary Goal

Highlight successful tiger conservation efforts in India through spatial analysis and compelling visual storytelling.

### Specific Objectives

1. ✅ **Objective 1:** Compile and integrate tiger census data (2006-2022) for major reserves
2. ✅ **Objective 2:** Identify top-performing reserves based on population growth metrics
3. ✅ **Objective 3:** Create density and hot spot maps showing spatial distribution patterns
4. ✅ **Objective 4:** Analyze habitat characteristics of successful reserves
5. ✅ **Objective 5:** Develop interactive Story Map with clear narrative structure
6. ✅ **Objective 6:** Document methodology and make project reproducible

### Success Metrics

- Story Map published and accessible via public URL
- Minimum 5 reserves featured with complete data
- All maps include proper citations and sources
- Analysis reproducible from documented methodology
- Positive feedback from test audience (if applicable)

---

## Milestones and Timeline

### 8-Week Project Timeline

| Week | Milestone | Key Deliverables | Status |
|------|-----------|------------------|--------|
| **Week 1** | Project Setup & Initial Data Collection | GitHub repo, proposal, GBIF/WDPA data downloaded | ✅ Complete |
| **Week 2** | Complete Data Collection | All datasets acquired, NTCA data extracted | ✅ Complete |
| **Week 3** | Data Processing & Cleaning | Cleaned datasets, joined tables, organized geodatabase | ✅ Complete |
| **Week 4** | Advanced Data Prep | Time-series tables, spatial data ready for analysis | ✅ Complete |
| **Week 5** | Spatial Analysis | Density maps, hot spot analysis, statistics complete | ✅ Complete |
| **Week 6** | Map Development | Web maps created, symbology finalized, charts made | ✅ Complete |
| **Week 7** | Story Map Development | Narrative written, maps integrated, content complete | ✅ Complete |
| **Week 8** | Finalization & Publication | Story Map published, documentation complete, presentation ready | 🟢 In Progress |

**Status Legend:**
- 🟢 In Progress
- 🟡 At Risk
- 🔴 Blocked
- ✅ Complete
- ⚪ Not Started

---

## Detailed Task Breakdown

### Week 1: Project Setup & Initial Data Collection

**Goal:** Establish project infrastructure and begin data acquisition

#### Tasks

- [x] Create GitHub repository with proper structure
- [x] Write project proposal
- [x] Create project plan document
- [x] Set up local project folder structure
- [x] Create ArcGIS Pro project (.aprx)
- [x] Download GBIF tiger occurrence data
- [x] Download WDPA protected area boundaries
- [x] Set up project geodatabase in ArcGIS Pro
- [x] Begin collecting reserve photographs
  - Collected 24 photos from Creative Commons sources
  - Documented attribution in media/photo-attributions.md
  - Organized in media/photos/reserves/
  - Ready for Story Map development (Week 7)

**Deliverables:**
- ✅ GitHub repository initialized
- ✅ Proposal.md complete
- ✅ Project-plan.md complete
- ✅ ArcGIS Pro project created
- ✅ Initial datasets downloaded

**Time Estimate:** 12-15 hours

---

### Week 2: Complete Data Collection

**Goal:** Acquire all remaining datasets and complete data inventory

#### Tasks

- [x] Access NTCA census reports
- [x] Download iNaturalist data
- [x] Obtain Forest Survey of India data
- [x] Download SRTM elevation data
- [x] Get Natural Earth administrative boundaries
- [x] Download OpenStreetMap data
- [x] Create data inventory spreadsheet
- [x] Create data-sources.md documentation

**Deliverables:**
- ✅ All datasets downloaded and organized
- ✅ NTCA population data extracted to table
- ✅ Data inventory complete
- ✅ Data-sources.md documentation

**Time Estimate:** 15-18 hours

---

### Week 3: Data Processing & Cleaning

**Goal:** Clean, standardize, and prepare all datasets for analysis

#### Tasks

- [x] Set up project projection (WGS 1984 UTM Zone 43N)
- [x] Process GBIF occurrence data
- [x] Process iNaturalist data
- [x] Clean WDPA protected areas
- [x] Process census population data
- [x] Join census data to spatial boundaries
- [x] Clip elevation data
- [x] Process forest cover data *(COMPLETE — approach changed)*
- [x] Quality check all datasets

**Deliverables:**
- ✅ All datasets cleaned and in consistent projection
- ✅ Census data joined to reserve boundaries
- ✅ Occurrence points filtered and validated
- ✅ Geodatabase organized with feature datasets
- ✅ Data dictionary started

**Time Estimate:** 18-20 hours

---

### Week 4: Advanced Data Preparation

**Goal:** Create derived datasets and analysis-ready tables

#### Tasks

- [x] Create time-series population table
- [x] Identify top performing reserves
- [x] Create reserve profile data
- [x] Prepare occurrence data for density analysis
- [x] Extract elevation statistics
- [x] Join forest cover statistics to reserve boundaries *(data already available)*
- [x] Create analysis extent/mask
- [x] Set up feature class templates for results

**Deliverables:**
- ✅ Time-series table with growth calculations
- ✅ List of 5-7 featured reserves finalized
- ✅ Reserve profile data compiled
- ✅ Occurrence data organized by time period
- ✅ Habitat statistics joined to reserves
- ✅ Data dictionary updated

**Time Estimate:** 12-15 hours

---

### Week 5: Spatial Analysis

**Goal:** Complete all spatial analyses and generate analytical outputs

#### Tasks

- [x] Kernel Density Analysis - Baseline (2006-2010)
- [x] Kernel Density Analysis - Current (2018-2022)
- [x] Hot Spot Analysis (Getis-Ord Gi*)
- [x] Reserve-level statistics
- [x] Summary statistics
- [x] Comparative analysis
- [x] Validate analysis results
- [x] Create analysis results folder

**Deliverables:**
- ✅ Kernel density rasters (baseline and current)
- ✅ Hot spot analysis results
- ✅ Reserve statistics table complete
- ✅ Summary statistics compiled
- ✅ Chart graphics created
- ✅ Analysis results documented in methodology.md

**Time Estimate:** 15-18 hours

---

### Week 6: Map Development

**Goal:** Create all web maps and finalize cartographic design

#### Tasks

- [x] Design symbology scheme
- [x] Create Web Map 1: Overview Map
- [x] Create Web Map 2: Density Comparison
- [x] Create Web Map 3: Hot Spot Analysis
- [x] Create individual reserve maps
- [x] Create population trend chart
- [x] Create growth ranking chart
- [x] Create comparison infographics
- [x] Test all web maps
- [x] Export static map versions

**Deliverables:**
- ✅ Symbology guide documented
- ✅ 3+ web maps published to ArcGIS Online
- ✅ 5-7 individual reserve maps
- ✅ Chart graphics (2+ charts)
- ✅ Infographic elements created
- ✅ All maps tested and functional

**Time Estimate:** 18-20 hours

---

### Week 7: Story Map Development

**Goal:** Build and populate ArcGIS Story Map with narrative and visual content

#### Tasks

- [x] Create Story Map outline
- [x] Write narrative text
- [x] Source and prepare media
- [x] Build Story Map in ArcGIS StoryMaps
- [x] Add overview map section
- [x] Add population trends section
- [x] Add density comparison section
- [x] Add hot spot analysis section
- [x] Create reserve profile sections
- [x] Add comparative analysis section
- [x] Create conclusion section
- [x] Add interactive elements
- [x] Configure Story Map settings

**Deliverables:**
- ✅ Story Map outline complete
- ✅ All narrative text written
- ✅ Media collected and optimized
- ✅ Story Map built with all content
- ✅ Interactive elements functional

**Time Estimate:** 18-22 hours

---

### Week 8: Finalization & Publication

**Goal:** Review, refine, publish, and document final project

#### Tasks

- [ ] Internal review and testing
  - Read through entire Story Map
  - Check for typos and grammar
  - Verify all maps load correctly
  - Test all links and buttons
  - Check on different devices (desktop, tablet, mobile)
  - Test in different browsers (Chrome, Firefox, Safari)
- [ ] Gather feedback (if possible)
  - Share draft link with 2-3 reviewers
  - Request specific feedback on:
    - Clarity of narrative
    - Map effectiveness
    - Technical issues
  - Document feedback received
- [ ] Make revisions
  - Address feedback items
  - Fix any identified issues
  - Refine text as needed
  - Adjust map configurations if necessary
- [ ] Final content polish
  - Verify all data sources cited
  - Check image attributions
  - Proofread all text
  - Ensure consistent formatting
  - Verify color accessibility
- [ ] Publish Story Map
  - Change privacy setting to public
  - Generate shareable URL
  - Test public link
  - Update GitHub repository with Story Map URL
- [ ] Complete project documentation
  - Finalize methodology.md
  - Complete data-dictionary.md
  - Write final-report.md
  - Update README.md with project status
  - Add Story Map link to all relevant docs
- [ ] Organize GitHub repository
  - Ensure all files properly organized
  - Remove any temporary/test files
  - Verify .gitignore working correctly
  - Write descriptive commit messages
  - Update project status
- [ ] Create presentation materials (if needed)
  - Prepare slides summarizing project
  - Include key maps and findings
  - Add Story Map screenshots
  - Practice presentation
- [ ] Archive project files
  - Backup geodatabase
  - Export final web maps
  - Save ArcGIS Pro project package
  - Document software versions used
- [ ] Submit final deliverables
  - Share Story Map URL
  - Submit required documentation
  - Provide GitHub repository link
  - Include any supplementary materials

**Deliverables:**
- [ ] Published Story Map (public URL)
- [ ] Complete project documentation
- [ ] Organized GitHub repository
- [ ] Final report submitted
- [ ] Presentation ready (if required)

**Time Estimate:** 15-18 hours

---

## Resource Requirements

### Software and Tools

**Required:**
- ✅ ArcGIS Pro (licensed version)
- ✅ ArcGIS Online account (organizational or public)
- ✅ ArcGIS StoryMaps (included with ArcGIS Online)
- ✅ Microsoft Excel or Google Sheets (data management)
- ✅ Git/GitHub (version control)
- ✅ Text editor (VS Code, Sublime, or similar)

**Optional:**
- Adobe Illustrator/PowerPoint (infographic creation)
- Python 3.x with arcpy (automation, if needed)
- QGIS (backup/alternative GIS software)
- Jupyter Notebooks (data exploration)

### Data Storage

**Estimated Storage Needs:**
- Raw data: 2-5 GB (primarily rasters)
- Processed data: 1-2 GB
- Project files: 500 MB - 1 GB
- Media/images: 500 MB
- **Total: ~5-10 GB**

**Storage Locations:**
- Local machine: Primary working storage
- ArcGIS Online: Web maps and Story Map
- GitHub: Documentation and small files (use Git LFS for large files)
- External backup: Cloud storage (Google Drive, Dropbox)

### Time Commitment

**Total Estimated Hours:** 120-150 hours over 8 weeks
- **Average:** 15-19 hours per week
- **Peak weeks:** Weeks 3, 5, 6, 7 (20+ hours)
- **Lighter weeks:** Weeks 1, 8 (12-15 hours)

### Skills Required

**Essential:**
- ArcGIS Pro proficiency (intermediate level)
- Spatial analysis concepts
- Data management and cleaning
- Basic cartography and map design
- Technical writing

**Helpful:**
- Web GIS and ArcGIS Online
- Data visualization principles
- Story mapping and narrative structure
- Python/arcpy (for automation)
- Project management

---

## Risk Management

### Identified Risks and Mitigation Strategies

#### Risk 1: Data Availability Issues
**Risk Level:** 🟡 Medium

**Description:** NTCA detailed spatial data may require formal data request or may not be available in usable format

**Impact:** Could delay analysis or require alternative approach

**Mitigation:**
- Start with publicly available GBIF/iNaturalist data as backup
- Request NTCA data early in Week 2
- Have contingency plan to use occurrence points + published census numbers
- Document alternative approach in methodology if needed

**Status:** Monitoring

---

#### Risk 2: Data Processing Complexity
**Risk Level:** 🟡 Medium

**Description:** Extracting population data from PDF reports may be time-consuming; data standardization across sources may be challenging

**Impact:** Could extend Week 2-3 timeline by 5-10 hours

**Mitigation:**
- Allocate extra time in Weeks 2-3 for data wrangling
- Use PDF extraction tools (Tabula, Adobe Acrobat) to speed up process
- Focus on featured reserves only if time becomes constrained
- Document data quality issues clearly

**Status:** Monitoring

---

#### Risk 3: Technical Issues with ArcGIS Online/StoryMaps
**Risk Level:** 🟢 Low

**Description:** Web map publishing or Story Map platform issues could cause delays

**Impact:** Could delay Week 7-8 activities by 1-2 days

**Mitigation:**
- Test web map publishing early (Week 4)
- Familiarize with StoryMaps interface before Week 7
- Have backup static map versions ready
- Contact Esri support if issues arise
- Allow buffer time in Week 8 for troubleshooting

**Status:** Low priority

---

#### Risk 4: Scope Creep
**Risk Level:** 🟡 Medium

**Description:** Temptation to add more analyses or expand to additional reserves beyond Phase 1 scope

**Impact:** Could push timeline past 8 weeks or compromise quality of core deliverables

**Mitigation:**
- Strictly adhere to 5-7 featured reserves
- Document expansion ideas for future phases
- Prioritize core deliverables over "nice to have" elements
- Review scope weekly and adjust if needed
- Remember: better to do Phase 1 well than Phase 1-2 poorly

**Status:** Active management required

---

#### Risk 5: Time Management
**Risk Level:** 🟡 Medium

**Description:** Underestimation of time required for certain tasks; competing priorities with work/life

**Impact:** Could result in rushed final product or missed deadline

**Mitigation:**
- Build in 10-15% buffer time in estimates
- Track actual time spent vs. estimated
- Identify tasks that can be shortened if needed
- Communicate early if timeline at risk
- Focus on minimum viable product for Phase 1

**Status:** Active monitoring

---

#### Risk 6: Data Quality Issues
**Risk Level:** 🟢 Low

**Description:** Occurrence data may have inaccuracies, duplicates, or sparse coverage in some areas

**Impact:** Could affect reliability of density and hot spot analyses

**Mitigation:**
- Use multiple data sources (GBIF + iNaturalist)
- Apply strict quality filters (coordinate uncertainty, verification status)
- Cross-reference with published census data
- Document data limitations clearly in methodology
- Use conservative language in findings

**Status:** Low priority

---

### Risk Response Plan

**If timeline slips by >1 week:**
1. Reduce number of featured reserves from 7 to 5
2. Simplify Story Map design (fewer interactive elements)
3. Use pre-built templates where possible
4. Focus on core analyses (skip optional habitat characterization)

**If critical data unavailable:**
1. Pivot to occurrence data-only approach
2. Modify analysis methods accordingly
3. Adjust research questions if needed
4. Document limitations transparently

**If technical issues arise:**
1. Contact Esri support immediately
2. Use alternative tools (QGIS, Python, Excel)
3. Create static maps as fallback
4. Adjust deliverable format if necessary

---

## Quality Assurance

### Quality Checkpoints

#### Data Quality
- [ ] All datasets have complete metadata
- [ ] Projections verified and consistent
- [ ] No missing or null values in critical fields
- [ ] Data sources properly cited
- [ ] Processing steps documented

#### Analysis Quality
- [ ] Analysis parameters documented and justified
- [ ] Results validated against published literature
- [ ] Statistical significance verified where applicable
- [ ] No obvious errors or anomalies
- [ ] Methodology reproducible from documentation

#### Map Quality
- [ ] All maps have clear titles and legends
- [ ] Symbology appropriate and accessible
- [ ] Labels readable at intended scale
- [ ] Popups informative and accurate
- [ ] Maps load quickly (<5 seconds)
- [ ] Color schemes colorblind-friendly

#### Story Map Quality
- [ ] Narrative clear and engaging
- [ ] No spelling or grammar errors
- [ ] Data sources properly cited
- [ ] Images properly attributed
- [ ] All links functional
- [ ] Responsive design (works on mobile)
- [ ] Consistent formatting throughout

#### Documentation Quality
- [ ] All required documents complete
- [ ] Methodology sufficiently detailed for reproduction
- [ ] Data dictionary includes all fields
- [ ] References properly formatted
- [ ] GitHub repository well-organized
- [ ] README provides clear overview

### Review Process

**Self-Review Checklist** (Week 8):
1. Read Story Map start to finish
2. Click every interactive element
3. Verify every data citation
4. Check every image attribution
5. Test on 3 different devices
6. Proofread all documentation

**Peer Review** (Optional, Week 8):
- Share with 2-3 reviewers
- Provide specific feedback questions
- Allow 2-3 days for review
- Incorporate constructive feedback

**Final Review** (Week 8):
- Complete quality checklist
- Address all identified issues
- Verify submission requirements met
- Get approval for publication

---

## Progress Tracking

### Weekly Status Updates

**Week 1 Status** (Current)
- **Date:** February 4, 2026
- **Progress:** ✅ Complete
- **Completed:**
  - ✅ GitHub repository created
  - ✅ Proposal written
  - ✅ Project plan drafted
  - ✅ Setting up ArcGIS Pro project
  - ✅ Beginning data downloads
  - ✅ Download GBIF tiger occurrence data
  - ✅ Download WDPA protected area boundaries
  - ✅ Set up project geodatabase in ArcGIS Pro
- **In Progress:** None
- **Blockers:** None
- **Next Week Focus:** Complete all data collection
- **Notes:** Project off to good start. Need to prioritize NTCA data access early

---

**Week 2 Status**
- **Date:** February 8, 2026
- **Progress:** ✅ Complete
- **Completed:**
  - ✅ Access NTCA census reports
  - ✅ Download iNaturalist data
  - ✅ Obtain Forest Survey of India data
  - ✅ Download SRTM elevation data
  - ✅ Get Natural Earth administrative boundaries
  - ✅ Download OpenStreetMap data
  - ✅ Create data inventory spreadsheet
  - ✅ Create data-sources.md documentation
- **In Progress:** None
- **Blockers:** None
- **Next Week Focus:** Complete data processing
- **Notes:** All data downloads completed and documented

---

**Week 3 Status**
- **Date:** February 12, 2026
- **Progress:** ✅ Complete
- **Completed:**
  - ✅ Set up project projection (WGS 1984 UTM Zone 43N); geodatabase structure documented
  - ✅ Extracted forest cover data from ISFR 2021 Chapter 4 (Table 4.5) — reserve-boundary
    level VDF/MDF/OF for all 7 reserves, 2011 & 2021 assessments with decadal change
  - ✅ Extracted tiger corridor forest cover (Tables 4.9/4.10) — 13 corridors relevant
    to project reserves with VDF/MDF/OF breakdown
  - ✅ Extracted ISFR 2017 district-level data (6 state chapters) as landscape context layer
  - ✅ Forest cover tabular extraction COMPLETE — ArcGIS Zonal Statistics not required
    for analysis (deferred to Week 6 as optional visualization task)
  - ✅ Output files: `data/processed/forest/isfr_2021_reserve_corridors.xlsx`,
    `data/processed/forest/isfr_2017_forest_cover.xlsx`
  - ✅ GBIF/iNaturalist occurrence data processing
  - ✅ Clean WDPA protected areas
  - ✅ Process census population data
  - ✅ NTCA census data join to reserve boundaries
  - ✅ Clip elevation data
  - ✅ Quality check all datasets
- **In Progress:** None
- **Blockers:** None
- **Next Week Focus:** Time-series population table; join ISFR 2021 forest stats to
  reserve attributes in geodatabase; reserve profile compilation; SRTM import
- **Notes:** ISFR 2021 Chapter 4 supersedes ISFR 2017 as primary forest source.
  Ranthambore shows +177 sq km forest gain (2011→2021) — strongest conservation
  success narrative in dataset. Corbett shows anomalous −595 sq km likely due to
  boundary revision; flag for verification against NTCA shapefile.

---

**Week 4 Status**
- **Date:** February 14, 2026
- **Progress:** ✅ Complete
- **Completed:**
  - ✅ Create time-series population table
  - ✅ Identify top performing reserves
  - ✅ Create reserve profile data
  - ✅ Prepare occurrence data for density analysis
  - ✅ Extract elevation statistics
  - ✅ Join forest cover statistics to reserve boundaries
  - ✅ Create analysis extent/mask
  - ✅ Set up feature class templates for results
- **In Progress:** None 
- **Blockers:** None
- **Next Week Focus:** Run kernel density estimation (baseline 2006–2010 vs current 2018–2022), execute hot spot analysis (Getis-Ord Gi), complete reserve-level Summarize Within point counts, populate Reserve_Summary_Stats table, and verify Jim Corbett forest boundary anomaly before analysis
- **Notes:** Week 4 completed ahead of schedule. Three analytical decisions revised during prep: GBIF uncertainty filter relaxed from ≤10,000m to IS NOT NULL (18 baseline points insufficient for KDE); temporal subsets realigned to census windows (2006–2010 / 2018–2022); top reserve selection used multi-criterion threshold instead of strict quartile (N=6 too small for quartile method). Pench confirmed as single combined landscape throughout all layers. Tiger_Reserves_Full is now the master spatial layer carrying population + elevation + forest cover attributes. All Week 5 result templates in place — HotSpot_Tiger_GiStar FC, Reserve_Summary_Stats table, and Analysis Environments configured. Jim Corbett forest anomaly (−594 km² change) flagged for verification before narrative use.

---

**Week 5 Status**
- **Date:** February 15, 2026
- **Progress:** ✅ Complete
- **Completed:**
  - ✅ Kernel Density Analysis - Baseline (2006-2010)
  - ✅ Kernel Density Analysis - Current (2018-2022)
  - ✅ Hot Spot Analysis (Getis-Ord Gi*)
  - ✅ Reserve-level statistics
  - ✅ Summary statistics
  - ✅ Comparative analysis
  - ✅ Validate analysis results
  - ✅ Create analysis results folder
- **In Progress:** None
- **Blockers:** None
- **Next Week Focus:** Build web maps in ArcGIS Online (KDE comparison, hot spot, reserve choropleth), finalise symbology and popups for all 7 reserves, create supporting charts and infographics, and complete Story Map narrative outline before beginning content assembly
- **Notes:** Week 5 completed on schedule. Analysis produced clean results with two documented flags (Jim Corbett density and forest cover, both traced to KBA boundary mismatch — not data errors) and three unexpected findings worth featuring in the Story Map: Ranthambore as a dispersal source population for Rajasthan, Kaziranga operating at carrying capacity as a Northeast source reserve, and the inverse GBIF density/tiger density relationship at Ranthambore as a teachable observer-effort moment. Hot spot analysis confirmed statistically significant clusters at Kanha/Pench and Kaziranga at 25km distance band; zero hot spots within strict KBA polygon boundaries confirmed as GBIF observer bias, not absence of clustering — 50km buffer used as spatial filter throughout. ISA ERROR_000541 was non-fatal. Reserve_Summary_Stats table fully populated across all 31 fields.

---

**Week 6 Status**
- **Date:** February 15, 2026
- **Progress:** ✅ Complete
- **Completed:**
  - ✅ Design symbology scheme
  - ✅ Create Web Map 1: Overview Map
  - ✅ Create Web Map 2: Density Comparison
  - ✅ Create Web Map 3: Hot Spot Analysis
  - ✅ Create individual reserve maps
  - ✅ Create population trend chart
  - ✅ Create growth ranking chart
  - ✅ Create comparison infographics
  - ✅ Test all web maps
  - ✅ Export static map versions
- **In Progress:** None
- **Blockers:** None
- **Next Week Focus:** Build ArcGIS StoryMap — draft chapter structure and
  narrative outline first; write introduction, success stories overview, and
  7 reserve profile sections; integrate all web maps and chart images;
  add media (reserve photos from `media/photos/reserves/`); configure
  interactive elements and Story Map settings; complete data sources and
  credits section
- **Notes:** Week 6 completed on schedule. Key cartographic decisions: Terrain
  with Labels basemap selected for all reserve detail maps — eliminates need
  to publish SRTM raster to AGOL and provides superior terrain context for
  free. Nagarahole created as separate map (Option B, tighter zoom) rather
  than sharing the Bandipur landscape map — 6 distinct reserve maps total.
  Ranthambore Cold Spot cluster north of reserve (dense purple dots near
  Sawai Madhopur) retained intentionally — strongest visual illustration of
  GBIF observer-effort bias in the dataset; earmarked as Story Map teaching
  moment. Kaziranga map is the most visually distinctive of the set —
  Brahmaputra braided channels and amber fill make it immediately identifiable.
  Chart 4 (bubble) and Chart 3 (density) are bonus deliverables beyond the
  original Week 6 scope. All 4 charts ready for Story Map integration as
  static PNG exports or direct HTML embed if AGOL supports custom embeds.

---

**Week 7 Status**
- **Date:** February 16, 2026
- **Progress:** 🟢 In Progress
- **Completed:**
  - ✅ Create Story Map outline
  - ✅ Write narrative text
  - ✅ Source and prepare media
  - ✅ Build Story Map in ArcGIS StoryMaps
  - ✅ Add overview map section
  - ✅ Add population trends section
  - ✅ Add density comparison section
  - ✅ Add hot spot analysis section
  - ✅ Create reserve profile sections
  - ✅ Add comparative analysis section
  - ✅ Create conclusion section
  - ✅ Add interactive elements
  - ✅ Configure Story Map settings
- **In Progress:** None
- **Blockers:** None
- **Next Week Focus:** Internal review and testing across devices (desktop/tablet/mobile), gather feedback from 2–3 reviewers, make revisions based on feedback, final content polish (proofread all text, verify all map/chart captions, test all links), change privacy to Public and publish, complete project documentation (finalize methodology.md, write final-report.md), organize GitHub repository, archive project files
- **Notes:** Story Map is functionally complete with all content in place — 7 sections, 9 embedded maps, 4 charts, 8 photos (including 3-photo intro slideshow), interactive elements (accordion for observer bias note, buttons for methodology and NTCA reports), and full credits. Privacy currently set to Private — will publish publicly after Week 8 review and polish pass. All interactive elements tested and rendering correctly. Photo attributions verified — all images properly licensed (21 CC BY-SA 4.0 from Wikimedia Commons, 3 Unsplash free-to-use). iNaturalist removed from credits section as decided — data processed but not used in any analysis or visualization. Narrative incorporates all key findings from Week 5 analysis: Pench highest growth (133%), Ranthambore observer bias teaching moment, Kaziranga carrying capacity interpretation, Corbett density caveat flagged. Ready for Week 8 QA and publication.

---

**Week 8 Status**
- **Date:** February 16, 2026
- **Progress:** 🟢 In Progress
- **Completed:**
  - [ ] 
- **In Progress:**
  - [ ] 
- **Blockers:** 
- **Next Week Focus:** 
- **Notes:** 

---

### Overall Project Health

**Current Status:** 🟢 On Track

**Completion Percentage:** 87%

**Key Metrics:**
- Tasks completed: 65 / 75
- Milestones completed: 7 / 8 (Weeks 1 - 7 complete)
- Days remaining: 7
- Estimated hours used: ~128 / 146

**Traffic Light Status:**
- 🟢 Schedule: On track (forest data extraction ahead of original plan)
- 🟢 Scope: Well-defined; 7 reserves confirmed
- 🟢 Resources: Adequate
- 🟢 Data: Forest cover complete; population data complete
- 🟡 Risks: Corbett boundary anomaly needs verification

---

## Notes and Lessons Learned

### Week 1 Notes
- GitHub repository structure working well
- Documentation-first approach helpful for planning
- Need to front-load data discovery to avoid delays
- Completed all items

### Week 3 Notes
- ISFR 2021 Chapter 4 is a significantly better data source than originally planned —
  provides exact reserve-boundary measurements rather than district proxies
- ArcGIS Zonal Statistics for forest cover is no longer needed for tabular analysis;
  deferred to optional visualization task in Week 6
- Ranthambore shows forest GAIN (+177 sq km) alongside strong tiger population
  recovery — the most compelling conservation success story in the dataset
- Kaziranga corridor situation (eastern corridors at 11–18% forest) adds important
  threat/vulnerability context alongside its reserve-level success
- Flag: Jim Corbett −595 sq km forest change likely a boundary issue, not real loss
- Missing SRTM files added to the project

### Ongoing Observations
- [To be updated weekly]

### Ideas for Future Phases
- Add corridor connectivity analysis between reserves
- Include threat mapping (roads, settlements, land use change)
- Develop case studies for 2-3 reserves with detailed management history
- Add temporal animation showing population expansion
- Include prey species distribution if data available

---

## Contact and Communication

**Project Lead:** Kiran Balasubramanian

**Communication Plan:**
- Weekly status updates in this document
- GitHub commits with descriptive messages

**Support:**
- Esri Community Forums (technical issues)
- Course discussion board (if applicable)
- GIS Stack Exchange (general GIS questions)

---

## Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-02-04 | 1.0 | Initial project plan created 			  | Kiran Balasubramanian |
| 2026-02-05 | 1.1 | GBIF data related updates    			  | Kiran Balasubramanian |
| 2026-02-07 | 1.2 | WDPA data related updates    			  | Kiran Balasubramanian |
| 2026-02-07 | 1.3 | Geodatabase setup and download photos    | Kiran Balasubramanian |
| 2026-02-08 | 2.0 | Downloaded and processed NTCA data 	  | Kiran Balasubramanian |
| 2026-02-09 | 2.1 | Downloaded iNaturalist and Forest data	  | Kiran Balasubramanian |
| 2026-02-10 | 2.2 | Downloaded SRTM and Natural Earth boundaries data	  | Kiran Balasubramanian |
| 2026-02-11 | 2.3 | Downloaded OpenStreet data, and documented data inventory and sources	  | Kiran Balasubramanian |
| 2026-02-12 | 3.0 | Extracted ISFR 2021 Ch.4 forest cover (reserve-boundary level, all 7 reserves); extracted 13 tiger corridor data; updated Week 3 status; revised forest cover approach (Zonal Statistics deferred) | Kiran Balasubramanian |
| 2026-02-13 | 3.1 | Processed GBIF and iNaturalist data, cleaned WDPA protected areas, processed census population data and joined to spatial boundaries  | Kiran Balasubramanian |
| 2026-02-13 | 3.2 | Processed elevation data and performed quality checks  | Kiran Balasubramanian |
| 2026-02-14 | 4.0 | Completed all tasks from Week 4  | Kiran Balasubramanian |
| 2026-02-15 | 5.0 | Completed all tasks from Week 5  | Kiran Balasubramanian |
| 2026-02-16 | 6.0 | Completed all tasks from Week 6  | Kiran Balasubramanian |
| 2026-02-16 | 7.0 | Completed all tasks from Week 7  | Kiran Balasubramanian |

---

*This is a living document and will be updated throughout the project lifecycle. All major changes will be documented in the revision history.*
