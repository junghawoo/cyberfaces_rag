---
title: "Lectures"
unit_id: 58
course_id: 2
level: "Foundation"
slug: lectures
is_course: 0
---

# Lectures

Comprehensive lecture series on SIMPLE-G (Simplified International Model of agricultural Prices, Land use and Environment—Gridded version), a multiscale framework for analyzing global-to-local sustainability challenges in land and water resources. Course location: Department of Agricultural Economics, Purdue University. All materials hosted on Dropbox and related platforms.

**Course Foundation & GLASSNET Context**: Presented by Thomas W. Hertel (GLASSNET PI), May 2022. Short Course in Multi-Scale Analysis of Sustainability. GLASSNET (Global-to-Local Analysis of Systems Sustainability) is an international network of networks addressing global sustainable development goals related to land/water resources through global-to-local-to-global analysis that recognizes global forces driving local sustainability stresses while accounting for locality-specific solutions with global consequences. GLASSNET organizational structure includes Maps/Data Visualization/Exploration, Analysis of Tradeoffs/Synergies, Policy Briefs, Community Interactions/Collaboration, Training/Courses, and Modeling Frameworks/Computation. GeoHub provides publishing/sharing infrastructure for data and tools.

**SIMPLE Framework Background**: Development led by Uris Baldos. Economic framework (2011), SIMPLE (non-gridded) model (2012) developed from AAEA presidential address. SIMPLE gridded variants (SIMPLE-G) introduced 2017 onward. Philosophy: avoid unnecessary complexity; create new model variants for each issue rather than adding to existing models. Historical validation (2006-1961) demonstrated that global models over-predicted land conversion due to: (1) absence of price sensitivity in demand, (2) absence of endogenous intensification. SIMPLE used as vehicle for interdisciplinary research in grad-level Global Change/Sustainability Course where students master SIMPLE through 5 lab assignments and undertake original projects in technology/preferences/land and nonland supply variations.

**SIMPLE-G Framework Architecture**: Gridded version avoiding data aggregation, working at physical scientists' resolution. Facilitated by GEMPACK (algebraic substitution of gridded variables solving for market prices with gridded outcomes following). Modeled on GTAP playbook: One basic framework, One database, Many aggregations, Many variants. Core model code features segmented markets. Core gridded datasets begin with ~175 FAO crops. Mapping files determine aggregation/study focus. Development variants: SIMPLE-G-Global (global water scarcity studies), SIMPLE-G-US (US land/water sustainability), SIMPLE-G-US-CS (Midwestern nitrate leaching management), SIMPLE-G-China (China land/water issues), SIMPLE-G-Brazil (domestic infrastructure, international trade, land use change).

**Core Model Structure**: One crop market (all crops, corn-soy composite, etc.), typically two production practices per grid cell (rainfed vs. irrigated), technology varying by grid cell per local conditions/crop composition. Competition for land/water with other uses via grid cell-specific land/water supply functions.

**Lecture Topics (16 Resources)**:

1. **Course Introduction** (Thomas W. Hertel): GLASSNET/SIMPLE-G overview, organizational structure, philosophy, historical context, interdisciplinary applications.

2. **Analytical Foundations - Fixed Price Closure in PE Model** (Thomas Hertel, Srabashi Ray): SIMPLE-G strengths (flexibility, analytical tractability). Factor markets with location-specific inputs (land, water—inelastically supplied) vs. mobile inputs (labor, capital—price-elastic). Zero pure profit condition. Land rent magnification under fixed nonland prices. Gridded analytical model variables (σ, Q, N, L, v_NN, v_LL). Impact of price rise on grid cell output with intensive/extensive margins.

3. **Model Condensation** (Iman Haqiqi): Computational efficiency via GEMPACK/TABLO. Reducing model size before solving linearized equations through omission, substitution, backsolving. Example: 4M unknowns with ~75K grid cells reduced from 45 minutes to 2 minutes solution time (laptop: i7-8th gen, 32GB). TABLO workflow: Check, Condensation, Code generation. Condensation status tracking (In condensed system, Used for BACKSOLVING, ELIMINATED from system).

4. **Nested Production Function** (Iman Haqiqi): Production structure of SIMPLE-G at grid cell level. Production inputs, production functions, nested production functions, constant elasticity of substitution (CES), tree structure, mathematical representations. Sub-regional trade assumptions.

5. **SIMPLE-G Plotting/Visualization** (Iman Haqiqi): Data visualization and exploration tools.

6. **Theoretical Framework Recap** (Uris Baldos): SIMPLE theoretical framework review.

7. **SIMPLE Non-Gridded Data** (Uris Baldos): Database structures (LANDDATA, PARM, SETS) for non-gridded SIMPLE model.

8. **SIMPLE-G Mapping** (Iman Haqiqi): Mapping files determining model aggregation and focus.

