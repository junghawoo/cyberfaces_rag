---
title: "Ecology: Downloading NEON Data"
unit_id: 212
course_id: 0
level: "Foundation"
slug: ecology-downloading-neon-data
is_course: 0
---

# Ecology: Downloading NEON Data

This module covers downloading and analyzing National Ecological Observatory Network (NEON) data for hydrology, biogeochemistry, and ecology research. NEON is a national network of research sites funded by NSF; each site collects wide arrays of hydrology, biogeochemistry, and ecology data. Complete dataset list available at http://data.neonscience.org.

**Primary Tool**: R package neonUtilities—designed to download and combine datasets from the NEON data repository.

**Required R Libraries**: neonUtilities, ggplot2, dplyr

**Data Display Configuration**: 
```r
options(repr.matrix.max.cols=40, repr.matrix.max.rows=10)
```

## Hydrology Data Downloads

### Setup and Data Storage

Create NEON data directory (~/neon_data); function handles existing directories with warnings suppressed:
```r
dir.create("~/neon_data", showWarnings=FALSE)
```

### Discharge Data (DP4.00130.001 - Continuous Discharge)

Example: Arikee River (site code ARIK)

Function: `loadByProduct(dpID = "DP4.00130.001", site = "ARIK", check.size = FALSE, startdate = "2023-01", enddate = "2023-12")`

Downloads continuous discharge data (~49.5 MB example), unpacks/stacks 2 data tables and 4 metadata tables. Access discharge via dataframe name: `Arik_Q[["csd_continuousDischarge"]]`; key column: `maxpostDischarge` (discharge measurements). Plot using ggplot with endDate and maxpostDischarge columns.

### Channel Geometry Data (DP1.20048.001 - Discharge Field Collection)

Uses Acoustic Doppler Current Profiler (ADCP) field surveys. Data location: list element `dsc_fieldDataADCP`. Contains hydraulic geometry parameters: `sectionArea`, `waterDepth`; derived field: `Channel_Width = sectionArea/waterDepth`. Enables analysis of relationships between hydraulic parameters (e.g., waterDepth vs. sectionArea).

### Rating Curves (DP4.00133.001 - Stage-Discharge Rating Curves)

Provides rating curves used to produce continuous discharge from pressure transducers. Access via: `Arik_RC$sdrc_gaugeDischargeMeas`. Key columns: `gaugeHeight`, `streamDischarge`. Visualizes stage-discharge relationships.

## Water Chemistry Data

### Grab Sample Data (DP1.20093.001 - Water Quality/Chemistry)

Includes anions, cations, conductivity, pH, carbon forms, nutrients (total, dissolved, particulate). Two data sources:
- `swc_domainLabData`: NEON domain lab collections
- `swc_externalLabDataByAnalyte`: External contracted lab data

Analytes available: unique analytes accessed via `unique(Arik_ExternalWC$analyte)` (includes Fe, NO3+NO2-N, etc.). Extract subset by analyte; plot over collection date (`collectDate`) and concentration (`analyteConcentration`).

### Continuous Sensor Data (DP1.20288.001 - Water Quality/YSI EXO 2)

In situ multiparameter sonde data. Data access: `Arik_WQ$waq_instantaneous`. Sensors measure: temperature, conductance, pH, fluorescence dissolved organic matter (fDOM), dissolved oxygen. Key columns: `specificConductance`, `localDissolvedOxygenSat`, `startDateTime`. Large datasets may require plotting optimization.

### Additional Water Chemistry Sensors

- SUNA V2 Nitrate Sensor (DP1.20033.001): nitrate, absorbance at 254 nm

