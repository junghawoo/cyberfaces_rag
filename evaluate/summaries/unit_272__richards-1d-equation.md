---
title: "Richard's 1D Equation"
unit_id: 272
course_id: 0
level: "Expert"
slug: richards-1d-equation
is_course: 0
---

# Richard's 1D Equation

Jupyter Notebook tutorial on solving Richards Equation for 1D water movement in soil. GitHub: https://github.com/I-GUIDE/hydroewd/blob/main/Richard%20Eqn/Richard%201D.ipynb.

Richards Equation solver for modeling soil water dynamics. Python libraries: matplotlib, numpy, scipy (odeint ODE solver, interp1d interpolation), vanGenuchten (soil moisture properties).

Soil property model: HygieneSandstone properties accessed via vanGenuchten module (thetaFun: soil water content, CFun: capillary pressure, KFun: hydraulic conductivity).

RichardsModel function parameters: psi (pressure head array at each node), t (time array), dz (vertical grid spacing), n (number of nodes), p (soil property model), vg (soil property module), qTop (top boundary flux/infiltration), qBot (bottom boundary flux/drainage), psiTop (pressure head at top boundary), psiBot (pressure head at bottom boundary).

Boundary conditions: Top boundary (infiltration): specified flux qTop or calculated from psiTop; Bottom boundary (drainage): specified flux qBot, defined pressure head psiBot, or free drainage.

Internal node calculations: Hydraulic conductivity at each node (Knodes); average conductivity between nodes (Kmid); flux at internal nodes calculated from pressure head gradient.

Continuity equation: Change in pressure head over time dpsidt = -(q[i+1]-q[i])/dz / C (where C is capillary pressure).

Model setup: Boundary conditions (qTop=-0.01 m/day infiltration, qBot=[] free drainage); spatial grid (dz=0.1m spacing, ProfileDepth=5m total, z=profile depths); temporal grid (t=0 to 10 days, 101 time steps); initial conditions (psi0=-z negative pressure head with depth).

Solution: odeint ODE solver (scipy.integrate) with mxstep=5000000 maximum steps.

Post-processing: Calculate water content (theta), total profile storage (S), storage change rate (dS), infiltration flux (qI), discharge flux (qD).

Visualization: Vertical profiles (pressure head ψ and water content θ with elevation z vs time); Timeseries plots (change in storage, infiltration, discharge over time).

Output plots: Soil properties (theta, C, K vs ψ), vertical profiles at different time steps, timeseries of water fluxes and storage.

## Summarized attachments
- **Jupyter Notebook (Richard's 1D Eqn)** (github.com/I-GUIDE/hydroewd, notebook): Jupyter Notebook implementing Richards Equation solver for 1D water movement in soil using scipy odeint ODE solver. Uses vanGenuchten soil property model (HygieneSandstone example) with functions for soil water content (thetaFun), capillary pressure (CFun), and hydraulic conductivity (KFun). Implements RichardsModel function with boundary conditions (infiltration, drainage, free drainage), internal node flux calculations, and continuity equation. Post-processing includes water content calculations, storage changes, and visualization of vertical pressure head/water content profiles and time-series plots of water fluxes.
