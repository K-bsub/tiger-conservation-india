# Story Map Outline
## Identifying Conservation Success Stories: Spatial Analysis of Tiger Population Recovery in India's Protected Areas (2006–2022)

**Author:** Kiran Balasubramanian  
**Platform:** ArcGIS StoryMaps  
**Created:** February 16, 2026  
**Status:** Week 7 — Draft outline

---

## Narrative Arc

> **Core argument:** India's tiger recovery is not a single national story —
> it is seven distinct local stories, each shaped by a different landscape,
> pressure, and strategy. What unites them is that they all worked.

The Story Map moves from **national context → spatial overview → data trends
→ reserve-by-reserve depth → synthesis**. Each section builds on the last.
A reader who only reads the intro and skims the maps should still leave with
the core finding. A reader who reads everything should leave with a nuanced
understanding of why each reserve succeeded differently.

---

## Chapter Structure

```
COVER
│
├── 1. INTRODUCTION
│     Why tigers? Why now? Why these seven reserves?
│
├── 2. THE OVERVIEW MAP
│     Where are these reserves? What category is each?
│
├── 3. THE NUMBERS
│     Population trend line graph + growth ranking bar chart
│
├── 4. WHERE TIGERS ARE DETECTED
│     KDE density comparison (before/after) + hot spot analysis
│
├── 5. RESERVE PROFILES  ← main content, 7 sections
│     5a. Ranthambore Tiger Reserve
│     5b. Pench Tiger Reserve
│     5c. Bandipur & Nagarahole National Parks
│     5d. Kanha National Park
│     5e. Kaziranga National Park
│     5f. Jim Corbett National Park
│
├── 6. WHAT THE DATA TELLS US
│     Density chart + bubble chart + key findings synthesis
│
└── 7. CONCLUSION & CREDITS
      Conservation implications, data sources, acknowledgments
```

---

## Section-by-Section Detail

---

### COVER

| Element | Content |
|---|---|
| Title | Identifying Conservation Success Stories |
| Subtitle | Spatial Analysis of Tiger Population Recovery in India's Protected Areas, 2006–2022 |
| Hero image | Full-bleed tiger reserve landscape photo (Bandipur or Corbett — highest quality CC image from `media/photos/reserves/`) |
| Byline | Kiran Balasubramanian · February 2026 |

---

### 1. INTRODUCTION
*~3 paragraphs · no maps · 1 photo*

**Paragraph 1 — The stakes**
India's paradox: a country of 1.4 billion people sharing a subcontinent with
the world's largest wild tiger population. Set up the scale — 70% of global
wild tigers in India, species nearly extinct in the 1970s, Project Tiger
launched 1973. Establish that this is a conservation story worth telling.

**Paragraph 2 — The monitoring system**
Introduce the NTCA census framework — camera trap SECR methodology, five
census rounds from 2006 to 2022, national total growing from ~1,411 to 3,682.
This is what makes the analysis possible: systematic, comparable data across
16 years. Briefly note what the data can and cannot tell us (estimates, not
exact counts).

**Paragraph 3 — This project**
Introduce the seven reserves. Name them and their landscapes. State the
central question: *What do the most successful tiger reserves have in common —
and what makes each one's story unique?* End with a forward-looking sentence
that invites the reader to explore.

**Media placement:**
- 1 photo: national map or iconic tiger image (CC licensed)

---

### 2. THE OVERVIEW MAP
*Web Map 1 embed · ~2 paragraphs*

**Map:** `Tiger Conservation – Reserve Overview` (Web Map 1)
- Full interactive embed
- Default zoom: all-India view showing all 7 reserves
- Bookmarks: All India / Western Ghats / Central India / Semi-Arid / Northeast / Terai Arc
- Popups active

**Paragraph 1 — Reading the map**
Explain the four growth categories (High growth / Moderate growth / Stable /
Stable at capacity) and what each color means. Point out the geographic spread
— reserves from Assam to Karnataka, Rajasthan to Uttarakhand.

**Paragraph 2 — The landscape diversity**
Emphasize that these reserves span radically different ecosystems: tropical
rainforest (Western Ghats), sal forest plateau (Central India), semi-arid
scrub (Rajasthan), Brahmaputra floodplain (Northeast), Himalayan foothills
(Terai Arc). Tigers succeed in all of them — that's the story.

