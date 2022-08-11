---
title: FAQ
permalink: /faq/
layout: default
toc: true
---

# General questions about FMI

## What are the new features of FMI 3.0?

- New FMU kind "Scheduled Execution":  
  Allows coupling several FMUs with one, external scheduler.

- Clocks:  
  Introduce clocks for synchronization of variable changes across FMUs. 

- Co-Simulation with events:  
  Introduces early return and event mode in co-simulation.

- Array variables:  
  Allow FMUs to communicate multi-dimensional variables and change their sizes using structural parameters.

- Numeric Variable Types:
  Adds 8, 16, 32 and 64-bit signed and unsigned integer and single precision floating point variable types to improve efficiency and type safety when importing / exporting models from the embedded, control and automotive domains.

- Binary Data Type:
  Adds an opaque binary data type to FMU variables to allow, for instance, efficiently exchanging of complex sensor data.

- Intermediate Variable Access:  
  Allow access to intermediate input and output values between communication time points from the FMU to disclose relevant subsystem behavior for analysis or advanced co-simulation master algorithms for enhanced numerical stability.

- Source Code FMUs:  
  Provide a build description file to improve automatic import of source code FMUs.

- Terminals and Icons:  
  Help the user to build consistent systems from FMUs and render the systems more intuitively with better representation of structured terminals (for instance busses and physical connectors) in a special XML file.

- Extra directory:
  Adding a new folder in the ZIP Archive representing an FMU, providing additional data to travel with the FMU which can be modified by different tools, allowing for layered standards.

## What are the license and usage conditions for the FMI standard?

Access and use of the FMI standard is free of charge. However, vendors may charge for their tools to support the FMI standard, either by exporting FMUs or by importing FMUs.

**To be clear: While the FMI standard is open and free, commercial implementations might not be.**


## How can I join the FMI mailing lists?

- The “FMI-Info-Mailing list” was discontinued (due to GDPR concerns).
  Please [subscribe to the MA Newsletter](https://creativeconnections.us12.list-manage.com/subscribe?u=0be901f875b69817eddd7e71b&id=0cb2cf5b72&group[20249][2]=true).
- The “FMI design” Mailing list is used by active developers of FMI (typically members of the FMI Advisory or Steering Committee).
- The “FMI Steering” Mailing list is used by members of the FMI Steering Committee. To join you need to be a member of the FMI Steering Committee.


## How is FMI related to Modelica?

- Technically FMI is not related to Modelica, and can be seen as a complementary technology.
- The intention of the FMI project is to be neutral with respect to tools, technologies (e.g. solvers, OS, files, systems…) and languages (including Modelica).
- The FMI standard is developed as a Modelica Association Project within the Modelica Association, an organization focused on the “coordinated standardization and development of software technology and methods in the area of cyber physical- systems and systems engineering”, see the Modelica Association Bylaws and the History page


## Does my simulation tool support FMI?

Please see the FMI [tools page](https://fmi-standard.org/tools/) for a list of tools for that tool vendors have announced their support of FMI.

**While the FMI project defines cross check rules, the tool vendors carry sole responsibility for their stated FMI support and the provided compatibility results.**


## Where can I get help when I have problems related to FMI in my simulation tool?

- Typically an exporting and an importing tool are involved in FMI-based simulation. So if problems occur and if it is not obvious which tool causes the problem, you should communicate the problem to the support team of both involved tools
- As a general discussion forum about FMI, you may use the FMI forum on Stack Overflow


# I'm a developer and want to support FMI with my tool

## What and in which order should I read/do to get started with FMI technology?

That depends mostly on your background knowledge. We assume here you already have fundamental knowledge of simulation technology (ODE vs. DAE, zero-crossing, state/time events, derivatives etc.):

- First make a quick pass trough the [standard document](https://github.com/modelica/fmi-standard/releases/download/v2.0.1/FMI-Specification-2.0.1.pdf).
- Then browse and play with the available [3rd party development toolkits](https://fmi-standard.org/downloads/).
- Read the implementation hints contained in [FMI_for_ModelExchange_v1.0.zip](https://svn.modelica.org/fmi/branches/public/specifications/v1.0/FMI_for_ModelExchange_v1.0.1.pdf) - not yet available for FMI 2.0.
- Re-read the [standard document](https://github.com/modelica/fmi-standard/releases/download/v2.0.1/FMI-Specification-2.0.1.pdf) in detail.


## Does FMI 2.0 support Partial Differential Equations (PDEs)?

There are two kinds of FMI variants: Model Exchange and Co-Simulation.

Model-Exchange FMUs encode ODEs. PDE-support is not planned yet, but the demand for it is increasing.

The second kind, Co-Simulation FMUs, can contain any kind of simulation component because it does not expose states. So as long as you want to simply encapsulate PDEs, this could be done.

But explicitly exposing a PDE to a solver using FMUs is currently not supported.


## I added my test FMUs/Cross-Check results but the tools page does not show "green". Why?

The Cross-Check Rules list a number of conditions before turning an entry “green”. In short:

- Exporting tools must provide at least 3 FMUs and at least one importer must report successful import.
- Importing tools must report (and prove) successful import of at least 3 FMUs of at least 3 exporting tools.

Please refer to the [FMI Cross-Check Rules](https://github.com/modelica/fmi-cross-check/blob/master/FMI-CROSS-CHECK-RULES.md).
