---
title: About
permalink: /about/
redirect_from:
  - /development/
  - /history/
  - /related/
layout: default
---

## Purpose of the Modelica Association Project Functional Mockup Interface

Development and promotion of the Functional Mock-up Interface (FMI) standard. The intention is to simplify the creation, storage, exchange and (re-) use of dynamic system models of different simluation systems for model/software/hardware-in-the-loop simulation, for cyber physical systems, and other applications.

The FMI specifications are published under the CC-BY-SA (Creative Common Attribution-ShareAlike 4.0 International) license, i.e., the license used by Wikipedia. A human-readable summary of the license text is available from [http://creativecommons.org/licenses/by-sa/4.0](https://creativecommons.org/licenses/by-sa/4.0). Source code, such as C-header and XML-schema files, that accompany the specification documents are provided under the [BSD license](https://www.opensource.org/licenses/bsd-license.html) with the extension that modifications must be also provided under the BSD license.

FMI is a registered trademark. The rules for trademark usage are [here](https://svn.fmi-standard.org/fmi/branches/public/docs/Trademark%20Guidelines%20for%20the%20Use%20of%20the%20FMI%20Trademark%20V1.0.pdf).

## Modelica Association Project (MAP) FMI

Today, the core development of the FMI standard is organised as [Modelica Association Project](https://modelica.org/projects) _Functional Mock-up Interface_ under the roof of the [Modelica Association](https://www.modelica.org/). (History below)

Current Project Leader and Deputy:
Andreas Junghanns (Synopsys) and Torsten Blochwitz (ESI ITI) projectleader@fmi-standard.org

Current Members of the Steering Committee:
AVL List, BOSCH, Dassault Systemes, dSPACE, ESI ITI, Maplesoft, Modelon, Siemens PLM, Synopsys

Current Members of the Advisory Committee:
ABB, DLR, Fraunhofer (IIS/EAS First, SCAI), Open Modelica Consortium, PMSF, TLK Thermo, TWT, University of Halle, Wolfram MathCore AB

## How to contribute to the development of the FMI standard

There are FMI tracks at other FMI related events like conferences and design meetings.
If you believe you could benefit from the standard or if you would like to contribute to the improvement or distribution of it, please contact us at: [contact@fmi-standard.org](mailto:contact@fmi-standard.org).

All contributors have to sign the [Corporate Contributor License Agreement (CCLA)](https://svn.fmi-standard.org/fmi/branches/public/FMI_CCLA_v1.0_2016_06_21.pdf).
Therefore, the first step is getting your company to agree and sign the CCLA.
The CCLA ensures that all IP contributed to the FMI standard will be licensed to the Modelica Association (MA) which in turn will sublicense the FMI standard to tool vendors implementing it and end users using it, free of charge.

With the CCLA signed by your company, we will grant you access to our IT infrastructure.
We will add you to the [FMI design mailing list](mailto:design@fmi-standard.org).
There you will be invited to our regular FMI design meetings.
You will get access to the FMI github repositories.
They are the central information hubs for the Modelica Association Project FMI.
Here you can also find which working groups are currently working on FMI Change Proposals (FCPs) and you can decide which one of them to join (email the respective working group leader shown in a wiki table), or, if you have other ideas, you may propose to start and lead a new working group addressing your improvement to the FMI standard by searching for collaborators on the FMI design mailing list and/or presenting your ideas at a face-to-face design meeting.

Companies that have shown continued commitment and valuable contributions will be invited to join the FMI Advisory Committee.
This membership is mostly ceremonial and its most important function is to recognize publicly who is actively helping to develop the FMI standard.

The next level of involvement is membership in the FMI Steering Committee which is the governing body of the MAP FMI.
You have to formally apply, explaining your past, current and future involvement and plans with the FMI standard.
The FMI Steering Committee will vote on your applications.

## Development Process

Today, we largely use github issues and pull requests to technically coordinate our design work.

## First version of the FMI Standard

[MODELISAR](https://itea3.org/project/modelisar.html) was an ![ITEA2](https://svn.fmi-standard.org/fmi/branches/public/img/itea2.png) European project to improve significantly the design of systems and of embedded software in vehicles.
MODELISAR had 29 partners and started in July 2008 and finished, after extension, in December 2011.
FMI 1.0 was one of the results of MODELISAR.

MODELISAR partners:
ARMINES, AIT, ATB, AVL List, Altran, Daimler, Dassault Systèmes, Dassault Systèmes AB, David, DLR, FhG (First, IIS,
EAS, SCAI), Geensoft, Halle University, IFP Energies nouvelles, LMS Imagine, INSPIRE, SIMPACK, ITI, LMS International,
QTronic, Trialog, Triphase, TWT, Verhaert, Volkswagen, Volvo

The core MODELISAR development partners agreed to continue FMI specification work under the roof of the [Modelica Association](https://www.modelica.org/) as newly created [Modelica Association Project](https://modelica.org/projects) _Functional Mock-up Interface_.

## Acknowledgement

The FMI development was partially funded within the ITEA2 project MODELISAR by

<table class="table table-borderless">
  <tr>
    <td> <img src="https://svn.fmi-standard.org/fmi/branches/public/img/bmbf.png" alt="bmbf.png" title="bmbf.png" /> </td>
    <td> <a href="http://www.bmbf.de/en/index.php">BMBF</a> for Daimler AG, DLR e.V., Fraunhofer IIS/EAS, ITI GmbH, Martin-Luther-University Halle-Wittenberg, QTronic GmbH, SIMPACK AG, TWT (BMBF Förderkennzeichen: 01lS08002)
    </td>
  </tr>
  <tr>
    <td> <img src="https://svn.fmi-standard.org/fmi/branches/public/img/dgcis.png" alt="dgcis.png" title="dgcis.png" /></td>
    <td> <a href="http://www.industrie.gouv.fr/portail/une/dgcis.html">DGCIS</a> for Dassault Systèmes, IFPEN, LMS Imagine, Trialog</td>
  </tr>
  <tr>
    <td> <img src="https://svn.fmi-standard.org/fmi/branches/public/img/vinnova.png" alt="vinnova.png" title="vinnova.png" /></td>
    <td> <a href="http://www.vinnova.se/en/">VINNOVA</a> for Dynasim AB, Volvo (funding number: 2008-02291)</td>
  </tr>
</table>

# Standardization Projects and Groups Related to FMI

## MAP SSP
In many applications there is the need to design, simulate and execute a network of components (simulation models,
software, hardware etc.).
In order to be able to do this tool independently and seamlessly,
the purposes of the “System Structure and Parameterization of Components for Virtual System Design (SSP)” project are:

 - Define a standardized way to store and apply parameters to these components.
 - Define a standardized format for the connection structure for a network of components.
 - The developed standard / APIs should be usable in all stages of development process (architecture definition, integration, simulation, test in MiL, SiL, HiL).

Link to [project page](https://ssp-standard.org/).

## MAP DCP

The DCP is a platform and communication medium independent standard for the integration
of real-time systems into simulation environments.
The DCP is standardized by the Modelica Association, where it is maintained as a Modelica Association Project (MAP).

Whereas the FMI represents an application programming interface (API), the DCP represents a communication protocol.
Therefore, it becomes possible to integrate various kinds of systems.
The DCP specification is suitable for a broad range of computing platforms.
It may be implemented on hardware as well as in software.
Typical examples are middleware, runtime environments, (virtualized) operating systems, electronic control units, FPGAs, and many more.

Link to [project page](https://dcp-standard.org/).

## ASAM XIL-MA

The ITEA2 project MODELISAR noticed the parallel work of the ASAM XIL standardization group.
Both groups came discussed and concluded not to develop a parallel standard but to cooperate.
The result of this cooperation is available as ASAM XIL-MA, which is a subset from ASAM XIL standard.
XIL-MA is open to public and the documentation of the standard can be obtained from ASAM for free without membership.

Link to [specification](https://www.asam.net/index.php?eID=dumpFile&t=f&f=991&token=43378ad14e9b23b84a2f97dfb2339eddd058f032).

## ProSTEP Smart System Engineering

One of the topics of the Smart Systems Engineering project is to find solutions for
the cross-disciplinary and cross-enterprise exchange of behavioral models.
The Functional Mockup Interface (FMI) is viewed as the basic technology for the exchange.

Link to [project page](http://www.prostep.org/en/projects/smart-systems-engineering.html).