---

### 3. THE NUMBERS
*2 charts · ~3 paragraphs*

**Chart placement 1:** Chart 1 — Population trend line graph (full width)

**Paragraph 1 — Reading the trend lines**
Walk the reader through the line graph. Highlight: Corbett's consistent
upward trajectory as the highest-population reserve; Pench's steep climb
from just 33 tigers in 2006; Kaziranga's flat line (ecologically significant —
not stagnation, but carrying capacity); Ranthambore's plateau from 2018→2022.

**Chart placement 2:** Chart 2 — Growth rate horizontal bar chart

**Paragraph 2 — The growth story**
Pench at 133% and Bandipur at 121% lead the ranking. Note that percent
growth and absolute population tell different stories — Corbett adds more
tigers in absolute terms despite lower percentage growth because it started
from a higher base.

**Paragraph 3 — What these numbers mean**
Contextualise: these are NTCA statistical estimates, not exact counts.
Confidence intervals exist. But the directional trend across 16 years and
five independent census rounds is unambiguous — these reserves are recovering.

---

### 4. WHERE TIGERS ARE DETECTED
*Web Maps 2 + 3 · ~4 paragraphs · ⚠️ observer bias teaching section*

**Map placement 1:** Web Map 2a — KDE Baseline 2006–2010  
**Map placement 2:** Web Map 2b — KDE Current 2018–2022  
*(side-by-side or swipe if StoryMaps supports it; otherwise sequential embeds)*

**Paragraph 1 — The density maps explained**
Introduce KDE — what it shows (spatial concentration of GBIF occurrence
records), what it doesn't show (actual tiger density from census). Explain the
shared classification breaks that make the two maps directly comparable.

**Paragraph 2 — What changed between 2006 and 2022**
Describe the visual difference: sparse, tight kernels in the baseline vs.
larger, more diffuse green areas in the current period. Name the reserves
where growth is most visible spatially.

**Map placement 3:** Web Map 3 — Hot Spot Analysis

**Paragraph 3 — The hot spot map explained**
Explain Getis-Ord Gi* in plain language: statistically significant clusters
of detections vs. random scatter. Note confirmed hot spot clusters at
Kanha/Pench corridor and Kaziranga at the 25km distance band.

**Paragraph 4 — The observer bias lesson (Ranthambore)**
This is the key analytical caveat and a genuine teaching moment. Ranthambore
shows dense Cold Spots north of the reserve near Sawai Madhopur despite
having 57 tigers in 2022. Explain: GBIF records reflect where people look,
not just where tigers are. Tourists and researchers cluster near park gates
and roads. The Cold Spot cluster at Ranthambore is a concentration of *human
observers*, not an absence of tigers. This limitation applies across all
reserves to varying degrees — the census data is the authoritative source
for population counts.

---

### 5. RESERVE PROFILES
*7 sections · each follows the same template*

**Profile template per reserve:**
```
[Reserve photo — full width or right-aligned]
[Reserve name heading]
[Individual reserve map embed]

Stat card row:
  Population 2006 → 2022  |  % Growth  |  Tigers/100km²  |  Forest Cover %  |  Landscape type

[Paragraph 1: The reserve's specific achievement — what makes it notable]
[Paragraph 2: Habitat context — terrain, forest, ecology]
[Optional: 1 sentence on the key analytical finding from hot spot / KDE maps]
```

---

