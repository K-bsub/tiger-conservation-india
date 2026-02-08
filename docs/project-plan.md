# Project Plan: Tiger Conservation Success Stories in India

**Project Title:** Identifying Conservation Success Stories: Spatial Analysis of Tiger Population Recovery in India's Protected Areas (2006-2022)

**Author:** Kiran Balasubramanian
**Start Date:** February 4, 2026  
**Target Completion:** April 2026 (8 weeks)  
**Last Updated:** February 4, 2026

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
| **Week 2** | Complete Data Collection | All datasets acquired, NTCA data extracted | 🟢 In Progress |
| **Week 3** | Data Processing & Cleaning | Cleaned datasets, joined tables, organized geodatabase | ⚪ Not Started |
| **Week 4** | Advanced Data Prep | Time-series tables, spatial data ready for analysis | ⚪ Not Started |
| **Week 5** | Spatial Analysis | Density maps, hot spot analysis, statistics complete | ⚪ Not Started |
| **Week 6** | Map Development | Web maps created, symbology finalized, charts made | ⚪ Not Started |
| **Week 7** | Story Map Development | Narrative written, maps integrated, content complete | ⚪ Not Started |
| **Week 8** | Finalization & Publication | Story Map published, documentation complete, presentation ready | ⚪ Not Started |

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
- [ ] Download iNaturalist data
  - Search for tiger observations in India
  - Filter by research grade/verified
  - Export observation data
  - Document data quality notes
- [ ] Obtain Forest Survey of India data
  - Access forest cover maps
  - Download vegetation classification if available
  - Note data year and resolution
- [ ] Download SRTM elevation data
  - Access USGS Earth Explorer
  - Select tiles covering study area
  - Download 30m resolution (preferred) or 90m
  - Mosaic if multiple tiles needed
- [ ] Get Natural Earth administrative boundaries
  - Download India states and districts
  - Verify projection and attributes
- [ ] Download OpenStreetMap data
  - Use Geofabrik India extract or QuickOSM
  - Focus on roads and settlements
  - Extract relevant features only
- [ ] Create data inventory spreadsheet
  - List all datasets with source, date, format
  - Document any access limitations
  - Note processing requirements
- [ ] Create data-sources.md documentation
  - Full citations for all data
  - Access URLs and methods
  - Known issues or limitations

**Deliverables:**
- [ ] All datasets downloaded and organized
- [ ] NTCA population data extracted to table
- [ ] Data inventory complete
- [ ] Data-sources.md documentation

**Time Estimate:** 15-18 hours

---

### Week 3: Data Processing & Cleaning

**Goal:** Clean, standardize, and prepare all datasets for analysis

#### Tasks

- [ ] Set up project projection (WGS 1984 UTM Zone 43N)
  - Reproject all vector data
  - Define projection for raster data
- [ ] Process GBIF occurrence data
  - Import CSV to ArcGIS Pro
  - Display XY coordinates
  - Filter to valid coordinates only
  - Remove duplicate records
  - Filter to coordinate uncertainty <1km
  - Export to feature class
  - Create 2006-2012 and 2013-2022 subsets
- [ ] Process iNaturalist data
  - Similar cleaning steps as GBIF
  - Verify research grade observations
  - Check for duplicates with GBIF
  - Combine or keep separate (document decision)
- [ ] Clean WDPA protected areas
  - Select only tiger reserves from dataset
  - Verify reserve names match NTCA data
  - Standardize name field for joining
  - Calculate area in km²
  - Create unique reserve ID field
- [ ] Process census population data
  - Create standardized reserve name field
  - Verify spelling consistency
  - Structure as long-format table (Reserve, Year, Population)
  - Add growth calculation fields
- [ ] Join census data to spatial boundaries
  - Create relationship class or multiple joined layers
  - Verify all reserves have matching spatial data
  - Document any missing matches
- [ ] Clip elevation data
  - Mosaic SRTM tiles if needed
  - Clip to extent of tiger reserves + buffer
  - Verify no data values are set correctly
- [ ] Process forest cover data
  - Clip to study area
  - Reclassify if needed for analysis
  - Document classification scheme
