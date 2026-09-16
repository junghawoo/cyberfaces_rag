---
title: "StreamCI - 4"
unit_id: 299
course_id: 0
level: "Developer"
slug: streamci-4
is_course: 0
objectives:
  - "Be a member of the dev. team!"
---

# StreamCI - 4

Developer-level StreamCI module (StreamCI - 4 - Member; objective: "Be a member of the dev. team!") whose extracted local resource `census.md` is a lesson titled "Data from U.S. Census Bureau" (teaching: 100, exercises: 5) on accessing, visualizing, and analyzing U.S. Census Bureau data for a retrieval corpus.

The lesson's guiding questions cover the kinds of Census Bureau datasets, visualizing/analyzing them for a region of interest, combining spatial and tabular Census data, and ACS variables. Objectives: overview of Census Bureau data, downloading and visualizing spatial data, querying/analyzing spatial data, and performing complex spatial joins.

Introduction describes three dataset categories: (1) Census TIGER/Line Shapefiles — TIGER (Topologically Integrated Geographic Encoding and Referencing) system, the Bureau's primary geospatial data, available 2007–present (pre-2007 in ASCII), covering legal boundaries for states, counties, places, zip codes, urban areas, census blocks, block groups, and tracts; records carry a GEOID linking to census data, and use ANSI codes including FIPS codes and USGS GNIS codes (fields like STATEFP = state FIPS, STATENS = state GNIS; five-digit county FIPS = 2-digit state + 3-digit county). Includes an official_census.png map image. (2) Decennial Census of Population and Housing — every ten years, counting every person; population by sex, age, race, Hispanic origin; housing occupancy, vacancy, tenure at all geographic levels; smallest margin of error. (3) American Community Survey (ACS) — annual sample survey with 1-year and 5-year estimates (higher margin of error), adding social characteristics (school enrollment, educational attainment, marital status, fertility, grandparents caring for children, veteran status, disability status, language spoken at home), income and benefits (SNAP/food stamps, health insurance coverage, income), employment (employment location, mode of travel to work), plus ancestry, citizenship status, place of birth, year of entry. Keypoints: census data supports service planning, business/facility site selection, public policy analysis, hazard-impact spatial analysis, and epidemiological models.

"Accessing the Census Data" covers manual downloads from data.census.gov, bulk downloads, and programmatic access via official Census APIs; explains what API-based census access means (structured URLs returning JSON or CSV), contrasts Census API data access vs. geocoding in a comparison table, and lists why APIs beat manual downloads (reproducibility, automation, Python/GIS integration). Typical workflow: construct request URL, send to Census API endpoint, receive JSON/CSV, convert to a DataFrame, join with geographic boundaries. Callout: APIs return aggregate data only for privacy.

"Expert Tutorial: Accessing ACS Data via the Census API" walks through the Census Developers Page (census.gov/data/developers.html), choosing the ACS API (1-/3-/5-year products; 2023 ACS 5-Year covers 2019–2023), Data Profiles example calls, and the 2023 ACS Comparison Profiles Variables page. Explains geographic-level API links (country, state, tract via state>county>tract), e.g. `https://api.census.gov/data/2023/acs/acs5/profile?get=NAME&for=tract:*&in=state:06&in=county:*&key=...` for California (state:06); state codes list at census.gov ANSI code lists; `state:*` is disallowed for tract queries. Shows adding variables such as DP04_0058E ("no vehicles available" estimate) for Indiana (state:18), optional `&descriptive=true` and `&outputFormat=csv` parameters, case sensitivity of variable names, and a YouTube video tutorial "How to Access ACS Data from the Census API" (youtube.com/watch?v=rqePUEBrcWQ). Example final call returns occupied households without a vehicle for every Indiana tract.

Module Overview table links three Google Colab notebooks from the SpatialTurn/DataCollection-Notebooks GitHub repo: Beginner (`Census/Beginner.ipynb`, visualize/analyze manually downloaded Census shapefiles), Intermediate (`Census/census_join.ipynb`, automatic dataset requests and interactive-map visualization of shapefiles), and Expert (`Census/CensusGeocodeAPI.ipynb`, Census API URL construction and visualization after joining with census tracts).

## Summarized attachments
- **census.md** (census.md, md): Comprehensive lesson (100 min teaching, 5 min exercises) on U.S. Census Bureau data covering three dataset categories (Census TIGER/Line Shapefiles with GEOID and FIPS/GNIS codes, Decennial Census of Population and Housing, American Community Survey with 1-year and 5-year estimates), data access methods (manual downloads from data.census.gov and programmatic access via Census API), Census API documentation, ACS API endpoints for geographic levels (country, state, county, tract), API variable references (DP04_0058E for vehicles available), parameter usage (state codes, tract queries, outputFormat, descriptive), YouTube tutorial references, and integration with Google Colab notebooks for beginner/intermediate/expert workflows combining Census shapefiles with attribute data for spatial analysis.
