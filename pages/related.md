---
title: Related
permalink: "/related/"
layout: default
---

# Standardization Projects and Groups Related to FMI

The FMI development is organised as a Modelica Association Project (MAP) inside the
[Modelica Association](https://www.modelica.org/).
See also [History](http://fmi-standard.org/history/).

## MAP SSP
In many applications there is the need to design, simulate and execute a network of components (simulation models,
software, hardware etc.). In order to be able to do this tool independently and seamlessly, the purposes
of the “System Structure and Parameterization of Components for Virtual System Design (SSP)” project are:

 - Define a standardized way to store and apply parameters to these components.
 - Define a standardized format for the connection structure for a network of components.
 - The developed standard / APIs should be usable in all stages of development process (architecture definition, integration, simulation, test in MiL, SiL, HiL).

Link to [project page](www.ssp-standard.org).

## MAP DCP

The DCP is a platform and communication medium independent standard for the integration of real-time systems into simulation environments. The DCP is standardized by the Modelica Association, where it is maintained as a Modelica Association Project (MAP). 

The DCP is defined in a way such that it supports the integration of FMI based systems within DCP slaves. This applies to FMI for Model Exchange as well as FMI for Co-Simulation. The DCP state machine is designed that it matches operations defined in the state machine of the FMI. Furthermore, the DCP slave description file is aligned to the model description file of the FMI. The data types defined in the DCP slave description file may also be converted to FMI compatible data types. This principle supports FMI-based simulation models, considering the fact that FMI is one of the most common co-simulation standards today.   

Whereas the FMI represents an application programming interface (API), the DCP represents a communication protocol. Therefore, it becom
es possible to integrate various kinds of systems. The DCP specification is suitable for a broad range of computing platforms. It 
may be implemented on hardware as well as in software. Typical examples are middleware, runtime environments, (virtualized) operating
 systems, electronic control units, FPGAs, and many more. 
 
Link to [project page](https://dcp-standard.org/).


## ASAM XIL-MA

At the beginning of the ITEA2 project MODELISAR (the project in which FMI was initially developed) it was planned
to develop FMI for Applications. The intention was to specify an API for simulation tools that allows the
access of model parameters, stimulations and simulation results and to control simulation experiments as
well. The API was supposed to provide tool independent access to simulation computations for optimization
tools, test management and workflow definition tools.

The project group noticed the parallel work of the ASAM XIL standardization group. Thus, both groups came to
the conclusion not to develop a parallel standard but to cooperate. The result of this cooperation is available
as ASAM XIL-MA, which is a subset from ASAM XIL standard. It contains the model access port specification
as well as necessary common functionality for a proper operation of the model access. XIL-MA is open to public
and the documentation of the standard can be obtained from ASAM for free without membership.

Link to [specification](https://www.asam.net/index.php?eID=dumpFile&t=f&f=991&token=43378ad14e9b23b84a2f97dfb2339eddd058f032).

## ProSTEP Smart System Engineering

One of the topics of the Smart Systems Engineering project is to find solutions for the cross-disciplinary and
cross-enterprise exchange of behavioral models. The Functional Mockup Interface (FMI) is viewed as the basic
technology for the exchange.

Link to [project page](http://www.prostep.org/en/projects/smart-systems-engineering.html).

## FMI for PLM

FMI for PLM was developed as part of the ITEA2 project MODELISAR.
The intention is to provide a generic way to handle all FMI related data needed in a simulation of systems in a “Product Lifecycle Management” system.

This includes:

- Functional Mock-up Units data needed for: edition, documentation, simulation, validation
- Co-simulation data needed for: edition, simulation, and results management
- Result valuation data needed for: post-processing, analysis, report

Generic processes are defined here, as well as a format description to communicate between the PLM system and the authoring tools.

**Version 1.0 was released on Mar. 31, 2011.**

<a class="btn btn-outline-primary" href="https://svn.modelica.org/fmi/branches/public/specifications/v1.0/FMI_for_PLM_v1.0.zip"><i class="fa fa-download mr-1"></i> Complete Package</a>
<a class="btn btn-outline-primary ml-2" href="https://svn.modelica.org/fmi/branches/public/specifications/v1.0/FMI_for_PLM_v1.0.pdf"><i class="fa fa-file mr-1"></i> Specification Only</a>
