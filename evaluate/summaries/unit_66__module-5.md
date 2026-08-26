---
title: "EAPS DataMine FAIR: R examples 1"
unit_id: 66
course_id: 3
level: "Expert"
slug: module-5
is_course: 0
---

# EAPS DataMine FAIR: R examples 1

Expert-level module in the EAPS DataMine FAIR course series (Module 5, "R examples 1") consisting of two fetched external web resources: the official CRAN manual "An Introduction to R" (PDF) and the Purdue RCAC Scholar cluster page for R-Studio Desktop access.

## Fetched resources (external URLs)

### Intro to R (link)
URL: https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf — "An Introduction to R: Notes on R, A Programming Environment for Data Analysis and Graphics," Version 4.6.1 (2026-06-24), by W. N. Venables, D. M. Smith, and the R Core Team (with copyrights citing R. Gentleman, R. Ihaka, M. Maechler). The full manual text is included, derived from original S/S-Plus notes written 1990–92 by Bill Venables and David M. Smith at the University of Adelaide; the S language was developed at Bell Laboratories by Rick Becker, John Chambers, and Allan Wilks (key references: The New S Language; Statistical Models in S, ed. Chambers & Hastie; Programming with Data). Contact address R-help@R-project.org; packages via CRAN (https://CRAN.R-project.org). Chapter coverage:

1. Introduction and preliminaries: the R environment; related software/documentation; R vs. statistics systems (SAS, SPSS); R and the X window system on UNIX/Windows/macOS; interactive use (prompt >, q(), mkdir work); getting help (help(), ?, help.start()); command syntax and case sensitivity; command recall; sourcing/sinking output; workspace permanency and removing objects (.RData, rm()).
2. Simple manipulations, numbers and vectors: assignment (<-, c(), assign()); vector arithmetic; regular sequences (seq(), rep()); logical vectors; missing values (NA, NaN, is.na()); character vectors (paste()); index vectors for subsetting; other object types.
3. Objects, modes and attributes: mode and length; changing object length; attributes(); the class of an object (unclass()).
4. Ordered and unordered factors: factor(); tapply() and ragged arrays; ordered factors (example: state-based tax data of Australian states).
5. Arrays and matrices: dim(); array indexing and index matrices; array() function; recycling rule; outer product (outer(), %o%); generalized transpose (aperm(), t()); matrix facilities—matrix multiplication (%*%), crossprod(), diag(); solving linear equations and inversion (solve()); eigenvalues/eigenvectors (eigen()); singular value decomposition and determinants (svd(), det()); least squares fitting and QR decomposition (lsfit(), qr()); cbind() and rbind(); c() with arrays; frequency tables from factors (table()).
6. Lists and data frames: list creation, indexing ([[ ]], $), concatenating lists; data.frame(); attach()/detach(); working with data frames; attaching arbitrary lists; managing the search path (search()).
7. Reading data from files: read.table(); scan(); accessing builtin datasets (data()), loading data from other R packages; editing data (edit(), fix()).
8. Probability distributions: R as statistical tables (d/p/q/r prefixes for distributions—normal, t, F, chisq, binomial, Poisson, uniform, etc.); examining distributions with stem(), hist(), density(), ecdf(), qqnorm(), qqplot() (example datasets: faithful eruptions); one- and two-sample tests including Shapiro-Wilk (shapiro.test), Kolmogorov-Smirnov (ks.test), Student's t test (t.test), F test (var.test), Wilcoxon test (wilcox.test).
9. Grouping, loops and conditional execution: grouped expressions; if/else, for, repeat, while control statements.
10. Writing your own functions: function definition; defining new binary operators (%anything%); named arguments and defaults; the '...' argument; assignments within functions (<<-); advanced examples—efficiency factors in block designs, dropping dimension names for compact printing (no.dimnames()), recursive numerical integration; lexical scope (cube/open.account bank-account closure example); customizing the environment (.Rprofile, .First(), .Last(), options()); classes, generic functions and object orientation (methods(), plot(), summary()).
11. Statistical models in R: model formulae syntax (~, +, :, *, /, ^, I(), poly()); contrasts; linear models (lm()); generic extractor functions (coef(), resid(), fitted(), predict(), anova(), deviance(), vcov()); ANOVA tables (aov()) and model comparison; updating fitted models (update()); generalized linear models—families (gaussian, binomial, poisson, Gamma, inverse.gaussian, quasi) and the glm() function; nonlinear least squares and maximum likelihood (nls(), optim(), nlm()) with the Puromycin-style enzyme kinetics example; non-standard models—mixed models (nlme package: lme(), nlme()), local approximating regression (loess()), robust regression (MASS package: rlm(), lqs()), additive models, tree-based models.
12. Graphical procedures: high-level plotting (plot(), pairs(), coplot(), qqnorm(), hist(), image(), contour(), persp()); low-level commands (points(), lines(), text(), abline(), polygon(), legend(), title(), axis()); mathematical annotation and Hershey vector fonts; interacting with graphics (locator(), identify()); graphics parameters via par() (pch, lty, col, cex, mar, mfrow multiple-figure layouts, axes and tick marks, figure margins); device drivers (postscript(), pdf(), X11()), PostScript for typeset documents, multiple devices (dev.new, dev.off); dynamic graphics.
13. Packages: standard packages; contributed packages and CRAN (library(), e.g. library(boot), library(MASS)); namespaces.
14. OS facilities: files and directories, filepaths, system commands, compression and archives.
Appendix A: a sample session (includes the morley Michelson speed-of-light dataset). Appendix B: invoking R from the command line, under Windows and macOS, and scripting with R (Rscript, R CMD BATCH). Appendix C: the command-line editor (readline editing actions and summary). References, function/variable index, and concept index (entries include QR decomposition, quantile-quantile plots, recycling rule, robust regression, Shapiro-Wilk test, tree-based models, Wilcoxon test, workspace).

### R-Studio Desktop (link)
URL: https://www.rcac.purdue.edu/compute/scholar/ — Purdue RCAC "Compute: Scholar" page. Scholar is a small computer cluster for classroom learning about high performance computing (HPC): 6 interactive login servers and 16 batch worker nodes, usable via a batch job scheduler or interactively through a Linux Remote Desktop, Jupyter notebook server, or R Studio server (Gateway/Remote Desktop launch links). Instructors register classes via the Class Account Request page; a Faculty Guide and Scholar User Guide are referenced. Hardware specifications: front-ends with AMD EPYC 9634 "Genoa" 84-core processors (384 GB) and Intel Xeon Gold 6126 "Skylake" nodes with NVIDIA Tesla V100 32GB GPUs (768 GB); sub-clusters A–J featuring AMD EPYC 7713 "Milan", 7702P "Rome", 7543 "Milan", and 9554 "Genoa" processors, plus GPU nodes with NVIDIA Tesla V100 16GB, A30 24GB (including Multi-Instance GPU/MIG configurations), and A40 48GB. The page also lists RCAC compute resources: Rossmann, Rowdy, Negishi, Geddes, Bell, Anvil, Weber, Gilbreth, Scholar, Hammer, Gautschi; plus Fortress Archive maintenance notice, software catalog, and outages/maintenance links.

## Summarized attachments

- **Intro to R** (`https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf`, PDF): The official CRAN manual "An Introduction to R" (Version 4.6.1, by W. N. Venables, D. M. Smith, and the R Core Team) covering R as a programming environment for data analysis and graphics. Includes 14 chapters spanning R environment setup, data manipulation, statistical models, graphical procedures, and packages, plus appendices on sample sessions and command-line invocation.

- **R-Studio Desktop** (`https://www.rcac.purdue.edu/compute/scholar/`, web page): The Purdue RCAC Scholar cluster page describing a small HPC system with 6 interactive login servers and 16 batch worker nodes designed for classroom learning. Provides access via Linux Remote Desktop, Jupyter notebook server, or R Studio server, and details hardware specifications including AMD EPYC and Intel Xeon processors with NVIDIA GPU options.
