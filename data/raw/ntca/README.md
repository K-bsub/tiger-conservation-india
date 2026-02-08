# NTCA Tiger Census Data

Official tiger population estimates from National Tiger Conservation Authority and peer-reviewed research publications.

---

## Data Sources

### Primary Source: NTCA Census Reports

#### 2006 Census
- **Title:** Status of Tigers in India 2006
- **Published:** 2008
- **Authors:** Jhala, Y.V., Gopal, R., & Qureshi, Q. (Eds.)
- **Publisher:** National Tiger Conservation Authority, Govt. of India, New Delhi, and Wildlife Institute of India, Dehradun
- **Download Date:** February 8, 2026
- **Source URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/Statusof_Tigers2008.pdf
- **File:** `Tiger_Status_2006.pdf`
- **Total India Population:** ~1,411 tigers
- **Pages with reserve data:** Check each Region's summary.

#### 2010 Census
- **Title:** Status of Tigers, Co-predators and Prey in India 2010
- **Published:** 2011
- **Authors:** Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.)
- **Publisher:** National Tiger Conservation Authority, Govt. of India, New Delhi, and Wildlife Institute of India, Dehradun
- **Download Date:** February 8, 2026
- **Source URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/Statusof_Tigers2010.pdf
- **File:** `Tiger_Status_2010.pdf`
- **Total India Population:** 1,706 tigers
- **Pages with reserve data:** 3, 39, 143

#### 2014 Census
- **Title:** Status of Tigers, Co-predators and Prey in India 2014
- **Published:** 2015
- **Authors:** Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.)
- **Publisher:** National Tiger Conservation Authority, Govt. of India, New Delhi, and Wildlife Institute of India, Dehradun
- **Download Date:** February 8, 2026
- **Source URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/AITE_2014_fullreport.pdf
- **File:** `Tiger_Status_2014.pdf`
- **Total India Population:** 2,226 tigers
- **Pages with reserve data:** 20

#### 2018 Census
- **Title:** Status of Tigers, Co-predators and Prey in India 2018
- **Published:** 2019
- **Authors:** Jhala, Y.V., Qureshi, Q., & Gopal, R. (Eds.)
- **Publisher:** National Tiger Conservation Authority, Govt. of India, New Delhi, and Wildlife Institute of India, Dehradun
- **Download Date:** February 8, 2026
- **Source URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/Tiger_Status_Report_2018.pdf
- **File:** `Tiger_Status_2018.pdf`
- **Total India Population:** 2,967 tigers
- **Pages with reserve data:** 40, 41

#### 2022 Census
- **Title:** All India Tiger Estimation Report 2022
- **Published:** 2023
- **Authors:** Jhala, Y.V., Qureshi, Q., Nayak, A.K., Chauhan, J.S., Sharma, K., Panchal, N., Talukdar, G., Sadhu, A., Dutta, R., Kandwal, R., & Nigam, P.
- **Publisher:** National Tiger Conservation Authority, Ministry of Environment, Forests and Climate Change, Government of India, New Delhi, and Wildlife Institute of India, Dehradun
- **Download Date:** February 8, 2026
- **Source URL:** https://ntca.gov.in/assets/uploads/Reports/AITM/status_of_tiger-copredators-2022.pdf
- **File:** `Tiger_Status_2022.pdf`
- **Total India Population:** 3,682 tigers
- **Pages with reserve data:** 20, 21

---

### Secondary Source: Research Publication

#### Bandipur & Nagarahole 2006-2010 Data

**[REPLACE WITH ACTUAL PAPER DETAILS]**

- **Title:** COMPARATIVE ANALYSIS OF TIGER LANDSCAPE COMPLEXES AND RESERVES IN INDIA: AN EVALUATION OF THE TIGER POPULATION 2006-2014.
- **Authors:** Singh, Bhanwar Vishvendra Raj, and Anjan Sen
- **Journal:** Am Research Thoughts 1
- **Year:** 2015
- **Volume/Issue:** 1
- **Pages:** 1796-1812
- **DOI:** NA
- **Source:** Google Scholar
- **Access URL:** https://www.researchgate.net/profile/Anjan-Sen/publication/281864332_Comparative_Analysis_of_Tiger_Landscape_Complexes_and_Reserves_in_India_An_Evaluation_of_the_Tiger_Population_2006-2014/links/55fc3bfa08aeba1d9f3c49e0/Comparative-Analysis-of-Tiger-Landscape-Complexes-and-Reserves-in-India-An-Evaluation-of-the-Tiger-Population-2006-2014.pdf
- **Download Date:** February 8, 2026

**Data Used:**
- Bandipur National Park population estimates: 2006, 2010
- Nagarahole National Park population estimates: 2006, 2010

**Relevance:**
This peer-reviewed publication provided reserve-specific tiger population 
estimates for Bandipur and Nagarahole that were not available at the 
individual reserve level in the 2006 and 2010 NTCA census reports.

**Data Validation:**
- Cross-referenced with NTCA 2014 baseline
- Consistent with Karnataka state-level trends
- Published in peer-reviewed journal
- Authors affiliated with Mohanlal Sukhadia University, University of Delhi

---

## Data Extraction

### Method Used
- Manual extraction from PDF reports
- Supplemented with peer-reviewed literature for missing data points

### Extracted Data
- **File:** `data/raw/ntca/population_data.xlsx`
- **Reserves Included:** 7 featured reserves
- **Years Covered:** 2006, 2010, 2014, 2018, 2022

