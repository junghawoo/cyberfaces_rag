---
title: "Downloading USGS Data"
unit_id: 206
course_id: 0
level: "Foundation"
slug: downloading-usgs-data
is_course: 0
---

# Downloading USGS Data

Note: This unit covers NEON (National Ecological Observatory Network) data access and download procedures using R, though titled "Downloading USGS Data." Content emphasizes NEON data repositories and neonUtilities R package functionality.

## Overview

NEON is a national network of research sites funded by the NSF with teams collecting hydrology, biogeochemistry, and ecology data. Complete datasets available at http://data.neonscience.org.

**Primary Tool**: R package neonUtilities—downloads and combines datasets from NEON data repository.

**Libraries**: neonUtilities, ggplot2, dplyr

## Summarized attachments
- **DownloadData** (https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%201/NEON%20Data.ipynb, notebook): NEON data download notebook using neonUtilities R package covering hydrology (continuous discharge DP4.00130.001, field discharge DP1.20048.001, rating curves DP4.00133.001), water chemistry (grab samples DP1.20093.001, YSI EXO water quality DP1.20288.001, nitrate sensor DP1.20033.001), and biodiversity data (macroinvertebrates DP1.20120.001, fish DP1.20107.001, benthic microbes DP1.20086.001) with Arikee River examples and assignment tasks.

**Display Configuration**: `options(repr.matrix.max.cols=40, repr.matrix.max.rows=10)` customizes Jupyter Lab/Notebook R kernel column/row display limits for datasets with extensive metadata.

## Data Organization

**Data Storage Setup**: Create ~/neon_data directory; `dir.create("~/neon_data", showWarnings=FALSE)` handles existing directories without errors.

## Hydrology Data

### Discharge (DP4.00130.001 - Continuous Discharge)

Example: Arikee River (ARIK). Function: `loadByProduct(dpID = "DP4.00130.001", site = "ARIK", check.size = FALSE, startdate = "2023-01", enddate = "2023-12")`

Downloads ~49.5 MB, unpacks/stacks 2 data tables and 4 metadata tables in ~7.6 seconds. Provisional data excluded by default; use `include.provisional=TRUE` to include. Access via: `Arik_Q[["csd_continuousDischarge"]]`; key column: `maxpostDischarge`. Plot with ggplot: `ggplot(data, aes(endDate, maxpostDischarge)) + geom_point() + geom_line()`.

### Channel Geometry (DP1.20048.001 - Discharge Field Collection)

Acoustic Doppler Current Profiler (ADCP) field surveys. Data: `dsc_fieldDataADCP` dataframe. Parameters: `sectionArea`, `waterDepth`; computed: `Channel_Width = sectionArea/waterDepth`. Visualizes hydraulic relationships.

### Rating Curves (DP4.00133.001 - Stage-Discharge Rating Curves)

Rating curves for continuous discharge conversion from pressure transducers. Access: `Arik_RC$sdrc_gaugeDischargeMeas`. Columns: `gaugeHeight`, `streamDischarge`.

## Water Chemistry

### Grab Samples (DP1.20093.001)

Anions, cations, conductivity, pH, carbon forms, nutrients (total, dissolved, particulate).

Two sources: `swc_domainLabData` (NEON domain lab), `swc_externalLabDataByAnalyte` (external contracted lab). Most data in external lab dataset. Access analytes: `unique(Arik_ExternalWC$analyte)` (e.g., Fe, NO3+NO2-N). Extract and plot by analyte and collection date.

### Continuous Sensor Data (DP1.20288.001 - YSI EXO 2 Water Quality)

In situ multiparameter sonde. Data: `waq_instantaneous` dataframe. Measures: temperature, conductance, pH, fluorescence dissolved organic matter (fDOM), dissolved oxygen. Key columns: `specificConductance`, `localDissolvedOxygenSat`, `startDateTime`.

### Additional Sensors
- SUNA V2 Nitrate Sensor (DP1.20033.001): nitrate, absorbance 254 nm
- Photosynthetically Active Radiation (PAR): ecosystem modeling input

## Biodiversity Data

### Macroinvertebrate Biodiversity (DP1.20120.001)

Routine collections all NEON aquatic sites. Data: `inv_taxonomyProcessed` element. Full taxonomy: phylum, subphylum, class, subclass, infraclass, superorder, order, suborder, infraorder, superfamily, family, subfamily, tribe, subtribe, genus; plus `individualCount`. Save as RDS: `saveRDS(data, "~/neon_data/biodiversity/filename.rds")`.

### Fish Diversity (DP1.20107.001)

Data: `fsh_bulkCount` dataframe. Format: `scientificName` (single column, genus+species). Process with dplyr: `group_by(scientificName) %>% summarize(Total_Count = sum(bulkFishCount))`. Bar plot visualization. Save as RDS.

### Microbial Diversity (DP1.20086.001)

Archaea, bacteria (16S), fungi (ITS). Metadata dataframes: `mcc_benthicSeqVariantMetadata_16S` (prokaryotes), `mcc_benthicSeqVariantMetadata_ITS` (fungi). Each contains URLs to CSV files (not direct abundance). Download/combine CSVs with dplyr functions. Substrates: episammon (sand), epiphyton (benthic plants). Taxonomy: `completeTaxonomy` (domain→species, semicolon-delimited); individual level columns. Output metrics: row count (complexity), unique OTU count (operational taxonomic units accounting for microbial asexual reproduction/horizontal gene transfer). Save combined data as RDS.

## Assignment

Download datasets from two different NEON sites. Deliverables include:
- 1-year graphs: discharge, channel geometry, rating curves, water quality sonde, PAR
- Species Order-level counts: fish, macroinvertebrates
- OTU count: microbial diversity

**Reference**: GitHub - https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%201/NEON%20Data.ipynb