## Summarized attachments
- **Ecology- Download Neon Data** (https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%201/NEON%20Data.ipynb, notebook): Comprehensive notebook demonstrating NEON data repository download and analysis using R package neonUtilities, covering hydrology (discharge DP4.00130.001, channel geometry DP1.20048.001, rating curves DP4.00133.001), water chemistry (grab samples DP1.20093.001, in situ sensors YSI EXO DP1.20288.001), and biodiversity datasets (macroinvertebrates DP1.20120.001, fish DP1.20107.001, benthic microbes DP1.20086.001) with examples from Arikee River site (ARIK) for data download, extraction, visualization, and assignment tasks.
- Photosynthetically Active Radiation (PAR): key input for ecosystem models

## Biodiversity Data

### Macroinvertebrate Biodiversity (DP1.20120.001 - Macroinvertebrate Collection)

Routine collections at all NEON aquatic sites. Data access: `ARIK_MI$inv_taxonomyProcessed` (processed taxonomy). Full taxonomy columns: phylum, subphylum, class, subclass, infraclass, superorder, order, suborder, infraorder, superfamily, family, subfamily, tribe, subtribe, genus; plus `individualCount`. Store as data frame: `as.data.frame()`. Select/export key columns; save as RDS file: `saveRDS(ARIK_MI_Taxonomy, "~/neon_data/biodiversity/ARIK_MI_Taxonomy.rds")`.

### Fish Diversity (DP1.20107.001 - Fish Population Survey)

Data access: `ARIK_Fish$fsh_bulkCount` (bulk count format). Fish taxonomy stored as single `scientificName` column (genus + species only), differs from macroinvertebrate multi-column format. Processing: use dplyr `group_by(scientificName)` and `summarize(Total_Count = sum(bulkFishCount))` for species counts. Visualize with ggplot bar plots. Save as RDS: `saveRDS(ARIK_Fish_Taxonomy, "~/neon_data/biodiversity/ARIK_Fish_Taxonomy.rds")`.

### Microbial Diversity (DP1.20086.001 - Aquatic Benthic Microbial Community Composition)

Abundance data: archaea, bacteria (16S), fungi (ITS). Two metadata dataframes:
- `mcc_benthicSeqVariantMetadata_16S`: prokaryote sequences
- `mcc_benthicSeqVariantMetadata_ITS`: fungal sequences

Each contains URLs to CSV files (not abundance directly). Download/combine CSVs using custom function with dplyr `lapply()` and `bind_rows()`. Datasets include multiple substrate types (episammon/sand, epiphyton/benthic plants). Taxonomy format: `completeTaxonomy` column with domain→species delimited by semicolons; individual taxonomic levels separate columns. Output: large high-abundance/high-species count datasets. Key metrics: row count (dataset complexity), unique OTU count (operational taxonomic units; species-equivalent for microbial ecology accounting for asexual reproduction/horizontal gene transfer). Save combined data: `saveRDS(ARIK_combined_microbe_data, "~/neon_data/biodiversity/ARIK_combined_microbe_data.rds")`.

## Assignment: Multi-Site Data Download and Visualization

**Instructions**: Download datasets from two different NEON sites for each data group.

**Graphical Requirements** (1 year each):
- Discharge hydrograph
- Channel geometry plots
- Rating curve (stage-discharge relationship)
- Water quality sonde continuous data (e.g., conductance, dissolved oxygen)
- Photosynthetically active radiation (PAR)

**Biodiversity Order-Level Analysis**:
- Fish biodiversity: figure with species taxonomic Order by counts
- Macroinvertebrate biodiversity: species taxonomic Order by counts
- Microbial biodiversity: unique OTU count from dataset

**Deliverable Format**: Visualizations presenting downloaded data from multiple NEON sites demonstrating competency in neonUtilities access, data extraction, and ecological analysis.

## External Resources

**GitHub Repository**: https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%201/NEON%20Data.ipynb

**NEON Data Portal**: https://data.neonscience.org/data-products/explore

**Key Concepts**: 
- NEON site codes (ARIK = Arikee River; etc.)
- Data product IDs (DPIDs): unique codes for each dataset
- Grab samples vs. continuous sensor data
- Taxonomy formatting variations (multi-column vs. single-column)
- RDS file format for data storage/sharing