9. **SIMPLE-G Road Map of Gridded Modeling** (Iman Haqiqi): Development pathway and strategic direction for gridded model.

10. **SIMPLE-G-Brazil Model Construction and Validation** (Zhan Wang): Development of SIMPLE-G-Brazil (SGB), downscaled to 50,598 grids (5 arcmin). SGB baseline 2017; Brazil gridded, other regions in 16 aggregate areas. Database sources: MapBiomas (cropland), IBGE (harvest area/yield), GCWM (irrigation), FAOSTAT (global crop data), World Bank (demographics), GTAP/GTAP-Bio (non-crop shares/biofuel). Grid-level data development roadmap: cropland (via MCD12Q1 MODIS 500m, GFSAD 30m), crop output, input use/cost shares, gridded parameters. Model validation against historical outcomes and applications to land use/trade scenarios.

11. **SIMPLE-G-CS Parameters, Emulators, Elasticities** (Jing Liu): Parameter estimation, model emulators, and input-output elasticity specifications for SIMPLE-G-China-US Corn-Soy application.

12. **SIMPLE-G-China** (Jing Liu): China-specific application of SIMPLE-G framework addressing land/water sustainability in Chinese agricultural systems.

13. **SIMPLE-G-US-CS Application: Nitrate Leaching Management** (Jing Liu): Water quality application for Midwestern US managing nitrate leaching from corn-soy production systems.

14. **SIMPLE-G1 Interactive Map** (Iman Haqiqi): Interactive visualization tool (GNLD1_p10.html) for exploring SIMPLE-G-Global results.

15. **Segmented Markets in SIMPLE** (Uris Baldos): Market segmentation theory and implementation (key differentiator validated historically for regional outcomes).

16. **Water Supply and Demand** (Iman Haqiqi): Water resource modeling within SIMPLE-G framework.

**Key Technical Tools**: GEMPACK (algebraic modeling system), TABLO (equation specification language), AnalyseGE (post-simulation analysis). Data sources: FAOSTAT, MapBiomas, IBGE, GCWM, World Bank, GTAP/GTAP-Bio, MODIS satellite data, GFSAD. Mathematical methods: CES production functions, linearization, condensation algorithms. Historical validation via regional trade and cropland outcomes.

**Development Status**: Work-in-progress framework striving for reproducible, publishable products. US-focused work furthest advanced with NSF/USDA funding supporting gridded input estimates, cropland supply response, input substitution relationships, hydrology/agronomy integration, and model validation. Replication efforts: China (NSF US-CHN grant), Brazil (NSF CHNS grant with Michigan State University). Europe extension planned. SIMPLE-G-Global provides global coverage at lesser quality data with incorporation of improved national data as available.

**Key References**: Baldos & Hertel (2013, Environmental Research Letters), Hertel & Baldos (2016, Springer e-book), Liu et al. (2017-2018, Environmental Research Letters & Purdue Policy Briefs), Haqiqi et al. (2018, Policy Brief).

