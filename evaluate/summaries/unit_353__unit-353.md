---
title: "Unit 353"
unit_id: 353
---

# Unit 353

This unit covers U.S. Census Bureau data access, visualization, and spatial analysis through multiple lesson progressions (census.md).

## Data from U.S. Census Bureau (census.md)

**Learning Objectives**: Provide overview of Census Bureau datasets; explain spatial data download/visualization; demonstrate querying and spatial joins; define ACS variables.

**Teaching**: 100 minutes; Exercises: 5 exercises.

### Three Broad Census Data Categories

1. **Census TIGER/Line Shapefiles**: Topologically Integrated Geographic Encoding and Referencing system. Primary geospatial Census Bureau data available 2007-present (pre-2007 in ASCII format). Includes legal boundaries and geographic unit names: states, counties, places, zip codes, urban areas, census blocks, census block groups, census tracts. Each record has standard geographic identifier (GEOID) linking to census data. Uses American National Standards Institute (ANSI) codes: Federal Information Processing Series (FIPS) codes and USGS Geographic Names Information System (GNIS) codes. Fields: STATEFP (state FIPS code), STATENS (state GNIS code). County FIPS codes 5-digit format: first two digits = state FIPS, remaining three = county codes. Associated image: official_census.png (U.S. state/county boundaries map).

2. **Decennial Census of Population and Housing**: Conducted every 10 years; counts all U.S. residents. Provides population characteristics (age, sex, race, ethnicity, household composition); point-in-time data with minimal margin of error. Variables: population data by sex/age/race/Hispanic origin; housing data by occupancy/vacancy/tenure at highest geographic resolution (all levels).

3. **American Community Survey (ACS)**: Conducted annually; samples population. Covers topics absent from decennial census: education, employment, internet access, transportation. ACS 1-year = 12-month continuous survey; ACS 5-year = 60-month continuous survey. Higher margin of error vs. decennial census. Social characteristics: school enrollment, educational attainment, marital status, fertility, grandparents caring for children, veteran status, disability status, language spoken at home. Income/benefits: SNAP (food stamps/Supplemental Nutrition Assistance Program), health insurance coverage, income. Employment: employment location, mode of travel to work. Other variables: ancestry, citizenship status, place of birth, year of entry.

### Data Access Methods

Multiple approaches to obtain data:
- Manual downloads from data.census.gov
- Bulk file downloads
- Programmatic access via official Census APIs

**API-Based Census Data Access** enables retrieval of demographic/socioeconomic data directly into Python workflows. APIs allow structured URL requests returning machine-readable data (JSON, CSV) for automated processing. Benefits: specify exact variables, choose geographic scale (state, county, tract, block group), automate downloads for reproducibility, integrate directly into scripts/analyses, support year-to-year consistency.

**Census API vs. Geocoding Comparison**: Census APIs download official census tables using predefined census geographies returning demographic attributes designed for aggregation emphasizing consistency; geocoding converts addresses to coordinates via external location services returning spatial point locations designed for individual locations emphasizing positional accuracy. This notebook retrieves attribute data organized by census geography, not geocoded addresses.

**Why Census APIs**: Reduce manual steps/human error; ensure reproducibility; make workflows scalable/automatable; allow Python/GIS integration; support consistent multi-year/multi-region retrieval; same query reused for annual updates, geographic extent changes, variable swaps without re-downloading.

**Typical Workflow**: (1) Construct request URL specifying variables/geography; (2) Send request to Census API endpoint; (3) Receive structured data (JSON/CSV); (4) Convert results to DataFrame; (5) Join with geographic boundaries (optional). Data tabular initially, becomes spatial through joins/mapping tools.

### Expert Tutorial: Accessing ACS Data via Census API

**Step 1 - Explore Census API**: Go to https://www.census.gov/data/developers.html; select Available APIs; scroll/click American Community Survey (ACS); review 1-year/3-year/5-year estimate options (5-year longer timeframe: 2023 ACS 5-Year covers 2019-2023; 2022 ACS 5-Year covers 2018-2022); scroll Data Profiles; review "Example Call" links (base API URLs); click html link next to 2023 ACS Comparison Profiles Variables (lists all variables/codes).

**Step 2 - Understanding API Geographic Levels**: ACS API base links for country/state/tract-within-state. Tract-level uses "state > county > tract" pattern. Example California (state code 06): https://api.census.gov/data/2023/acs/acs5/profile?get=NAME&for=tract:*&in=state:06&in=county:*&key=YOUR_KEY_GOES_HERE. Key points: tract:* (all tracts selected state), county:* (all counties selected state), replace state:06 with desired state code (see https://www.census.gov/library/reference/code-lists/ansi.html#state), state:* not allowed for tract-level (dataset size limitation).

**Step 3 - Adding Variables**: On variables page, press Ctrl+F search for variable (example: "no vehicles available" → DP04_0058E estimate version); add variable after NAME comma-separated. Before: https://api.census.gov/data/2023/acs/acs5/profile?get=NAME&for=tract:*&in=state:18&in=county:*. After: https://api.census.gov/data/2023/acs/acs5/profile?get=NAME,DP04_0058E&for=tract:*&in=state:18&in=county:*. Add multiple variables comma-separated.

**Step 4 - Optional Enhancements**: &descriptive=true (view variable descriptions); &outputFormat=csv (spreadsheet-friendly download). API calls case-sensitive. Video tutorial: https://www.youtube.com/watch?v=rqePUEBrcWQ.

**Example Final Call**: https://api.census.gov/data/2023/acs/acs5/profile?get=NAME,DP04_0058E&for=tract:*&in=state:18&in=county:*&descriptive=true&outputFormat=csv (returns occupied households without vehicle for every Indiana tract).

## Summarized attachments

- **census.md** (census.md, markdown): Carpentry-style lesson module providing comprehensive overview of U.S. Census Bureau data sources including TIGER/Line shapefiles with geographic boundaries and GEOID identifiers, Decennial Census population/housing counts at all geographic levels, and American Community Survey annual sampling with demographic, socioeconomic, and housing attributes, plus hands-on tutorials for programmatic API access to retrieve and join census data with spatial boundaries for analysis.

### Module Lessons (3-Tier Progression)

1. **Beginner**: https://colab.research.google.com/github/SpatialTurn/DataCollection-Notebooks/blob/main/Census/Beginner.ipynb — visualize/analyze manually downloaded Census Bureau shapefiles.

2. **Intermediate**: https://colab.research.google.com/github/SpatialTurn/DataCollection-Notebooks/blob/main/Census/census_join.ipynb — request dataset automatically from webpage; visualize downloaded shapefile using interactive map.

3. **Expert**: https://colab.research.google.com/github/SpatialTurn/DataCollection-Notebooks/blob/main/Census/CensusGeocodeAPI.ipynb — uses Census APIs to create URL download desired dataset; visualize after joining with census tract.

### Census Data Applications

- Planning services for specific population groups
- Site selection for new businesses/service facilities
- Public policy analysis
- Spatial analysis of hazard impact and epidemiological models

### Key Concepts

- Census API returns aggregate data only (individual-level records never provided for privacy protection)
- Data available at multiple geographic scales for flexible analysis
- API approach enables reproducible, automatable workflows
- Privacy-preserving aggregate format suitable for research, teaching, large-scale analysis
