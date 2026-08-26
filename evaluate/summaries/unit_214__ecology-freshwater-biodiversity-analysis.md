---
title: "Ecology: Freshwater Biodiversity Analysis"
unit_id: 214
course_id: 0
level: "Expert"
slug: ecology-freshwater-biodiversity-analysis
is_course: 0
---

# Ecology: Freshwater Biodiversity Analysis

Expert-level ecology module taught in R, delivered as a Jupyter notebook "JN-Freshwater Biodiversity Analysis" hosted at github.com/jakehosen/cybertraining_ecology (Level 2, "Freshwater Biodiversity Analysis.ipynb"). It teaches analysis of freshwater community diversity and composition for aquatic organisms from microbes to fish using data from the National Environmental Observation Network (NEON) data portal (data.neonscience.org). Data are accessed with the R package neonUtilities (loadByProduct); the environment also loads ggplot2, doBy, lubridate, dplyr, reshape2, and stringr.

Setting up the R environment. Loads neonUtilities, ggplot2, doBy, lubridate, dplyr, reshape2, stringr; references the neonUtilities package documentation (neonscience.org NEON Data STACKR tutorial) and NEON field-site metadata.

Fish Diversity. Downloads NEON fish survey data (data product DP1.20107.001, include.provisional=TRUE) for three aquatic sites: King's Creek (KING), Lower Hop Brook (HOPB), and Mayfield Creek (MAYF). Extracts the fsh_bulkCount list element, uses lubridate (year/month) and summaryBy to build fish_counts_sum (species counts per site, month, year, scientificName).

Diversity metrics. Introduces alpha, beta, and gamma diversity (illustrated by DiversityGraphic.jpg).

Alpha Diversity covers richness, evenness, and composite metrics. Richness: computed with summaryBy(length) on scientificName; visualized with ggplot geom_point/geom_line line plots and geom_jitter plots with stat_summary (mean_cl_boot), referencing geom_boxplot. Statistical testing: linear model (lm) ANOVA of richness by siteID, followed by a Tukey HSD test (HSD.test from the agricolae package, alpha=0.05) placing KING in group a and HOPB/MAYF in group b; discusses Type I/II error (link to rpubs.com Tukey post-hoc article) and adds group labels via geom_text. Diversity: defines Shannon Diversity H' = -Σ(p_i·ln(p_i)) with a custom shannon_diversity() function, using dplyr pipe/group_by/summarize per site_date. Evenness: Pielou's evenness index computed as Shannon diversity divided by richness.

Beta-Diversity. Explains distance/dissimilarity metrics Euclidean (Pythagorean, with generalized n-dimensional formula), Manhattan, and Bray-Curtis (illustrated by DistanceGraphic.png), with full equations. Converts long to wide format via acast (reshape2) into fish_counts_wide, computes Euclidean and Bray-Curtis distance matrices with vegdist from the vegan package (also loads ecodist). Ordination: describes Principal Coordinate Analysis (PCoA), Non-Metric Multidimensional Scaling (NMDS), and Correspondence Analysis (chi-square distance). PCoA run with pco() (ecodist, negvals handling per Legendre and Anderson 1999), plotted with ggplot, sites parsed from rownames via str_split_fixed (stringr). NMDS run with metaMDS (k=2, trymax=100), assessed with stressplot (Shepard plot), points plotted on MDS1/MDS2.

Gamma Diversity: total taxa richness via length(unique(scientificName)); exercise to compute Shannon and evenness for the full dataset.

Macroinvertebrate Diversity. Downloads NEON benthic macroinvertebrate data (data product DP1.20120.001) for KING/HOPB/MAYF, extracts inv_taxonomyProcessed. Organizes counts by genus (summaryBy), removes NA genera, computes genus richness and jitter plots. %EPT Taxa: percentage of taxa from orders Ephemeroptera, Plecoptera, and Trichoptera (labeled here as stoneflies/mayflies/caddisflies) as a water-quality indicator, computed via acast order-count wide table and row-wise math (EPT_count, total_ind_count, Percent_EPT). Mentions functional feeding groups (Shredders, Scrapers, Collector/Gatherers, Predators) and a review article by Kenneth W. Cummins (gavinpublishers.com). Macroinvertebrate Beta Diversity: Bray-Curtis PCoA of genus counts, ggplot with stat_ellipse 95% confidence ellipses. Beta-diversity statistical tests: ANOSIM (statistic R, permutations=9999, grouping by site, date, site_date) and ADONIS (non-parametric MANOVA permutation test; notes adonis2 as the updated vegan function), compared to Kruskal-Wallis. Concludes with an exercise applying NMDS or Correspondence Analysis plus ANOSIM/Adonis.

Learning objectives: access NEON freshwater biodiversity data via neonUtilities; compute and visualize alpha (richness, Shannon, Pielou evenness), beta (Euclidean/Manhattan/Bray-Curtis distances, PCoA/NMDS ordination), and gamma diversity; apply ANOVA/Tukey, ANOSIM, and Adonis significance tests; and use specialized macroinvertebrate metrics (%EPT).

## Summarized attachments

- **JN-Freshwater Biodiversity Analysis (notebook)** (GitHub jakehosen/cybertraining_ecology/Level 2/Freshwater Biodiversity Analysis.ipynb, Jupyter notebook): Expert-level ecology module in R teaching freshwater community diversity analysis for aquatic organisms (microbes to fish) using NEON data portal data accessed via neonUtilities package. Fish diversity: downloads DP1.20107.001 for King's Creek (KING), Lower Hop Brook (HOPB), Mayfield Creek (MAYF); extracts fsh_bulkCount, uses lubridate for date/month/year, summaryBy for species counts. Diversity metrics: alpha (richness via summaryBy length, Shannon diversity H'=-Σ(p_i·ln(p_i)), Pielou's evenness = Shannon/richness), visualized with ggplot geom_point/geom_jitter, stat_summary (mean_cl_boot); ANOVA/Tukey HSD test (agricolae package). Beta diversity: Euclidean/Manhattan/Bray-Curtis distance metrics (vegan vegdist, ecodist), PCoA (Principal Coordinate Analysis) and NMDS (metaMDS, stressplot Shepard plot) ordination; Correspondence Analysis. Gamma diversity: total taxa richness. Macroinvertebrate diversity: NEON DP1.20120.001 benthic data, genus-level counts, %EPT taxa (Ephemeroptera/Plecoptera/Trichoptera water-quality indicator), functional feeding groups (Shredders/Scrapers/Collector-Gatherers/Predators; Cummins review). Beta tests: ANOSIM (R statistic, permutations=9999) and Adonis (non-parametric MANOVA, adonis2 vegan function). Visualization: ggplot stat_ellipse 95% confidence ellipses for PCoA.