### Featured Reserves

| Reserve | State | Data Source |
|---------|-------|-------------|
| Jim Corbett National Park | Uttarakhand | NTCA Reports (all years) |
| Kaziranga National Park | Assam | NTCA Reports (all years) |
| Bandipur National Park | Karnataka | NTCA (2014-2022), Singh, Bhanwar Vishvendra Raj, and Anjan Sen, 2015 (2006, 2010) |
| Nagarahole National Park | Karnataka | NTCA (2014-2022), Singh, Bhanwar Vishvendra Raj, and Anjan Sen, 2015 (2006, 2010) |
| Kanha National Park | Madhya Pradesh | NTCA Reports (all years) |
| Pench Tiger Reserve | MP/Maharashtra | NTCA Reports (all years) |
| Ranthambore National Park | Rajasthan | NTCA Reports (all years) |

---

## Data Quality Notes

### Data Confidence by Source

#### NTCA Census Reports (High Confidence)
- Official government census
- Standardized methodology across reserves
- Camera trap and occupancy-based estimates
- Comprehensive landscape-level surveys

#### Peer-Reviewed Publication (High Confidence)
- Published in reputable journal
- Peer-reviewed methodology
- Consistent with regional trends
- Cross-validated with NTCA baselines

### Known Limitations

**2006 Census:**
- Some reserves reported at landscape level
- Older methodology (less camera trap coverage)
- Higher uncertainty in estimates

**2010 Census:**
- Transition period in methodology
- Some individual reserve data not published separately

**2014-2022 Censuses:**
- Improved camera trap coverage
- More standardized protocols
- Higher confidence in estimates

### Methodological Notes

**Population Estimates vs. Exact Counts:**
- All figures represent population estimates, not exact counts
- Based on camera trap capture-recapture analysis
- Include confidence intervals in original reports
- We report point estimates (midpoints) for consistency

**Reserve Boundary Changes:**
- Some reserve boundaries expanded between censuses
- Population increases partly reflect expanded survey areas
- Core area populations tracked for consistency where possible

---

## Usage in Project

### Story Map Attribution

**When presenting data:**

"Tiger population data sourced from the National Tiger Conservation Authority's 
All India Tiger Estimation Reports (2006-2022) and Singh, Bhanwar Vishvendra Raj, and Anjan Sen, 2015 for 
Bandipur and Nagarahole reserves (2006, 2010)."

### Map/Figure Captions

**Example caption:**
```
Figure 1: Tiger population trends in featured reserves, 2006-2022.
Data: NTCA Tiger Census Reports (2006, 2010, 2014, 2018, 2022); 
Bandipur and Nagarahole 2006-2010 data from [Author et al., Year].
```

### Story Map Credits Section

Include in your Story Map's "Data Sources" or "References" section:

**Data Sources:**

1. National Tiger Conservation Authority. (2006-2023). All India Tiger 
   Estimation Reports. New Delhi: Government of India.

2. Singh, Bhanwar Vishvendra Raj, and Anjan Sen. "COMPARATIVE ANALYSIS OF TIGER LANDSCAPE COMPLEXES AND RESERVES IN INDIA: AN EVALUATION OF THE TIGER POPULATION 2006-2014." Am Research Thoughts 1 (2015): 1796-1812.

3. World Database on Protected Areas. (2026). UN Environment Programme. 
   Retrieved from www.protectedplanet.net

4. GBIF.org. (2026). Panthera tigris occurrence records. 
   Retrieved from www.gbif.org

---

## Data Processing

### Files Created

**Raw Data:**
- `population_data.xlsx` - Extracted census data

**Processed Data:**
- `data/processed/tiger_population_2006_2022.xlsx` - Clean dataset with:
  - All reserve population figures
  - Calculated growth metrics
  - Data source annotations
  - Ready for analysis

**Metadata:**
- This README.md
- `data_gaps.md` - Documentation of data limitations
- Attribution notes in Excel comments

---

## Data Integrity

### Verification Steps Completed

- [x] Cross-referenced values across multiple reports
- [x] Verified Bandipur/Nagarahole 2014 data matches NTCA baseline
- [x] Checked for consistency in reserve naming
- [x] Validated growth trends are biologically plausible
- [x] Documented all data sources with full citations
- [x] Noted confidence levels for each data point

### Reproducibility

All data sources are publicly available:
- NTCA reports: Available from ntca.gov.in or wii.gov.in
- Research paper: Available through [institution library/Google Scholar]
- Processing steps: Documented in `docs/methodology.md`

---

## License and Usage

### NTCA Data
- Published by Government of India
- Public domain for educational and research use
- Attribution required

### Research Publication
- Copyright held by [Publisher/Journal]
- Used under [Fair Use for educational purposes / Open Access license]
- Full citation provided

### This Compilation
- Data compilation and processing: © 2026 Kiran Balasubramanian
- Available for non-commercial, educational use
- Attribution required

---

## Contact

**For questions about data sources or processing:**

- **Project Lead:** Kiran Balasubramanian
- **Email:** kbsub@umich.edu
- **Project Repository:** https://github.com/K-bsub/tiger-conservation-india

**For original data inquiries:**

- **NTCA:** https://ntca.gov.in/
- **Wildlife Institute of India:** https://wii.gov.in/
- **Research Paper:** Singh, Bhanwar Vishvendra Raj

---

*Last Updated: February 8, 2026*  
*Data extracted for: Tiger Conservation Success Stories in India (2006-2022)*  
*Academic GIS Project*