#### 5a. Pench Tiger Reserve
**Category:** High growth (133% · #1 ranked)  
**Map:** `Reserve – Pench Tiger Reserve`  
**Key narrative:** Smallest reserve of the high-growth group (combined 1,907 km²)
achieving the highest growth rate. The combined MP/Maharashtra landscape — a
deliberate management decision to treat the trans-boundary reserve as one unit.
Pench River corridor visible in the map. Central Indian sal forest habitat.
**Analytical note:** Hot spot cluster at 25km distance band in Kanha/Pench
corridor — statistically significant concentration linking these two reserves.

---

#### 5b. Bandipur & Nagarahole National Parks
**Category:** High growth (Bandipur 121% · #2; Nagarahole 81% · #3)  
**Map:** `Reserve – Bandipur & Nagarahole National Parks` (combined landscape map)  
**Key narrative:** The Western Ghats connected complex. Two separately managed
parks forming one contiguous tiger landscape of nearly 3,000 km². The
Mysore-Ooty highway (NH-181) bisecting Bandipur — one of India's most
contentious wildlife corridor roads — and the Kabini Reservoir in Nagarahole
as the ecological heart of the complex. Tiger success here despite persistent
road pressure is remarkable.
**Analytical note:** Not Significant hot spot results throughout — attributed
to lower GBIF observer density in this region, not absence of tigers.

---

#### 5c. Ranthambore Tiger Reserve
**Category:** High growth (78% · #4)  
**Map:** `Reserve – Ranthambore Tiger Reserve`  
**Key narrative:** The semi-arid outlier. Ranthambore proves tigers can thrive
in rocky, dry deciduous terrain as well as lush forest. The Aravalli Hills
setting. Sawai Madhopur town sitting directly at the park boundary. The
plateau from 2018→2022 (57→57 tigers) — likely carrying capacity for this
landscape size, with the reserve functioning as a **dispersal source**
for tigers moving into the broader Rajasthan landscape.
**Analytical note:** The Cold Spot cluster near Sawai Madhopur is the
dataset's clearest illustration of GBIF observer bias — high human visitation
concentrated near the gate, not representative of tiger distribution across
the reserve interior.

---

#### 5d. Kanha National Park
**Category:** Stable (18% growth · highest absolute population stability)  
**Map:** `Reserve – Kanha National Park`  
**Key narrative:** Kanha's story is not dramatic growth but sustained
excellence — maintaining 89–105 tigers over 16 years in the largest reserve
(2,072 km²) of the seven. The two-lobe polygon reflecting core zone and
buffer. The Maikal Hills sal forest habitat. Kanha as the template for Indian
tiger reserve management — the model other reserves have learned from.
**Analytical note:** Blue/purple Cold Spot dots visible in the right lobe —
correct result given moderate GBIF coverage of Central India; NTCA census
data shows stable population.

---

#### 5e. Kaziranga National Park
**Category:** Stable at capacity (~10 tigers/100km² · highest density in India)  
**Map:** `Reserve – Kaziranga National Park`  
**Key narrative:** Kaziranga is not a growth story — it is a density story.
India's highest tiger density, a narrow floodplain reserve bounded by the
Brahmaputra to the north and Karbi Anglong Hills to the south. The seasonal
tiger movement between the reserve and the hills during monsoon flooding.
The reserve as a **source population** for Northeast India. The flat census
line (103→104 tigers over 12 years) is not failure — it is a reserve
operating at ecological carrying capacity.
**Analytical note:** Sparse GBIF detections despite exceptional tiger density
— reflects Kaziranga's remote Northeast location and lower tourist/researcher
observer effort relative to more accessible reserves.

---

#### 5f. Jim Corbett National Park
**Category:** Moderate growth (58% · highest absolute population of all 7)  
**Map:** `Reserve – Jim Corbett National Park`  
**Key narrative:** India's oldest national park and its most populous tiger
reserve — 260 tigers in 2022. The Himalayan foothills setting, Ramganga
Reservoir, the elevation range from Terai plains to Himalayan ridges. Corbett
as the reserve that has sustained the largest single tiger population in India
across all five census rounds. The name — honoring Jim Corbett, who both
hunted and ultimately championed the conservation of big cats in these forests.
**Data caveat:** Corbett's density figure (17.78 tigers/100km²) is likely
inflated — KBA polygon smaller than legal TR area. Use with caution;
population absolute count (260) is the reliable figure.

---

### 6. WHAT THE DATA TELLS US
*2 charts · ~3 paragraphs · synthesis section*

**Chart placement 1:** Chart 3 — Density comparison grouped bar (2006 vs 2022)

**Paragraph 1 — Density as the real measure**
Growth percentage is one metric; density is another. Nagarahole and Corbett
lead on tigers/100km², but for different reasons. Pench shows the most
dramatic density increase despite modest absolute numbers. Introduce the
idea that reserve size and reserve density tell complementary stories.

**Chart placement 2:** Chart 4 — Bubble chart (area vs population vs growth)

**Paragraph 2 — The bubble chart finding**
The key insight: reserve area alone does not predict tiger population or
growth. Kanha (largest reserve, 2,072 km²) has lower growth than Pench
(smaller combined area). Nagarahole (1,153 km²) has higher density than
Kanha. What matters more than size: habitat quality, prey availability,
anti-poaching effort, and connectivity to other protected areas.

**Paragraph 3 — Common threads**
Synthesize across all 7 reserves: what they share despite their differences.
Effective anti-poaching. Community engagement programs. Forest department
capacity. NTCA monitoring framework providing accountability. The role of
systematic census data in driving evidence-based management decisions.

---

### 7. CONCLUSION & CREDITS
*~2 paragraphs · data sources · acknowledgments*

**Paragraph 1 — The broader significance**
India's tiger recovery from ~1,411 in 2006 to 3,682 in 2022 is one of the
most remarkable large carnivore conservation achievements in history. These
seven reserves are not outliers — they are exemplars of what is possible
when habitat protection, scientific monitoring, and community partnerships
work together. What India has demonstrated can inform tiger conservation
across South and Southeast Asia.

**Paragraph 2 — What remains**
Acknowledge the challenges ahead: habitat corridors between reserves,
human-wildlife conflict at reserve boundaries, climate change altering
prey distribution, the need to sustain political will and funding. The
success documented here is real and hard-won — and it is not finished.

**Data Sources block** (from `docs/data-sources.md` attribution block)

**Methodology note** (brief — link to GitHub repository for full documentation)

---

## Map & Chart Placement Summary

| Section | Content type | Asset |
|---|---|---|
| Cover | Hero photo | `media/photos/reserves/` |
| 1. Introduction | Photo | National context image |
| 2. Overview | Interactive map | Web Map 1 |
| 3. The Numbers | Chart | Chart 1 — line graph |
| 3. The Numbers | Chart | Chart 2 — bar chart |
| 4. Detection | Interactive map | Web Map 2a (KDE baseline) |
| 4. Detection | Interactive map | Web Map 2b (KDE current) |
| 4. Detection | Interactive map | Web Map 3 (hot spots) |
| 5a. Pench | Photo + map | Reserve photo + Web Map embed |
| 5b. Bandipur/Nag | Photo + map | Reserve photo + Web Map embed |
| 5c. Ranthambore | Photo + map | Reserve photo + Web Map embed |
| 5d. Kanha | Photo + map | Reserve photo + Web Map embed |
| 5e. Kaziranga | Photo + map | Reserve photo + Web Map embed |
| 5f. Corbett | Photo + map | Reserve photo + Web Map embed |
| 6. Synthesis | Chart | Chart 3 — density bar |
| 6. Synthesis | Chart | Chart 4 — bubble chart |
| 7. Conclusion | Text + credits | Data sources attribution block |

**Total interactive maps:** 5 (Web Maps 1, 2a, 2b, 3 + 6 reserve maps = 9 map embeds)  
**Total charts:** 4  
**Total photos:** minimum 8 (cover + intro + 6 reserve profiles)

---

## ArcGIS StoryMaps Build Notes

- **Story Map type:** Narrative (scrolling) — not tabbed or guided map tour
- **Section blocks to use:**
  - Sidecar block for reserve profiles (stat card on left, map on right)
    works well if available in your AGOL plan
  - Alternatively: map embed + text block + image block in sequence
- **Chart integration:** Export Chart 1–4 as PNG from Chrome → insert as
  image blocks; or test custom HTML embed for interactive tooltip versions
- **Observer bias callout (Section 4):** Use a colored callout/quote block
  in StoryMaps to visually distinguish this analytical caveat from narrative text
- **Photo licensing:** Verify all `media/photos/reserves/` attributions in
  `media/photo-attributions.md` before publishing publicly

---

*Document: `docs/storymap_outline.md`*  
*Repository: https://github.com/K-bsub/tiger-conservation-india*