## Summarized attachments
- **Course Introduction** (https://www.dropbox.com/s/dydj9719dp7yf6s/Course%20Introduction_TH.pdf?dl=0, PDF): Presented by Thomas W. Hertel, GLASSNET PI, May 2, 2022. Introduces GLASSNET (Global-to-Local Analysis of Systems Sustainability) and SIMPLE-G Short Course. Addresses three sustainability research traps (too disciplinary, too local, too complex) and proposes global-to-local-to-global analysis recognizing global forces driving local stresses while accounting for locality-specific solutions and global consequences.
- **Fixed Price Closure in PE Model: Analytics of Gridded Model** (https://www.dropbox.com/s/va09ux2dpqo9oaa/Analytics%20of%20the%20Gridded%20Model-2022%20Short%20Course.pdf?dl=0, PDF): Presented by Thomas Hertel and Srabashi Ray, May 2, 2022. Covers SIMPLE-G analytical foundations including factor market divisions (location-specific inputs like land/water vs. mobile inputs like labor/capital), land rent magnification, zero pure profit conditions, and gridded analytical model variables (σ, Q, N, L, v_NN, v_LL) with intensive/extensive supply margins.
- **Model Condensation** (https://www.dropbox.com/s/i7ms6h9sec6y6tg/Condensation_2022-04-26.pdf?dl=0, PDF): Presented by Iman Haqiqi, May 3, 2022. Addresses computational efficiency via GEMPACK/TABLO through model size reduction via omission, substitution, and backsolving—reducing 4M unknowns with 75K grid cells from 45 minutes to 2 minutes solution time (i7-8th gen laptop, 32GB RAM).
- **Nested Production Function** (https://www.dropbox.com/s/pof0fo6uo6bfxwh/Nested%20Production%20Structure_2022-04-26.pdf?dl=0, PDF): Presented by Iman Haqiqi, May 3, 2022. Describes SIMPLE-G production structure at grid cell level including production inputs, production functions, nested production functions, constant elasticity of substitution (CES), tree structure representations, and sub-regional trade assumptions.
- **Plot SIMPLE-G Maps** (https://www.dropbox.com/s/rrgr2ft7bv8pie5/Plot%20SIMPLE-G_2022-05-05.pdf?dl=0, PDF): Presented by Iman Haqiqi, May 5, 2022. Covers data visualization and exploration for SIMPLE-G model family with basic plotting approaches and examples of county-level and gridded visualization using the Immediate Impact Model of Local Agricultural Production (IMLAP).
- **Recap of Theory in SIMPLE** (https://www.dropbox.com/s/kyqjw1005g1zpjt/Day1_Theoretical_Framework_2022_v1.pdf?dl=0, PDF): Presented by Uris Baldos, May 2, 2022. Provides theoretical framework review of the SIMPLE model covering key assumptions including aggregate demand for agricultural output and market equilibrium principles.
- **SIMPLE Non-Gridded Data** (https://www.dropbox.com/s/e115wak0a6fmupr/Day2_SIMPLE_Database_2022_v1.pdf?dl=0, PDF): Presented by Uris Baldos, May 5, 2022. Describes SIMPLE database and parameters covering database structures (LANDDATA, PARM, SETS) and data sources including FAOSTAT for agricultural statistics.
- **SIMPLE-G Mapping** (https://www.dropbox.com/s/mcj6fdk1amnsm1s/SIMPLE-G-Mapping_2022-05-04.pdf?dl=0, PDF): Presented by Iman Haqiqi, May 4, 2022. Covers grid cell to regions mapping fundamentals with gridded indices for model aggregation and focus determination.
- **SIMPLE-G Road Map of Gridded Modeling** (https://www.dropbox.com/s/ia8olegs44cocvn/SIMPLE-G%20road%20map_2022-04-26.pdf?dl=0, PDF): Presented by Iman Haqiqi, May 2, 2022. Outlines SIMPLE-G overview and strategic development roadmap for the gridded modeling framework.
- **SIMPLE-G-Brazil Model Construction and Validation** (https://www.dropbox.com/s/0njf57ir1yp73c6/Wang_Shortcourse_2022_SGB%20and%20Validation.pdf?dl=0, PDF): Presented by Zhan Wang, May 4, 2022. Covers development of SIMPLE-G-Brazil (SGB) downscaled to 50,598 grids (5 arcmin) with baseline 2017, gridded and aggregate regions. Data sources: MapBiomas (cropland), IBGE (harvest area/yield), GCWM (irrigation), FAOSTAT (global data), World Bank (demographics), GTAP/GTAP-Bio (biofuel).
- **SIMPLE-G-CS Parameters: Emulators and Elasticities** (https://www.dropbox.com/s/hmjbijqcb75t2vf/Liu_Shortcourse_2022_%20Parameters-emulators-elasticities.pdf?dl=0, PDF): Presented by Jing Liu, May 3, 2022. Covers parameter estimation, model emulators, and input-output elasticity specifications for SIMPLE-G-China-US Corn-Soy application.
- **SIMPLE-G-China** (https://www.dropbox.com/s/3zokzx7b8jg2tco/Liu_Shortcourse_2022_%20SIMPLE-G-China.pdf?dl=0, PDF): Presented by Jing Liu, May 4, 2022. Addresses China-specific application of SIMPLE-G framework for analyzing land and water sustainability in Chinese agricultural systems.
- **SIMPLE-G-US-CS Application: Nitrate Leaching Management** (https://www.dropbox.com/s/a7lxvxdq1368u0j/Liu_Shortcourse_2022_%20Water_quality_applications.pdf?dl=0, PDF): Presented by Jing Liu, May 3, 2022. Covers water quality applications evaluating alternative options for managing nitrogen losses from US corn production in the Midwest, demonstrating SIMPLE-G's capability for environmental management scenarios.
- **SIMPLE-G1 Interactive Map** (https://www.dropbox.com/s/z2gavpj7aosxrlp/GNLD1_p10.html?dl=0, interactive map): Presented by Iman Haqiqi. Interactive visualization tool (GNLD1_p10.html) for exploring SIMPLE-G-Global results and outputs geographically.
- **Segmented Markets in the SIMPLE Model** (https://www.dropbox.com/s/oqv6bx8ry7wjn5u/Day1_Segmented_Markets_2022_v1.pdf?dl=0, PDF): Presented by Uris Baldos, May 2, 2022. Covers market segmentation theory and implementation in SIMPLE as key differentiator validated historically for explaining regional agricultural outcomes.
- **Water Supply and Demand** (https://www.dropbox.com/s/yl7chjo419m21pk/Water%20Supply%20and%20Demand_2022_04_26.pdf?dl=0, PDF): Presented by Iman Haqiqi, May 3, 2022. Covers water balance-economic equilibrium integration within SIMPLE-G framework for water resource modeling and sustainability analysis.
