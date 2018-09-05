---
title: FAQ
permalink: /faq/
layout: default
toc: true
---

# General questions about FMI

## How are the FMI version numbers defined and what does backwards compatibility of a minor version mean?

According to the FMI development process (link), the version number of an FMI release is defined in the following way:

- Version number: `MajorVersion.MinorVersion.MaintnanceVersion`
- Changes introduced by Major versions don't have to be *backward nor forward compatible*.
- Minor versions within the same Major version have to be backward compatible.
- Maintenance versions must not introduce new features and have to be forward and backward compatible.
- All versions will have semantic version numbers.

Note that **backward and forward compatibility** is with respect to the FMI specification, not with respect to a tool. For example, if FMI 2.1 is backward compatible to FMI 2.0, then every 2.0 FMU must be also a valid 2.1 FMU. As a consequence, a minor version implies restrictions with respect to the previous minor version, especially, but not limited to: (a) new XML elements and attributes, as well as new C API functions must be optional, (b) the argument lists of existing C API functions cannot change (only the meaning of existing arguments can be enhanced, if this is signaled in the modelDescription.xml file with new, optional, XML elements or attributes).

A change to the previous FMI version is called backwards compatible if every FMU compliant with the previous version is also a valid component of the new FMI version. In more detail this means:

- XML elements can be added in the new version, but existing XML elements cannot be removed.
- An existing XML enumeration can be extended, but only in a way that the mapping of the enumeration to Integer does not change for the enumeration values of the previous version.
- New function prototypes can be added in the new version, but existing function prototypes cannot be changed and cannot be removed.
- New struct prototypes can be added in the new version, but existing struct prototypes cannot be changed and cannot be removed.

## Why shall the next FMI release with new features be 3.0 and not 2.1?

After intense struggles to build easy to understand FMI Change Proposals (FCPs), the FMI Steering Committee decided that a point was reached where the cost to keep the FMI 2.1 release backward compatible with 2.0 was too high. Consequently, the decision was reached to rename the next release to "FMI 3.0".

- The alpha feature list remains the same for 3.0 as it was published for 2.1: It is not intended to include additional new features in FMI 3.0 beyond the alpha features list.
- The authors of the FCPs are requested to keep the non-backwards compatible changes at a minimum in order to keep the implementation effort at a minimum.
- We will try to keep the release schedule largely the same: partial reformulation of some FCPs to take advantage of the fact that we are not bound to be backward compatible anymore will only create a limited additional effort.
- We are considering some minor cleanup work in the standard document.
- There are no current plans to release a FMI 2.1 version.
- For importing tools there will be no higher effort to implement this 3.0 standard than the previously intended 2.1 version.
We are certain that FMI 3.0 will be simpler to understand and implement now that we can simplify the FCPs.


## What are the license and usage conditions for the FMI standard?

Access and use of the FMI standard is free of charge. However, vendors may charge for their tools to support the FMI standard, either by exporting FMUs or by importing FMUs.

**To be clear: While the FMI standard is open and free, commercial implementations might not be.**


## How can I join the FMI Mailing Lists?

- The “FMI-Info-Mailing list” is used for public announcements. You can find a registration link on our contact page.
- The “FMI design” Mailing list is used by active developers of FMI (typically members of the FMI Advisory or Steering Committee). If you are interested please contact contact@fmi-standard.org
- The “FMI Steering” Mailing list is used by members of the FMI Steering Committee. To join you need to be a member of the FMI Steering Committee.


## How is FMI related to Modelica?

- Technically FMI is not related to Modelica, and can be seen as a complementary technology.
- The intention of the FMI project is to be neutral with respect to tools, technologies (e.g. solvers, OS, files, systems…) and languages (including Modelica).
- The FMI standard is developed as a Modelica Association Project within the Modelica Association, an organization focused on the “coordinated standardization and development of software technology and methods in the area of cyber physical- systems and systems engineering”, see the Modelica Association Bylaws and the History page


# I'm a modeler and want to use FMI in my simulation tool

## How can I get a first overview on FMI?

Please have a look at the literature page, especially on the overview talks/slides from the 8th, 9th and 10th Modelica Conference

- FMI 1.0: “The Functional Mock-up Interface for Tool independent Exchange of Simulation Models” PDF
- FMI 2.0: “Functional Mock-up Interface 2.0: The Standard for Tool independent Exchange of Simulation Models” PDF
- FMI 2.0: Presentations about new features and applications ZIP


## Does my simulation tool support FMI?

Please see the FMI tools page for a list of tools for that tool vendors have announced their support of FMI.

**While the FMI project defines cross check rules, the tool vendors carry sole responsibility for their stated FMI support and the provided compatibility results.**


## Where can I get help when I have problems related to FMI in my simulation tool?

- Typically an exporting and an importing tool are involved in FMI-based simulation. So if problems occur and if it is not obvious which tool causes the problem, you should communicate the problem to the support team of both involved tools
- As a general discussion forum about FMI, you may use the FMI forum on Stack Overflow


## Is there a tool vendor independent way to access model information during simulation?

ASAM XIL-MA is a standardized API that allows the access of model parameters, stimulations and simulation results and to control simulation experiments as well. Please see the related ASAM XIL-MA section.


# I'm a developer and want to support FMI with my tool

## What and in which order should I read/do to get started with FMI technology?

That depends mostly on your background knowledge. We assume here you already have fundamental knowledge of simulation technology (ODE vs. DAE, zero-crossing, state/time events, derivatives etc.):

- First make a quick pass trough the standard document.
- Then browse and play with the available 3rd party development toolkits.
- Read the implementation hints contained in FMI_for_ModelExchange_v1.0.zip - not yet available for FMI 2.0.
- Re-read the standard document in detail.


## Does FMI 2.0 support Partial Differential Equations (PDEs)?

There are two kinds of FMI variants: Model Exchange and Co-Simulation.

Model-Exchange FMUs encode ODEs. PDE-support is not planned yet, but the demand for it is increasing.

The second kind, Co-Simulation FMUs, can contain any kind of simulation component because it does not expose states. So as long as you want to simply encapsulate PDEs, this could be done.

But explicitly exposing a PDE to a solver using FMUs is currently not supported.


## I added my test FMUs/Cross-Check results but the tools page does not show "green". Why?

The Cross-Check Rules list a number of conditions before turning an entry “green”. In short:

- Exporting tools must provide at least 3 FMUs and at least one importer must report successful import.
- Importing tools must report (and prove) successful import of at least 3 FMUs of at least 3 exporting tools.

Please refer to the complete set of rules and notes.


## Why are the badge-numbers of the platform-drop-down not adding up to the badge-number in the overview?

The platform-drop-down list contains only platforms the tool has passed the Cross-Check Rules. But the overview lists all FMUs or Cross-Check Results submitted.
