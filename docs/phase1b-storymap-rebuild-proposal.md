# Plan Proposal: Rebuilding the Tiger Conservation Story Map on a Free, Permanent Stack

**Project:** Identifying Conservation Success Stories: Spatial Analysis of Tiger Population Recovery in India's Protected Areas (2006–2022)
**Author:** Kiran Balasubramanian
**Document type:** Migration / rebuild proposal
**Status:** ✅ Complete — published at https://k-bsub.github.io/tiger-conservation-india/
**Created:** June 19, 2026
**Completed:** June 2026

---

## 1. Why This Rebuild Exists

The published ArcGIS Story Map (`https://arcg.is/00bXi44`) became inaccessible because the
ArcGIS Online account entered a negative credit balance (−488), which suspended the hosted
feature services the story depends on. Diagnosis traced 99.9% of the credit burn to
**Feature Storage** (646.80 credits) — the cost of running 5 vector layers as live, queryable
hosted feature services inside a **Standard-tier Feature Data Store**.

**Key finding:** The data itself is tiny (~167 MB) and static. The cost was provisioned
feature-service *capacity*, not data volume — capacity this finished, non-updating project
never actually needed.

**Decision:** Rebuild the story as a static, interactive website on free infrastructure.
Nothing in this project requires live/queryable services or a paid tier.

---

## 2. Target Architecture

| Layer | Original (paid) | Rebuild (free) |
|---|---|---|
| Storytelling shell | ArcGIS StoryMaps | Static HTML + scrollytelling CSS/JS |
| Interactive maps | ArcGIS web maps (hosted feature services) | Leaflet + GeoJSON |
| Basemap | Esri Terrain w/ Labels | Free tile providers (CARTO / OSM / Esri free tiles) |
| KDE swipe comparison | StoryMaps Swipe block | `leaflet-side-by-side` plugin |
| Charts | Chart.js (already on GitHub Pages) | Chart.js (reuse as-is) |
| Data hosting | Feature Data Store (credit-billed) | Static GeoJSON files in repo |
| Site hosting | ArcGIS Online | GitHub Pages (free, permanent) |

**Why Leaflet over MapLibre GL:** Data is small and static (largest point layer ~1,400
features), the developer is new to JS mapping, and Leaflet has the gentler learning curve plus
a mature side-by-side swipe plugin. MapLibre's advantages (WebGL, vector tiles, huge data
density) don't apply here. If a wall is ever hit, Leaflet → MapLibre migration is well-trodden.

**Why GitHub Pages:** The project already has a repo (`github.com/K-bsub/tiger-conservation-india`).
Hosting the story there keeps documentation, data, and the public deliverable version-controlled
in one place, free forever, with no account or credit that can ever suspend it.

---

## 3. Critical Constraint — Export Before Access Is Lost

⚠️ **The single most time-sensitive task.** The source feature layers currently live in the
suspended Feature Data Store. The local `tiger_project.gdb` is the safe master copy, so source
data is **not** at risk — but exporting clean GeoJSON is easiest done now from ArcGIS Pro while
the project is intact.

All five layers must be exported to **GeoJSON in WGS84 (EPSG:4326)** — Leaflet requires
lat/long, not the project's analysis CRS (UTM 43N / EPSG:32643).

---

## 4. Data Inventory & Handling

| Source layer | Type | Size | Rebuild treatment |
|---|---|---|---|
| `Tiger_Reserves_Full` | Polygon | ~228 KB | GeoJSON, choropleth by `Growth_Category` |
| `HotSpot_Tiger_GiStar` | Point | ~175 KB | GeoJSON, styled by `Gi_Bin` |
| `GBIF_Tiger_Points_UTM43N` | Point | ~198 KB | GeoJSON + **marker clustering** |
| `OSM_Settlements` | Point | ~436 KB | GeoJSON (context layer, toggle) |
| `OSM_Roads_Major` | Line | **75.5 MB** | ⚠️ **Simplify + clip before export** |
| KDE Baseline 2006–2010 | Raster | (local) | Static **PNG image overlay** (georeferenced) |
| KDE Current 2018–2022 | Raster | (local) | Static **PNG image overlay** (georeferenced) |

**Two flagged data problems:**

1. **OSM_Roads_Major at 75.5 MB will crash the browser** if served raw. Must be reduced via
   ArcGIS **Simplify Line** (tolerance ~50–100 m) and/or clipped to the 50 km reserve buffers.
   Target: < 2–3 MB. You likely only need roads near the featured reserves anyway.

2. **GBIF points need clustering** (`leaflet.markercluster`) so ~1,400 points render smoothly
   and the known observer-bias clustering reads clearly rather than as a blob.

---

## 5. Scope — What Carries Over

**Preserved from the original (assets already exist):**
- 7-section narrative structure (Introduction → Overview → The Numbers → Where Tigers Are
  Detected → Reserve Profiles → What the Data Shows → Conclusion & Credits)
