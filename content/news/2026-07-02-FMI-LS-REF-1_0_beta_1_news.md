---
title: Beta version v1.0.0-beta.1 of the FMI Layered Standard References (FMI-LS-REF) published
date: 2026-07-01
---

# Beta version v1.0.0-beta.1 of the FMI Layered Standard References (FMI-LS-REF) published

The FMI Project is happy to announce the Pre-Release v1.0.0-beta.1 of the FMI Layered Standard References (FMI-LS-REF)! 
Many thanks to the FMI Project - especially to the working group leader Pierre R. Mai - for their contributions!

This layered standard provides the capability to clearly designate the roles of additional related files included in an FMU in a structured way. 
These files are described in the layered standard manifest file, which is part of the FMU archive. 
In this way, an FMU can be shipped together with related files that are helpful in understanding and correctly using the FMU in a recognizable way.
Note that this layered standard does not mandate the inclusion of any related files with an FMU. 
It only provides a structured way to describe such files, if they are included. 
The included related files can be of arbitrary types, as long as their roles are described in the layered standard manifest file. 
This layered standard can be used in addition to other layered standards, and allows the central description of related files included with the FMU, independently of their use in other layered standards.
Thus an implementation can treat the related files described in this layered standard in a uniform way, regardless of whether they are used in other layered standards or not, and regardless of whether the other layered standards are supported by the implementation or not.

The experiments format that was formerly part of this layered standard can be used beyond FMI and will therefore be defined in the "harmonized specification" ma-hs-experiments developed by the new Coordination Project within Modelica Association, see https://github.com/modelica/ma-hs-experiments.

Learn more here: https://github.com/modelica/fmi-ls-ref/ and https://github.com/modelica/fmi-ls-ref/releases/tag/v1.0.0-beta.1


