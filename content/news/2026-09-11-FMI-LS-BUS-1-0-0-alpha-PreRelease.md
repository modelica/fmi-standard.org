---
title: v1.0.0-alpha.1 Pre-Release of FMI Layered Standard for DAE (FMI-LS-DAE) published
date: 2026-09-11
---

#  v1.0.0-alpha.1 Pre-Release of FMI Layered Standard for DAE (FMI-LS-DAE) published

The FMI Project is happy to announce the pre-release v1.0.0-alpha.1 of the FMI Layered Standard for DAE (FMI-LS-DAE) that brings support for Differential Algebraic Equations to FMI.
Many thanks to the the whole working group and especially to the working group leaders Andreas Heuermann (Santa Ana Research Ininstute) and Joel Andersson (FMIOPT https://fmiopt.com/)!

For the full picture please check out the preprint of our paper "Towards an FMI Layered Standard for DAE: Applications for Simulation and Optimization" for the coming American Modelica and FMI Conference 2026 (https://modelica.org/events/american2026/) on arXive:
https://arxiv.org/abs/2606.22544
There also successful tests in the following tools are reported: CasADi, FMIOPT, Simcenter Twin Activate, and MOO (the dynamic optimization tool of OpenModelica).

From the Pre-Release notes (https://lnkd.in/eSMhRSXp)
This is the first pre-release of the FMI Layered Standard for Differential-Algebraic Equations (FMI-LS-DAE). It specifies how semi-explicit index-1 differential-algebraic equations can be exposed by FMI 3.0 Model Exchange FMUs, so that the algebraic equations and their
associated algebraic variables are solved by the importer instead of inside the FMU.
The specification of version 1.0.0-alpha.1 is published at https://github.com/modelica/fmi-ls-dae/releases/tag/v1.0.0-alpha.1
Being a pre-release, this version is published for review and for prototype implementations. The specification is not yet stable and is subject to change before version 1.0.0 is released.

Key features:
A layered standard manifest stored inside the FMU at /extra/org.fmi-standard.fmi-ls-dae/fmi-ls-manifest.xml, defined by the XML schema fmi3LayeredStandardDaeManifest.xsd.
Declaration of the algebraic variables and of the residual equations of the DAE in the manifest, together with the model structure and the dependencies of outputs, continuous state derivatives, event indicators and residuals. The dependency information preserves the sparsity of the DAE system, which is lost in the corresponding reduced ODE system.
A structural parameter enableDAEModeParameter that switches the FMU between ODE mode and DAE mode. An FMU implementing this layered standard is at the same time a valid FMI 3.0 Model Exchange ODE FMU and defaults to ODE mode, so that importers that do not support this layered standard can use it unchanged.
No extension of the FMI 3.0 C API is required. Algebraic variables and residuals are exchanged through the existing FMI 3.0 getter and setter functions.
As a consequence, index reduction and local non-linear equation solvers are no longer required inside the FMU.
