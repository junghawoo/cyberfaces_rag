---
title: "Gempack User Manual"
unit_id: 22
course_id: 1
level: "Foundation"
slug: gempack-user-manual
is_course: 0
---

# Gempack User Manual

## Summary

GEMPACK is a comprehensive Fortran-based software system for implementing and solving computable general equilibrium (CGE) and economic models. This manual (Release 12.2+, ISBN 978-1-921654-90-9) covers the complete GEMPACK ecosystem authored by Mark Horridge, Michael Jerie, Dean Mustakinov, and Florian Schiffmann. The documentation includes extensive guidance on Windows, Linux, Mac OS X, and cross-platform usage.

**Core System Components:** GEMPACK comprises command-line Fortran programs (TABLO, GEMSIM, SLTOHT, SEEHAR, MODHAR) and Windows graphical interfaces (TABmate, WinGEM, RunGEM, AnalyseGE, ViewHAR, ViewSOL, RunDynam). The TABLO program translates TAB (TABLO input) files into either Fortran TABLO-generated programs or GEMSIM bytecode auxiliary files (GSS/GST). GEMSIM interprets these auxiliary files for simulation without compilation.

**Installation & System Requirements:** Installation targets Windows PCs (32-bit and 64-bit, Windows 7-10), with source-code and unlimited/limited executable-image versions available. System environment variables (PATH, GEMPACK licence file handling) require configuration. Anti-virus programs must be configured to allow GEMPACK operations. Performance optimization uses math library settings. Fortran compilers (LF90, LF95, GFortran, Intel) are supported for source-code versions.

**Simulation Workflow:** Three-step process: (1) Run TABLO on TAB file to create TABLO-generated program (option WFP) or GEMSIM auxiliary files (option PGS); (2) Compile/link or run GEMSIM with Command file (CMF) specifying data files, closure (exogenous/endogenous variable assignment), and shocks; (3) View results via ViewSOL or AnalyseGE. Closure swaps toggle variable assignments; shock statements specify percentage changes, absolute CHANGE statements, or FINAL_LEVEL assignments.

**TABLO Language & Model Building:** TABLO is a domain-specific language for model specification combining declarative and imperative features. Core statements include: SET (defines index sets), VARIABLE (levels variables with automatic linear counterparts prefixed p_), COEFFICIENT (parameters, scalars), EQUATION (model equations, can be LINEAR), FORMULA (variable definitions/data calculations), READ (read data from files), FILE (logical file declaration). Files use Header Array (HAR) format with set/element information. Comments use ! ... ! or # ... # delimiters. Data manipulation uses FORMULA & EQUATION combined statements.

**File Types & Management:** Key file suffixes include TAB (TABLO input), EXE (TABLO-generated program), GSS/GST (GEMSIM auxiliary), HAR (Header Array data), SL4 (Solution file), CMF (Command file), MIN (Model information), STI (Symbol Table Index), AXT (auxiliary text), CVL (CVL file), LU (equations/LU factorization), SLC/UDC/AVC (post-simulation). Filename rules prohibit spaces; use <CMF> substitution token for dynamic naming. Updated data files read intermediate results.

**Advanced Model Features:** Intertemporal models use recursive formulas over time-period sets with INTEGER coefficients for counting years. Conditional functions/equations support logical branching. Linearizing equations requires differentiation rules (TABLO automatically linearizes declared variables). Homogeneity testing validates model logic. Condensation reduces model dimensions via variable substitution using TABLO condensation actions. CondOpt tool finds optimal condensation strategies.

**Solution & Computation:** Closure checking ensures well-posed systems (equations count = endogenous variable count). Singular matrix detection during initial closure check. Multi-step simulations decompose shocks sequentially; solution uses Johansen (linearized) or levels method. Parallel processing exploits multi-processor machines. Memory management via coefficient arrays and file strategies. Pivoting strategies and LU factorization handling documented. Run-time errors include handling negative values, division errors, and solver divergence.

**Data Input/Output & Results Processing:** HAR files store multi-dimensional coefficient arrays with headers. SEEHAR converts HAR to text; SLTOHT processes SL4 solution files to HAR or spreadsheet formats. ViewSOL displays results (Pre/Post/Change values) interactively. AnalyseGE integrates data, equations, results for decomposition analysis. ACCUM/DEVIA compute accumulation and differences. Spreadsheet output via SLTOHT options. Submatrix nonzeros information files (smnzinffile) document solution structure.

**Model Examples & Tutorials:** Supplied models include Stylized Johansen (SJ), ORANI-G variants (ORANIG98, ORANIG01, ORANIF), and ORANI-INT (multi-sector rational expectations). WinGEM guides users through model specification workflow. RunGEM provides convenient GUI for simulation/results viewing. Hands-on tutorials (chapters 42-46) cover model setup, data examination, TABLO implementation, closure modification, SAGEM batch simulations.

**Command-Line Operation & Utilities:** Interactive/batch modes with stored-input (sif) and auto-submit (asi) options. Log file output, screen control (-los, -lon options). SEENV examines closure from environment files. TEXTBI extracts TAB/STI/CMF from AXT/SL4/CVL files. SUMEQ extracts equation summary info. Automated homogeneity testing. Translation between GEMPACK HAR and GAMS GDX data files (gdxhar). Complement/complementarity statements for non-linear models via SAGEM simultaneous Johansen solver.

**Platform & Version Management:** Source-code GEMPACK requires Fortran compiler; executable-image versions pre-compiled. Licence activation for certain versions. Running TABLO-generated programs on other machines requires licence. Exe-image and source-code can be used together. Limited executable-image size constraints documented. Unix/Linux/Mac OS X support with limitations. Converting binary files between LF90/F77L3 and Intel/LF95/GFortran formats.

**Post-Simulation Analysis:** Display files show selected results. Writes to terminal/files at all multi-step simulation stages. Assertions validate result ranges; range tests on coefficients. Transfer statements, subtotals via TABLO statements. Equations files and LU files document linearized equations. Assertion failures handled on preliminary/PostSim passes. Decomposition analysis via recursive formula inspection.

The manual includes extensive cross-referenced chapters (81 total), detailed contents, index with topic IDs for error message references, and recommendations for experienced vs. new users. Citation guidance provided; GEMPACK acknowledgement required for published results using the software.

## Summarized attachments
- **GEMPACK user manual** (https://www.copsmodels.com/gpmanual.htm, link): Comprehensive Fortran-based software documentation for implementing and solving computable general equilibrium (CGE) and economic models, including TABLO language specification, file formats, installation procedures, simulation workflows, Windows/Linux/Mac OS X platform support, and extensive hands-on tutorials.