- [ ] Quality check all datasets
  - Verify projections
  - Check for null values
  - Validate attribute accuracy
  - Document any issues in methodology.md

**Deliverables:**
- [ ] All datasets cleaned and in consistent projection
- [ ] Census data joined to reserve boundaries
- [ ] Occurrence points filtered and validated
- [ ] Geodatabase organized with feature datasets
- [ ] Data dictionary started

**Time Estimate:** 18-20 hours

---

### Week 4: Advanced Data Preparation

**Goal:** Create derived datasets and analysis-ready tables

#### Tasks

- [ ] Create time-series population table
  - Structure: Reserve | 2006 | 2010 | 2014 | 2018 | 2022
  - Calculate absolute change (2022 - 2006)
  - Calculate percent change ((2022-2006)/2006 * 100)
  - Calculate average annual growth rate
  - Rank reserves by growth metrics
- [ ] Identify top performing reserves
  - Select reserves in top quartile for percent growth
  - Verify data completeness for selected reserves
  - Create final list of 5-7 featured reserves
  - Document selection criteria
- [ ] Create reserve profile data
  - For each featured reserve compile:
    - Area (km²)
    - 2006 population
    - 2022 population
    - Growth rate
    - State/region
    - Establishment year
  - Add to attribute table or separate table
- [ ] Prepare occurrence data for density analysis
  - Create separate point layers by time period
  - 2006-2010 (baseline)
  - 2018-2022 (current)
  - Verify point counts sufficient for kernel density
- [ ] Extract elevation statistics
  - Run zonal statistics for each reserve
  - Calculate: min, max, mean, std dev elevation
  - Join results to reserve attributes
- [ ] Extract forest cover statistics
  - Calculate dominant forest type per reserve
  - Calculate percent forest cover
  - Join to reserve attributes
- [ ] Create analysis extent/mask
  - Buffer around study area for context
  - Create clipping boundary for maps
- [ ] Set up feature class templates for results
  - Hot spot analysis output
  - Density raster output
  - Summary statistics table

**Deliverables:**
- [ ] Time-series table with growth calculations
- [ ] List of 5-7 featured reserves finalized
- [ ] Reserve profile data compiled
- [ ] Occurrence data organized by time period
- [ ] Habitat statistics joined to reserves
- [ ] Data dictionary updated

**Time Estimate:** 12-15 hours

---

### Week 5: Spatial Analysis

**Goal:** Complete all spatial analyses and generate analytical outputs

#### Tasks

- [ ] Kernel Density Analysis - Baseline (2006-2010)
  - Input: occurrence points 2006-2010
  - Set appropriate search radius (test 10km, 20km, 30km)
  - Set cell size to 1km
  - Output to raster
  - Classify into 5-7 density classes
  - Document parameters used
- [ ] Kernel Density Analysis - Current (2018-2022)
  - Repeat above with 2018-2022 points
  - Use same parameters for consistency
  - Enable comparison between periods
- [ ] Hot Spot Analysis (Getis-Ord Gi*)
  - Input: occurrence points (full dataset or by period)
  - Test different distance bands
  - Identify statistically significant clusters
  - Generate confidence level outputs
  - Map hot spots, cold spots, and non-significant areas
- [ ] Reserve-level statistics
  - Calculate for each reserve:
    - Total occurrence points
    - Point density (points per 100 km²)
    - Tigers per 100 km² (from census)
    - Population rank
    - Growth rate rank
  - Add to attribute table
- [ ] Summary statistics
  - Calculate study area totals:
    - Total tiger population 2006 vs 2022
    - Overall percent change
    - Mean reserve growth rate
    - Range of growth rates
  - Create summary table for Story Map
- [ ] Comparative analysis
  - Create charts in Excel/Python:
    - Population trends line graph (5-7 reserves)
    - Growth rate bar chart (ranked)
    - Density comparison (2006 vs 2022)
    - Reserve size vs population scatter plot
  - Export as images for Story Map
- [ ] Validate analysis results
  - Check for outliers or errors
  - Verify statistical significance
  - Cross-reference with published literature
  - Document any unexpected findings