- All 4 Chart.js charts (population trend, growth ranking, density, bubble)
- 8 reserve photos (already licensed: 21 CC BY-SA Wikimedia, 3 Unsplash)
- WCAG AA color scheme (already documented in `symbology_scheme.html` — hex codes port directly)
- KDE swipe comparison (re-implemented as Leaflet side-by-side)
- Hot spot diverging palette, growth-category choropleth, popups
- All political-sensitivity narrative revisions (Kanha, Pench) carry over unchanged

**Explicitly out of scope (matches original decisions):**
- iNaturalist data (excluded in Phase 1 — stays excluded)
- Live/queryable services (the entire point of the rebuild is to avoid these)
- Any new analysis — this is a presentation-layer migration, not re-analysis

---

## 6. Phased Build Plan

Each step is self-contained and produces something testable before moving on. We do them
**one at a time** — you confirm each works before we proceed.

### Step 1 — Export & Prepare Data *(your machine, ArcGIS Pro)*
- Export 5 layers to GeoJSON (WGS84)
- Simplify + clip OSM roads to < 3 MB
- Export 2 KDE rasters as georeferenced PNGs + capture their geographic bounds
- **Deliverable:** a `/data` folder of clean GeoJSON + 2 PNGs
- **You do this; I give you exact tool settings and a QC checklist**

### Step 2 — Repo Scaffold & GitHub Pages *(15 min)*
- Set up folder structure in the existing repo
- Enable GitHub Pages, confirm a "hello world" page loads at the live URL
- **Deliverable:** working public URL serving a static page

### Step 3 — First Leaflet Map: Reserve Overview *(the learning step)*
- Single map, basemap + reserve choropleth by growth category + popups
- This is where you learn Leaflet fundamentals (map, tile layer, GeoJSON, style, popup)
- **Deliverable:** interactive overview map matching original Web Map 1

### Step 4 — Occurrence + Hot Spot Maps
- Add GBIF points with clustering
- Add hot spot layer styled by `Gi_Bin` (diverging palette)
- Layer toggles
- **Deliverable:** "Where Tigers Are Detected" interactive maps

### Step 5 — KDE Swipe Comparison
- `leaflet-side-by-side` with the two KDE PNG overlays
- Shared legend
- **Deliverable:** baseline-vs-current swipe matching the StoryMaps version

### Step 6 — Reserve Detail Maps
- 6 individual reserve maps (or one map with a reserve selector)
- **Deliverable:** "Reserve Profiles" section maps

### Step 7 — Narrative Shell & Scrollytelling
- Build the 7-section HTML page, port narrative text
- Embed maps + the 4 Chart.js charts + photos
- Scroll-driven transitions
- **Deliverable:** full single-page story with all content assembled

### Step 8 — Polish, Accessibility, Publish
- Mobile responsiveness, WCAG AA contrast verification, alt text
- Cross-browser/device testing (mirrors original Week 8 QA)
- Final commit; update all docs with the new live URL
- **Deliverable:** published rebuilt story + updated documentation

---

## 7. What You'll Learn (Leaflet concepts, in build order)
1. Map init + tile basemap (Step 3)
2. Loading GeoJSON (Step 3)
3. Styling features by attribute (Step 3 — choropleth)
4. Popups & interaction (Step 3)
5. Point styling + clustering (Step 4)
6. Layer control / toggles (Step 4)
7. Image overlays + side-by-side plugin (Step 5)
8. Tying maps to scroll position (Step 7)

I scaffold the code; you supply data + text and learn by modifying working examples.

---

## 8. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| OSM roads too large, slows page | High if not simplified | Simplify + clip in Step 1; hard target < 3 MB |
| GBIF points render as a blob | Medium | `leaflet.markercluster` from the start |
| KDE PNG misaligns with basemap | Medium | Capture exact bounds in Step 1; verify overlay in Step 5 |
| New to JS, get stuck | Medium | One step at a time; every step starts from working code |
| Losing AGOL access mid-export | Low (data is local) | `tiger_project.gdb` is the master; re-export anytime from Pro |
| Scope creep into re-analysis | Low | Presentation-layer only; analysis is frozen from Phase 1 |

---

## 9. Cost & Permanence

- **Recurring cost:** $0 (GitHub Pages free tier, open-source libraries, free basemap tiles)
- **Credits:** none — nothing provisioned, nothing to suspend
- **Longevity:** survives account lapses; lives in version control; portable to any static host
- **Maintenance:** none required for a finished project

---

## 10. Open Decisions Before Step 1

1. **Reserve detail maps:** 6 separate maps, or 1 map with a dropdown selector? *(affects Step 6)*
2. **Basemap provider:** CARTO Positron (clean/light), OSM standard, or Esri free tiles
   (closest to original Terrain look)? *(affects every map)*
3. **Narrative shell:** hand-built HTML/CSS (full control, more work) or a lightweight
   scrollytelling library (e.g., Scrollama)? *(affects Step 7)*

These can be deferred — none block Step 1 (data export), which is the time-sensitive task.

---

## 11. Immediate Next Action

**Begin Step 1: data export.** It's the only time-sensitive piece and unblocks everything else.
On confirmation, I'll provide exact ArcGIS Pro export settings (Features To JSON parameters,
Simplify Line tolerances, KDE PNG export + bounds capture) and a QC checklist to verify each
file before we touch any code.