- [ ] Create analysis results folder
  - Export all analysis outputs
  - Save rasters with descriptive names
  - Export tables as CSV for backup
  - Screenshot key results

**Deliverables:**
- [ ] Kernel density rasters (baseline and current)
- [ ] Hot spot analysis results
- [ ] Reserve statistics table complete
- [ ] Summary statistics compiled
- [ ] Chart graphics created
- [ ] Analysis results documented in methodology.md

**Time Estimate:** 15-18 hours

---

### Week 6: Map Development

**Goal:** Create all web maps and finalize cartographic design

#### Tasks

- [ ] Design symbology scheme
  - Choose color palette (green theme for success)
  - Define classification breaks
  - Create legend graphics
  - Test color accessibility
  - Document color codes (RGB/Hex)
- [ ] Create Web Map 1: Overview Map
  - Add reserve boundaries
  - Symbolize by population growth category
  - Add labels for featured reserves
  - Set appropriate zoom levels
  - Configure popups with key statistics
- [ ] Create Web Map 2: Density Comparison
  - Add baseline density raster (2006-2010)
  - Add current density raster (2018-2022)
  - Set up swipe/slider tool if available
  - Or create side-by-side layout
  - Add reserve boundaries for context
- [ ] Create Web Map 3: Hot Spot Analysis
  - Add hot spot results layer
  - Symbolize by confidence level
  - Add occurrence points (optional)
  - Configure informative popups
- [ ] Create individual reserve maps
  - One detailed map per featured reserve (5-7 maps)
  - Show reserve boundary, density, key features
  - Add context layers (roads, settlements, terrain)
  - Configure zoom level to reserve extent
- [ ] Create population trend chart
  - Line graph showing 2006-2022 trends
  - Include 5-7 featured reserves
  - Label axes and lines clearly
  - Export as high-res image
- [ ] Create growth ranking chart
  - Horizontal bar chart
  - Rank reserves by % growth
  - Color code featured reserves
  - Export as image
- [ ] Create comparison infographics
  - 2006 vs 2022 total population
  - Top 3 reserves highlights
  - Key statistics callouts
  - Design in PowerPoint/Illustrator or similar
- [ ] Test all web maps
  - Verify popups display correctly
  - Check layer visibility at different scales
  - Test on mobile device if possible
  - Ensure fast loading times
- [ ] Export static map versions
  - Create PDF/PNG versions as backup
  - Save map layouts in ArcGIS Pro
  - Document map specifications

**Deliverables:**
- [ ] Symbology guide documented
- [ ] 3+ web maps published to ArcGIS Online
- [ ] 5-7 individual reserve maps
- [ ] Chart graphics (2+ charts)
- [ ] Infographic elements created
- [ ] All maps tested and functional

**Time Estimate:** 18-20 hours

---

### Week 7: Story Map Development

**Goal:** Build and populate ArcGIS Story Map with narrative and visual content

#### Tasks

- [ ] Create Story Map outline
  - Define chapter structure
  - Plan content flow
  - Identify map/chart placements
  - Sketch layout (paper or digital)
- [ ] Write narrative text
  - Introduction (2-3 paragraphs)
    - Tiger conservation context
    - Project Tiger history
    - Why this matters
  - Success Stories chapter (main content)
    - Overview of featured reserves
    - What makes them successful
    - Key statistics and highlights
  - Reserve profiles (5-7 sections)
    - Individual reserve stories
    - Specific achievements
    - Habitat characteristics
  - Conclusion (2 paragraphs)
    - Key takeaways
    - Conservation importance
    - Call to action
- [ ] Source and prepare media
  - Find tiger photos (with attribution)
  - Collect reserve photographs
  - Create or source icons
  - Verify all images are properly licensed
  - Resize images for web optimization
- [ ] Build Story Map in ArcGIS StoryMaps
  - Create new Story Map
  - Set up navigation structure
  - Add cover/title section with hero image
  - Insert introduction text
- [ ] Add overview map section
  - Embed Web Map 1 (Overview)
  - Add explanatory text
  - Configure map settings
  - Add legend if needed
- [ ] Add population trends section
  - Insert line graph chart
  - Add supporting text explaining trends
  - Include data source citation
- [ ] Add density comparison section
  - Embed Web Map 2 (Density)
  - Add before/after comparison text
  - Explain significance of spatial changes
- [ ] Add hot spot analysis section
  - Embed Web Map 3 (Hot Spots)
  - Explain clustering patterns
  - Discuss implications
- [ ] Create reserve profile sections
  - For each of 5-7 reserves:
    - Add reserve name heading
    - Insert individual reserve map
    - Add profile statistics (sidebar or cards)
    - Write 1-2 paragraph story
    - Add reserve photo
- [ ] Add comparative analysis section
  - Insert ranking bar chart
  - Add infographics
  - Include summary statistics
- [ ] Create conclusion section
  - Summarize key findings
  - Broader conservation implications
  - Acknowledgments
  - Data sources and credits
- [ ] Add interactive elements
  - Image carousels if multiple photos
  - Expandable text for details
  - Buttons or links to resources
- [ ] Configure Story Map settings
  - Set privacy to public/private as appropriate
  - Configure sharing options
  - Add metadata/tags
  - Set thumbnail image

**Deliverables:**
- [ ] Story Map outline complete
- [ ] All narrative text written
- [ ] Media collected and optimized
- [ ] Story Map built with all content
- [ ] Interactive elements functional

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
- **Notes:** Project off to good start. Need to prioritize NTCA data access early.

---

**Week 2 Status**
- **Date:** February 8, 2026
- **Progress:** 🟢 In Progress
- **Completed:**
  - ✅ Access NTCA census reports 
- **In Progress:**
  - 🟢 Download iNaturalist data
- **Blockers:** 
- **Next Week Focus:** 
- **Notes:** 

---

**Week 3 Status**
- **Date:** [To be updated]
- **Progress:** ⚪ Not Started
- **Completed:**
  - [ ] 
- **In Progress:**
  - [ ] 
- **Blockers:** 
- **Next Week Focus:** 
- **Notes:** 

---

**Week 4 Status**
- **Date:** [To be updated]
- **Progress:** ⚪ Not Started
- **Completed:**
  - [ ] 
- **In Progress:**
  - [ ] 
- **Blockers:** 
- **Next Week Focus:** 
- **Notes:** 

---

**Week 5 Status**
- **Date:** [To be updated]
- **Progress:** ⚪ Not Started
- **Completed:**
  - [ ] 
- **In Progress:**
  - [ ] 
- **Blockers:** 
- **Next Week Focus:** 
- **Notes:** 

---

**Week 6 Status**
- **Date:** [To be updated]
- **Progress:** ⚪ Not Started
- **Completed:**
  - [ ] 
- **In Progress:**
  - [ ] 
- **Blockers:** 
- **Next Week Focus:** 
- **Notes:** 

---

**Week 7 Status**
- **Date:** [To be updated]
- **Progress:** ⚪ Not Started
- **Completed:**
  - [ ] 
- **In Progress:**
  - [ ] 
- **Blockers:** 
- **Next Week Focus:** 
- **Notes:** 

---

**Week 8 Status**
- **Date:** [To be updated]
- **Progress:** ⚪ Not Started
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

**Completion Percentage:** 5%

**Key Metrics:**
- Tasks completed: 10 / ~80
- Milestones completed: 1 / 8
- Days remaining: 56
- Estimated hours used: 5 / 150

**Traffic Light Status:**
- 🟢 Schedule: On track
- 🟢 Scope: Well-defined
- 🟢 Resources: Adequate
- 🟢 Quality: Not yet assessed
- 🟡 Risks: Monitoring data availability

---

## Notes and Lessons Learned

### Week 1 Notes
- GitHub repository structure working well
- Documentation-first approach helpful for planning
- Need to front-load data discovery to avoid delays
- Completed all items

### Week 2 Notes
- Found all population numbers from NTCA and secondary source

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

**Project Advisor/Instructor:** [If applicable]

**Communication Plan:**
- Weekly status updates in this document
- GitHub commits with descriptive messages
- Reach out immediately if blocked >2 days

**Office Hours / Support:**
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
| | | | |

---

*This is a living document and will be updated throughout the project lifecycle. All major changes will be documented in the revision history.*
